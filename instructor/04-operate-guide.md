# Module 4 instructor guide: Earn the pilot

**LO4:** Evaluate, publish, observe, and govern the agent using analytics, agent evaluations, Power Platform Well-Architected guidance, and security principles.

**50 minutes total, including five minutes of Q&A.** Teach the decision, demonstrate the mechanics, then have learners defend their decision. Procedures are grounded in current **standard-harness** Microsoft Learn pages, checked 2026-09-05. They are not tenant observations.

## Rehearsal gate

Before class, use a licensed course environment with generative orchestration, an approved test identity, and the real Module 3 **GetStudySession** flow. Verify twelve repository evaluation cases, plus actual missing-input conversation and the documented tool-unavailability exercise. Prepare **AZ900-live-three** with E04/E05/E08 and **Compare meaning only**, plus **AZ900-tool-one** with E08 alone and **Tool use only**, selecting the real GetStudySession capability. Blank Tool use expectations are not skipped cases: they produce Invalid method results. Prepare two runs of AZ900-live-three before and after one deliberate repair in an isolated teaching copy, and a completed tool-set run for recovery. E09 is an interactive follow-up if time permits. Save actual result exports and sanitized activity captures. Preserve the working checkpoint.

Generate permitted channel traffic before class and allow sessions and analytics processing to finish. Save a sanitized genuine transcript and Monitor view with period, timezone, channel, and collection date. Test-panel traffic is excluded from Monitor. Configure the Teams-only channel, install for the instructor, and test one approved second identity before class. Keep that channel ready for an actual live republish and fresh-session test. Do not invite actual attendees or change tenant policy during rehearsal without an authorized distribution plan.

**Required evidence still pending until recorded:** native runs, actual connected flow, publish result, Teams fresh-session result, second-user access, genuine analytics, sanitized native YAML. Written procedures and synthetic examples do not satisfy those gates. Use the central [rehearsal record](rehearsal-record.md).

## 0-4 minutes: Recall the promises

**SAY:** "A fluent answer is easy to admire. We need to know whether it is correct, whether it used the tool when required, and whether the learner knows what to do next. Which of those could fail while the answer still sounds convincing?"

**DO:** Show the three live case prompts and cover the expected results. Learners predict the acceptance checks. Reveal the expected grounded source, practice question that waits for the learner, and actual 30-minute tool result.

**EXPECT:** Someone identifies that a made-up plan could look like a successful action. Reinforce that the trace must show the tool call.

**RECOVERY:** If predictions are vague, ask: "What would you point to on screen as evidence that the tool ran?"

## 4-15 minutes: Native evaluation and one diagnosis

**SAY:** "Evaluation repeats the promise. The activity map helps us locate the break. A grade is a clue; we still inspect the answer."

**DO:** Spend two minutes opening the two prepared sets from [lab section 2](../modules/04-operate/lab.md). Show **Compare meaning at 80%** in AZ900-live-three and **Tool use with GetStudySession selected** in AZ900-tool-one. Each set uses only its stated method; remove the default General quality method if present. Neither CSV contains capability-selection metadata. That selection belongs in the native UI. Confirm identity and connections under Additional configuration > Manage, then start a live rerun of the one-case tool set. The 80% threshold is a teaching choice, not a certification of correctness. Do not import and configure both sets live.

Use up to three minutes for the tool result and trace. While results arrive, ask learners to classify the three failure types: source, premature answer, action. Open E08 and select **Show activity map**. Inspect actual `focus=cloud`, then `status` and `plan`; verify 30 minutes and visible action output. Tool use proves use of the selected capability, not correct parameters or output. Do not interpret generated rationale as an authoritative record of the model's internal reasoning.

Use four minutes to open the prepared before/after runs of **AZ900-live-three**, select **Compare with**, and name the single changed instruction or configuration. Inspect a failure and each case for regression. Show expected/actual response, grader explanation and resources. Export via **Export test results**. Record Invalid/Error outcomes separately; never quietly remove them to inflate the pass rate. Native response time is a measurement and does not itself change the native pass rate. Keep results from the two sets separate. Reserve two minutes for learners to name the smallest repair. **Timing: 2 + 3 + 4 + 2 = 11 minutes.**

**EXPECT:** Learners distinguish a content failure from a missing tool call and can explain why the same tests must be rerun. Show native method labels, not only a spreadsheet of predictions.

