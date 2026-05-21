#Requires -Version 5.1
<#
.SYNOPSIS
    PowerShell entry point for the Grey Star terminal assistant.
#>

param(
    [string]$Load = "",
    [string]$SaveDir = "",
    [string]$DataDir = ""
)

$Root = $PSScriptRoot
$Assistant = Join-Path $Root "greystar.py"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python not found. Install Python 3 and try again." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path -LiteralPath $Assistant)) {
    Write-Host "Terminal assistant not found: $Assistant" -ForegroundColor Red
    exit 1
}

$argsList = @($Assistant)
if ($Load) {
    $argsList += @("--load", $Load)
}
if ($SaveDir) {
    $argsList += @("--save-dir", $SaveDir)
}
if ($DataDir) {
    $argsList += @("--data-dir", $DataDir)
}

& python @argsList
exit $LASTEXITCODE
