# Knowledge: choose the right evidence

**Start with one source and verify retrieval before adding more.** The files below have different
authority. Their descriptions help the agent choose relevant evidence.

| File | Suggested description | Boundary |
| --- | --- | --- |
| [ai901-concepts.txt](ai901-concepts.txt) | Original Contoso explanations of responsible AI, AI workloads, and Foundry agent concepts | Course-authored teaching text, not a complete syllabus |
| [ai901-objective-domain.md](ai901-objective-domain.md) | Dated Microsoft Learn AI-901 skills snapshot, including audience, domains, weights, and objectives | Check the live guide for current scope and availability |
| [contoso-ai-cert-challenge.md](contoso-ai-cert-challenge.md) | Fictional Contoso reward policy: first 50 qualifying employees, $100 each, with human verification | No real entitlement, live award count, or payment capability |
| [contoso-enablement-policy.txt](contoso-enablement-policy.txt) | Fictional rules for fixed study sessions, synthetic signups, fresh confirmation, and separate Teams announcements | No exam booking, verified pass, reward reservation, or human transfer |

## Optional upload and test

1. Follow [Microsoft's file knowledge procedure](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-file-upload).
   Add ai901-concepts.txt first and wait for its status to become Ready.
2. Request the six responsible AI principles. Inspect the answer and its supporting source.
3. Request an exact exam appointment time. Verify an honest limitation because these files contain no booking data.
4. Add the objective and policy files with their descriptions. Request the domains and the fictional
   challenge rules, checking that the response attributes each claim to the appropriate source.
5. Ask whether the company reward is a Microsoft rule. The answer must distinguish fictional policy
   from official exam requirements.

Keep evaluation answers, agent instructions, and native topic files out of general knowledge.
After editing a local knowledge file, update the tenant upload and repeat the relevant retrieval test.

All four files reported Ready in the instructor's environment. Ready establishes ingestion, not
correctness of every possible answer. Verify your own retrieval and source boundaries.

[Knowledge guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio) · [Current AI-901 guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)
