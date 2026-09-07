# Delivery status and remaining checks

## Authored and reviewable

Four redesigned modules preserve the approved objectives. Each has a lab, worksheet, worked answers, and timed instructor guide. The package includes a 35-slide manuscript, source-reviewed native build procedures, the simple GetStudySession recipe, native evaluation and scoped publishing procedures, synthetic operational examples, a YAML inspection guide, a promise register, and a learner-package generator.

There is one agent kit. `contoso-ai901-agent/` carries the brief, instructions, knowledge with recorded
provenance, topic map, practice-question topic, milestone workflow, tool contracts, runbook, talk track,
icons, and evaluation sets for the **Contoso AI Fundamentals Coach** on **AI-901**. The predecessor
AZ-900 kit at `sample-agent/` was retired on September 7, 2026 and the repository validator now binds to
the AI-901 kit by path. Its own [README](../contoso-ai901-agent/README.md) and
[STATUS](../contoso-ai901-agent/STATUS.md) are the authority for its build order and open gates.

The existing local repository has been preserved and published privately to GitHub. Local validation establishes repository integrity and optional Node reference behavior. It does not execute Copilot Studio.

## Tenant and delivery gates

**September 7 live update:** The coach was created and published. Knowledge ingestion, practice,
GetStudySession, and the simplified signup-to-Teams route have actual tenant smoke-test evidence.
The [dated rehearsal record](../contoso-ai901-agent/tenant-rehearsal-2026-09-07.md) is authoritative
for completed checks and the September 8 demo route. The following gates remain broader than those
smoke tests and must not be inferred complete.

- Actual environment, authoring experience, roles, licenses, credits, models and policy configuration.
- Real shell creation, source retrieval, topic wait point and fallback behavior.
- Real GetStudySession flow, agent binding, all supported inputs, unsupported input, missing input and tool unavailability behavior.
- Native evaluation runs and same-case comparison, plus manual multi-turn checks.
- Genuine operational evidence from channel use, scoped publishing and second-user access.
- A real sanitized native YAML artifact for the promised follow-up inspection. The guide is provided; an export is not fabricated.
- Producer-approved learner distribution and verified attendee access. A private GitHub URL alone does not satisfy this.
- Timed rehearsal of all blocks and genuine recorded recovery material.
- Editorial correction of the registration-page audience mismatch.
- **LO2 wording. The one open decision for September 8.** The approved objective and the published
  registration page name AZ-900; the delivered build is AI-901. Nothing in `course.json` or the
  [proposal excerpt](../sources/proposal-curriculum.md) has been changed, because that excerpt is a
  verbatim quotation of the approved proposal. Two resolutions remain in
  [STATUS.md](../contoso-ai901-agent/STATUS.md): narrate the difference in Hour One, which costs about
  20 seconds and needs no approval, or request an editorial correction from O'Reilly after delivery.
  Silently editing the objective is not an option.
- **AI-901 evaluation and quality.** Native evaluation CSVs have not been imported or run. Four
  generated practice samples do not close the full item-quality review. The original RecordExamMilestone
  design was not deployed; the user-requested Certification Signups route was deployed and tested.
- **AI-901 objective snapshot.** The Microsoft Learn Skills measured conversion is dated and hashed, but
  its upload now reports Ready. Recheck the live study guide before teaching the
  weights as current.
- **Learner package contents.** `learner/package-files.json` now points at the AI-901 kit and every entry
  resolves, but the generated package has not been rebuilt and inspected since the conversion. Run the
  generator and read `PACKAGE-STATUS.md` before sending anything to the producer.

Closed on September 7, 2026: the slide manuscript, the [slide map](presentation-coverage.md), the
evaluation set names, and the optional Node reference were all converted from AZ-900 to AI-901 in one
pass, so the deck and the demo now name the same exam.

Use [the rehearsal record](../instructor/rehearsal-record.md) to close gates with actual observations. The [promise map](promise-coverage.md) identifies what each supports. Synthetic examples are labelled and must never be presented as tenant results. Runtime-exception testing beyond the supplied tool-unavailability exercise remains an optional separate check; do not claim it from a disabled-tool test.

## Materials and binary outputs

Tim approved the [44-slide September 8 PowerPoint](../slides/Warner-CopilotStudio-Agents-2026-09-08.pptx) for inclusion in Git and learner sharing on September 7. The exact file has a narrow ignore-rule exception; the source template, private builds, and generated learner ZIP remain excluded. The editable manuscript and package generator are versioned. Preparing these files does not send them to attendees or change repository visibility. Complete [the preflight](../instructor/preflight.md) before delivery.
