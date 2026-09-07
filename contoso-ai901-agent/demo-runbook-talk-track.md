# Live talk track - Contoso AI Fundamentals Coach

**Drafted in Tim's spoken register and linted. [SAY] blocks are yours to recite; [DO], [VERIFY],
[PAUSE], and [IF IT BREAKS] are stage directions and aren't governed by the voice rules.**

**Three [SAY] blocks carry a labeled opinion and are marked PROPOSED. Those are your professional
judgment going in front of an audience, not mine. Read them, change them, or cut them, but sign
off before you say them.**

Timing runs about 155 words of [SAY] per minute. Demo time sits on top of that.

## Segment 1: Open and clear the assumptions (~2 min)

[SAY] Welcome to the session. Tim Warner here, and over the next four hours I'm gonna teach you
how to design, build, extend, and operate an AI agent in Microsoft Copilot Studio. We're building
one agent the whole way through, and it gets more capable every hour.

[SAY] Here's what I'm assuming about you. You work somewhere in the Microsoft 365 or Power
Platform world, you've got a browser open, and you're comfortable clicking around a portal. You
don't need to write code today, you don't need an API key, and you don't need any Copilot Studio
experience at all. I'm driving the tenant and you're making the design calls, and that's how we
run the whole session, so we're dialed in.

## Segment 2: The exam correction (~1 min)

[SAY] One correction before we go anywhere, because it changes what we're building. Microsoft
retired AI-900 on June thirtieth of this year. The exam behind Azure AI Fundamentals is AI-901
now, and the certification name didn't change at all, so anybody who earned it the old way holds
exactly the credential you'd earn today. Our Contoso agent coaches people toward AI-901.

[SAY] Now you might be looking at the course description and thinking, hang on, Tim, the
objective on that page says AI-901. You're right, and I'm leaving it right where it is, because
it's the published objective and I don't get to quietly rewrite it mid-session. The design skill
is identical either way. Grounding a study assistant in approved evidence works the same whether
the subject is cloud fundamentals or AI fundamentals, and I'd rather build against an exam
somebody can actually register for.

## Segment 3: Boundaries, stated before they're demonstrated (~2 min)

[SAY] Before I build anything, I want to tell you what this agent isn't allowed to do, because
you should be able to predict its behavior before you ever watch it run. It won't state a fact it
can't trace back to a source somebody gave it. It won't use or invent real exam items, and it
won't tell anybody they're going to pass. And it won't write into SharePoint or Teams until the
person in that conversation says yes, in that turn, to that specific thing.

[SAY] Every hour I add one capability, and every capability I add creates a new thing I have to
prove. That pairing is the course. If you take one idea home today, take that one.

## Segment 4: Create the shell (~4 min)

[DO] Copilot Studio > Create > New agent. Name: Contoso AI Fundamentals Coach. Paste the
description, then Overview > Instructions > Edit, paste the instruction block, Save.
[VERIFY] Instructions saved without a length warning. Character count well under the cap.

[SAY] Notice that the description isn't decoration. Under generative orchestration the agent
reads these names and descriptions to work out what to call and when, so the description is doing
routing work. When routing goes sideways later today, that's the first place I'll look, and the
instructions are the second.

[DO] In the instructions editor, type "/" and insert a live reference to a topic or tool.
[SAY] Watch this. When I type a slash, I can point at an actual object instead of describing it
in prose, and that's the difference between an instruction that hopes and an instruction that
wires up.

[PAUSE] Take questions here before knowledge goes in.

## Segment 5: Knowledge, and the refusal that matters (~5 min)

[DO] Knowledge > Add > upload ai901-concepts.txt. Wait for ready. Test: "What are the responsible
AI principles?"
[VERIFY] Response names fairness, reliability and safety, privacy and security, inclusiveness,
transparency, and accountability, with a citation to the uploaded file.

[SAY] That works, and honestly that's the boring half. Let me show you the half I care about.

[DO] Test: "How many questions are on the AI-901 exam?"
[VERIFY] Stated limitation plus a pointer to the official study guide. No number.

[SAY] The file doesn't say, so the agent says it can't verify that and points at the official
study guide. That refusal is worth more to you than the answer before it, because a study
assistant that invents an exam detail is worse than no study assistant at all. And getting a
model to say "I don't know" reliably is genuinely hard. It's mostly a grounding job rather than a
prompting job, which is why we scoped the source before we wrote a single clever sentence.

