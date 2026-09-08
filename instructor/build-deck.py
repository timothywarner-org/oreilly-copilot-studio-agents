"""Build the O'Reilly deck from instructor/teaching-slides.json using the repo-root template.

Structure follows Tim's shipped prompt-pro O'Reilly deck: course title, timed course flow,
session materials, Q&A housekeeping, segment dividers, content, Warner's Laws, thank-you.
Speaker notes come straight from the manuscript, which is already voice-linted.
"""
import copy
import json
import os
import re

from pptx import Presentation
from pptx.util import Pt

REPO = "C:/github/oreilly-copilot-studio-agents"
os.chdir(REPO)

TEMPLATE = "oreilly_blue_slide_template.pptx"
MANIFEST = "instructor/teaching-slides.json"
# Rebuild the exact learner-approved artifact so the README does not point at a stale private copy.
OUT = "slides/Warner-CopilotStudio-Agents-2026-09-08.pptx"

REPO_URL = "github.com/timothywarner-org/oreilly-copilot-studio-agents"

L_COVER = 0        # TITLE_2: TITLE + SUBTITLE
L_CONTENT = 2      # CUSTOM: TITLE + BODY + BODY + slide number
L_STATEMENT = 22   # CUSTOM_2: TITLE only
L_DIVIDER = 23     # CUSTOM_2_1: TITLE only


def strip_all_slides(prs):
    """Remove the template's 19 demo slides, leaving masters and layouts intact."""
    xml_slides = prs.slides._sldIdLst
    for sld in list(xml_slides):
        rId = sld.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        prs.part.drop_rel(rId)
        xml_slides.remove(sld)


def ph(slide, idx):
    for p in slide.placeholders:
        if p.placeholder_format.idx == idx:
            return p
    return None


def fit_size(lines):
    """Pick a point size from content density. The template body box is roughly
    8.6in x 3.4in, so about 95 characters per line at 14pt."""
    total = sum(len(l) for l in lines)
    longest = max((len(l) for l in lines), default=0)
    count = len([l for l in lines if l.strip()])
    if total > 520 or longest > 130 or count > 7:
        return 11
    if total > 380 or longest > 95 or count > 6:
        return 12
    if total > 260 or longest > 70:
        return 13
    return 15


def set_text(placeholder, lines, size=None):
    tf = placeholder.text_frame
    tf.clear()
    tf.word_wrap = True
    if size is None:
        size = fit_size(lines)
    for i, line in enumerate(lines):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = line
        for run in para.runs:
            run.font.size = Pt(size)


def drop_placeholder(slide, idx):
    p = ph(slide, idx)
    if p is not None:
        p._element.getparent().remove(p._element)


def add(prs, layout_idx, notes=None):
    slide = prs.slides.add_slide(prs.slide_layouts[layout_idx])
    if notes:
        slide.notes_slide.notes_text_frame.text = notes
    return slide


def title_of(slide, text, size=None):
    t = slide.shapes.title
    if t is None:
        t = ph(slide, 0)
    set_text(t, [text], size)
    return t


def clean(text):
    """Manuscript titles carry hard line breaks for the cover; flatten for body slides."""
    return re.sub(r"\s*\n\s*", " ", text).strip()


