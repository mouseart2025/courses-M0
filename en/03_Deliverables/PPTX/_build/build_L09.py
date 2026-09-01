"""
Build L09 EN PPTX: Call In Reinforcements
20 slides, Chaihuo brand rebuild from M0_EN_PPTPlan_CFG-5_Lesson09_v1.md
"""
from pptx.util import Inches, Pt
import os
import sys
from builder_lib import (
    new_deck, add_bg, add_rect, add_oval, add_text, add_multiline,
    add_title_bar, add_subtitle, add_footer, add_card, add_grey_box,
    add_red_rule_box, add_yellow_dot_item, YELLOW, WHITE, INK, RED, CODEBG,
    PP_ALIGN, MSO_ANCHOR, set_notes
)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

DECK_LABEL = "Call In Reinforcements"
TOTAL = 20
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson09_CallInReinforcements_v1.pptx")

COVER_ART = "/Users/leonfeng/Baiduyun/M0/M0-V2/assets/L9_封面插画_请外援.png"
MATERIALS_WALL = "/Users/leonfeng/Baiduyun/M0/M0-V2/assets/L9_插图_就地取材材料墙.png"


# ------------------------------------------------------------------ page setup
def page(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(s)
    add_footer(s, n, TOTAL, DECK_LABEL)
    return s


def num_block(s, x, y, num, size=0.34):
    add_rect(s, x, y, size, size, fill=YELLOW, border=None)
    add_text(s, x, y + 0.03, size, 0.32, num, size=15, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER)


def yellow_box(s, x, y, w, h, lines, size=13, line_spacing=1.25):
    add_rect(s, x, y, w, h, fill=YELLOW, border=None)
    if isinstance(lines, str):
        lines = [lines]
    add_multiline(s, x + 0.18, y + 0.12, w - 0.36, h - 0.24, lines, size=size,
                  line_spacing=line_spacing)


def grey_box(s, x, y, w, h, lines, size=10.5, line_spacing=1.35):
    add_card(s, x, y, w, h, fill=CODEBG, border=INK, border_w=1.0)
    items = [(t, {"mono": True}) if isinstance(t, str) else t for t in lines]
    add_multiline(s, x + 0.16, y + 0.10, w - 0.32, h - 0.20, items, size=size,
                  line_spacing=line_spacing)


def check_item(s, x, y, w, text, size=12, h=0.30):
    add_rect(s, x, y + 0.04, 0.20, 0.20, fill=YELLOW, border=None)
    add_text(s, x + 0.34, y, w - 0.34, h, text, size=size)


def red_line(s, x, y, w, h, title, body=None, body_size=13):
    """Single red-line warning box."""
    add_rect(s, x, y, 0.07, h, fill=RED, border=None)
    add_oval(s, x + 0.18, y + 0.12, 0.11, fill=RED, border=None)
    add_text(s, x + 0.40, y + 0.06, w - 0.55, 0.35, title, size=19, bold=True)
    if body:
        add_text(s, x + 0.40, y + 0.42, w - 0.55, h - 0.50, body, size=body_size)


def add_photo_or_placeholder(s, path, x, y, w, h, label="photo"):
    if path and os.path.exists(path):
        s.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h))
    else:
        add_card(s, x, y, w, h, fill=WHITE, border=INK, border_w=1.5)
        add_text(s, x, y + h / 2 - 0.25, w, 0.50,
                 f"[ {label} — to be captured at rehearsal ]", size=11,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


# ------------------------------------------------------------------ slides
def slide_01(prs):
    s = page(prs, 1)
    add_text(s, 0.62, 1.20, 6.4, 0.3,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0)",
             size=13)
    add_text(s, 0.62, 1.55, 8.76, 0.75, "Call In Reinforcements", size=38,
             bold=True)
    add_rect(s, 0.62, 2.50, 1.6, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 2.68, 6.4, 0.6,
             "Give Your MVP a New Power · The Marathon's Second Leg · Chaihuo "
             "Maker Academy · M0 Lesson 9", size=14, line_spacing=1.2)
    add_multiline(s, 0.62, 3.60, 5.8, 0.95, [
        ("Today: the hardware store — a library, a decision, a wiring-in —",
         {"size": 12.5}),
        ("and a first look for your project.", {"size": 12.5}),
    ], line_spacing=1.35)
    add_photo_or_placeholder(s, COVER_ART, 6.80, 3.05, 2.45, 2.45,
                             label="toolbox illustration")
    set_notes(s, "Cover page only; students see it as they sit down. No "
                 "script. When the session starts, go straight to slide 02 — "
                 "the opener's 30-second recap is spoken, not projected. Right "
                 "side: the toolbox cover illustration reused from the CN deck "
                 "because it carries no Chinese glyphs. Footer: Chaihuo Maker "
                 "Academy · M0 · Call In Reinforcements | 01 / 20.")
    return s


