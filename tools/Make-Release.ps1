param(
    [string]$OutputDir = "",
    [string]$Version = ""
)

$ErrorActionPreference = "Stop"

$Root = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")
if (-not $OutputDir) {
    $OutputDir = Join-Path $Root "dist"
}
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$insideWorkTree = git -C $Root rev-parse --is-inside-work-tree
if ($insideWorkTree -ne "true") {
    throw "This script must be run inside the Grey Star git repository."
}

if (-not $Version) {
    $Version = (git -C $Root rev-parse --short HEAD).Trim()
}

$trackedBookFiles = @(git -C $Root ls-files "books/gs")
if ($trackedBookFiles.Count -gt 0) {
    throw "Project Aon book files are tracked under books/gs. Remove them from git before packaging."
}

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$zipName = "GreyStar_ActionAssistant-$Version-$stamp.zip"
$zipPath = Join-Path $OutputDir $zipName

if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}

git -C $Root archive --format=zip --output $zipPath HEAD

Write-Host "Created release package:"
Write-Host $zipPath
