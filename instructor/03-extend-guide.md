# Co-instructor guide: Extend

**LO3:** Extend the agent with actions, agent flows, MCP and subagent concepts, and human handoff patterns.

**Teaching intent:** Learners distinguish an answer from a bounded operation, then justify when a person or specialist is needed. The single action is GetStudySession. Complete the build recipe in rehearsal; live time is for reasoning and visible evidence.

**Audience anchor:** Contoso's internal training team is the maker; colleagues studying Azure fundamentals are the assistant's users. Keep every comparison tied to that job. Learners need to choose a suitable extension, not memorize a product catalog.

**Before class:** Follow [the full flow recipe](../sample-agent/tools/core-study-session.md). Prepare one agent with the working tool and a second flow draft with just the cloud condition for explanation. Keep a real verified checkpoint ready. If no live checkpoint exists, use the recipe as a clearly labeled walkthrough and leave execution unverified. Do not present an authored fixture as captured output. Confirm standard harness, access, policies, and actual tests.

## 0-5 minutes: retrieval before explanation

**SAY:** "Our assistant can explain a concept. Now somebody wants a study session. We need to decide whether this is an answer, a missing detail, an operation, or a request for a person."

**DO:** Display four requests: "Explain shared responsibility"; "Make a study session"; "Give me a 30-minute cloud study session"; "Approve my exam accommodation." Give learners 30 seconds to choose a next move, then take two explanations.

**EXPECT:** Shared responsibility is grounded explanation; missing focus needs clarification; a cloud session fits the tool; accommodation approval requires another authority.

**RECOVERY:** If everything is classified as a tool, say: "A tool should have a reason to exist. Reading a reviewed answer does not require a new integration."

## 5-10 minutes: make the boundary visible

**SAY:** "This tool has one input and two outputs. Cloud, security, or governance goes in. A status and a fixed 30-minute session come back. It doesn't save progress or book anything."

**SAY:** "Tool names a capability the assistant can call. This capability is implemented by an agent flow. The condition and variable steps inside that flow are actions. Those are three views of the same small operation, not three separate systems."

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

Use two paired pictures instead of reading every row: **HTTP request to a known service / MCP server exposing described tools**, then **specialist inside this agent / separately maintained agent outside it**. Say: "If Contoso already has an approved course-catalog API, HTTP can call a defined operation. If a team publishes a governed catalog of tools for several assistants, MCP can expose those capabilities. If the work needs its own instructions and judgment, then consider another agent. Our fixed study session needs none of those additions."

**A2A sentence:** "A2A is a way to connect agents over a protocol; child describes an agent's place inside our solution. They answer different questions." Foundry, Fabric, and Microsoft 365 Agents SDK name specialist implementation routes. Leave their setup in the reference sheet. These are hypothetical Contoso extension decisions, not claims that those systems are deployed.

**DO:** Spend three minutes on identity, resource permissions, data policies, external-model approval, and least privilege. Use the Contoso public-material/employee-records example in the decision sheet.

**DO:** Spend three minutes comparing referral, request submission, and live handoff. Read the accommodation boundary response. Explain that a real transfer needs a configured receiving system and observed receipt.

**EXPECT:** Learners choose the simple flow for the current need and can describe when a specialist might earn its extra operational cost.

**RECOVERY:** For requests for detailed SDK setup, point to the referenced Microsoft Learn page and preserve the no-code learning objective. Do not substitute a diagram for a claim that a connection exists.

## 30-33 minutes: universal decision exercise

**SAY:** "Stay with our Contoso assistant. Name the input and outputs for cloud, predict quantum, and write the boundary for exam registration. You have three minutes. Chat, paper, or the worksheet all work."

**DO:** Run the [three-minute exercise](../modules/03-extend/lab.md). Allow one minute per answer. Keep the three prompts visible. Do not assign account setup, flow attachment, or authoring to learners.

**EXPECT:** A bounded contract, a missing-input response, and an honest escalation path.

**RECOVERY:** If the contract is still unclear, point to the labeled input/output diagram. Every learner can participate without tenant access.

## 33-40 minutes: instructor evidence walkthrough

**SAY:** "Now compare those predictions with the record of what ran. A readable answer and a successful operation are different things to check."

**DO:** Spend two minutes inspecting the actual cloud input and returned status/plan. Spend two minutes on the quantum result and missing-focus conversation. Spend two minutes showing the prepared tool-unavailability check, restoring Enabled and rerunning the valid request if performed live. Use the final minute to take one explanation from the group. Show a genuine labeled rehearsal recording if needed; otherwise mark the live check unperformed.

**EXPECT:** Learners distinguish ok, unsupported, and unavailable. Turning a tool off tests unavailability, not a runtime exception. No one claims an email, booking, or stored record.

**RECOVERY:** If the demonstration fails, retain the error as evidence, describe what is known, and use the expected-output fixture only as a labeled prediction. Keep the five-minute Q&A block intact.

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

## Slide sequence for this block

Keep diagrams labeled by function and position. Use solid lines for the core flow and dashed lines labeled **concept only** for hypothetical connections. Never depend on red/green distinctions.

| Slide | Main idea | Visual and teaching move |
| --- | --- | --- |
| 1. What should the assistant do next? | Answer, clarify, call, or refer | Four labeled request cards. Learners choose before labels are revealed. |
| 2. One capability, one contract | focus in; status and plan out | Three boxes: Contoso colleague, GetStudySession, returned session. Annotate fixed 30 minutes. |
| 3. The flow behind the tool | Rules choose authored text | Trigger, defaults, three sequential conditions, one response. Reveal one condition before the repeated pattern. |
| 4. Show me the evidence | A claim is not a call record | Compare labeled **chat response** and **actual input/output** panels. Predict cloud and quantum first. |
| 5. HTTP or MCP? | Choose how to access a capability | Two labeled lanes: defined API operation; server-described tools/resources. Same hypothetical Contoso catalog, no new demo. |
| 6. When would another agent help? | Separate specialization from connection method | Child inside parent boundary; connected specialist outside. A2A labels a connection, not a third nesting level. |
| 7. Who has authority? | Permissions and real human receipt matter | Three labeled stages: referral, submitted request, accepted live transfer. Highlight what evidence each requires. |
| 8. Defend one tool decision | Name one allowed operation and one human boundary | Worksheet prompt, then valid/unsupported/unavailable outcome cards for debrief and Q&A. |

Slides 1-4 support minutes 0-20, slides 5-7 support minutes 20-30, and slide 8 stays visible during minutes 30-50. They do not add time to the block. Source URLs are recorded in [the research note](../sources/research-extend.md).

## Rehearsal sign-off

Record actual elapsed time, cloud/security/governance/quantum run evidence, missing-focus behavior, scope-refusal behavior, unavailability behavior, and recovered valid call. **All tenant execution remains NOT RUN in this repository until real evidence is supplied.** Review [source notes](../sources/research-extend.md) before recording.
