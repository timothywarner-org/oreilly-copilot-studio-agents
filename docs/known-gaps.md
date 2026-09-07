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
- **AI-901 kit, every claim.** Instructions, topics, prompt output binding, the AI-901 GetStudySession
  plan text, the RecordExamMilestone flow, its SharePoint list and Teams channel, and the native
  evaluation CSVs are authored and NOT RUN. The SharePoint list and Teams channel have not been created.
- **AI-901 objective snapshot.** The Microsoft Learn Skills measured conversion is dated and hashed, but
  its upload and retrieval in a tenant are NOT RUN. Recheck the live study guide before teaching the
  weights as current.
- **Learner package contents.** `learner/package-files.json` now points at the AI-901 kit and every entry
  resolves, but the generated package has not been rebuilt and inspected since the conversion. Run the
  generator and read `PACKAGE-STATUS.md` before sending anything to the producer.

Closed on September 7, 2026: the slide manuscript, the [slide map](presentation-coverage.md), the
evaluation set names, and the optional Node reference were all converted from AZ-900 to AI-901 in one
pass, so the deck and the demo now name the same exam.

Use [the rehearsal record](../instructor/rehearsal-record.md) to close gates with actual observations. The [promise map](promise-coverage.md) identifies what each supports. Synthetic examples are labelled and must never be presented as tenant results. Runtime-exception testing beyond the supplied tool-unavailability exercise remains an optional separate check; do not claim it from a disabled-tool test.

## Materials and binary outputs

The PowerPoint companion and generated learner ZIP are delivered separately from Git under the repository's binary/distribution rules. The editable slide manuscript and package generator are versioned. Creating the package does not send it to attendees, change visibility, or establish publisher distribution approval. Complete [the preflight](../instructor/preflight.md) before delivery.
