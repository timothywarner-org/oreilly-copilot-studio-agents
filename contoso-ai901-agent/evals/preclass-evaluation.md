# One-time preclass evaluation

**Scheduled target: September 8, 2026, 6:00 AM Central, once.** The instructor's Power Automate
flow uses a manually queued run followed by **Delay until** `2026-09-08T11:00:00Z`. It has no
recurrence. The private handoff contains the actual queued run and maker links. Tomorrow's outcome
cannot be claimed before the run happens.

## The sequence to inspect in the designer

1. **Manually trigger a flow.** Start it once during preparation.
2. **Delay until** the UTC timestamp above.
3. **Evaluate Agent** with **Contoso AI-901 - Core Five** and the connected evaluation profile.
4. **Get Agent Test Run Details** inside **Do until**, pausing 30 seconds between checks. Continue
   only after the state is Completed. A failed run or a one-hour polling limit stops the sequence.
5. Repeat for **Contoso AI-901 - Knowledge and Challenge**, then **Contoso AI-901 - Routing**.
6. Inspect the saved result objects in the flow and the individual responses in Copilot Studio Evaluation.

Only one evaluation can run at a time. The sequence waits for actual completion rather than assuming
an evaluation has finished after a fixed delay. The connector pattern is documented in
[Trigger agent evaluations with connectors](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-automate-tools)
and the [Microsoft Copilot Studio connector reference](https://learn.microsoft.com/en-us/connectors/microsoftcopilotstudio/),
verified September 7, 2026.

## What the two success signals mean

| Signal | Meaning |
| --- | --- |
| Power Automate run succeeded | All three evaluation jobs completed and their results were captured |
| An evaluation case passed | That case met its configured method and threshold |
| A SharePoint row and Teams message exist | Separate integration evidence of the intended effects |

A successful runner can contain failed evaluation cases. **A completed test is not a passing test.**
Core Five and Knowledge and Challenge use Compare meaning at the course's 80% threshold. Routing
uses Tool use with actual topic/tool expectations. None of these initial-turn cases confirms a write;
inspect the signup list to verify no extra rows were created.

The same-case rehearsal preserved the original reference answers and threshold. Making all three
practice-area choices explicit in the opening question changed that case's score from 50 to 100.
Other generated answers and grades varied between runs. Use the
[dated rehearsal](../tenant-rehearsal-2026-09-07.md) for the observed results and their limits.
