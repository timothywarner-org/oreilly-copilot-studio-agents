# Inspect genuine Copilot Studio topic YAML

**Status: native artifact NOT CAPTURED.** This directory contains instructions, not an exported agent. Do not rename an authored specification to `.yaml` or present it as a working export. The promised follow-up artifact is a genuine, sanitized topic capture from the rehearsed course agent. Capturing it is a **learner-distribution gate**.

## No-code inspection route

Microsoft documents that the topic canvas generates YAML automatically. This procedure captures that native topic configuration as a text file for inspection. It is **not** a full-agent solution export, portable deployment package, or claim that topic dependencies are included. [Use the topic code editor](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/topics-code-editor)

1. In the rehearsed standard-harness course agent, open **Topics** and the teach-check-handoff topic. Inspect its canvas and identify the question, answer variable, condition and mentor message.
2. Select **More (...) > Open code editor** on the topic toolbar. Read the generated configuration. Locate the corresponding question/message nodes, variables, conditions and any redirects or tool references. Do not assume a node exists simply because an authored specification mentions it.
3. Copy the genuine contents to a local file named `teach-check-handoff.native.yaml` in a private review location. Record capture date, agent checkpoint, topic name and source experience in a companion note. Use VS Code or another text editor to inspect it. No CLI extension is required.
4. Compare three lines or blocks with their canvas counterparts: where a learner answer is stored, where a condition reads it, and where the fallback redirects or displays a message. Explain why indentation and identifiers matter. Do not modify the agent to perform this reading exercise.
5. For an optional edit, first make a copy of the topic using the documented topic-copy feature. Change a harmless teaching message on the copy, inspect its YAML, select **Save**, return to the canvas, and test the copy. Save is documented for code-editor changes; this does not publish the agent. Keep the original rehearsed topic intact.
6. Sanitize the captured file before distribution: remove tenant/environment/user identifiers, connector and flow identifiers where sensitive, private source URLs, credentials, personal content, and internal paths. Inspect every property and companion note. Use clear placeholders only in the distribution copy and mark it **SANITIZED, INSPECTION ONLY** because replacement can break importability. Never upload private YAML to a public validator.
7. Put the reviewed capture and a brief provenance note in this directory only after the course owner approves it for learner distribution. Record what was redacted, the capture date and checkpoint, and whether any reimport was actually tested. If no reimport was tested, say so. Do not claim this topic snapshot can recreate knowledge, flow connections, environment policies or the complete agent.

## Completion check

A learner can open the actual captured file, identify a variable and condition, and compare it to the demonstrated topic. Until that file and its provenance note exist, the YAML follow-up promise remains **PENDING**, even though these instructions are complete.

Reference: [copy a topic](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-topic-management#copy-a-topic). If your tenant has a different harness or no code-editor option, record the actual surface and use a genuine instructor capture; do not invent an export button.
