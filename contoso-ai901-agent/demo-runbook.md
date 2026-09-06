# Live build runbook - Contoso AI Fundamentals Coach

**Build four things, prove four things.** Each hour adds one capability and one way to check it. If you
are behind, cut the explanation and keep the proof; the proof is the course.

**Authored 2026-09-06. Nothing here has been rehearsed in a tenant. Every timing is an estimate until
you run it once with a clock.**

**The spoken lines live in [`demo-runbook-talk-track.md`](demo-runbook-talk-track.md).** This file is
the operator sequence; that one is the talk track, in SAY / DO / PAUSE format.

## Prebuild before 8:30

Nothing on this list is worth an audience's attention, and every item on it can fail slowly.

| # | Prebuild | Why it can't be live |
| --- | --- | --- |
| 1 | Environment, licenses, publishing access confirmed | A permission dialog isn't a lesson |
| 2 | SharePoint `ExamMilestones` list with the two seed rows | See [`tools/exam-milestones-list-schema.md`](tools/exam-milestones-list-schema.md) |
| 3 | Teams `Certification Milestones - Demo` channel, empty | Creating a channel live burns three minutes |
| 4 | SharePoint and Teams connections, scoped | Connection consent screens are unpredictable |
| 5 | `GeneratePracticeQuestion` prompt created with its saved output format | Typing an output contract on camera is the worst 8 minutes of any workshop |
| 6 | `RecordExamMilestone` flow built, published, tested, minus the two effect actions | You will add those two live; the plumbing is prebuilt |
| 7 | Six generated sample items reviewed against their packets | This is the only quality check that exists |
| 8 | Baseline evaluation run saved, if you are doing before-and-after | A probabilistic failure won't appear on cue |
| 9 | One reviewed fallback item, printed | For when generation fails on camera |
| 10 | The `cloud` regression test run once | Proves the AI-901 focus swap actually landed |

**Recovery rule:** one deliberate retry of a failed live operation, then move to the rehearsed
checkpoint or the labeled prepared example. Never spend a teaching block debugging authentication.

## Hour One - Inception, 9:00 to 9:50

**Exit evidence:** a real shell with real instructions and one demonstrated boundary.

| Min | Beat | Artifact |
| --- | --- | --- |
| 4 | The Contoso enablement problem. 400 employees, one certification, no shared study support. | [`agent-brief.md`](agent-brief.md) |
| 7 | Topic, prompt, flow: controlled conversation, generation in a defined shape, coordinated work. | - |
| 8 | Access and trial reality. Show what a trial can and can't do, including publishing. | - |
| 9 | The agent brief. Persona, job, four capabilities, four verification obligations. | [`agent-brief.md`](agent-brief.md) |
| 10 | **Create the shell.** Name, description, paste instructions, save. Type `/` once to insert a live object reference. | [`instructions.md`](instructions.md) |
| 7 | Universal design exercise. | worksheet |
| 5 | Q&A | - |

**Say the exam-number correction once, at minute 4.** AI-900 retired June 30, 2026; the current exam is
AI-901; the certification name didn't change. Then say the published objective LO2 names AZ-900 and
that the design skill is identical. Twenty seconds, and nobody emails you about it afterward. Sourcing
is in [`STATUS.md`](STATUS.md).

**Announce the three boundaries before demonstrating any of them:** no ungrounded certainty, no real
exam items, no enterprise write without confirmation. An audience that can predict behavior is an
audience that is learning rather than watching.

**Cut first:** feature history, licensing comparisons, model-selection tangents. **Never cut:** the
boundary statement and the shell creation.

## Hour Two - Build, 10:00 to 10:50

**Exit evidence:** a grounded answer, and a dynamic quiz item with a real wait point.

| Min | Beat | Artifact |
| --- | --- | --- |
| 4 | Recall the component model. | - |
| 8 | Add one knowledge source. Retrieve a known statement. **Then ask something it doesn't cover.** | [`knowledge/upload-metadata.md`](knowledge/upload-metadata.md) |
| 5 | Inspect the prebuilt prompt's structured output contract. Read it, don't type it. | [`prompts/generate-practice-question.md`](prompts/generate-practice-question.md) |
| 15 | **Build the topic canvas.** Variables, branch, prompt call, validation gate, and the Question node. | [`topics/practice-ai901-question.md`](topics/practice-ai901-question.md) |
| 6 | Correction, invalid input, and the fallback path. | same |
| 7 | Predict-and-trace exercise. | worksheet |
| 5 | Q&A | - |

**The 8-minute knowledge beat lands on the refusal, not the retrieval.** "What are the six responsible
AI principles?" is unremarkable. "How many questions are on the exam?" is the demo.

