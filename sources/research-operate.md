# Operate source review

**Initial review 2026-09-05; evaluation-method correction checked 2026-09-06 with Microsoft Learn MCP search and full-page fetch.** This is a product-documentation review, not a tenant rehearsal. Authored examples and teaching judgments are identified separately below. Sources are mutable; recheck the matching standard-harness surface before delivery.

| Official source | Verified use in course |
| --- | --- |
| [Create single-response tests](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create) | Evaluation > New evaluation > Single responses; CSV headers Question and Expected response; methods and authenticated profiles |
| [Choose evaluation methods](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-overview) | Methods belong to the set; missing expected tools/topics produces Invalid; General quality is added by default; separate semantic and E08-only Tool use sets avoid blank expectations |
| [Modify test cases](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-edit-cases) | Add expected answers, keywords or capabilities to each case as required; CSV expected-response text is not capability-selection metadata |
| [Run and compare results](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results) | Same-set Compare with; Show activity map; export results; response time is a measurement, not a pass/fail score |
| [Activity review](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-review-activity) | Inspect knowledge/tool input-output nodes; generated rationale can be inaccurate |
| [Monitor overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-summary) | Monitor excludes test-panel traffic; channel analytics latency; transcript role; generative versus classic topic analytics |
| [Conversational outcomes](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-improve-agent-effectiveness) | Confirmed/implied resolution, escalation, abandonment, survey and feedback interpretation |
| [Publish and channels](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels) | Publish updates connected channels; new-session behavior; self-test before wider distribution |
| [Teams and Microsoft 365](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams) | Separate Microsoft 365 option, Add channel, See agent in Teams, Add, installation link and access distinction |
| [SharePoint publishing](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-sharepoint) | WRITE site access, publish prerequisite, capacity consumption, separate deployment and site discovery |
| [Licensing](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions) | Trial creates/tests but cannot publish; Teams plan does not include generative orchestration |
| [Model selection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model) | Overview > Model; separate orchestration/prompt model settings; availability and external/cross-geo controls |
| [Data policies](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention) | Connector groups, authentication/channel restrictions, endpoint controls, blocked authenticated evaluations |
| [Power Platform Well-Architected](https://learn.microsoft.com/en-us/power-platform/well-architected/what-is-power-well-architected) | Reliability, Security, Operational Excellence, Performance Efficiency, Experience Optimization |
| [Topic YAML editor](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/topics-code-editor) | Canvas-generated YAML, More > Open code editor, inspect/copy, Save for actual edits, copy topic before modifying |

## Newly authored teaching choices

The fifty-minute sequence, three-case live slice, full twelve-case rehearsal, five-user/one-week pilot, 80% initial meaning threshold, five concrete controls, model selection recommendation and all worked-example numbers are course design choices. They are not Microsoft guarantees or observed tenant facts. The manual rubric and containment proxy are not native import or metric schemas.

## Unresolved until rehearsal

**Correction made:** the previous three-case recipe added Tool use only for E08 without specifying expectations for the other cases. The current procedure uses Compare meaning alone on E04/E05/E08 and a separate E08-only Tool use set. A Tool use pass does not establish correct parameters, successful output, or full-suite success. The native UI must select the real capability. Both prepared CSVs remain **NOT RUN**; the method configuration and import must be rehearsed in the tenant.

Actual licenses, credits, region, harness, visible controls, model options, evaluation methods available in the tenant, connector policies, identities, native execution, channel installation, published behavior, analytics records and native YAML capture all remain unverified by this documentation work. Publishing and native-feature promises require genuine rehearsal evidence; a manual fallback demonstrates reasoning but does not prove a native operation succeeded.

The documentation now exposes both standard-harness and New experience articles with different navigation. This lesson deliberately uses the standard-harness references. Do not combine their UI steps. The native CSV/template and UI still need a rehearsal import in the actual teaching tenant.