def slide_02(prs):
    s = page(prs, 2)
    add_title_bar(s, "Today, Your MVP Grows a New Power")
    add_rect(s, 0.62, 1.10, 0.07, 0.95, fill=YELLOW, border=None)
    add_text(s, 0.88, 1.12, 8.40, 0.90,
             "Last session: you ran the first lap — your project has an MVP. "
             "It can be demonstrated, two judges picked at it, and you made "
             "Accept-or-Reject calls. Is your baton handoff sheet on the desk? "
             "We read it at the opening of the build.", size=11.5)
    add_text(s, 0.62, 2.15, 8.76, 1.10,
             "TODAY, YOUR MVP GROWS A NEW POWER.", size=28, bold=True)
    add_multiline(s, 0.62, 3.30, 8.76, 1.00, [
        ("FIRST HALF: THE HARDWARE STORE — call in reinforcements.",
         {"size": 13, "bold": True}),
        ("A library: someone else's well-tested, free toolbox.",
         {"size": 11.5}),
        ("SECOND HALF: FINISH THE CORE FUNCTION — the leg-two sprint.",
         {"size": 13, "bold": True}),
    ], line_spacing=1.30)
    yellow_box(s, 0.62, 4.40, 8.76, 0.80, [
        "Same rhythm as leg one — STAND-UP | BUILD | AI REVIEW | DECIDE | HANDOFF."],
        size=12)
    set_notes(s, "30-second recap: last session you ran the first lap — your "
                 "project has an MVP. It can be demonstrated, two judges "
                 "picked at it, and you made Accept-or-Reject calls. Did you "
                 "bring your baton handoff sheet? Put it on the desk — we "
                 "read it at the opening of the build. Today, two things: "
                 "first half, the hardware store — call in reinforcements; "
                 "second half, the leg-two sprint — finish the core function. "
                 "The rhythm is exactly the same as leg one.")
    return s


