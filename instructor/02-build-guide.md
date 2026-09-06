# Module 2 delivery guide: Evidence and a real pause

**LO2:** Build a grounded AZ-900 study assistant using knowledge sources, topics, generative answers, and test prompts.

**Duration:** 50 teaching minutes, then a 10-minute break. **Status:** Documentation-grounded build instructions; live results remain **NOT RUN** until rehearsed. **Format:** Instructor-led demonstration with universal prediction and decision exercises. No learner account or builder time is required. **Core:** one file and one practice topic. Azure subject matter is deliberately narrow so learners can concentrate on agent behavior.

**Before class:** Open the saved shell, [learner lab](../modules/02-build/lab.md), [concept file](../sample-agent/knowledge/azure-concepts.txt), [worksheet](../modules/02-build/worksheet.md), and [sources](../sources/research-build.md). Rehearse the full topic and source processing in advance. Keep a completed topic available to inspect if live authoring exceeds 12 minutes. Prepare the small input demonstration described below; disable it after the comparison. Do not invent a recording or ready agent if preparation has not happened.

## 0-4: Recall the model from the previous block

**SAY:** “Which part tells the agent how to behave, and which part gives it evidence? Today we make those two things visible. Then we make it wait for a student's answer.”

**DO:** Collect an answer in chat. Show the failed quiz pattern: a Message node that asks a question and immediately sends the key. Ask what is missing.

**EXPECT:** Instructions versus knowledge; a real Question node.

**IF IT FAILS:** Show a two-box diagram: evidence into an answer, learner response into feedback. Keep the repair under a minute.

## 4-12: Add a small source and inspect the evidence

**SAY:** “This small text file is ours. It paraphrases Microsoft Learn, and labels Contoso's invented rule. It is not Microsoft policy. A small source makes it possible to inspect whether an answer is supported.”

**DO:**

1. Show the local [concept file](../sample-agent/knowledge/azure-concepts.txt). Identify the IaaS paragraph, the fictional rule, and the source trail.
2. Open **Knowledge > Add knowledge**. Upload the TXT file by browsing or drag and drop. Use name **Contoso Azure concepts** and description “Original course reference for shared responsibility and the three narrow study focuses; not current exam administration or a Microsoft publication.” Select **Add to agent**.
3. Wait for processing. Inspect the source's actual readiness state. Dataverse search is required for file knowledge; admin access and storage are preflight dependencies.
4. In **Settings > Generative AI**, set **Allow ungrounded responses** off and **Use information from the web** off for this controlled demo. The **Web Search** control on Overview refers to the broad-web setting. Do not turn off or weaken content moderation to obtain an answer.
5. In a fresh test ask: “Who patches the guest operating system of Contoso's Azure virtual machine?” Inspect the output, citation, and supporting paragraph.
6. In a new test ask: “What is my exact AZ-900 exam appointment time?” Compare its evidence and response.

**EXPECT:** The first response attributes guest-OS responsibility to Contoso and has support in the file. The second cannot establish an appointment. Cite the retrieved course file as such; a Microsoft URL printed inside it does not mean that webpage was retrieved.

**IF IT FAILS:** If processing takes more than two minutes, use a previously processed rehearsal checkpoint if available. Otherwise inspect the paragraph manually and mark retrieval **NOT RUN**. If the correct response is withheld, inspect source readiness, actual retrieval, and citation behavior. With ungrounded responses off, current docs say missing in-text citations can cause a retrieved answer to be withheld. Do not “fix” this by removing the need for evidence.

**SAY:** “Turning off ungrounded responses is useful, but it does not certify every sentence. The model can still combine retrieved material with its own knowledge. Even a follow-up can fail if it answers from history without retrieving again.”

## 12-17: Show scope, source limits, and the official-guide extension

**SAY:** “Agent knowledge is the shared library. A generative answers node can choose a smaller reading list for one conversation. Neither the order we upload files nor a reassuring source name proves which evidence will be used.”

**DO:** Open **Topics > System > Conversational boosting** and inspect its **Create generative answers** node. If absent in this agent, use the rehearsed topic that contains the node; to add one, use **Add node > Advanced > Generative answers**. Its **Input** can use the **Activity.Text** system variable selected through the variable picker.

Open node **Properties**, inspect **Knowledge sources > Search only selected sources**, and demonstrate the documented scope. Leave native answer/citation rendering intact; do not replace it with a manually formatted answer variable.

| Configuration | Current documented behavior | Course choice |
| --- | --- | --- |
| Agent Knowledge | Available to orchestration and default node searches | One small original file |
| Node, selected-sources setting off | Searches current agent sources | Inspect as the starting state |
| Node, selected-sources setting on | Searches the selected set instead of the agent set for that node | Select the original file when teaching narrow scope |
| Broad Web Search on | Searches beyond configured sites; results interleave | Off for the controlled core |
| Source order | No dependable “first uploaded wins” rule | Inspect evidence; narrow scope if needed |

**Limits to explain, not memorize:** Microsoft currently documents 25 public websites in generative mode and four public URLs in classic mode. More than 25 knowledge sources cause selection by descriptions; uploaded files are excluded from that 25-source selection limit. Uploaded knowledge currently supports TXT, up to 512 MB per file and up to 500 files, subject to environment storage. These are ceilings, not curriculum targets. Our one short file is far below them. Source type, mode, indexing, and permissions matter more than collecting URLs.

**Official guide extension:** Open the [current AZ-900 guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) in the browser and show the three actual domain names. The course's cloud/security/governance labels are practice categories, not those official domains. For an instructor-prepared web-source demonstration, use **Add knowledge > Public websites**, enter **https://learn.microsoft.com/en-us/credentials** under **Public website link**, select **Add**, set a scope description, then **Add to agent**. This prefix deliberately includes more than AZ-900. Current docs limit a public source URL to two path levels, so do not tell learners to paste the longer guide URL as a supported source configuration. If the tenant requests an ownership confirmation you cannot truthfully supply, stop the web-source addition and use the guide as a browser reference.

**EXPECT:** Learners can distinguish a link for manual reading from a configured retrieval scope. For the prepared extension, ask “What are the AZ-900 exam domains?” and confirm the returned source is the actual guide, not a different credential page. Do not claim success without checking.

**IF IT FAILS:** Public sources rely on Bing indexing and may not return the exact guide. Keep the local core, show the guide directly, and mark website retrieval unverified. Do not silently broaden to all web content. The exact page remains useful for manual verification.

## 17-29: Build one teach-check topic

**SAY:** “We need a deliberate conversation here. We will not ask a model to invent a quiz and grade it in the same breath. The lesson and question are authored. Grounded open answers were the separate test you just saw.”

**DO:** Follow [lab steps 4-8](../modules/02-build/lab.md), with its paste-ready text. Budget two minutes for trigger and lesson, four for the Question and properties, three for branches, and three for tests.

1. Create **Shared responsibility practice** through **Topics > Add a topic > From blank**.
2. In generative mode, **The agent chooses** appears on the trigger. Its description routes shared-responsibility practice only. If the trigger instead reads **User says a phrase**, recheck orchestration rather than silently teaching classic routing.
3. Add the fixed lesson Message, then the multiple-choice Question from the lab. Store the native choice as **PracticeChoice**.
4. Set **Ask every time**, **Repeat once**, and **Set variable to empty (no value)** after no valid entity is found. Use the lab's three choice branches plus recovery. Compare native choice values using the picker; do not compare a choice object with an arbitrary text string.
5. Test “Teach me shared responsibility and give me one practice question.” Stop talking while the agent waits. Choose **Microsoft**, inspect corrective feedback, then restart and choose **Contoso**.
6. Test an unmatched response twice. It should reach an honest pause/recovery, not imply a mentor was contacted. Test a second practice attempt in the same conversation to verify **Ask every time**.

**EXPECT:** First response has one question without an answer key. Subsequent feedback matches the choice. The teaching explanation naturally contains the concept being assessed; it does not announce which choice to click before the response.

**IF IT FAILS:** If routing chooses general knowledge, sharpen the topic description and retry a fresh conversation. If a learner answer triggers another topic, inspect **Question properties > Interruptions > Allow switching to another topic**. Turn it off for this tightly bounded quiz if needed, then retest. If a previously filled variable skips the question, verify **Ask every time**. If time expires, inspect the rehearsed completed topic and retain live authoring as incomplete.

## 29-34: Automatic input collection versus teaching

**SAY:** “The proposal calls out AutomaticTaskInput. That is not a control name I will tell you to hunt for. The current documented topic UI says how the agent fills an input. Use context to collect a known preference. Use an explicit question when the learner must do new thinking.”

