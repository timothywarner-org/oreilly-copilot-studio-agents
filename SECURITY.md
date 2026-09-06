# Security

Do not post tokens, tenant identifiers, learner records, presenter links, or private transcripts in issues.
For a sensitive report, contact the owner through an existing trusted private channel.
Do not manufacture a public issue to test disclosure.

Use a nonproduction environment and least-privilege identities. Review every tool’s data access and side
effects. The local reference demo has no network calls or credentials.

`GITHUB_TOKEN` or `GH_TOKEN` may be consumed by GitHub CLI at publication time. Neither is printed,
placed in a remote URL, or written to a repository file by these scripts.
If a secret is exposed, revoke/rotate it; deleting a working-tree file does not erase Git history.

CI receives read-only contents permission. Action revisions are pinned. No deployment or public-publish
workflow is included. Branch/ruleset protection remains an explicit owner administration decision.
