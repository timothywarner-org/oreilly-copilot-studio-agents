# AZ-900 Cert-Prep Assistant — sample design

This folder contains a **design and authoring kit**, not an importable Copilot Studio solution.
Create the actual shell in your environment and use these reviewed inputs there.

| Material | Use |
| --- | --- |
| [instructions.md](instructions.md) | Agent instruction draft to paste and test |
| [topic-map.json](topic-map.json) | Routing design; not native Copilot Studio YAML |
| [knowledge/upload-metadata.md](knowledge/upload-metadata.md) | Explicit scope for each knowledge source |
| [tools/core-study-session.md](tools/core-study-session.md) | Core GetStudySession flow, one focus and a fixed 30-minute plan |
| [tools/study-plan-contract.json](tools/study-plan-contract.json) | Optional advanced multi-day input contract |
| [tools/flow-design.md](tools/flow-design.md) | Optional advanced no-code implementation plan |
| [tools/extension-decisions.md](tools/extension-decisions.md) | Actions versus flows versus MCP versus agent handoff |

No tenant bindings, secrets, connection references, or imported publisher assets are included.
The optional local reference function implements the advanced multi-day design. The live lesson uses the simpler native GetStudySession flow. Neither document establishes a deployed agent.
