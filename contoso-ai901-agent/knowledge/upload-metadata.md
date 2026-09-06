# Knowledge upload metadata

**Start with one source.** Adding a source isn't proof that retrieval works, and three sources on a
cold tenant is three ways for the first demo to fail. Add `ai901-concepts.txt` first, prove a known
statement comes back, then add the rest.

| Source | Suggested description | Don't use it for |
| --- | --- | --- |
| [`ai901-concepts.txt`](ai901-concepts.txt) | Original Contoso course reference for responsible AI principles, AI workload shapes, and Microsoft Foundry agent types. Use first for concept questions. | A complete AI-901 syllabus, an official Microsoft document, current exam weights, or exam policy. |
| [`contoso-enablement-policy.txt`](contoso-enablement-policy.txt) | FICTIONAL Contoso rules defining what the coach's tools accept, the consent requirement before recording a milestone, and the actions it refuses. | Microsoft policy, real employee entitlements, or an actual support service. |
| Microsoft Learn AI-901 study guide | Official current scope of Microsoft Certified: Azure AI Fundamentals. Use for questions about what the exam covers. Prefer the source's own current wording. | Guessing exam items, predicting a score, or promising an administrative outcome. |
| [`evidence-register.json`](evidence-register.json) | Not uploaded as agent knowledge. Its packets are passed into the practice-question prompt by the topic, and its source mapping is used to display a citation. | Agent-wide retrieval. Keep it out of the general knowledge scope so a concept answer can't leak an answer key. |

## Verification, in order

1. Add the source, then wait for ingestion to report ready. A source that is still processing isn't a
   configuration bug.
2. **Retrieve a known statement.** Ask something the file answers plainly, such as
   *"What are the six responsible AI principles?"* Confirm the six named principles come back.
3. **Inspect the citation.** Confirm the response attributes the answer to the source you added, in a
   channel that supports citations.
4. **Test the boundary.** Ask something the file doesn't cover, such as *"How many questions are on
   the exam?"* Confirm you get a stated limitation and a pointer to the official guide, not a number.
5. **Test the fictional-policy boundary.** Ask *"Is that a Microsoft rule?"* about a policy statement.
   Confirm the agent identifies it as the course scenario's invented rule.

Step 4 is the demo. A source that answers what it knows is unremarkable; a source that refuses what it
doesn't know is the thing your audience came to see.

## Scoping the AI-901 study guide

Inspect the study guide as a human reference. For a URL knowledge source, verify that the specific
intended material is actually retrievable rather than assuming a deep link imports that page verbatim,
and follow the URL constraints recorded in the
[Build guide](../../instructor/02-build-guide.md). Restrict the source scope and the general-knowledge
fallback so a concept answer can't quietly become a general web answer.

Add permitted sources under **Knowledge**, or within a topic-level generative answers configuration
when you want the retrieval bounded to one topic. Follow current Microsoft Learn instructions for the
authoring surface your tenant presents.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio
