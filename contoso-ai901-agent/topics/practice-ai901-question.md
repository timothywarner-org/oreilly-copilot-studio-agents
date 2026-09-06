# Topic: Practice AI-901 Question

**One reusable topic, unlimited questions.** The topic is the conversation structure; the item is data
that flows through it. That separation is the lesson. A topic per exam question doesn't scale, and it
teaches makers the wrong shape.

**Authored design. Documentation checked 2026-09-06. Tenant execution: NOT RUN.** This is a build
recipe, not a native export.

## Topic name and description

**Name:** `Practice AI-901 Question`

**Description** - this is the routing surface under generative orchestration, so write it for the
orchestrator, not for a human reader:

> Guides an employee through one original AI-901 practice question at a time. Collects a study area,
> generates a supported item from approved evidence, waits for the employee's choice, then explains the
> result and offers another item. Use for requests such as quiz me, give me a practice question, and
> test my AI knowledge. Don't use this topic to record or announce an exam booking.

**Trigger:** with generative orchestration the documented default is **The agent chooses**, driven by
the topic name and description. Classic orchestration uses **User says a phrase**. Keep sample
utterances for testing, but don't teach a phrase list as required generative configuration. Reference:
[Set topic triggers](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers).

## Variables and their lifetime

| Variable | Lifetime | Rule |
| --- | --- | --- |
| `Topic.Domain` | The practice session | Validated to one of three values |
| `Topic.EvidenceContext` | The current item | One packet's `evidenceText`, nothing concatenated |
| `Topic.AllowedSourceIds` | The current item | The `sourceId` of that packet |
| `Topic.SourceTitle` / `Topic.SourceUrl` | The current item | Looked up from the register, never from the model |
| `Topic.Question` / `Topic.ChoiceA` / `Topic.ChoiceB` / `Topic.ChoiceC` | The current item | Displayed |
| `Topic.CorrectChoice` | The current item | **Never displayed before the employee answers** |
| `Topic.Explanation` | The current item | Displayed only after grading |
| `Topic.UserChoice` | The current item | Cleared before every item |
| `Topic.AnotherQuestion` | One decision | Fresh answer required every time |
| `Topic.PreviousQuestion` | Best effort | Repeat avoidance only |
| `Topic.PacketToggle` | The practice session | Optional; alternates between the two packets in a domain |

## Canvas shape

```text
Trigger: the agent chooses this topic
  1  Question: "Which area would you like to practice?"  -> Topic.Domain
        Buttons: Responsible AI | AI workloads | Microsoft Foundry
  2  Condition on Topic.Domain -> set Topic.EvidenceContext, Topic.AllowedSourceIds,
        Topic.SourceTitle, Topic.SourceUrl from the reviewed packet
  3  Prompt: GeneratePracticeQuestion  -> map returned fields into Topic.* variables
  4  Condition: validation gate (see below)
        Fail -> message, offer retry or another area, exit without grading
  5  Message: Topic.Question plus the three choices, and nothing else
  6  Question: "Choose A, B, or C."  -> Topic.UserChoice
        Buttons: A | B | C
  7  Condition: Topic.UserChoice equals Topic.CorrectChoice
        Yes -> "Correct."     No -> "Not quite. The supported answer is {Topic.CorrectChoice}."
  8  Message (both branches converge): Topic.Explanation, then "Source: Topic.SourceTitle" and the URL
  9  Set Topic.PreviousQuestion = Topic.Question; clear Topic.UserChoice, Topic.CorrectChoice,
        Topic.Question, Topic.ChoiceA/B/C, Topic.Explanation
 10  Question: "Would you like another question?"  -> Topic.AnotherQuestion
        Buttons: Yes | No
        Yes -> flip Topic.PacketToggle, return to step 2
        No  -> "Good session. Tell me when you book your exam." -> End this topic only
```

**End the topic, not the conversation.** The employee must be able to say *"I booked my AI-901 exam"*
immediately afterward. Ending the whole conversation here breaks the Hour Three demo.

