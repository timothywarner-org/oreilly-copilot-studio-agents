# September 8, 2026: run of show

**All times America/Chicago (CDT).** Production check: **08:30**. Learner start: **09:00**.
Producer: **Joan Lee**. Use the private presenter link in the calendar invitation, not a repo link.

| Central time | Activity | Exit evidence |
| --- | --- | --- |
| 08:30–09:00 | Producer/audio/screen-share check; resource-link and title-slide confirmation | Console and primary/fallback demo paths ready |
| 09:00–09:50 | Inception: trial setup, design and shell; practice and Q&A within block | Agent brief and explicit success metrics |
| 09:50–10:00 | Break | Display return time in text |
| 10:00–10:50 | Build: knowledge, topics, input handling; practice and Q&A | Teach-check-handoff topic and grounded answer |
| 10:50–11:00 | Break | Save checkpoint |
| 11:00–11:50 | Extend: actions, flows, MCP, delegation, human handoff; practice and Q&A | Tool contract and bounded demonstration |
| 11:50–12:00 | Break | Save checkpoint |
| 12:00–12:50 | Operate: evaluate, observe, govern, scoped publishing demonstration | Evidence-backed pilot decision |
| 12:50–13:00 | Wrap-up and Q&A | First safe pilot plus next practice action |

This implements the public page’s 60/60/60/50/10 schedule. It does not add breaks or Q&A on top of it.

## Teaching guides and slides

| Block | Detailed guide | Companion slides | Checkpoint |
| --- | --- | --- | --- |
| Inception | [01 guide](01-inception-guide.md) | 1-9, break 10 | C1: shell and boundary |
| Build | [02 guide](02-build-guide.md) | 11-16, break 17 | C2: source and wait point |
| Extend | [03 guide](03-extend-guide.md) | 18-25, break 26 | C3: GetStudySession result |
| Operate | [04 guide](04-operate-guide.md) | 27-34 | C4: evaluation and scoped channel |
| Wrap-up | [Co-instructor desk](co-instructor.md) | 35 | First pilot and next independent attempt |

The four guides contain the authoritative minute allocations, worked examples and recovery actions. Slides prompt discussion and demonstrations; they do not replace the guides. Each block includes short, account-independent decisions and question time. The instructor performs the build; independent authoring is optional follow-up. Keep the same agent visible and reuse its brief, sources, tool boundary and evidence sheet.

Read [teaching design](../docs/teaching-design.md) for the rationale and [promise coverage](../docs/promise-coverage.md) for the full registration-page map. Record a timed rehearsal using [this template](rehearsal-record.md).

## Scope gate

When a topic does not help the audience plan, ground, extend, or evaluate this assistant, park it.
Explain Foundry, Fabric, A2A, child agents, connected agents, and M365 SDK connections as distinctions
in the promised agent topology. Do not start six additional implementation demos.

## Recovery rule

One deliberate retry of a failed cloud operation, then switch to the rehearsed checkpoint or observer
exercise. Label the fallback. Do not improvise policy changes or teach a screenshot as a live result.
A recovered lesson is better than a 20-minute debugging broadcast.
