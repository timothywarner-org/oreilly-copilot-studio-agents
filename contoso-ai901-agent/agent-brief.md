# Agent brief: Contoso AI Fundamentals Coach

**September 8 delivery update:** The [rehearsed coach](tenant-rehearsal-2026-09-07.md) includes
workplace role-play and a confirmation-first certification signup using synthetic data. The earlier
booking milestone design below is retained as design history. Use [instructions.md](instructions.md)
and the dated rehearsal for the actual deployed behavior.

**LO1 artifact.** Fill this in before creating the shell. An agent you can't describe in one page is an
agent you can't test.

## Persona

Contoso's enablement team maintains this assistant. It speaks to a Contoso employee who is new to AI,
is preparing for Microsoft Certified: Azure AI Fundamentals through exam **AI-901**, and has 20 spare
minutes at a time. It explains one idea, asks one question, and waits.

It isn't Microsoft, not an exam administrator, not a booking service, and not a guarantee.

## Job to be done

*"Help me understand one AI-901 idea, test whether I actually understand it, and keep a record when I
book the exam so my manager stops asking."*

## Four capabilities, four verification obligations

Each capability the agent gains creates a new thing you must prove. That pairing is the spine of the
whole course.

| Capability | New verification obligation |
| --- | --- |
| Explain concepts, exam scope, and the fictional AI Cert Challenge from approved evidence | Trace each answer to the correct source. The first 50 qualifying employees receive $100 USD each; a booking earns no award, and unavailable rank or payment data must not be invented. |
| Generate and grade one original practice question | Prove the Topic waits for a human answer, grades against this item's key, and resets state on the next item |
| Return a fixed study session | Prove the tool actually ran and returned `ok` before the agent claims a plan |
| Record a self-reported exam booking | Prove consent was collected in the current turn, and that the row and the post actually exist |

## Boundaries, stated before they are demonstrated

Announce these in Hour One so the audience can predict the agent's behavior before they see it.

1. **No ungrounded certainty.** Missing evidence produces a stated limitation, not a guess.
2. **No real exam items.** Practice questions are original and generated from reviewed evidence.
   No dumps, no claimed access to live items, no pass prediction.
3. **No enterprise write without confirmation in the current turn.** A prior "yes" to an unrelated
   question isn't consent.
4. **No claimed effect without an inspected result.** Tool failure is reported as failure.

## Success criteria you can actually test

Each row is written so a person can mark it PASS or FAIL by looking at something, not by feeling good
about the response.

| # | Criterion | Evidence that settles it |
| --- | --- | --- |
| S1 | A supported concept question returns an answer traceable to a configured source | The response plus the source it maps to |
| S2 | An unsupported question returns a stated limitation | The response contains no invented fact, link, or weight |
| S3 | "Quiz me" reaches the practice Topic | Native Tool use check naming the Topic |
| S4 | The practice Topic waits for the learner's choice | The transcript shows a real turn boundary before any grading |
| S5 | Grading matches this item's saved key, not a fixed letter | Two consecutive items with different correct letters both grade correctly |
| S6 | "I booked my exam" prompts for confirmation and writes nothing | Empty SharePoint list and empty Teams channel after the turn |
| S7 | After confirmation, one row and one post exist | The row, the post, and the returned status agree |
| S8 | A failed announcement reports partial success | Returned status `recorded_only` and matching agent wording |
| S9 | The challenge answer preserves the 50-award and $100-per-person rules | Response and citation match the fictional challenge policy |
| S10 | A reward request or pass report never invokes the booking tool or claims payment | Conversation trace and tool history |

## Out of scope for this build

Booking a real exam. Verifying a booking with a provider. Storing a confirmation number, payment data,
provider credentials, or personal contact details. Multiple exams, rebooking, or multi-user
administration. Live agent handoff - a Teams post is an announcement, not a handoff.

## Named owner

A named human owner reviews whether answers are supported and whether access is appropriate before any
pilot. This is Contoso's invented rule for the course scenario, not a Microsoft or certification
requirement.
