# Operate exercise: would you release it?

**Seven-minute decision, no account required.** Use the [worksheet](worksheet.md). Label every result
as observed, a prediction, a manual test, or a synthetic exercise.

## Predict and inspect

Start with the [five-case reference set](../../contoso-ai901-agent/evals/native-core-five.csv): grounded
principles, a Foundry distinction, refusal of real exam items, a practice opener, and signup confirmation.
The [evaluation guide](../../contoso-ai901-agent/evals/README.md) explains the separate methods and sets.

1. Write what each response must contain and what it must avoid.
2. Compare the actual response with its reference and source. Record PASS, FAIL, ERROR, or NOT RUN.
3. For tool/topic routing, inspect the expected capability and actual activity. A matching sentence
   does not prove GetStudySession ran or that a writing flow waited for consent.
4. Test the RAI topic's answer and feedback interactively. A single-response score cannot test the
   full conversation. Test signup cancellation separately and inspect for no new row or post.

## Optional native evaluation practice

Follow [Microsoft's single-response evaluation procedure](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create).
Compare the native template with the supplied CSV before importing. Review reference answers,
methods, expected capabilities, test identity, and connections before running.

Use **Compare meaning** for answer comparison and a separate **Tool use** set for expected capabilities.
Our 80% comparison threshold is an authored teaching choice. Inspect failures and arguments manually.
Compare the same cases before and after one change, keeping each set and method's denominator visible.

See [evaluation results](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results)
and [activity review](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-review-activity).

## Make the pilot decision

1. Read the [synthetic operational example](worked-example.md). Calculate its rates and identify the
   unfulfilled promise. The figures are invented learning data, not measurements of the course agent.
2. Choose **GO**, **CONDITIONAL**, or **NO-GO**. For CONDITIONAL, users wait until the named conditions are met.
3. Record audience, owner, data boundary, access checks, stop condition, and recovery plan.
4. Name a concrete control for each [Power Platform Well-Architected concern](https://learn.microsoft.com/en-us/power-platform/well-architected/).
5. Name the missing evidence that could change your decision.

**Publication check:** Saving changes and publishing them are separate operations. Inspect the actual
published version and test a new channel conversation using an intended user identity. A maker's test
does not establish another person's access. Trials cannot publish; use the [access guide](../../learner/access.md)
and [Microsoft publication guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels).

**Success:** Your decision distinguishes response quality, successful effects, and usable access.
Never infer production readiness from a single successful demo.