**RECOVERY:** Allow two minutes for the live run. If delayed, switch to the genuine dated rehearsal capture. If no native feature/capture exists, explicitly state "native evaluation demonstration not completed" and use the manual test route. Do not call a manually completed worksheet a native evaluation. Authenticated evaluations can be blocked by policy on the Microsoft Copilot Studio connector; repair through the admin outside class.

Sources: [test creation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-create), [results](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results), [activity map](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-review-activity).

## 15-23 minutes: Read what users did

**SAY:** "Ninety percent never reached a human. That sounds impressive until three people simply gave up. Containment needs a definition and a transcript."

**DO:** Use the explicitly [synthetic worked example](../modules/04-operate/worked-example.md). Give learners 60 seconds to calculate 6/10 resolution, 9/10 no-escalation, and 3/10 abandonment. Reveal the answer. Read the repeated-question transcript and ask which component needs repair. Reveal the incorrect tool input setting and contrast it with an actual map before diagnosing a real incident.

Show **Monitor** for the precollected period, using the outcome names as well as counts. Open one permitted session transcript. Identify resolved confirmed versus implied, abandoned, and escalated. A mentor signpost in text does not establish a live handoff; a native Escalated label does not prove a representative accepted the conversation. Show available feedback and explain the survey denominator. For a generative agent use conversation outcomes and themes, not the classic-only topic Monitor pane.

**EXPECT:** The first repair is the tool input setting, not a larger model. A survey mean from four respondents describes four respondents. A passing offline case is not the same as a successful user session.

**RECOVERY:** Analytics can take up to an hour after a session ends. Use dated genuine channel captures, then the synthetic exercise if needed. Label which is which. Do not wait for test-panel traffic to appear. If transcripts are denied, name the missing approved access; do not expand permissions on stage. Bot Transcript Viewer is required for transcript information.

Sources: [Monitor](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-summary), [outcomes and feedback](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-improve-agent-effectiveness).

## 23-29 minutes: Five questions, one model decision

**SAY:** "Governance is deciding who can use this, what it can touch, and who owns the mess when it fails. We can answer that in plain English."

**DO:** Walk the five-control table in the [worksheet](../modules/04-operate/worksheet.md). Reliability: a working checkpoint and truthful failure path. Security: authenticated users, approved sources and least privilege. Operational Excellence: owner, changelog, repeated tests and failure review. Performance Efficiency: bounded tool and measured latency. Experience Optimization: one short question, keyboard-accessible choices and usable citations.

Read the worked model decision. On **Overview > Model**, identify the actual approved GA selection without changing it. Explain that swapping a model cannot fix a wrongly configured input. If a later comparison is warranted, hold tests, sources, identity and tools constant. Preview/experimental availability, external-provider permission and cross-region data processing are separate administrative considerations. Do not enable them during class.

Describe the operational promotion path: **development** for changes with synthetic inputs; **test** for validation with intended policies and identities; **production** for approved release and restricted makers. This is a planning explanation; the class uses the approved teaching environment. Connections and permissions must be rechecked after promotion.

**DLP example:** approve the course's document/public-source and tool connectivity as required by policy; block unauthenticated chat and unneeded outbound HTTP. Business and non-business connectors cannot share data across policy groups. Endpoint restrictions can further limit public-web or HTTP destinations. DLP is not a replacement for data-source permissions. If a connector is blocked, the course owner records the requirement and the admin decides; never turn the whole policy off.

**EXPECT:** Learners name an owner and a control rather than "we use responsible AI." For this synthetic-only assistant, adding confidential employee records would be a new data-boundary decision.

**RECOVERY:** If this becomes an admin-console discussion, return to "Which permission does our single read-only tool actually need?" Save tenant implementation detail for follow-up.

Sources: [five pillars](https://learn.microsoft.com/en-us/power-platform/well-architected/what-is-power-well-architected), [data policies](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention), [model selection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model).

## 29-38 minutes: Publish to a scoped Teams destination

**SAY:** "The maker's test panel is our workbench. Teams is where we verify what the user receives. Publishing updates every connected channel, so we check that audience first."

**DO, in this order:** Use the prepared channel and installed app. Budget two minutes for scope/authentication, two for publication, three for new-session testing, and two for the channel comparison. **2 + 2 + 3 + 2 = 9 minutes.** First-time setup steps below belong in rehearsal; inspect them live without recreating them.

1. Confirm the teaching agent and environment, successful evaluation checkpoint, intended channel, licensed publishing entitlement, and authorized self-test/pilot users. Check **Settings > Security > Authentication** for **Authenticate with Microsoft**. Review existing channels and agent access before publishing, because publication updates all connected channels.
2. Select **Publish**, select **Publish** again, and confirm. Wait for the actual success state. Record time and displayed status; never narrate success while the operation is still running.
3. Open **Channels > Teams and Microsoft 365 Copilot**. For this Teams-only pilot, leave **Make agent available in Microsoft 365 Copilot** unselected. Select **Add channel**. If the channel already exists from rehearsal, inspect its configuration rather than adding it again.
4. In the channel configuration select **See agent in Teams**, then **Add**. Install to the instructor's own profile first. Run `start over` in an existing conversation to see newly published content, then ask the grounded question and request a 30-minute cloud study session. Verify citations, actual result, input behavior, and readable presentation in Teams.
5. Explain the scoped sharing path: grant only approved pilot users access using the agent's sharing controls, then use the channel's **Availability options > Copy link** for installation. A link does not itself grant agent access. Demonstrate the already-approved second identity if available. Do not send a new invitation or submit organization-wide availability during the class.
6. Record the actual outcome and audience. If the published result differs from test, stop expansion. Inspect the session/version, authentication, dependencies, and channel behavior.

**EXPECT:** A genuine Teams response from the newly published agent, plus an explicit boundary between self-installation and a wider pilot. The demo's success does not authorize production rollout.

**RECOVERY:** Trial licenses can create and test but **cannot publish**. The Teams-only Copilot Studio plan lacks this course's generative orchestration, so it is not a workaround. If publishing is blocked, show the error and switch to a genuine dated capture of the same agent's publication and Teams test. Without that evidence, record the publishing demonstration as incomplete. Do not switch to No authentication, remove DLP, or claim publication from the test panel. If an update seems stale, start a new session rather than repeatedly publishing.

| Channel | Preparation difference | Course treatment |
| --- | --- | --- |
| Teams | Approved apps policy, agent sharing, Microsoft authentication, self-install and new-session test | Actual instructor demonstration, five-user pilot candidate |
| Microsoft 365 Copilot | Enable the channel option, confirm user access/entitlement and admin deployment requirements; test in its own host | Preparation comparison; not an additional live deployment |
| SharePoint | Published agent, WRITE access to the target site, allowed SharePoint channel, capacity and site-context test | Preparation comparison; Channels > SharePoint > choose site > Deploy > Confirm is documented, but not executed in class |

Adding a SharePoint knowledge source does not publish a SharePoint channel. Site-wide approval/discovery is a separate decision after testing. Microsoft 365 availability is not implied by a Teams install when its option is unselected.

Sources: [publish](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels), [Teams and Microsoft 365](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams), [SharePoint](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-sharepoint), [licensing](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions).

## 38-45 minutes: Learner decision

**SAY:** "Name the first agent you would safely pilot, then name the governance question that must be answered first. You are allowed to say no. You must explain what evidence would change that answer."

**DO:** Two minutes to decide, three minutes to complete controls, two minutes for peer challenge. Use the worksheet's worked answer only after learners commit to a decision.

**EXPECT:** A proposed five-user, one-week pilot with owner, explicit data boundary, actual test evidence, daily review and stop condition. CONDITIONAL means no users start before conditions are met. Synthetic evidence alone gives NO-GO for a real deployment.

**RECOVERY:** If a learner writes "GO because it works," ask them to name the tested identity, failure case, and person who can remove access. No tenant access is needed to complete the reasoning exercise.

## 45-50 minutes: Q&A and transfer

**SAY:** "The same teach, check, act, observe pattern could support internal onboarding. The moment we add internal documents, we add access-control tests. Reusing the pattern does not reuse approval."

**DO:** Answer questions, then point to [native YAML inspection](../sample-agent/exports/README.md). Explain that the topic canvas generates YAML and that inspecting a real copy is optional follow-up, not a coding prerequisite. The learner package must contain a genuine sanitized topic capture before advertising that artifact as delivered.

**EXPECT:** Learners can name one new source, one new risk and one new evaluation for their own assistant.

**RECOVERY:** Route platform-specific installation and licensing issues to the documented follow-up; preserve the ten-minute course wrap-up after this module.
