# Extend lab

**Target:** LO3. **Artifact:** [worksheet.md](worksheet.md).

These steps operationalize the approved activity. They are newly authored guidance, not proof that the
workflow has been run in your tenant. Never bypass tenant policy to complete an exercise.

## Steps

1. Read the study-plan contract and flow design. Identify every input and confirm that the tool has no external side effects.
2. Predict the output for the three-day example. Decide how the agent should handle missing days, negative minutes, or an unsupported focus code.
3. For the maker route, implement the bounded agent flow in an approved environment and bind it to the agent. Follow the flow-design sequence; record the actual binding privately.
4. Test a valid plan and an invalid request. Inspect returned data. A generated sentence about success is not tool execution evidence.
5. Compare actions, agent flows, HTTP, MCP, and delegation using extension-decisions.md. Choose one real approved MCP capability only when available; do not expose unrelated tools.
6. Test an exam-registration request. The sample tool cannot register anyone. Require a truthful boundary and an actual configured handoff or an honest limitation.
7. Use the optional Node reference demo only as a contract oracle or declared offline fallback. Never relabel its output as a Copilot Studio execution.

## Checkpoint

You can distinguish a narrative answer, a validated tool result, a blocked action, and a real human handoff.

## Recovery

Without working tenant access, complete the worksheet using a diagram and predicted behavior.
Label predicted responses **PREDICTED**. Leave execution results **NOT RUN**.
Do not publish personal data or screenshots containing identities or secrets.

## Optional stretch

Change one assumption in your worksheet, then explain which downstream module or evaluation case must change.
Do not add a new platform, production connector, or unrelated scenario.
