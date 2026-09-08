# Operate worksheet

**LO4:** Evaluate, publish, observe, and govern the agent using analytics, agent evaluations, Power Platform Well-Architected guidance, and security principles.

Complete this in seven minutes. Label the evidence source **LIVE**, **REHEARSAL CAPTURE**, **MANUAL TEST**, or **SYNTHETIC EXERCISE**. Keep unperformed execution checks **NOT RUN**.

| Decision or evidence | Your record |
| --- | --- |
| First safe pilot, audience, duration | |
| Governance question that must be answered first | |
| Agent checkpoint and one change being tested | |
| Evidence source and date | |
| Cases executed / passed / failed / errors / not run | NOT RUN |
| Most consequential failure and smallest repair | |
| Same-test comparison: changed case and any regression | |
| Resolution rate with denominator | |
| Containment definition and why it can mislead | |
| Reliability control | |
| Security control and approved data boundary | |
| Operational excellence control and owner | |
| Performance efficiency control and model decision | |
| Experience optimization control | |
| Environment / approved connectors / tenant approver | NOT VERIFIED |
| Publication entitlement / channel / tested identity | NOT VERIFIED |
| Stop condition, access-removal owner, recovery checkpoint | |
| GO / CONDITIONAL / NO-GO and supporting evidence | NO DECISION YET |
| One next action and who owns it | |

**Peer review:** What missing evidence would change your decision most?

## Worked answer for the synthetic exercise

**NO-GO.** B passes three of four sample cases but still promises a mentor response it cannot deliver. The synthetic repeated question reveals a binding failure. There are no actual tenant results or channel checks in these invented records. The maker repairs wording and input binding, then executes all twelve actual cases and verifies the learner identity in Teams.

| Pillar | Concrete course control and reason |
| --- | --- |
| Reliability | Preserve a working checkpoint; use a truthful failure message when the flow cannot return a plan |
| Security | Require Microsoft authentication; approve only the course sources and intended connectors; no learner personal records |
| Operational Excellence | Named owner reviews failed sessions daily, records changes, and reruns the same twelve cases |
| Performance Efficiency | Start with an approved GA model and one bounded tool; measure actual response time before increasing complexity |
| Experience Optimization | Use one short question at a time, readable source links, and an honest mentor signpost; test keyboard interaction in Teams |

A proposed five-volunteer, one-week Teams pilot becomes eligible only after the evidence and approvals exist. The platform administrator owns access removal if a data boundary fails. The maker restores the known-good checkpoint and republishes after verification; publication is not an automatic rollback guarantee. Use separate development, test, and production environments for a later operational rollout, with environment-specific connections and a reviewed promotion process. Do not provision three environments during this class.

**Strategic extension:** an internal onboarding assistant can reuse the teach-check-handoff pattern. Replacing public Azure sources with internal policy documents adds new access-control and outdated-policy tests before a pilot.
