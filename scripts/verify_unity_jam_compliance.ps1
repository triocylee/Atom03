param(
  [Parameter(Mandatory = $true)]
  [string]$GameName
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$unityRoot = Join-Path $root ("local_projects\" + $GameName + "\UnityProject")

if (-not (Test-Path $unityRoot)) {
  Write-Error "Unity project not found: $unityRoot"
  exit 1
}

$manifestPath = Join-Path $unityRoot "Packages\manifest.json"
$graphicsPath = Join-Path $unityRoot "ProjectSettings\GraphicsSettings.asset"
$qualityPath = Join-Path $unityRoot "ProjectSettings\QualitySettings.asset"

$checks = @()

function Add-Check {
  param(
    [string]$Name,
    [bool]$Passed,
    [string]$Detail
  )
  $script:checks += [PSCustomObject]@{
    Check  = $Name
    Passed = $Passed
    Detail = $Detail
  }
}

# 1) Required files
Add-Check -Name "Manifest exists" -Passed (Test-Path $manifestPath) -Detail $manifestPath
Add-Check -Name "GraphicsSettings exists" -Passed (Test-Path $graphicsPath) -Detail $graphicsPath
Add-Check -Name "QualitySettings exists" -Passed (Test-Path $qualityPath) -Detail $qualityPath

if (Test-Path $manifestPath) {
  $manifestRaw = Get-Content $manifestPath -Raw
  $hasSrpPkg = ($manifestRaw -match "com\.unity\.render-pipelines")
  Add-Check -Name "No SRP package in manifest" -Passed (-not $hasSrpPkg) -Detail "com.unity.render-pipelines.* should be absent"
}

if (Test-Path $graphicsPath) {
  $graphicsRaw = Get-Content $graphicsPath -Raw
  $graphicsBuiltin = ($graphicsRaw -match "m_CustomRenderPipeline:\s*\{fileID:\s*0\}")
  Add-Check -Name "Graphics uses Built-in pipeline" -Passed $graphicsBuiltin -Detail "m_CustomRenderPipeline must be fileID: 0"
}

if (Test-Path $qualityPath) {
  $qualityRaw = Get-Content $qualityPath -Raw
  $matches = [regex]::Matches($qualityRaw, "customRenderPipeline:\s*\{fileID:\s*0\}")
  $count = $matches.Count
  $anyNonBuiltin = ($qualityRaw -match "customRenderPipeline:\s*\{fileID:\s*(?!0)\d+")
  Add-Check -Name "Quality levels use Built-in pipeline" -Passed (($count -gt 0) -and (-not $anyNonBuiltin)) -Detail "all quality customRenderPipeline should be fileID: 0"
}

# 2) Required folder skeleton
$requiredDirs = @(
  "Assets\Scenes",
  "Assets\Scripts\Gameplay",
  "Assets\Scripts\Systems",
  "Assets\Scripts\UI",
  "Assets\Scripts\Tools",
  "Assets\Scripts\Debug",
  "Assets\ArtPlaceholders",
  "Assets\Prefabs"
)

foreach ($d in $requiredDirs) {
  $full = Join-Path $unityRoot $d
  Add-Check -Name ("Dir exists: " + $d) -Passed (Test-Path $full) -Detail $full
}

$failed = $checks | Where-Object { -not $_.Passed }
$reportPath = Join-Path $unityRoot "JAM_COMPLIANCE_REPORT.md"

$lines = @()
$lines += "# Jam Compliance Report"
$lines += ""
$lines += ("GameName: " + $GameName)
$lines += ("UnityProject: " + $unityRoot)
$lines += ("Generated: " + (Get-Date -Format "yyyy-MM-dd HH:mm:ss"))
$lines += ""
$lines += "| Check | Passed | Detail |"
$lines += "|---|---|---|"
foreach ($c in $checks) {
  $ok = if ($c.Passed) { "YES" } else { "NO" }
  $lines += ("| " + $c.Check + " | " + $ok + " | " + $c.Detail + " |")
}
$lines += ""
$lines += ("Result: " + $(if ($failed.Count -eq 0) { "PASS" } else { "FAIL" }))

Set-Content -Path $reportPath -Value $lines -Encoding UTF8

$checks | Format-Table -AutoSize
Write-Output ("REPORT: " + $reportPath)

if ($failed.Count -gt 0) {
  exit 2
}

exit 0
