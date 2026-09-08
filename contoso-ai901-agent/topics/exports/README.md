# Inspect the native topics

**Read the saved conversation structure alongside the visual canvas.** These are native topic
captures, not a complete agent solution or proof that another tenant can run them unchanged.

| File | What to trace | Dependency boundary |
| --- | --- | --- |
| [RAI Single Question Demo](rai-single-question.native.yaml) | One fixed four-choice question, CorrectAnswer, StudentAnswer, IsCorrect, two feedback branches, and End all topics | No external tool or tenant binding; portability to another agent has not been tested |
| [Practice AI-901 Question](practice-ai901-question.native.yaml) | Study-area selection, evidence, generated three-choice item, answer wait, saved-key grading, citation, and repeat loop | The prompt binding is redacted as `<PROMPT_ID_REDACTED>`; a separate prompt resource is required |

The fixed topic was saved and tested in the instructor tenant on September 8. The generated topic
was captured September 7 after native checker and conversation tests. The redaction and header
comments are identified in the generated-topic file. No credentials or live connector bindings are included.

Start with [the fixed-topic walkthrough](../rai-single-question-demo.md). Identify the Question node
that pauses, the variable that records the choice, and the condition that selects feedback. Then
compare the more complex generated example. A successful checker does not establish practice-item quality.

[Microsoft topic guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-create-edit-topics)
