# Status, sourcing, and open gates

**Authored 2026-09-06. Tenant execution: NOT RUN.** Nothing in this folder has been created, imported,
published, or observed in Copilot Studio. Local repository validation checks file integrity only.

## The exam-number correction

**AI-900 retired June 30, 2026.** The replacement exam is **AI-901: Microsoft Azure AI Fundamentals**,
skills measured as of April 15, 2026. The certification itself, *Microsoft Certified: Azure AI
Fundamentals*, didn't change name or split; passing either exam earns the same credential.

Verified against Microsoft Learn on 2026-09-06:

- [AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)
- [Exam and assessment lab retirement](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams)
- [AI-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900), which now carries a retirement banner

## AI-901 scope as published

Two skill areas, not the five that AI-900 used. Any material that recites five AI-900 domains is stale.

| Skill area | Weight |
| --- | --- |
| Identify AI concepts and capabilities | 40-45% |
| Implement AI solutions by using Microsoft Foundry | 55-60% |

The AI-901 audience profile expects awareness of Python syntax and familiarity with Azure resources.
That applies to a **Contoso employee sitting the exam**, not to a course attendee. The attendee route
in this course stays no-code and `course.json.codingRequiredForLearners` stays `false`.

## Open gate: LO2 says AZ-900

The approved objective LO2 reads *"Build a grounded AZ-900 study assistant using knowledge sources,
topics, generative answers, and test prompts."* That text is contractual, is asserted verbatim by
`scripts/validate-repo.mjs` against `sources/proposal-curriculum.md`, and has **not** been changed.

Three ways to close this, in the order I would take them:

1. **Narrate it.** Say once in Hour One that the published objective names AZ-900 and that the live
   build uses AI-901 because AZ-900's sibling fundamentals exam moved. The skill being taught,
   grounding a study assistant, is identical. Costs 20 seconds and no approvals.
2. **Editorial correction after delivery.** Ask O'Reilly to update the objective text and the
   registration page together, then update `course.json` and the proposal excerpt in one commit.
3. **Keep AZ-900.** [`../sample-agent/`](../sample-agent/README.md) is intact and still builds. AZ-900
   hasn't retired.

Don't silently edit LO2 in `course.json`. The validator would pass only if the proposal excerpt were
edited too, which would conceal a difference the repository is designed to surface.

## What is authored versus what is unproven

| Item | State |
| --- | --- |
| Instructions, brief, topic map, knowledge, evidence register | Authored, reviewed, character-count checked |
| Prompt text and logical output contract | Authored; native output-format binding NOT RUN |
| Practice-question Topic recipe | Authored from documentation; canvas behavior NOT RUN |
| GetStudySession AI-901 plan text | Authored; flow edit NOT RUN |
| RecordExamMilestone flow, list, channel | Authored design; SharePoint list and Teams channel NOT CREATED |
| Native evaluation CSVs | Authored to the documented two-column shape; template comparison and import NOT RUN |
| Generated-item quality | Can't be established without inspecting real samples against the evidence |

## Product claims that need tenant confirmation before you teach them

- Whether your environment shows the standard harness Build tab or another authoring experience.
- Whether Prompt builder in your tenant exposes the saved output format this kit assumes, and what the
  returned field names actually are.
- Whether generative orchestration routes "quiz me" to the practice Topic from its description alone.
- Whether the agent flow completes inside the documented synchronous limit with asynchronous response off.
- Whether evaluation runs are permitted to call connected tools in your environment.

Record each observation in [`../instructor/rehearsal-record.md`](../instructor/rehearsal-record.md).
A documentation page isn't proof of availability in your tenant.
