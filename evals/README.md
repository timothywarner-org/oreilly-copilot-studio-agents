# Agent evaluation scenarios

**These cases have not been run against an agent.** Local unit tests check the optional reference
function and repository consistency. They cannot establish Copilot Studio behavior.

[Case definitions](cases.json) describe 12 original scenarios mapped to the four outcomes.
[The result template](results.template.json) starts with every case **NOT RUN**.
This is a portable review format, not a native Copilot Studio import schema.

## Run the cases

1. Copy the result template to `.local/agent-results.json`, or run `npm run eval:template`.
2. Execute each case using the actual configured agent. Inspect citations and tool results.
3. Record PASS, FAIL, BLOCKED, or NOT RUN. Keep expected behavior separate from observed behavior.
4. Fix a failing configuration, then rerun that case and relevant regressions.
5. Report counts and hard-boundary failures explicitly. Never hide unexecuted cases in an overall score.

Suggested rehearsal criterion: no hard-boundary failure among executed cases, plus explicit ownership
of every blocked/unexecuted check before a pilot decision. This is a course design criterion,
not a guarantee of safety or production readiness.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro
