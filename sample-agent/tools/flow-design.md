# CreateStudyPlan — bounded agent-flow design

**Optional advanced follow-up.** The live course uses [GetStudySession](core-study-session.md), with one text input and a fixed 30-minute output. This older multi-day design and its Node reference are retained for independent extension. They are not prerequisites or the core demonstration.

**Implementation specification, not a deployed flow.** This is a suggested teaching realization of
the proposal’s study-plan or lab-generator action pattern. The core route is no-code.

## Contract

Inputs: `days` (integer 1–14), `minutesPerDay` (integer 10–120), and `focus` (one to three unique codes
from the [contract](study-plan-contract.json)). These numeric limits are invented for this demonstration.
Output: an array of daily sessions, each with day, focus code, minutes, and a read/practise/review allocation.
A result is a **plan suggestion**, not an exam registration or a side effect.

## No-code implementation sequence

1. In the supported Copilot Studio authoring experience, create an agent flow callable as a tool.
   Use the current tool/flow authoring controls; rehearse them before class.
2. Define the three inputs. Choose a native array or a documented mapping for `focus`; do not silently
   treat a string as an array. Write down that binding decision.
3. Validate bounds and supported codes before generating the plan. Reject missing, ambiguous,
   duplicate, fractional, or out-of-range inputs with a clear response.
4. Initialize an empty result collection. Iterate `days` times using a bounded native loop.
5. For each day, rotate through the selected focus codes. Allocate 40% of minutes to reading and
   40% to original-question practice, rounding those two allocations down. Assign the remainder to review.
6. Return the structured result to the calling agent. Do not create a connector side effect.
7. Bind the real flow to the study-plan topic/tool, then verify one valid and two invalid invocations.
8. Compare the observed output with the local reference function. Record the actual flow result,
   not the output of the local function, as evidence of the cloud integration.

## Local reference and fallback

`npm run demo:plan` runs [src/study-plan.mjs](../../src/study-plan.mjs) with the provided fixture.
It gives a deterministic contract oracle and an honest offline fallback. It is not an HTTP endpoint,
MCP server, published agent, or substitute for a real integration test.

## Permission boundary

The design has no need to send mail, access a calendar, collect an email address, write a database,
or request an Azure subscription. Adding any such action changes its risk and scope.
A mentor contact requires a separate authorized route; no fake ticket IDs are permitted.