**Before you click Test on the topic, tell the room what to watch for:** the turn must end on the
question. Then run it. If the agent answers itself, you have a genuine finding - trace it live rather
than moving on.

**Pause point at minute 12 of the canvas build.** Ask the room to predict which variables change on
"another question" and which must stay hidden until the employee answers. Then show them.

**Cut first:** adaptive cards, large topic inventories, a full MCP walkthrough. **Never cut:** the wait
state, answer validation, or the evidence boundary.

## Hour Three - Extend, 11:00 to 11:50

**Exit evidence:** a confirmed milestone, one SharePoint row, one Teams post, and an inspected status.

| Min | Beat | Artifact |
| --- | --- | --- |
| 4 | Answer, clarify, call a tool, or reach a human. Four different decisions. | - |
| 4 | `GetStudySession` invoked once. Fixed scope, inspected status. | [`tools/get-study-session.md`](tools/get-study-session.md) |
| 19 | **The milestone workflow.** Show the empty list and empty channel first. Add the two effect actions. Build the consent topic. Run it. | [`tools/record-exam-milestone.md`](tools/record-exam-milestone.md), [`topics/record-exam-milestone.md`](topics/record-exam-milestone.md) |
| 8 | Extension patterns compared: MCP, HTTP tools, connected agents, A2A, Foundry, human handoff. | [`../sample-agent/tools/extension-decisions.md`](../sample-agent/tools/extension-decisions.md) |
| 5 | Duplicates, partial failure, and privacy. | [`tools/milestone-result.contract.json`](tools/milestone-result.contract.json) |
| 5 | Learner decision exercise. | worksheet |
| 5 | Q&A | - |

**Order matters in the 19-minute block.** Empty destinations first, then decline the write, then inspect
that both are still empty, and only then confirm. Proving absence before presence is what separates this
from a product tour.

**The Jordan Reyes seed row** is your `already_recorded` example: a record exists and its announcement
never went out. The agent has to report both facts.

**Keep the extension-pattern block at comparison level.** MCP, Foundry, Fabric, and A2A are named and
distinguished, not configured. A Teams post is an announcement, not a human handoff - say that plainly.

**Cut first:** extra connector demos, platform taxonomy depth. **Never cut:** the confirmation gate or
the inspection of actual effects.

## Hour Four - Operate, 12:00 to 12:50

**Exit evidence:** an imported evaluation set, a run you can explain, and a defensible pilot decision.

| Min | Beat | Artifact |
| --- | --- | --- |
| 4 | Revisit the acceptance criteria written in Hour One. | [`agent-brief.md`](agent-brief.md) |
| 13 | Download the template, compare, import, configure methods, run the five cases. | [`evals/native-method-configuration.md`](evals/native-method-configuration.md) |
| 6 | Inspect routing evidence and the workflow run. | [`evals/native-routing.csv`](evals/native-routing.csv) |
| 6 | Analytics, transcripts, environment controls, and the five Well-Architected concerns. | [`../modules/04-operate/README.md`](../modules/04-operate/README.md) |
| 9 | Scoped publishing and a fresh-session test in a separate channel. | - |
| 7 | Pilot decision exercise. | worksheet |
| 5 | Q&A | - |

**The line to land in the evaluation block:** the booking case can score a perfect semantic match while
an unintended write happened. Show the trace. Semantic agreement measures wording, not effects.

**Separate the announcement channel from the publishing channel.** Posting a message doesn't
demonstrate publishing an agent, and conflating them is an easy accidental lie.

**Cut first:** touring every metric, running every case live. **Never cut:** expected versus observed,
or the pilot decision.

## Wrap-up - 12:50 to 1:00

Transfer the design, not the scenario. Each attendee names one workplace problem, the one capability
their agent would need first, and the one test that would settle whether they can trust it.

## When something breaks

| Symptom | First move | Fallback |
| --- | --- | --- |
| Routing misses the practice topic | Edit the **topic description**, not the instructions | Invoke the topic directly and explain the difference |
| Prompt returns malformed output | Show the validation gate rejecting it - this is a feature | Use the printed reviewed item, labeled as prepared |
| Flow times out | Check asynchronous response is off | Show the prebuilt successful run and its outputs |
| Teams post fails | Don't fix it. Show `recorded_only` | This is the best accident you can have |
| Evaluation set won't import | Compare against the downloaded template live | Show the saved baseline run |
| Tenant unavailable | Stop trying at two minutes | Teach from [`STATUS.md`](STATUS.md) and the saved evidence |

A failure you narrate accurately is worth more than a demo that works. Say what happened, say what you
don't know yet, and move to the next checkpoint.
