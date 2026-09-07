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

### Completed authoring assets, September 7

| Asset | Ready to use |
| --- | --- |
| Agent identity | **Contoso AI Fundamentals Coach**. Description: Helps Contoso employees study for AI-901 using approved knowledge, original practice questions, and fixed study sessions. Explains the fictional AI Cert Challenge and records self-reported exam bookings after confirmation. |
| Formal Markdown instructions | Paste the complete contents of [`instructions.md`](instructions.md) into the agent instructions. The entire file is below the 8,000-character limit; headings and lists are part of the instructions. |
| Designer prompts | [`Three matching icon prompts`](prompts/designer-agent-icons.md), with the book-and-nodes design as the main avatar. |
| Finished icons | [`Avatar and Teams/Microsoft 365 listing icons`](assets/icons/README.md): 192-pixel avatar/color PNGs and a 32-pixel white transparent outline, with verified requirements and file checks. |
| Official objective domain | [`MarkItDown knowledge file`](knowledge/ai901-objective-domain.md), with complete objective wording from Microsoft Learn and dated provenance. |
| Company grounding | [`Fictional Contoso AI Cert Challenge`](knowledge/contoso-ai-cert-challenge.md): **first 50 qualifying employees, $100 USD each**. |
| Evaluation | [`AI-901 and challenge CSV`](evals/ai901-challenge.csv) and [`import, coverage, and scoring notes`](evals/ai901-challenge-guide.md). |

Use [`knowledge/upload-metadata.md`](knowledge/upload-metadata.md) for source descriptions and retrieval
checks. The challenge is a grounded policy conversation. The booking workflow does not verify passes,
rank winners, submit reward claims, or pay employees.

### Existing progressive build

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

## This is the only agent kit

The predecessor AZ-900 kit at `sample-agent/` was retired on September 7, 2026. Its still-useful pieces
moved here: [`exports/README.md`](exports/README.md), [`tools/extension-decisions.md`](tools/extension-decisions.md),
[`tools/flow-design.md`](tools/flow-design.md), [`tools/study-plan-contract.json`](tools/study-plan-contract.json),
and [`tools/example-input.json`](tools/example-input.json). Everything else it held is superseded by a
file in this folder.

`scripts/validate-repo.mjs` now binds to this kit by path. It asserts the **GetStudySession** name, the
30-minute session, the three focus values, and that every plan string in
[`tools/get-study-session.json`](tools/get-study-session.json) also appears in
[`tools/get-study-session.md`](tools/get-study-session.md). Renaming or restructuring those two files
fails the build.

## The rule that governs every file here

A fluent answer isn't proof that a tool ran. Inspect the actual returned result before claiming an
effect happened. Every claim of tenant behavior in this folder is marked **NOT RUN** until an
observation replaces it.
