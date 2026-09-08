# Contoso AI Fundamentals Coach: learner examples

**One fictional employee-learning agent, studied across all four modules.** Use these files to
understand the demonstration and adapt the design in your own approved environment. They are not
an importable complete agent or a connection to the instructor's tenant.

## Explore in this order

| Example | What to inspect |
| --- | --- |
| [Agent brief](agent-brief.md) | User, job, boundaries, and observable success criteria |
| [Instructions](instructions.md) | Role, source hierarchy, practice behavior, and fresh signup confirmation |
| [Knowledge descriptions](knowledge/upload-metadata.md) | Which sources are official, original, or fictional |
| [RAI Single Question Demo](topics/rai-single-question-demo.md) | Four choices, three variables, a condition, and feedback |
| [GetStudySession](tools/get-study-session.md) | One input and two outputs for a fixed 30-minute session |
| [Signup event](signup-trigger-2026-09-08.md) | A new SharePoint row causes a separate Teams announcement |
| [Extension decisions](tools/extension-decisions.md) | When to use a tool, MCP, another agent, or a human referral |
| [Evaluation files](evals/README.md) | Reference answers, expected capabilities, and checks that need conversation traces |
| [Native topic inspection](topics/exports/README.md) | Compare the fixed RAI topic with the generated practice topic |
| [Icons](assets/icons/README.md) | Use the supplied artwork in a personal learning build |

## Requests used in the demonstration

- `What are the six responsible AI principles?`
- `Give me a sample question on RAI.`
- `Give me a 30-minute study session for responsible-ai.`
- `Sign me up for AI-901.`
- `How does the fictional Contoso $100 challenge work?`

The fixed RAI question is the simplest way to study normal topic flow. The generated practice
topic is a separate advanced example that depends on a prompt resource. Keep the first build small.

## What was observed

The instructor tested both fixed RAI answer branches on September 8. A new synthetic signup also
completed the independent notification flow to **Contoso Ltd Community > General** that morning.
The source list was **Certification Signups** on **Contoso HR Portal**. The coach was republished
with the matching confirmation wording. These observations do not establish access or behavior in
another tenant, and the shipped evaluation CSVs are reference answers rather than passing results.

The instructions describe the completed demonstration. Configure and test the named capabilities
before retaining claims about them in your own agent. The signup records a study intention. It does
not book an exam, verify a pass, reserve a reward, or send a payment.