def slide_03(prs):
    s = page(prs, 3)
    add_title_bar(s, "Readable Isn't the Same as Worth Writing")
    # left card: no reinforcements
    add_card(s, 0.62, 1.45, 4.20, 2.80, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.86, 1.62, 3.72, 0.30, "NO REINFORCEMENTS", size=13,
             bold=True)
    add_text(s, 0.86, 2.05, 3.72, 0.70,
             "Ask AI to write the driver from scratch — over a hundred lines. "
             "Three screens of scrolling.", size=11.5)
    # grey scroll shading
    for i, gy in enumerate([2.95, 3.25, 3.55]):
        add_rect(s, 0.86, gy, 3.30, 0.22, fill=CODEBG, border=INK, border_w=1.0)
    # right card: with a library
    add_card(s, 5.18, 1.45, 4.20, 2.80, fill=YELLOW, border=INK, border_w=1.5)
    add_text(s, 5.42, 1.62, 3.72, 0.30, "WITH A LIBRARY", size=13, bold=True)
    add_text(s, 5.42, 2.20, 3.72, 0.90, "Three lines.", size=28, bold=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # bottom line
    add_text(s, 0.62, 4.55, 8.76, 0.50,
             "That hundred-line thing was already written, tested, and given "
             "away free — that's OPEN SOURCE. This toolbox is called A LIBRARY.",
             size=12.5, align=PP_ALIGN.CENTER)
    set_notes(s, "Look at this complex sensor. No help from anyone — ask AI "
                 "to write the driver from scratch — over a hundred lines. "
                 "Three screens of scrolling. Can you read it? By now, yes, "
                 "you can read it — but being able to read it doesn't mean "
                 "you should write it. Now: three lines. That hundred-line "
                 "thing was already written, tested, and given away free — "
                 "that's open source: engineers all over the world send each "
                 "other toolboxes. This toolbox is called a library. Today "
                 "you learn to shop the hardware store: whatever your project "
                 "needs, someone on earth has probably already built the wheel.")
    return s


def slide_04(prs):
    s = page(prs, 4)
    add_title_bar(s, "The Three Checks Before Calling in a Library")
    grey_box(s, 0.62, 1.42, 8.76, 2.90, [
        "Three checks before calling in a library (2 of 3 pass — bring it in):",
        "",
        "1) When was it last updated? (Nothing in three years — think twice.)",
        "2) Does it have examples? (No examples = no manual.)",
        "3) Is it documented completely?",
        "",
        "(Fourth check, for when something breaks: is my board on the",
        "supported-hardware list?)",
    ], size=11.5, line_spacing=1.35)
    add_text(s, 0.62, 4.55, 8.76, 0.40,
             "This page stays up today — install, pick, wire in: come back to it.",
             size=11.5, align=PP_ALIGN.CENTER)
    set_notes(s, "Step one, search — find it in the hardware store. Step two, "
                 "read the page and judge it: the three checks. 1) When was it "
                 "last updated? Nothing in three years — think twice. 2) Does "
                 "it have examples? No examples = no manual. 3) Is it "
                 "documented completely? Two of three pass — bring it in. This "
                 "page stays up today — install, pick, wire in: anytime you see "
                 "'should I install this library?', run the three checks first. "
                 "Write them into your student document.")
    return s


def slide_05(prs):
    s = page(prs, 5)
    add_title_bar(s, "One Library for the Whole Class")
    steps = [
        "SEARCH — find it in the hardware store",
        "CHECK — the three checks (back to slide 04)",
        "INSTALL — it moves into YOUR project's tool room",
        "RUN — run its built-in example",
    ]
    sy = 1.62
    for i, st in enumerate(steps):
        num_block(s, 0.74, sy, str(i + 1), size=0.34)
        add_text(s, 1.20, sy + 0.04, 7.80, 0.36, st, size=13.5, bold=True)
        sy += 0.62
    yellow_box(s, 0.62, 4.28, 8.76, 0.85, [
        "...stop. How many seconds did that compile take?",
        "The reinforcement you called in is already compiled — that's the second reason to call in help."],
        size=12.5, line_spacing=1.35)
    set_notes(s, "Let's call in the same reinforcement together and walk the "
                 "whole process once. Step one, search. Step two, check — the "
                 "three checks, back to that page. Step three, install — "
                 "that's taking the toolbox into your project's tool room. "
                 "Step four, run its built-in example. Stop. How many seconds "
                 "did that compile take? Right — the reinforcement you called "
                 "in is already compiled. That's the second reason to call in "
                 "help.")
    return s


def slide_06(prs):
    s = page(prs, 6)
    add_title_bar(s, "Every Project Has Its Own Tool Room")
    # two room cards + wall
    add_card(s, 0.62, 1.55, 4.05, 1.80, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.86, 1.70, 3.57, 0.30, "THE TOMATO CLOCK PROJECT", size=12,
             bold=True)
    add_text(s, 0.86, 2.15, 3.57, 0.80,
             "the library it called in lives here", size=11.5)
    add_rect(s, 4.77, 1.55, 0.18, 1.80, fill=INK, border=None)
    add_card(s, 5.03, 1.55, 4.05, 1.80, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.27, 1.70, 3.57, 0.30, "MY PROJECT", size=12, bold=True)
    add_text(s, 5.27, 2.15, 3.57, 0.80,
             "the library it called in lives here", size=11.5)
    add_text(s, 0.62, 4.10, 8.76, 0.75,
             "One room on fire doesn't burn the next one — each in its own room, they don't fight.",
             size=13.5, bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "See this — this project's tool room, and that project's tool "
                 "room: two separate rooms. Why design it this way? One "
                 "sentence: one room on fire doesn't burn the next one. The "
                 "library your tomato clock called in and the library your "
                 "project called in each live in their own room — they don't "
                 "fight. Write the three checks into your student document — "
                 "anywhere you ever see 'should I install this library?', run "
                 "the three checks first.")
    return s


def slide_07(prs):
    s = page(prs, 7)
    add_title_bar(s, "Importing Is a Trade-off Decision — Not a Default Move")
    # case one
    add_card(s, 0.62, 1.45, 8.76, 0.78, fill=YELLOW, border=INK, border_w=1.5)
    add_text(s, 0.86, 1.55, 8.28, 0.28, "A COMPLEX SENSOR", size=12,
             bold=True)
    add_text(s, 0.86, 1.88, 8.28, 0.30,
             "writing the driver yourself is a hundred lines — IMPORT IT",
             size=12.5)
    # case two
    add_card(s, 0.62, 2.35, 8.76, 0.78, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.86, 2.45, 8.28, 0.28, "A LIGHT THAT BLINKS THREE TIMES",
             size=12, bold=True)
    add_text(s, 0.86, 2.78, 8.28, 0.30,
             "three lines does it — DON'T go hunting for a \"blink library\"",
             size=12.5)
    # three questions
    add_multiline(s, 0.62, 3.35, 8.76, 0.55, [
        ("1) IS IT CORE?    2) CAN WE GET IT WORKING TODAY?    3) WHAT IF WE DON'T?",
         {"size": 14, "bold": True}),
    ], line_spacing=1.3)
    red_line(s, 0.62, 4.18, 8.76, 0.78,
             "PICK EXACTLY ONE",
             "three picks gets sent back.")
    set_notes(s, "The hardware store is fun to browse — but importing is a "
                 "trade-off decision, not a default move. Two real cases: case "
                 "one, your project drives a complex sensor; writing the "
                 "driver yourself is a hundred lines — import it. Case two, "
                 "you want a light to blink three times; three lines does it — "
                 "and you go hunting for a 'blink library' — don't. What's the "
                 "difference? Three questions: is it core? can we get it "
                 "working today? what happens if we don't import it? Now, "
                 "against your requirements sheet, let AI be your selection "
                 "advisor — it lists candidates; you pick exactly one, and "
                 "that's the one we install today. Three picks gets sent back — "
                 "greed is today's most common failure.")
    return s


def slide_08(prs):
    s = page(prs, 8)
    add_title_bar(s, "Let AI Be Your Selection Advisor")
    grey_box(s, 0.62, 1.42, 8.76, 2.35, [
        "This is my requirements sheet's core function: ______.",
        "The board I'm using: ______.",
        "Be my selection advisor: recommend 3 external libraries that might help,",
        "one line each — what it does and why it fits me — ranked by fit.",
        "Reminder: only recommend libraries that really exist and support my board.",
    ], size=11, line_spacing=1.35)
    yellow_box(s, 0.62, 3.95, 8.76, 0.82, [
        "It lists candidates — YOU pick exactly one.",
        "AI will confidently invent libraries; the hardware store only stocks real ones."],
        size=12, line_spacing=1.35)
    set_notes(s, "Against your requirements sheet, send this prompt in the "
                 "same chat window you've been using — don't open a new one. "
                 "It lists candidates; you pick exactly one, and that's the one "
                 "we install today. AI recommends a library you can't find? "
                 "It invents things — what's searchable in the hardware store "
                 "is what counts. If no library fits: writing 'why not import' "
                 "with your reason is a valid trade-off — it scores the same as "
                 "importing.")
    return s


def slide_09(prs):
    s = page(prs, 9)
    add_title_bar(s, "Example Code Is Not Your Feature")
    add_text(s, 0.62, 1.42, 8.76, 0.35,
             "THE EXAMPLE = \"here's what this library can do\"    "
             "YOUR FEATURE = \"my core function\"",
             size=12.5, bold=True, align=PP_ALIGN.CENTER)
    steps = [
        ("Ask AI: \"what is this code doing?\" — your translator, built for code "
         "that wasn't written for you", 1.95),
        ("Have AI reshape it to your need — one minimal change at a time", 2.55),
    ]
    for txt, sy in steps:
        num_block(s, 0.74, sy, str(1 if sy < 2.2 else 2), size=0.34)
        add_text(s, 1.20, sy + 0.04, 7.80, 0.46, txt, size=11.5)
    grey_box(s, 0.62, 3.15, 8.76, 1.25, [
        "Building on our last round: I installed the library ______; its example",
        "can ___ (one line).",
        "My core function is: ______.",
        "Reshape the example into my feature: change only the smallest piece first —",
        "let it run, then I'll ask for the next piece.",
    ], size=10.5, line_spacing=1.35)
    yellow_box(s, 0.62, 4.58, 8.76, 0.58, [
        "THE BAR: installed + example runs. If you don't finish the wiring, it moves into the build block — that's fine."],
        size=11.5)
    set_notes(s, "The last step is the hardest: example code is not your "
                 "feature. The example demonstrates what the library can do; "
                 "what you want is your core function. Two steps: one, ask AI "
                 "'what is this code doing?' — it's your translator, built for "
                 "code that wasn't written for you; two, have AI reshape it to "
                 "your need — one minimal change at a time. The bar: installed + "
                 "example runs. If you don't finish the wiring, it moves into "
                 "the build block this afternoon — that's fine.")
    return s


def slide_10(prs):
    s = page(prs, 10)
    add_title_bar(s, "One Line Each")
    add_card(s, 0.62, 1.55, 4.20, 2.40, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.86, 1.75, 3.72, 0.85,
             "WHAT I IMPORTED — AND WHAT IT SAVED ME", size=14, bold=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_card(s, 5.18, 1.55, 4.20, 2.40, fill=YELLOW, border=INK, border_w=1.5)
    add_text(s, 5.42, 1.75, 3.72, 0.85,
             "WHY I DIDN'T — SAME APPLAUSE", size=14, bold=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, 0.62, 4.30, 8.76, 0.45,
             "Big class: desk-pairs report to each other; the teacher calls a few to the whole room.",
             size=11.5, align=PP_ALIGN.CENTER)
    set_notes(s, "One line each: what I imported, and what it saved me. "
                 "No-import students report: why I didn't — and they get the "
                 "same applause. The code reinforcement is in the door. But "
                 "help isn't only one kind — your project is still wearing "
                 "nothing. Next twenty minutes: the second reinforcement — a "
                 "look.")
    return s


def slide_11(prs):
    s = page(prs, 11)
    add_title_bar(s, "Help Isn't Only Code — an MVP Has Two Faces")
    add_card(s, 0.62, 1.55, 4.20, 2.30, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.86, 1.72, 3.72, 0.35, "IT WORKS (the inside)", size=14,
             bold=True)
    add_text(s, 0.86, 2.25, 3.72, 1.05,
             "the function runs — loose parts and a nest of wires", size=12.5)
    add_card(s, 5.18, 1.55, 4.20, 2.30, fill=YELLOW, border=INK, border_w=1.5)
    add_text(s, 5.42, 1.72, 3.72, 0.55, "IT LOOKS LIKE SOMETHING (the outside)",
             size=14, bold=True)
    add_text(s, 5.42, 2.45, 3.72, 0.85,
             "you can tell what it is at a glance — and you'd dare to touch it",
             size=12.5)
    add_text(s, 0.62, 4.25, 8.76, 0.70,
             "On demo day, people see the outside first — then they get to the inside. "
             "Trash is the hardware store for looks.",
             size=13, bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "Help isn't only code. Look at your project — the function "
                 "runs, but it's still a table of loose parts and a nest of "
                 "wires. An MVP has two faces: it works (the inside), and it "
                 "looks like something (the outside). On demo day, people see "
                 "the outside first — then they get to the inside. The look "
                 "costs nothing and gets printed nothing — trash is the "
                 "hardware store for looks.")
    return s


def slide_12(prs):
    s = page(prs, 12)
    add_title_bar(s, "The Four Moves")
    moves = [
        ("GIVE IT A SHELL", "a cardboard box, a takeout box, an old toy shell; "
                             "it is what it is, so make it look like what it is"),
        ("HOLD IT STILL", "tape, rubber bands, zip ties; wires don't dangle, demos don't wobble"),
        ("LABEL IT", "marker the button names, tape an arrow; someone can touch it without reading a manual"),
        ("HIDE THE MESS", "tuck the wiring into the box; only the \"face\" shows"),
    ]
    positions = [(0.62, 1.50), (5.23, 1.50), (0.62, 3.15), (5.23, 3.15)]
    for i, ((x, y), (title, body)) in enumerate(zip(positions, moves)):
        add_card(s, x, y, 4.15, 1.45, fill=WHITE, border=INK, border_w=1.5)
        num_block(s, x + 0.14, y + 0.14, str(i + 1), size=0.32)
        add_text(s, x + 0.56, y + 0.12, 3.35, 0.30, title, size=11.5, bold=True)
        add_text(s, x + 0.56, y + 0.50, 3.35, 0.80, body, size=10.5)
    yellow_box(s, 0.62, 4.55, 8.76, 0.66, [
        "LOOKS SERVE THE DEMO — it exists for a 30-second demonstration. "
        "Looks take no more than a third of your build time; if you disappear into it, the teacher pulls you back.",
        "Scissors and knives live with the teacher — take them on demand, return when done."],
        size=10, line_spacing=1.30)
    set_notes(s, "Four moves: one, give it a shell — a cardboard box, a "
                 "takeout box, an old toy shell; it is what it is, so make it "
                 "look like what it is. Two, hold it still — tape, rubber "
                 "bands, zip ties; wires don't dangle, demos don't wobble. "
                 "Three, label it — marker the button names, tape an arrow; "
                 "someone can touch it without reading a manual. Four, hide "
                 "the mess — tuck the wiring into the box; only the 'face' "
                 "shows. One rule: looks serve the demo — it exists for a "
                 "30-second demonstration. Looks take no more than a third "
                 "of your build time; if you disappear into it, I'll pull you "
                 "back. Scissors and knives live with me — take them on "
                 "demand, return them when done.")
    return s


def slide_12b(prs):
    s = page(prs, 13)
    add_title_bar(s, "The Materials Wall — Pick, Don't Buy")
    add_photo_or_placeholder(s, MATERIALS_WALL, 1.20, 1.45, 7.60, 2.85,
                             label="materials wall")
    yellow_box(s, 0.62, 4.45, 8.76, 0.62, [
        "FIND MATERIAL | BUILD THE STRUCTURE | ADD THE LOOK | READY TO DEMO"],
        size=12.5)
    add_text(s, 0.62, 5.10, 8.76, 0.15,
             "Cardboard boxes · takeout boxes · bottle caps · old toy shells · "
             "tape · rubber bands · zip ties",
             size=9.5, align=PP_ALIGN.CENTER)
    set_notes(s, "The materials wall — everything here is clean junk brought "
                 "from home or picked from the public pool. Pick, don't buy. "
                 "Find material → build the structure → add the look → ready "
                 "to demo.")
    return s


def slide_13(prs):
    s = page(prs, 14)
    add_title_bar(s, "Leg-Two Stand-Up")
    add_card(s, 0.62, 1.50, 8.76, 0.80, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.86, 1.62, 8.28, 0.55,
             "READ YOUR BATON SHEET — what did last leg say is the first thing this leg?",
             size=13, bold=True)
    add_rect(s, 0.62, 2.50, 8.76, 0.78, fill=YELLOW, border=None)
    add_text(s, 0.80, 2.62, 8.40, 0.55,
             "\"TODAY I'LL GET THE CORE FUNCTION TO ___.\"",
             size=18, bold=True, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    add_card(s, 0.62, 3.45, 8.76, 1.20, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.86, 3.60, 8.28, 0.55,
             "\"DONE\" IS NOT EVERYTHING YOU CAN IMAGINE — it's the core function on your requirements sheet. "
             "Say it against the sheet; anything beyond it gets pulled back.",
             size=12, bold=True)
    add_text(s, 0.86, 4.25, 8.28, 0.50,
             "You may add half a sentence: \"...and give it a (shell / label)\" — no fit, skip it. "
             "Looks are optional; function is the required question.",
             size=10.5)
    set_notes(s, "Stand-up. First read your baton sheet — what did last leg "
                 "say is the first thing this leg? Then one sentence: 'Today "
                 "I'll get the core function to ___.' Definition check: "
                 "'done' is not everything you can imagine — it's the core "
                 "function on your requirements sheet. Say it against the "
                 "sheet; anything beyond it gets pulled back. You may add half "
                 "a sentence: '...and give it a (shell / label)' — no fit, skip "
                 "it. Looks are optional; function is the required question.")
    return s


def slide_14(prs):
    s = page(prs, 15)
    add_title_bar(s, "Go — Rules as Leg One")
    add_card(s, 0.62, 1.50, 8.76, 1.35, fill=WHITE, border=INK, border_w=1.5)
    rules = [
        "CHECK AGAINST YOUR REQUIREMENTS SHEET — change it, cross it out, don't delete",
        "15 MINUTES NO PROGRESS = RAISE YOUR HAND — stuck is no shame; grinding alone is",
        "CODE QUESTIONS GO TO AI FIRST — one step at a time",
    ]
    ry = 1.65
    for i, r in enumerate(rules):
        num_block(s, 0.78, ry, str(i + 1), size=0.32)
        add_text(s, 1.22, ry + 0.04, 7.80, 0.34, r, size=12, bold=True)
        ry += 0.38
    yellow_box(s, 0.62, 3.05, 8.76, 0.58, [
        "aily unsure? Flip your two-views cheat sheet — it was written for today."],
        size=12.5)
    yellow_box(s, 0.62, 3.75, 8.76, 0.72, [
        "THE LAST 10 MINUTES ARE THE QUICK SHELL — function runs first, then the scissors: "
        "shell, still, label, hide. Land as many of the four as you can. Function is always the required question."],
        size=10.5)
    red_line(s, 0.62, 4.50, 8.76, 0.72,
             "15 MINUTES BEFORE REVIEW, HANDS OFF EVERYWHERE",
             "get ready with two lines: \"right now it can ___; it still can't ___.\"")
    set_notes(s, "Go. Rules as leg one: check against your requirements sheet; "
                 "15 minutes no progress — raise your hand; code questions go "
                 "to AI first. One thing new today: aily unsure? Flip your "
                 "two-views cheat sheet — it was written for today. The last "
                 "10 minutes are the quick shell: once the function runs, then "
                 "the scissors — shell, still, label, hide; land as many of "
                 "the four as you can. Not getting one in is no shame — "
                 "function is always the required question. 15 minutes before "
                 "review, table by table: get ready with two lines — 'right "
                 "now it can ___; it still can't ___.' Review starts on time — "
                 "nobody squeezes it out.")
    return s


def slide_15(prs):
    s = page(prs, 16)
    add_title_bar(s, "Hands Off. Review Time — How Sturdy Is It?")
    add_text(s, 0.62, 1.42, 8.76, 0.55,
             "Last leg's reviewer asked \"does it look right?\" THIS leg's reviewer checks "
             "\"how sturdy is it?\" — the 5-point sturdiness checklist, tested one by one.",
             size=12.5, bold=True, align=PP_ALIGN.CENTER)
    grey_box(s, 0.62, 2.08, 8.76, 1.55, [
        "Quinn, still you. Based on the current state: my project can ___ now,",
        "and can't ___ yet.",
        "You're a test engineer. Give me a 5-point \"sturdiness checklist\":",
        "use it 10 times in a row? leave it alone 5 minutes, then touch it?",
        "a different person tries it? press fast, press slow, press randomly?",
        "— make each one specific: exactly how to operate it, and what to watch for.",
    ], size=10.5, line_spacing=1.35)
    add_card(s, 0.62, 3.78, 8.76, 0.58, fill=CODEBG, border=INK, border_w=1.0)
    add_text(s, 0.78, 3.88, 8.44, 0.45,
             "Quinn is the BMAD team's test engineer — this conversation needs the team in it. "
             "The project conversation has run since Lesson 8 — send the prompt directly. "
             "A fresh conversation sends the background line first: "
             "\"This conversation has a BMAD team: John (PM), Sally (UX designer), "
             "Winston (architect), Amelia (developer), Quinn (test engineer). "
             "Remember them — I'll call on them directly from now on.\"",
             size=9)
    red_line(s, 0.62, 4.45, 8.76, 0.75,
             "THE REVIEW STARTS ON TIME",
             "NOBODY SQUEEZES IT OUT, NOT EVEN ME.")
    set_notes(s, "Hands off. Review time — last leg's reviewer asked 'does it "
                 "look right?'; this leg's reviewer checks 'how sturdy is it?' "
                 "The lead is old friend Quinn: a 5-point sturdiness checklist, "
                 "tested one by one — this leg upgrades, no more picking two. "
                 "The Picky User drops to a single most-lethal fault. Prompts "
                 "up, same old rules: feed the real current state, no bragging; "
                 "and keep going in the same chat window — don't open a new one.")
    return s


def slide_16(prs):
    s = page(prs, 17)
    add_title_bar(s, "The Picky User — This Leg, One Fault")
    grey_box(s, 0.62, 1.42, 8.76, 1.25, [
        "You are now my real user (___). My project currently does: ___,",
        "and still can't: ___.",
        "No praise allowed. As them, pick only 1 fault — the single most lethal one.",
    ], size=11, line_spacing=1.4)
    yellow_box(s, 0.62, 2.85, 8.76, 0.58, [
        "AI starts praising? Push back — \"No praise. Faults only.\""],
        size=13)
    add_text(s, 0.62, 3.60, 8.76, 0.55,
             "All five pass? Congratulations, it's sturdy — have your desk-mate try it the barbarian way.",
             size=12, align=PP_ALIGN.CENTER)
    set_notes(s, "The Picky User, this leg downgraded: pick only 1 fault — the "
                 "single most lethal one. AI starts praising? Push back — 'No "
                 "praise. Faults only.' All five pass? Congratulations, it's "
                 "sturdy — have your desk-mate try it the barbarian way.")
    return s


def slide_17(prs):
    s = page(prs, 18)
    add_title_bar(s, "Review Record · Leg 2 — Write It Down as You Go")
    grey_box(s, 0.62, 1.42, 8.76, 2.65, [
        "# Review Record · Leg 2",
        "## Quinn's 5-point sturdiness checklist (test every one, note the result)",
        "1. ______ tested: passed/broke ______",
        "2. ______ tested: passed/broke ______",
        "3. ______ tested: passed/broke ______",
        "4. ______ tested: passed/broke ______",
        "5. ______ tested: passed/broke ______",
        "",
        "## The Picky User's 1 fault",
        "______ -> my decision: accept/reject, reason: ______",
    ], size=10.5, line_spacing=1.35)
    add_text(s, 0.62, 4.35, 8.76, 0.40,
             "Same chat window as the review — don't open a new one.",
             size=11.5, align=PP_ALIGN.CENTER)
    set_notes(s, "This page is the EN structural delta — the CN v2.2 plan has "
                 "no review-record projected page, but the EN Teacher's Guide's "
                 "zero-print rule names the review record explicitly: all "
                 "projected. The template is identical to the student "
                 "document — the page exists so the room fills the same grid "
                 "the workbook carries. The five tested lines are filled for "
                 "real as they go. The decision line feeds slide 18's decide "
                 "block. Stand-still during fill-in.")
    return s


def slide_18(prs):
    s = page(prs, 19)
    add_title_bar(s, "Decide One by One — Fill the Leg-Two Baton Sheet")
    add_card(s, 0.62, 1.40, 8.76, 0.90, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.86, 1.52, 8.28, 0.70,
             "ACCEPT OR REJECT — BOTH NEED A REASON. "
             "Heads-up: next leg is the sprint leg — FIX-ONLY, NO ADDING. "
             "Anything you can't finish today, think hard before you write it as "
             "\"first thing next leg\": that's your last chance to fix it.",
             size=11.5, bold=True)
    grey_box(s, 0.62, 2.36, 8.76, 1.62, [
        "# Baton Handoff Sheet · Leg 2",
        "Name: ______  Date: ______",
        "",
        "## Where this leg ended (one verifiable sentence: what it can demo)",
        "## I called in ___ (no library? write: \"I didn't import, because ___\")",
        "## What the look is now (one line: what it looks like now; no shell? write: \"still loose parts\")",
        "## The review point that matters most + my decision (accept/reject + reason)",
        "## The first thing next leg (specific, verifiable — next leg is fix-only, think it through)",
    ], size=9, line_spacing=1.20)
    red_line(s, 0.62, 4.00, 8.76, 0.78,
             "ACCEPT EVERYTHING? I'M COMING TO TALK TO YOU",
             "no backbone is more dangerous than no changes.")
    yellow_box(s, 0.62, 4.82, 8.76, 0.40, [
        "\"DID\" — I called in ___ and it saved me ___; the look used ___ (materials); sturdiness passed ___ checks."],
        size=9, line_spacing=1.0)
    set_notes(s, "One by one: accept or reject — and both need a reason. "
                 "Heads-up: next leg is the sprint leg — fix-only, no adding. "
                 "Anything you can't finish today, think hard before you write "
                 "it as 'first thing next leg': that's your last chance to fix "
                 "it. Fill the leg-two baton handoff sheet — into your student "
                 "document. Log, four lines as usual — 'did' reads: I called "
                 "in ___ and it saved me ___; the look used ___ (materials); "
                 "sturdiness passed ___ checks.")
    return s


def slide_19(prs):
    s = page(prs, 20)
    add_title_bar(s, "The Capstone — Nine Lessons, and Here We Are")
    journey = [
        "Lesson 1 — you lit your first lamp",
        "Lesson 2 — you found a question worth doing",
        "Lesson 3 — your project grew a screen",
        "Lesson 4 — you got an AI team",
        "Lesson 5 — you taught hardware to see",
        "Lesson 6 — you moved your project home",
        "Lesson 7 — you briefed it",
        "Lesson 8 — you ran the first lap",
        "TODAY — you called in reinforcements",
    ]
    jy = 1.42
    for i, line in enumerate(journey):
        sz = 12 if i < 8 else 14
        b = i == 8
        check_item(s, 0.62, jy, 8.76, line, size=sz, h=0.26)
        jy += 0.30
    yellow_box(s, 0.62, 4.10, 8.76, 0.62, [
        "From daring, to reading, to calling in help — your function has capped out, and it has a face for the first time.",
        "(Pause one second — look at it.)"],
        size=10.5, line_spacing=1.25)
    add_text(s, 0.62, 4.78, 8.76, 0.42,
             "NEXT LESSON: THE LAST LEG + THE ROADSHOW. Sprint discipline in four words: "
             "FIX-ONLY, NO ADDING. Bring your baton sheet, your project, and the side of it "
             "you most want to show.",
             size=10, align=PP_ALIGN.CENTER, line_spacing=1.20)
    set_notes(s, "Lesson one, you lit your first lamp; two, you found a "
                 "question worth doing; three, your project grew a screen; "
                 "four, you got an AI team; five, you taught hardware to see; "
                 "six, you moved your project home; seven, you briefed it; "
                 "eight, you ran the first lap; today, you called in "
                 "reinforcements — code help and look help — from daring, to "
                 "reading, to calling in help. Your project's function has "
                 "capped out, and it has a face for the first time. (Pause one "
                 "second — look at it.) This is what nine lessons look like. "
                 "Next lesson: the last leg + the roadshow. Sprint discipline "
                 "in four words: fix-only, no adding. Bring your baton sheet, "
                 "your project, and the side of it you most want to show.")
    return s


# ------------------------------------------------------------------ build
def main():
    prs = new_deck()
    slide_01(prs)
    slide_02(prs)
    slide_03(prs)
    slide_04(prs)
    slide_05(prs)
    slide_06(prs)
    slide_07(prs)
    slide_08(prs)
    slide_09(prs)
    slide_10(prs)
    slide_11(prs)
    slide_12(prs)
    slide_12b(prs)
    slide_13(prs)
    slide_14(prs)
    slide_15(prs)
    slide_16(prs)
    slide_17(prs)
    slide_18(prs)
    slide_19(prs)
    prs.save(OUT)
    print(f"Saved: {OUT} slides: {len(prs.slides)}")


if __name__ == "__main__":
    main()
