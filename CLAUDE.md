# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A **course teaching kit** for one O'Reilly live session, "Build AI Agents to Automate Your Workflows"
(Tim Warner, September 8, 2026). The deliverable is **prose plus machine-readable contracts**, not an
application. Learners build an **AZ-900 Cert-Prep Assistant** in **Microsoft Copilot Studio** by hand
through the portal; the Node.js code here exists only to keep the written materials internally
consistent and to package them for distribution.

Two consequences shape almost every task:

- The **learner route stays no-code**. Node.js and PowerShell are optional instructor tooling. Never
  introduce a coding prerequisite into a module, lab, or worksheet.
- **No agent has ever been deployed or tested from this repo.** Evaluation results ship as `NOT RUN`
  and the validator enforces that. Never fabricate tenant observations, portal behavior, or deployable
  Copilot Studio YAML.

Read `AGENTS.md` before editing. It is the working agreement and is intentionally short.

## Commands

Requires **Node.js 22 or newer**. Zero third-party npm packages, by design and by assertion in the
validator.

| Command | What it does |
| --- | --- |
| `npm test` | Runs `node --test` over `tests/`. 28 tests, includes a full validator run. |
| `npm run validate` | Cross-file integrity checks. The primary gate; see below. |
| `npm run demo:plan` | Runs the optional deterministic study-plan reference function locally. |
| `npm run eval:template` | Copies the `NOT RUN` eval template to `.local/agent-results.json`. Refuses to overwrite. |
| `node --test tests/study-plan.test.mjs` | Single test file. |
| `node --test --test-name-pattern="safe relative"` | Single test by name. |
| `node scripts/build-learner-package.mjs <new-dir>` | Builds the allowlisted learner folder. Fails if the directory exists. |
| `.\scripts\Publish-PrivateRepo.ps1` | PowerShell 7.2+. Creates and verifies the **private** GitHub origin via `gh`. |

CI (`.github/workflows/validate.yml`) runs exactly `npm test` then `npm run validate` on Node 22.

`instructor/build-presentation.mjs` will **not** run in a normal checkout. It needs the `@oai/artifact-tool`
runtime plus `PRESENTATION_SKILL_DIR`, `ARTIFACT_RUNTIME_PYTHON`, and `RUNTIME_NODE_MODULES`. PPTX output
is gitignored.

## Architecture: the invariant web

There is no app graph to learn. What matters is which files must agree with which other files, because
`scripts/validate-repo.mjs` fails the build when they drift. Editing one file in isolation is the most
common way to break this repo.

**`course.json` is the spine.** It defines the four objectives (LO1-LO4), the four modules, and the
timing. From it, the validator requires:

- Each objective's `text` appears **verbatim** in `sources/proposal-curriculum.md`. The proposal is the
  contractual source; do not reword an objective to improve it.
- Exactly four modules with ids `01-inception`, `02-build`, `03-extend`, `04-operate`, each holding
  `README.md`, `lab.md`, and `worksheet.md`.
- Per module, `instructionAndPracticeMinutes + breakMinutes == scheduledMinutes`, and the modules plus
  `wrapUpMinutes` total **240**. That number is the advertised public schedule.
- Each `instructor/<module-id>-guide.md` contains its module's first objective text verbatim.
- `codingRequiredForLearners` stays `false`.

**Traceability chain.** `curriculum/alignment.json` maps each objective to a module path, a learner
artifact file, and evaluation case ids. `evals/cases.json` holds exactly **12** unique cases, each
bound to a real objective id. `evals/results.template.json` must mirror all 12 with
`status: "NOT RUN"`, `observedResponse: null`, `evidence: null`, and `agentTested: false`. Adding a
case means touching all three files.

**Two study-plan artifacts that are easy to confuse.** They are deliberately different:

| Artifact | Role | Shape |
| --- | --- | --- |
| `sample-agent/tools/core-study-session.json` plus `.md` | **GetStudySession**, the tool learners actually build in Copilot Studio | One focus from `cloud`, `security`, `governance`; fixed 30-minute output |
| `src/study-plan.mjs` | Optional advanced Node reference, never required in class | `days`, `minutesPerDay`, `focus[]` with different focus codes |

The validator asserts that every plan string in `core-study-session.json` also appears in
`core-study-session.md`, so the contract and the paste-ready recipe cannot diverge. Do not "unify" the
two artifacts; the split is pedagogical.

**Distribution boundary.** `learner/package-files.json` is a 40-entry allowlist. `build-learner-package.mjs`
refuses traversal, symlinks, and `.git`/`.local`/`.private`/`.env` paths, rewrites Markdown links whose
targets are not in the allowlist into "(instructor reference, not included)", and blocks any file
containing a Google Docs proposal URL, a presenter link, a token pattern, or a private key. It emits
`package-manifest.json` with `nativeYamlIncluded: false` and `tenantExecuted: false`. Adding a file to
the allowlist without checking its outbound links produces a degraded learner package rather than an error.

**Safety scan.** The validator sweeps all text files for GitHub token formats, private keys,
credential-bearing remote URLs, presenter links, and a personal postal address, and it asserts that no
`.local/`, `.private/`, or `.env` file is git-tracked. It is not a general secret scanner; treat it as a
tripwire, not a guarantee.

## Content conventions

- **Sources are ranked and separated.** `sources/README.md` is the register. Microsoft Learn, not the
  predecessor `agents-pro` repository, is the authority for product behavior. Keep source text,
  newly authored activities, product documentation, and actual tenant observations distinguishable in
  prose. Re-verify volatile product facts against Microsoft Learn rather than from memory.
- **Status language is textual, never color-coded.** Use `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`. Keep
  expected behavior and observed behavior in separate columns or sentences.
- **Synthetic examples must be labelled as synthetic.** `evals/native-live-three.csv` and
  `evals/native-tool-one.csv` contain authored reference responses that have not been imported or run.
- `docs/known-gaps.md` is the live gate list. When a tenant, rehearsal, or distribution check closes,
  update it there rather than softening the caveats scattered through `README.md` and `START-HERE.md`.
- `docs/course-delta.md` records what changed from the predecessor course and the discrepancies between
  the approved proposal and the published registration page. Do not silently resolve those.

## Hard boundaries

1. **Never make this repository public.** `private: true` is asserted in both `package.json` and
   `repo-metadata.json`, and the license stays `UNLICENSED`. Publication needs Tim's explicit approval
   plus a rights and privacy review (`RIGHTS.md`, `docs/github-maintenance.md`).
2. **Never add an npm dependency.** The validator fails on any `dependencies` or `devDependencies` key.
   If one is truly needed, justify why zero-dependency tooling is insufficient before adding it.
3. **Do not broaden scope.** One course, one scenario, four objectives. `course.json.scopeExclusions`
   lists what stays out, including the separate MCP course and any Foundry SDK material.
4. No AWS. No credentials, learner records, private correspondence, contracts, or presenter URLs.
5. Report what actually ran. Keep executed local checks separate from unperformed tenant, Windows, and
   GitHub operations. Readiness is evidenced, never inferred from file count.

## Copilot Studio work

This repo intentionally contains **no `.mcs.yml` files**. If a task ever produces or edits Copilot Studio
YAML here, route it through the `copilot-studio:author`, `copilot-studio:test`, or
`copilot-studio:troubleshoot` sub-agents, and confirm the artifact is a genuine capture rather than an
invented export before committing it.
