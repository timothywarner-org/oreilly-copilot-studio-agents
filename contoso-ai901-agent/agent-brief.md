# Agent brief: Contoso AI Fundamentals Coach

**User:** A fictional Contoso employee preparing for AI-901.
**Job:** Understand one idea, practice it, and choose a useful next study action.
**Maker:** The person designing and evaluating the coach, which is your role in this course.

| Capability | Boundary | Evidence of success |
| --- | --- | --- |
| Explain an AI concept | Use relevant configured sources and admit missing evidence | Answer and supporting source agree |
| Practice an original question | Wait for the answer before revealing feedback | A real turn boundary and the correct topic branch |
| Return a study session | Exactly 30 minutes for responsible-ai, workloads, or foundry | Actual GetStudySession input, status, and plan |
| Explain the fictional reward | $100 each for the first 50 qualifying employees; no live award administration | Response matches the fictional policy without invented counts or payment claims |
| Save a synthetic signup | Fresh confirmation covers the row and public channel announcement | Saved row, followed by separate notification-flow evidence |

## Acceptance checks

1. A grounded answer identifies a source that actually supports the claim.
2. Missing exam administration data produces an honest limitation.
3. The RAI topic captures StudentAnswer, sets IsCorrect, and selects the matching feedback branch.
4. GetStudySession returns the exact authored plan only after an actual successful call.
5. `Sign me up for AI-901.` requests fresh confirmation. Declining creates no new row or post.
6. Confirming creates one synthetic row. The separate notification flow supplies its own evidence.
7. A saved-row response never claims that Teams has already posted without the notification result.
8. Exam booking, verified achievement, award placement, and payment remain outside the signup flow.

**Source hierarchy:** Microsoft Learn defines product behavior and exam scope. Original course
explanations support the examples. Fictional Contoso policies define only the invented company rules.

**Pilot decision:** A human owner reviews failed cases, intended users, data boundaries, and access
before any rollout. One successful demonstration is not a production-readiness claim.
