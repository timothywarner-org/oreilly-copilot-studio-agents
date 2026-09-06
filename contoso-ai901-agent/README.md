# Contoso AI Fundamentals Coach - live-build authoring kit

**This is a design and authoring kit, not an importable Copilot Studio solution.** Every file here is
paste-ready input for a build you perform by hand in the portal during class. Nothing in this folder
has been executed in a tenant. Status language stays textual: **PASS**, **FAIL**, **BLOCKED**, **NOT RUN**.

## The scenario in one paragraph

Contoso is putting 400 employees through **Microsoft Certified: Azure AI Fundamentals**. The current
exam for that certification is **AI-901**. Contoso's enablement team builds one agent that explains an
AI-901 concept from approved evidence, generates and grades one original practice question at a time,
returns a fixed study session, and records a self-reported exam booking to SharePoint and Teams after
the employee confirms it. Course attendees aren't Contoso employees. Attendees are learning to
**design** this agent; Contoso employees are the people who would use it.

## Why AI-901 and not AI-900

**AI-900 retired June 30, 2026.** AI-901 replaced it; the certification name didn't change. See
[`STATUS.md`](STATUS.md) for the exact sourcing and the one wording gate this creates against the
published course objective LO2.

## Build order and file map

Build in this order. Each row is a checkpoint you can stop at with something that works.

| # | Do this | Files |
| --- | --- | --- |
| 1 | Decide what the agent is allowed to do | [`agent-brief.md`](agent-brief.md) |
| 2 | Create the shell, paste instructions | [`instructions.md`](instructions.md), [`instructions-compact.md`](instructions-compact.md) |
| 3 | Add knowledge, verify retrieval | [`knowledge/`](knowledge/upload-metadata.md) |
| 4 | Author the practice-question Topic | [`topics/practice-ai901-question.md`](topics/practice-ai901-question.md), [`prompts/generate-practice-question.md`](prompts/generate-practice-question.md) |
| 5 | Swap the study-session flow to AI-901 | [`tools/get-study-session.md`](tools/get-study-session.md) |
| 6 | Add the confirmed milestone workflow | [`topics/record-exam-milestone.md`](topics/record-exam-milestone.md), [`tools/record-exam-milestone.md`](tools/record-exam-milestone.md) |
| 7 | Import and run the evaluation set | [`evals/native-method-configuration.md`](evals/native-method-configuration.md) |

The click-by-click sequence with timings, pause points, and fallbacks is
[`demo-runbook.md`](demo-runbook.md). The words you actually say are in
[`demo-runbook-talk-track.md`](demo-runbook-talk-track.md), drafted in Tim's spoken register and
linted clean.

## Routing design and contracts

| File | What it is | What it isn't |
| --- | --- | --- |
| [`topic-map.json`](topic-map.json) | Routing design specification | Native Copilot Studio YAML |
| [`prompts/practice-question.contract.json`](prompts/practice-question.contract.json) | Logical output shape for offline checks | An importable Prompt definition |
| [`tools/milestone-result.contract.json`](tools/milestone-result.contract.json) | Application status vocabulary | Connector status names |
| [`tools/get-study-session.json`](tools/get-study-session.json) | Expected-output fixture | A flow export |
| [`knowledge/evidence-register.json`](knowledge/evidence-register.json) | Reviewed evidence packets and their source mapping | Retrieval proof |

## Relationship to the AZ-900 kit

[`../sample-agent/`](../sample-agent/README.md) is the original AZ-900 authoring kit. It is unchanged
and remains the fallback if the AI-901 path is blocked in your tenant. The repository validator still
binds to it, so don't delete or rewrite it.

## The rule that governs every file here

A fluent answer isn't proof that a tool ran. Inspect the actual returned result before claiming an
effect happened. Every claim of tenant behavior in this folder is marked **NOT RUN** until an
observation replaces it.
