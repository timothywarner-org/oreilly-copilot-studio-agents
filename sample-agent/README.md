# AZ-900 Cert-Prep Assistant — sample design

This folder contains a **design and authoring kit**, not an importable Copilot Studio solution.
Create the actual shell in your environment and use these reviewed inputs there.

| Material | Use |
| --- | --- |
| [instructions.md](instructions.md) | Agent instruction draft to paste and test |
| [topic-map.json](topic-map.json) | Routing design; not native Copilot Studio YAML |
| [knowledge/upload-metadata.md](knowledge/upload-metadata.md) | Explicit scope for each knowledge source |
| [tools/study-plan-contract.json](tools/study-plan-contract.json) | Portable input contract for the bounded tool |
| [tools/flow-design.md](tools/flow-design.md) | No-code agent-flow implementation and verification plan |
| [tools/extension-decisions.md](tools/extension-decisions.md) | Actions versus flows versus MCP versus agent handoff |

No tenant bindings, secrets, connection references, or imported publisher assets are included.
The local reference function is separate from the agent; binding it to a live tool is an instructor task.
