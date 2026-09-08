# RAI Single Question Demo

**Purpose:** Show a normal Copilot Studio topic: capture one answer, store variables, evaluate a
condition, and give feedback. This is a fixed, original responsible AI practice item for the
Contoso AI Fundamentals Coach. It does not call a prompt, flow, or connector.

**Student entry:** `Give me a sample question on RAI.`

## The question

Contoso uses an AI system to shortlist job applicants. Equally qualified applicants from one
demographic group are consistently rejected more often than applicants from another group.
Which responsible AI principle most directly addresses this unequal treatment?

- **A.** Transparency
- **B.** Fairness
- **C.** Privacy and security
- **D.** Reliability and safety

**Answer key: B. Fairness.** The live topic waits for a response before revealing the key or explanation.
The concept is grounded in [Microsoft Learn: What is Responsible AI?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai?view=azureml-api-2),
checked September 8, 2026. The scenario and feedback are newly authored teaching content, not a real exam item.

## Variables to show

| Topic variable | Type | Purpose |
| --- | --- | --- |
| `CorrectAnswer` | String | Set to `B` before the question |
| `StudentAnswer` | Choice | Stores the single A, B, C, or D selection |
| `IsCorrect` | Boolean | Stores the result of comparing the selected letter with the key |

The Set variable node uses `Text(Topic.StudentAnswer) = Topic.CorrectAnswer`. The conversion matters:
the Question node produces a choice value, while the saved key is a string. The Condition checks
`Topic.IsCorrect = true` and selects the correct-feedback branch or **All other conditions**.

## Optional canvas construction

1. Create a blank topic named **RAI Single Question Demo**. Describe it as one original responsible AI
   question with a required answer before feedback. Use the entry phrase above for testing.
2. Add a Set variable node for **CorrectAnswer**, with the text value **B**.
3. Add a Question node containing the scenario and four choices above. Use multiple-choice options
   **A**, **B**, **C**, and **D**; save the answer as **StudentAnswer** and configure it to always prompt.
4. Set **IsCorrect** using the expression in the variables section. Add the true condition and an
   all-other-values branch. Put correct and corrective messages in the respective branches.
5. Join the branches at the source-backed explanation, then add **End all topics**. Save and test.

The [native capture](exports/rai-single-question.native.yaml) shows the exact saved node structure.
Use your tenant's native controls and [Microsoft's topic guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics)
if labels differ. No coding is required for this canvas exercise.

## Trace the topic, then try it yourself

1. Open **RAI Single Question Demo** under the coach's **Topics**.
2. Show **CorrectAnswer** being assigned `B` and the Question node saving **StudentAnswer**.
3. In the test pane's **More** menu, enable **Track between topics** and disable **Show activity map
   when testing** to keep the normal topic canvas visible. Enter the student phrase above and pause
   before selecting an option.
4. Predict **IsCorrect** and the branch taken for A, then submit A.
5. Start a fresh test session, repeat the phrase, and select B to demonstrate the other branch.
6. Trace the shared explanation and Microsoft Learn link through **End all topics**.

For live values, use **Variables on the topic toolbar > Test > Topic (3)**. That panel showed
`CorrectAnswer = B`, `StudentAnswer = B`, and `IsCorrect = true` in the verified correct-answer run.
The separate Variables button inside the test-chat pane did not show these topic values.

The final node ends the active topic stack so the orchestrator does not immediately repeat the
question. It does not write a grade, create a signup, or clear global variables. There are no topic
inputs that could automatically fill the answer, and the Question node always prompts.

The [saved native source](exports/rai-single-question.native.yaml) is available for inspection.
See [Microsoft's topic guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics),
[variables guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables),
and [topic ending behavior](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-topic-management#end-the-current-topic-or-all-topics)
for the product mechanics.

## Tenant verification, September 8

- The native topic checker reported **zero errors and zero warnings**.
- Both `Give me a sample question on RAI.` and `Quiz me on responsible AI.` reached this topic.
- The question displayed four separately spaced options and waited without revealing the answer key.
- Selecting **A** took **All other conditions**, explained the correction, cited Microsoft Learn,
  and ended without repeating the question.
- Selecting **B** took the correct branch, displayed the expected variable values, cited the source,
  and ended without repeating the question.
- **Track between topics** showed the actual nodes and branch being executed.

These are maker-test observations. Separate Teams-channel playback and a native evaluation-set
update for this fixed topic were not performed during that test.
