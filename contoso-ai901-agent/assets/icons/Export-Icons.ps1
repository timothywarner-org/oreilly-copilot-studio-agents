<#
.SYNOPSIS
Export the generated Contoso artwork as exact-size Copilot Studio and Teams/Microsoft 365 icons.
.DESCRIPTION
Normalizes the generated flat-color art, preserves its silhouette, and exports the required
192-pixel color and 32-pixel transparent outline files. The user authorized ImageMagick finishing.
.EXAMPLE
pwsh -File ./contoso-ai901-agent/assets/icons/Export-Icons.ps1
#>
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
try {
    $magick = (Get-Command magick -ErrorAction Stop).Source
    $iconRoot = $PSScriptRoot
    $repoRoot = Split-Path (Split-Path (Split-Path $iconRoot -Parent) -Parent) -Parent
    $workPath = Join-Path $repoRoot '.local/ai901-icons'
    New-Item -ItemType Directory -Force -Path $workPath | Out-Null
    $master = Join-Path $iconRoot 'source/color-master.png'
    $palette = Join-Path $workPath 'palette.png'
    $normalized = Join-Path $workPath 'normalized.png'
    $mark = Join-Path $workPath 'mark.png'
    $storeMark = Join-Path $workPath 'store-mark.png'
    $outlineMark = Join-Path $workPath 'outline-mark.png'
    $colorOutput = Join-Path $iconRoot 'color.png'
    $agentOutput = Join-Path $iconRoot 'agent-icon.png'
    $outlineOutput = Join-Path $iconRoot 'outline.png'

    # Remove generated texture so the flat background and the two symbol colors are exact.
    & $magick -size 1x1 'xc:#10243A' 'xc:#FFFFFF' 'xc:#F6B51B' +append $palette
    if ($LASTEXITCODE -ne 0) { throw 'Palette creation failed.' }
    & $magick $master -colorspace sRGB +dither -remap $palette $normalized
    if ($LASTEXITCODE -ne 0) { throw 'Artwork normalization failed.' }
    & $magick $normalized -transparent '#10243A' -trim +repage $mark
    if ($LASTEXITCODE -ne 0) { throw 'Symbol extraction failed.' }

    # Reserve a little antialiasing room inside Microsoft's 120-pixel store safe area.
    & $magick $mark -filter Lanczos -resize 116x116 $storeMark
    if ($LASTEXITCODE -ne 0) { throw 'Color symbol resize failed.' }
    & $magick -size 192x192 'xc:#10243A' $storeMark -gravity center -compose Over -composite -alpha off -strip -depth 8 -define png:color-type=2 $colorOutput
    if ($LASTEXITCODE -ne 0) { throw 'Color export failed.' }
    Copy-Item -LiteralPath $colorOutput -Destination $agentOutput -Force

    # Build alpha from the selected artwork, never from a painted checkerboard.
    & $magick $mark -channel RGB -fill white -colorize 100 +channel -filter Lanczos -resize 32x32 $outlineMark
    if ($LASTEXITCODE -ne 0) { throw 'Outline resize failed.' }
    & $magick -size 32x32 xc:none $outlineMark -gravity center -compose Over -composite -channel RGB -fill white -colorize 100 +channel -strip -depth 8 -define png:color-type=6 $outlineOutput
    if ($LASTEXITCODE -ne 0) { throw 'Outline export failed.' }

    # Show the white alpha glyph on a preview-only background; that background is not in outline.png.
    & $magick $outlineOutput -background '#10243A' -alpha remove -alpha off -filter point -resize 192x192 (Join-Path $workPath 'outline-preview.png')
    if ($LASTEXITCODE -ne 0) { throw 'Preview export failed.' }
    & $magick $colorOutput (Join-Path $workPath 'outline-preview.png') +append (Join-Path $iconRoot 'preview.png')
    if ($LASTEXITCODE -ne 0) { throw 'Preview assembly failed.' }
    & $magick identify -format '%f: %wx%h %[channels] opaque=%[opaque] bytes=%b\n' $agentOutput $colorOutput $outlineOutput
    if ($LASTEXITCODE -ne 0) { throw 'Export inspection failed.' }
} catch {
    Write-Error "Icon export failed: $($_.Exception.Message)"
    exit 1
}
