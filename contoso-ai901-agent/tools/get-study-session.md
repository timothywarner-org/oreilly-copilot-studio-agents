# GetStudySession: one fixed study activity

**Purpose:** Learn a tool's input/output contract using a flow that returns authored text and makes
no external writes. The three focus values are teaching shortcuts, not official exam-domain names.

| Contract element | Value |
| --- | --- |
| Tool | GetStudySession |
| Required input | focus, Text |
| Supported values | responsible-ai, workloads, foundry |
| Outputs | status, Text; plan, Text |
| Supported result | ok and the matching 30-minute plan |
| Unsupported result | unsupported and Choose responsible-ai, workloads, or foundry. |

The [JSON fixture](get-study-session.json) supplies expected values for inspection. It is not a flow import.

## Optional flow walkthrough

1. Create an agent flow with **When an agent calls the flow** and **Respond to the agent**, following
   [Microsoft's flow guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create).
2. Add the required Text input **focus**. Describe its three allowed values and the need to collect a missing choice.
3. Initialize two String variables: **sessionStatus** = `unsupported` and **sessionPlan** =
   `Choose responsible-ai, workloads, or foundry.`. These defaults make unsupported input explicit.
4. Add three sequential conditions comparing focus with each supported value. In each Yes branch,
   set sessionStatus to `ok` and sessionPlan to its exact text below. Leave the No branches empty.
5. In the single response action, return Text outputs **status** and **plan**, mapped to those variables.
   Keep the response synchronous. Publish the flow, then add the actual flow as the agent's tool.
6. Test each supported focus and `quantum` directly. Inspect the input, branch, and response outputs.
7. In agent chat, test a supplied focus and then a missing one. Verify the actual tool call and returned text.

**Suggested tool description:** Return one fixed 30-minute AI-901 study session for responsible-ai,
workloads, or foundry. Collect a missing focus. Explain the limit for custom durations or multi-day plans.
This flow cannot book an exam, store progress, or contact anyone.

## Authored plan values

### responsible-ai

Responsible AI study session, 30 minutes. Minutes 0-10: Read the responsible AI section of the current AI-901 study guide and name all six principles without looking. Minutes 10-20: For a Contoso hiring-model example, write one concrete failure for fairness and one for accountability, and explain why they are different failures. Minutes 20-25: Without notes, explain the difference between transparency and accountability in two sentences. Minutes 25-30: Check your explanation against Microsoft Learn and write one question for your mentor.

### workloads

AI workloads study session, 30 minutes. Minutes 0-10: Read the AI workloads section of the current AI-901 study guide and list the workload shapes it names. Minutes 10-20: Sort five Contoso requests into workload shapes, including scanned expense receipts, a call-centre transcript, and a product photo, and say which service family each one points to. Minutes 20-25: Without notes, tell keyword extraction, entity detection, sentiment analysis, and summarization apart in one sentence each. Minutes 25-30: Check your answers against Microsoft Learn and write one question for your mentor.

### foundry

Microsoft Foundry study session, 30 minutes. Minutes 0-10: Read the Foundry section of the current AI-901 study guide and the Foundry agents overview. Minutes 10-20: Open the Foundry portal and inspect one prompt agent's instructions, model, and attached tools without changing anything. Minutes 20-25: Without notes, explain when a Contoso team should build a hosted agent rather than a prompt agent. Minutes 25-30: Check your explanation against Microsoft Learn and write one question for your mentor.

The Foundry activity is optional practice for someone with approved Foundry access. Class participants
can inspect the instructor's example without signing in. These are original activities, not official
exam questions or a guarantee of certification readiness.

## Check the boundary

| Test | Expected evidence |
| --- | --- |
| Each supported direct flow input | status=ok and the exact matching plan |
| Direct flow input quantum | status=unsupported and the choice prompt |
| Chat request without focus | Collect a choice before calling |
| A request for 90 minutes or seven days | Explain the fixed 30-minute limit |
| Tool unavailable | State the failure without inventing a successful result |

The instructor tested the supported values, missing focus, and unsupported focus on September 7.
A broader-duration request still needed clearer limitation wording in that rehearsal. Treat that as a
test to perform, not a passed capability. A disabled-tool test also does not establish how runtime
exceptions are handled.

[AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)
