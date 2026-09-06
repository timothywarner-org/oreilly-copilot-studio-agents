#requires -Version 7.2
<#
.SYNOPSIS
Creates and verifies the PRIVATE GitHub origin for this single O'Reilly course.
.DESCRIPTION
Uses GitHub CLI's existing authentication, including GITHUB_TOKEN/GH_TOKEN.
Never displays a token, embeds one in a URL, force-pushes, or changes visibility to public.
Run from the installed repository after committing reviewed changes.
.EXAMPLE
.\scripts\Publish-PrivateRepo.ps1
.EXAMPLE
.\scripts\Publish-PrivateRepo.ps1 -ResumeExisting
#>
[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'Medium')]
param(
    [string] $RepositoryPath = (Split-Path -Parent $PSScriptRoot),
    [switch] $ResumeExisting
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $false

function Invoke-Checked {
    param([string] $Command, [string[]] $Arguments)
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Command failed with exit code $LASTEXITCODE. No force or destructive recovery was attempted."
    }
}

function Get-NativeText {
    param([string] $Command, [string[]] $Arguments)
    $lines = @(& $Command @Arguments 2>&1)
    if ($LASTEXITCODE -ne 0) {
        throw "$Command failed with exit code $LASTEXITCODE. Check authentication, permissions, or local Git state."
    }
    return ($lines -join "`n").Trim()
}

function Get-GhJson {
    param([string[]] $Arguments)
    $text = Get-NativeText -Command 'gh' -Arguments $Arguments
    return ($text | ConvertFrom-Json -Depth 50)
}

$root = [IO.Path]::GetFullPath($RepositoryPath)
$metadata = Get-Content -LiteralPath (Join-Path $root 'repo-metadata.json') -Raw | ConvertFrom-Json
$course = Get-Content -LiteralPath (Join-Path $root 'course.json') -Raw | ConvertFrom-Json
if ($metadata.owner -cne 'timothywarner-org' -or $metadata.name -cne 'oreilly-copilot-studio-agents' -or
    $metadata.private -ne $true -or $course.id -cne 'oreilly-copilot-studio-agents-2026-09-08') {
    throw 'Course identity or PRIVATE visibility guard does not match. Stopping.'
}
$fullName = "$($metadata.owner)/$($metadata.name)"
$remoteUrl = "https://github.com/$fullName.git"

if (-not $PSCmdlet.ShouldProcess($fullName, 'Create/configure a PRIVATE repository and push the reviewed local main branch')) {
    return
}
foreach ($command in @('git', 'gh', 'node')) {
    if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
        throw "Required command is missing: $command. Nothing has been published."
    }
}
$gitRoot = Get-NativeText 'git' @('-C', $root, 'rev-parse', '--show-toplevel')
if ([IO.Path]::GetFullPath($gitRoot).TrimEnd([IO.Path]::DirectorySeparatorChar) -ne
    $root.TrimEnd([IO.Path]::DirectorySeparatorChar)) {
    throw 'RepositoryPath is not the actual Git root. Stopping.'
}
$branch = Get-NativeText 'git' @('-C', $root, 'branch', '--show-current')
if ($branch -cne 'main') { throw 'Switch to the reviewed main branch before publishing.' }
$dirty = Get-NativeText 'git' @('-C', $root, 'status', '--porcelain')
if ($dirty) { throw 'Commit or resolve local changes before publishing. The publisher never stages arbitrary files.' }
$localCommit = Get-NativeText 'git' @('-C', $root, 'rev-parse', 'HEAD')
$remoteNames = @(Get-NativeText 'git' @('-C', $root, 'remote'))
$hasOrigin = (($remoteNames -join "`n") -split "`n") -contains 'origin'
if ($hasOrigin) {
    $origin = Get-NativeText 'git' @('-C', $root, 'remote', 'get-url', 'origin')
    if ($origin -cne $remoteUrl) { throw 'Existing origin does not match the expected credential-free HTTPS URL. Stopping.' }
}

