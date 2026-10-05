param(
    [Parameter(Mandatory=$true)]
    [string]$PrivateRepo,

    [Parameter(Mandatory=$true)]
    [string]$PublicRepo
)

$ErrorActionPreference = "Stop"

$manifest = Join-Path $PublicRepo "PUBLIC_RELEASE_MANIFEST.txt"
if (!(Test-Path $manifest)) {
    throw "Manifest not found: $manifest"
}

$privateRoot = (Resolve-Path $PrivateRepo).Path
$publicRoot  = (Resolve-Path $PublicRepo).Path

Write-Host "Private source:" $privateRoot
Write-Host "Public target :" $publicRoot
Write-Host ""

$paths = Get-Content $manifest |
    Where-Object { $_ -and -not $_.Trim().StartsWith("#") }

$copied = 0

foreach ($rel in $paths) {
    $rel = $rel.Trim()
    if (!$rel) { continue }

    $src = Join-Path $privateRoot $rel
    $dst = Join-Path $publicRoot  $rel

    if (!(Test-Path $src)) {
        throw "Whitelisted source file is missing: $rel"
    }

    $dstDir = Split-Path $dst -Parent
    if (!(Test-Path $dstDir)) {
        New-Item -ItemType Directory -Force -Path $dstDir | Out-Null
    }

    Copy-Item -Force $src $dst
    $copied += 1
    Write-Host "[COPY]" $rel
}

Write-Host ""
Write-Host "Copied $copied whitelisted files."
Write-Host "No non-whitelisted file was copied."

# Safety check: flag common secret-like filenames if any somehow appeared.
$bad = Get-ChildItem -Path $publicRoot -Recurse -File |
    Where-Object {
        $_.Name -match '(?i)(\.env$|secret|token|credential|private[_-]?key|id_rsa|\.pem$|\.p12$)'
    }

if ($bad) {
    Write-Host ""
    Write-Host "WARNING: suspicious filenames found in public tree:" -ForegroundColor Red
    $bad | ForEach-Object { Write-Host $_.FullName -ForegroundColor Red }
    throw "Aborting before commit. Inspect suspicious files."
}

Write-Host ""
Write-Host "Whitelist sync completed safely." -ForegroundColor Green
Write-Host "Next commands:"
Write-Host "  cd `"$publicRoot`""
Write-Host "  git status"
Write-Host "  git add ."
Write-Host "  git commit -m `"Publish curated PIFI-3D reproducibility snapshot v0.5`""
Write-Host "  git push origin main"
