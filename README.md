# Build AI Agents to Automate Your Workflows

### One assistant. Four capability layers. Evidence before confidence.

**Tim Warner · O’Reilly Live · September 8, 2026 · 9:00 AM–1:00 PM Central**

[Course & registration](https://www.oreilly.com/live-events/build-ai-agents-to-automate-your-workflows/0642572413361/0642572413354/) · [Start learning](START-HERE.md) · [Instructor desk](instructor/run-of-show.md) · [TechTrainerTim](https://techtrainertim.com)

> **Course teaching kit, private source repository.** The learning path, sample inputs, worksheets,
> worked examples, timed instructor guides, and local checks are supplied. A Copilot Studio agent has **not** been deployed or certified by these tests.
> See [remaining checks](docs/known-gaps.md). Node.js and GitHub tools are optional instructor tooling,
> not prerequisites for the no-code class.

Build the **Contoso AI Fundamentals Coach** in **Microsoft Copilot Studio**.
Start with a clear job and safe boundaries. Add trusted knowledge. Give it a bounded tool.
Then test it and decide whether it is ready for a limited pilot.
AI-901 is the assistant’s subject matter; this repository teaches agent building.

## Your route through the course

| Module | What you do | What you leave with |
| --- | --- | --- |
| [01 · Inception](modules/01-inception/README.md) | Define persona, instructions, topic map, guardrails, and success metrics. | An agent brief you can actually test. |
| [02 · Build](modules/02-build/README.md) | Ground answers and design a teach-check-handoff topic. | A traceable answer and a topic that handles uncertainty. |
| [03 · Extend](modules/03-extend/README.md) | Add a study-plan action; distinguish flows, MCP, and agent delegation. | A bounded tool contract and a deliberate escalation path. |
| [04 · Operate](modules/04-operate/README.md) | Evaluate, observe, govern, and prepare publication. | Evidence and a go/no-go pilot decision. |

Each module contains a learner lab and worksheet, with worked answers and a timed instructor guide.
**The instructor builds; everyone participates.** No account, tenant, or build time is required during the
session, and the prediction, tracing, and decision exercises are the same for every attendee. Module 1
demonstrates trial signup. The full authoring recipes support independent practice afterward. See the
[pedagogy revision](docs/pedagogy-revision.md) for the delivery format that governs this.

## The four promised outcomes

- **LO1** — Plan a Copilot Studio agent from persona, job-to-be-done, instructions, topic map, guardrails, and success metrics.
- **LO2** — Build a grounded AZ-900 study assistant using knowledge sources, topics, generative answers, and test prompts.
- **LO3** — Extend the agent with actions, agent flows, MCP and subagent concepts, and human handoff patterns.
- **LO4** — Evaluate, publish, observe, and govern the agent using analytics, agent evaluations, Power Platform Well-Architected guidance, and security principles.

These four strings are quoted verbatim from the approved proposal and are not edited here. **LO2 names
AZ-900 while the delivered build is AI-901**, for the reason explained under [the agent kit](#the-agent-kit).

The [alignment map](docs/acceptance-map.md) connects each outcome to a demo, a learner artifact,
and evaluation cases. The [curriculum delta](docs/course-delta.md) explains what changed from
*How to Create AI Agents Like a Pro* without dragging its old scope into this class.

## The agent kit

[`contoso-ai901-agent/`](contoso-ai901-agent/README.md) is the single agent kit: brief, instructions,
knowledge with recorded provenance, topic map, practice-question topic, milestone workflow, tool
contracts, runbook, talk track, icons, and evaluation sets. It is **paste-ready design input for a build
performed by hand in the portal**, not an importable Copilot Studio solution.

**AI-900 retired June 30, 2026.** AI-901 replaced it under the same certification name, *Microsoft
Certified: Azure AI Fundamentals*. The predecessor AZ-900 kit was retired on September 7, 2026 and its
still-useful pieces moved into the AI-901 kit.

> **One wording difference, deliberately preserved.** The approved O’Reilly proposal and the published
> registration page both name AZ-900 in objective LO2, so [`course.json`](course.json) and the
> [proposal excerpt](sources/proposal-curriculum.md) keep that wording verbatim. The delivered build is
> AI-901. Editing a quotation of the approved proposal to match delivery would hide the difference
> instead of resolving it. See [STATUS.md](contoso-ai901-agent/STATUS.md) for the two live options and
> [remaining checks](docs/known-gaps.md) for the gate.

## Teaching and distribution

Read the [teaching design](docs/teaching-design.md), [complete promise map](docs/promise-coverage.md), and [co-instructor desk](instructor/co-instructor.md). The core tool is **GetStudySession**, with one focus and a fixed 30-minute output. The multi-day Node example is optional advanced practice.

The [slide manuscript](instructor/teaching-slides.json) supports a 35-slide companion. Binary slides stay outside Git. The [learner package procedure](learner/README.md) produces a curated local folder for the producer. A genuine native YAML capture and attendee-access check remain distribution gates.

## Start here

For learners, open [START-HERE.md](START-HERE.md). No local runtime is needed for the core exercises.

For instructor maintenance in PowerShell, after installation:

```powershell
Set-Location C:\github\oreilly-copilot-studio-agents
npm test
npm run validate
npm run demo:plan
```

These commands use **Node.js 22 or newer** and no third-party npm packages.
`demo:plan` executes a local, deterministic reference function. It does not call Copilot Studio,
create cloud resources, or impersonate a working agent flow.

## Repository map

```text
modules/                 Four modules: README, lab, worksheet
contoso-ai901-agent/     The agent kit: brief, instructions, knowledge, topics, tools, runbook, evals
practice/                Two-phase self-study and retrieval practice
instructor/              Run of show, slide manuscript, rehearsal, answer guidance, preflight
docs/                    Teaching design, coverage maps, delta register, remaining gates
curriculum/              Machine-readable outcome-to-evidence mapping
sources/                 Curriculum-only proposal excerpt and source provenance
evals/                   Agent test scenarios and unexecuted result template
learner/                 Distribution allowlist and packaging procedure
src/                     Optional deterministic study-plan reference function
scripts/                 Local validation, demo runner, and private-origin publisher
tests/                   Offline tests for repository tooling and reference function
.github/                 CI, Copilot instructions, review and issue templates
```

## Source and safety boundaries

[The approved proposal](https://docs.google.com/document/d/1FbWRkrqNZOhhlR71ru2cRMhenH3UQs-3k3T8zkqOI58/edit) provides the instructional scope.
[The published page](https://www.oreilly.com/live-events/build-ai-agents-to-automate-your-workflows/0642572413361/0642572413354/) provides the learner-facing description and schedule.
They are **not perfectly identical**; [the discrepancy register](docs/course-delta.md#source-discrepancies)
keeps those differences visible.

Microsoft Learn, not the predecessor repository, is the authority for product behavior.
[The source register](sources/README.md) separates these roles.
No customer records, presenter access links, contracts, tokens, or private correspondence belong here.

**Do not publish this repository publicly without Tim’s explicit approval and a rights/privacy review.**
A private GitHub URL alone is not a learner-access plan.
See [distribution guidance](docs/github-maintenance.md) and [RIGHTS.md](RIGHTS.md).
