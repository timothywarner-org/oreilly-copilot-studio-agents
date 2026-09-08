# Status, sourcing, and open gates

**Updated 2026-09-07. Tenant smoke tests performed.** The coach, knowledge, practice topic, study
flow, signup list, and Teams notification now exist and have live evidence. Follow the
[dated demo route and evidence](tenant-rehearsal-2026-09-07.md) for September 8. Native evaluations
completed with failures: Core Five **2/5**, Knowledge and Challenge **8/32**, Routing **2/3**.
One preclass run is waiting for September 8 at **6:00 AM Central**. Second-user channel access and
timed delivery remain unverified. Local validation checks integrity only.

## September 7 authoring update

- Formal Markdown instructions now include distinct exam-scope and fictional challenge grounding.
- Three Microsoft 365 Designer prompts provide a main agent avatar and matching companion artwork.
- [Finished avatar and listing icons](assets/icons/README.md) now include the 192-pixel color PNG and
  the 32-pixel white outline with verified alpha transparency. Artwork was generated with ImageGen
  and finished with user-authorized ImageMagick. Stored avatar and channel icons match the kit after
  publication; installed appearance and store validation remain **NOT RUN**.
- `knowledge/ai901-objective-domain.md` was actually generated using **MarkItDown 0.1.2** from
  Microsoft Learn. The complete Skills measured section contains two domains, seven groups, and
  all objective bullets. [Conversion provenance](sources/ai901-objective-domain.provenance.json)
  records source and output hashes. Source ingestion now reports **Ready**; retrieval evidence is
  scoped in the dated rehearsal record.
- `knowledge/contoso-ai-cert-challenge.md` is newly authored fictional policy: first 50 qualifying
  Contoso employees receive **$100 USD each**, with human verification and one award per employee.
- `evals/ai901-challenge.csv` contains **32 original cases** in Microsoft's documented template schema.
  The native template control was inspected, but no downloaded template file was captured. Native
  template file comparison remains **NOT RUN**. All three evaluation sets were imported and run;
  scores, changes, and the one-time schedule are recorded in the dated rehearsal.

This update fulfills the requested AI-901 scaffold work. The approved four objective strings in
`course.json` and `sources/proposal-curriculum.md` remain the course commitment record and are
unchanged. The AZ-900 kit was retired on September 7, 2026; this is now the only agent kit.

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
3. ~~**Keep AZ-900.**~~ **No longer available.** The AZ-900 kit was retired on September 7, 2026 at
   Tim's direction. This is the only agent kit, so option 1 or option 2 is the live choice.

Don't silently edit LO2 in `course.json`. The validator would pass only if the proposal excerpt were
edited too, and that excerpt is a verbatim quotation of the approved O'Reilly proposal. Rewriting a
quotation to match delivery conceals the exact difference this repository is designed to surface.
**Option 1 is the recommended close for the September 8 delivery**, because the registration page and
the approved proposal both still say AZ-900 and neither can be changed before the session.

## What is authored versus what is unproven

| Item | State |
| --- | --- |
| Instructions, brief, topic map, knowledge, evidence register | Authored, reviewed, character-count checked |
| Prompt text and logical output contract | Saved native JSON format bound as `predictionOutput.structuredOutput` |
| Practice-question Topic recipe | Checker passed; four live items, grading, citation, wait point, and loop observed |
| GetStudySession AI-901 plan text | Flow published and bound; supported, unsupported, and missing focus tested |
| RecordExamMilestone flow, list, channel | Original design retained; simplified Certification Signups route deployed and tested instead |
| Native evaluation CSVs | All three sets imported and run; failed grades retained; downloaded-template comparison NOT RUN |
| Generated-item quality | Four samples inspected; broader quality review remains open, including answer-position variety |

## Product claims that need tenant confirmation before you teach them

- Whether your environment shows the standard harness Build tab or another authoring experience.
- Whether Prompt builder in your tenant exposes the saved output format this kit assumes, and what the
  returned field names actually are.
- Whether generative orchestration routes "quiz me" to the practice Topic from its description alone.
- Whether the agent flow completes inside the documented synchronous limit with asynchronous response off.
- Whether evaluation runs are permitted to call connected tools in your environment.

Record each observation in [`../instructor/rehearsal-record.md`](../instructor/rehearsal-record.md).
A documentation page isn't proof of availability in your tenant.
