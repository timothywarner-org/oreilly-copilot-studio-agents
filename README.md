# Build AI Agents to Automate Your Workflows

### One agent. Four capability layers. Evidence before confidence.

**Tim Warner · O’Reilly Live · September 8, 2026 · 9:00 AM–1:00 PM Central**

[Start here](START-HERE.md) · [The agent kit](contoso-ai901-agent/README.md) · [Every link, verified](sources/link-register.md) · [Course page](https://www.oreilly.com/live-events/build-ai-agents-to-automate-your-workflows/0642572413361/0642572413354/) · [TechTrainerTim](https://techtrainertim.com)

## What you build

The **Contoso AI Fundamentals Coach**, a Microsoft Copilot Studio agent for a fictional company putting
400 employees through **Microsoft Certified: Azure AI Fundamentals**, currently exam **AI-901**.

The coach does four things and refuses everything else:

1. **Explains** an AI-901 concept from approved evidence, with a citation you can trace.
2. **Quizzes** you with one original practice question at a time, then waits for your answer before grading it.
3. **Returns** a fixed 30-minute study session for one focus: `responsible-ai`, `workloads`, or `foundry`.
4. **Records** a self-reported exam booking to SharePoint and Teams, but only after you confirm it.

That fourth one is where the interesting judgment lives. The agent writes to a real system, so it has to
ask first, and it must never claim a booking happened when it did not.

AI-901 is the subject matter. **Agent building is the skill.** You can swap the exam for your own domain
and the four layers do not change.

## Your route

| Module | What you do | What you leave with |
| --- | --- | --- |
| [01 · Inception](modules/01-inception/README.md) | Define persona, instructions, topic map, guardrails, and success metrics. | An agent brief you can actually test. |
| [02 · Build](modules/02-build/README.md) | Ground answers and design a teach-check-handoff topic. | A traceable answer and a topic that handles uncertainty. |
| [03 · Extend](modules/03-extend/README.md) | Add a study-session action; distinguish flows, MCP, and agent delegation. | A bounded tool contract and a deliberate escalation path. |
| [04 · Operate](modules/04-operate/README.md) | Evaluate, observe, govern, and prepare publication. | Evidence and a go/no-go pilot decision. |

Each module has a lab, a worksheet, and worked answers. After the session,
[practice mode](practice/README.md) and the [evaluation cases](evals/README.md) let you check your own build.

## What you need

**Nothing.** The agent is built live in front of you, and every exercise is a prediction, a trace, or a
decision you can make without an account. Module 1 demonstrates trial signup for anyone who wants to
follow along later.

For independent practice afterward you will want a Microsoft 365 work or trial account with Copilot
Studio access, in a nonproduction environment, using synthetic data only. A trial supports building and
testing but not publishing. No coding, no paid API key, no Python, no GitHub Copilot subscription.

## What you get

| Folder | What is in it |
| --- | --- |
| [`contoso-ai901-agent/`](contoso-ai901-agent/README.md) | The whole agent: brief, instructions, knowledge, topic map, topics, tool contracts, evaluation sets, icons, and a click-by-click build runbook |
| [`modules/`](modules/01-inception/README.md) | Four modules, each with a lab and a worksheet |
| [`sources/link-register.md`](sources/link-register.md) | Every Microsoft Learn page behind the course, grouped by segment and checked for reachability |
| [`practice/`](practice/README.md) | Two-phase self-study: question first, feedback after you answer |
| [`evals/`](evals/README.md) | Twelve scenarios for checking your own agent |

The kit is **paste-ready design input for a build you perform by hand in the portal**. It is not an
importable solution file, and nothing in it has been run in a tenant, so treat every expected result as
something to verify rather than something already proven.

## The one wording difference

Objective LO2 below says **AZ-900** while the build is **AI-901**. AI-900 retired on June 30, 2026 and
AI-901 replaced it under the same certification name, after the objectives were approved. The objective
text is quoted exactly as approved rather than quietly rewritten. Same skill, current exam.

- **LO1** — Plan a Copilot Studio agent from persona, job-to-be-done, instructions, topic map, guardrails, and success metrics.
- **LO2** — Build a grounded AZ-900 study assistant using knowledge sources, topics, generative answers, and test prompts.
- **LO3** — Extend the agent with actions, agent flows, MCP and subagent concepts, and human handoff patterns.
- **LO4** — Evaluate, publish, observe, and govern the agent using analytics, agent evaluations, Power Platform Well-Architected guidance, and security principles.

## Optional local tooling

You do not need any of this to take the course. It exists to keep the written material consistent.

```powershell
npm test          # offline tests for the reference function and repository checks
npm run validate  # cross-file integrity checks, no network
npm run check:links   # reachability of every link in the link register, two passes
npm run demo:plan # optional multi-day study-plan reference function
```

**Node.js 22 or newer**, zero third-party packages. None of it calls Copilot Studio or creates cloud resources.

## For the instructor

[Run of show](instructor/run-of-show.md) · [Teaching design](docs/teaching-design.md) ·
[Delivery status and open gates](docs/known-gaps.md) · [Source register](sources/README.md) ·
[Curriculum delta](docs/course-delta.md) · [Rights and distribution](RIGHTS.md)

Microsoft Learn is the authority for product behavior; re-verify anything that looks stale before you
teach it. This repository stays private until Tim approves publication after a rights and privacy review.
