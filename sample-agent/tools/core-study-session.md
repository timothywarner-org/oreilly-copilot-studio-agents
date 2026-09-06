# GetStudySession: core no-code build recipe

**Authored course design. Documentation checked 2026-09-05 using Microsoft Learn MCP search and full-page retrieval. Tenant execution: NOT RUN.** This is a specification, not a native flow export.

**Purpose:** return one fixed, reviewed 30-minute session. The conversational model selects the tool and collects the focus; the flow selects authored text. This makes the tool boundary visible without introducing scheduling algorithms.

## Contract and design choices

| Element | Exact value | Why |
| --- | --- | --- |
| Flow/tool name | GetStudySession | Describes the bounded operation |
| Required trigger input | focus, Text | One small decision for a new maker |
| Supported focus | cloud, security, governance | No arrays, duration arithmetic, or free-form plans |
| Response outputs | status, Text; plan, Text | Caller can distinguish unsupported from success |
| Supported status | ok | Only after a matching condition |
| Default status | unsupported | Unknown values do not create a fake session |
| Default plan | Choose cloud, security, or governance. | Gives a recovery choice |
| External side effects | None | No HTTP, connector data access, storage, email, or booking |

The canonical authored texts are in [core-study-session.json](core-study-session.json). This JSON is an expected-output fixture, **not an import format**. The existing [multi-day flow design](flow-design.md) and local Node reference are **optional advanced material**, not prerequisites or proof this core flow works.

## Instructor preparation: build and test before class

Use the **standard harness** experience. [Create-flow documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create) names the route below. If your tenant shows the new experience instead, record that difference and locate the standard route during rehearsal; do not translate UI labels live by guesswork.

1. In Copilot Studio select **Flows > New flow > Agent flow**. Name it **GetStudySession**. Keep **When an agent calls the flow** and **Respond to the agent**.
2. Select the trigger card. Add one **Text** input named **focus**. Its description should read: "One study area: cloud, security, or governance. Obtain a choice if missing."
3. Between trigger and response, use **Insert a new action**, search **Initialize variable**, and add two separate initialization actions at the top level:
   - **status**, type **String**, value **unsupported**.
   - **plan**, type **String**, value **Choose cloud, security, or governance.**
4. Below both initializations, insert a **Condition**. Use the trigger's **focus** dynamic-content token in the left field, equality comparison, and literal **cloud** in the right field. Do not type the word focus as the compared value.
5. In the condition's true/**If yes** branch add **Set variable** for plan with the cloud text below, then **Set variable** for status with **ok**. Leave the false/**If no** branch empty.
6. After that condition at the same outer level, add a second condition for **security** with its matching plan and ok status. Add a third outer-level condition for **governance** with its matching plan and ok status. Each compares the same input against a different allowed value; a normal input can match only one. Do not nest variable initialization or reference outputs from skipped branches.
7. Keep **one Respond to the agent** after all three conditions. Add two **Text** outputs, **status** and **plan**. Set each output using the corresponding **variable token**, not the literal variable name. Do not place a response inside each condition.
8. In **Respond to the agent > Settings > Networking**, verify **Asynchronous response = Off**. The response must complete within the documented 100-second limit.
9. Open **Flow checker**, correct errors, then **Publish**. Publishing the flow makes it eligible as an agent tool; it does not publish the agent to a user channel.
10. Use **Test > Manually**, supply each test input, then run the flow. Inspect action inputs and response outputs. Save the actual run references privately. A successful flow-checker result establishes valid structure, not correct behavior.

**Why three conditions:** This course adapts the documented cloud-flow Condition and Variable controls. The repeated comparison is easy to narrate and avoids nested logic. It is a deliberate small teaching design, not Microsoft's prescribed sample. [Designer](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-designer), [conditions](https://learn.microsoft.com/en-us/power-automate/add-condition), [variables](https://learn.microsoft.com/en-us/power-automate/create-variable-store-values).

## Copy-ready plan values

### cloud

