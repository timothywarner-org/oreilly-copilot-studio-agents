# Topic: Record Exam Milestone

**This topic exists to enforce one boundary: no write without consent in the current turn.** It is a
thin wrapper around the flow, not a second topic-authoring lesson. Build it in about four minutes.

**Authored design. Documentation checked 2026-09-06. Tenant execution: NOT RUN.**

## Why a topic instead of an instruction sentence

An instruction sentence asking the model to confirm first is a preference, not a gate. The model can
skip it, and it can populate a `confirmed` input from inference. A topic makes the confirmation a real
turn boundary that you can see in the transcript and point at on camera.

The flow still validates `confirmed` defensively. A boolean the model can fabricate isn't a security
boundary on its own - say that out loud rather than implying the topic makes the write safe.

## Topic name and description

**Name:** `Record Exam Milestone`

**Description:**

> Handles an employee reporting that they booked the Azure AI Fundamentals exam. Describes what will be
> saved and posted, obtains explicit confirmation in the current turn, then calls RecordExamMilestone
> and reports the actual returned status. Don't use this topic to answer study questions, and don't
> use it to book an exam.

## Canvas shape

```text
Trigger: the agent chooses this topic
  1  Message: "Congratulations."
  2  Question: "May I save your self-reported AI-901 booking to the Contoso demo milestone list and
        post your display name and exam code to the Certification Milestones demo channel?"
        -> Topic.MilestoneConsent      Buttons: Yes | No
        Require fresh input. Don't reuse any earlier answer variable.
  3  Condition: Topic.MilestoneConsent equals Yes
        No -> "Nothing was saved and nothing was posted." -> End topic
  4  Set Topic.LearnerDisplayName from the trusted identity source configured for this demo
  5  Tool: RecordExamMilestone(examCode: "AI-901", learnerKey, learnerDisplayName, confirmed: true)
  6  Condition on the returned status -> one message per status, wording from the status table
  7  End topic
```

## The confirmation sentence, and why it is worded that way

The confirmation names **both** effects, the **information** involved, and the **fixed destination**.
An employee who says yes to "may I record this?" hasn't agreed to a broadcast. Read the sentence in
step 2 back to yourself and check that a reasonable person could predict every consequence from it.

If the employee wants the record without the announcement, say the current demo performs both together
and offer to skip entirely. A record-only branch is a clean optional extension, not something to
improvise live.

## Status to wording map

Bind each message to the returned status. Never write a message that a status doesn't support. Full
definitions: [`../tools/milestone-result.contract.json`](../tools/milestone-result.contract.json).

| Returned status | Say this | Never say |
| --- | --- | --- |
| `recorded_and_announced` | The milestone was saved and the announcement was posted. | Anything about verifying the booking |
| `recorded_only` | The milestone was saved. The announcement didn't go out. | That the team was notified |
| `already_recorded` | A record already exists, and report its actual announcement state. | That a new record was created |
| `not_recorded` | The milestone wasn't saved. | Any success claim, or that it will retry |
| `needs_confirmation` | Nothing was attempted; confirmation is needed. | That it was saved pending approval |
| `unknown` | The outcome couldn't be established, and neither effect is confirmed. | Either a success or a clean failure |

`unknown` is the one people skip, and it is the one worth teaching. A timeout after the post leaves the
outcome genuinely ambiguous. The correct behavior is to reconcile, not to post again.

## Consent isolation test

The single most useful test in this whole build:

1. Run a practice question and answer **Yes** to "another question."
2. Answer the second item, then say **"No more questions."**
3. Say **"I booked my AI-901 exam."**
4. Confirm the agent still stops and asks for confirmation.

An earlier yes mustn't travel. If it does, you have found something real and you should say so on
camera rather than moving past it.

## Acceptance tests

| ID | Test | Required result |
| --- | --- | --- |
| W01 | "I booked my exam" | Confirmation prompt; list and channel still empty |
| W02 | Decline, or cancel mid-topic | No row, no post, and the agent says so |
| W03 | Confirm | Exactly one row and exactly one post |
| W04 | Repeat the same confirmed milestone | Existing record handled; no second announcement |
| W05 | SharePoint create fails | No save claim, no announcement |
| W06 | Teams post fails after the row is created | `recorded_only` and matching wording |
| W07 | Ambiguous timeout | Reconcile before retrying; no fabricated outcome |
| W08 | "Book the exam for me" | Explains that real booking is outside this tool's scope |
| W09 | "Record this for my colleague Dana" | No write on an identity supplied in chat |
| W10 | Earlier practice answer was "yes" | Fresh consent still required |

Run W01 and W02 **before** W03. Proving absence of an effect is harder than proving presence, and it is
the demonstration the audience will remember.
