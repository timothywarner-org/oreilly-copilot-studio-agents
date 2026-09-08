# Link register: every source behind the four segments

Every page the course relies on, grouped by the segment that uses it. Microsoft Learn is the authority
for product behavior, so almost everything here is a Learn page. Locale-neutral URLs are used on purpose;
Microsoft serves your own language from them.

**How this list was built.** Each candidate was found and confirmed through the Microsoft Learn
documentation index rather than typed from memory, then every URL was requested twice over the public
internet. Only entries that returned HTTP 200 on both passes are listed. The verification record at the
bottom carries the date and counts.

**What reachability does not prove.** Reachability is not accuracy. A page can answer 200 and still have
been rewritten since this list was made. Copilot Studio changes quickly. Re-read anything that contradicts
what you see in your own tenant. Use Microsoft Learn for supported behavior and inspect tenant settings when the experience differs.

## Start here

| URL | Page | Why it matters |
| --- | --- | --- |
| https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-901 | Study guide for Exam AI-901 | The skills measured list the coach is grounded in, and the source of the two weighted skill areas. |
| https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-900 | Study guide for Exam AI-900 | Carries the retirement banner confirming AI-900 ended on June 30, 2026 and AI-901 replaced it. |
| https://learn.microsoft.com/credentials/support/retired-certification-exams | Retired certification exams | The authority for which exams have retired, useful whenever a course or a study plan looks out of date. |
| https://learn.microsoft.com/microsoft-copilot-studio/ | Copilot Studio documentation | The product documentation root, worth bookmarking before anything else. |

## Segment 1: Inception

Plan the agent from persona, job, instructions, topic map, guardrails, and success metrics.

| URL | Page | What it supports |
| --- | --- | --- |
| https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/overview | Agents overview | The current agent model as one set of configurable parts: instructions, knowledge, tools, model, and connected agents. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-first-bot | Create and delete agents | The step-by-step route for creating the agent shell through the standard harness. |
| https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-get-started | Quickstart: create and deploy an agent | The end-to-end first-agent walkthrough tying together sign-up, build, test, and publish to a demo site. |
| https://learn.microsoft.com/microsoft-copilot-studio/requirements-licensing-subscriptions | Get access to Copilot Studio | Trial access, and the point that a trial supports building and testing but not publishing. |
| https://learn.microsoft.com/microsoft-copilot-studio/environments-first-run-experience | Power Platform environments in Copilot Studio | Environments and the first-run experience behind your first agent. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-instructions | Write agent instructions | The instruction-design exercise: persona, tone, and rules. |
| https://learn.microsoft.com/microsoft-copilot-studio/guidance/generative-mode-guidance | High-quality instructions for generative orchestration | Guardrails and scope boundaries, including instructions that state what the agent must not answer. |
| https://learn.microsoft.com/microsoft-copilot-studio/guidance/generative-orchestration | Apply generative orchestration | The planner architecture and control layers behind routing decisions. |
| https://learn.microsoft.com/microsoft-copilot-studio/advanced-generative-actions | Orchestrate agent behavior with generative AI | How the agent chooses between topics, tools, and knowledge, and how that differs from classic orchestration. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics | Create and edit topics | Designing the topic map and its trigger phrases. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-triggers | Set topic triggers | Trigger types, one of the named parts of the agent model. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-select-agent-model | Select a primary AI model | Choosing the model that powers the agent's reasoning, and recording that choice in the brief. |
| https://learn.microsoft.com/microsoft-copilot-studio/knowledge-copilot-studio | Knowledge sources summary | Where grounding fits in the plan before any source is added. |
| https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels | Publish and deploy your agent | The build-and-test versus publish distinction, framed early so expectations stay honest. |

## Segment 2: Build

Ground the answers, then design a topic that teaches, waits, and hands off.

| URL | Page | What it supports |
| --- | --- | --- |
| https://learn.microsoft.com/microsoft-copilot-studio/knowledge-copilot-studio | Knowledge sources summary | Agent-level versus topic-level knowledge, citation settings, and the allow-ungrounded-responses control. |
| https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-existing-copilot | Add knowledge to an agent | Where a source is attached at the agent level rather than inside a topic. |
| https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-file-upload | Upload files as a knowledge source | The file-upload demo and the supported document types. |
| https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-public-website | Add a public website as a knowledge source | Adding and then testing a public website as agent-level knowledge. |
| https://learn.microsoft.com/microsoft-copilot-studio/requirements-quotas | Quotas and limits | The file size and file count limits quoted during the upload demo. |
| https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-node | Use generative answers in a topic | The generative answers node, the search-only-selected-sources setting, and topic sources overriding agent sources. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics | Create and edit topics | The core topic-authoring demo and the full node type list. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-ask-a-question | Ask a question | The node that makes the topic genuinely wait for an answer instead of lecturing past the learner. |
| https://learn.microsoft.com/microsoft-copilot-studio/advanced-managing-topic-inputs-outputs | Manage topic inputs and outputs | Automatic slot filling versus an explicit question, and when each is right. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-system-topics | Use system topics | Every system topic, including Fallback and Conversational boosting. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-system-fallback-topic | Configure the system fallback topic | Editing the default Fallback flow to repair an unhelpful failure response. |
| https://learn.microsoft.com/microsoft-copilot-studio/guidance/fallback-topic | Use the Fallback topic | Design patterns beyond the default rephrase-and-escalate behavior. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-test-bot | Test your agent | The test panel, node highlighting, and variable inspection while running test prompts. |

## Segment 3: Extend

Give the agent a bounded tool, then decide where its authority stops.

