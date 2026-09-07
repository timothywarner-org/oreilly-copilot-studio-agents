# Native evaluation: methods, mapping, and what each one can't prove

**Four different questions, four different checks.** Confusing them is the most common evaluation
mistake, and separating them is the whole point of Hour Four.

| Question | Appropriate check | What it doesn't establish |
| --- | --- | --- |
| Did the response express the right answer? | Compare meaning against a reference answer | That any particular tool ran |
| Did the expected topic or tool participate? | Native Tool use with actual expected capabilities | Correct arguments, completed effects, or valid consent |
| Did the whole quiz or consent conversation behave? | Conversational evaluation, or a manual multi-turn trace | Independent proof that external systems changed |
| Did the row and the post actually exist? | Connector run evidence plus direct inspection of the list and the channel | General correctness of future runs |

**Authored. Native template comparison and import: NOT RUN.** These files were written to the documented
two-column shape. They haven't been compared against a template downloaded from your tenant.

## Import the single-response set

For the completed objective-domain and reward scenario, use the **32-case**
[`ai901-challenge.csv`](ai901-challenge.csv) and its
[`template, coverage, and scoring guide`](ai901-challenge-guide.md). The original five-case set below
remains the short live demonstration. The expanded set adds company grounding and missing-information
checks without changing the native two-column schema.

1. Open the agent's **Evaluation** page.
2. Select **New evaluation → Single response**.
3. Download the CSV template under **Data source**.
4. **Compare the template's headings with [`native-core-five.csv`](native-core-five.csv) before
   importing.** If they differ, the template wins; adjust the file and record the difference.
5. Import, configure methods and the test user, then run the set.

Documentation specifies the first two columns as `Question` and `Expected response`, up to 100 cases,
and a 1,000-character limit per question. Expected responses are optional at import and required for
comparison methods that use them. Don't invent native ID, rubric, or tool columns. Reference:
[Create a single response test set](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create).

## Method configuration for the five-case set

Start with **Compare meaning** only. Remove **General quality** if it appears by default; a second
score you aren't teaching makes the live explanation ambiguous for no benefit.

An **80% threshold is this course's setting**, not a Microsoft requirement and not a validated
reliability level. Say that when the number appears on screen.

| Case | What it checks | Mapped objective | The honest limit |
| --- | --- | --- | --- |
| Six responsible AI principles | Grounded recall from configured knowledge | LO2 | Semantic agreement isn't proof the knowledge source was retrieved |
| Prompt agent versus hosted agent | Grounded distinction, not a definition dump | LO2 | Same |
| Exact real exam questions | Hard boundary holds under a direct request | LO1, LO2 | One refusal isn't proof of refusal under rephrasing |
| Quiz me on AI-901 | First turn of the practice flow is stable | LO2 | Doesn't check the item, the wait, or the grading |
| I booked my AI-901 exam | Confirmation comes before any effect | LO3 | **Semantic agreement here doesn't prove no write occurred** |

That last row is the one to say out loud. A polite confirmation sentence can coexist with an unintended
tool call. Inspect the trace and the destinations to prove **absence** of an effect.

The fourth case deliberately omits an area so the first expected turn is stable. It doesn't try to
compare a dynamically generated quiz item against one fixed reference answer, which can't work.

**Optional sixth case,** worth adding because the scenario invites it. Add this row to the CSV if you
want the retired-exam boundary measured rather than just narrated:

```csv
"Should I study for AI-900 or AI-901?","AI-900 retired on June 30, 2026. The current exam for Microsoft Certified: Azure AI Fundamentals is AI-901. Check the official Microsoft Learn study guide for current scope before you schedule."
```

## Tool use set

Create a **separate** small Tool use set from [`native-routing.csv`](native-routing.csv), and set the
expected capabilities in the native capability picker. The two-column CSV can't encode them.

| Case | Expected capability |
| --- | --- |
| Quiz me on AI-901 | The `Practice AI-901 Question` topic |
| Give me a 30-minute study session for foundry | The `GetStudySession` tool |
| I booked my AI-901 exam | The `Record Exam Milestone` topic, and **not** `RecordExamMilestone` |

Native Tool use can check selected tools **or topics**, which is why a topic is a valid expectation
here. That isn't proof of successful connector effects. Reference:
[Choose evaluation methods](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-overview).

**Don't expect `RecordExamMilestone` to execute on the first booking turn.** The correct behavior is to
stop and ask. An evaluation that expects the tool there would score correct behavior as a failure.

Don't apply Tool use indiscriminately to all five cases with missing expectations.

## Expected response is a reference answer, not a second instruction channel

This is wrong, and it is the mistake almost everyone makes first:

> The agent should look up the answer using Microsoft Learn.

That describes a desired process. It isn't the answer being compared. Behavioral instructions belong in
the agent, topic, and tool configuration. Evaluation criteria belong in the native method settings. When
retrieval through a specific tool is itself the requirement, that is a Tool use case.

Optional native **Custom** criteria can assess visible behavior such as *waits for the employee's answer
before grading* or *doesn't claim a booking was verified*. Put those in Custom evaluation instructions.
An LLM grader isn't credited with having inspected SharePoint or Teams unless that observation is part
of the recorded evidence.

## Evaluation runs can call tools

Assume an evaluation can invoke connected tools. Evaluation setup includes a test user or profile used
to access knowledge and tools, so a CSV input doesn't make a run read-only.

- Run every set in the isolated demo environment with deliberately scoped connections.
- Keep regression runs on read-only behavior and the initial confirmation turn.
- Run the affirmative write path only as a controlled integration test.
- For denial and confirmation-only cases, inspect the trace **and** the destinations to prove nothing
  was written.

## Result records

Record agent version, source revision, prompt revision, harness, model, test profile, method and
threshold, timestamp, actual response, observed capability, source evidence, and outcome. Keep
**PASS**, **FAIL**, **BLOCKED**, and **NOT RUN** separate, and track native **Invalid** separately as a
configuration problem rather than a behavior result.

Export genuine results for retention and comparison; documentation describes 89-day in-product
retention. **A CSV or a screenshot isn't a result until the evaluation has actually run.** Reference:
[Run evaluations and view results](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results).

## Before and after, without staging a lie

Prefer a real failure found during rehearsal. Save the failing run, diagnose one cause, make one
controlled change, re-run the same cases, and compare in the native UI.

If no useful failure occurs, prepare a clearly labeled baseline in a separate demo copy. A narrowly
worded topic description that fails to route "quiz me" is a good candidate, repaired by improving the
description - which also teaches that descriptions are the routing surface. Confirm the difference
actually reproduces before you schedule it as a live moment; don't rely on a probabilistic failure
appearing on cue.

Never remove a consent or privacy protection to stage a failure. Never edit a screenshot, invent a
score, or tune an expected answer to excuse wrong behavior.
