# Evaluate your agent

**Reference answers and scenarios are not observed results.** Use these materials to test your own
configuration and keep actual responses in a private evidence record.

| Resource | Use |
| --- | --- |
| [Twelve review scenarios](cases.json) | Human-reviewed checks mapped to the four objectives |
| [Blank results record](results.template.json) | Starts every case at NOT RUN |
| [Native evaluation files and guide](../contoso-ai901-agent/evals/README.md) | Five-case answer check, three-case routing check, and 32-case knowledge/challenge set |
| [RAI topic walkthrough](../contoso-ai901-agent/topics/rai-single-question-demo.md) | Interactive tests of waiting, variables, and feedback |

1. Copy the blank record to your own private working location.
2. Execute the case in the actual configured agent, recording source, version, identity, and date.
3. Inspect citations, topic branches, and tool input/output as applicable.
4. Record PASS, FAIL, BLOCKED, or NOT RUN and the supporting observation.
5. Repair a failure, rerun that case, and check related behavior for regressions.

The twelve-case JSON is a portable review format, not a Copilot Studio import schema. Native CSVs
use the documented two-column format, with methods and expected tools configured separately.
The five-, three-, and 32-case sets overlap; do not add their counts into a unique coverage claim.

E05 requires a multi-turn RAI test. E07's direct override prompt alone does not test retrieval injection.
E11's request to lie about a failure alone does not establish runtime failure handling. Record those
controlled variants separately. The signup affirmative path creates effects and requires its own
synthetic-data test; first-turn confirmation scoring does not prove absence of a write.

[Microsoft agent evaluations](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro)
