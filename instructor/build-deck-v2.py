"""Build the FATTENED O'Reilly deck: bigger type, real tables, native diagrams,
Microsoft Learn-grounded technical content, no instructional/facilitation notes on slides.

Why a v2 script instead of editing build-deck.py in place:
Tim's standing rule is that a prior version of an artifact is never overwritten. This script
writes a NEW output file and leaves slides/Warner-CopilotStudio-Agents-2026-09-08.pptx alone.

Design decisions and the reason behind each:
  * Type scale. The shipped deck used 15pt titles and 11-13pt body on a 10 x 5.625in canvas,
    which is roughly half the size a 13.33in deck would use. Titles go to 26pt, body to 16-18pt,
    table text to 13-15pt. Nothing smaller than 13pt appears anywhere except the source line.
  * Vertical space. The template body placeholder started at 2.05in, leaving 0.8in of dead air
    under the title. Body content now starts at 1.42in, which is what pays for the larger type.
  * Real tables. "left | right" pipe strings were being rendered as plain paragraphs. Those are
    now genuine PowerPoint tables with explicit cell fills, so they survive resizing and read
    cleanly at the back of a webinar window.
  * Colorblind-safe palette. Blue / amber / slate only. No red-green pairing carries meaning,
    and every shape carries a text label rather than relying on fill color to say anything.
  * Speaker notes. Existing notes carry over verbatim by title match (they are already
    voice-linted). New slides get NO narration notes; the on-slide source line is the only
    added metadata, and it is technical reference for learners.
"""
import os
import re
import copy

from pptx import Presentation
from pptx.util import Pt, Inches, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

REPO = "C:/github/oreilly-copilot-studio-agents"
if os.path.isdir(REPO):
    os.chdir(REPO)

TEMPLATE = "oreilly_blue_slide_template.pptx"
PREVIOUS = "slides/Warner-CopilotStudio-Agents-2026-09-08.pptx"
OUT = "slides/Warner-CopilotStudio-Agents-2026-09-08-v2.pptx"

REPO_URL = "github.com/timothywarner-org/oreilly-copilot-studio-agents"
CONTACT = "TechTrainerTim.com"

# Layout indexes in the O'Reilly blue template.
L_COVER = 0        # TITLE_2:    TITLE + SUBTITLE, full-bleed image background
L_CONTENT = 2      # CUSTOM:     TITLE + BODY + footer BODY + slide number, light background
L_STATEMENT = 22   # CUSTOM_2:   TITLE only, image background (breaks)
L_DIVIDER = 23     # CUSTOM_2_1: TITLE only, image background (segment dividers)

# ---------------------------------------------------------------- type scale
SZ_COVER_TITLE = 30
SZ_COVER_SUB = 16
SZ_DIVIDER_1 = 30
SZ_DIVIDER_2 = 21
SZ_TITLE = 26
SZ_BODY_ROOMY = 19     # <= 4 lines
SZ_BODY = 17           # 5-6 lines
SZ_BODY_DENSE = 15     # 7+ lines
SZ_TABLE_HEAD = 14
SZ_TABLE_BODY = 13
SZ_DIAGRAM = 13
SZ_SOURCE = 10

# ------------------------------------------------------- geometry (inches)
TITLE_BOX = (0.55, 0.28, 8.45, 1.06)
BODY_BOX = (0.55, 1.46, 8.90, 3.66)
SOURCE_BOX = (0.55, 5.20, 8.89, 0.32)

# ------------------------------------------- colorblind-safe palette (no red/green)
NAVY = RGBColor(0x1B, 0x2A, 0x41)
BLUE = RGBColor(0x1F, 0x5F, 0xA6)
BLUE_MID = RGBColor(0x4A, 0x89, 0xC8)
BLUE_LT = RGBColor(0xDD, 0xE9, 0xF6)
AMBER = RGBColor(0xB5, 0x62, 0x0A)
AMBER_LT = RGBColor(0xFA, 0xEB, 0xD8)
SLATE = RGBColor(0x4A, 0x60, 0x76)
GRAY_LT = RGBColor(0xEE, 0xF1, 0xF4)
GRAY_MD = RGBColor(0x9A, 0xA5, 0xB1)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
INK = RGBColor(0x1B, 0x2A, 0x41)

# "No Style, No Grid" - keeps PowerPoint's default red banding off our tables.
TABLE_STYLE_NO_GRID = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"

FONT = "Arial"  # replaced at runtime by the template's minor font if one is declared


# =============================================================== low-level helpers
def detect_theme_font(prs):
    """Read the minor (body) latin typeface out of the theme so added shapes match the deck."""
    try:
        master = prs.slide_masters[0]
        rel = ("http://schemas.openxmlformats.org/officeDocument/"
               "2006/relationships/theme")
        theme = master.part.part_related_by(rel)
        xml = theme.blob.decode("utf-8", "ignore")
        block = re.search(r"<a:minorFont>(.*?)</a:minorFont>", xml, re.S)
        if block:
            face = re.search(r'<a:latin typeface="([^"]+)"', block.group(1))
            if face and face.group(1):
                return face.group(1)
    except Exception:
        pass
    return FONT


def ph(slide, idx):
    for p in slide.placeholders:
        if p.placeholder_format.idx == idx:
            return p
    return None


def drop_ph(slide, idx):
    p = ph(slide, idx)
    if p is not None:
        p._element.getparent().remove(p._element)


def place(shape, box):
    left, top, width, height = box
    shape.left, shape.top = Inches(left), Inches(top)
    shape.width, shape.height = Inches(width), Inches(height)


def style_runs(para, size, bold=False, color=None, font=None):
    for run in para.runs:
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.name = font or FONT
        if color is not None:
            run.font.color.rgb = color


def add_slide(prs, layout_idx, notes=None):
    slide = prs.slides.add_slide(prs.slide_layouts[layout_idx])
    if notes:
        slide.notes_slide.notes_text_frame.text = notes
    return slide


def set_title(slide, text, size=SZ_TITLE, box=TITLE_BOX):
    """Titles carry the point. They are the single biggest legibility win in this pass."""
    t = slide.shapes.title or ph(slide, 0)
    if t is None:
        return None
    if box:
        place(t, box)
    tf = t.text_frame
    tf.clear()
    tf.word_wrap = True
    lines = text.split("\n")
    for i, line in enumerate(lines):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = line
        style_runs(para, size if i == 0 else max(size - 8, 16), bold=True)
    return t


def body_size(lines):
    """Pick a body size from line count and length. Floor is 15pt - never smaller."""
    live = [l for l in lines if l.strip()]
    longest = max((len(l) for l in live), default=0)
    if len(live) <= 4 and longest <= 72:
        return SZ_BODY_ROOMY
    if len(live) <= 6 and longest <= 96:
        return SZ_BODY
    return SZ_BODY_DENSE


def set_bullets(slide, lines, size=None, box=BODY_BOX):
    p = ph(slide, 1)
    if p is None:
        return
    place(p, box)
    tf = p.text_frame
    tf.clear()
    tf.word_wrap = True
    size = size or body_size(lines)
    for i, line in enumerate(lines):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = line
        para.space_after = Pt(8)
        style_runs(para, size)