| URL | Page | What it supports |
| --- | --- | --- |
| https://learn.microsoft.com/microsoft-copilot-studio/add-tools-custom-agent | Add tools to custom agents | Adding GetStudySession to the Tools page and configuring its inputs and completion behavior. |
| https://learn.microsoft.com/microsoft-copilot-studio/flows-overview | Agent flows overview | What an agent flow is, and the two ways to create one. |
| https://learn.microsoft.com/microsoft-copilot-studio/flow-agent | Add an agent flow as a tool | The exact trigger and action requirements for calling a flow from an agent. |
| https://learn.microsoft.com/microsoft-copilot-studio/flow-designer | Edit and manage your agent flow | The designer canvas, error checking, and publishing a flow. |
| https://learn.microsoft.com/power-automate/create-variable-store-values | Store and manage values in variables | The Initialize, Set, and Increment variable actions used inside the flow. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-review-activity | Review agent activity | The evidence that a tool actually ran, with its real inputs and outputs. This is the antidote to a fluent answer. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-http-node | Make HTTP requests | The HTTP Request node, its headers and body, and its error handling. |
| https://learn.microsoft.com/microsoft-copilot-studio/agent-extend-action-mcp | Extend your agent with Model Context Protocol | What MCP is, and the steps to connect an agent to an MCP server as a tool. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-add-other-agents | Add other agents overview | Child agents, connected agents, and A2A compared, so you can argue why this agent needs none of them. |
| https://learn.microsoft.com/microsoft-copilot-studio/advanced-hand-off | Hand off to a live agent | The Escalate system topic and the Transfer conversation node. |
| https://learn.microsoft.com/microsoft-copilot-studio/configuration-end-user-authentication | Configure user authentication | The three authentication options and the least-privilege scopes field. |
| https://learn.microsoft.com/microsoft-copilot-studio/admin-data-loss-prevention | Configure data policies for agents | How data policies restrict connectors, channels, and HTTP requests before a maker ever sees them. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-select-agent-model | Select a primary AI model | The available models and their use tags, revisited once the agent has a tool. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-select-external-response-model | Choose an external model | Selecting an external model, and the admin approvals required first. |
| https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-sharepoint | Add SharePoint as a knowledge source | The steps and authentication scopes for connecting a SharePoint site or list. |
| https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams | Connect an agent to Teams and Microsoft 365 | Publishing to the Teams channel, which the milestone workflow announces into. |

## Segment 4: Operate

Test it, watch it, govern it, and decide whether it is ready for anyone else.

| URL | Page | What it supports |
| --- | --- | --- |
| https://learn.microsoft.com/microsoft-copilot-studio/analytics-agent-evaluation-intro | About agent evaluation | The test case and test set concepts that open the evaluation work. |
| https://learn.microsoft.com/microsoft-copilot-studio/analytics-agent-evaluation-create | Create a single response test set | The exact CSV shape for import, including the column headers and the row limit. |
| https://learn.microsoft.com/microsoft-copilot-studio/analytics-agent-evaluation-overview | Choose evaluation methods | Each method defined, so a set is not scored by the wrong one. |
| https://learn.microsoft.com/microsoft-copilot-studio/analytics-agent-evaluation-results | Run evaluations and view results | Reading results, comparing versions, and exporting to find failure patterns. |
| https://learn.microsoft.com/microsoft-copilot-studio/authoring-review-activity | Review agent activity | The activity map and transcript views for reconstructing a conversation turn by turn. |
| https://learn.microsoft.com/microsoft-copilot-studio/analytics-overview | Monitor overview | The summary view and how sessions are counted before you interpret any number. |
| https://learn.microsoft.com/microsoft-copilot-studio/analytics-improve-agent-effectiveness | Monitor conversational agents | Resolved, escalated, and abandoned outcomes as the containment signals. |
| https://learn.microsoft.com/microsoft-copilot-studio/analytics-transcripts-studio | Understand downloaded session data | The fields in a downloaded transcript, which is where an anonymization decision becomes real. |
| https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels | Publish and deploy your agent | Publishing fundamentals, authentication choices, and configuring channels after the first publish. |
| https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams | Connect an agent to Teams and Microsoft 365 | Publishing to Teams and scoping the audience from personal install to org-wide approval. |
| https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-sharepoint | Publish an agent to SharePoint | Deploying to a SharePoint site and using Approved status to control visibility. |
| https://learn.microsoft.com/power-platform/well-architected/what-is-power-well-architected | What is Power Platform Well-Architected? | The framework and its five pillars. |
| https://learn.microsoft.com/power-platform/well-architected/pillars | Well-Architected pillars | All five pillars with their design principles, used to fill the pilot worksheet. |
| https://learn.microsoft.com/microsoft-copilot-studio/admin-data-loss-prevention | Configure data policies for agents | The policies that decide what a pilot is even allowed to do. |
| https://learn.microsoft.com/microsoft-copilot-studio/security-and-governance | Copilot Studio security and governance | The security and data governance controls, including DLP, customer-managed keys, and audit logging. |
| https://learn.microsoft.com/microsoft-copilot-studio/guidance/sec-gov-phase2 | Implement a zoned governance strategy | Environment strategy and tenant data boundaries through the zoned governance model. |

## Reference check

**Checked September 8, 2026.** Every URL in this list returned successfully. The broader learner-tree
check reached all 96 distinct URLs at least once; Microsoft rate-limited some repeat requests.
Reachability does not prove that a page's content is unchanged or that your tenant has the feature.
Use the current linked guidance when making a product decision.
