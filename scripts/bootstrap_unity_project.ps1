param(
  [Parameter(Mandatory = $true)]
  [string]$GameName
)

$root = Split-Path -Parent $PSScriptRoot
$localRoot = Join-Path $root "local_projects"
$gameRoot = Join-Path $localRoot $GameName
$unityRoot = Join-Path $gameRoot "UnityProject"
$templateUnity = Join-Path $root "projects/_template/unity_base"

if (-not (Test-Path $gameRoot)) {
  Write-Error "Local game instance not found: $gameRoot"
  Write-Error "Run init_local_project.ps1 first."
  exit 1
}

if (-not (Test-Path $templateUnity)) {
  Write-Error "Unity template not found: $templateUnity"
  exit 1
}

$dirs = @(
  (Join-Path $unityRoot "Assets"),
  (Join-Path $unityRoot "Assets/Scenes"),
  (Join-Path $unityRoot "Assets/Scripts"),
  (Join-Path $unityRoot "Assets/Scripts/Gameplay"),
  (Join-Path $unityRoot "Assets/Scripts/Systems"),
  (Join-Path $unityRoot "Assets/Scripts/UI"),
  (Join-Path $unityRoot "Assets/Scripts/Tools"),
  (Join-Path $unityRoot "Assets/Scripts/Debug"),
  (Join-Path $unityRoot "Assets/ArtPlaceholders"),
  (Join-Path $unityRoot "Assets/Prefabs"),
  (Join-Path $unityRoot "Packages"),
  (Join-Path $unityRoot "ProjectSettings")
)

foreach ($d in $dirs) {
  if (-not (Test-Path $d)) {
    New-Item -ItemType Directory -Path $d -Force | Out-Null
  }
}

Copy-Item -Path (Join-Path $templateUnity "Packages/manifest.json") -Destination (Join-Path $unityRoot "Packages/manifest.json") -Force
Copy-Item -Path (Join-Path $templateUnity "ProjectSettings/ProjectVersion.txt") -Destination (Join-Path $unityRoot "ProjectSettings/ProjectVersion.txt") -Force

$readme = @"
# UnityProject

This Unity project skeleton is generated from the framework template.

## Next Step

1. Open Unity Hub
2. Add this project path:
$unityRoot
3. Open with Unity 2022.3 LTS
"@

Set-Content -Path (Join-Path $unityRoot "README.md") -Value $readme -Encoding UTF8
Write-Output "Bootstrapped Unity project at: $unityRoot"
