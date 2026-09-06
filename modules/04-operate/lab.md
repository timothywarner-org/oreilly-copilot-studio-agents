# Operate lab

**Target:** LO4. **Artifact:** [worksheet.md](worksheet.md).

These steps operationalize the approved activity. They are newly authored guidance, not proof that the
workflow has been run in your tenant. Never bypass tenant policy to complete an exercise.

## Steps

1. Read the 12 evaluation scenarios. Copy the result template to a private local working location and leave every case NOT RUN until executed.
2. For the maker route, implement the cases in the current supported native evaluation experience or execute them manually with recorded evidence. The repository JSON is not a native import promise.
3. Run the cases against the actual configured agent. Record observed responses, inspected sources, and failures separately from expected behavior.
4. Use native activity/analytics/transcript views where available. Label historical or sanitized evidence accurately; do not assume test-panel traffic is equivalent to production-channel analytics.
5. Review permissions, data policy, environment isolation, data boundaries, selected model, and publishing entitlement. Identify the intended channel and real audience.
6. Apply the five Well-Architected concerns to this assistant. Record one risk or concrete control for each in the worksheet.
7. Choose GO, CONDITIONAL, or NO-GO for a small pilot. State the evidence, unexecuted checks, owner, rollback route, and one safe next step.

## Checkpoint

A reader can distinguish actual results, remaining risks, and the reason for the pilot decision. No production-readiness claim is inferred from the scaffold.

## Recovery

Without working tenant access, complete the worksheet using a diagram and predicted behavior.
Label predicted responses **PREDICTED**. Leave execution results **NOT RUN**.
Do not publish personal data or screenshots containing identities or secrets.

## Optional stretch

Change one assumption in your worksheet, then explain which downstream module or evaluation case must change.
Do not add a new platform, production connector, or unrelated scenario.
