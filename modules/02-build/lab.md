# Build exercise: trace the RAI question

**Seven minutes. No account required.** Use the [worksheet](worksheet.md) and
[RAI Single Question Demo](../../contoso-ai901-agent/topics/rai-single-question-demo.md).

The topic presents a Contoso hiring scenario with four labeled choices. It saves one answer, computes
a Boolean, and follows a feedback branch. The key appears only after the student responds.

1. Predict CorrectAnswer, StudentAnswer, and IsCorrect after choosing **A**.
2. Trace the branch and rewrite the corrective feedback in your own words.
3. Repeat the prediction for **B**. Explain exactly which node makes the conversation wait.
4. Separate the fixed topic message from a generated answer that retrieves a knowledge source.

## Worked answer

| Selection | CorrectAnswer | StudentAnswer | IsCorrect | Branch |
| --- | --- | --- | --- | --- |
| A | B | A | false | All other conditions, corrective feedback |
| B | B | B | true | Correct-feedback branch |

The **Question** node saves StudentAnswer and always prompts. A question mark in a Message node
does not create the same wait point. The Set variable expression converts the choice to text before
comparing it with the saved key. The condition uses the resulting Boolean.

**Corrective explanation:** Equally qualified applicants receive different treatment across groups,
which identifies fairness. Transparency concerns understanding decisions.

## Optional independent practice

1. Add [ai901-concepts.txt](../../contoso-ai901-agent/knowledge/ai901-concepts.txt) as knowledge using the
   [source descriptions](../../contoso-ai901-agent/knowledge/upload-metadata.md). Wait for Ready, then
   request the six responsible AI principles and inspect the supporting citation.
2. Request an exact exam appointment time. No source in the kit supplies that personal information.
   Verify that the agent states the limitation.
3. Build the fixed topic from [the learner walkthrough](../../contoso-ai901-agent/topics/rai-single-question-demo.md).
   Test A and B in fresh conversations, inspect the three variables, and verify that the topic ends.
4. Compare your canvas with the [saved native source](../../contoso-ai901-agent/topics/exports/rai-single-question.native.yaml).
   Source inspection is optional and requires no programming.

**Success:** A source supports the generated answer; the fixed topic pauses; each choice follows the
appropriate feedback branch. Mark any unexecuted check **NOT RUN**.

[Topic documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics) · [Variables documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-variables)
