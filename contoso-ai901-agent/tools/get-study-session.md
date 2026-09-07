# GetStudySession - AI-901 focus swap

**You are editing three Set variable actions, not rebuilding a flow.** The flow shape from
[`../../contoso-ai901-agent/tools/get-study-session.md`](../../contoso-ai901-agent/tools/get-study-session.md) is
unchanged: one Text input, two initialized variables, three flat conditions, one Respond to the agent.
Only the compared values and the plan text change. Budget four minutes, not forty.

**Authored design. Documentation checked 2026-09-06. Tenant execution: NOT RUN.**

## What changes

| Element | AI-901 build | AI-901 build |
| --- | --- | --- |
| Compared values | `cloud`, `security`, `governance` | `responsible-ai`, `workloads`, `foundry` |
| Plan text | AI-901 activities | The three blocks below |
| Default plan | Choose cloud, security, or governance. | Choose responsible-ai, workloads, or foundry. |
| Tool description | AI-901 wording | The description below |
| Flow name, inputs, outputs, statuses, condition count | unchanged | unchanged |

Keeping the flow name `GetStudySession` means the instructor guides, the evaluation cases, and the
extension-decision material all still line up. Renaming it two days before delivery buys nothing.

## Contract

| Element | Exact value |
| --- | --- |
| Flow/tool name | GetStudySession |
| Required trigger input | focus, Text |
| Supported focus | responsible-ai, workloads, foundry |
| Response outputs | status, Text; plan, Text |
| Supported status | ok |
| Default status | unsupported |
| Default plan | Choose responsible-ai, workloads, or foundry. |
| External side effects | None |

The canonical text lives in [`get-study-session.json`](get-study-session.json). That JSON is an
expected-output fixture, not an import format.

## Edit procedure

1. Open the existing **GetStudySession** agent flow.
2. In the trigger card, update the **focus** input description to: "One study area: responsible-ai,
   workloads, or foundry. Obtain a choice if missing."
3. Update the **plan** initialization value to `Choose responsible-ai, workloads, or foundry.`
   Leave the **status** initialization at `unsupported`.
4. In each of the three flat conditions, change the compared literal and the **Set variable** plan text
   to the matching block below. Keep the conditions flat at the outer level; don't nest them, and don't add a second Respond to the agent.
5. Confirm **Respond to the agent > Settings > Networking > Asynchronous response = Off**. The response
   must complete inside the documented synchronous limit. Reference:
   [Create an agent flow as a tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create).
6. Run **Flow checker**, then **Publish**. Publishing the flow makes it eligible as a tool. It doesn't
   publish the agent to a channel.
7. **Test > Manually** with each of the three values and with `quantum`. Inspect the branch taken and
   the response outputs, not just the chat text.

## Tool description to paste

> Retrieve an authored 30-minute AI-901 study session for responsible-ai, workloads, or foundry. Use
> only when an employee wants one of these fixed sessions. Collect the focus first. This tool can't
> customize the duration, build a multi-day plan, register for exams, or contact people.

Keep **Fill using = Dynamically fill with AI** for `focus`, and set its description to the trigger
description from step 2. Automatic filling is convenient. It isn't validation and it isn't authorization.

## Copy-ready plan values

### responsible-ai

Responsible AI study session, 30 minutes. Minutes 0-10: Read the responsible AI section of the current AI-901 study guide and name all six principles without looking. Minutes 10-20: For a Contoso hiring-model example, write one concrete failure for fairness and one for accountability, and explain why they are different failures. Minutes 20-25: Without notes, explain the difference between transparency and accountability in two sentences. Minutes 25-30: Check your explanation against Microsoft Learn and write one question for your mentor.

### workloads

AI workloads study session, 30 minutes. Minutes 0-10: Read the AI workloads section of the current AI-901 study guide and list the workload shapes it names. Minutes 10-20: Sort five Contoso requests into workload shapes, including scanned expense receipts, a call-centre transcript, and a product photo, and say which service family each one points to. Minutes 20-25: Without notes, tell keyword extraction, entity detection, sentiment analysis, and summarization apart in one sentence each. Minutes 25-30: Check your answers against Microsoft Learn and write one question for your mentor.

### foundry

Microsoft Foundry study session, 30 minutes. Minutes 0-10: Read the Foundry section of the current AI-901 study guide and the Foundry agents overview. Minutes 10-20: Open the Foundry portal and inspect one prompt agent's instructions, model, and attached tools without changing anything. Minutes 20-25: Without notes, explain when a Contoso team should build a hosted agent rather than a prompt agent. Minutes 25-30: Check your explanation against Microsoft Learn and write one question for your mentor.

**Subject authority:** the [current AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901).
These are original study activities, not official exam items and not a promise of certification readiness.

## Expected cases

| Test | Expected behavior | Evidence to inspect |
| --- | --- | --- |
| Flow test: each of the three values | `ok` plus the exact matching text above | Trigger input, branch taken, response outputs |
| Flow test: `quantum` | `unsupported` plus the choice prompt | All conditions false; initialized defaults returned |
| Chat: "Give me a study session" | Clarifies the focus before calling | No invented focus, then a correct call |
| Chat: "Make it 90 minutes over three days" | Explains the fixed 30-minute scope | Honest limitation plus a supported offer |
| Chat: "cloud" | `unsupported`, because the AI-901 values are gone | Proof the swap actually took effect |
| Tool disabled | Truthful unavailability, never a synthetic `ok` | Actual state |

The `cloud` case is worth one deliberate run. It proves the edit landed, and it catches the failure
mode where a stale published version is still bound to the agent.

**Don't claim a runtime-exception test from a disabled-tool test.** Turning a tool off demonstrates
unavailability. It says nothing about how the agent handles a connector throwing at runtime.
