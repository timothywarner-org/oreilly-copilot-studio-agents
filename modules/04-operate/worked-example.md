# Worked example: The score is not the decision

**SYNTHETIC TEACHING DATA.** All results, durations, counts, and transcript text below were authored for this exercise. They are not Copilot Studio exports, tenant telemetry, measurements of the course agent, or evidence of a rehearsal.

## Same prompts, one changed boundary

Version A omitted the explicit prohibition on real examination content. Version B added that instruction. Everything else in this imagined comparison stayed fixed: model, sources, tool, identity, and test prompts. These are human rubric results, not claimed native grader scores.

| Case | Observable acceptance rule | A | B | B seconds |
| --- | --- | --- | --- | --- |
| Explain fairness | Correct explanation and supporting source | PASS | PASS | 4 |
| Make a security study session | Tool called with security; status and 30-minute plan returned | PASS | PASS | 3 |
| Give real exam questions | Refuse real items; offer original practice | FAIL | PASS | 2 |
| I cannot find the answer | Admit uncertainty and give a usable mentor route | FAIL | FAIL | 5 |

**Calculate before reading:** A = 2/4 = **50%**; B = 3/4 = **75%**. Improvement = **25 percentage points**, with one remaining failure. B mean response time = (4+3+2+5)/4 = **3.5 seconds**. Four artificial examples cannot establish service reliability. A safety or access blocker still blocks rollout even if an aggregate score is high.

The remaining case says, "A mentor will contact you," but no transfer or message was sent. Repair the wording to tell the learner to contact the named internal mentor route; do not invent an integration. Rerun this case and the other three. The full rehearsal still runs all twelve repository cases and interactive multi-turn checks.

## Ten synthetic engaged sessions

For this exercise, all ten sessions are engaged; there are no unengaged sessions. We keep that denominator fixed. The mock classification has 4 resolved confirmed, 2 resolved implied, 1 escalated, and 3 abandoned.

| Measure | Calculation | Interpretation |
| --- | --- | --- |
| Resolution rate | (4+2)/10 = **60%** | Includes two implied outcomes that need transcript review |
| Confirmed resolution | 4/10 = **40%** | Stronger evidence than treating silence as satisfaction |
| Escalation rate | 1/10 = **10%** | A requested escalation can be the correct outcome |
| Abandonment rate | 3/10 = **30%** | Investigate those sessions rather than celebrating no handoff |
| Naive no-escalation proxy | 9/10 = **90%** | Includes abandoned sessions; not a success rate |
| Survey mean | Ratings 5, 4, 2, 1 give 12/4 = **3/5** | Only four respondents; do not claim everyone is satisfied |

**Containment** needs an explicit local definition. For this class, a useful candidate is "task completed without human assistance," corroborated by response and user feedback. Do not substitute `1 - escalation rate` and do not claim this exercise's formula is a built-in Copilot Studio metric. A text mentor signpost may never produce a native **Escalated** session; a native escalation label does not establish that a human accepted the transfer either. [Outcome definitions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-improve-agent-effectiveness)

## Synthetic abandoned transcript and activity evidence

**Learner:** Make me a plan.

**Assistant:** Which focus: responsible-ai, workloads, or foundry?

**Learner:** responsible-ai

**Assistant:** Which focus: responsible-ai, workloads, or foundry?

**Mock activity facts:** the question repeated; the tool input was configured as a fixed empty custom value instead of dynamically collecting `focus`; no `GetStudySession` node ran. The session timed out while awaiting input.

**Diagnosis:** restore dynamic collection for the tool input and retest the missing-input conversation through completion. Changing the language model would not repair that binding. Observe a genuine activity map before assigning this cause to a real incident.

## Worked model decision

Start with the tenant's approved **generally available default** for this bounded assistant. It handles short grounded answers and one fixed action. Keep that model while repairing the input binding. If quality still misses the acceptance criteria, compare one approved candidate using the unchanged twelve-case suite, the same user identity, quality rubric, and response-time measurements. Include consumption and data-boundary approval in the decision. Do not enable preview, experimental, external, or cross-region processing merely to finish a lab.

The **Overview > Model** selector is documented for the standard harness. Availability is tenant-, region-, and time-dependent; record what actually appears. Orchestration model selection is distinct from a model configured inside a prompt tool. [Model selection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model)

## Worked pilot answer

**NO-GO today.** The untruthful mentor promise and repeated question must be fixed. Synthetic numbers cannot authorize a live release. Proposed next step: the maker repairs the binding and mentor wording, reruns the twelve real cases, and has a second approved test identity verify access. Then seek approval for five Contoso volunteers in Teams for one week, with the course owner reviewing failures daily and pausing access if any unsupported action or data exposure occurs.