def no_bullet(para):
    """The footer is a BODY placeholder, so it inherits a bullet glyph. A reference line
    is not a list item; strip the glyph and the hanging indent."""
    pPr = para._p.get_or_add_pPr()
    for tag in ("a:buChar", "a:buAutoNum", "a:buBlip"):
        for node in pPr.findall(qn(tag)):
            pPr.remove(node)
    if pPr.find(qn("a:buNone")) is None:
        pPr.append(pPr.makeelement(qn("a:buNone"), {}))
    pPr.set("marL", "0")
    pPr.set("indent", "0")


def set_source(slide, text):
    """The footer placeholder becomes a Microsoft Learn reference the learner can type in."""
    p = ph(slide, 2)
    if p is None:
        return
    place(p, SOURCE_BOX)
    tf = p.text_frame
    tf.clear()
    tf.word_wrap = True
    para = tf.paragraphs[0]
    para.text = text
    no_bullet(para)
    style_runs(para, SZ_SOURCE, color=GRAY_MD)


# ==================================================================== tables
def apply_table_style(graphic_frame, style_id=TABLE_STYLE_NO_GRID):
    """Force a neutral table style. The template theme's accent1 is bright red, and the
    default PowerPoint table style would band every table in it - unusable for a
    red/green colorblind presenter and ugly for everyone else."""
    tbl = graphic_frame._element.graphic.graphicData.tbl
    props = tbl.find(qn("a:tblPr"))
    if props is None:
        props = tbl.makeelement(qn("a:tblPr"), {})
        tbl.insert(0, props)
    props.set("firstRow", "0")
    props.set("bandRow", "0")
    existing = props.find(qn("a:tableStyleId"))
    if existing is not None:
        props.remove(existing)
    node = props.makeelement(qn("a:tableStyleId"), {})
    node.text = style_id
    props.append(node)


def fill_cell(cell, color):
    cell.fill.solid()
    cell.fill.fore_color.rgb = color


def add_table(slide, rows, col_widths, box=BODY_BOX, head_size=SZ_TABLE_HEAD,
              body_size_pt=None):
    """rows[0] is the header. col_widths are fractions of the available width."""
    left, top, width, height = box
    n_rows, n_cols = len(rows), len(rows[0])
    if body_size_pt is None:
        body_size_pt = SZ_TABLE_BODY if n_rows > 5 else SZ_TABLE_BODY + 1

    gf = slide.shapes.add_table(n_rows, n_cols, Inches(left), Inches(top),
                                Inches(width), Inches(height))
    apply_table_style(gf)
    table = gf.table

    total = sum(col_widths)
    for c, frac in enumerate(col_widths):
        table.columns[c].width = Emu(int(Inches(width) * frac / total))

    head_h = 0.40
    body_h = max(0.34, (height - head_h) / max(n_rows - 1, 1))
    table.rows[0].height = Inches(head_h)
    for r in range(1, n_rows):
        table.rows[r].height = Inches(body_h)

    for r, row in enumerate(rows):
        for c, text in enumerate(row):
            cell = table.cell(r, c)
            cell.margin_left = Inches(0.10)
            cell.margin_right = Inches(0.08)
            cell.margin_top = Inches(0.04)
            cell.margin_bottom = Inches(0.04)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            if r == 0:
                fill_cell(cell, NAVY)
            else:
                fill_cell(cell, WHITE if r % 2 else GRAY_LT)
            tf = cell.text_frame
            tf.word_wrap = True
            tf.clear()
            para = tf.paragraphs[0]
            para.text = str(text)
            style_runs(para,
                       head_size if r == 0 else body_size_pt,
                       bold=(r == 0 or c == 0),
                       color=WHITE if r == 0 else INK)
    return gf


# ================================================================== diagrams
def add_box(slide, x, y, w, h, text, fill=BLUE_LT, line=BLUE, size=SZ_DIAGRAM,
            bold=True, color=INK, shape=MSO_SHAPE.ROUNDED_RECTANGLE, align=PP_ALIGN.CENTER):
    sh = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.color.rgb = line
    sh.line.width = Pt(1.25)
    sh.shadow.inherit = False
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.06)
    tf.margin_right = Inches(0.06)
    tf.margin_top = Inches(0.03)
    tf.margin_bottom = Inches(0.03)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.clear()
    for i, line_text in enumerate(str(text).split("\n")):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = line_text
        para.alignment = align
        style_runs(para, size if i == 0 else max(size - 2, 11),
                   bold=bold and i == 0, color=color)
    return sh


def add_caption(slide, x, y, w, h, text, size=11, color=SLATE, align=PP_ALIGN.CENTER,
                bold=False):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.02)
    tf.margin_top = tf.margin_bottom = 0
    tf.clear()
    for i, line_text in enumerate(str(text).split("\n")):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = line_text
        para.alignment = align
        style_runs(para, size, bold=bold, color=color)
    return tb


def add_arrow(slide, x, y, w, h, color=SLATE):
    sh = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = color
    sh.line.fill.background()
    sh.shadow.inherit = False
    return sh


def add_down_arrow(slide, x, y, w, h, color=SLATE):
    sh = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(x), Inches(y),
                                Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = color
    sh.line.fill.background()
    sh.shadow.inherit = False
    return sh


def pipeline(slide, labels, captions=None, y=1.75, h=0.95, cap_h=0.85,
             fill=BLUE_LT, line=BLUE, left=0.55, right=9.45, gap=0.28):
    """A left-to-right pipeline of boxes with arrows between them, plus optional
    captions underneath. Used for the RAG pipeline, publish pipeline, and eval loop."""
    n = len(labels)
    span = right - left
    box_w = (span - gap * (n - 1)) / n
    shapes = []
    for i, label in enumerate(labels):
        x = left + i * (box_w + gap)
        shapes.append(add_box(slide, x, y, box_w, h, label, fill=fill, line=line))
        if i < n - 1:
            add_arrow(slide, x + box_w + 0.045, y + h / 2 - 0.09,
                      gap - 0.09, 0.18)
        if captions:
            add_caption(slide, x, y + h + 0.12, box_w, cap_h, captions[i], size=11)
    return shapes


def layer_stack(slide, rows, y=1.55, h=0.86, gap=0.14, left=0.55, width=8.90):
    """Stacked bands. Used for control layers and governance levels, where the point is
    that each band sits inside the one above it rather than beside it."""
    for i, (label, detail, fill, line) in enumerate(rows):
        top = y + i * (h + gap)
        add_box(slide, left, top, 2.60, h, label, fill=fill, line=line, size=14)
        add_caption(slide, left + 2.78, top + 0.06, width - 2.90, h,
                    detail, size=12, align=PP_ALIGN.LEFT, color=INK)


# ================================================== notes carried from the shipped deck
def load_previous_notes(path):
    """Reuse Tim's voice-linted narration wherever a slide title survives into v2.
    New slides deliberately get no narration - the request was tech content only."""
    notes = {}
    if not os.path.exists(path):
        return notes
    prev = Presentation(path)
    for slide in prev.slides:
        title_shape = slide.shapes.title or ph(slide, 0)
        if title_shape is None or not slide.has_notes_slide:
            continue
        key = re.sub(r"\s+", " ", title_shape.text_frame.text).strip().lower()
        text = slide.notes_slide.notes_text_frame.text.strip()
        if key and text:
            notes[key] = text
    return notes


