# Build AI Agents to Automate Your Workflows

### One assistant. Four capability layers. Evidence before confidence.

**Tim Warner · O’Reilly Live · September 8, 2026 · 9:00 AM–1:00 PM Central**

[Course & registration](https://www.oreilly.com/live-events/build-ai-agents-to-automate-your-workflows/0642572413361/0642572413354/) · [Start learning](START-HERE.md) · [Instructor desk](instructor/run-of-show.md) · [TechTrainerTim](https://techtrainertim.com)

> **Preparation scaffold — private origin intended.** The learning path, sample inputs, worksheets,
> and local checks are supplied. A Copilot Studio agent has **not** been deployed or certified by these tests.
> See [remaining checks](docs/known-gaps.md). Node.js and GitHub tools are optional instructor tooling,
> not prerequisites for the no-code class.

Build the **AZ-900 Cert-Prep Assistant** in **Microsoft Copilot Studio**.
Start with a clear job and safe boundaries. Add trusted knowledge. Give it a bounded tool.
Then test it and decide whether it is ready for a limited pilot.
AZ-900 is the assistant’s subject matter; this repository teaches agent building.

## Your route through the course

| Module | What you do | What you leave with |
| --- | --- | --- |
| [01 · Inception](modules/01-inception/README.md) | Define persona, instructions, topic map, guardrails, and success metrics. | An agent brief you can actually test. |
| [02 · Build](modules/02-build/README.md) | Ground answers and design a teach-check-handoff topic. | A traceable answer and a topic that handles uncertainty. |
| [03 · Extend](modules/03-extend/README.md) | Add a study-plan action; distinguish flows, MCP, and agent delegation. | A bounded tool contract and a deliberate escalation path. |
| [04 · Operate](modules/04-operate/README.md) | Evaluate, observe, govern, and prepare publication. | Evidence and a go/no-go pilot decision. |

Each module contains a learner lab and a worksheet. You can participate through a **maker route**
with tenant access or an **observer route** using the same prompts and acceptance criteria.

## The four promised outcomes

- **LO1** — Plan a Copilot Studio agent from persona, job-to-be-done, instructions, topic map, guardrails, and success metrics.
- **LO2** — Build a grounded AZ-900 study assistant using knowledge sources, topics, generative answers, and test prompts.
- **LO3** — Extend the agent with actions, agent flows, MCP and subagent concepts, and human handoff patterns.
- **LO4** — Evaluate, publish, observe, and govern the agent using analytics, agent evaluations, Power Platform Well-Architected guidance, and security principles.

The [alignment map](docs/acceptance-map.md) connects each outcome to a demo, a learner artifact,
and evaluation cases. The [curriculum delta](docs/course-delta.md) explains what changed from
*How to Create AI Agents Like a Pro* without dragging its old scope into this class.

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
sample-agent/            Instructions, topic map, knowledge, and tool specification
practice/                Two-phase self-study and retrieval practice
instructor/              Run of show, rehearsal, answer guidance, preflight
curriculum/              Machine-readable outcome-to-evidence mapping
sources/                 Curriculum-only proposal excerpt and source provenance
evals/                   Agent test scenarios and unexecuted result template
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
