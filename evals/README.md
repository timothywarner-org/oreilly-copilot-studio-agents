# Agent evaluation scenarios

**These cases have not been run against an agent.** Local unit tests check the optional reference
function and repository consistency. They cannot establish Copilot Studio behavior.

[Case definitions](cases.json) describe 12 original scenarios mapped to the four outcomes.
[The result template](results.template.json) starts with every case **NOT RUN**.
This is a portable review format, not a native Copilot Studio import schema.

For the documented native single-response route, [native-live-three.csv](native-live-three.csv) uses Microsoft's `Question` and `Expected response` columns. It contains authored reference responses for E04, E05 and E08 and has **not been imported or run in the tenant**. Compare the actual downloaded template before import. Create `AI901-live-three` with **Compare meaning only**, using the authored 80% threshold. Create a separate `AI901-tool-one` from [native-tool-one.csv](native-tool-one.csv), with **Tool use only** and the actual GetStudySession capability selected in the native UI. Remove General quality if added by default. The CSV does not carry capability metadata. Missing per-case Tool use expectations produce Invalid, so do not add that method to the three-case set and leave E04/E05 blank. [Method configuration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-overview#tool-use).

Inspect E05's topic trace, waiting and feedback manually; semantic similarity to a reference question does not establish a correct conversation. Inspect E08 parameters and output even when Tool use passes. References are grading aids, not observed results. [Documented CSV format](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create).

| Prepared set | Cases | Sole method | Additional native configuration |
| --- | --- | --- | --- |
| AI901-live-three | E04, E05, E08 | Compare meaning, authored 80% threshold | Review expected answer for all three |
| AI901-tool-one | E08 | Tool use | Select real GetStudySession capability for E08 |

Rehearse both sets, then rerun only the one-case set live while reviewing a genuine prepared same-set semantic comparison. Evaluations run sequentially. Report each set separately; do not combine their method pass rates into a claim that all twelve scenarios passed. A repeated E08 in two sets is still one scenario with two checks.

The core tool cases target **GetStudySession**, not the optional multi-day Node reference. Run E04, E05 and E08 as the compact native live subset after the full rehearsal; use E09 interactively if time permits. E05 also requires the authored topic trace and a separate manual feedback conversation. E07 and E11 user prompts do not establish actual retrieval injection or runtime failure handling. Those require separate controlled variants if you choose to test them. The core recipe supplies a safe tool-unavailability test, which is distinct from a runtime exception. Record every variant separately.

## Run the cases

1. Copy the result template to a private local working file. Only when using the full source repository, you may instead run `npm run eval:template`; the learner package does not include the Node tooling.
2. Execute each case using the actual configured agent. Inspect citations and tool results.
3. Record PASS, FAIL, BLOCKED, or NOT RUN. Keep expected behavior separate from observed behavior.
4. Fix a failing configuration, then rerun that case and relevant regressions.
5. Report counts and hard-boundary failures explicitly. Never hide unexecuted cases in an overall score.

Suggested rehearsal criterion: no hard-boundary failure among executed cases, plus explicit ownership
of every blocked/unexecuted check before a pilot decision. This is a course design criterion,
not a guarantee of safety or production readiness.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro
