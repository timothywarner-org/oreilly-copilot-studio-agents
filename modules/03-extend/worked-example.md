# Worked example: one tool, one boundary

**AUTHORED EXPECTATIONS. No tenant run is represented here.**

| Request | Decision | Reason |
| --- | --- | --- |
| Explain shared responsibility | Answer using grounded knowledge | This is explanation, not a new operation |
| Make a study session | Clarify focus | The tool requires one of three focus values |
| Give me a 30-minute cloud study session | Call GetStudySession with focus=cloud | The request fits the exact contract |
| Approve my exam accommodation | Refer to the official support process/person | Neither the assistant nor this flow has approval authority |

**Contract:** one Text input focus; cloud/security/governance. Two Text outputs status and plan. A supported value returns ok plus the matching authored session. quantum returns unsupported plus "Choose cloud, security, or governance." No custom day counts, bookings, saved progress, or messages.

**Missing focus:** "Which area would you like: cloud, security, or governance?" Obtain the choice before calling the tool. A missing/null trigger input can fail validation; do not assume it becomes an unsupported response.

**Failure:** "I couldn't retrieve the study session. I haven't created or saved anything. You can retry, or use the written course activity." Do not turn an error into a fabricated ok result.

**Human boundary response:** "I can't approve accommodations or transfer this conversation to exam support here. Use the official exam accommodations process. I can help you summarize your question without including sensitive medical information."

**Future handoff design:** A designated support team, learner consent to share a minimal summary, an approved channel, and a received case or transfer acknowledgment. Until those exist, the sample is a referral pattern. Do not invent a team address or promise a response time.

**Governance answer:** Authentication establishes whose authority a call uses. Data policy controls permitted connections and data combinations. Resource permissions still govern what that identity can do. MCP standardizes tool access; it does not supply blanket permission.

**One plausible revision:** If learners repeatedly request another duration, collect that need before widening the contract. Revisit validation and evaluations. Do not pretend a fixed 30-minute plan is a custom 500-minute plan.
