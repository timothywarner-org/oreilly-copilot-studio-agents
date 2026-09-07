# Extension decisions: the smallest sufficient capability

**Documentation checked 2026-09-05.** These are authored comparisons grounded in [Microsoft Learn research](../../sources/research-extend.md). They are discussion patterns, not configured integrations.

## First decide what the user needs

| User need | Next move | Course example |
| --- | --- | --- |
| Explanation from trusted material | Answer with grounding | Explain shared responsibility |
| Required information is missing | Clarify | Which study focus? |
| A bounded operation has a reviewed contract | Call the tool | GetStudySession |
| Authority, personal judgment, or an unavailable capability is required | Refer/escalate honestly | Exam accommodation decision |

**A tool result is evidence of an operation only when you inspect the actual call.** A generated "done" message proves very little.

## Tool and agent taxonomy

| Pattern | What it adds | When it earns its complexity | Our decision |
| --- | --- | --- | --- |
| Action/tool | A capability the agent can invoke | The request requires a specific operation | One bounded study-session tool |
| Agent flow | A visual sequence of actions and rules | Repeated workflow logic belongs outside prose | Core demonstration |
| HTTP/REST tool | A request to an endpoint using a defined API contract | An approved service already exposes the operation | Compare only; no endpoint needed for fixed text |
| MCP | Standard discovery and use of server-described tools/resources | Multiple agents need a governed tool interface | Compare only; a server is unnecessary for this local decision |
| Child agent | Specialized instructions, tools, and knowledge within the main agent | One team needs logical separation without independent publishing | Unnecessary for three focus choices |
| Connected Copilot Studio agent | A separately maintained agent in the environment | Another team owns a reusable capability and separate lifecycle | Future mentor-service example, not a human transfer |
| A2A | Protocol-based connection to another agent | Another agent exposes a compatible endpoint | Recognition-level concept, not a new lab |
| Microsoft Foundry agent connection | Reuse an agent built in Foundry | A team already owns an appropriate specialist | Discuss dependency and test boundary |
| Fabric data agent connection | Delegate questions to a data specialist | Governed organizational analytics are required | Not needed for public AI-901 study topics |
| Microsoft 365 Agents SDK connection | Reuse a programmatically built agent | A developer-owned agent is already available | No SDK installation or coding in the learner route |

**Version-sensitive facts:** Microsoft's add-other-agents overview currently labels the Foundry, Fabric, and Microsoft 365 Agents SDK connections preview. Child agents are not independently deployed services. Connected-agent solutions add orchestration hops and testing/governance work. Check current docs before naming a feature's availability. [Source](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-add-other-agents)

**MCP distinction:** The protocol defines tools, resources, and prompts; the reviewed Copilot Studio page states support for **tools and resources**. Generative orchestration is required. Server changes can change the exposed capability set, so review more than the initial connection. MCP does not prove that a tool is safe, authorized, or read-only. [Source](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp)

## Make security concrete

| Question | Core flow answer | Extension review |
| --- | --- | --- |
| Whose identity executes? | Verify the actual agent/flow configuration | Prefer user authority where supported; maker-provided connections can expose shared authority |
| What can it touch? | Only focus and authored text, no external system actions | Limit operations and resource permissions to the task |
| Which policies apply? | Stay in the approved environment | Data policies can block connectors, HTTP, channels, and MCP access through connectors |
| What data crosses a boundary? | No personal study records are required | Review destination, retention, and minimum necessary context |
| Who approves model use? | Keep the approved model selected for the course | External-model use needs appropriate Power Platform and Microsoft 365 admin settings; external and preview are different categories |
| What proves a claim? | Actual returned status/plan | Call record, permitted result, and operation-specific receipt |

Sources: [tool authentication](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent), [data policies](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention), [external models](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-external-response-model), [MCP authentication](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-create-new-server).

**Worked decision:** Contoso wants an MCP server that exposes both public study material and employee performance records. The study assistant needs the first capability only. Do not grant the whole service's data access because the connection succeeds. Constrain the exposed tools and enforce the caller's permissions in the service; test an unauthorized request. If the required controls are unavailable, do not connect it.

## Human handoff is a separate design

**Referral:** Explain the limit and tell the learner where to seek help. Our course uses this honest pattern.

**Request submission:** An approved tool sends a minimal, consented summary to a named destination and returns a receipt. This is not live chat transfer.

**Live handoff:** A configured engagement hub routes the conversation to an available person with appropriate context. Generic integration requires an adapter and channel-specific work. A line of agent instructions cannot implement that infrastructure. [Source](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-generic-handoff)

**Worked response:** "I can't approve an exam accommodation or transfer you to support here. Use the official exam accommodations process. I can help summarize the question without sensitive medical details."

**Before adding real handoff:** Name the recipient, obtain appropriate consent, minimize context, define unavailable-person behavior, and verify receipt. Never announce "I've notified your mentor" without an actual successful operation.