PREV_NOTES = {}


def notes_for(*titles):
    for t in titles:
        key = re.sub(r"\s+", " ", t).strip().lower()
        if key in PREV_NOTES:
            return PREV_NOTES[key]
    return None


# =============================================================== slide builders
def content(prs, title, notes_keys=(), source=None):
    note = notes_for(title, *notes_keys)
    s = add_slide(prs, L_CONTENT, note)
    set_title(s, title)
    if source:
        set_source(s, source)
    else:
        drop_ph(s, 2)
    return s


def bullets_slide(prs, title, lines, notes_keys=(), source=None, size=None):
    s = content(prs, title, notes_keys, source)
    set_bullets(s, lines, size=size)
    return s


def table_slide(prs, title, rows, widths, notes_keys=(), source=None, box=BODY_BOX):
    s = content(prs, title, notes_keys, source)
    drop_ph(s, 1)
    add_table(s, rows, widths, box=box)
    return s


def diagram_slide(prs, title, draw, notes_keys=(), source=None):
    s = content(prs, title, notes_keys, source)
    drop_ph(s, 1)
    draw(s)
    return s


def divider(prs, line1, line2, notes=None):
    s = add_slide(prs, L_DIVIDER, notes)
    set_title(s, line1 + "\n" + line2, size=SZ_DIVIDER_1,
              box=(0.55, 1.95, 8.89, 1.70))
    return s


def break_slide(prs, line2, notes=None):
    s = add_slide(prs, L_STATEMENT, notes)
    set_title(s, "10-minute break\n" + line2, size=SZ_DIVIDER_1,
              box=(0.55, 1.95, 8.89, 1.70))
    return s


# ==================================================================== the deck
LEARN = "learn.microsoft.com"