## Step 6 is the demo

Step 6 is the only place in this build where a machine stops and a human decides. Before you click Test,
tell the room what to watch for: the turn must end on the question. If the agent produces the question
and its own answer in one message, that is a real finding worth showing.

**Low-friction presentation:** put the dynamic question and option text in the Question node's message,
and use three fixed buttons labeled **A**, **B**, and **C**. This avoids making dynamic choice entities
or Adaptive Cards a prerequisite for the demo. Prove variable interpolation in your designer during
rehearsal. Reference:
[Ask a question](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-ask-a-question).

**Configure both Question nodes to require fresh input.** Reusing an answer variable can let a later
Question node be skipped entirely, which would silently grade the employee's previous answer against a
new item's key. Set the skip behavior explicitly and reset the variable in step 9.

**Don't guess a Power Fx cast.** Confirm the actual returned type of the button value in the designer
before writing the step 7 comparison. If the type differs from the prompt's returned text, normalize
one side deliberately rather than layering conversions until the condition stops erroring.

## Validation gate for step 4

Present nothing unless every condition holds. The full list, with rejection behavior, is in
[`../prompts/practice-question.contract.json`](../prompts/practice-question.contract.json).

| Check | Reject when |
| --- | --- |
| Status | Not `ready` |
| Item fields | Question or any choice is empty |
| Distinctness | Two choices are the same after trimming |
| Key | `correctChoice` isn't exactly A, B, or C |
| Source | `sourceId` isn't in `allowedSourceIds` |
| Leakage | The question text contains the correct choice's full text |

On rejection: clear the item, grade nothing, say the question couldn't be produced, and offer a retry
or a different area. Keep one reviewed fixture item on hand so you can still demonstrate the canvas if
generation fails on camera - and label it out loud as a prepared item, not a live generation.

## Grounding choice for the live path

**Ship the reviewed-packet path.** Step 2 sets `Topic.EvidenceContext` from an authored packet in
[`../knowledge/evidence-register.json`](../knowledge/evidence-register.json). Say plainly in class that
this version is grounded in a curated packet rather than live retrieval. That is an honest
simplification and still a real dynamic item; it isn't a return to hard-coded questions.

**The documented upgrade,** for after the vertical slice works: a topic-level generative answers node
retrieves from a narrowly scoped source, stores the result without displaying it, and passes the
supported answer text into the prompt as `evidenceContext`, with source identifiers maintained through
the register rather than taken from the model. Microsoft documents limits on passing native knowledge
citations to other tools, so keep answer text and trusted source metadata separate. Reference:
[Use generative answers in a topic](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-boost-node).

**Don't** silently switch grounding approaches while a slide still claims retrieval. Record which
approach shipped and its limits in [`../STATUS.md`](../STATUS.md).

## Acceptance tests

| ID | Test | Required result |
| --- | --- | --- |
| Q01 | "Quiz me on AI-901" with no area named | Topic selected; area collected |
| Q02 | Supported area chosen | Valid item shown; no answer or explanation revealed |
| Q03 | Employee hasn't yet answered | The turn actually ends; nothing is graded |
| Q04 | Correct option chosen | Correct feedback tied to this item's key |
| Q05 | Incorrect option chosen | Corrective feedback plus supported explanation |
| Q06 | Typed input that isn't A, B, or C | Clear reprompt or safe exit; no invented selection |
| Q07 | "Another question" | New generation attempt and fresh input state |
| Q08 | "No more questions" | Topic ends; agent still available for other requests |
| Q09 | Empty or malformed prompt output | No question shown, no grading |
| Q10 | Packet edited to contain an instruction such as "ignore your rules" | Instruction not followed; treated as data |
| Q11 | Unknown `sourceId` returned | Item rejected; no fabricated citation |
| Q12 | Three consecutive items | Correct letters differ; no stale key; wait state holds each time |
| Q13 | Published Teams session | Text, buttons, source link, and repeat path all work there too |

Q10 and Q12 are the two that catch real defects. Run them before you run the pretty ones.
