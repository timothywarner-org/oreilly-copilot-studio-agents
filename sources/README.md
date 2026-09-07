# Source register

**Checked for this preparation on 2026-09-05.** Links are mutable; dates describe this review, not a guarantee
that a page or product will remain unchanged.

| Source | Role in this repo | Handling |
| --- | --- | --- |
| [Approved O’Reilly proposal](https://docs.google.com/document/d/1FbWRkrqNZOhhlR71ru2cRMhenH3UQs-3k3T8zkqOI58/edit) | Exact objectives, the approved AZ-900 assistant scenario, topic coverage, activities | Curriculum-only [excerpt](proposal-curriculum.md); original kept outside Git. |
| [September course page](https://www.oreilly.com/live-events/build-ai-agents-to-automate-your-workflows/0642572413361/0642572413354/) | Published title, learner promises, prerequisites, 60/60/60/50/10 schedule | [Structured snapshot](published-course.json); discrepancies recorded. |
| [Predecessor page](https://www.oreilly.com/live-events/how-to-create-ai-agents-like-a-pro/0642572257712/) | Legacy four-segment scope and three advertised business demos | Summarized in the delta; not treated as current product documentation. |
| [agents-pro README](https://github.com/timothywarner-org/agents-pro/blob/main/README.md) | Existing single progressive Pinball Concierge, explicit knowledge descriptions, honest asset gaps | Pattern adaptation only; no copied code, binary assets, or history. |
| [agents-pro July instructor plan](https://github.com/timothywarner-org/agents-pro/blob/main/docs/course-plan-july-2026.md) | Timed demonstrations, expected behaviors, governance connections | Pattern adaptation only. |
| [Microsoft Press AI-901 repo](https://github.com/timothywarner-org/ai901/blob/main/README.md) | Outcome-to-lesson alignment and two-phase practice | Structure adapted; no AI-901 scope imported. |
| [Create agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot) | Current documented standard-harness creation route | Checked separately; actual tenant still needs rehearsal. |
| [Knowledge](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio) | Knowledge placement and retrieval boundaries | Current product reference. |
| [Agent evaluations](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro) | Native evaluation concepts | Repo JSON is not a native import format. |
| [MCP extension](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp) | Tool extension concepts | No connector is provisioned by this scaffold. |
| [Licensing](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions) | Build/test versus publish preflight | No entitlement inferred. |
| [AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901) | Assistant subject-matter authority for the delivered build | Dated snapshot in the kit; use the live guide for current exam objectives. |
| [AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) | Subject matter named in the approved proposal and objective LO2 | Retained only to explain the objective wording; the build no longer uses it. |
| [Power Platform Well-Architected](https://learn.microsoft.com/en-us/power-platform/well-architected/) | The proposal’s governance lens | Recheck feature-specific claims against Microsoft Learn. |

## GitHub implementation sources

- Create a private repo: https://cli.github.com/manual/gh_repo_create
- About metadata and merge/settings options: https://cli.github.com/manual/gh_repo_edit
- Environment authentication: https://cli.github.com/manual/gh_help_environment
- Least privilege and immutable action references: https://docs.github.com/en/actions/reference/security/secure-use

The action revisions used by CI were resolved through GitHub in this conversation:
`actions/checkout` v6 → `d23441a48e516b6c34aea4fa41551a30e30af803`;
`actions/setup-node` v6 → `249970729cb0ef3589644e2896645e5dc5ba9c38`.
Dependabot is configured for future action updates. No hosted CI success is claimed before the first actual run.

## Current course build research

The redesign uses Microsoft Learn MCP search followed by full-page retrieval. Read [Inception and Build sources](research-build.md), [Extend sources](research-extend.md), and [Operate sources](research-operate.md) for the checked pages, supported procedures, and authored teaching choices. These notes supersede broad scaffold descriptions where details differ. No documentation retrieval establishes tenant execution.

## AI-901 scaffold additions requested September 7, 2026

The user explicitly requested completion of `contoso-ai901-agent`, including AI-901 objective knowledge
and a fictional company reward. On September 7, 2026 Tim further directed that AI-901 become the only
agent and that the AZ-900 kit be retired. Neither instruction rewrites the approved objective text, which
still names AZ-900 in LO2 and is preserved verbatim.

| Source | Use | Evidence boundary |
| --- | --- | --- |
| [AI-901 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901) | MarkItDown conversion of the complete Skills measured section | [Snapshot](../contoso-ai901-agent/knowledge/ai901-objective-domain.md) and [provenance](../contoso-ai901-agent/sources/ai901-objective-domain.provenance.json); upload and retrieval NOT RUN. |
| [Create a single response test set](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create) | Evaluation template columns, limits, and import process | Documentation verified September 7; evaluation execution remains separate. |
| [Upload files as knowledge](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-file-upload) | Markdown upload support | Documentation verified September 7; source ingestion NOT RUN. |
| User-provided fictional reward premise | First 50 employees earning AI-901 receive $100 each | [Newly authored Contoso policy](../contoso-ai901-agent/knowledge/contoso-ai-cert-challenge.md); no real entitlement or transaction. |

## Source hierarchy

Keep the proposal and public page distinct. Do not silently erase a difference between them.
Use Microsoft Learn to verify technical behavior, and label any tenant observation separately.
Prior repos inform teaching patterns only. New worksheets, test cases, and reference code in this package
are implementation choices, not quotations from or additions approved by O’Reilly.
