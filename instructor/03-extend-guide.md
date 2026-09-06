# Co-instructor guide: Extend

**LO3:** Extend the agent with actions, agent flows, MCP and subagent concepts, and human handoff patterns.

**Teaching intent:** Learners distinguish an answer from a bounded operation, then justify when a person or specialist is needed. The single action is GetStudySession. Complete the build recipe in rehearsal; live time is for reasoning and visible evidence.

**Before class:** Follow [the full flow recipe](../sample-agent/tools/core-study-session.md). Prepare one agent with the working tool and a second flow draft with just the cloud condition for explanation. Keep a real verified checkpoint ready. If no live checkpoint exists, use the recipe as a clearly labeled walkthrough and leave execution unverified. Do not present an authored fixture as captured output. Confirm standard harness, access, policies, and actual tests.

## 0-5 minutes: retrieval before explanation

**SAY:** "Our assistant can explain a concept. Now somebody wants a study session. We need to decide whether this is an answer, a missing detail, an operation, or a request for a person."

**DO:** Display the four requests from the [lab](../modules/03-extend/lab.md). Give learners 30 seconds to choose a next move, then take two explanations.

**EXPECT:** Shared responsibility is grounded explanation; missing focus needs clarification; a cloud session fits the tool; accommodation approval requires another authority.

**RECOVERY:** If everything is classified as a tool, say: "A tool should have a reason to exist. Reading a reviewed answer does not require a new integration."

## 5-10 minutes: make the boundary visible

**SAY:** "This tool has one input and two outputs. Cloud, security, or governance goes in. A status and a fixed 30-minute session come back. It doesn't save progress or book anything."

**DO:** Show [the contract](../sample-agent/tools/core-study-session.md). Open the prepared flow draft. Show the trigger focus, both String initializations, and one cloud Condition. Add or explain its two Set variable actions. Point to the one response after all conditions.

**EXPECT:** Learners see unsupported as the initial state and ok only when a supported choice matches. Explain that variables must be initialized outside the conditions.

**RECOVERY:** If adding a card consumes two minutes, switch to the completed checkpoint and inspect it. Do not teach designer troubleshooting at the expense of the tool boundary.

## 10-15 minutes: reveal and bind

**SAY:** "The other two branches repeat the same idea. We use one response after the decisions so a skipped branch cannot supply a missing output."

**DO:** Reveal the completed security and governance conditions. Show the response mapping from variable tokens and asynchronous response Off. Show the published flow. In the agent, **Tools > Add a tool > Flow > GetStudySession > Add and configure**. If already added, open its configuration.

**DO:** Inspect **Inputs > Fill using = Dynamically fill with AI**, the focus description, and **Completion > After running > Send specific response**, with status and plan output tokens. Explain why we display returned data directly for this demonstration.

**EXPECT:** Learners can point to the boundary between conversational input collection and the flow's decision.

**RECOVERY:** If no flow appears, verify environment, access, publication, and required trigger/response. Use the prepared agent checkpoint after one attempt. Document the issue for rehearsal; do not improvise a new integration.

## 15-20 minutes: predict, run, inspect

**SAY:** "Predict the result first. Now we'll look at what actually ran."

**DO:** Directly test focus=cloud, then focus=quantum. Inspect inputs and response values. In **Test your agent**, start a fresh conversation: "Give me a 30-minute cloud study session." Inspect the tool call and output. Then start fresh: "Make a study session."

**EXPECT:** cloud gives ok with the authored text. quantum gives unsupported with the choice prompt. Missing focus prompts for a choice before calling. Record actual behavior rather than grading the chat's confidence.

**RECOVERY:** If the agent answers without the tool, inspect selection metadata and instructions. Use the direct flow run to establish what is known, and label conversational binding unresolved. If the entire tenant is unavailable, compare predicted outputs from the fixture but explicitly say no call was observed.

## 20-30 minutes: extension patterns, with decisions

**SAY:** "We have one small workflow. MCP would add a standard tool interface. A second agent would add another decision-maker. Neither automatically improves this study session."

**DO:** Spend four minutes on the [taxonomy table](../sample-agent/tools/extension-decisions.md): flow and HTTP operate on a contract; MCP exposes tools/resources; child agents organize one solution; connected agents reuse separately maintained specialists. Identify A2A, Foundry, Fabric, and Microsoft 365 Agents SDK as distinct connection routes. Mention the documented preview labels without opening six setup wizards.

**DO:** Spend three minutes on identity, resource permissions, data policies, external-model approval, and least privilege. Use the Contoso public-material/employee-records example in the decision sheet.

**DO:** Spend three minutes comparing referral, request submission, and live handoff. Read the accommodation boundary response. Explain that a real transfer needs a configured receiving system and observed receipt.

**EXPECT:** Learners choose the simple flow for the current need and can describe when a specialist might earn its extra operational cost.

**RECOVERY:** For requests for detailed SDK setup, point to the referenced Microsoft Learn page and preserve the no-code learning objective. Do not substitute a diagram for a claim that a connection exists.

## 30-40 minutes: learner decision task

**SAY:** "Choose one thing this assistant should do and one thing it must leave to a person. Make the boundary specific enough that someone else could test it."

**DO:** Run the [10-minute lab](../modules/03-extend/lab.md). Call time at minutes 32, 35, and 38. Makers with the prebuilt shared flow may attach and test it; observers complete the same contract and failure predictions.

**EXPECT:** A bounded contract, a missing-input response, and an honest escalation path.

**RECOVERY:** If learners lack access, move immediately to the worksheet. No points are awarded for wrestling a license dialog.

## 40-45 minutes: debrief and failure

**SAY:** "Unsupported is a valid answer from our flow. A failed call is different. We don't get to fill the gap with a cheerful success message."

**DO:** Compare [worked answers](../modules/03-extend/worked-example.md). Present "minus five days and 500 minutes" and ask whether the current contract supports it. It does not. Explain the difference between a disabled tool and a flow that throws an error. Show a previously recorded real failure only if available and labeled with its provenance; otherwise use a clearly labeled hypothetical.

**EXPECT:** Learners preserve scope and refuse to invent execution. They name the recipient and receipt needed before claiming a real handoff.

**RECOVERY:** If someone proposes broad maker credentials to get past a denial, explain whose authority would be exposed and return to the approved environment.

## 45-50 minutes: Q&A and exit check

**SAY:** "What evidence would convince you that this assistant actually used its tool? What evidence would convince you it really reached a person?"

**DO:** Take questions. Close with the distinction between the tool response and the generated answer. Transition to Operate: "Now we turn these expectations into tests and decide whether real users should get access."

**EXPECT:** Actual invocation and returned values for the tool; destination acknowledgment for a transfer. Learners carry their worksheet forward.

**RECOVERY:** Capture unresolved product-specific questions for documentation follow-up. Do not fill uncertainty with an invented menu label.

**Break:** 10 minutes after the teaching block.

## Rehearsal sign-off

Record actual elapsed time, cloud/security/governance/quantum run evidence, missing-focus behavior, scope-refusal behavior, unavailability behavior, and recovered valid call. **All tenant execution remains NOT RUN in this repository until real evidence is supplied.** Review [source notes](../sources/research-extend.md) before recording.
