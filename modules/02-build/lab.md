# Build lab: Teach, wait, then respond

**LO2. No account or code required during class.** Watch the instructor build and test the topic, then complete the seven-minute explanation-and-trace exercise. The authoring recipe is supplied for optional independent practice afterward.

## Instructor demonstration and optional after-class authoring recipe

1. Start with your saved Module 1 agent. Upload [azure-concepts.txt](../../contoso-ai901-agent/knowledge/ai901-concepts.txt) through **Knowledge > Add knowledge**, name it **Contoso Azure concepts**, and describe it as “Original course reference for shared responsibility and the three narrow study focuses; not current exam administration or a Microsoft publication.” Select **Add to agent**. Wait for processing and check an actual response; file upload alone is not verification.
2. In **Settings > Generative AI**, turn off **Allow ungrounded responses** and **Use information from the web** for the controlled demonstration. Review the [caveats](../../instructor/02-build-guide.md): this does not make all generated claims correct.
3. In fresh conversations test “Who patches the guest operating system of Contoso's Azure virtual machine?” and “What is my exact exam appointment time?” The first should have support in the uploaded file. The second has no supporting appointment data. Open the cited file or retrieved evidence; do not mistake a link inside that file for proof the webpage was retrieved.
4. In **Topics > Add a topic > From blank**, create **Shared responsibility practice**. For generative orchestration, describe **The agent chooses** trigger: “Teach shared responsibility and give one original practice question when the user requests practice or a quiz about shared responsibility. Do not handle exam registration or study-session planning.”
5. Add **Send a message** for the lesson text below. Add **Ask a question** for the practice question. Use **Identify > Multiple choice options**, add the three choices below, and rename the variable under **Save user response as** to **PracticeChoice**.
6. On the question, **Properties > Question behavior > Skip behavior > Ask every time**. Set **How many reprompts > Repeat once**. Under **Entity recognition > No valid entity found**, set **Action if no entity found > Set variable to empty (no value)**. This allows an authored recovery rather than implying live human transfer.
7. Use the choice branches, or **Add a condition** if needed, to compare **PracticeChoice** with each choice using the native option picker. Add its feedback as a **Message**. The default or empty branch uses the recovery below. Save.
8. Test each choice in a fresh conversation. The first turn must stop at the question. The feedback must depend on the selected choice. Test an unrecognized answer twice and verify honest recovery. Record actual results in the worksheet.

## Paste-ready lesson and branches

**Lesson:** “Shared responsibility means Microsoft and the customer each have jobs to do. For an Azure virtual machine, Microsoft manages the physical host; the customer manages the guest operating system and applications. A managed platform moves more operational work to the service, but the customer still controls data and access. This explanation uses our course reference, Contoso Azure concepts.”

**Question:** “Contoso uses an Azure virtual machine. Who is responsible for patching its guest operating system?”

| Choice | Feedback, only after the learner responds |
| --- | --- |
| Contoso | “Correct. An Azure virtual machine is IaaS. Contoso manages the guest operating system, including its patching. Microsoft operates the physical infrastructure.” |
| Microsoft | “Microsoft operates the physical infrastructure. Contoso still manages the guest operating system in this IaaS example. You may be thinking of a managed platform, where the service manages the operating system.” |
| Nobody | “The operating system still needs maintenance. Moving it to a virtual machine does not remove that work; Contoso remains responsible for the guest operating system.” |
| Default or empty | “We can pause here. I could not match that answer to a choice. Review shared responsibility in the course reference, or discuss it with a mentor. I cannot contact a mentor from this agent.” |

These are **original teaching materials**, not real exam questions. A fixed authored lesson is a controlled instructional message. It does not prove generative retrieval; step 3 supplies that separate test.

## Seven-minute learner exercise

1. **Minutes 0-2:** Rewrite the incorrect-answer feedback to explain the misconception in your own words.
2. **Minutes 2-5:** Trace the nodes and tell your partner, or write down, exactly when the agent waits and which feedback follows the Microsoft choice. The instructor tests a selected example. Label predictions **PREDICTED** and its actual response **OBSERVED DEMO**.
3. **Minutes 5-7:** Record the supporting passage, the wait point, and your feedback. Explain why an automatically filled topic input is wrong for a new quiz answer.

**Worked answer:** “Microsoft manages the physical host, but Contoso manages the guest OS. I confused the host with the guest.” The wait point is the Question node configured **Ask every time**, not a question mark in a Message node.

**Recovery:** If knowledge is still processing, inspect the file and mark retrieval **NOT RUN**. If authoring is blocked, use the worksheet and complete the build after class. Do not call observer predictions a working assistant.

**Optional after class:** Use the Module 1 trial walkthrough, then complete the full build from step 1 in your approved environment. You do not need an instructor-shared flow. This is independent practice, not required class participation. Use the [instructor guide](../../instructor/02-build-guide.md) for automatic inputs, fallback repair, source limits, and the official-guide extension.