def main():
    deck = json.load(open(MANIFEST, encoding="utf-8"))
    slides = deck["slides"]
    by_id = {s["id"]: s for s in slides}

    prs = Presentation(TEMPLATE)
    strip_all_slides(prs)

    # 1. Course title
    s = add(prs, L_COVER, by_id["S01"]["notes"])
    title_of(s, "Build AI Agents to\nAutomate Your Workflows")
    sub = ph(s, 1)
    if sub is not None:
        set_text(sub, ["Tim Warner  |  September 8, 2026",
                       "Microsoft Copilot Studio  |  TechTrainerTim.com"])

    # 2. Course flow
    s = add(prs, L_CONTENT,
            "Here's our shape for the morning, all times Central. Four segments, three ten-minute "
            "breaks, and a wrap-up at the end. I'll build one agent straight through all four, and "
            "you'll never need an account to take part. If you have to step away, the breaks land on "
            "the hour, so you can plan around them.")
    title_of(s, "Course flow (Central Time)")
    set_text(ph(s, 1), [
        "09:00  Segment 1 [Inception: design the agent]",
        "10:00  Segment 2 [Build: knowledge and grounded answers]",
        "11:00  Segment 3 [Extend: actions, MCP, handoff]",
        "12:00  Segment 4 [Operate: evaluate, govern, publish]",
        "12:50  Wrap-up, next steps, and Q&A",
        "Ten-minute breaks at 09:50, 10:50, and 11:50",
    ])
    drop_placeholder(s, 2)

    # 3. Session materials
    s = add(prs, L_CONTENT,
            "Everything I use today lives in one public-facing repo, and I'd rather you had the link "
            "now than hunt for it later. You'll find the agent kit, the four labs, the worksheets, and "
            "a verified link register with every Microsoft Learn page behind this course. Grab it now, "
            "because the demos move quickly and I want you following along rather than transcribing.")
    title_of(s, "Session materials")
    set_text(ph(s, 1), [
        REPO_URL,
        "",
        "The agent kit: brief, instructions, knowledge, topics, tool contracts, runbook",
        "Four labs and worksheets, with worked answers",
        "sources/link-register.md: every Learn page, grouped by segment and checked live",
    ])
    drop_placeholder(s, 2)

    # 4. Questions
    s = add(prs, L_CONTENT,
            "Quick housekeeping on questions. Put them in the Q&A window rather than chat, because "
            "chat scrolls and I'll lose them. Only the O'Reilly team and I can see the Q&A window, so "
            "ask freely. I'll take questions inside each segment rather than saving them all for the "
            "end, and I'd rather answer three good questions properly than twenty in a rush.")
    title_of(s, "Questions?")
    set_text(ph(s, 1), [
        "Use the Q&A window, not chat, so nothing scrolls away",
        "Only the O'Reilly team and I can read the Q&A window",
        "I answer inside each segment, not only at the end",
        "Session is recorded; materials stay in the repo",
    ])
    drop_placeholder(s, 2)

    divider_notes = {
        "Inception": "Segment one. Before anybody touches a control, we decide what this agent is for "
                     "and what it must refuse. A brief you can't test is just a wish, so we'll write one "
                     "that ends in a measurable boundary.",
        "Build": "Segment two. Now we give the agent something true to say and a conversation that "
                 "genuinely waits for the learner. Grounding and a real wait point are what separate a "
                 "study assistant from a chatbot with opinions.",
        "Extend": "Segment three, and this is where it gets fun. We hand the agent one bounded tool, "
                  "then spend most of our time on the harder question: where its authority stops and a "
                  "human's begins.",
        "Operate": "Segment four. Everything so far was building. This is the part that decides whether "
                   "anyone else should be allowed to use the thing, and we'll answer it with evidence "
                   "rather than enthusiasm.",
    }

    section_titles = {
        "Inception": "Segment 1\nInception: design the agent",
        "Build": "Segment 2\nBuild: knowledge and grounded answers",
        "Extend": "Segment 3\nExtend: actions, MCP, and handoff",
        "Operate": "Segment 4\nOperate: evaluate, govern, publish",
    }
    seen_sections = set()

    for src in slides:
        sec = src["section"]
        kind = src["kind"]
        if kind == "cover":
            continue  # already used as the course title

        if sec in section_titles and sec not in seen_sections:
            seen_sections.add(sec)
            d = add(prs, L_DIVIDER, divider_notes.get(sec))
            title_of(d, section_titles[sec])

        if kind == "break":
            b = add(prs, L_STATEMENT, src["notes"])
            title_of(b, clean(src["title"]) + "\n" + (src["lines"][0] if src["lines"] else ""))
            continue

        if kind == "closing":
            c = add(prs, L_CONTENT, src["notes"])
            title_of(c, clean(src["title"]))
            set_text(c and ph(c, 1), src["lines"])
            drop_placeholder(c, 2)
            continue

        s = add(prs, L_CONTENT, src["notes"])
        title_of(s, clean(src["title"]))
        lines = src["lines"]
        # Manuscript tables encode "left | right"; keep the pipe, it reads fine at 14pt.
        set_text(ph(s, 1), lines)
        drop_placeholder(s, 2)

    # Warner's Laws, his signature closing artifact
    s = add(prs, L_CONTENT,
            "I close every course with a short list of laws, because principles survive a product "
            "rename and screenshots don't. These six are the whole morning compressed. If you forget "
            "every click I showed you, keep these. Number one is the one I'd tattoo on the inside of "
            "your eyelids: a fluent answer isn't proof that a tool ran, and the only cure is to go and "
            "look at the execution record yourself.")
    title_of(s, "Warner's Laws of Agent Building")
    set_text(ph(s, 1), [
        "1.  A fluent answer isn't proof that a tool ran. Go read the activity record.",
        "2.  Instructions steer behavior. They never grant permission.",
        "3.  If the agent doesn't wait, it isn't teaching. It's lecturing.",
        "4.  Ground it or don't claim it. A citation is something you inspect.",
        "5.  Name the boundary before you name the features.",
        "6.  A green score on the wrong test set is just a nicer way to be wrong.",
    ])
    drop_placeholder(s, 2)

    # Thank you
    s = add(prs, L_CONTENT,
            "That's our four hours. Thank you for spending your morning with me, and please do fill in "
            "the course evaluation, because O'Reilly reads every one and it genuinely shapes what I get "
            "to teach next. All the materials stay in the repo, so nothing you saw today disappears "
            "when this window closes. I hope you found this session helpful, and I'll see you next time.")
    title_of(s, "Thank you for attending")
    set_text(ph(s, 1), [
        "Please complete the course evaluation",
        "",
        "Session materials:  " + REPO_URL,
        "Tim Warner  |  TechTrainerTim.com",
    ])
    drop_placeholder(s, 2)

    os.makedirs(".local", exist_ok=True)
    prs.save(OUT)

    notes_n = sum(1 for sl in prs.slides if sl.has_notes_slide
                  and sl.notes_slide.notes_text_frame.text.strip())
    print(f"built: {OUT}")
    print(f"slides: {len(prs.slides)}   slides with speaker notes: {notes_n}")
    print(f"size: {os.path.getsize(OUT)/1024:.0f} KB")


if __name__ == "__main__":
    main()
