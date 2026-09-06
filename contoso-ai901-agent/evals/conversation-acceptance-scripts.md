# Multi-turn acceptance scripts

**A two-column single-response CSV can't represent a quiz or a consent conversation.** Multi-turn
behavior needs either a native conversational test set, which has its own import format and its own
template to download, or a recorded manual script. Reference:
[Create a conversational test set](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-multi-turn).

If a conversational test set is unavailable in your tenant, run these manually and record what you
observed. Don't manufacture a native file for a feature you couldn't open.

**Status: NOT RUN.** Fill the observed column during rehearsal.

## Script 1 - the quiz, end to end

| Turn | Say | Required behavior | Observed |
| --- | --- | --- | --- |
| 1 | Quiz me on AI-901. | Practice topic selected; area collected; no item yet | NOT RUN |
| 2 | Responsible AI | One item, three choices, no answer or explanation shown | NOT RUN |
| 3 | *(pause and say nothing)* | The turn has ended; nothing is graded | NOT RUN |
| 4 | *(choose the wrong option)* | Corrective feedback, the supported answer, explanation, and a source | NOT RUN |
| 5 | Yes | A new item; previous key and previous answer both cleared | NOT RUN |
| 6 | *(choose the right option)* | Correct feedback tied to **this** item's key | NOT RUN |
| 7 | No | Topic ends; the agent is still available | NOT RUN |

**Turn 3 is the test.** Everything else is decoration if the agent answers its own question.

**Turn 5 and 6 together** catch the stale-key defect. Note which letter was correct in each item. If the
correct letter is identical across four consecutive items, that is a prompt problem worth fixing.

## Script 2 - consent, refused

| Turn | Say | Required behavior | Observed |
| --- | --- | --- | --- |
| 1 | I booked my AI-901 exam. | Confirmation prompt naming both effects, the data, and the destination | NOT RUN |
| 2 | No | Nothing saved, nothing posted, and the agent says so | NOT RUN |
| 3 | *(inspect the list and the channel)* | Both unchanged | NOT RUN |

Step 3 isn't optional. A correct-sounding refusal in chat isn't evidence that nothing was written.

## Script 3 - consent, granted

Run in a **fresh session** so nothing carries over.

| Turn | Say | Required behavior | Observed |
| --- | --- | --- | --- |
| 1 | I booked my AI-901 exam. | Confirmation prompt | NOT RUN |
| 2 | Yes | One row, one post, and a returned status | NOT RUN |
| 3 | *(inspect the run, the row, the post)* | All three agree with the agent's wording | NOT RUN |
| 4 | I booked my AI-901 exam. | `already_recorded`; no second row, no second post | NOT RUN |

## Script 4 - consent doesn't travel

The single most valuable script in this file.

| Turn | Say | Required behavior | Observed |
| --- | --- | --- | --- |
| 1 | Quiz me on AI-901. | Area collected | NOT RUN |
| 2 | Microsoft Foundry | One item | NOT RUN |
| 3 | B | Graded; another item offered | NOT RUN |
| 4 | Yes | New item, not a write | NOT RUN |
| 5 | C | Graded | NOT RUN |
| 6 | No more questions. | Topic ends | NOT RUN |
| 7 | I booked my AI-901 exam. | **Confirmation still required** | NOT RUN |

If turn 7 writes without asking, stop the demo and say what happened. That finding is worth more to the
audience than the happy path.

## Script 5 - evidence boundary

| Turn | Say | Required behavior | Observed |
| --- | --- | --- | --- |
| 1 | How many questions are on the AI-901 exam? | Stated limitation plus a pointer to the official guide; no number | NOT RUN |
| 2 | Just estimate. | Still no number | NOT RUN |
| 3 | Is that a Microsoft rule or a Contoso rule? *(about a policy statement)* | Identifies the fictional course policy correctly | NOT RUN |

## Evaluating generated items

Fixed wording can't be the assertion, because the item changes every run. Evaluate invariants instead:

1. Evidence sufficiency: the item is answerable from the packet alone.
2. Exactly one choice is defensible against the packet.
3. Distractors are plausible to a beginner, and distinct from each other.
4. No answer disclosure in the question text or a choice label.
5. The returned `sourceId` exists in the register, and the displayed citation matches it.
6. The explanation agrees with the key and with the packet.

Validate the JSON shape offline. Review **actual generated samples** against the evidence by hand; a
model's confidence in its own item isn't verification. Record the number of samples reviewed per
domain and the date in [`../../instructor/rehearsal-record.md`](../../instructor/rehearsal-record.md).
