<#
.SYNOPSIS
Refresh the AI-901 objective-domain knowledge using MarkItDown and Microsoft Learn.
.DESCRIPTION
Converts official HTML, preserves the complete Skills measured section, and records provenance.
Navigation and exam administration are excluded so the upload has one clear purpose.
.EXAMPLE
pwsh -File ./contoso-ai901-agent/scripts/Update-AI901Knowledge.ps1
#>
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
try {
    $agentRoot = Split-Path $PSScriptRoot -Parent
    $repoRoot = Split-Path $agentRoot -Parent
    $sourceUrl = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901'
    $workPath = Join-Path $repoRoot '.local/ai901-authoring'
    $sourcePath = Join-Path $workPath 'ai-901.html'
    $convertedPath = Join-Path $workPath 'ai-901.markitdown.md'
    $outputPath = Join-Path $agentRoot 'knowledge/ai901-objective-domain.md'
    $provenancePath = Join-Path $agentRoot 'sources/ai901-objective-domain.provenance.json'
    $converter = Get-Command markitdown -ErrorAction Stop
    New-Item -ItemType Directory -Force -Path $workPath, (Split-Path $provenancePath) | Out-Null
    Invoke-WebRequest -Uri $sourceUrl -OutFile $sourcePath
    $retrievedAt = [DateTimeOffset]::UtcNow.ToString('o')
    & $converter.Source $sourcePath -o $convertedPath
    if ($LASTEXITCODE -ne 0) { throw 'MarkItDown conversion failed; existing knowledge was not replaced.' }
    $converterVersion = (& $converter.Source --version | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) { throw 'Could not record the MarkItDown version.' }
    $converted = (Get-Content -LiteralPath $convertedPath -Raw).Replace("`r`n", "`n")
    $html = Get-Content -LiteralPath $sourcePath -Raw
    $section = [regex]::Match($converted, '(?ms)^## Skills measured[^\n]*\n.*?(?=^## Study resources\s*$)')
    if (-not $section.Success) { throw 'The study-guide section boundaries changed. Review before refreshing.' }
    $objectiveText = $section.Value.TrimEnd()
    $domains = [regex]::Matches($objectiveText, '(?m)^### .+\([0-9]+[–-][0-9]+%\)$')
    $groups = [regex]::Matches($objectiveText, '(?m)^#### .+$')
    $skillsHeading = ($objectiveText -split "`n")[0] -replace '^## ', ''
    if ($domains.Count -eq 0 -or $groups.Count -eq 0) { throw 'No domains or objective groups found.' }
    # The visible date and HTML metadata are different source fields; preserve both honestly.
    $visibleDate = [regex]::Match($converted, '(?s)Last updated on\s+(\d{4}-\d{2}-\d{2})').Groups[1].Value
    $updatedAt = [regex]::Match($html, '<meta name="updated_at" content="([^"]+)"').Groups[1].Value
    $preface = @"
# AI-901 objective domain - Microsoft Learn snapshot

**Authority:** Microsoft Learn, Study guide for Exam AI-901: Microsoft Azure AI Fundamentals.
**Source:** $sourceUrl
**Retrieved (UTC):** $retrievedAt
**Source scope:** $skillsHeading.
**Conversion:** $converterVersion, official HTML to Markdown; complete Skills measured section retained.

## How to use this source

This file contains the official exam audience profile, domain weights, and every objective bullet in
the source's Skills measured section. The Microsoft text below is preserved from the MarkItDown
conversion. This introduction is course-authored metadata.

Use this dated snapshot for AI-901 scope and objective questions. It does not contain actual exam
items, an exhaustive teaching text, exam booking information, or Contoso reward rules. Check the live
Microsoft Learn guide for changes before claiming these are current exam requirements.
The exam candidate's Python prerequisites do not make this Copilot Studio workshop a code-along.

---

"@
    Set-Content -LiteralPath $outputPath -Value ($preface + "`n" + $objectiveText + "`n") -Encoding utf8NoBOM -NoNewline
    [ordered]@{
        sourceUrl = $sourceUrl
        retrievedAtUtc = $retrievedAt
        sourceVisibleUpdatedDate = $visibleDate
        sourceHtmlUpdatedAt = $updatedAt
        converter = $converterVersion
        transformation = 'HTML -> MarkItDown -> complete Skills measured section, with course-authored provenance preface. Source wording and order preserved.'
        skillsHeading = $skillsHeading
        weightedDomains = @($domains | ForEach-Object { $_.Value -replace '^### ', '' })
        objectiveGroupCount = $groups.Count
        sourceHtmlSha256 = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash.ToLowerInvariant()
        fullConversionSha256 = (Get-FileHash -LiteralPath $convertedPath -Algorithm SHA256).Hash.ToLowerInvariant()
        knowledgeFile = 'contoso-ai901-agent/knowledge/ai901-objective-domain.md'
        knowledgeSha256 = (Get-FileHash -LiteralPath $outputPath -Algorithm SHA256).Hash.ToLowerInvariant()
        tenantUpload = 'NOT RUN'
        tenantRetrieval = 'NOT RUN'
    } | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $provenancePath -Encoding utf8NoBOM
    Write-Output "Created knowledge with $($domains.Count) weighted domains and $($groups.Count) objective groups."
} catch {
    Write-Error "AI-901 knowledge refresh failed: $($_.Exception.Message)"
    exit 1
}
