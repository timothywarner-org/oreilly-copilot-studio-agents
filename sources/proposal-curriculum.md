# Approved proposal: curriculum excerpt

Source: https://docs.google.com/document/d/1FbWRkrqNZOhhlR71ru2cRMhenH3UQs-3k3T8zkqOI58/edit

Retrieved as an actual Google Drive Markdown export in this conversation. Extracted on 2026-09-05.
The original curriculum wording and timing notation are preserved below; trailing whitespace is normalized. Contacts, home address,
family scheduling information, and administrative sections are deliberately excluded.
This is **an excerpt**, not a replacement for the original proposal.

> **Do not edit the quoted text below.** It names **AZ-900** throughout, including in objective LO2.
> The delivered build is **AI-901**, because AI-900 retired on June 30, 2026 and AI-901 replaced it under
> the same certification name. This file is a verbatim record of what O'Reilly approved, so it is left
> exactly as approved and the difference is recorded instead. See
> [source discrepancies](../docs/course-delta.md#source-discrepancies) and
> [remaining checks](../docs/known-gaps.md). `scripts/validate-repo.mjs` asserts that every objective
> string in `course.json` still appears verbatim below, so editing either one alone fails the build and
> editing both together would conceal the difference.

---

### Course Registration Page Information

**Course Description**

Copilot Studio changes fast, so this course teaches the current agent model through one progressive build instead of a grab bag of disconnected demos. In this four-hour live course, learners build an AZ-900 Cert-Prep Assistant for a cloud beginner preparing for Microsoft Azure Fundamentals.

The agent starts as a planned scenario with clear instructions, topics, guardrails, and success metrics. It then grows into a grounded knowledge agent, a tool-using agent, and finally a governed agent that can be tested, observed, and prepared for real users. Learners work with current Copilot Studio concepts including generative orchestration, knowledge sources, topics, actions and tools, agent flows, MCP and connected-agent patterns, model selection, evaluations, analytics, VS Code/YAML awareness, and Power Platform Well-Architected guidance.

**Course Objectives**

* Plan a Copilot Studio agent from persona, job-to-be-done, instructions, topic map, guardrails, and success metrics.
* Build a grounded AZ-900 study assistant using knowledge sources, topics, generative answers, and test prompts.
* Extend the agent with actions, agent flows, MCP and subagent concepts, and human handoff patterns.
* Evaluate, publish, observe, and govern the agent using analytics, agent evaluations, Power Platform Well-Architected guidance, and security principles.


**Target Audience**

* You’re a Microsoft 365 or Power Platform maker, technical trainer, business analyst, IT professional, or solution architect who needs a current mental model for Copilot Studio agents.
* You support training, enablement, help desk, cloud adoption, internal knowledge work, or governed automation where accurate answers and clear handoff paths matter.
* You want to understand current Copilot Studio capabilities without chasing every feature rename in the portal.

**Prerequisites**

* Basic comfort using Microsoft 365 and web-based admin or authoring tools.
* Basic familiarity with Microsoft Azure concepts is helpful but not required.
* No coding required. Some Power Automate or workflow design experience is helpful.
* Learners do not need prior Copilot Studio experience.

**Course Preparation**

To follow along, you’ll need:

* A Microsoft 365 work or trial account with Copilot Studio access.
* Microsoft Teams available in the browser or desktop app.
* Access to the course repository materials supplied before the event.
* A browser, plus optional VS Code if learners want to inspect exported Copilot Studio YAML files.

**Course Follow-Up**

* Use the course repo to review the AZ-900 assistant, extend the topic map, inspect exported Copilot Studio YAML, and compare current Microsoft Learn feature names with what appears in your tenant.

**Course schedule**

The time frames are only estimates and may vary according to how the class is progressing.

Segment 1: Inception \- Design the AZ-900 Agent (50 minutes)

Define the current Copilot Studio agent model: instructions, knowledge, topics, tools, triggers, channels, and orchestration
Explain the course arc: one AZ-900 Cert-Prep Assistant built across design, build, extend, and operate
Frame the learner persona: a cloud beginner preparing for Microsoft Azure Fundamentals
Demo: create the agent shell, draft instructions, enable generative orchestration, and sketch the topic map
Plan the AZ-900 topic map and knowledge strategy
Define guardrails for unsupported claims and human mentor handoff
Mini-exercise: write one instruction, one success metric, and one topic for the AZ-900 assistant
Q\&A (5 minutes)

Break (10 minutes)

Segment 2: Build \- Topics, Triggers, Knowledge, and Grounded Answers (50 minutes)

Add trusted AZ-900 knowledge sources and explain when to use agent-level knowledge versus topic-level grounding
Build exam-domain overview, practice question, study-plan, fallback, and search topics
Demo: test grounded responses, improve fallback behavior, and tune topic inputs
Use AutomaticTaskInput and explicit questions where each makes sense
Discuss knowledge limits, source ordering, and citation expectations
Mini-exercise: write a topic that teaches, checks understanding, and hands off cleanly
Q\&A (5 minutes)

Break (10 minutes)

Segment 3: Extend \- Actions, MCP, and Subagent Patterns (50 minutes)

Explain when the assistant should answer, ask a follow-up question, call a tool, or hand off to a human mentor
Show how actions, agent flows, HTTP tools, MCP, and add-other-agent patterns fit into the current Copilot Studio model
Demo: extend the AZ-900 assistant with a study-plan or lab-generator action pattern
Discuss current multi-agent taxonomy: child agents, connected agents, A2A, Foundry, Fabric, and M365 SDK connections
Cover DLP, authentication, tenant approvals, external models, and least-privilege tool use
Mini-exercise: choose one tool the agent should call and one situation it must escalate
Q\&A (5 minutes)

Break (10 minutes)

Segment 4: Operate \- Test, Observe, Govern, and Publish (50 minutes)

Prepare the agent for publishing to supported channels such as Teams, SharePoint, and Microsoft 365 Copilot
Use native agent evaluations, test sets, activity maps, and version comparison to find failure patterns
Review analytics, conversation transcripts, containment signals, and user experience metrics
Apply the Power Platform Well-Architected lens: reliability, security, operational excellence, performance efficiency, and experience optimization
Review environment strategy, DLP, data boundaries, tenant approvals, and rollout planning
Show the extension path from AZ-900 study assistant to other internal knowledge and enablement agents
Wrap-up exercise: name the first agent you would safely pilot and the governance question it must answer first
Q\&A (5 minutes)

Overall wrap-up and next steps (5 minutes)
