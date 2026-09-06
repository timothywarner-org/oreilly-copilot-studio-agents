# ExamMilestones - SharePoint list schema

**Minimum visible row, plus the few operational fields that make rehearsal safe.** Everything here is
synthetic. No real identities, site IDs, or channel IDs belong in this file or in any learner-facing
fixture.

**Suggested names, not resources known to exist.** List: `ExamMilestones`. Channel:
`Certification Milestones - Demo`. Create them in an isolated non-production location.

| Column | Type | Purpose |
| --- | --- | --- |
| `Title` | Single line of text | Human-readable label, for example `AI-901 booking - Avery Quinn` |
| `LearnerDisplayName` | Single line of text | Synthetic or authenticated display name |
| `ExamCode` | Single line of text | `AI-901` for this demo |
| `ReportType` | Choice | `SelfReportedBooking` |
| `RecordedAtUtc` | Date and time | Set by the workflow, not supplied by the agent |
| `MilestoneKey` | Single line of text | Stable duplicate-protection key, `learnerKey|examCode` |
| `AnnouncementStatus` | Choice | `NotAttempted`, `Posted`, `Failed`, `Unknown` |
| `TeamsMessageId` | Single line of text, optional | Actual returned identifier when the connector provides one |

SharePoint's own item ID is the record identifier. Don't add a second one.

## Columns deliberately absent

No confirmation number. No payment or voucher data. No exam provider credential. No email address,
phone number, or personal contact detail. No score, no pass or fail, no readiness estimate.

Each absence is a design decision worth naming in class. The list records what someone said, on a date.
That is the entire claim it makes, and keeping the schema that narrow is what makes the claim honest.

## Seed rows for rehearsal

Create these two by hand before class so the duplicate path and the partial-failure path have something
to hit. Use obviously synthetic names.

| Title | LearnerDisplayName | ExamCode | ReportType | MilestoneKey | AnnouncementStatus |
| --- | --- | --- | --- | --- | --- |
| AI-901 booking - Avery Quinn | Avery Quinn | AI-901 | SelfReportedBooking | avery.quinn\|AI-901 | Posted |
| AI-901 booking - Jordan Reyes | Jordan Reyes | AI-901 | SelfReportedBooking | jordan.reyes\|AI-901 | Failed |

The Jordan Reyes row is the one to show when you explain `already_recorded`: a record exists, and its
announcement never went out. The agent must report both facts, not just the first one.

## Reset procedure

Delete only rows whose `MilestoneKey` you created for this demo, and only from this list. Delete only
messages your own rehearsal posted, and only from the demo channel. Write the reset steps down before
delivery day; improvising a cleanup in a shared tenant at 12:55 is how a demo becomes an incident.
