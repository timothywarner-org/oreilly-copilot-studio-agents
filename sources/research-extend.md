# Extend research record

**Checked:** 2026-09-05. **Method:** Microsoft Learn MCP search, followed by full-page fetch for the pages below. Documentation establishes a supported design; it does not establish behavior in Tim's tenant.

| Microsoft source | Confirmed basis | Course application |
| --- | --- | --- |
| [Create an agent flow](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create) | Standard harness; required trigger/response; real-time response; publishing | Core creation sequence |
| [Call an agent flow](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-flow) | Add published flow through Tools; inputs/completion; test agent | Bind and verify |
| [Agent flow as tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-agent) | Agent-level and topic-level use; 100-second response requirement | One bounded operation |
| [Flow designer](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-designer) | Insert action, parameter cards, Flow checker, Publish, manual Test | Rehearsal procedure |
| [Cloud flow conditions](https://learn.microsoft.com/en-us/power-automate/add-condition) | Dynamic-content comparison and true/false branches | Three mutually exclusive conditions |
| [Cloud flow variables](https://learn.microsoft.com/en-us/power-automate/create-variable-store-values) | Initialize at global level; String supported; Set variable; variable values | Two variables, one response outside branches |
| [Tool configuration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent) | Dynamically fill with AI, Customize, Custom value, Send specific response, output picker, Enabled toggle | Exact configuration and unavailability test |
| [MCP extension](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp) | Current tools/resources support, generative orchestration requirement, dynamic server definitions | Recognition-level comparison |
| [MCP server authentication](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-create-new-server) | API-key and OAuth patterns | Authentication does not imply unlimited authority |
| [Other agents overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-add-other-agents) | Child/connected/external taxonomy; preview notices; governance and latency costs | One comparison instead of multiple builds |
| [Data policies](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) | Connector grouping, HTTP/channel controls; connector blocking affects MCP | Concrete policy boundary |
| [External models](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-external-response-model) | Power Platform plus Microsoft 365 admin controls; preview is separate from external | Keep approved model; discuss review responsibilities |
| [Generic human handoff](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-generic-handoff) | Engagement hub and adapter needed; channel-specific limitations | Referral is not live transfer |

**Authored design, not Microsoft prescription:** GetStudySession, the three focus codes, fixed 30-minute study activities, status/plan names, repeated conditions, classroom timing, worked learner answers, and failure wording. These are intentionally small adaptations of the documented primitives.

**Why not Switch:** A Condition route is directly documented for Power Automate cloud flows and uses the standard designer's action insertion. We avoid relying on desktop-flow Switch documentation for a cloud-flow recipe. The resulting three comparisons are simple enough to inspect in one screen.

**Recheck before delivery:** Actual harness, labels, flow field type picker, tenant availability and permissions, preview states, model approvals, channel handoff limitations, and actual runtime behavior. Documentation is mutable. Nothing here is a recorded deployment, native export, or live evaluation result.