**DO:** Inspect the prepared **Input collection demonstration** custom topic. Create it during rehearsal using **Topics > Add a topic > From blank**, with trigger description “Demonstrate collecting study focus only when the user explicitly requests the input collection demonstration.” It must not compete with the real study-session tool.

1. Select **Details > Inputs > Create a new variable**. Name it **focus**, choose **string**, and describe it: “The study focus explicitly requested by the user. Examples: cloud, security, governance. Ask when missing; do not guess.”
2. Under **How will the agent fill this input?**, inspect **Dynamically fill with the best option**. Set **Identify as** to the text entity appropriate to this string. **Should prompt user** stays selected.
3. Add one Message that says “Captured focus:” and inserts the **focus** variable through the editor's variable picker. This is an input prototype, not a working study plan or validation layer.
4. Test “Run the input collection demonstration with focus security.” Inspect whether it uses security without asking again.
5. Restart and test “Run the input collection demonstration.” Inspect whether it asks for a missing focus. Respond “governance” and inspect the captured value.
6. Show **Set as a value** as the alternative for fixed or already-known input, without changing the working demonstration. Disable this demonstration topic when finished so Module 3 has one clear planning route.

**EXPECT:** Supplied context can fill an input; missing information elicits a question. Neither the description nor a string type enforces the allowed list. Module 3 validates focus at the tool boundary. Automatic collection is unsuitable for **PracticeChoice**, which must reflect a new learner response.

**IF IT FAILS:** Check input description, type, prompt setting, and actual orchestration. Show the two documented cases and mark live collection **NOT RUN** if access differs. Do not fabricate an **AutomaticTaskInput** YAML node or claim an exact schema mapping without a real export.

## 34-38: Repair fallback in public

**SAY:** “I don't know is a start. A useful fallback says what could not be established and what the person can do next. It must not invent a handoff.”

**DO:** In a new test use “What is my exact exam appointment time?” Preserve the before response. Open **Topics > System > Fallback**. Inspect its Message and redirect logic. Edit the rephrase message to:

> I could not establish an answer from the available information. I can explain the course's Azure concepts or offer shared-responsibility practice. For personal exam details, check your official booking information. I cannot contact a mentor or book an exam from this agent.

The default topic can redirect to **Escalate** after repeated unsuccessful attempts. Inspect that destination and replace any misleading “connecting you” message with the honest no-connection statement before demonstrating repeated fallback. Do not delete system topics or reset their customization.

Save and repeat the same unsupported prompt in a fresh test. Inspect the actual topic path; an instruction-based refusal can answer without traversing Fallback. If this prompt does not reach Fallback, use the unknown-intent prompt identified in rehearsal to test the modified system topic separately. Never label an unvisited node a verified repair.

**EXPECT:** The user receives a next step and no claim of external contact. Source failure, unknown intent, and unsupported requests are related but do not always take the same path.

**IF IT FAILS:** Do not spend Q&A rebuilding escalation. Stop at an honest message, preserve the failed path, and mark repeated fallback as needing rehearsal. Never assert a human agent is connected just because a topic is named Escalate.

## 38-45: Everyone diagnoses one teaching decision

**SAY:** “Rewrite the feedback for one wrong answer. Your learner should understand the misconception, not just see the word incorrect.”

**DO:** Use the lab's two-minute rewrite, three-minute node trace, and two-minute evidence record. The instructor runs the selected example while learners predict its branch; no learner authoring is scheduled. Reveal the worked answer only after the rewrite. Ask a maker to explain both the supporting paragraph and the wait point.

**EXPECT:** Everyone can explain the wait and feedback from the demonstrated trace. Label the response OBSERVED DEMO and predictions PREDICTED. Personal agent execution is not assessed during class; optional independent authoring is available afterward.

**IF IT FAILS:** Use “host versus guest” as the prompt. Keep the same question and change only feedback.

## 45-50: Hinge question and Q&A

**SAY:** “The answer cites our text file. Inside that file is a Microsoft Learn link. Has the agent proved that it searched Microsoft Learn?”

**DO:** Collect responses before revealing **No**. It retrieved the course file; confirm the underlying source separately. Use the remaining four minutes for Q&A.

**EXPECT:** Learners distinguish provenance, retrieval, and correctness.

**IF IT FAILS:** Open the file and point at the printed URL. A bibliography is not a browser history.

**Break:** 10 minutes. **Carry forward:** Source, practice topic, and no-side-effect boundary. [Extend](../modules/03-extend/README.md) adds the one study-session tool.
