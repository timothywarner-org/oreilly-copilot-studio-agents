# Extend lab: decide before adding a tool

**Target:** LO3. **Time:** 10 minutes. **Deliverable:** [worksheet](worksheet.md).

**Starting state:** You have seen the grounded assistant and GetStudySession demonstration. No tenant access is required for the decision task. The [flow recipe](../../sample-agent/tools/core-study-session.md) supplies expected behavior.

1. **Minutes 0-2:** Classify these requests as answer, clarify, tool, or mentor: "Explain shared responsibility"; "Make a study session"; "Give me a 30-minute cloud study session"; "Approve my exam accommodation." Give one reason for each.
2. **Minutes 2-5:** Define the smallest tool contract. Include allowed focus values, outputs, and one operation it cannot perform. Predict focus=quantum. Explain what to do before calling a tool when focus is missing.
3. **Minutes 5-8:** Choose the mentor case. Draft the response and identify who would receive it, what the learner must agree to share, and how you would prove receipt. If no recipient/integration exists, say so. A referral sentence is not a completed transfer.
4. **Minutes 8-10:** Compare with a partner or the [worked example](worked-example.md). Record one difference and the evidence needed to settle it.

**Optional maker route during minutes 2-8:** If the instructor has already published and shared the flow in your approved environment, use **Agents > your agent > Tools > Add a tool > Flow**, select GetStudySession, then **Add and configure**. Follow the input and completion configuration in the [recipe](../../sample-agent/tools/core-study-session.md). Test cloud and inspect returned data. Do not spend the exercise building the entire flow or diagnosing licensing. If the flow is unavailable, complete the decision task immediately.

**Success:** Correct contract, honest unsupported/failure behavior, and a justified human boundary. A live maker run is extra evidence.

**Recovery:** Label predictions **PREDICTED** and observations **OBSERVED**. Leave execution **NOT RUN** unless inspected. Never bypass data policy or use real personal records to finish this exercise.
