# Learner package

**No local runtime is needed to take the class.** The package contains the four labs and worksheets, complete walkthroughs for independent practice, worked examples, source notes, the original knowledge files, and the small study-session recipe. A browser and approved Copilot Studio access support the maker route. The observer route uses the same decision exercises.

## Instructor packaging

Run the dependency-free generator from the repository in PowerShell:

```powershell
# A new destination prevents stale or unrelated files entering the learner package.
node scripts/build-learner-package.mjs .local/learner-package
if ($LASTEXITCODE -ne 0) { throw 'Learner package generation failed.' }
Compress-Archive -LiteralPath .local/learner-package -DestinationPath .local/learner-package.zip
```

The destination must not exist. Choose a new destination for a revised build. The generator uses an explicit allowlist, rewrites links to excluded instructor-only references as plain text, and records hashes. It excludes Git history, private correspondence, original proposal links, presenter details, credentials, and local evidence. Newly authored demonstration guides are deliberately included because they support independent practice.

## Before distribution

1. Follow [the export inspection procedure](../sample-agent/exports/README.md) to capture a genuine native topic. Inspect it for identities, secrets, private endpoints and dependency assumptions. This package does not invent an export.
2. Add the reviewed native capture to the package using your approved distribution workflow. Recheck the final archive and update its artifact inventory. Until then, the generator marks the promised native sample **MISSING** in PACKAGE-STATUS.md.
3. Confirm the learner-resource URL with the producer and open it with attendee-equivalent access. The private GitHub URL is not the distribution route.
4. Complete tenant rehearsal separately. The package is teaching material, not an importable complete agent or proof of a live deployment.

The generated ZIP is a local preparation output. Building it does not publish, send, or share anything.
