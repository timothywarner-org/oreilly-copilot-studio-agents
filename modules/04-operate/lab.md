# Operate lab: Would you release it?

**Target:** LO4. **Submit:** a [pilot decision](worksheet.md), backed by observed evidence or explicitly labelled synthetic evidence. This is a no-code exercise. Procedures describe the **standard harness**; use the observer route if your tenant presents a different experience.

## 1. Predict, then observe

Use the Module 3 checkpoint. Twelve cases belong in the instructor's full rehearsal. The live slice is three: E04 (grounded explanation), E08 (valid `cloud` study session), and E05 (original practice question that waits for the learner). Use the canonical E05 prompt: "Teach me shared responsibility and give me one practice question." The native first-turn score is only one check: inspect the authored topic and Question-node trace to confirm it presents a question and withholds the answer key. In a separate manual test, invoke the same topic and then answer its question in that conversation to test feedback. Missing-input behavior also needs a separate interactive conversation because single-response evaluation does not simulate the learner's reply.

1. Before each prompt, write what must happen. For a cloud session, expect the actual **GetStudySession** tool to receive `focus=cloud`, return `status` and `plan`, and produce a 30-minute session. A plausible plan without the expected tool call fails this test.
2. Run those three prompts in new test conversations. Record the response and visible evidence. Inspect the cited source; count the plan minutes; verify the practice question stops before the answer.
3. Mark each case **PASS**, **FAIL**, **ERROR**, or **NOT RUN**. An unavailable service is an error, not a passing refusal. A result with no trace is insufficient evidence of tool execution.

## 2. Observe or run native evaluation

The instructor demonstrates these steps. Makers with the matching surface may follow; everyone else records the demonstration evidence.

1. Open the agent's **Evaluation** page. Select **New evaluation**, then **Single responses**. Choose **Import**, or **Or, write some questions yourself** if composing the three live prompts manually.
2. For CSV import, download the tenant's template and compare it with [the prepared three-case CSV](../../evals/native-live-three.csv). The documented headers, in order, are `Question` and `Expected response`. Use one question per row and at most 1,000 characters per question. The repository scenario JSON is not that import format. The prepared CSV has authored expectations and is not an executed result. Review imported text before running.
3. Name the set `AZ900-live-three`. Use **Compare meaning** for a reference answer and inspect the expected response. Add **Tool use** for the plan case and select the actual `GetStudySession` capability. We use an 80% meaning threshold as an initial teaching choice, not a Microsoft recommendation; manually inspect answer correctness and citations even when the grader passes.
4. Under **Additional configuration > Manage**, check the user and connections. Use an approved test identity with intended learner access. A maker's access does not establish a learner's access. Save and run using the tenant's displayed control.
5. Open a completed case. Read expected versus actual response and grading explanation; select **Show activity map**. Inspect knowledge and tool nodes, including actual inputs and outputs. Generated rationale is a troubleshooting aid, not proof that a claim is correct.
6. Compare two runs of the **same test set** using **Compare with**. Record the one change between runs and inspect improvements and regressions individually. Export actual results using **Export test results** from the results menu. Keep sensitive exports in the approved private evidence location.

**Recovery:** if native evaluation is unavailable or blocked, manually run the same prompts and label results **MANUAL TEST**. The instructor shows a dated genuine rehearsal capture for the native feature. If none exists, that native demonstration remains a delivery gap. Do not disable data policy to make a test pass.

Sources: [Create test sets](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create), [results and comparisons](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results), [activity review](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-review-activity).

## 3. Diagnose operational evidence

Read [the synthetic example](worked-example.md). Calculate resolution and no-escalation rates using the stated denominators. Identify why the superficially good containment number hides failure. Read the short transcript and name the smallest repair. Do not copy invented numbers into an actual evidence record.

In the real tenant, open **Monitor**, select the rehearsed reporting period, inspect outcome labels and a permitted transcript. **Test-panel traffic does not populate Monitor.** Analytics can take up to an hour after a session ends to appear; use precollected, sanitized channel evidence instead of waiting in class. Missing transcript permissions do not prove that no conversation occurred. [Monitor documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-summary)

## 4. Observe actual publishing

Predict: will saving a topic change the agent installed in Teams? No. It must be republished; existing conversations may need a new session.

Watch the instructor confirm authentication and authorized audience, publish, enable Teams, install for their own use, and test a fresh conversation. Record the actual result. Learners on trial accounts observe this step because their trial cannot publish. Follow the [instructor procedure](../../instructor/04-operate-guide.md). Learners publish only within their organization's approved scope.

## 5. Make the pilot decision in seven minutes

1. **Two minutes:** choose GO, CONDITIONAL, or NO-GO. CONDITIONAL means approval is pending and users do not start yet. Unknown access or untested publication blocks GO.
2. **Three minutes:** identify a control for each Well-Architected pillar, plus owner, audience, data boundary, and stop condition.
3. **Two minutes:** exchange the decision with a partner. Your partner names the missing evidence that would most change the decision. Revise your answer.

**Success check:** distinguish synthetic examples, manually observed results, native results, and unperformed checks. Follow-up includes [genuine topic YAML inspection](../../sample-agent/exports/README.md); no coding is required during class.
