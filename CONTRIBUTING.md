# Contributing during private preparation

Keep changes within this O’Reilly course’s four objectives.

1. Identify the learning objective and the authoritative source for the change.
2. Edit the relevant module, agent design, or test case rather than adding a parallel curriculum.
3. Run `npm test` and `npm run validate` using Node.js 22 or newer.
4. Inspect the diff for private data, unsupported claims, broken paths, and accidental audience changes.
5. Submit a focused pull request with actual test results. Mark tenant checks NOT RUN when appropriate.

Use plain language and textual statuses. Never rely on color alone. Keep the no-code learner route intact.
Do not add a dependency without explaining why the existing zero-dependency tooling is insufficient.
Public release, license changes, and new external integrations require explicit owner approval.
