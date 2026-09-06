# Environment and feature preflight

**No tenant configuration has been verified by this repository.**
The June proposal’s terminology is preserved in the course; current product documentation is checked separately.

## Product surface to verify

Microsoft’s **Create and delete agents** page, updated September 1, 2026, now describes the
**standard harness** and says to turn off **New experience** for that authoring route.
This matters because the course explicitly uses topics, knowledge, tools, and orchestration.
Rehearse the documented surface in your actual tenant rather than silently swapping in a different agent experience.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot

## Access, cost, and policy

The published preparation requires a Microsoft 365 work or trial account with Copilot Studio access.
Trial availability and permissions vary. Microsoft documents a build/test versus publish distinction;
do not advertise publication as available merely because agent creation succeeds.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions

Check the environment role, current license/credit entitlement, data policies, allowed connectors,
authentication, and model availability with the tenant administrator. Do not bypass a restriction.
There is no Azure subscription requirement for this repo’s local reference demo.

## Knowledge

Agent-level knowledge and a topic-level generative answers node are distinct configuration choices.
A citation must support the answer, not merely look plausible. Check ingestion readiness and retrieval
in your environment. Preserve source descriptions and the distinction between original synthetic
training policy and Microsoft’s authoritative certification documentation.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio

## MCP and evaluation

MCP is an extension mechanism, not permission to use every exposed tool. Pick one allowed endpoint,
review its authentication and tools, and record what the agent may actually call.
The repository does not start a server or bind any endpoint automatically.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp

The JSON scenarios under `evals/` are a portable planning format, **not a claim of compatibility with
Copilot Studio’s current native test-set import schema**. Follow the current native format after checking
Microsoft’s documentation. Use anonymized evidence, and do not commit conversation transcripts.

Source: https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro
