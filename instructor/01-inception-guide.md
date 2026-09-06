# Module 1 delivery guide: One useful job

**LO1:** Plan a Copilot Studio agent from persona, job-to-be-done, instructions, topic map, guardrails, and success metrics.

**Duration:** 50 teaching minutes, including exercise and Q&A, followed by a 10-minute break. **Evidence status:** Documented procedures and expected results. No tenant execution is implied.

**Before class:** Rehearse in the approved nonproduction environment. Open [instructions](../sample-agent/instructions.md), [concept file](../sample-agent/knowledge/azure-concepts.txt), [worksheet](../modules/01-inception/worksheet.md), and [sources](../sources/research-build.md). Have a saved shell and Module 2 checkpoint ready as recovery, created during rehearsal. Record their actual names privately. If none exists, say so; a guide describing a checkpoint does not create it.

## 0-5: Start with a learner problem

**SAY:** “A Contoso employee has half an hour to study Azure. They ask a chatbot for practice and it immediately gives away the answer. Technically, it answered. As a teacher, it failed. Today we build a coach that explains one idea, waits for a response, and gives useful feedback. You are the maker. The beginner studying Azure is the person your agent serves.”

**DO:** Display: “Teach me shared responsibility and check my understanding.” Give everyone 20 seconds to predict a good first response. Invite two answers.

**EXPECT:** An explanation, one original question, and a pause. An answer key in that first response is a teaching failure.

**IF IT FAILS:** Explain that shared responsibility means the customer and Microsoft each have jobs to do. The course tests agent design, not prior Azure knowledge.

## 5-13: Name only the parts we will use

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

## 13-21: Write the brief together

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

## 21-33: Build the shell and test a boundary

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

## 33-38: Map conversations and choose a model baseline

**SAY:** “The map describes five conversation jobs. We hand-author the sequence where teaching matters. Knowledge handles open questions. The next exercise builds one topic.”

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

## 38-45: Learner exercise

**SAY:** “Write one instruction, one measurable test, and one topic. Then let someone else try to score your test. You have seven minutes.”

**DO:** Use [the lab](../modules/01-inception/lab.md): one minute persona, two draft, two peer check, two revision. At minute 43 show its worked answer. Revise one weak criterion publicly.

**EXPECT:** Everyone produces a brief even without tenant access. Browser troubleshooting must not consume the practice period.

**IF IT FAILS:** Give the question “What appears before I answer, and what waits until after?” Require that criterion before extending the brief.

## 45-50: Hinge question and Q&A

**SAY:** “A learner says, 'I wrote do not hallucinate in the instructions, so the agent is grounded.' What is missing?”

**DO:** Collect answers, then reveal: “Configured evidence, retrieval, and tests that inspect support for the answer.” Use the remaining four minutes for Q&A.

**EXPECT:** Learners distinguish behavioral instructions from evidence.

**IF IT FAILS:** Revisit the component table for 30 seconds. Park integrations for Extend.

**Break:** 10 minutes. **Next:** [Module 2](02-build-guide.md).
