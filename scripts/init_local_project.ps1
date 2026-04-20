param(
  [Parameter(Mandatory = $true)]
  [string]$GameName
)

$root = Split-Path -Parent $PSScriptRoot
$template = Join-Path $root "projects/_template"
$targetRoot = Join-Path $root "local_projects"
$target = Join-Path $targetRoot $GameName

if (-not (Test-Path $template)) {
  Write-Error "Template not found: $template"
  exit 1
}

if (-not (Test-Path $targetRoot)) {
  New-Item -ItemType Directory -Path $targetRoot | Out-Null
}

if (Test-Path $target) {
  Write-Error "Target already exists: $target"
  exit 1
}

Copy-Item -Path $template -Destination $target -Recurse -Force
Write-Output "Initialized local project: $target"
