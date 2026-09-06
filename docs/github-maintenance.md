# GitHub metadata and maintenance

The intended repository is **timothywarner-org/oreilly-copilot-studio-agents**, with default branch **main** and **PRIVATE** visibility.
The [metadata file](../repo-metadata.json) is the source for its description, homepage, topics, initial
scaffold tag, and labels. The homepage is the actual course advertisement, not a presenter link.

## Publication behavior

`Publish-PrivateRepo.ps1` consumes existing GitHub CLI authentication. The CLI supports `GH_TOKEN`
and `GITHUB_TOKEN`; its documented precedence is GH_TOKEN first, then GITHUB_TOKEN, then stored credentials.
The script never requests a token pasted into chat or inserts a token into Git configuration.

It verifies the authenticated login, creates a private repository, verifies visibility **before pushing**,
applies About metadata and labels, enables issues and squash merging, disables unused wiki/projects/
discussions and other merge methods, pushes main, and creates the scaffold tag.
It then reads back repository identity, visibility, homepage, description, topics, and the main commit.
It does not publish a release, enable Pages, or change visibility to public.

A collision stops the first run. Resume is allowed only for a private repo with a matching local
creation receipt or matching course identity, plus an explicit `-ResumeExisting` switch.
There is no force push and no destructive overwrite of an existing local course directory.

## Review and security

CODEOWNERS identifies Tim for review. **CODEOWNERS alone does not enforce review.**
Rulesets/branch protection and org-specific security features are not enabled automatically;
confirm plan support and a usable owner workflow before requiring them on a private repo.

CI is read-only, uses pinned action revisions, and has no deployment job.
Dependabot proposes GitHub Actions updates. A workflow file’s existence is not a passing workflow run.

## Learner distribution and visual polish

Use the clear course title, linked module table, source map, and About fields for discovery.
No invented short URL, publisher logo, fake CI badge, or fabricated social-proof metric is included.
A social preview image is optional and must use cleared artwork.

Keep the origin private until Tim explicitly approves otherwise. Before learner distribution,
review the history and create an approved learner package or grant appropriate access.
The current public page says the resource link is still to come; do not send attendees an inaccessible link.

## References

- https://cli.github.com/manual/gh_repo_create
- https://cli.github.com/manual/gh_repo_edit
- https://cli.github.com/manual/gh_help_environment
- https://docs.github.com/en/actions/reference/security/secure-use
