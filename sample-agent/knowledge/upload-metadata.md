# Knowledge upload metadata

These descriptions implement an existing `agents-pro` teaching pattern. They are newly written for
this assistant, not copied Pinball knowledge. Adding a source is not proof that retrieval works.

| Source | Suggested description | Do not use it for |
| --- | --- | --- |
| Microsoft Learn AZ-900 study guide | Official, current scope of Microsoft Azure Fundamentals. Use for objective-domain questions. Prefer the source’s actual current wording. | Guessing exact exam questions, unofficial score predictions, unsupported administrative promises. |
| `azure-concepts.txt` | Original course reference for shared responsibility and a bounded practice example. Use first for the core knowledge demonstration. | A complete exam-preparation syllabus, official Microsoft document, or current exam policies. |
| `training-policy.txt` | FICTIONAL training rules defining the sample tool’s supported inputs and unsupported administrative actions. | Microsoft policy, actual learner entitlements, or an actual support service. |

In Copilot Studio, add permitted sources under **Knowledge** or within the chosen topic-level
generative answers configuration. Follow current Microsoft Learn instructions for the authoring
surface. Check ingestion status, retrieve a known statement, and inspect the citation.
For URL knowledge, verify that the specific intended material is actually retrievable.
Do not assume adding a deep link imports that page verbatim.

**Core order:** start with azure-concepts.txt only. Add the fictional policy when explaining the tool boundary if needed. Inspect the official study guide directly as a human reference; the full deep URL is not the core website-ingestion recipe. Follow the [Build guide](../../instructor/02-build-guide.md) and its verified URL constraints for the optional website extension.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio
