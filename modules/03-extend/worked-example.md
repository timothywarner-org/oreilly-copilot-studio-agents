# Worked example: a bounded tool and a confirmed signup

**Authored expectations.** These rows are a reasoning guide, not a record of your own tenant execution.

| Request | Decision | Evidence |
| --- | --- | --- |
| Explain fairness | Answer from relevant knowledge | Response and supporting source |
| Give me a study session | Collect the missing focus | Fresh choice before the call |
| Give me a 30-minute session for responsible-ai | Call GetStudySession with focus=responsible-ai | Actual input, status=ok, and the matching plan |
| Give me a session for quantum | State the supported choices | Direct flow returns unsupported and the choice prompt |
| Sign me up for AI-901 | Request confirmation of the row and announcement | No new effect before a fresh affirmative reply |
| Book my exam or pay my reward | Explain the boundary and official/human process | No invented booking, eligibility, or payment result |

**Contract:** one Text input, focus. Allowed values: responsible-ai, workloads, foundry.
Two Text outputs: status and plan. A supported value returns ok with an authored 30-minute session.
Unsupported input returns unsupported and "Choose responsible-ai, workloads, or foundry."

**Missing focus:** "Which area would you like: responsible-ai, workloads, or foundry?"
A missing required trigger input may fail validation, so collect it before calling the tool.

**Failed call:** "I couldn't retrieve the study session. I haven't saved anything."
Never fabricate an ok result or substitute a generated plan while claiming the tool succeeded.

**Signup:** Fresh confirmation covers both the synthetic SharePoint row and the General-channel
announcement. The agent's saved-row result proves the row operation. The notification flow's result
supplies separate evidence for the Teams post. If the post fails, the saved row can still exist.

**Human referral:** "I can't approve an exam accommodation or transfer you to support here. Use the
official exam accommodations process." A Teams announcement does not transfer the conversation to a person.

**Governance:** Authentication identifies the authority used for a call. Resource permissions and
data policy constrain it. MCP supplies an interface, not blanket access.
