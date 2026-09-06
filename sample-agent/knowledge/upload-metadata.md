# Knowledge upload metadata

These descriptions implement an existing `agents-pro` teaching pattern. They are newly written for
this assistant, not copied Pinball knowledge. Adding a source is not proof that retrieval works.

| Source | Suggested description | Do not use it for |
| --- | --- | --- |
| Microsoft Learn AZ-900 study guide | Official, current scope of Microsoft Azure Fundamentals. Use for objective-domain questions. Prefer the source’s actual current wording. | Guessing exact exam questions, unofficial score predictions, unsupported administrative promises. |
| `azure-concepts.txt` | Original brief demonstration notes for a source-grounded study assistant. Use to explain the study loop and the distinction between objective categories. | A complete exam-preparation syllabus or official exam policies. |
| `training-policy.txt` | FICTIONAL training rules defining the sample tool’s supported inputs and unsupported administrative actions. | Microsoft policy, actual learner entitlements, or an actual support service. |

In Copilot Studio, add permitted sources under **Knowledge** or within the chosen topic-level
generative answers configuration. Follow current Microsoft Learn instructions for the authoring
surface. Check ingestion status, retrieve a known statement, and inspect the citation.
For URL knowledge, verify that the specific intended material is actually retrievable.
Do not assume adding a deep link imports that page verbatim.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio
