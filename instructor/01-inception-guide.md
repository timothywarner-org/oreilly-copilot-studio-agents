# Module 1 delivery guide: One useful job

**LO1:** Plan a Copilot Studio agent from persona, job-to-be-done, instructions, topic map, guardrails, and success metrics.

**Format:** Instructor-led demonstrations and short universal exercises. No learner authoring or trial activation is required during class. **Duration:** 50 teaching minutes, including exercise and Q&A, followed by a 10-minute break. **Evidence status:** Documented procedures and expected results. No tenant execution is implied.

**Before class:** Rehearse in the approved nonproduction environment. Open [instructions](../sample-agent/instructions.md), [concept file](../sample-agent/knowledge/azure-concepts.txt), [worksheet](../modules/01-inception/worksheet.md), and [sources](../sources/research-build.md). Have a saved shell and Module 2 checkpoint ready as recovery, created during rehearsal. Record their actual names privately. If none exists, say so; a guide describing a checkpoint does not create it.

## 0-4: Start with a learner problem

**SAY:** “Contoso trainers need a consistent Azure-onboarding activity. An employee has half an hour to study Azure. They ask a chatbot for practice and it immediately gives away the answer. Technically, it answered. As a teacher, it failed. Today we build a coach that explains one idea, waits for a response, and gives useful feedback. You are the maker. The beginner studying Azure is the person your agent serves.”

**DO:** Display: “Teach me shared responsibility and check my understanding.” Give everyone 20 seconds to predict a good first response. Invite two answers.

**EXPECT:** An explanation, one original question, and a pause. An answer key in that first response is a teaching failure.

**IF IT FAILS:** Explain that shared responsibility means the customer and Microsoft each have jobs to do. The course tests agent design, not prior Azure knowledge.

## 4-11: Name only the parts we will use

**SAY:** “Instructions describe behavior. Knowledge supplies evidence. A topic controls a conversation that needs a deliberate sequence. A tool does a bounded job. Orchestration chooses what to use. A channel is where the person meets the agent; a trigger starts work.”

**DO:** Walk the same request across this table. Ask which part forces a pause.

| Part | Concrete role |
| --- | --- |
| Instructions | Explain one idea; do not guarantee a pass. |
| Knowledge | Short source explaining shared responsibility. |
| Topic | Teach, question, wait, then feedback. |
| Tool | Return a fixed 30-minute session in Module 3. |
| Orchestration | Select the practice topic for a practice request. |
| Trigger | A conversational request; event triggers are an extension. |
| Channel | Test chat now; a governed pilot in Module 4. |

**EXPECT:** “A Question node in the topic” is the eventual reliable pause. Instructions alone request behavior; they do not establish a controlled wait point.

**IF IT FAILS:** Contrast printing a question with a teacher actually waiting for the student.

## 11-20: Show how to start a Copilot Studio trial

**SAY:** “You do not need an account to participate today. I will show you the access path so you can try this afterward. A trial lets you build and test; it does not let you publish the agent. We will use my licensed teaching environment for the publishing demonstration.”

**DO, minutes 11-14:** Open the official [trial sign-up page](https://go.microsoft.com/fwlink/?LinkId=2107702) from [Microsoft Learn's access guide](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions). Explain a modern supported browser and an organizational **work or school account**. A personal account can be rejected. Do not show passwords, verification codes, or private account details on screen.

**DO, minutes 14-17:** Demonstrate the documented entry steps with the approved demonstration identity or a genuine, sanitized recording:

1. Enter the work or school email address.
2. Select **Next**.
3. Follow the account-specific verification and sign-up instructions actually displayed.
4. After successful completion, open [Copilot Studio](https://copilotstudio.microsoft.com/) and inspect the available approved environment.

The docs do not specify one universal sequence after Next, so narrate only controls actually present. If the instructor already has access and the sign-up flow skips enrollment, state that and use the prepared capture to explain the missing steps. Do not claim that a new trial was activated when an existing account simply signed in.

**DO, minutes 17-20:** Show this decision table and ask everyone which next step fits a blocked sign-up.

| What you see | Next step |
| --- | --- |
| Personal address rejected | Use an eligible work or school account |
| Self-service sign-up blocked | Contact the organization's administrator after class; the administrator reviews trial sign-up policy |
| Signed in but environment access missing | Request appropriate environment access through the organization's process |
| Trial working | Create and test in the test chat panel; inspect expiry notices |
| Publish unavailable on trial | Expected limitation; a publishing entitlement is a separate decision |

**SAY:** “Check the expiry shown for your account. The current access article documents a 30-day extension when the trial expires, but it does not state the initial trial length. I am not going to promise a fixed starting duration from memory. Also, an expiring trial environment is different: Microsoft's environment article says those expire after 30 days and their agents and related data are deleted when the environment expires. Check both the license and the environment.”

**EXPECT:** Learners can explain the work/school-account route, recognize an admin-controlled block, and distinguish trial build/test from publication. Activation is an optional after-class action, not the exercise result.

**IF IT FAILS:** Allow one deliberate retry, then show the documented route or genuine recording. No learner is expected to obtain administrator approval during class. Do not enable self-service, create a tenant, change policy, or purchase capacity to get through this demonstration. Do not imply a Teams-only plan provides the generative-orchestration experience demonstrated later.

**Sources checked 2026-09-06:** [Get access](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions), [administrator trial policy](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing#trial-plans), [environment expiry](https://learn.microsoft.com/en-us/microsoft-copilot-studio/environments-first-run-experience#trial-environments). See [research notes](../sources/research-trial.md).
## 20-28: Write the brief together

**SAY:** “If we cannot say what failure looks like, we cannot judge whether this agent works.”

**DO:** Fill the brief aloud. Before revealing the criterion, invite learners to improve “be helpful.”

| Decision | Worked choice |
| --- | --- |
| Persona | Contoso employee new to Azure, comfortable with chat. |
| Job | Understand a concept, attempt a question, choose a study session. |
| Initial scope | Shared responsibility, then three narrow study focuses. |
| Sources | Course-authored concept file; live Microsoft Learn guide for current exam scope. |
| Guardrail | No booking, pass guarantees, exam dumps, or invented mentor contact. |
| Success test | First practice turn shows one question and no key; second turn explains the actual choice. |
| Failure test | A request to book an exam never produces a booking claim. |

**EXPECT:** Observable criteria. “Cites something” is weaker than “the cited passage supports the factual claim.”

**IF IT FAILS:** Supply the prompt first. Ask, “What must we see in the next message to score this?”

## 28-38: Build the shell and test a boundary

**SAY:** “We create the smallest agent we can inspect. The source and teaching flow come next. A friendly answer at this point does not prove grounding.”

**DO:** Use the documented **standard harness** route. Current docs distinguish it from **New experience**. Recheck the actual tenant in rehearsal.

1. Sign in to [Copilot Studio](https://copilotstudio.microsoft.com/). If **New experience** is enabled, turn it off and dismiss its feedback panel with **Submit** as documented. Select the approved environment.
2. On **Agents**, choose **Create blank agent**, name it **AZ-900 Cert-Prep Assistant**, and select **Create**. Do not provision an environment just to bypass permissions.
3. On **Overview**, in **Instruction**, select **Edit**. Paste the reviewed [sample instructions](../sample-agent/instructions.md), then **Save**. Identify purpose, grounding, teaching, tools, handoff, and boundaries without reading every line.
4. Inspect **Settings > Generative AI > Orchestration > Use generative AI orchestration for your agent's responses?** Set **Yes** if permitted. New standard-harness agents currently default to generative orchestration; verify instead of toggling blindly.
5. Open the test panel. In a fresh conversation enter “Can you guarantee that I will pass AZ-900?” Capture the response. Expect no guarantee and an offer of study support. Test “Please register me for the exam.” It must not claim a completed booking.
6. Record the shell's actual name, saved state, and how to reopen it for the next checkpoint. This guide is not an exported agent.

**EXPECT:** A saved shell with bounded instructions. A refusal is a narrow test result, not proof of comprehensive safety.

**IF IT FAILS:** Spend at most two minutes on authoring problems. Reopen the rehearsed shell if available, or show the instruction decisions from the file and mark creation **NOT RUN**. Record exact UI differences. If the agent makes an unsupported claim, retain that failed baseline for repair.

## 38-45: Learner exercise

**SAY:** “Write one instruction, one measurable test, and one topic. Then let someone else try to score your test. You have five minutes.”

**DO:** Use [the lab](../modules/01-inception/lab.md): one minute persona, two minutes draft, one minute compare, one minute revise. Use the final two minutes to show the five conversation purposes and the model baseline decision below. Everyone can complete this exercise without an account.

**EXPECT:** Everyone produces a brief even without tenant access. Browser troubleshooting must not consume the practice period.

**IF IT FAILS:** Give the question “What appears before I answer, and what waits until after?” Require that criterion before extending the brief.

## 45-50: Hinge question and Q&A

**SAY:** “A learner says, 'I wrote do not hallucinate in the instructions, so the agent is grounded.' What is missing?”

**DO:** Collect answers, then reveal: “Configured evidence, retrieval, and tests that inspect support for the answer.” Use the remaining four minutes for Q&A.

**EXPECT:** Learners distinguish behavioral instructions from evidence.

**IF IT FAILS:** Revisit the component table for 30 seconds. Park integrations for Extend.

**Break:** 10 minutes. **Next:** [Module 2](02-build-guide.md).

### Reference for the final two-minute map and model comparison

**SAY:** “The map describes five conversation jobs. We hand-author the sequence where teaching matters. Knowledge handles open questions. The next demonstration builds one topic; your exercise traces how it works.”

**DO:** Show the five promised intents and their course implementations.

| Intent | Implementation |
| --- | --- |
| Exam-domain overview | Official guide and grounded knowledge route. No memorized objective weights. |
| Practice question | One authored teach-check topic in Module 2. |
| Study plan | One bounded 30-minute tool in Module 3. |
| Fallback | Honest missing-evidence message and mentor limitation. |
| Search | Generative answers over configured sources, with evidence inspection. |

Inspect **Overview > Model**. Record the actual primary model name and release label. Keep the tenant-approved production baseline for this simple task. Do not choose preview or external models solely because they are newer.

**EXPECT:** “Use the approved baseline; test grounding, routing, waiting, response time, and consumption before changing it.” Primary orchestration, deep reasoning, generative responses, and prompt-builder models can have separate settings. This introduction covers the primary model.

**IF IT FAILS:** If the selector is unavailable, record the configured value you can establish or **UNKNOWN**. Do not imply availability across tenants. A model change requires rerunning identical tests.