Push-Location $root
$oldHost = [Environment]::GetEnvironmentVariable('GH_HOST', 'Process')
$oldPrompt = [Environment]::GetEnvironmentVariable('GH_PROMPT_DISABLED', 'Process')
try {
    # Scope the CLI to the intended host. Authentication is left to gh; tokens are never read or printed here.
    $env:GH_HOST = 'github.com'
    $env:GH_PROMPT_DISABLED = '1'
    Invoke-Checked 'node' @('--test')
    Invoke-Checked 'node' @('scripts/validate-repo.mjs')

    $login = Get-NativeText 'gh' @('api', '--hostname', 'github.com', 'user', '--jq', '.login')
    if ($login -cne 'timothywarner') {
        throw "GitHub CLI is authenticated as '$login', not the intended owner 'timothywarner'. Stopping."
    }
    Write-Host "Authenticated as $login. Credentials have not been displayed."

    $probe = @(& gh api --hostname github.com --include "repos/$fullName" 2>&1)
    $probeExit = $LASTEXITCODE
    $probeText = $probe -join "`n"
    $exists = $probeExit -eq 0
    if (-not $exists -and $probeText -notmatch '(?m)^HTTP/\S+\s+404\b') {
        throw 'Repository existence check failed without a confirmed HTTP 404. No create request was attempted.'
    }

    $receiptPath = Join-Path $root '.local/publish-receipt.json'
    if ($exists) {
        if (-not $ResumeExisting) {
            throw "Repository $fullName already exists. Nothing was overwritten. See docs/github-maintenance.md before using -ResumeExisting."
        }
        $remote = Get-GhJson @('api', '--hostname', 'github.com', "repos/$fullName")
        if (-not $remote.private -or $remote.visibility -cne 'private') {
            throw 'Existing repository is not PRIVATE. Refusing to upload any content.'
        }
        $identityMatches = $false
        if (Test-Path -LiteralPath $receiptPath) {
            $receipt = Get-Content -LiteralPath $receiptPath -Raw | ConvertFrom-Json
            $identityMatches = ($receipt.repositoryId -eq $remote.id -and $receipt.fullName -ceq $fullName -and
                $receipt.courseId -ceq $course.id)
        }
        if (-not $identityMatches) {
            try {
                $existingCourse = Get-GhJson @('api', '--hostname', 'github.com',
                    '-H', 'Accept: application/vnd.github.raw+json', "repos/$fullName/contents/course.json")
                $identityMatches = $existingCourse.id -ceq $course.id
            }
            catch { $identityMatches = $false }
        }
        if (-not $identityMatches) {
            throw 'Cannot establish that the existing private repository belongs to this course. Stopping without changes.'
        }
    }
    else {
        Invoke-Checked 'gh' @('repo', 'create', $fullName, '--private',
            '--description', [string]$metadata.description, '--homepage', [string]$metadata.homepage)
        $remote = Get-GhJson @('api', '--hostname', 'github.com', "repos/$fullName")
        if (-not $remote.private -or $remote.visibility -cne 'private' -or $remote.full_name -cne $fullName) {
            throw 'PRIVATE identity verification failed immediately after creation. No content has been pushed.'
        }
        New-Item -ItemType Directory -Path (Join-Path $root '.local') -Force | Out-Null
        @{
            repositoryId = $remote.id
            fullName = $fullName
            courseId = $course.id
            createdAt = (Get-Date).ToUniversalTime().ToString('o')
        } | ConvertTo-Json | Set-Content -LiteralPath $receiptPath -Encoding utf8
    }

    # The repository was verified private before any local content leaves the machine.
    if (-not $hasOrigin) { Invoke-Checked 'git' @('-C', $root, 'remote', 'add', 'origin', $remoteUrl) }
    $pushArgs = @('-C', $root, '-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential',
        'push', '--set-upstream', 'origin', 'main')
    Invoke-Checked 'git' $pushArgs

    Invoke-Checked 'gh' @('repo', 'edit', $fullName,
        '--description', [string]$metadata.description, '--homepage', [string]$metadata.homepage,
        '--add-topic', ($metadata.topics -join ','), '--default-branch', 'main',
        '--enable-issues=true', '--enable-wiki=false', '--enable-projects=false', '--enable-discussions=false',
        '--enable-squash-merge=true', '--enable-merge-commit=false', '--enable-rebase-merge=false',
        '--delete-branch-on-merge=true')
    foreach ($label in $metadata.labels) {
        Invoke-Checked 'gh' @('label', 'create', [string]$label.name, '--repo', $fullName,
            '--color', [string]$label.color, '--description', [string]$label.description, '--force')
    }

    $tag = [string]$metadata.initialTag
    $tagRefs = Get-NativeText 'git' @('-C', $root, 'tag', '--list', $tag)
    if (-not $tagRefs) {
        Invoke-Checked 'git' @('-C', $root, 'tag', '-a', $tag, '-m', 'Private course scaffold; tenant rehearsal still required.')
    }
    Invoke-Checked 'git' @('-C', $root, '-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential',
        'push', 'origin', "refs/tags/$tag")

    $verified = Get-GhJson @('api', '--hostname', 'github.com', "repos/$fullName")
    $remoteCommit = Get-NativeText 'gh' @('api', '--hostname', 'github.com', "repos/$fullName/commits/main", '--jq', '.sha')
    $topicDifferences = @(Compare-Object -ReferenceObject @($metadata.topics | Sort-Object) -DifferenceObject @($verified.topics | Sort-Object))
    if (-not $verified.private -or $verified.visibility -cne 'private' -or $verified.full_name -cne $fullName -or
        $verified.homepage -cne $metadata.homepage -or $verified.description -cne $metadata.description -or
        $verified.default_branch -cne 'main' -or $topicDifferences.Count -gt 0 -or $remoteCommit -cne $localCommit) {
        throw 'Publication completed partially, but metadata/privacy/commit readback did not match. Inspect the private repository before continuing.'
    }
    New-Item -ItemType Directory -Path (Join-Path $root '.local') -Force | Out-Null
    @{
        url = $verified.html_url
        visibility = $verified.visibility
        repositoryId = $verified.id
        mainCommit = $remoteCommit
        tag = $tag
        verifiedAt = (Get-Date).ToUniversalTime().ToString('o')
        hostedCiVerified = $false
        tenantDeploymentVerified = $false
    } | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $root '.local/publish-result.json') -Encoding utf8
    Write-Host "PRIVATE repository and main commit verified: $($verified.html_url)"
    Write-Host 'About metadata, topics, labels, and scaffold tag are configured. No public release was created.'
    Write-Host 'Next: inspect the actual Actions run, then rehearse the four agent checkpoints.'
}
finally {
    [Environment]::SetEnvironmentVariable('GH_HOST', $oldHost, 'Process')
    [Environment]::SetEnvironmentVariable('GH_PROMPT_DISABLED', $oldPrompt, 'Process')
    Pop-Location
}
