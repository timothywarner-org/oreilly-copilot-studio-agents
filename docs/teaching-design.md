# Teaching design: one assistant, four decisions

**Audience:** first-time Copilot Studio makers with ordinary Microsoft 365 skills. The assistant's user is an Azure beginner. Teaching Azure certification content is not this class's learning outcome.

**Design decision:** keep the approved four objectives verbatim. Teach one small assistant through a worked example, a short attempt, and a visible check. Add each capability only after learners can explain the previous one.

## The minimum successful course

| Stage | Learner decision | Instructor demonstration | Learner evidence |
| --- | --- | --- | --- |
| Inception | What job is this assistant allowed to do? | Create the shell and test an explicit boundary | One instruction, one topic, one measurable success criterion |
| Build | What supports this answer? | Add one small original knowledge file and one teach-question-wait-feedback topic | A topic sequence, a source check, and a response to missing evidence |
| Extend | When must the agent use a tool? | Call GetStudySession for a fixed 30-minute session | A tool contract and an escalation decision |
| Operate | What would justify a limited pilot? | Inspect test results, compare a change, and publish to a scoped channel when authorized | A defensible pilot decision with an owner and unresolved checks |

The first three blocks each contain 50 teaching minutes plus a 10-minute break. Operate contains 50 teaching minutes. The final 10 minutes are wrap-up and questions. Detailed allocations live in the four instructor guides. **Total: 240 minutes.**

## What makes this achievable

1. Use a prepared nonproduction environment. Account creation and tenant troubleshooting happen before class.
2. Begin with one short, original text file. Public search ingestion is an extension, not the first success dependency.
3. Build one explicit practice topic. Show the other topic purposes in the map without authoring five separate topics live.
4. Use one text input and a fixed study-session output. Arrays, loops, daily allocations, APIs, and hosting are unnecessary for the first tool call.
5. Demonstrate native evaluation and one selected publishing channel. Explain other channels through the same identity, audience, and approval questions.
6. Prepare checkpoints in advance. Live-build the instructive change, then inspect its result. A 20-minute rescue operation teaches very little about agent design.

## Participation and assessment

**Maker:** follows the demonstrated configuration with a working account. **Observer:** predicts the branch or result, inspects the instructor's evidence, and explains the decision. Observer participation supports conceptual understanding but does not establish independent authoring proficiency. Offer the same lab for later independent completion.

Use the rhythm **predict, demonstrate, try, explain**. Give the question before the answer. Allow 30 to 60 seconds of thinking before inviting responses. Ask learners to identify the evidence that would change their answer.

| Check | Ready to continue | Reteach when |
| --- | --- | --- |
| Job | Learner names a specific user, allowed behavior, and testable boundary | They describe an all-purpose assistant or use only 'be accurate' |
| Grounding | Learner can inspect the supporting passage and identify a missing answer | They treat a plausible citation as proof |
| Tool | Learner distinguishes returned data from a generated claim of success | They believe naming a tool means it ran |
| Pilot | Learner names evidence, audience, failure handling, and owner | They equate one good answer with operational readiness |

The four worksheet exercises assess the advertised decisions. They do not certify product mastery or AZ-900 readiness.

## Depth budget

**Build and inspect:** instructions, one knowledge source, one practice topic, one study-session flow, a small live evaluation subset, and one scoped publishing route.

**Explain with an example:** triggers versus topic initiation, agent/topic knowledge scope, model choice, MCP, HTTP, child and connected agents, A2A and the named platform connections, DLP, authentication, human handoff, other channels, version comparison, containment, and the five Well-Architected concerns.

**After class:** extend the topic map, inspect a genuine native YAML export, complete independent authoring, run all 12 cases, or attempt the existing multi-day reference design. The optional Node example remains an advanced local oracle and is not the tool demonstrated in the core class.

## Rehearsal acceptance

The written course can be complete while delivery checks remain pending. Sign-off requires a real shell, working retrieval, an actual wait point, a bound flow with inspected outputs, a native evaluation record, a rehearsed scoped publication route, operational evidence, and a sanitized native export. Use [the preflight](../instructor/preflight.md) and [remaining checks](known-gaps.md). Never turn an expected output into a claimed observation.

## Source policy

The public page determines learner promises. The approved proposal preserves the exact objectives. Microsoft Learn establishes documented product behavior. The three research notes separate mutable UI facts from the stable teaching decisions above. A documentation check establishes what Microsoft documents, not what Tim's tenant has enabled.
