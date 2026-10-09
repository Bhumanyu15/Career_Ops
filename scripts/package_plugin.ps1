param(
  [string]$Output = "dist/career-ops-plugin.zip"
)

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) {
  Write-Error "python is required for packaging helper"
  exit 1
}

python "$RepoRoot/scripts/package_plugin.py" --output $Output
