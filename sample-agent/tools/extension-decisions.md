# Explain the extension choices without starting another course

Use the assistant’s next job to choose a mechanism. This is an instructional comparison drawn from
the proposal, not a guarantee that each mechanism is enabled in every tenant.

| Mechanism | Teaching decision | Boundary to demonstrate |
| --- | --- | --- |
| Topic | The interaction needs an explicit teaching sequence or a clarification. | A conversation branch is not a completed external action. |
| Action/tool | A named, bounded capability must return an inspectable result. | Validate inputs; inspect success and failure. |
| Agent flow | The steps should follow a deterministic workflow. | Explain exactly what side effects exist; the sample plan has none. |
| HTTP tool | A separately hosted API capability is appropriate and authorized. | Authentication, endpoint ownership, data policy, and response schema. |
| MCP | Expose an approved provider’s tools through the protocol. | Protocol support does not imply every exposed tool is safe or authorized. |
| Child/connected agent | Delegate to a scoped specialist rather than making the main assistant do everything. | Scope, identity, data flow, result validation, and return control. |
| A2A / Foundry / Fabric / M365 SDK connection | Situate other agent technologies named in the proposal. | Confirm current support separately; no cross-platform build required today. |
| Human handoff | Evidence or authority is insufficient. | Use a real route or state clearly that none is configured. |

Mini-exercise: choose one tool this assistant should call and one request that must escalate.
Explain why a normal source lookup, a deterministic plan, and an exam-registration request require
different decisions.

Product reference: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp
