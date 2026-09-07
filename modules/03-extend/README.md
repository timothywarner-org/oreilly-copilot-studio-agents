# 03 · Extend: give the assistant one reliable tool

**LO3:** Extend the agent with actions, agent flows, MCP and subagent concepts, and human handoff patterns.

**The question:** When should our assistant stop writing an answer and use a bounded capability?

**Your role:** You are a Contoso maker helping colleagues study Azure fundamentals. Decide what capability their assistant needs and what evidence would show that it worked.

Our demonstration is **GetStudySession**: choose cloud, security, or governance and receive an authored 30-minute study session. This illustrates predictable tool behavior without arrays, coding, deployment, or complex scheduling. It does not book exams, create resources, or contact a mentor.

**50 minutes of teaching and practice, followed by a 10-minute break.**

| Minutes | Activity | Evidence of learning |
| --- | --- | --- |
| 0-5 | Predict answer, clarify, tool, or mentor | Explain the next move for four requests |
| 5-20 | Build one condition, inspect the completed flow, bind and test | Identify input, returned status, and actual flow run |
| 20-30 | Compare extension and human handoff patterns | Choose the smallest sufficient capability |
| 30-33 | Universal decision exercise | Three brief contract and boundary answers |
| 33-40 | Instructor evidence walkthrough | Compare predictions with actual input/output and unavailable-tool behavior |
| 40-45 | Debrief and failure check | Separate a failed call from an unsupported request |
| 45-50 | Q&A | Resolve uncertainties before operations |

Start with [the lab](lab.md), complete [the worksheet](worksheet.md), and compare [worked answers](worked-example.md) after committing to your answer. The [instructor guide](../../instructor/03-extend-guide.md) contains the demonstration and talk track.

**Instructor-led demonstration, no learner tenant required.** Everyone predicts and interprets the same Contoso cases. The three-minute exercise uses chat, paper, or the worksheet. Independent authoring and workplace adaptation are after-class practice. This repository provides a build recipe, not an importable flow or a claim of tenant execution.

**Checkpoint:** Explain why a fluent sentence is insufficient proof of a tool call. Identify one request this agent must decline or refer to a person.

**References:** [Core flow recipe](../../contoso-ai901-agent/tools/get-study-session.md), [extension decisions](../../contoso-ai901-agent/tools/extension-decisions.md), [verified documentation](../../sources/research-extend.md).

**Continue:** [Operate](../04-operate/README.md)
