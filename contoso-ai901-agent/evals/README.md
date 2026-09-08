# Native evaluation examples

**These CSVs contain authored expected responses, not scores or passing agent outputs.** The course
uses separate sets so you can tell which question each evaluation method answers.

| File | Cases | Intended check |
| --- | --- | --- |
| [Core five](native-core-five.csv) | 5 | Compare meaning: concept answers, refusal, practice opener, signup confirmation |
| [Routing](native-routing.csv) | 3 | Tool use: expected practice topic, GetStudySession, and signup topic |
| [Knowledge and challenge](ai901-challenge.csv) | 32 | Compare meaning: AI-901 scope and fictional Contoso policy |

## Configure and inspect

1. Follow [Microsoft's single-response procedure](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create)
   and compare the downloaded template with the supplied CSV. The documented first two headings are
   `Question` and `Expected response`.
2. Review each reference answer. Configure **Compare meaning** for the answer sets. The course uses
   an 80% threshold as a teaching choice, not a Microsoft requirement or a reliability guarantee.
3. Configure **Tool use** separately for the routing set. Select actual capabilities in the native UI:
   **Practice AI-901 Question**, **GetStudySession**, and **Record AI-901 Certification Signup**.
4. Inspect the test identity and connections. Run sets sequentially and review expected versus actual
   responses, errors, and activity evidence. Keep sensitive exports in a private location.
5. Compare the same cases before and after one change. Report each method's counts separately.

The CSV does not configure expected tools. Signup's first turn should reach the confirmation topic,
then wait. Expecting the writing flow on that turn would reward incorrect behavior.

## Checks that need more evidence

- Test the fixed RAI topic interactively with A and B. It has four choices; the generated practice
  topic is a separate three-choice example. Inspect the wait point, variables, feedback, and ending.
- Decline a signup and inspect for no new row or post. A refusal sentence alone is insufficient.
- After a practice answer, request a signup and verify that a previous answer is not reused as consent.
- For a confirmed signup, inspect the saved row and the separate Teams notification result.
- Inspect actual source citations for scope and fictional-policy claims. A meaning score does not
  prove retrieval, correct attribution, or absence of an unauthorized action.

The instructor loaded these sets on September 7. Those historical runs included failures. The
September 8 destination change updated affected references to **General** in **Contoso Ltd Community**;
the sets were not rerun as part of that change. No current pass rate is claimed here.

[Choose methods](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-overview) · [Review results](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results)
