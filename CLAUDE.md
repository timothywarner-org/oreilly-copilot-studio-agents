# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A **course teaching kit** for one O'Reilly live session, "Build AI Agents to Automate Your Workflows"
(Tim Warner, September 8, 2026). The deliverable is **prose plus machine-readable contracts**, not an
application. The instructor builds an agent by hand in the **Microsoft Copilot Studio** portal while
attendees predict, trace, and evaluate; the Node.js code here exists only to keep the written materials
internally consistent and to package them for distribution.

Three consequences shape almost every task:

- **Delivery is instructor-led.** `docs/pedagogy-revision.md` (2026-09-06) is authoritative and replaced
  the earlier maker-time design. No attendee needs a tenant, an account, or build time during class.
  Full authoring recipes are optional after-class practice. Never reintroduce mandatory learner build time.
- **The learner route stays no-code.** Node.js and PowerShell are optional instructor tooling. Never
  introduce a coding prerequisite into a module, lab, or worksheet, and leave
  `course.json.codingRequiredForLearners` set to `false`.
- **No agent has ever been deployed or tested from this repo.** Evaluation results ship as `NOT RUN` and
  the validator enforces that. Never fabricate tenant observations, portal behavior, or deployable
  Copilot Studio YAML.

Read `AGENTS.md` before editing. It is the working agreement and is intentionally short.

## Commands

Requires **Node.js 22 or newer**. Zero third-party npm packages, by design and by assertion in the
validator.

| Command | What it does |
| --- | --- |
| `npm test` | `node --test` with auto-discovery. 28 tests, includes a full validator run. |
| `npm run validate` | Cross-file integrity checks. The primary gate; see below. |
| `npm run demo:plan` | Runs the optional deterministic study-plan reference function locally. |
| `npm run eval:template` | Copies the `NOT RUN` eval template to `.local/agent-results.json`. Refuses to overwrite. |
| `node --test tests/study-plan.test.mjs` | Single test file. |
| `node --test --test-name-pattern="safe relative"` | Single test by name. |
| `node scripts/build-learner-package.mjs <new-dir>` | Builds the allowlisted learner folder. Fails if the directory exists. |
| `.\scripts\Publish-PrivateRepo.ps1` | PowerShell 7.2+. Creates and verifies the **private** GitHub origin via `gh`. |

CI (`.github/workflows/validate.yml`) runs exactly `npm test` then `npm run validate` on Node 22, with
action SHAs pinned and `persist-credentials: false`.

`instructor/build-presentation.mjs` will **not** run in a normal checkout. It needs the `@oai/artifact-tool`
runtime plus `PRESENTATION_SKILL_DIR`, `ARTIFACT_RUNTIME_PYTHON`, and `RUNTIME_NODE_MODULES`. PPTX output
is gitignored.

## One agent kit, and one deliberate wording gap

`contoso-ai901-agent/` is the **only** agent kit. The predecessor `sample-agent/` AZ-900 kit was retired
on September 7, 2026; its still-useful pieces (`exports/README.md`, `tools/extension-decisions.md`,
`tools/flow-design.md`, `tools/study-plan-contract.json`, `tools/example-input.json`) moved into the
AI-901 kit and the rest was superseded. Do not resurrect it or add a second kit.

**AI-900 retired June 30, 2026.** AI-901 replaced it under the same certification name, *Microsoft
Certified: Azure AI Fundamentals*, with two skill areas instead of five.

**The wording gap is intentional and must survive your edits.** Objective LO2 reads *"Build a grounded
AZ-900 study assistant..."* while the delivered build is AI-901. That string is quoted verbatim in three
places that must agree: `course.json`, `sources/proposal-curriculum.md`, and
`instructor/02-build-guide.md`. The validator asserts all three.

`sources/proposal-curriculum.md` is a **verbatim quotation of the approved O'Reilly proposal**, retrieved
as a real Google Drive export. Rewriting it to say AI-901 would falsify a record of an external
contractual document and would make the validator pass by concealing the very difference this repository
exists to surface. Do not do it, and do not "fix" LO2 in `course.json` either, because the two must match.
`contoso-ai901-agent/STATUS.md` holds the two live options; narrating the difference in Hour One is the
recommended close for the September 8 delivery.

Everything else in the repository says AI-901. If you find a stray AZ-900 outside those three quoted
locations and the documents that explain the gap, it is a miss and should be converted.

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
| `contoso-ai901-agent/tools/get-study-session.json` plus `.md` | **GetStudySession**, the tool built live in Copilot Studio | One focus from `responsible-ai`, `workloads`, `foundry`; fixed 30-minute output |
| `src/study-plan.mjs` | Optional advanced Node reference, never required in class | `days`, `minutesPerDay`, `focus[]` from `ai-concepts`, `ai-workloads`, `foundry-solutions` |

The validator asserts the tool name, the 30-minute session, those exact three focus values, and that
every plan string in `get-study-session.json` also appears in `get-study-session.md`, so the contract and
the paste-ready recipe cannot diverge. Do not "unify" the two artifacts; the split is pedagogical. The
three focus labels are Contoso teaching shortcuts, not official AI-901 skill-area names, and the kit says
so in `knowledge/contoso-enablement-policy.txt`.