## Segment 6: The practice topic and the wait point (~15 min)

[SAY] Somebody out there is thinking, Tim, I could hard-code a practice question in about ninety
seconds. You absolutely could, and then you'd do it again for the next question, and again for
the one after that, and pretty soon you've got a topic per exam item and a maintenance problem
you'll be sweeping up for months. So we're building one topic that any question flows through,
and the question itself becomes data.

[DO] Build: Question node for the study area, condition that loads the evidence packet, prompt
call, validation condition, message with the question and choices, Question node with A/B/C.

[SAY] This next node is the whole reason we're here. It's the only place in the entire build
where a machine stops and a human decides. Watch the turn end right here.

[DO] Test: "Quiz me on AI-901" > choose an area > read the item > stop.
[VERIFY] The turn ends on the question. No grading, no explanation, no answer key on screen.

[SAY] That's exactly what we want to see. The agent presented an item and then it waited.
[IF IT BREAKS] If the agent answers its own question, don't paper over it. Trace it live, show
the skip setting on the question node, and let them watch the fix.

[SAY] Now I'm going to answer it wrong on purpose, because the grading has to come from this
item's saved key rather than from whatever the model remembers.
[DO] Choose a wrong option. Then request another question and answer that one correctly.
[VERIFY] Correct letter differs between the two items. Both graded correctly.

## Segment 7: Work that changes other systems (~19 min)

[DO] Show the empty SharePoint list. Show the empty Teams channel. Leave both visible.

[SAY] Hold onto those two empty screens for the next few minutes, because everything we do now
gets measured against them.

[DO] Test: "I booked my AI-901 exam." Then answer "no."
[VERIFY] Confirmation prompt appeared. List still empty. Channel still empty.

[SAY] The agent asked, I declined, and now look at the list and look at the channel. Both still
empty. Proving that nothing happened is harder than proving something did, and it's the check
almost every agent demo skips.

[DO] Fresh test: "I booked my AI-901 exam." Answer "yes." Open the flow run.

[SAY] The employee says yes, and only then does the agent make it so. Now here's the part I want
you doing at work on Monday. I'm opening the flow run, I'm reading the status it actually
returned, and then I'm reading what the agent said, and I'm comparing the two. A fluent sentence
isn't evidence that anything happened.

[SAY] **[PROPOSED, needs your sign-off]** Suppose SharePoint works and the Teams post fails. The
honest answer is that the milestone got saved and the announcement didn't go out, and that
deserves a status of its own. Here's my take rather than Microsoft's guidance: design the partial
outcome before you design the happy path, because somebody downstream is waiting on a
notification that never arrived, and a workflow that reports "done" for that case has told them a
lie. It costs you one more branch and it buys you a system people can trust.

## Segment 8: Evidence, and what a score can't tell you (~13 min)

[DO] Evaluation > New evaluation > Single response > download template > compare > import the
five cases > configure Compare meaning > run.

[SAY] **[PROPOSED, needs your sign-off]** Eighty percent is my threshold here, not Microsoft's.
Pick your own number and be ready to defend it, because the threshold is a business decision
about what you'll tolerate rather than something the product hands you.

[SAY] Look at the booking case. It scored a clean pass on meaning, and I want to show you what
that score doesn't cover. The agent said the right words about asking permission, and semantic
comparison measured the words. It never looked at SharePoint. A score with no trace behind it is
a parlor trick, so let's open the trace and see whether anything actually got written.

[DO] Open the trace for that case. Show tool invocations. Show the destinations unchanged.

[SAY] **[PROPOSED, needs your sign-off]** Here's where I'd go further than the documentation
does. A regression suite that only measures answers will pass an agent that writes to your
systems without permission, so I keep the write path in a separate controlled test with its own
destinations. That's my call, and the cost is that I maintain two suites instead of one.

## Segment 9: Close (~3 min)

[SAY] Let me give you the one two three. One, write down what your agent isn't allowed to do
before you create it, because that's the list you'll test against. Two, make the thing it
generates into data that flows through one structure, so you're maintaining a conversation rather
than a catalog. Three, never let the agent tell you what happened. Read the returned result and
then read what it said.

[SAY] Your homework isn't this agent. Pick one problem at your own shop, name the first
capability it would need, and name the one test that would settle whether you can trust it. If
you can answer that second part, you're ready to build.

[SAY] I hope you found this session helpful, and thanks a lot for spending your morning with me.
I'll see you next time.