Cloud study session, 30 minutes. Minutes 0-10: Read the cloud concepts section of the current AZ-900 study guide. Minutes 10-20: Explain shared responsibility for infrastructure, platform, and software services using a Contoso example. Minutes 20-25: Without notes, name one responsibility the customer keeps in every service model. Minutes 25-30: Check your explanation against Microsoft Learn and write one question for your mentor.

### security

Security study session, 30 minutes. Minutes 0-10: Read the identity, access, and security material linked from the current AZ-900 study guide. Minutes 10-20: Explain authentication and authorization using a WoodGrove Bank employee example. Minutes 20-25: Without notes, explain why signing in does not grant every permission. Minutes 25-30: Check your explanation against Microsoft Learn and write one question for your mentor.

### governance

Governance study session, 30 minutes. Minutes 0-10: Read the management and governance material linked from the current AZ-900 study guide. Minutes 10-20: Explain Azure Policy and resource locks using a Tailwind Traders example. Minutes 20-25: Without notes, explain why a resource lock and an access permission solve different problems. Minutes 25-30: Check your explanation against Microsoft Learn and write one question for your mentor.

**Subject authority:** use the [current AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900). These are original study activities, not official exam items or promises of certification readiness.

## Add and configure the agent tool

1. Select **Agents > your agent > Tools > Add a tool > Flow**.
2. Select **GetStudySession > Add and configure**. If it is missing, verify the environment, access, published state, and required trigger/response.
3. Set **Name** to **GetStudySession** and **Description** to: "Retrieve an authored 30-minute AZ-900 study session for cloud, security, or governance. Use only when a user wants one of these fixed sessions. Collect the focus first. This tool cannot customize duration, create a multi-day plan, register for exams, or contact people."
4. Under **Inputs**, keep **Fill using = Dynamically fill with AI** for focus. Use **Customize** to set its description to the trigger description above. Automatic filling is convenient, not authorization or foolproof validation.
5. Under **Completion > After running**, choose **Send specific response**. Insert the **status** and **plan** output variables using the variable picker. Template: "Study session result: [insert status token]. [insert plan token]." The bracketed phrases describe picker actions; do not paste them as literal placeholders.
6. Save and use **Test your agent**. Inspect the actual invocation, focus, and returned status/plan, not just the chat response.
7. Test missing focus and check it requests a choice. Test an unrelated duration and check it explains the limit before offering a fixed session. Revise descriptions/instructions if the model silently widens the contract.

The exact input and completion labels come from [tool configuration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent); the add-flow route comes from [call an agent flow](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-flow).

## Expected cases and honest recovery

| Test | Expected behavior | Evidence to inspect |
| --- | --- | --- |
| Direct flow: cloud, security, governance separately | ok plus exact matching authored text | Trigger input, selected branch, response outputs |
| Direct flow: quantum | unsupported plus choice prompt | All conditions false, initialized defaults returned |
| Chat: "Make a study session" | Clarify focus before calling | No invented focus; then correct call after user answers |
| Direct trigger: omitted/null focus | May be rejected as invalid input; not guaranteed to reach conditions | Trigger validation or real failure details |
| Chat: "Make it minus five days and 500 minutes" | Explain fixed 30-minute scope; do not claim requested customization | Honest limitation and supported offer |
| Tool unavailable or flow errors | No fabricated result; truthful failure or unavailability | Actual error/state, never synthetic ok |
| Chat: "Register me for the exam" | Explain boundary and direct to official process | No booking, transfer, or confirmation claim |

**Failure handling:** unsupported is a valid response from a completed flow. Runtime failure is different. This minimal flow has no catch-all that converts errors to success. Inspect the real error, correct configuration, and retest. If testing an unavailable tool, turn **Enabled** off in this teaching agent, save, test, then restore it and retest. This demonstrates unavailability, **not** a flow-runtime exception. Do not pretend a disabled-tool test proves handling of every connector failure.

**Sample recovery wording:** "I couldn't retrieve the study session. I haven't created or saved anything. You can retry or use the written course activity." This is an authored response expectation, not a claim that platform errors automatically use these words.

**Rehearsal record:** date, harness, flow published state, valid/unsupported outputs, missing-focus behavior, unavailable-tool behavior, recovered valid run. Keep every unperformed case **NOT RUN**.
