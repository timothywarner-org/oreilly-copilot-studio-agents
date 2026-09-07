# RecordExamMilestone - agent flow recipe

**Two business effects, one honest status.** The flow creates one SharePoint row and posts one Teams
message, then tells the agent exactly what happened. Everything else in it is bookkeeping you build
before class.

**Authored design. Documentation checked 2026-09-06. Tenant execution: NOT RUN. The list, the channel,
and the connections don't exist yet.**

## Prebuild this, demonstrate that

| Prebuild before class | Demonstrate live |
| --- | --- |
| Connections, list, channel, duplicate check, status bookkeeping, error branches | Trigger inputs, the confirmation gate, the two effects, the returned status |

Nobody learns anything from watching you fill dropdowns. They learn from watching an empty list and an
empty channel become one row and one post, and from watching you read the returned status before you
believe it.

## Flow shape

**Challenge boundary:** This flow handles self-reported bookings only. It does not verify passes,
rank employees, submit AI Cert Challenge claims, reserve awards, or issue payment. Keep that boundary
in the tool description as well as the [topic description](../topics/record-exam-milestone.md).

```text
When an agent calls the flow
  -> validate: confirmed is true, examCode is AI-901, learnerKey is present
       any check fails -> Respond: status = needs_confirmation, nothing attempted
  -> compute MilestoneKey  (learnerKey + "|" + examCode)
  -> look up MilestoneKey in ExamMilestones
       found  -> Respond: status = already_recorded, with the row's actual AnnouncementStatus
       absent -> SharePoint: Create item
                   failed  -> Respond: status = not_recorded
                   created -> Teams: Post message in a chat or channel
                                posted -> update row AnnouncementStatus = posted
                                          Respond: status = recorded_and_announced
                                failed -> update row AnnouncementStatus = failed
                                          Respond: status = recorded_only
  -> Respond to the agent with the actual outcome fields
```

Use **When an agent calls the flow** and **Respond to the agent** for the standard harness, and keep
**Asynchronous response = Off**. Return only after the effects whose completion you are claiming. An
acknowledgment that work started isn't evidence that it finished. Reference:
[Create an agent flow as a tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create).

## Inputs and how each one is trusted

| Input | Type | Source | Trust |
| --- | --- | --- | --- |
| `examCode` | Text | Fixed by the topic | Validated against the literal `AI-901`; reject anything else |
| `learnerKey` | Text | Configured identity for this demo | Trusted only because the topic set it, never from chat |
| `learnerDisplayName` | Text | Same source | Display only; never treated as proof of identity |
| `confirmed` | Boolean | The topic's Question node | Validated defensively; a boolean isn't a security boundary on its own |

**Never accept an identity supplied in chat.** "Record this for my colleague Dana" is a test case, not
a feature. For a controlled demo without suitable end-user identity, use a fixed synthetic persona and
say on camera that it is synthetic - that keeps the demo honest and it keeps you from claiming
authenticated per-user behavior you haven't proven.

State plainly whether connector operations run with a maker connection or an end-user connection. The
difference decides who the row is actually created by, and it is the question a governance-minded
attendee will send you afterward.

## Destination is configuration, not a model decision

The site, list, team, and channel stay fixed in trusted configuration or connection references. The
model must never choose where a write lands. Give the demo connections the minimum access the flow
needs. If policy or licensing blocks something, record the blocker rather than working around it to
rescue a demo.

## Announcement text

Build it from validated fields. Plain text is fine; the Teams announcement formatting adds nothing here.

> Demo milestone: {LearnerDisplayName} reports booking the AI-901 exam. Recorded by the Contoso AI
> Fundamentals Coach.

No broad mentions, no scores, no booking references, no generated prose. A message assembled from
fields can't say something you didn't intend.

## Duplicate handling

`MilestoneKey` is one self-reported booking per employee per exam. Don't use a fresh random request ID
as the key; repeated requests would then look like distinct milestones and the channel would fill with
duplicates on your second rehearsal run.

Prefer an enforced unique key with collision handling where the list supports it. A lookup before
creation doesn't prevent concurrent duplicates. Keep that distinction in your notes rather than
turning Hour Three into a concurrency workshop.

## Partial failure, stated as a rule

- SharePoint create fails: announce nothing, claim nothing.
- SharePoint succeeds, Teams fails: keep the row, return `recorded_only`, and say the announcement didn't go out.
- Timeout after posting: the outcome is genuinely ambiguous. Return `unknown`, reconcile by looking, and
  don't post again.

Don't promise a transaction or exactly-once delivery across SharePoint and Teams. This is a small demo
that handles repeat requests and reports truthful partial outcomes. Stronger guarantees are a different
system and a different conversation.

## Contracts and schemas

- Status vocabulary and permitted claims: [`milestone-result.contract.json`](milestone-result.contract.json)
- List columns: [`exam-milestones-list-schema.md`](exam-milestones-list-schema.md)
- Consent gate and status-to-wording map: [`../topics/record-exam-milestone.md`](../topics/record-exam-milestone.md)

Connector references to verify before authoring instructions, because action names change:
[SharePoint connector](https://learn.microsoft.com/en-us/connectors/sharepointonline/) and
[Send a Teams message using Power Automate](https://learn.microsoft.com/en-us/power-automate/teams/send-a-message-in-teams).

## Rehearsal procedure

Use an isolated non-production list and channel with synthetic identities. Show both empty. Run the
confirmed conversation. Inspect the flow run's actual inputs, action statuses, and outputs, then the new
row, then the new post, then the agent's final wording against all three. Reset only known demo records
through a controlled procedure; never delete shared content or notify a real team as part of a test.

Run failure tests only through controlled demo configuration. A disabled tool tests unavailability. It
doesn't prove handling of a real connector runtime exception, and saying otherwise on camera is the
kind of claim that comes back.
