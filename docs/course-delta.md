# Curriculum delta: predecessor → September 8 course

**Scope: only Build AI Agents to Automate Your Workflows.**
The source course is *How to Create AI Agents Like a Pro*, not *Context Engineering with MCP*
and not *Build Production-Ready AI Agents*. Louise’s transition correspondence explicitly
linked the old title to this proposal.

## Old advertised course versus current commitment

| Dimension | Old advertised course | September commitment | Repository decision |
| --- | --- | --- | --- |
| Scenario | FAQ/customer service, HR onboarding, document processing | One AZ-900 Cert-Prep Assistant | One shared agent across four modules, delivered as the AI-901 Contoso AI Fundamentals Coach. |
| First segment | Create an agent and add knowledge | Design from persona, instructions, guardrails, and metrics | Add an explicit design brief before authoring. |
| Conversation | Topics, actions, approval workflows | Grounded answers, topic inputs, practice, fallback, and search | Teach-check-handoff topic with source evidence. |
| Extension | Autonomous event triggers are central | Actions, agent flows, MCP, delegation, and human handoff | A bounded study-plan tool; event triggers remain a comparison, not a fifth module. |
| Operation | Publish, analytics, and ROI | Evaluate, observe, govern, and publish | Evidence-based pilot decision; no unsupported ROI promises. |

The scenario row records what the proposal committed. **The delivered assistant is the Contoso AI
Fundamentals Coach on AI-901**, after AI-900 retired on June 30, 2026 and the sibling fundamentals exam
moved. The predecessor AZ-900 kit was retired on September 7, 2026, so `contoso-ai901-agent/` is the only
kit. The four objectives, the four modules, and the 240-minute schedule are unchanged by that swap, and
the AZ-900 wording inside objective LO2 is deliberately preserved. See the exam-number entry under
[source discrepancies](#source-discrepancies).

Sources: [old advertisement](https://www.oreilly.com/live-events/how-to-create-ai-agents-like-a-pro/0642572257712/), [approved curriculum](../sources/proposal-curriculum.md),
[current advertisement](https://www.oreilly.com/live-events/build-ai-agents-to-automate-your-workflows/0642572413361/0642572413354/).

## What the existing working material adds

The newer `agents-pro` README and July plan already consolidate the old scenarios into the
**Contoso Pinball Gallery Concierge**. Therefore, “moving from three agents to one” is a change from
**old marketing copy**, not a claim that Tim’s latest delivery still used three separate builds.

Carry forward the single progressive agent, explicit knowledge-source descriptions, deterministic
boundaries for tools, expected-result prompts, and recovery checkpoints. Change the subject to
AI-901. Leave Pinball assets, Foundry code, Kubernetes examples, and repository histories behind.

From the Microsoft Press `ai901` repo, carry forward objective-to-module alignment,
per-module quick starts, and two-phase practice: question first, feedback after the learner responds.
Do not copy that repository's scope, assets, or history, and do not make coding mandatory.

**Narrowed September 7, 2026.** An earlier version of the line above prohibited importing the AI-901
objective domain outright. That prohibition was aimed at the predecessor repository, and it is now too
broad: the AI-901 live-build kit deliberately carries a dated snapshot of the published Skills measured
section at `contoso-ai901-agent/knowledge/ai901-objective-domain.md`, converted from Microsoft Learn with
recorded provenance. It is a first-party source retrieved directly from Microsoft Learn, not a copy of
the Microsoft Press repo, and the assistant needs it to answer scope questions from evidence rather than
from model memory. The exam candidate's Python prerequisites do not travel with it:
`course.json.codingRequiredForLearners` stays `false` and the attendee route stays no-code.

## Source discrepancies

**Exam number:** The proposal and the published registration page both name **AZ-900**, including inside
objective LO2. The delivered build is **AI-901**, because AI-900 retired on June 30, 2026 and AI-901
replaced it under the same certification name. The objective strings and the proposal excerpt are left
exactly as approved; the difference is narrated rather than concealed. Tracked in
[remaining checks](known-gaps.md) and [STATUS.md](../contoso-ai901-agent/STATUS.md).

**Audience:** The current public description opens by calling this a class for cloud beginners preparing
for Azure Fundamentals. The proposal instead has makers build an assistant **for** that persona.
The public audience section also describes makers and technical professionals. Flag this wording to
editorial; do not rewrite the repo into a certification cram course to conceal the mismatch.

**Timing:** The proposal lists four 50-minute blocks, Q&A lines, three 10-minute breaks, and a 5-minute
wrap-up. Reading every Q&A as extra would exceed four hours. The current public schedule states
60/60/60/50 plus 10 minutes of wrap-up: exactly 240 minutes. The run of show follows that public
schedule and embeds Q&A inside each block. It does not claim the proposal text was changed.

**Learner access:** The public preparation still says the repo link is “to come.” The requested
private origin cannot be assumed accessible to attendees. An authorized distribution decision is
required before sending a learner link.

**Product surface:** Current Microsoft creation guidance distinguishes the standard harness from
New experience. This is a technical preflight item, not grounds for adding another course track.
See [environment notes](environment-notes.md).

## Keep the scope honest

Worksheets, reference code, and acceptance tests are newly authored teaching aids. They implement
the existing four objectives. They are not a new promise of full production deployment, certification
success, a commercial support arrangement, or new publisher-approved curriculum.
