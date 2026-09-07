# Research notes: Inception and Build

**Checked:** 2026-09-05. **Method:** Microsoft Learn MCP search followed by full-page fetch for the sources below. Search snippets and Microsoft Q&A answers were not treated as authoritative procedures. These notes record documentation, not tenant observations. UI and limits must be rechecked during rehearsal.

| Official source | What was verified | Teaching decision |
| --- | --- | --- |
| [Create agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot) | Standard-harness creation, New experience distinction, blank agent, Overview Instruction Edit | One blank agent, controlled setup |
| [Generative orchestration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-generative-actions) | New-agent default, Settings path, description-based topic selection, The agent chooses trigger | Inspect mode before explaining routing |
| [Primary model](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model) | Overview Model selector, availability differences, production versus preview distinction, separate model settings | Keep approved baseline; compare identical tests before changing |
| [Knowledge summary](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio) | Agent and topic scope, source-selection limits, broad-web search, ungrounded-response caveats | Start with one file and controlled search |
| [Upload files](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-file-upload) | TXT support, Dataverse search prerequisite, upload steps, size and count limits | Original small TXT avoids a web-indexing dependency in the core |
| [Public website](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-public-website) | Public websites UI, two-level URL restriction, Bing indexing, descendant scope | Official guide is a direct reading link; broader credentials prefix is an optional tested search scope |
| [Generative answers node](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-boost-node) | Node creation, source selection, native citation behavior | Inspect selected-sources setting; preserve native rendering |
| [Create topics](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics) | Topics Add a topic From blank, supported node types, distinction between modes | One authored learning conversation |
| [Question nodes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-ask-a-question) | Multiple choice, response variable, Ask every time, reprompt, empty-value recovery, interruptions | Explicit quiz wait; honest unmatched-answer recovery |
| [Topic inputs and outputs](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-managing-topic-inputs-outputs) | Details Inputs, new variable, dynamic filling, Set as a value, Should prompt user | Short input demonstration contrasting context reuse with new learner thinking |
| [System fallback](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-system-fallback-topic) | Topics System Fallback, unknown intent, default retries and Escalate redirect | Inspect actual path before calling a message change a verified repair |
| [AI-901 guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901) | Current scope includes cloud concepts, architecture and services, management and governance | Preserve official names; do not mislabel the three tool focus codes as exam domains |
| [Shared responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) | IaaS guest OS, PaaS platform, continuing customer data and access responsibilities | Original narrow explanation and original practice item |

## Corrections that affect delivery

- **AutomaticTaskInput:** Exact-term Learn search did not locate a relevant authoritative authoring procedure. The course names this proposal term, then teaches the documented **Dynamically fill with the best option** topic-input behavior. It does not assert that the term is a current button or supply unverified YAML. A native export can establish the actual serialization later.
- **Scope is explicit:** Current generative-node documentation says **Search only selected sources** on replaces the agent source set for that node; off searches the current agent set. The same article contains older general language about node priority and agent fallback. Teach the specific current setting and test actual behavior rather than turning that older sentence into a universal source-order rule.
- **No “first source wins”:** Descriptions guide selection. The guides do not promise upload order, source rank, or deterministic citations.
- **Grounding is not a correctness switch:** Current docs say turning off ungrounded responses blocks generated answers that use neither source nor tool, and may withhold an answer without an in-text citation. It can also block a follow-up answered from history. The model can still combine its knowledge with retrieved information.
- **Broad web versus configured website:** Web Search can search beyond configured websites. The core turns it off. The exact AI-901 guide is deeper than the documented public-source URL allowance. A credentials prefix expands scope and requires testing, not a claim that it isolates the guide. Do not falsely attest ownership.
- **Source trust versus product tag:** Calling Microsoft Learn authoritative is an editorial judgment. The product's **Official source** feature is documented as incompatible with generative orchestration. This course does not require that tag.
- **Human contact:** A default topic named Escalate does not establish an actual mentor connection. Inspect and adapt its message before claiming any handoff behavior.
- **Limits are current reference facts:** 25 public websites in generative mode, four public URLs in classic mode; files excluded from the 25-source filtering limit; uploaded-file ceiling 512 MB and 500 files, subject to storage. These are not performance targets. Recheck the cited pages before teaching changed numbers.

## Authored material and evidence boundaries

The original [concept file](../contoso-ai901-agent/knowledge/ai901-concepts.txt), question, feedback, timing, examples, and worksheets are newly authored teaching material. The fictional Contoso governance rule is explicitly labeled. A fixed lesson Message does not establish generative retrieval. The separate known-answer test does that only when its actual source evidence is inspected.

The [Module 1 guide](../instructor/01-inception-guide.md) and [Module 2 guide](../instructor/02-build-guide.md) specify expected behavior and repairs. No uploaded file, topic, native export, model selection, fallback path, or live evaluation is claimed to have executed by writing these documents.