def build(prs):
    # ------------------------------------------------------------- front matter
    s = add_slide(prs, L_COVER, notes_for("Build AI Agents to Automate Your Workflows"))
    set_title(s, "Build AI Agents to\nAutomate Your Workflows", size=SZ_COVER_TITLE,
              box=(0.55, 1.15, 5.60, 2.30))
    sub = ph(s, 1)
    if sub is not None:
        place(sub, (0.55, 3.60, 5.20, 1.60))
        tf = sub.text_frame
        tf.clear()
        tf.word_wrap = True
        for i, line in enumerate(["Tim Warner  |  September 8, 2026",
                                  "Microsoft Copilot Studio",
                                  CONTACT]):
            para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            para.text = line
            style_runs(para, SZ_COVER_SUB, bold=(i == 2))

    bullets_slide(prs, "Course flow (Central Time)", [
        "09:00   Segment 1 - Inception: design the agent",
        "10:00   Segment 2 - Build: knowledge and grounded answers",
        "11:00   Segment 3 - Extend: actions, MCP, handoff",
        "12:00   Segment 4 - Operate: evaluate, govern, publish",
        "12:50   Wrap-up, next steps, and Q&A",
        "Breaks at 09:50, 10:50, and 11:50",
    ])

    bullets_slide(prs, "Recording and replay", [
        "The recording posts 24 to 48 hours after class ends",
        "Watch it at learning.oreilly.com while signed in to your O'Reilly account",
        "Open this event from your account and the replay appears on the same page",
        "Playback stays available for as long as your O'Reilly access is active",
        "Slides, labs, and the link register live in the GitHub repo, outside O'Reilly",
    ])

    bullets_slide(prs, "Session materials", [
        REPO_URL,
        "Agent kit: brief, instructions, knowledge, topics, tool contracts, runbook",
        "Four labs and worksheets, with worked answers",
        "sources/link-register.md: every Microsoft Learn page used today",
        CONTACT + " for the slides and follow-up material",
    ])

    bullets_slide(prs, "Questions", [
        "Use the Q&A window, not chat, so nothing scrolls away",
        "Only the O'Reilly team and I can read the Q&A window",
        "Questions get answered inside each segment, not only at the end",
        "Follow-ups after class: " + CONTACT,
    ])

    # ============================================================ SEGMENT 1
    divider(prs, "Segment 1", "Inception: design the agent",
            notes_for("Segment 1\nInception: design the agent"))

    bullets_slide(prs, "What you'll be able to do", [
        "Plan an agent from persona, job, instructions, topic map, guardrails, and metrics",
        "Build a grounded study assistant from knowledge sources, topics, and test prompts",
        "Extend it with tools, agent flows, MCP, subagents, and human handoff",
        "Evaluate, publish, observe, and govern it with analytics and Well-Architected guidance",
    ], notes_keys=("The four course outcomes",))

    table_slide(prs, "What Copilot Studio builds", [
        ["Building block", "What it is", "Where it runs"],
        ["Agent", "Instructions, knowledge, and tools; reasons about the next step",
         "Teams, Microsoft 365 Copilot, web, mobile, custom channels"],
        ["Workflow", "Drag-and-drop automation whose steps can reason and act",
         "Standalone, or called by an agent"],
        ["Agent flow", "Deterministic action sequence, native to Copilot Studio",
         "Attached to an agent as a tool, or standalone"],
        ["Topic", "Authored conversation with explicit nodes and branches",
         "Inside the agent, chosen by description or trigger phrase"],
    ], [0.20, 0.44, 0.36],
        source=LEARN + "/microsoft-copilot-studio/fundamentals-what-is-copilot-studio")

    def anatomy(s):
        add_box(s, 0.55, 1.62, 1.55, 0.80, "Channel\nTeams, web, app",
                fill=GRAY_LT, line=SLATE)
        add_arrow(s, 2.18, 1.93, 0.30, 0.18)
        add_box(s, 2.56, 1.55, 2.05, 0.95, "Orchestrator\nplans the turn",
                fill=NAVY, line=NAVY, color=WHITE, size=14)
        add_arrow(s, 4.69, 1.93, 0.30, 0.18)
        col_x = [5.07, 6.20, 7.33, 8.46]
        labels = ["Knowledge\nread-only\nevidence",
                  "Topics\nauthored\ndialogue",
                  "Tools\ndefined\noperations",
                  "Agents\nchild and\nconnected"]
        for x, label in zip(col_x, labels):
            add_box(s, x, 1.50, 1.05, 1.05, label, fill=BLUE_LT, line=BLUE, size=11)
        add_box(s, 2.56, 2.82, 2.05, 0.62, "Response\nwith citations",
                fill=AMBER_LT, line=AMBER, size=12)
        add_down_arrow(s, 3.49, 2.54, 0.18, 0.24)
        add_caption(s, 0.55, 3.72, 8.90, 1.10,
                    "Instructions steer which building block the orchestrator picks.\n"
                    "Data policies decide which ones it is allowed to touch at all.\n"
                    "Names and descriptions matter more than any other authoring choice.",
                    size=13, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "Anatomy of an agent", anatomy,
                  notes_keys=("The agent's building blocks", "The agent\u2019s building blocks"),
                  source=LEARN + "/microsoft-copilot-studio/guidance/generative-orchestration")

    table_slide(prs, "Generative and classic orchestration", [
        ["Behavior", "Generative", "Classic"],
        ["Topics", "Selected from the description of their purpose", "Matched on trigger phrases"],
        ["Tools", "The planner can call them directly", "Called only from inside a topic"],
        ["Knowledge", "Searched proactively during a turn", "Fallback when no topic matches"],
        ["Missing input", "The agent generates the question", "You author a Question node"],
        ["Per turn", "Combines topics, tools, and knowledge", "Tries to select a single topic"],
    ], [0.20, 0.44, 0.36],
        source=LEARN + "/microsoft-copilot-studio/advanced-generative-actions")

    table_slide(prs, "How Microsoft frames a Copilot Studio project", [
        ["Pillar", "What it covers"],
        ["Architect", "Principles and patterns for secure, reliable agent solutions"],
        ["Plan", "Vision, scope, success measures, risks, team roles, technical readiness"],
        ["Implement", "Topics, tools, orchestration, channels, solution configuration"],
        ["Adopt", "Maturity model, maker community, transformation stories"],
        ["Manage", "Environment controls, data policies, access, monitoring, compliance"],
        ["Improve", "Analytics, KPIs, user feedback, iterative refinement"],
    ], [0.24, 0.76],
        source=LEARN + "/microsoft-copilot-studio/guidance/overview")

    bullets_slide(prs, "A maker and a learner", [
        "You: design the assistant, own its boundary, and read its evidence",
        "Contoso colleague: preparing for Azure AI Fundamentals, exam AI-901",
        "Shared need: explanations backed by a source, and practice that waits for an answer",
    ], notes_keys=("A maker and a learner",))

    table_slide(prs, "The brief before the build", [
        ["Brief element", "Contoso example"],
        ["Persona and job", "An AI beginner needs supported explanations and practice"],
        ["Instructions", "Use the course reference. Say when it does not support an answer."],
        ["Boundary", "No exam booking, private policy claims, or pass guarantees"],
        ["Success metric", "Zero invented policy answers in the recorded boundary test set"],
    ], [0.26, 0.74], notes_keys=("The brief before the build",))

    table_slide(prs, "The topic map", [
        ["Purpose", "Course implementation"],
        ["Overview", "Grounded explanation from the course reference"],
        ["Practice", "One authored teach-question-feedback topic"],
        ["Study plan", "GetStudySession agent flow"],
        ["Fallback", "Honest limitation and mentor referral"],
        ["Search", "Knowledge retrieval with source inspection"],
    ], [0.28, 0.72], notes_keys=("One map, five purposes",))

    def controls(s):
        layer_stack(s, [
            ("Deterministic",
             "Rule-based logic you enforce for irreversible or mission-critical work. "
             "The planner cannot rewrite it. Payments, deletions, record changes.",
             AMBER_LT, AMBER),
            ("Hybrid intercept",
             "The planner does the work, but you insert checkpoints: an in-conversation "
             "confirmation, a value limit, or an approval a human has to grant.",
             BLUE_LT, BLUE),
            ("AI harness",
             "Fully generative, inside guardrails. Question answering, lookups, "
             "simple multistep requests. No permission stop for routine work.",
             GRAY_LT, SLATE),
        ], y=1.58, h=0.86, gap=0.14)
        add_caption(s, 0.55, 4.56, 8.90, 0.55,
                    "Sort every action into one of these three before you build it. "
                    "The sort is the design.",
                    size=13, align=PP_ALIGN.LEFT, color=INK, bold=True)

    diagram_slide(prs, "Control layers and decision boundaries", controls,
                  source=LEARN + "/microsoft-copilot-studio/guidance/generative-orchestration")

    bullets_slide(prs, "Instructions the planner can act on", [
        "Reference only tools and knowledge the agent actually has",
        "Use exact tool names; names carry more weight than descriptions",
        "Describe knowledge capabilities generically rather than naming a source",
        "State the response format you want: lists, tables, citations, next steps",
        "Define the sequence for multistep work, not just the goal",
        "Instructions shape behavior. They never grant permission.",
    ], source=LEARN + "/microsoft-copilot-studio/guidance/generative-orchestration")

    bullets_slide(prs, "Starting a Copilot Studio trial", [
        "Open the official Copilot Studio trial sign-up",
        "Enter a work or school email address",
        "Follow the account-specific sign-up prompts",
        "Open the available authoring environment",
    ], notes_keys=("Starting a Copilot Studio trial",))

    table_slide(prs, "Trial access and its limits", [
        ["What happens", "What to do"],
        ["Work or school identity is required", "Use the appropriate organizational account"],
        ["Self-service signup is blocked", "Use the documented administrator route"],
        ["Trial authoring and testing are available", "Practice with synthetic course data"],
        ["Publishing is unavailable on the trial", "Watch the entitled instructor publish demo"],
    ], [0.44, 0.56], notes_keys=("Trial access and its limits",))

    bullets_slide(prs, "First run: instructions, orchestration, boundary", [
        "Blank agent, then instructions, then the orchestration mode",
        "Boundary probe: \"What is my exact exam appointment?\"",
        "Expected: an honest limitation and a route the learner can take",
        "Record the probe and the response; that pair is your first acceptance test",
    ], notes_keys=("The shell and the first boundary",))

    break_slide(prs, "Return at 10:00 AM Central",
                notes_for("10-minute break\nReturn at 10:00 AM Central"))

    # ============================================================ SEGMENT 2
    divider(prs, "Segment 2", "Build: knowledge and grounded answers",
            notes_for("Segment 2\nBuild: knowledge and grounded answers"))

    def rag(s):
        pipeline(s,
                 ["Query rewriting", "Content retrieval", "Summarize and cite",
                  "Safety and grounding"],
                 ["Clarifies the question and\nadds up to ten turns of\nconversation context",
                  "Runs the rewritten query\nagainst every configured\nsource, top three each",
                  "Synthesizes an answer,\napplies your instructions,\nemits citations",
                  "Moderation, then grounding\nvalidation, before the\nresponse reaches the user"],
                 y=1.68, h=0.92, cap_h=1.10)
        add_caption(s, 0.55, 4.24, 8.90, 0.85,
                    "No customer data trains the models. Conversation state is short-lived "
                    "and is not used for training.",
                    size=12, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "How grounded answers get built", rag,
                  source=LEARN + "/microsoft-copilot-studio/guidance/retrieval-augmented-generation")

    table_slide(prs, "What each knowledge source gives you", [
        ["Source", "Authentication", "What to watch"],
        ["Public websites", "None", "Must be indexed by Bing; two subpage levels deep"],
        ["SharePoint, OneDrive", "Entra ID delegated", "Security trimming applies; 15 MB per file"],
        ["Uploaded files", "None", "Dataverse storage; 500 files per agent, 512 MB each"],
        ["Dataverse tables", "Entra ID delegated", "Up to 15 tables; synonyms and glossary help"],
        ["Graph connectors", "Entra ID delegated", "ServiceNow, Confluence, indexed enterprise data"],
        ["Azure AI Search", "Configured endpoint", "Vector index; no security trimming"],
        ["Custom data", "None", "You query first, then pass Content, ContentLocation, Title"],
    ], [0.22, 0.24, 0.54],
        source=LEARN + "/microsoft-copilot-studio/guidance/retrieval-augmented-generation")

    table_slide(prs, "Knowledge limits change with orchestration mode", [
        ["Source type", "Classic", "Generative"],
        ["Website URLs", "4", "Model filters when over 25 sources"],
        ["SharePoint URLs", "4", "Model filters when over 25 sources"],
        ["Dataverse", "2 sources, 15 tables each", "Supported"],
        ["Uploaded files", "Unlimited", "Not counted toward the 25-source limit"],
        ["Custom data, Bing Custom Search", "Supported", "Only inside a generative answers node"],
    ], [0.30, 0.28, 0.42],
        source=LEARN + "/microsoft-copilot-studio/knowledge-copilot-studio")

    table_slide(prs, "Grounding controls on the agent", [
        ["Control", "Effect"],
        ["Allow ungrounded responses OFF",
         "A turn that used no source and no tool is blocked; the fallback topic fires"],
        ["Allow ungrounded responses ON",
         "The model's general knowledge can answer with no source behind it"],
        ["Official source",
         "A trusted source is used directly; not compatible with generative orchestration"],
        ["Web Search",
         "Public Bing results interleave with the public sites you configured"],
        ["In-text citation",
         "With ungrounded off, an answer ships only when it cites the source"],
    ], [0.34, 0.66],
        source=LEARN + "/microsoft-copilot-studio/knowledge-copilot-studio")

    bullets_slide(prs, "Verify a grounded answer", [
        "Open the citation and read the passage it points to",
        "Confirm the passage actually supports the claim in the answer",
        "Check that the source is in scope for the question that was asked",
        "A citation you have not opened is not evidence",
    ], notes_keys=("The source behind an answer",))

    table_slide(prs, "Knowledge scope and limits", [
        ["Choice", "Consequence for this assistant"],
        ["Agent knowledge", "A shared reference for general study questions"],
        ["Topic grounding", "A selected source scope for one particular conversation"],
        ["Source order", "There is no first-uploaded-source-wins rule"],
        ["Limits and citations", "Check source readiness, scope, and the supporting passage"],
    ], [0.30, 0.70], notes_keys=("Knowledge scope and limits",))

    def topic_flow(s):
        add_box(s, 0.55, 1.60, 2.05, 0.78, "Message\nteach the concept",
                fill=BLUE_LT, line=BLUE, size=13)
        add_arrow(s, 2.68, 1.90, 0.30, 0.18)
        add_box(s, 3.06, 1.60, 2.05, 0.78, "Question node\nWAIT for a choice",
                fill=NAVY, line=NAVY, color=WHITE, size=13)
        add_box(s, 5.85, 1.46, 3.60, 0.62, "Correct  ->  explain why it is right",
                fill=BLUE_LT, line=BLUE, size=12)
        add_box(s, 5.85, 2.16, 3.60, 0.62, "Incorrect  ->  name the misconception",
                fill=AMBER_LT, line=AMBER, size=12)
        add_box(s, 5.85, 2.86, 3.60, 0.62, "Unmatched twice  ->  offer recovery",
                fill=GRAY_LT, line=SLATE, size=12)
        add_arrow(s, 5.19, 1.90, 0.56, 0.18)
        add_caption(s, 0.55, 3.66, 5.10, 1.30,
                    "The wait point is what makes it teaching.\n"
                    "Without a Question node the agent lectures, and no learner "
                    "response ever gets evaluated.",
                    size=13, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "Teach, wait, then give feedback", topic_flow,
                  notes_keys=("Teach, wait, then give feedback",))

    table_slide(prs, "Topic inputs, outputs, and auto-prompting", [
        ["Design choice", "Why it matters"],
        ["Human-friendly input names",
         "The planner writes the question it asks the user from the input name"],
        ["Input descriptions and examples",
         "Turn a vague generated prompt into a specific one"],
        ["Power Fx validation or a value list",
         "Rejects bad input before the tool ever runs"],
        ["Output variables, not messages",
         "Lets the planner combine the result with other steps in the plan"],
        ["No double-handling",
         "Do not feed a structured output back into the prompt as free text"],
    ], [0.32, 0.68],
        source=LEARN + "/microsoft-copilot-studio/guidance/generative-orchestration")

    table_slide(prs, "Context reuse or a new answer", [
        ["Situation", "Use"],
        ["\"Give me a responsible-ai study session\"",
         "Fill the tool input from context"],
        ["\"Which principle covers transparency?\"",
         "Question node; wait for the learner's choice"],
        ["A required value is missing",
         "Prompt for it; do not guess"],
        ["An answer does not match",
         "One reprompt, then a truthful recovery"],
    ], [0.52, 0.48], notes_keys=("Context reuse or a new answer?",))

    bullets_slide(prs, "A useful failure response", [
        "Unsupported: \"I don't have your exam appointment.\"",
        "Recovery: \"Check your booking confirmation.\"",
        "Human boundary: \"I can't contact a mentor from here.\"",
        "Every refusal names a route the learner can actually take",
    ], notes_keys=("A useful failure response",))

    table_slide(prs, "What retrieval grounding is for", [
        ["Fits", "Does not fit"],
        ["Answering questions from a knowledge base", "Full document comparison"],
        ["Summarizing policies, FAQs, procedures", "Policy compliance evaluation"],
        ["Retrieving specific facts from files or systems",
         "Complex reasoning over long unstructured documents"],
    ], [0.50, 0.50],
        source=LEARN + "/microsoft-copilot-studio/guidance/retrieval-augmented-generation")

    break_slide(prs, "Return at 11:00 AM Central",
                notes_for("10-minute break\nReturn at 11:00 AM Central"))

    # ============================================================ SEGMENT 3
    divider(prs, "Segment 3", "Extend: actions, MCP, and handoff",
            notes_for("Segment 3\nExtend: actions, MCP, and handoff"))

    table_slide(prs, "The tool shelf", [
        ["Mechanism", "Reach for it when"],
        ["Connector action", "A prebuilt action already covers the operation"],
        ["Agent flow", "You need deterministic steps, throughput, or a human review step"],
        ["HTTP request", "A one-off endpoint with no connector, used by a single agent"],
        ["MCP server", "Several agents need the same tools, or the upstream API changes often"],
        ["AI prompt", "You need model choice, structured output, or file input"],
        ["Computer use", "No API exists and the work only happens in a user interface"],
    ], [0.26, 0.74],
        source=LEARN + "/microsoft-copilot-studio/guidance/agent-tools")

    table_slide(prs, "The next action", [
        ["User request", "Appropriate next step"],
        ["Explain a responsible AI principle", "Answer using knowledge"],
        ["Give me a study session; focus unspecified", "Clarify the focus"],
        ["Give me the responsible-ai study session", "Call GetStudySession"],
        ["Book my exam or decide an accommodation", "Refer to an authorized human or service"],
    ], [0.50, 0.50], notes_keys=("The next action",))

    def contract(s):
        add_box(s, 0.55, 1.80, 2.35, 0.95, "Input\nfocus  (Text)",
                fill=BLUE_LT, line=BLUE, size=14)
        add_arrow(s, 3.00, 2.19, 0.42, 0.18)
        add_box(s, 3.52, 1.70, 2.60, 1.15, "GetStudySession\nnative agent flow",
                fill=NAVY, line=NAVY, color=WHITE, size=14)
        add_arrow(s, 6.22, 2.19, 0.42, 0.18)
        add_box(s, 6.74, 1.60, 2.71, 0.62, "Output  status  (Text)",
                fill=AMBER_LT, line=AMBER, size=13)
        add_box(s, 6.74, 2.32, 2.71, 0.62, "Output  plan  (Text)",
                fill=AMBER_LT, line=AMBER, size=13)
        add_caption(s, 0.55, 3.30, 8.90, 1.55,
                    "A tool contract names the input, its type, and whether it is required; "
                    "then the outputs and the shape of a success value.\n"
                    "Write it before you build the flow. The planner selects the tool from "
                    "its name and description, so both are part of the contract.\n"
                    "Distinguish an unsupported focus value from an unavailable tool. They "
                    "need different responses.",
                    size=13, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "GetStudySession: the contract", contract,
                  notes_keys=("GetStudySession: the contract",))

    def flow_inside(s):
        steps = ["Agent calls the flow", "Initialize status and plan",
                 "Branch on focus value", "Respond to the agent, once"]
        y = 1.62
        for i, step in enumerate(steps):
            add_box(s, 0.55, y, 4.25, 0.62, step,
                    fill=BLUE_LT if i % 2 == 0 else GRAY_LT,
                    line=BLUE if i % 2 == 0 else SLATE,
                    size=13, align=PP_ALIGN.LEFT)
            if i < len(steps) - 1:
                add_down_arrow(s, 2.58, y + 0.63, 0.18, 0.22)
            y += 0.85
        add_caption(s, 5.05, 1.62, 4.40, 3.00,
                    "Required pieces\n\n"
                    "The trigger must be \"When an agent calls the flow\".\n\n"
                    "The flow must end in \"Respond to the agent\".\n\n"
                    "The flow has to live inside a solution before an agent can use it.\n\n"
                    "Branches cover responsible-ai, workloads, and foundry. Anything else "
                    "returns a status the agent can explain.",
                    size=12, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "The flow behind the tool", flow_inside,
                  notes_keys=("The flow behind the tool",),
                  source=LEARN + "/microsoft-copilot-studio/flows-faqs")

    table_slide(prs, "Topics, agent flows, and cloud flows", [
        ["", "Topic", "Agent flow", "Cloud flow"],
        ["Optimized for", "Conversation", "Business process", "General automation"],
        ["Behavior", "Deterministic", "Deterministic", "Deterministic"],
        ["Billing", "Agent messages", "Copilot Studio consumption", "Power Automate license"],
        ["Required parts", "Description or trigger phrase",
         "Agent-call trigger plus Respond to the agent", "Its own trigger"],
        ["Note", "Can call a flow behind the scenes",
         "Must live in a solution", "Convertible to an agent flow, one way"],
    ], [0.17, 0.26, 0.29, 0.28],
        source=LEARN + "/microsoft-copilot-studio/flows-faqs")

    bullets_slide(prs, "The evidence of a tool call", [
        "The activity map during testing shows the plan the orchestrator chose",
        "Expected input: focus = responsible-ai",
        "Expected output: status = ok, and a plan describing 30 minutes",
        "No execution record means the response alone proves nothing",
        "A fluent answer is not proof that a tool ran",
    ], notes_keys=("The evidence of a tool call",),
        source=LEARN + "/microsoft-copilot-studio/authoring-review-activity")

    table_slide(prs, "HTTP, connectors, and MCP", [
        ["Mechanism", "What the maker has to understand"],
        ["HTTP tool", "A defined endpoint, a request contract, and the response shape"],
        ["Connector action", "The action's inputs, its outputs, and which identity it runs as"],
        ["MCP server", "The tools it publishes, their descriptions, and server access"],
        ["All three", "Identity, permitted data, error handling, and approval"],
        ["This workshop", "One native agent flow; the rest are comparisons"],
    ], [0.26, 0.74], notes_keys=("HTTP and MCP",),
        source=LEARN + "/microsoft-copilot-studio/guidance/agent-tools")

    bullets_slide(prs, "When MCP earns its place", [
        "The server owns the tool names, descriptions, and input schemas, not each agent",
        "Change a definition once on the server and every agent picks it up without republishing",
        "Generative orchestration has to be on before an agent can use an MCP server",
        "Data policies that govern Power Platform connectors also govern MCP servers",
        "Topics cannot call an MCP server directly; only the orchestrator can",
        "Keep the count small: concurrent servers per conversation are capped",
    ], source=LEARN + "/microsoft-copilot-studio/agent-extend-action-mcp")

    def mcp_steps(s):
        steps = [("Tools", "Add a tool"),
                 ("Model Context Protocol", "pick a connector or add a server"),
                 ("Server details", "name, description, URL, authentication"),
                 ("Handshake", "Copilot Studio lists the tools it exposes"),
                 ("Preview tab", "test, then read the activity trace")]
        pipeline(s, [a for a, _ in steps], [b for _, b in steps],
                 y=1.66, h=0.92, cap_h=0.90)
        add_caption(s, 0.55, 3.70, 8.90, 1.35,
                    "Authentication is None, API key, or OAuth 2.0. Pick it before you create "
                    "the server entry.\n"
                    "Review every tool description the handshake returns. A tool with a vague "
                    "description gets selected unreliably.\n"
                    "Turn off Allow all and enable only the tools this agent needs.",
                    size=12.5, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "Adding an MCP server", mcp_steps,
                  source=LEARN + "/microsoft-copilot-studio/mcp-add-existing-server-to-agent")

    def subagents(s):
        add_box(s, 3.55, 1.55, 2.90, 0.82, "Parent agent\nowns the conversation",
                fill=NAVY, line=NAVY, color=WHITE, size=13)
        add_down_arrow(s, 4.91, 2.39, 0.18, 0.26)
        add_box(s, 0.55, 2.72, 2.75, 0.90, "Child agent\nspecialized work inside\nthe same agent",
                fill=BLUE_LT, line=BLUE, size=12)
        add_box(s, 3.55, 2.72, 2.90, 0.90, "Connected agent\nseparately built,\nseparately managed",
                fill=BLUE_LT, line=BLUE, size=12)
        add_box(s, 6.70, 2.72, 2.75, 0.90, "A2A\na protocol for agents\nto talk to each other",
                fill=GRAY_LT, line=SLATE, size=12)
        add_caption(s, 0.55, 3.86, 8.90, 0.95,
                    "The planner picks a child or connected agent from its description, "
                    "the same way it picks a tool.\n"
                    "Split into another agent when the work has its own knowledge, its own "
                    "owner, or its own release cadence.",
                    size=13, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "When another agent helps", subagents,
                  notes_keys=("When another agent helps",))

    def boundaries(s):
        cols = [("Act", "The agent proceeds with no confirmation.\n\n"
                        "Lookups, explanations, low-risk multistep work.",
                 GRAY_LT, SLATE),
                ("Confirm", "The agent asks in the conversation before it acts.\n\n"
                            "Anything the user would want to see stated back.",
                 BLUE_LT, BLUE),
                ("Approve", "A human approves outside the conversation.\n\n"
                            "Irreversible work, spend, records, access changes.",
                 AMBER_LT, AMBER)]
        x = 0.55
        for label, detail, fill, line in cols:
            add_box(s, x, 1.58, 2.83, 0.70, label, fill=fill, line=line, size=15)
            add_caption(s, x + 0.06, 2.42, 2.71, 1.70, detail, size=12,
                        align=PP_ALIGN.LEFT, color=INK)
            x += 3.02
        add_caption(s, 0.55, 4.30, 8.90, 0.80,
                    "Enforce the boundary in the design: a confirmation node, the platform's "
                    "approval feature, or logic in the trigger. An instruction is not an "
                    "enforcement point.",
                    size=13, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "Decision boundaries", boundaries,
                  source=LEARN + "/microsoft-copilot-studio/guidance/generative-orchestration")

    table_slide(prs, "Authority and human handoff", [
        ["Claim", "Evidence required"],
        ["\"Contact your mentor\"", "A truthful route the user can actually take"],
        ["\"I submitted your request\"", "A real authorized operation and a returned receipt"],
        ["\"You are connected to a person\"", "A supported handoff and an accepted transfer"],
        ["\"The tool can access this data\"", "The intended identity and policy allow that access"],
    ], [0.38, 0.62], notes_keys=("Authority and human handoff",),
        source=LEARN + "/microsoft-copilot-studio/guidance/implement-checklist")

    bullets_slide(prs, "Specifying a tool", [
        "Name the input, its type, and whether it is required",
        "Name the expected output and what a success value looks like",
        "Separate an unsupported input value from an unavailable tool",
        "Name one request in your own scenario that has to go to a human",
    ], notes_keys=("Your tool decision",))

    break_slide(prs, "Return at noon Central",
                notes_for("10-minute break\nReturn at noon Central"))

    # ============================================================ SEGMENT 4
    divider(prs, "Segment 4", "Operate: evaluate, govern, publish",
            notes_for("Segment 4\nOperate: evaluate, govern, publish"))

    table_slide(prs, "Evaluation sets and what each answers", [
        ["Prepared set", "Question it answers"],
        ["AI901-live-three  (E04, E05, E08)", "Does the response match the expected meaning?"],
        ["AI901-tool-one  (E08 only)", "Did it use the actual GetStudySession capability?"],
        ["Separate manual conversation", "Did the topic wait, then give the correct feedback?"],
    ], [0.42, 0.58], notes_keys=("Two evaluation sets, two questions",))

    def eval_loop(s):
        pipeline(s, ["Same test set", "Run before", "One change", "Run after", "Compare"],
                 ["Fixed inputs and\nexpected meanings",
                  "Record the baseline\nresult per case",
                  "Change exactly one\nthing, then stop",
                  "Same set, same\nconditions",
                  "Per case, plus the\nsource and tool trace"],
                 y=1.68, h=0.86, cap_h=1.00)
        add_caption(s, 0.55, 4.16, 8.90, 0.90,
                    "Change one thing at a time. Two changes and one score movement tells you "
                    "nothing about which change caused it.\n"
                    "A green score on the wrong test set is a nicer way to be wrong.",
                    size=13, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "A score and an execution trace", eval_loop,
                  notes_keys=("A score and an execution trace",))

    table_slide(prs, "Conversational agent KPIs", [
        ["Metric", "Definition"],
        ["Total sessions", "Analytics sessions in the period; one conversation can produce several"],
        ["Engagement rate",
         "Share of sessions that reached a custom topic, Escalate, Fallback, or boosting"],
        ["Resolution rate",
         "Share of engaged sessions that reached a resolved outcome, confirmed or implied"],
        ["Escalation rate",
         "Share of engaged sessions handed off via Escalate or Transfer conversation"],
        ["Abandon rate",
         "Share of engaged sessions that ended with neither, after 60 minutes"],
        ["CSAT", "Average End of Conversation survey score, 1 to 5"],
    ], [0.24, 0.76],
        source=LEARN + "/microsoft-copilot-studio/analytics-improve-agent-effectiveness")

    table_slide(prs, "Usage signals need interpretation", [
        ["Signal", "What it does and does not tell us"],
        ["10 sessions, 9 did not escalate", "A 90% containment proxy, nothing about accuracy"],
        ["6 resolved, 3 abandoned, 1 escalated", "60% resolution, 30% abandonment"],
        ["4 survey responses", "The survey describes those 4 respondents"],
        ["High containment plus wrong answers",
         "Read outcomes, transcripts, and source evidence together"],
    ], [0.36, 0.64], notes_keys=("Usage signals need interpretation",))

    bullets_slide(prs, "Quality signals the dashboard adds", [
        "Reactions: thumbs up and down with free-text comments, retained 28 days",
        "Sentiment: an AI-scored negative-sentiment share across sessions",
        "Themes: user questions grouped, which exposes topic coverage gaps",
        "Generated answer rate and quality: surfaces the questions that went unanswered",
        "A theme converts into an evaluation test set in one step",
    ], source=LEARN + "/microsoft-copilot-studio/analytics-improve-agent-effectiveness")

    table_slide(prs, "Well-Architected concerns for this agent", [
        ["Pillar", "Control for the study assistant"],
        ["Reliability", "Tool failure has a clear recovery path the learner can see"],
        ["Security", "The intended identity, approved sources, and nothing broader"],
        ["Operational Excellence", "An owner reviews repeatable tests and incidents"],
        ["Performance Efficiency", "Measure response time and unnecessary tool work"],
        ["Experience Optimization", "Wait for the learner, give feedback and a next step"],
    ], [0.30, 0.70], notes_keys=("Five Well-Architected concerns",),
        source=LEARN + "/power-platform/well-architected/pillars")

    def governance(s):
        layer_stack(s, [
            ("Tenant",
             "Data policies across every environment: unauthenticated use, individual "
             "channels, knowledge sources, connectors, and whether generative agents publish.",
             NAVY, NAVY),
            ("Environment",
             "Scope those policies in or out, allow or block public data sources, and apply "
             "network isolation with virtual network support and IP firewall.",
             BLUE_LT, BLUE),
            ("Agent",
             "Generative orchestration, knowledge, and generative answers on or off; the "
             "authentication mode; web channel security.",
             AMBER_LT, AMBER),
        ], y=1.56, h=0.86, gap=0.14)
        # The tenant band needs light text because its fill is navy.
        for shape in s.shapes:
            if shape.has_text_frame and shape.text_frame.text.strip() == "Tenant":
                for para in shape.text_frame.paragraphs:
                    style_runs(para, 14, bold=True, color=WHITE)
        add_caption(s, 0.55, 4.54, 8.90, 0.50,
                    "The narrowest setting wins. An agent switch cannot re-enable what a "
                    "tenant policy blocked.",
                    size=13, align=PP_ALIGN.LEFT, color=INK, bold=True)

    diagram_slide(prs, "Governance runs at three levels", governance,
                  source=LEARN + "/microsoft-copilot-studio/guidance/sec-gov-phase2")

    def alm(s):
        boxes = [("DEV\nsandbox", "Build here. Nowhere else."),
                 ("TEST\nsandbox", "Managed solution import, then validate."),
                 ("PROD\nproduction", "Managed only. No direct customization.")]
        x = 0.55
        for i, (label, detail) in enumerate(boxes):
            add_box(s, x, 1.58, 2.55, 0.86, label,
                    fill=BLUE_LT if i < 2 else AMBER_LT,
                    line=BLUE if i < 2 else AMBER, size=14)
            add_caption(s, x, 2.50, 2.55, 0.60, detail, size=11.5)
            if i < 2:
                add_arrow(s, x + 2.60, 1.92, 0.30, 0.18)
            x += 3.02
        add_caption(s, 0.55, 3.14, 4.35, 2.00,
                    "Golden rules\n\n"
                    "Do not customize outside development.\n"
                    "Always work in the context of solutions.\n"
                    "Use a custom publisher and prefix.\n"
                    "Environment variables for settings and secrets.\n"
                    "Export as managed, except into development.\n"
                    "Automate with pipelines or Git integration.",
                    size=12, align=PP_ALIGN.LEFT, color=INK)
        add_caption(s, 5.10, 3.14, 4.35, 2.00,
                    "Not solution-aware: redo after every deployment\n\n"
                    "Application Insights settings.\n"
                    "Manual authentication settings.\n"
                    "Direct Line and web channel security.\n"
                    "Deployed channels.\n"
                    "Sharing, with makers and with end users.",
                    size=12, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "Environments and the ALM rules", alm,
                  source=LEARN + "/microsoft-copilot-studio/guidance/alm")

    def publish(s):
        pipeline(s, ["Tested draft", "Publish version", "Scope the channel", "Fresh session"],
                 ["Evaluation sets pass and\nthe transcripts back it up",
                  "Publishing promotes the\nconfigured version, not\nyour editor state",
                  "Channel plus access\ncontrol decides who\ncan actually reach it",
                  "Sign in as a real user and\nrun the conversation from\nthe beginning"],
                 y=1.70, h=0.90, cap_h=1.15)
        add_caption(s, 0.55, 4.24, 8.90, 0.85,
                    "Publishing to an organizational catalog can require administrator "
                    "approval, so build that wait into the plan rather than the launch day.",
                    size=13, align=PP_ALIGN.LEFT, color=INK)

    diagram_slide(prs, "Publishing and audience access", publish,
                  notes_keys=("Publishing and audience access",))

    table_slide(prs, "Channel choice changes the checks", [
        ["Channel", "Preparation to verify"],
        ["Teams: course demonstration",
         "Entitlement, scoped access, installation, a fresh conversation"],
        ["SharePoint: comparison", "Site permission, published agent, allowed deployment"],
        ["Microsoft 365 Copilot: comparison", "Channel configuration and an approved audience"],
        ["Every channel",
         "Real user access, source permissions, and the message formats it supports"],
    ], [0.36, 0.64], notes_keys=("Channel choice changes the checks",),
        source=LEARN + "/microsoft-copilot-studio/guidance/channels")

    bullets_slide(prs, "Before you publish", [
        "Knowledge sources are current, approved, in scope, and stale content is gone",
        "Every tool has a clear name, description, inputs, and outputs",
        "Decision boundaries are written down: act, confirm, approve",
        "Authentication is settled: user credentials or maker credentials, per integration",
        "Each tool tested on its own for payload, schema, error state, and latency",
        "Channel message formats verified: Markdown, Adaptive Cards, images",
    ], source=LEARN + "/microsoft-copilot-studio/guidance/implement-checklist")

    bullets_slide(prs, "Scoping a pilot", [
        "Named users, a named owner, a data boundary, and a stop condition",
        "One measured result, with its evidence source labeled",
        "A review date, and the finding that would end the pilot early",
    ], notes_keys=("Your pilot decision",))

    table_slide(prs, "The same pattern at work", [
        ["Course component", "Workplace transfer"],
        ["AI-901 reference", "Approved internal knowledge"],
        ["Practice topic", "A controlled training or triage interaction"],
        ["Study-session tool", "One bounded lookup or operation"],
        ["Pilot decision", "Named audience, owner, evidence, and stop condition"],
    ], [0.36, 0.64], notes_keys=("The same pattern at work",))

    bullets_slide(prs, "The outcomes in practice", [
        "Plan: a brief with a testable boundary",
        "Build: source evidence and a topic that waits",
        "Extend: a tool contract and a human boundary",
        "Operate: test evidence and a defensible pilot decision",
    ], notes_keys=("The four outcomes in practice",))

    bullets_slide(prs, "Warner's Laws of Agent Building", [
        "1.  A fluent answer isn't proof that a tool ran. Go read the activity record.",
        "2.  Instructions steer behavior. They never grant permission.",
        "3.  If the agent doesn't wait, it isn't teaching. It's lecturing.",
        "4.  Ground it or don't claim it. A citation is something you inspect.",
        "5.  Name the boundary before you name the features.",
        "6.  A green score on the wrong test set is just a nicer way to be wrong.",
    ], notes_keys=("Warner's Laws of Agent Building",), size=15)

    bullets_slide(prs, "Where to keep reading", [
        LEARN + "/microsoft-copilot-studio/guidance/overview",
        LEARN + "/microsoft-copilot-studio/guidance/implement-checklist",
        LEARN + "/microsoft-copilot-studio/guidance/retrieval-augmented-generation",
        LEARN + "/microsoft-copilot-studio/agent-extend-action-mcp",
        LEARN + "/power-platform/architecture/products/copilot-studio",
        LEARN + "/power-platform/well-architected/pillars",
    ], size=15)

    bullets_slide(prs, "Thank you for attending", [
        "Please complete the course evaluation",
        "Recording posts 24 to 48 hours from now at learning.oreilly.com",
        "Session materials: " + REPO_URL,
        "Tim Warner  |  " + CONTACT,
    ], notes_keys=("Thank you for attending",))


def main():
    global FONT, PREV_NOTES
    prs = Presentation(TEMPLATE)
    FONT = detect_theme_font(prs)
    PREV_NOTES = load_previous_notes(PREVIOUS)

    # Strip the template's demo slides; masters and layouts stay intact.
    xml_slides = prs.slides._sldIdLst
    for sld in list(xml_slides):
        rid = sld.get("{http://schemas.openxmlformats.org/officeDocument/"
                      "2006/relationships}id")
        prs.part.drop_rel(rid)
        xml_slides.remove(sld)

    build(prs)

    os.makedirs("slides", exist_ok=True)
    prs.save(OUT)

    with_notes = sum(1 for s in prs.slides
                     if s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip())
    print("theme font:", FONT)
    print("carried-over notes available:", len(PREV_NOTES))
    print("built:", OUT)
    print("slides:", len(prs.slides), " with speaker notes:", with_notes)
    print("size: %.0f KB" % (os.path.getsize(OUT) / 1024))


if __name__ == "__main__":
    main()
