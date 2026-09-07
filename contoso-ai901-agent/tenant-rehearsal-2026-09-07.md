# September 8 live demo route

**Tenant rehearsal performed September 7, 2026.** This is a sanitized record of actual instructor
tenant work. Resource identifiers, maker links, run details, and synthetic test conversations remain
in the private local handoff. This record does not establish attendee access or full course readiness.

## The deployed learner journey

**Contoso AI Fundamentals Coach** was created from this kit in the standard authoring experience.
The agent uses GPT-5.5 Chat, Microsoft authentication, configured knowledge, a practice topic, and
two agent flows. General model knowledge and web search are disabled. The practice prompt uses
GPT-4.1 mini with a saved JSON output format.

The September 8 signup demonstration follows Tim's simplified request. **Certification Signups**
stores **Name** and **Signup Date**. **RecordCertificationSignup** writes the synthetic name
**Jordan Reyes (Demo)** and today's date only after fresh confirmation. A separate automated flow,
**Contoso AI-901 - Announce certification signup**, reacts to the new item and posts through Flow bot
to **Certification Signups - Demo** in the selected Contoso community team.

This route replaces the original **RecordExamMilestone / ExamMilestones** build for this delivery.
Those earlier files remain design references. Do not describe the deployed signup as an exam booking,
verified pass, reward claim, or authenticated employee enrollment. The existing demo connection
supplies access; the synthetic identity is deliberate.

## Rehearse these steps in the maker test pane

1. Start a new test session. Request the six responsible AI principles and a source citation.
2. Request the number of questions on the exam. Explain the boundary when the coach cannot verify it.
3. Say **Give me an AI-901 practice question**. Choose a study area. Stop at the question before
   answering, then inspect feedback and the source. Choose **Yes** for a fresh item and **No** to finish.
4. Say **Give me a study session**. Supply **responsible-ai**, **workloads**, or **foundry** when prompted.
   Inspect the returned `status` and fixed 30-minute `plan` in the trace.
5. Say **Sign me up for AI-901**. Read the confirmation, including both the SharePoint write and Teams
   announcement. Choose **No** first and verify the list did not grow.
6. Repeat **Sign me up for AI-901**, then choose **Yes**. Inspect the saved row and returned record link.
   Open the separate notification flow's run history and inspect its Teams result and message link.

**Signup routing is explicit.** The native **A message is received** trigger has a Power Fx condition
for a small set of direct signup phrases, including the phrase above. Description-based generative
routing repeatedly skipped this topic during rehearsal. The condition does not match Yes/No replies.
Every entry still prompts for fresh consent. Use the rehearsed phrase in the live demonstration.

**Each new confirmation creates another demo row.** This minimal example does not deduplicate
enrollments. Do not resubmit a successful flow run. After an ambiguous failure, inspect the list
before retrying. The independent notification can arrive after the agent returns its saved result;
the agent correctly does not claim that Teams has posted without separate evidence.

## Evidence actually observed

| Check | Result observed September 7 |
| --- | --- |
| Agent creation and publication | Agent created and native publication succeeded; broad distribution not tested |
| Knowledge ingestion | `ai901-concepts.txt`, `ai901-objective-domain.md`, and `contoso-ai-cert-challenge.md` all Ready |
| Grounded concepts | Correct six-principles response cited the concepts file |
| Unsupported exam-count question | Coach explicitly could not verify the count instead of inventing one |
| Practice prompt binding | Native output is `predictionOutput.structuredOutput`; topic checker reported zero errors and warnings |
| Practice behavior | Four generated items across all three study areas; correct and incorrect grading, source links, fresh-item loop, and exit observed |
| Study session | All three supported focuses returned `ok`; unsupported focus returned `unsupported`; missing focus requested clarification |
| Study response fidelity | Fresh session returned the fixed responsible-AI plan without additional activities |
| Signup declined | Cancellation response; list stayed at the single pre-existing synthetic test row |
| Signup confirmed | Exactly one new Jordan demo row, dated September 7; agent returned saved record number and link |
| Teams notification | Both the initial seeded signup and agent-created signup produced successful runs; Teams returned HTTP 201 and actual message identifiers |
| Native inspection artifact | [Sanitized saved practice topic](topics/exports/practice-ai901-question.native.yaml), with its [scope and provenance](topics/exports/README.md) |

## Remaining checks

- The full 32-case native evaluation and same-case comparison have **not** run.
- Four generated samples are a smoke test. The broader item-quality review has **not** run. All four
  observed keys were A, so answer-position variety is not established. Source packets are currently
  fixed to one reviewed packet per study area; this is a bounded demonstration, not an exam simulator.
- Malformed prompt output and tool-unavailability branches were inspected but not fault-injected.
- Publishing succeeded, but a second user and the agent's Teams channel installation have **not** been
  tested. A successful Teams notification is not proof of agent availability in Teams.
- Store validation of the uploaded icon, full timed rehearsal, recovery recording, producer-approved
  distribution, and attendee access remain unverified.

Preserve the four approved objective quotations. Say that **LO2 names AZ-900 while this live build
uses AI-901**. The audience follows the instructor demonstration and needs no tenant or local code.