**Slides.** `instructor/teaching-slides.json` is a 35-slide manuscript and the only versioned slide
source; every slide needs a title, lines, and notes. `docs/presentation-coverage.md` maps objectives to
exact slide numbers, so inserting a slide renumbers that table. Binary `.pptx` stays out of Git.

**Distribution boundary.** `learner/package-files.json` is a 40-entry allowlist and every entry must
exist on disk or the validator fails. `build-learner-package.mjs` refuses traversal, symlinks, and
`.git`/`.local`/`.private`/`.env` paths, rewrites Markdown links whose targets are not in the allowlist
into "(instructor reference, not included)", and blocks any file containing a Google Docs proposal URL, a
presenter link, a token pattern, or a private key. It emits `package-manifest.json` with
`nativeYamlIncluded: false` and `tenantExecuted: false`. Adding a file to the allowlist without checking
its outbound links produces a degraded learner package rather than an error.

**Safety scan.** The validator sweeps all text files for GitHub token formats, private keys,
credential-bearing remote URLs, presenter links, and a personal postal address, and it asserts that no
`.local/`, `.private/`, or `.env` file is git-tracked. It is not a general secret scanner; treat it as a
tripwire, not a guarantee.

**A local pass is not a CI pass.** The validator walks the working tree, so a Markdown link pointing at
an untracked file resolves locally and then breaks in CI after checkout. Run `git status` before
trusting a green local run, especially when another session has been writing in this repo.

## Which document wins

The prose is layered, and the layers disagree on purpose. Resolve conflicts in this order:

| Question | Authority |
| --- | --- |
| Objective wording, module count, timing | `course.json`, backed verbatim by `sources/proposal-curriculum.md` |
| Delivery format and minute-by-minute pedagogy | `docs/pedagogy-revision.md`, then `docs/teaching-design.md` |
| What is still unproven before delivery | `docs/known-gaps.md`, then `instructor/rehearsal-record.md` |
| Proposal versus published-page differences | `docs/course-delta.md#source-discrepancies` |
| Where a claim came from | `sources/README.md` |
| Copilot Studio product behavior | Microsoft Learn, re-verified; never the predecessor `agents-pro` repo |
| Agent kit specifics, build order, open gates | `contoso-ai901-agent/README.md` and `STATUS.md` |
| AI-901 exam scope and weights | `contoso-ai901-agent/knowledge/ai901-objective-domain.md`, re-checked against the live study guide |

`docs/known-gaps.md` is the live gate list. When a tenant, rehearsal, or distribution check closes,
update it there rather than softening the caveats scattered through `README.md` and `START-HERE.md`.
`docs/course-delta.md` records what changed from the predecessor course and the differences between the
approved proposal and the published registration page. Do not silently resolve those.

## Content conventions

- **Sources are ranked and separated.** `sources/README.md` is the register. Keep source text, newly
  authored activities, product documentation, and actual tenant observations distinguishable in prose.
  Re-verify volatile product facts against Microsoft Learn rather than from memory.
- **Status language is textual, never color-coded.** Use `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`. Keep
  expected behavior and observed behavior in separate columns or sentences. `OBSERVED DEMO`,
  `PREDICTED`, and `NOT RUN` are distinct evidence labels, not a ranking of participation.
- **Synthetic examples must be labelled as synthetic.** `evals/native-live-three.csv` and
  `evals/native-tool-one.csv` hold authored reference responses that have not been imported or run. The
  same applies to every CSV under `contoso-ai901-agent/evals/`.
- **One scenario name.** The agent is the *Contoso AI Fundamentals Coach*. Contoso is a fictional company
  and the **AI Cert Challenge** ($100 each to the first 50 employees who pass AI-901) is invented policy,
  labelled as such in `knowledge/contoso-ai-cert-challenge.md`. Never present it as a Microsoft benefit,
  an O'Reilly policy, or a real entitlement, and never let the agent claim it can verify a pass, rank an
  employee, reserve an award, or pay anyone.

## Hard boundaries

1. **Never make this repository public.** `private: true` is asserted in both `package.json` and
   `repo-metadata.json`, and the license stays `UNLICENSED`. Publication needs Tim's explicit approval
   plus a rights and privacy review (`RIGHTS.md`, `docs/github-maintenance.md`).
2. **Never add an npm dependency.** The validator fails on any `dependencies` or `devDependencies` key.
   If one is truly needed, justify why zero-dependency tooling is insufficient before adding it.
3. **Do not broaden scope.** One course, four objectives. `course.json.scopeExclusions` lists what stays
   out, including the separate MCP course and any Foundry SDK material.
4. No AWS. No credentials, learner records, private correspondence, contracts, or presenter URLs.
5. Report what actually ran. Keep executed local checks separate from unperformed tenant, Windows, and
   GitHub operations. Readiness is evidenced, never inferred from file count.

## Copilot Studio work

This repo intentionally contains **no `.mcs.yml` files**. Both kits ship design specifications
(`topic-map.json`, contract JSON, Markdown recipes), not importable exports, and both say so explicitly.
If a task ever produces or edits Copilot Studio YAML here, route it through the `copilot-studio:author`,
`copilot-studio:test`, or `copilot-studio:troubleshoot` sub-agents, and confirm the artifact is a genuine
capture rather than an invented export before committing it.
