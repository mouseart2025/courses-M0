"""
Build the English Lesson 8 deck (Run the First Lap, 42 slides):
17 main slides from M0_EN_PPTPlan_CFG-5_Lesson08_RunTheFirstLap_v1.md
+ 25-page Brandy appendix (content spine from the plan, localized text).

Output: 交付物_EN/03_Deliverables/PPTX/M0_EN_Deck_CFG-5_Lesson08_RunTheFirstLap_v1.pptx
Chaihuo brand spec; red budget exactly 4 (slides 05, 12, 13, 15).
No CJK / emoji / fullwidth vertical bars on screen. Photos with Chinese
 glyphs are replaced by placeholder cards; only confirmed Chinese-free
Brandy photos are embedded.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder_lib import *
from pptx.util import Inches
from pptx.enum.text import MSO_ANCHOR

TOTAL = 42
DECK_LABEL = "Run the First Lap"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson08_RunTheFirstLap_v1.pptx")

COVER_ART = "/Users/leonfeng/Baiduyun/M0/M0-V2/assets/L8_封面插画_第一棒MVP.png"
BRANDY_KBD = ("/Users/leonfeng/Baiduyun/M0/M0-V2/旧版与中间件_归档/"
              "演示文稿_工程与截图/M0_演示文稿_CFG-5_第8课_跑通第一圈_v2/"
              "media/brandy_kbd.jpg")
BRANDY_SINGLE = ("/Users/leonfeng/Baiduyun/M0/M0-V2/旧版与中间件_归档/"
                 "演示文稿_工程与截图/M0_演示文稿_CFG-5_第8课_跑通第一圈_v2/"
                 "media/brandy_single_key.jpg")
BRANDY_INTERACT = ("/Users/leonfeng/Baiduyun/M0/M0-V2/旧版与中间件_归档/"
                   "演示文稿_工程与截图/M0_演示文稿_CFG-5_第8课_跑通第一圈_v2/"
                   "media/brandy_interact.jpg")
BRANDY_HOURGLASS = ("/Users/leonfeng/Baiduyun/M0/M0-V2/旧版与中间件_归档/"
                    "演示文稿_工程与截图/M0_演示文稿_CFG-5_第8课_跑通第一圈_v2/"
                    "media/brandy_hourglass_final.jpg")


def page(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(s)
    add_footer(s, n, TOTAL, DECK_LABEL)
    return s


def num_block(s, x, y, num, size=0.40):
    add_rect(s, x, y, size, size, fill=YELLOW, border=None)
    add_text(s, x, y + 0.03, size, 0.32, num, size=15, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER)


def yellow_box(s, x, y, w, h, lines, size=13, line_spacing=1.25):
    add_rect(s, x, y, w, h, fill=YELLOW, border=None)
    add_multiline(s, x + 0.18, y + 0.12, w - 0.36, h - 0.24, lines, size=size,
                  line_spacing=line_spacing)


def grey_box(s, x, y, w, h, lines, size=10, line_spacing=1.3):
    add_card(s, x, y, w, h, fill=CODEBG, border=INK, border_w=1.0)
    items = [(t, {"mono": True}) if isinstance(t, str) else t for t in lines]
    add_multiline(s, x + 0.16, y + 0.10, w - 0.32, h - 0.20, items, size=size,
                  line_spacing=line_spacing)


def check_item(s, x, y, w, text, size=12, h=0.30):
    add_rect(s, x, y + 0.04, 0.20, 0.20, fill=YELLOW, border=None)
    add_text(s, x + 0.34, y, w - 0.34, h, text, size=size)


def add_photo_or_placeholder(s, path, x, y, w, h, label="photo"):
    if path and os.path.exists(path):
        s.shapes.add_picture(path, Inches(x), Inches(y), Inches(w),
                             Inches(h))
    else:
        add_card(s, x, y, w, h, fill=CODEBG, border=INK, border_w=1.0)
        add_text(s, x + 0.10, y + h / 2 - 0.10, w - 0.20, 0.20,
                 f"[ {label} — to be captured at rehearsal ]", size=9, mono=True,
                 align=PP_ALIGN.CENTER)


def red_line(s, y, text, size=13, h=0.30):
    add_rect(s, 0.62, y, 0.07, 0.46, fill=RED, border=None)
    add_oval(s, 0.86, y + 0.06, 0.12, fill=RED, border=None)
    add_text(s, 1.12, y + 0.02, 8.26, h, text, size=size, bold=True, color=RED)


def red_multiline(s, y, lines, size=13, h=0.46):
    add_rect(s, 0.62, y, 0.07, h, fill=RED, border=None)
    add_oval(s, 0.86, y + 0.06, 0.12, fill=RED, border=None)
    add_multiline(s, 1.12, y + 0.02, 8.26, h - 0.04, lines, size=size,
                  line_spacing=1.2)


# ------------------------------------------------------------------ main slides

def slide_01(prs):
    s = page(prs, 1)
    add_text(s, 0.62, 1.20, 6.4, 0.3,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0)",
             size=13)
    add_text(s, 0.62, 1.55, 8.76, 0.75, "Run the First Lap", size=38,
             bold=True)
    add_rect(s, 0.62, 2.50, 1.6, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 2.68, 6.4, 0.6,
             "Build Your Project's MVP · The Marathon's First Leg · Chaihuo "
             "Maker Academy · M0 Lesson 8", size=14, line_spacing=1.2)
    add_multiline(s, 0.62, 3.60, 5.8, 0.95, [
        ("Today: from a requirements sheet to a running first version —",
         {"size": 12.5}),
        ("and AI becomes a reviewer for the first time.", {"size": 12.5}),
    ], line_spacing=1.35)
    add_photo_or_placeholder(s, COVER_ART, 6.80, 3.05, 2.45, 2.45,
                             label="baton illustration")
    set_notes(s, "Cover page only; students see it as they sit down. No "
                 "script. When the session starts, go straight to slide 02 — "
                 "the opener's 30-second look-back is spoken, not projected. "
                 "Right side: the baton illustration (the CN deck's "
                 "IMG-01-01 — reused because it carries no Chinese glyphs); "
                 "yellow rule under the subtitle. Footer: Chaihuo Maker "
                 "Academy · M0 · Run the First Lap | 08 / 42.")
    return s


def slide_02(prs):
    s = page(prs, 2)
    add_title_bar(s, "From Today, I Only Circulate")
    add_subtitle(s, "I don't teach", y=1.00, size=13)
    add_rect(s, 0.62, 1.50, 0.07, 1.05, fill=YELLOW, border=None)
    add_multiline(s, 0.88, 1.52, 8.50, 1.00, [
        ("Last session: your project got its brief — the requirements "
         "sheet is in your workbook, the core feature is down to one, and "
         "what got cut keeps its name.", {"size": 11}),
        ("The session before: your project moved into your own computer — "
         "from tenant to owner — and for the first time you saw what lives "
         "inside the code AI writes.", {"size": 11}),
    ], line_spacing=1.35)
    add_text(s, 0.62, 2.72, 8.76, 0.26, "THE THREE LEGS", size=10.5, bold=True)
    legs = [
        ("LEG 1 (today)", "BUILD YOUR PROJECT'S MVP"),
        ("LEG 2 (Lesson 9)", "CALL IN REINFORCEMENTS — new modules, new "
                              "libraries, the MVP grows new abilities"),
        ("LEG 3 (Lesson 10)", "FINAL POLISH — out to the showcase to meet "
                               "people"),
    ]
    ly = 3.05
    for i, (tag, body) in enumerate(legs):
        add_card(s, 0.62, ly, 8.76, 0.60, fill=WHITE, border=INK,
                 border_w=1.5)
        num_block(s, 0.74, ly + 0.10, str(i + 1), size=0.34)
        add_text(s, 1.20, ly + 0.08, 8.00, 0.22, tag, size=11, bold=True)
        add_text(s, 1.20, ly + 0.32, 8.00, 0.22, body, size=10)
        ly += 0.72
    yellow_box(s, 0.62, 4.50, 8.76, 0.72, [
        "Every leg runs the same rhythm — STAND-UP → BUILD → AI REVIEW → "
        "DECIDE → HANDOFF. Run all three legs, and your project has grown "
        "up."], size=12)
    set_notes(s, "30-second look-back: last session, your project got its "
                 "brief — the requirements sheet is in your workbook, the "
                 "core feature is down to one, and what got cut keeps its "
                 "name. The session before, your project moved into your own "
                 "computer — from tenant to owner — and for the first time "
                 "you saw what lives inside the code AI writes. From today, "
                 "the course shifts gear. Before, you followed me; from "
                 "today, I only circulate. I don't teach. What comes next is "
                 "the marathon — three legs. Leg one (today): build your "
                 "project's MVP. Leg two (Lesson 9): bring in the help — "
                 "new modules, new libraries, and the MVP grows new "
                 "abilities. Leg three (Lesson 10): the final polish — out "
                 "to the showcase to meet people. Every leg runs the same "
                 "rhythm: stand-up → build → AI review → decide → handoff. "
                 "Run all three legs, and your project has grown up. This "
                 "page is the first golden-line peak — big type, wide white "
                 "space, the three legs as the visual spine.")
    return s


def slide_03(prs):
    s = page(prs, 3)
    add_title_bar(s, "Today's Goal — Build Your MVP")
    add_rect(s, 0.62, 1.10, 8.76, 0.46, fill=YELLOW, border=None)
    add_text(s, 0.80, 1.18, 8.40, 0.30,
             "MVP = MINIMUM VIABLE PRODUCT — the smallest version you can put "
             "on the table and demonstrate.", size=12, bold=True)
    add_text(s, 0.62, 1.72, 8.76, 0.24, "THE CLOSED LOOP", size=10.5,
             bold=True)
    add_card(s, 0.62, 2.02, 3.80, 0.85, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 2.16, 3.44, 0.60,
             "IT SENSES SOMETHING\n(the sensor has a reading)", size=11.5,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.2)
    add_text(s, 4.62, 2.18, 0.76, 0.55, "→", size=28, bold=True,
             color=YELLOW, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_card(s, 5.50, 2.02, 3.88, 0.85, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.68, 2.16, 3.52, 0.60,
             "IT REACTS\n(light / buzzer / screen)", size=11.5,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
             line_spacing=1.2)
    add_text(s, 0.62, 3.05, 8.76, 0.24,
             "— start to finish, once.", size=12, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.45, 8.76, 0.24, "YES / NO", size=10.5, bold=True)
    yesno = [
        ("YES", "minimal but one complete loop — it senses, then it reacts, "
                "once. Today is lap one of Neil's spiral development."),
        ("NOT", "every feature on your requirements sheet — the rest sleeps "
                "soundly on the \"later\" list."),
        ("NOT", "a half-finished thing. Half-finished is \"made half of it.\""),
    ]
    yy = 3.78
    for label, body in yesno:
        add_rect(s, 0.62, yy, 0.80, 0.40, fill=YELLOW if label == "YES" else
                 WHITE, border=INK if label == "YES" else INK, border_w=1.5)
        add_text(s, 0.70, yy + 0.05, 0.64, 0.30, label, size=10, bold=True,
                 align=PP_ALIGN.CENTER)
        add_text(s, 1.60, yy + 0.04, 7.78, 0.36, body, size=10.5)
        yy += 0.48
    set_notes(s, "What's an MVP? It's engineer slang for minimum viable "
                 "product — the smallest version you can put on the table "
                 "and demonstrate. Careful: it's not a half-finished thing. "
                 "Half-finished is 'made half of it.' MVP is 'minimal but "
                 "one complete loop' — it senses something, then it reacts, "
                 "start to finish, once. All the features on your "
                 "requirements sheet? Not today. Today is only the smallest "
                 "loop. Remember Neil's spiral development? Today is lap one. "
                 "'What if I don't finish?' → 'The first version is only the "
                 "smallest closed loop. Everything else on the sheet is "
                 "sleeping soundly on the later list.' The two NOT lines "
                 "sell the definition by contrast — the 'half-finished' line "
                 "is the commonest misunderstanding.")
    return s


def slide_04(prs):
    s = page(prs, 4)
    add_title_bar(s, "Brandy's First Version? One Key.")
    add_multiline(s, 0.62, 1.02, 8.76, 0.56, [
        ("Remember Brandy — Seeed's application engineer, the one who built "
         "a voice keyboard with ZERO code. Her first version had ONE key. "
         "One.", {"size": 12.5}),
    ], line_spacing=1.3)
    add_card(s, 0.62, 1.72, 8.76, 1.08, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.84, 1.86, 8.32, 0.84, [
        ("20 presses in a row, not one missed.", {"size": 16, "bold": True}),
        ("Doesn't pass? No new features. Passes? Then the second key goes "
         "in. She uses that keyboard every day now.", {"size": 11.5}),
    ], line_spacing=1.35)
    add_photo_or_placeholder(s, BRANDY_SINGLE, 3.20, 3.00, 3.60, 2.20,
                             label="one-key first version")
    add_rect(s, 0.62, 4.42, 0.07, 0.80, fill=YELLOW, border=None)
    add_multiline(s, 0.88, 4.48, 8.50, 0.74, [
        ("MINIMAL IS NOT CRUDE — IT'S PROFESSIONAL.",
         {"size": 13, "bold": True}),
        ("Your first loop is the same: don't grab for more. Walk it through "
         "once. Twenty presses, not one missed.", {"size": 11}),
    ], line_spacing=1.25)
    set_notes(s, "Remember Brandy from the kickoff session? Li Shiwen, "
                 "Seeed's application engineer — the one who built a voice "
                 "keyboard with zero code. Look at her first version — it "
                 "had one key. One. And the acceptance standard was a single "
                 "line: 20 presses in a row, not one missed. Doesn't pass? "
                 "No new features. Passes? Then the second key goes in. She "
                 "uses that keyboard every day now. That's a professional "
                 "engineer's MVP: minimal, but a complete loop, with an "
                 "acceptance standard stated out loud. Minimal is not crude "
                 "— it's professional. Your first loop is the same: don't "
                 "grab for more. Walk it through once. Twenty presses, not "
                 "one missed. 'Does one key really count as a project?' → "
                 "'Yes. She verified the hardest segment first — your first "
                 "loop verifies your hardest segment first, too.' This page "
                 "is a V4 addition the CN v2 plan never had — the reason "
                 "Act 1 is 7 pages. Keep it to one minute; the golden line "
                 "is the payload.")
    return s


def slide_05(prs):
    s = page(prs, 5)
    add_title_bar(s, "The Three Rules of Build Time")
    add_card(s, 0.62, 1.12, 8.76, 1.02, fill=WHITE, border=INK, border_w=1.5)
    num_block(s, 0.74, 1.22, "1", size=0.34)
    add_text(s, 1.24, 1.28, 7.90, 0.78,
             "Check against your requirements sheet — changing it is "
             "allowed, CROSS IT OUT, DON'T ERASE.", size=14, bold=True,
             line_spacing=1.2)
    add_card(s, 0.62, 2.24, 8.76, 1.02, fill=WHITE, border=INK, border_w=1.5)
    num_block(s, 0.74, 2.34, "2", size=0.34)
    add_rect(s, 0.62, 2.24, 0.07, 1.02, fill=RED, border=None)
    add_oval(s, 0.86, 2.36, 0.12, fill=RED, border=None)
    add_multiline(s, 1.24, 2.30, 7.90, 0.90, [
        ("15 MINUTES WITH NO PROGRESS = RAISE YOUR HAND —", {"size": 14,
                                                             "bold": True,
                                                             "color": RED}),
        ("STUCK IS NOT SHAMEFUL; TOUGHING IT OUT SILENTLY IS",
         {"size": 13.5, "bold": True, "color": RED}),
    ], line_spacing=1.2)
    add_card(s, 0.62, 3.36, 8.76, 1.02, fill=WHITE, border=INK, border_w=1.5)
    num_block(s, 0.74, 3.46, "3", size=0.34)
    add_text(s, 1.24, 3.52, 7.90, 0.78,
             "Code questions go to your AI first — \"one step at a time.\"",
             size=14, bold=True, line_spacing=1.2)
    yellow_box(s, 0.62, 4.52, 8.76, 0.70, [
        "Change is allowed — cross it out, don't erase — so everyone can "
        "see you changed your mind."], size=13)
    set_notes(s, "Three rules. One: check against your requirements sheet — "
                 "changing it is allowed, cross it out, don't erase. Two: 15 "
                 "minutes with no progress = raise your hand. Stuck is not "
                 "shameful; toughing it out silently is. Three: code "
                 "questions go to your AI first. I and the TAs answer "
                 "direction only and rescue the stuck only. The red line is "
                 "the deck's first red — the survival rule. After reading, "
                 "do NOT flip away — this page stays up for the whole build "
                 "(115 min); slides 08/09/10/11 are temporary cut-ins that "
                 "return here. Largest type in the deck — readable from the "
                 "back row. Rule two is rendered entirely in red. A student "
                 "quietly changes the sheet and adds features during the "
                 "build → point at the projected rule, no scolding: 'Change "
                 "is allowed — cross it out, don't erase. But ask first: "
                 "does it serve the core feature? No? It goes on the later "
                 "list.'")
    return s


def slide_06(prs):
    s = page(prs, 6)
    add_title_bar(s, "The Stand-Up")
    add_subtitle(s, "one sentence each, verifiable", y=1.00, size=13)
    add_card(s, 0.62, 1.45, 8.76, 1.20, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 1.00, 1.75, 8.00, 0.65,
             "\"TODAY I'LL FIRST MAKE ___ RUN.\"", size=22, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.88, 8.76, 0.24, "CONTRAST", size=10.5, bold=True)
    add_card(s, 0.62, 3.18, 8.76, 0.48, fill=WHITE, border=INK, border_w=1.5)
    add_rect(s, 0.62, 3.18, 0.80, 0.48, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.72, 3.28, 0.60, 0.28, "NO", size=11, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 1.60, 3.24, 7.60, 0.36,
             "\"Keep working on my project\" — doesn't count", size=11)
    add_card(s, 0.62, 3.74, 8.76, 0.70, fill=WHITE, border=INK, border_w=1.5)
    add_rect(s, 0.62, 3.74, 0.80, 0.70, fill=YELLOW, border=INK, border_w=1.5)
    add_text(s, 0.72, 3.94, 0.60, 0.28, "YES", size=11, bold=True,
             align=PP_ALIGN.CENTER)
    add_multiline(s, 1.60, 3.82, 7.60, 0.56, [
        ("\"Make the button light the LED when pressed\" — counts",
         {"size": 11.5, "bold": True}),
        ("(The moment you finish — what will I be able to see?)",
         {"size": 10.5}),
    ], line_spacing=1.3)
    yellow_box(s, 0.62, 4.44, 8.76, 0.70, [
        "SMALL CLASS: everyone stands — really standing, that's the "
        "stand-up's dignity — one by one. | LARGE CLASS: pair up and say it "
        "to each other, then write the sentence at the top of your "
        "requirements sheet (that's the stand-up's trace)."], size=10)
    set_notes(s, "The stand-up — the first thing every marathon work session "
                 "does. The rule: one sentence each, no more: 'Today I'll "
                 "first make ___ run.' It has to be verifiable — 'keep "
                 "working' doesn't count; 'make the button light the LED "
                 "when pressed' counts. Vague goal ('keep working on my "
                 "project') → push on the spot: 'The moment you finish — "
                 "what will I be able to see?' Push until it's one "
                 "verifiable action. The stand-up turns into a report "
                 "(someone talks over 30 seconds) → raise the hourglass: "
                 "'Noted. Details are for build time, one-on-one.' Two ways "
                 "to run it — pick by headcount (small: everyone stands and "
                 "says it, you hold the hourglass, 'you first'; large: no "
                 "going around — pair up, write the sentence at the top of "
                 "the requirements sheet, you call 3–4 people at random to "
                 "stand and say it to the class, the rest get a glance at "
                 "their page as you circulate).")
    return s


def slide_07(prs):
    s = page(prs, 7)
    add_title_bar(s, "Check Out the Parts")
    add_subtitle(s, "by the sheet, register everything", y=1.00, size=13)
    rules = [
        ("1", "Take only what your requirements sheet's hardware row says — "
              "NO TAKING PARTS YOU DON'T NEED (everything you eyed during "
              "the tour waits until the sheet changes)"),
        ("2", "Register everything you take — name on your table's sheet"),
        ("3", "Hot part already gone? Write it in the queue area on the "
              "board — then find a substitute. Engineer's first lesson: "
              "solve the problem with what you have"),
        ("4", "Sheet lists something not in the pool? Change the need on "
              "the spot — cross it out, don't erase, write the substitute"),
    ]
    ry = 1.42
    for num, txt in rules:
        add_card(s, 0.62, ry, 8.76, 0.70, fill=WHITE, border=INK,
                 border_w=1.5)
        num_block(s, 0.74, ry + 0.18, num, size=0.34)
        add_text(s, 1.24, ry + 0.10, 8.00, 0.52, txt, size=10.5,
                 line_spacing=1.15)
        ry += 0.78
    yellow_box(s, 0.62, 4.58, 8.76, 0.64, [
        "At the end of every leg, parts you're not using go back — it's a "
        "shared pool; you'll need it next leg."], size=12)
    set_notes(s, "Check-out rules: take only what your requirements sheet's "
                 "hardware row says; register everything you take — name on "
                 "the sheet on your table. No taking parts you don't need "
                 "(everything you eyed during the tour waits until the sheet "
                 "changes). Hot part already gone? Write it in the queue "
                 "area on the board — then find a substitute. Remember? An "
                 "engineer's first lesson: solve the problem with what you "
                 "have. At the end of every leg, parts you're not using go "
                 "back. It's a shared pool — you'll need it next leg. "
                 "Check-out bottleneck → TA B calls tables in batches (tables "
                 "1 and 3 first); whoever's checked out starts building. A "
                 "hot part runs out and there's an argument → register in "
                 "the queue area + the 'make it or not' three questions to "
                 "coordinate substitutes; no purchase promises. A student's "
                 "sheet lists something not in the pool → change the need on "
                 "the spot (cross out, don't erase, write the substitute); "
                 "TA A helps in 2 minutes. Stand-still while check-out runs.")
    return s


def slide_08(prs):
    s = page(prs, 8)
    add_title_bar(s, "Start — Cut the Loop in Two")
    add_card(s, 0.62, 1.45, 3.80, 1.10, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.80, 1.62, 3.44, 0.80, [
        ("1", {"size": 16, "bold": True}),
        ("MAKE IT SENSE", {"size": 13.5, "bold": True}),
        ("the sensor has a reading", {"size": 11}),
    ], line_spacing=1.3)
    add_text(s, 4.62, 1.72, 0.76, 0.55, "→", size=28, bold=True,
             color=YELLOW, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_card(s, 5.50, 1.45, 3.88, 1.10, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 5.68, 1.62, 3.52, 0.80, [
        ("2", {"size": 16, "bold": True}),
        ("MAKE IT REACT", {"size": 13.5, "bold": True}),
        ("light / buzzer / screen", {"size": 11}),
    ], line_spacing=1.3)
    yellow_box(s, 0.62, 2.80, 8.76, 0.88, [
        "ONE STEP AT A TIME. Devices stay on; AI conversation windows stay "
        "open. Water and bathroom — your call."], size=13)
    set_notes(s, "Start. First move: cut the smallest loop into two steps — "
                 "first make it sense (the sensor has a reading), then make "
                 "it react (light / buzzer / screen). One step at a time. I "
                 "do one lap every 15 minutes; raise your hand and I'm "
                 "there. Water and bathroom — your call. Devices stay on; "
                 "AI conversation windows stay open. Then immediately back "
                 "to slide 05. Your circulation rhythm (this lesson's core "
                 "skill — the shift from teaching to circulating): one lap "
                 "every 15 minutes, three looks per lap — the screen "
                 "(chatting with AI, or staring off / browsing?), the "
                 "requirements sheet (is it on the table? are they building "
                 "to it?), the face (a frown past 5 minutes — stop and ask "
                 "one question). Intervention red line: direction only ('Back "
                 "to your sheet — what's the core feature?'); no writing "
                 "code, no thinking up solutions, no making decisions; a "
                 "student asks 'which should I do?' → 'What does your "
                 "requirements sheet say?'")
    return s


def slide_09(prs):
    s = page(prs, 9)
    add_title_bar(s, "The Mid-Way Stand-Up")
    add_subtitle(s, "still standing, still one line", y=1.00, size=13)
    add_rect(s, 0.62, 1.45, 0.09, 1.20, fill=YELLOW, border=None)
    add_text(s, 0.96, 1.60, 8.30, 0.90,
             "WHERE I AM  |  WHERE I'M STUCK  |  WHAT I DO NEXT",
             size=18, bold=True, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.MIDDLE)
    yellow_box(s, 0.62, 2.90, 8.76, 0.60, [
        "Anyone who can't say \"next\" — the TA notes your name; you get "
        "rescued first when the second half starts."], size=12.5)
    set_notes(s, "One line: where I am / where I'm stuck / what I do next. "
                 "Anyone who can't say 'next' — the TA notes your name, and "
                 "you get rescued first when the second half starts. No "
                 "unified break; the mid-way stand-up is done standing (a "
                 "stretch too), hourglass timed. Noting who can't say 'next "
                 "step' and rescuing them first in the second half is the "
                 "pace officer's job (TA C) — instructor-side, never on "
                 "screen.")
    return s


def slide_10(prs):
    s = page(prs, 10)
    add_title_bar(s, "Second Half — Close the Loop")
    add_text(s, 0.62, 1.35, 8.76, 0.55,
             "Whatever segment the loop is still broken on — that's what you "
             "fix.", size=17, bold=True, align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 2.08, 8.76, 0.80, [
        "15 MINUTES BEFORE REVIEW, EVERYONE STOPS — WHEREVER YOU ARE, THE "
        "REVIEW STARTS ON TIME."], size=12.5)
    add_rect(s, 0.62, 2.95, 0.07, 0.78, fill=YELLOW, border=None)
    add_multiline(s, 0.88, 3.00, 8.50, 0.72, [
        ("A half-finished thing deserves the faults even more.",
         {"size": 13, "bold": True}),
        ("The review isn't a reward for finishing — it's how you finish.",
         {"size": 12}),
    ], line_spacing=1.25)
    set_notes(s, "Second half's job: close the loop. Whatever segment the "
                 "loop is still broken on — that's what you fix. 15 minutes "
                 "before review, everyone stops. Wherever you are, the "
                 "review starts on time. Remember: the review isn't "
                 "something you earn by finishing — a half-finished thing "
                 "deserves the faults even more. Circulation rhythm same as "
                 "slide 08's notes; from '15 minutes to review' onward, "
                 "remind table by table: 'Save your progress. Prepare two "
                 "lines: my project can ___ now; it still can't ___.' — and "
                 "flip to slide 11. A student begs 'give me 10 more minutes' "
                 "at the stop → warm but firm: 'The review 15 is the "
                 "institutional floor — nobody squeezes it, including me. "
                 "Write your can't yet clearly — that's the review's first "
                 "material.' Morale-drained ('everyone else's is so good') → "
                 "TA C: 'One thing more than yesterday is a win. Is your "
                 "loop closed? Closed = today's 100.' After the announcement, "
                 "return to slide 05.")
    return s


def slide_11(prs):
    s = page(prs, 11)
    add_title_bar(s, "Hands Off — Prepare Two Lines")
    add_card(s, 0.62, 1.45, 4.28, 0.85, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 1.64, 3.92, 0.50,
             "MY PROJECT CAN ___ NOW.", size=15, bold=True,
             align=PP_ALIGN.CENTER)
    add_card(s, 5.10, 1.45, 4.28, 0.85, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.28, 1.64, 3.92, 0.50,
             "IT STILL CAN'T ___ YET.", size=15, bold=True,
             align=PP_ALIGN.CENTER)
    add_rect(s, 0.62, 2.55, 0.07, 1.20, fill=YELLOW, border=None)
    add_multiline(s, 0.88, 2.60, 8.50, 1.12, [
        ("The review must be fed your CURRENT real state — sending the old "
         "brief description gets you sent back to rewrite.",
         {"size": 11.5, "bold": True}),
        ("A bragging review is no review at all.", {"size": 12, "bold": True}),
    ], line_spacing=1.3)
    set_notes(s, "Save your progress. Prepare two lines: my project can ___ "
                 "now; it still can't ___. The two lines are the review's "
                 "feeding lines — the review conversation must be fed the "
                 "current real state; anyone feeding the old brief "
                 "description gets sent back to rewrite (this is the "
                 "review's only food). The warning line carries the "
                 "discipline — bold black on yellow, NOT red (outside the "
                 "quota). Cut in once at '15 minutes to review'; after the "
                 "table-by-table reminder, the deck returns to slide 05 "
                 "until the review actually starts, then on to slide 12.")
    return s


def slide_12(prs):
    s = page(prs, 12)
    add_title_bar(s, "Hands Off. Review Time.")
    add_multiline(s, 0.62, 1.05, 8.76, 0.60, [
        ("Before, AI was your colleague. Today, it's a JUDGE — its job is "
         "finding faults, not praising you.", {"size": 13}),
    ], line_spacing=1.25)
    add_card(s, 0.62, 1.78, 8.76, 0.90, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 1.96, 8.40, 0.30,
             "JUDGE 1 · THE PICKY USER — the real person from your "
             "requirements sheet — 3 FAULTS", size=11.5, bold=True)
    add_text(s, 0.80, 2.30, 8.40, 0.30,
             "JUDGE 2 · QUINN — old friend, the team's test engineer — a "
             "5-ITEM \"BREAK IT\" LIST", size=11.5)
    yellow_box(s, 0.62, 2.85, 8.76, 0.58, [
        "In Lesson 3, it picked ONE fault. From today: the full edition — 3 "
        "faults + a 5-item list. Every leg from here runs this size."],
        size=11)
    add_rect(s, 0.62, 3.58, 0.07, 0.58, fill=YELLOW, border=None)
    add_text(s, 0.88, 3.60, 8.50, 0.54,
             "Both reviews run in the conversation you already have — NO "
             "NEW WINDOWS. A new window = a dropped baton.", size=10.5,
             bold=True)
    red_line(s, 4.28,
             "THE REVIEW STARTS ON TIME — NOBODY SQUEEZES IT, INCLUDING ME",
             size=13.5)
    set_notes(s, "Hands off. Review time. Before, you had AI as a colleague. "
                 "Today, it's a judge — its job is finding faults, not "
                 "praising you. Two judges: first, the real person from your "
                 "requirements sheet (the Picky User); second, an old friend "
                 "— Quinn. A sizing note: in Lesson 3's group build, the "
                 "Picky User picked one fault. From today it's the full "
                 "edition — 3 faults + a 5-item list — and every leg from "
                 "here runs this size. Two review prompts, on screen; keep "
                 "going in the conversation you already have — no new "
                 "windows. Note: you must feed the current real state — 'it "
                 "can do this now, it can't do that' — a bragging review is "
                 "no review at all. The red line is the deck's second red — "
                 "the institutional floor. This is the Act 3 gear change "
                 "('hands off — review time'); whatever's done, you shift "
                 "gears on time — that rhythm itself is part of what today "
                 "teaches.")
    return s


def slide_13(prs):
    s = page(prs, 13)
    add_title_bar(s, "The Picky User — 3 Faults")
    add_text(s, 0.62, 1.05, 8.76, 0.24,
             "Send this in the conversation you already have — no new "
             "windows.", size=12, bold=True)
    grey_box(s, 0.62, 1.40, 8.76, 1.80, [
        "You are now my real user (name: ___; their situation: ___ — copy "
        "the real",
        "person from my requirements sheet).",
        "My project currently does: ___ (current real state, no bragging).",
        "It still can't: ___.",
        "You are not allowed to praise me. As them, pick 3 faults:",
        "the one they'd care about most, the one most likely to make them "
        "not use it,",
        "the one most confusing. One sentence per fault.",
    ], size=10, line_spacing=1.3)
    red_multiline(s, 3.34, [
        ("AI STARTED PRAISING? PUSH BACK —",
         {"size": 12.5, "bold": True, "color": RED}),
        ("\"NO PRAISING. FAULTS ONLY — 3, ONE SENTENCE EACH.\"",
         {"size": 12.5, "bold": True, "color": RED}),
    ], size=12.5, h=0.62)
    yellow_box(s, 0.62, 4.12, 8.76, 0.60, [
        "The 3 faults + your notes go into your review record in your "
        "workbook."], size=12)
    set_notes(s, "Send this to AI (project it). You must feed the current "
                 "real state — what it can do now, what it can't. If it "
                 "dares to praise you, push the red line back at it — a "
                 "review that praises you is a review that didn't show up "
                 "to work. The red line is the deck's third red — the "
                 "push-back line. The AI review turns into AI praise ('your "
                 "project is great, may I suggest some features…') → the "
                 "student pushes back (projected): 'No praising. Faults "
                 "only — 3, one sentence each.' Project your own "
                 "pre-rehearsed 'AI praised → I pushed back' demo "
                 "conversation once. A review item contradicts the "
                 "requirements sheet (AI pushing a cut feature) → a "
                 "teaching point: 'It doesn't know your trade-off history. "
                 "Flip to your later list — this one's already slept "
                 "there. Original verdict stands.' Stand-still. The prompt "
                 "box is 6.2 verbatim — shared text with the Teacher's Guide "
                 "and the workbook; any edit must sync all three documents. "
                 "The review record template (6.5) is workbook-borne — no "
                 "projected page; students fill it as they go.")
    return s


def slide_14(prs):
    s = page(prs, 14)
    add_title_bar(s, "Quinn — the 5-Item \"Break It\" List")
    grey_box(s, 0.62, 1.18, 8.76, 1.28, [
        "Quinn, still you. Based on the current state: my project can ___ "
        "now, and can't ___ yet.",
        "You're a test engineer. Give me a 5-item list of \"how to break "
        "or fail it,\"",
        "specific to how I operate it and what I watch for.",
    ], size=10, line_spacing=1.3)
    yellow_box(s, 0.62, 2.58, 8.76, 0.58, [
        "List in hand — PICK 2 ITEMS AND TEST THEM FOR REAL. Record pass / "
        "broke in your review record."], size=11.5)
    add_card(s, 0.62, 3.28, 8.76, 1.60, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.84, 3.40, 8.32, 1.38, [
        ("Quinn is the BMAD team's test engineer — this conversation needs "
         "the team in it.", {"size": 10.5, "bold": True}),
        ("Ran continuously since Lesson 4 → send it directly. Fresh window "
         "→ send this background line FIRST, then the prompt above:",
         {"size": 10}),
        ("This conversation has a BMAD team: John (PM), Sally (UX "
         "designer), Winston (architect), Amelia (developer), Quinn (test "
         "engineer).", {"size": 9.5, "mono": True}),
        ("Remember them — I'll call on them directly from now on.",
         {"size": 9.5, "mono": True}),
    ], line_spacing=1.25)
    set_notes(s, "Quinn, same deal. List in hand — pick 2 items and test "
                 "them for real. Don't be polite — it's built to be used the "
                 "wrong way. Record the results in the review record in your "
                 "workbook. One reminder: Quinn is the BMAD team's test "
                 "engineer — this conversation window needs the team in it "
                 "for Quinn to appear. Projects running since Lesson 4's "
                 "team build can send it directly; a fresh conversation "
                 "sends the background line first (the small print on "
                 "screen), then the prompt. Verify Quinn's entrance "
                 "condition in a fresh window during rehearsal (Section "
                 "1.3) — what happens calling Quinn with no background vs. "
                 "with the background sentence; mention this contrast in "
                 "one line in class. Offline → human peer review instead "
                 "(the same 3-faults-5-items frame, executed by the "
                 "neighbor, swapped) — the review is never canceled, only "
                 "its executor changes (instructor-side, never on screen). "
                 "Stand-still. The prompt box is 6.3 verbatim and the "
                 "entrance line is 6.3's small print — shared text; any edit "
                 "must sync all three documents.")
    return s


def slide_15(prs):
    s = page(prs, 15)
    add_title_bar(s, "Decide — Accept or Reject")
    add_subtitle(s, "both need a reason", y=1.00, size=13)
    add_card(s, 0.62, 1.48, 4.28, 1.60, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.80, 1.62, 3.92, 1.36, [
        ("ACCEPT", {"size": 13.5, "bold": True}),
        ("fix it now if it's under 5 minutes; can't finish? → the baton "
         "sheet, under \"first thing next leg\"", {"size": 10.5}),
    ], line_spacing=1.3)
    add_card(s, 5.10, 1.48, 4.28, 1.60, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 5.28, 1.62, 3.92, 1.36, [
        ("REJECT", {"size": 13.5, "bold": True}),
        ("write the reason — rejecting with a reason scores the same as "
         "accepting", {"size": 10.5}),
    ], line_spacing=1.3)
    add_rect(s, 0.62, 3.30, 0.07, 0.62, fill=YELLOW, border=None)
    add_text(s, 0.88, 3.32, 8.50, 0.58,
             "\"First thing next leg\" is not \"later\" — it's the FIRST "
             "action of next leg's build time.", size=11, bold=True)
    red_multiline(s, 4.10, [
        ("ACCEPT EVERYTHING? I'M COMING TO TALK TO YOU —",
         {"size": 12.5, "bold": True, "color": RED}),
        ("NO BACKBONE IS MORE DANGEROUS THAN NO CHANGES",
         {"size": 12.5, "bold": True, "color": RED}),
    ], size=12.5, h=0.64)
    set_notes(s, "Old rule, item by item: Accept or Reject — and both need "
                 "a reason. One reminder: rejecting with a reason scores "
                 "the same as accepting — but if you accept everything, "
                 "I'm coming to talk to you (no backbone is more dangerous "
                 "than no changes). Accepted and fixable now — fix it "
                 "(anything under 5 minutes). Can't finish? Into the handoff "
                 "sheet under 'first thing next leg' — not 'later,' the "
                 "first action of next leg's build time. The red line is "
                 "the deck's fourth red — the decision discipline. "
                 "Accept-everything → 30-second one-on-one: 'Eight items "
                 "all in? Can you even finish them? Take the 3 most "
                 "important; reject the rest — rejecting is a professional "
                 "decision too.' The sheet's 'first thing next leg' says "
                 "'keep going' → send it back: 'Write it as a verifiable "
                 "action — make ___ work even when ___.' Fixable-now items "
                 "stay under 5 minutes; anything bigger goes to the handoff "
                 "sheet — the review's decisions move the project, not "
                 "stall it.")
    return s


def slide_16(prs):
    s = page(prs, 16)
    add_title_bar(s, "The Baton Handoff Sheet")
    add_subtitle(s, "your marathon baton", y=1.00, size=13)
    grey_box(s, 0.62, 1.42, 8.76, 2.10, [
        "# Baton Handoff Sheet · Leg 1",
        "Name: ______  Date: ______",
        "## Where this leg ended (one verifiable sentence: what it can demo)",
        "## The review fault that matters most + my decision "
        "(accept/reject + reason)",
        "## The first thing next leg (specific, verifiable)",
    ], size=10.5, line_spacing=1.35)
    yellow_box(s, 0.62, 3.66, 8.76, 0.76, [
        "Into your workbook. Walk into Lesson 9 — this is how you find "
        "today's feeling again. It's also the comeback anchor for anyone "
        "who missed class."], size=11)
    yellow_box(s, 0.62, 4.48, 8.76, 0.74, [
        "Today's \"done\" line —",
        "MY PROJECT'S FIRST VERSION CAN ___; THE REVIEW PICKED ___ FAULTS; "
        "I ACCEPTED ___ AND REJECTED ___."], size=11)
    set_notes(s, "Fill the baton handoff sheet (template on screen, into "
                 "your workbook). It's your marathon baton — the moment you "
                 "walk into Lesson 9, it's how you find today's feeling "
                 "again. It's also the comeback anchor for anyone who missed "
                 "class. Log finish: four-line template; 'done' reads as on "
                 "screen. The template is 6.4 verbatim — identical to the "
                 "workbook; any edit must sync all three documents. "
                 "Stand-still while students fill.")
    return s


def slide_17(prs):
    s = page(prs, 17)
    add_title_bar(s, "Today, You Ran a Whole Lap")
    review = [
        "From a requirements sheet, you made a DEMONSTRABLE FIRST VERSION — "
        "it really sensed something, it really reacted",
        "You took a full round of faults from two judges — and you're still "
        "standing",
        "You made Accept-or-Reject calls with reasons — and you know the "
        "first thing next leg",
    ]
    ry = 1.05
    for r in review:
        check_item(s, 0.62, ry, 8.76, r, size=11, h=0.44)
        ry += 0.52
    yellow_box(s, 0.62, 2.70, 8.76, 0.90, [
        "NEXT TIME — the marathon's second leg: BOTH HOMES AT ONCE (aily + "
        "the web version), and your project grows new abilities. Bring your "
        "baton handoff sheet and your two-views cheat sheet."], size=11)
    add_text(s, 0.62, 3.72, 8.76, 0.55,
             "Return modules you're not using; main kits in the box; the "
             "Brief Wall stickies stay.", size=11, align=PP_ALIGN.CENTER)
    set_notes(s, "Look back at this leg — three things done. One: from a "
                 "requirements sheet, you made a demonstrable first version "
                 "— it really sensed something, it really reacted. Two: you "
                 "took a full round of faults from two judges, and you're "
                 "still standing. Three: you made Accept-or-Reject calls "
                 "with reasons, and you know the first thing next leg. "
                 "That's one complete engineer's iteration — today, you "
                 "really ran a whole lap. Next session preview: the "
                 "marathon's second leg — both homes at once (aily and the "
                 "web version), and your project grows new abilities. Bring "
                 "your baton handoff sheet and your two-views cheat sheet. "
                 "Return modules you're not using; main kits in the box; "
                 "the Brief Wall stickies stay. This page is the second "
                 "golden-line peak (same register as slide 02) — it closes "
                 "the arc and previews the second leg; no ability-card "
                 "ceremony today.")
    return s


# ---------------------------------------------------------- Brandy appendix

def appendix_page(prs, n, title, subtitle, bullets, photo=None, photo_label="photo"):
    s = page(prs, n)
    add_title_bar(s, title)
    if subtitle:
        add_subtitle(s, subtitle, y=1.00, size=12)
    # bullets card
    if bullets:
        h = 0.50 + len(bullets) * 0.34
        y = 1.50 if subtitle else 1.40
        add_card(s, 0.62, y, 8.76, min(h, 2.50), fill=WHITE, border=INK,
                 border_w=1.5)
        cy = y + 0.14
        for b in bullets:
            check_item(s, 0.82, cy, 8.30, b, size=10.5, h=0.28)
            cy += 0.34
    # optional photo
    if photo:
        py = 4.10 if bullets else 2.40
        add_photo_or_placeholder(s, photo, 2.20, py, 5.60, 1.20, photo_label)
    set_notes(s, f"Brandy appendix slide {n}: {title}. Flexible use — pick "
                 "pages if time remains, or a full walkthrough after class. "
                 "See Teacher's Guide Section 6 for script.")
    return s


APPENDIX_PAGES = [
    # (n, title, subtitle, bullets, photo, photo_label)
    (18, "Who Is Brandy?", "Seeed's application engineer",
     ["Built a voice keyboard with zero code.",
      "Her method: one closed loop at a time, with an acceptance test.",
      "The appendix walks her two projects end to end."], None, None),
    (19, "Look Beyond the Finished Product", None,
     ["The polished keyboard is the LAST frame, not the first.",
      "The real story is what the first frame looked like: one key.",
      "Every finished thing you admire started embarrassingly small."],
     BRANDY_KBD, "finished voice keyboard"),
    (20, "The Big-Picture Before / After", None,
     ["Before: talking into a computer and typing it out by hand.",
      "After: one button press turns speech into text.",
      "The gap is closed by a chain of tiny, tested loops."],
     BRANDY_INTERACT, "keyboard in use"),
    (21, "90% of Attention Interrupted", None,
     ["Switching windows costs more than you think.",
      "A physical button keeps your eyes on the work that matters.",
      "Good tools remove friction, not add features."], None, None),
    (22, "Two Devices, One Method", None,
     ["Voice keyboard: press → hear → text appears.",
      "Digital hourglass: tilt → sand falls → time shows.",
      "Both start with ONE loop, then grow."],
     BRANDY_HOURGLASS, "digital hourglass final"),
    (23, "Where to Start", None,
     ["Don't start with the final enclosure.",
      "Start with the riskiest part: does the input become an output?",
      "Everything else is decoration until that loop works."],
     BRANDY_SINGLE, "one-key first version"),
    (24, "The Method Overview", "four tools",
     ["Input / output contract — write what goes in and what must come out.",
      "One-key first loop — prove the hardest part first.",
      "AI as teammate — generate, fix, explain code one step at a time.",
      "Acceptance test — state what 'good enough' looks like."], None, None),
    (25, "A Live Mini-Exercise", "try it now",
     ["Name one thing you use every day that has ONE button.",
      "What is its input? What is its output?",
      "That's an I/O contract — and you already understand it."], None, None),
    (26, "The Voice Keyboard", "breaking the problem",
     ["Input: press and hold a button while speaking.",
      "Process: turn speech into text.",
      "Output: paste the text where the cursor is."],
     BRANDY_KBD, "keyboard hardware"),
    (27, "The Voice Keyboard", "mind map",
     ["Hardware: button, microphone, microcontroller.",
      "Software: speech-to-text service, hotkey simulation.",
      "Experience: one press, one sentence, one less context switch."],
     None, None),
    (28, "The Voice Keyboard", "I/O contract",
     ["INPUT: button press + voice.",
      "CONSTRAINTS: hold while talking, release to send.",
      "OUTPUT: text pasted at cursor.",
      "SUCCESS: 20 presses in a row, zero misses."], None, None),
    (29, "The Voice Keyboard", "the one-key first loop",
     ["Version 1 had exactly one key.",
      "The acceptance test was brutal: 20 presses, no misses.",
      "Only after passing did she add key 2, 3, 4, 5."],
     BRANDY_SINGLE, "one-key version"),
    (30, "The Voice Keyboard", "final interaction",
     ["Five keys now: input, end, send, delete, and a custom shortcut.",
      "Each key grew from a loop that was proven first.",
      "The form followed the function."],
     BRANDY_INTERACT, "keyboard interaction labels"),
    (31, "The Voice Keyboard", "enclosure pitfalls",
     ["3D prints warp; keycaps wobble; USB cables snag.",
      "Every enclosure problem was found by using it, not imagining it.",
      "Test the loop first; the box comes last."], None, None),
    (32, "The Voice Keyboard", "sketch to 3D",
     ["A paper sketch is faster than any CAD tool at the start.",
      "Only lock dimensions after the electronics fit in your hand.",
      "Draw → measure → print → test → redraw."], None, None),
    (33, "The Voice Keyboard", "demo checklist",
     ["Power on, connect, press button, speak a sentence, text appears.",
      "Repeat three times without failure.",
      "This same checklist protects your Lesson 10 showcase."],
     BRANDY_KBD, "keyboard ready for demo"),
    (34, "The Digital Hourglass", "breaking the problem",
     ["Input: tilt the device to start a timer.",
      "Process: count down like falling sand.",
      "Output: LEDs show remaining time."],
     BRANDY_HOURGLASS, "hourglass final"),
    (35, "The Digital Hourglass", "wiring & SOP",
     ["One microcontroller, one accelerometer, one LED matrix.",
      "Standard operating procedure: tilt → start, flat → pause, upright "
      "→ reset.",
      "The behavior was decided before the code was written."],
     None, None),
    (36, "The Digital Hourglass", "decomposing \"like sand\"",
     ["Sand doesn't fall as a block; it falls grain by grain.",
      "An LED matrix can mimic that with small steps.",
      "Break the effect into tiny frames, then loop them."],
     BRANDY_HOURGLASS, "hourglass close-up"),
    (37, "The Digital Hourglass", "the photo where the logic was wrong",
     ["A wrong photo is evidence, not failure.",
      "It tells you which assumption broke — light? angle? timing?",
      "Fix the data, fix the logic, or fix the threshold."], None, None),
    (38, "Two Key Translations", None,
     ["Translation 1: user words → engineering requirements.",
      "Translation 2: engineering requirements → a closed loop.",
      "If you can do both, you can make anything."], None, None),
    (39, "A Reusable Hardware Prompt", "photograph this page",
     ["\"I have a ___ module. What does it sense or do? Which pin is "
      "which?\"",
      "Use it whenever you meet a new module in Lesson 9.",
      "The prompt lives in your workbook too."], None, None),
    (40, "The Five-Step Loop", None,
     ["Say the need in plain language.",
      "Write the input / output / success contract.",
      "Build the smallest closed loop.",
      "Test it with a real failure scenario.",
      "Decide: accept, reject, or make it smaller."], None, None),
    (41, "Closing on the Four-Line Spec", None,
     ["Every new module starts with four lines:",
      "INPUT → CONSTRAINTS → OUTPUT → SUCCESS CRITERIA.",
      "That's the Brandy method. That's your method now."], None, None),
    (42, "Your Turn", "next leg and beyond",
     ["Bring a new module into your project in Lesson 9.",
      "Run it through the same four-line spec first.",
      "Minimal, closed, tested — then grow."], None, None),
]


def build_appendix(prs):
    for n, title, subtitle, bullets, photo, label in APPENDIX_PAGES:
        appendix_page(prs, n, title, subtitle, bullets, photo, label)


def main():
    prs = new_deck()
    for f in (slide_01, slide_02, slide_03, slide_04, slide_05, slide_06,
              slide_07, slide_08, slide_09, slide_10, slide_11, slide_12,
              slide_13, slide_14, slide_15, slide_16, slide_17):
        f(prs)
    build_appendix(prs)
    prs.save(OUT)
    print(f"Saved: {OUT} slides: {len(prs.slides._sldIdLst)}")


if __name__ == "__main__":
    main()
