"""
Build the English Lesson 6 deck (Move Your Project Home, 20 slides)
from M0_EN_PPTPlan_CFG-6_Lesson06_MoveYourProjectHome_v1.md (brand rebuild).

Output: 交付物_EN/03_Deliverables/PPTX/M0_EN_Deck_CFG-5_Lesson06_MoveYourProjectHome_v1.pptx
Layout per chaihuo-ppt-brand.md: white 70 / yellow 15 / ink 10 / red 5, 960x540.
Red budget: slide 03 (14:18 checkpoint red line) + slide 10 (quotes-and-brackets
boundary). All other warnings are bold black on yellow. No CJK / emoji on
screen; full-width bars replaced with ASCII. Board-picker screenshot is the
real user-provided capture (English UI).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder_lib import *
from pptx.util import Inches
from pptx.enum.text import MSO_ANCHOR

TOTAL = 20
DECK_LABEL = "Move Your Project Home"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson06_MoveYourProjectHome_v1.pptx")
PICKER = ("/Users/leonfeng/Baiduyun/M0/M0-V2/旧版与中间件_归档/素材_原始输入/"
          "screenshot-20260803-154849.png")


def page(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(s)
    add_footer(s, n, TOTAL, DECK_LABEL)
    return s


def num_block(s, x, y, num, size=0.42):
    add_rect(s, x, y, size, size, fill=YELLOW, border=None)
    add_text(s, x, y + 0.04, size, 0.34, num, size=15, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER)


def yellow_box(s, x, y, w, h, lines, title=None, size=13, title_size=15,
               line_spacing=1.25):
    add_rect(s, x, y, w, h, fill=YELLOW, border=None)
    tx, ty = x + 0.18, y + 0.12
    tw, th = w - 0.36, h - 0.24
    if title:
        add_text(s, tx, ty, tw, 0.32, title, size=title_size, bold=True)
        add_multiline(s, tx, ty + 0.36, tw, th - 0.4, lines, size=size,
                      line_spacing=line_spacing)
    else:
        add_multiline(s, tx, ty, tw, th, lines, size=size,
                      line_spacing=line_spacing)


def grey_card(s, x, y, w, h):
    add_card(s, x, y, w, h, fill=CODEBG, border=INK, border_w=1.0)


def check_item(s, x, y, w, text, size=14):
    add_rect(s, x, y + 0.05, 0.22, 0.22, fill=YELLOW, border=None)
    add_text(s, x + 0.38, y, w - 0.38, 0.32, text, size=size)


def main():
    prs = new_deck()

    # ---------------------------------------------------------------- 01 cover
    s = page(prs, 1)
    add_text(s, 0.62, 1.20, 6.4, 0.3,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0)",
             size=13)
    add_text(s, 0.62, 1.55, 8.76, 0.75, "Move Your Project Home", size=38,
             bold=True)
    add_rect(s, 0.62, 2.50, 1.6, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 2.68, 6.2, 0.6,
             "The Big Move: from the Web into Your Own Computer · Chaihuo "
             "Maker Academy · M0 Lesson 6", size=14, line_spacing=1.2)
    add_text(s, 0.62, 3.45, 6.2, 0.35, "Lesson 6 · From Tenant to Owner",
             size=17, bold=True)
    add_text(s, 0.62, 3.90, 6.2, 0.55,
             "New tool: aily-blockly — the open-source hardware dev "
             "environment that lives on your computer", size=12.5,
             line_spacing=1.2)
    add_card(s, 7.0, 3.30, 2.36, 1.5, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 7.1, 3.55, 2.16, 0.9,
             "[ aily-blockly blocks view — screenshot at rehearsal ]", size=9,
             mono=True, align=PP_ALIGN.CENTER, line_spacing=1.2)
    add_text(s, 7.0, 4.88, 2.36, 0.2, "the new house", size=9.5,
             align=PP_ALIGN.CENTER)
    set_notes(s, "Cover page only; students see it as they sit down. No "
                 "script. When the session starts, go straight to slide 02 — "
                 "the opener's 30-second look-back is spoken, not projected. "
                 "Right side: aily-blockly blocks-view screenshot (an open "
                 "project) + a small XIAO board photo ('the new house') — "
                 "placeholder card until the rehearsal capture; yellow rule "
                 "under the subtitle.")

    # ---------------------------------------------------------------- 02 tenant
    s = page(prs, 2)
    add_title_bar(s, "Today We Don't Create. Today We Move.")
    add_card(s, 0.62, 1.30, 4.0, 1.55, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.78, 1.42, 3.68, 1.32, [
        ("OLD", {"size": 14, "bold": True}),
        ("lived on someone else's server; close the browser, it's gone",
         {"size": 11.5}),
    ], line_spacing=1.25)
    add_text(s, 4.68, 1.85, 0.7, 0.5, "→", size=28, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER)
    add_card(s, 5.44, 1.30, 4.0, 1.55, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 5.60, 1.42, 3.68, 1.32, [
        ("NEW", {"size": 14, "bold": True}),
        ("lives in MY computer — unplug the internet, it's there; shut down "
         "the website, it's there; ten years later, it's still there",
         {"size": 11.5}),
    ], line_spacing=1.25)
    add_golden_line(s, 0.62, 3.10, 8.76,
                    "Moving isn't a step back — it's buying the house.",
                    size=16, h=None)
    add_text(s, 0.62, 3.82, 8.76, 0.24, "TODAY'S FIVE STEPS", size=10.5,
             bold=True)
    steps5 = [
        (0.62, "checkpoint", False), (2.39, "tour the new home", False),
        (4.16, "unpack the old project", False),
        (5.93, "lift the floor", False),
        (7.70, "build something new with AI", True),
    ]
    for sx, txt, hi in steps5:
        add_card(s, sx, 4.12, 1.66, 0.95, fill=YELLOW if hi else WHITE,
                 border=INK, border_w=1.5)
        add_text(s, sx + 0.08, 4.12, 1.5, 0.95, txt, size=9.5,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                 line_spacing=1.15)
    set_notes(s, "30-second look-back: last session, you taught your hardware "
                 "to see — you ran a ready model, then trained a model that's "
                 "entirely yours. From Lesson 1 to now, your projects keep "
                 "coming, and they keep getting better. Then the close-the-tab "
                 "demo: today we don't create. Today we do one big thing: "
                 "until now, your projects have lived on someone else's server "
                 "— close the browser, and they're gone. Today, you move from "
                 "tenant to owner. (demo: close the Codecraft tab) See? "
                 "Closed. Where's your project? — At someone else's house. "
                 "(open a local folder) Now look here: after class today, your "
                 "project will live in this folder. Unplug the internet — "
                 "it's there. Shut down the website — it's there. Ten years "
                 "after graduation — it's still there. Moving isn't a step "
                 "back — it's buying the house. Then the five steps (point at "
                 "the screen) and the Lesson 7 hook: once the house is set up, "
                 "what's next? — Next session, you give your project a brief: "
                 "the topic grows out of your own experience, not copied from "
                 "the internet. Brief done, the marathon starts. 'Why move if "
                 "the web version works fine?' — the web version isn't "
                 "retiring; during the marathon you'll use both. But the "
                 "feeling of owning it — you have to taste that once today. "
                 "Flat energy — this is a celebration, not moving day: "
                 "over-act the opener.")

    # ---------------------------------------------------------------- 03 checkpoint (RED 1)
    s = page(prs, 3)
    add_title_bar(s, "Install Checkpoint — Three Checks")
    add_card(s, 0.62, 1.25, 8.76, 1.30, fill=WHITE, border=INK, border_w=1.5)
    cy_ = 1.38
    for t in ["It's installed", "It opens", "I can reach the main screen"]:
        check_item(s, 0.90, cy_, 8.2, t, size=14)
        cy_ += 0.38
    yellow_box(s, 0.62, 2.75, 8.76, 1.05, [
        "Not done? Share one computer with your neighbor — you're the "
        "COMMANDER: you say what to do, they press the buttons.",
        "Give your name to a TA — we'll get you set up within 10 minutes "
        "after class."], size=12.5)
    add_rect(s, 0.62, 4.05, 0.07, 0.85, fill=RED, border=None)
    add_oval(s, 0.86, 4.15, 0.12, fill=RED, border=None)
    add_text(s, 1.12, 4.10, 8.26, 0.32,
             "THE CHECKPOINT CLOSES AT 14:18 — NOT INSTALLED? PAIR UP ON THE "
             "SPOT.", size=15, bold=True, color=RED)
    add_text(s, 1.12, 4.48, 8.26, 0.28, "NO INSTALLING IN CLASS.", size=15,
             bold=True, color=RED)
    set_notes(s, "Finished your install homework? Open the tool, fill in the "
                 "self-test on screen (it's in your workbook too): three "
                 "checks — it's installed / it opens / I can reach the main "
                 "screen. Not done — raise your hand. No more installing now; "
                 "you pair up on the spot: share one computer with your "
                 "neighbor, you're the commander — you say what to do, they "
                 "press the buttons. Give your name to a TA; we'll make sure "
                 "you're set up within 10 minutes after class. More than 1/3 "
                 "not installed — the homework pipeline broke: extend this "
                 "block 5 minutes for a focused group install (all TAs on "
                 "it); whoever still isn't done pairs up; note it on the "
                 "reflection page. Installed but the board won't connect — "
                 "TA B handles one-on-one (cable, port, permission); not "
                 "fixed in 5 minutes — pair up. Whole-room permission block "
                 "(a night policy change) — execute the 4.1 downgrade. The "
                 "red line is the deck's first red — the 14:18 close is "
                 "today's iron law, never softened. No install steps ever "
                 "appear on this page.")

    # ---------------------------------------------------------------- 04 tool
    s = page(prs, 4)
    add_title_bar(s, "Your New Tool Is Called aily-blockly")
    add_text(s, 0.62, 1.10, 8.76, 0.28,
             "A hardware dev environment that lives on your computer — open "
             "source and free (GPL),", size=12.5)
    add_text(s, 0.62, 1.42, 8.76, 0.28,
             "by the aily Project · the site is yiyu.pro", size=12, mono=True)
    facts = [
        ("UNIVERSAL", "not some one-board companion app; 100+ development "
                      "boards fit here, and your future boards will too"),
        ("AI-NATIVE", "say what you need, get a wiring diagram, get code, "
                      "get errors fixed — AI is there the whole way"),
        ("MADE FOR BEGINNERS", "the official goal in one line: break the line "
                               "between professional and amateur — let "
                               "anyone make hardware with plain language"),
    ]
    for i, (head, body) in enumerate(facts):
        cx = 0.62 + i * 2.96
        add_card(s, cx, 1.90, 2.84, 2.10, fill=WHITE, border=INK,
                 border_w=1.5)
        add_text(s, cx + 0.15, 2.02, 2.54, 0.28, head, size=12.5, bold=True)
        add_text(s, cx + 0.15, 2.34, 2.54, 1.55, body, size=10.5,
                 line_spacing=1.2)
    yellow_box(s, 0.62, 4.22, 8.76, 0.60, [
        "The old home got you daring quickly; the new home gets you "
        "finishing properly."], size=13.5)
    set_notes(s, "Every house needs a name — this one is aily-blockly. Three "
                 "facts, and that's it. One: it's open source and free — the "
                 "site is yiyu.pro, anyone can install it. Two: it's "
                 "universal — not some one-board companion app; it takes 100+ "
                 "development boards, so when you change boards later, it's "
                 "still your home. Three: it's AI-native — say what you need, "
                 "get a wiring diagram, get code, get errors fixed — AI is "
                 "there the whole way. The third one matters most: the people "
                 "who built it set out to break the line between professional "
                 "and amateur — to let anyone make hardware with plain "
                 "language. It was built for you. The old home got you daring "
                 "quickly; the new home gets you finishing properly. Three "
                 "facts skimmed fast — the page is a name-introduction, not "
                 "a lecture.")

    # ---------------------------------------------------------------- 05 picker
    s = page(prs, 5)
    add_title_bar(s, "Look at the Real Thing — Pick Your Board")
    if os.path.exists(PICKER):
        s.shapes.add_picture(PICKER, Inches(2.2), Inches(1.10), Inches(5.6),
                             Inches(3.22))
    else:
        add_card(s, 2.2, 1.10, 5.6, 3.22, fill=CODEBG, border=INK,
                 border_w=1.5)
        add_text(s, 2.4, 2.5, 5.2, 0.4, "[ board-picker screenshot ]",
                 size=12, mono=True, align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 4.48, 8.76, 0.68, [
        "Grove Beginner Kit is in there — and so is Wio Terminal. That's "
        "what \"universal\" means.",
        "Whatever board you use next, it's got a place here."], size=12)
    set_notes(s, "Words are cheap — look at the real thing (point at the "
                 "screen). This is the first screen aily-blockly shows: pick "
                 "your board. Look for it: Grove Beginner Kit is in there — "
                 "and so is Wio Terminal. That's what 'universal' means. "
                 "Whatever board you use next, it's got a place here. "
                 "Screenshot = evidence — '100+ boards' isn't claimed, it's "
                 "shown. The screenshot is already English UI — no "
                 "localization needed.")

    # ---------------------------------------------------------------- 06 empty house
    s = page(prs, 6)
    add_title_bar(s, "Build Your First Empty House — Four Steps")
    steps4 = [
        ("1", "NEW PROJECT"),
        ("2", "PICK THE BOARD — today: WIO TERMINAL"),
        ("3", "NAME IT — use English"),
        ("4", "CREATE"),
    ]
    sy = 1.35
    for num, txt in steps4:
        num_block(s, 0.62, sy, num, size=0.4)
        if num == "3":
            add_text(s, 1.2, sy + 0.02, 5.3, 0.30, txt, size=14, bold=True)
            add_text(s, 1.2, sy + 0.32, 5.3, 0.24,
                     "point the save path at your projects folder", size=10.5)
        else:
            add_text(s, 1.2, sy + 0.02, 5.3, 0.32, txt, size=14, bold=True)
        sy += 0.58
    add_card(s, 6.7, 1.35, 2.68, 2.1, fill=CODEBG, border=INK, border_w=1.0)
    add_text(s, 6.85, 1.55, 2.38, 1.7,
             "[ four-step screenshots — captured on the teacher machine at "
             "rehearsal, English UI ]", size=9.5, mono=True,
             align=PP_ALIGN.CENTER, line_spacing=1.3)
    yellow_box(s, 0.62, 3.85, 8.76, 0.65, [
        "You're in the blocks screen — and the folder already has it."],
        size=13.5)
    set_notes(s, "Build-along — 'where I click, you click'. Intro done — time "
                 "to build your first empty house. Four steps: new project → "
                 "pick the board: today, Wio Terminal → name it: use English, "
                 "and point the save path at your projects folder → create. "
                 "The sign it worked: you're in the blocks screen, and the "
                 "folder already has it. Why the Wio today? — spoken, not on "
                 "screen: the Wio is the board we'll team up with this "
                 "afternoon — build its house first. Students follow on "
                 "their own machines; paired groups: the installed partner "
                 "operates, the other points and commands (commander mode "
                 "carries over). Can't find the project folder — whole-class "
                 "sync: 'Where I click, you click — found it? Hands up.' This "
                 "page is a V3 addition the CN v2 plan never had — the "
                 "build-along is part of the 12-minute 'meet the new home' "
                 "block, not a separate lesson.")

    # ---------------------------------------------------------------- 07 tour
    s = page(prs, 7)
    add_title_bar(s, "Tour the New House — Three Rooms")
    rooms = [
        ("YOUR PROJECTS' HOME", "this folder IS your project: copy it out "
                                "and it's portable, send it and it's shared"),
        ("THE BLOCKS VIEW", "drag and drop, the same graphical feel you "
                            "already know"),
        ("THE CODE VIEW", "what AI has been writing for you; we lift that "
                          "floor in a few minutes"),
    ]
    for i, (head, body) in enumerate(rooms):
        cx = 0.62 + i * 2.96
        add_card(s, cx, 1.30, 2.84, 1.70, fill=WHITE, border=INK, border_w=1.5)
        add_text(s, cx + 0.15, 1.44, 2.54, 0.5, head, size=11.5, bold=True,
                 line_spacing=1.1)
        add_text(s, cx + 0.15, 2.02, 2.54, 0.9, body, size=10.5,
                 line_spacing=1.2)
    grey_card(s, 0.62, 3.20, 8.76, 1.80)
    add_multiline(s, 0.80, 3.32, 8.40, 1.56, [
        ("Whatever buttons there are, remember two today",
         {"size": 12.5, "bold": True}),
        ("1 · AI CODING — tell it what you need in plain language; it writes "
         "code and fixes errors (today runs on it)", {"size": 10.5}),
        ("2 · FLASH — click, and the program goes into the board (know what "
         "the \"upload\" button looks like)", {"size": 10.5}),
        ("Every other button — ask AI when you need it. It knows them better "
         "than you.", {"size": 10.5}),
    ], line_spacing=1.2)
    set_notes(s, "Tour the new house — three rooms. First room (open the file "
                 "manager): this is where your projects live from now on. "
                 "This folder is your project — copy it out and it's "
                 "portable, send it and it's shared. Second room (back to the "
                 "tool): this is the blocks view — drag and drop, same "
                 "graphical feel you already know. Third room (click the code "
                 "view): this is the code view — one of today's main courses; "
                 "we lift that floor in a few minutes. Whatever buttons there "
                 "are, remember just two today. One: AI coding — tell it what "
                 "you need in plain language, it writes your code and fixes "
                 "your errors; today runs on it. Two: flash — click, and the "
                 "program goes into the board; know what the 'upload' button "
                 "looks like. Every other button — ask AI when you need it. "
                 "It knows them better than you. Students point to where 'AI "
                 "coding' and 'flash (upload)' live in the interface (the "
                 "'did it land' check). Stand-still during the tour. The "
                 "two-buttons box is 6.2 verbatim — shared text with the "
                 "Teacher's Guide and the workbook; any later edit must "
                 "sync all three.")

    # ---------------------------------------------------------------- 08 unpack
    s = page(prs, 8)
    add_title_bar(s, "Unpack Your Most Precious Thing")
    add_subtitle(s, "your very first project", y=1.00, size=13)
    add_card(s, 0.62, 1.40, 8.76, 1.15, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.80, 1.50, 8.40, 0.95, [
        ("Redo \"show your name on screen\" in the new tool.",
         {"size": 12.5, "bold": True}),
        ("Lesson 1: how long did it take you? I bet you finish in HALF the "
         "time today.", {"size": 12.5}),
        ("This isn't repetition — it's watching yourself grow in real time.",
         {"size": 12.5}),
    ], line_spacing=1.3)
    yellow_box(s, 0.62, 2.72, 8.76, 0.55, [
        "Lesson 1: ___ min   →   today: ___ min"], size=16)
    add_text(s, 0.62, 3.50, 8.76, 0.24, "THE OWNERSHIP RITUAL", size=10.5,
             bold=True)
    ritual = ["SAVE", "OPEN THE FOLDER", "SEE IT WITH YOUR OWN EYES"]
    for i, txt in enumerate(ritual):
        rx = 0.62 + i * 3.03
        add_card(s, rx, 3.80, 2.70, 0.60, fill=WHITE, border=INK,
                 border_w=1.5)
        add_text(s, rx, 3.80, 2.70, 0.60, txt, size=12, bold=True,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < 2:
            add_text(s, rx + 2.70, 3.80, 0.33, 0.60, "→", size=16, bold=True,
                     color=YELLOW, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, wrap=False)
    add_text(s, 0.62, 4.55, 8.76, 0.28,
             "From today, every project you make takes this step.", size=12,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 4.95, 8.76, 0.24,
             "Write your two times in the workbook — Lesson 1 vs today.",
             size=10.5)
    set_notes(s, "First thing after moving in: put out your most precious old "
                 "thing — your very first project: showing your name on "
                 "screen. Don't roll your eyes. In Lesson 1, how long did it "
                 "take you? (wait for answers) Timer starts now — I bet you "
                 "finish in half the time. This isn't repetition; it's "
                 "watching yourself grow in real time. The one step that "
                 "matters most when you're done: save, then open the folder "
                 "and see it with your own eyes. That ritual has a name — the "
                 "ownership ritual. From today, every project you make takes "
                 "this step. Redo = AI-coding entry + the flash five-step "
                 "(rule: pick the right port first, then click upload). "
                 "'This is boring' — the frame is built in; still resisting "
                 "— let them redo any old project — but the ownership ritual "
                 "is never skipped; fast students go straight into the "
                 "night-light block (give them the 6.4 prompt early). Paired "
                 "groups — both students must do the save→folder→confirm run "
                 "themselves (acceptance: each partner operates "
                 "independently).")

    # ---------------------------------------------------------------- 09 two views
    s = page(prs, 9)
    add_title_bar(s, "What AI Has Been Writing for You All Along")
    add_card(s, 0.62, 1.45, 3.60, 1.85, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 1.80, 3.24, 0.9,
             "[ blocks view — one block, enlarged ]", size=10, mono=True,
             align=PP_ALIGN.CENTER, line_spacing=1.3)
    add_text(s, 0.80, 2.75, 3.24, 0.3, "BLOCKS", size=10.5, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 4.40, 2.05, 1.2, 0.65, "⇄", size=40, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER, wrap=False)
    add_card(s, 5.76, 1.45, 3.62, 1.85, fill=CODEBG, border=INK, border_w=1.5)
    add_text(s, 5.94, 1.80, 3.26, 0.9,
             "[ code view — the matching lines ]", size=10, mono=True,
             align=PP_ALIGN.CENTER, line_spacing=1.3)
    add_text(s, 5.94, 2.75, 3.26, 0.3, "CODE", size=10.5, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.48, 8.76, 0.35, "ONE BLOCK  ⇄  A FEW LINES OF CODE",
             size=16, bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.88, 8.76, 0.28,
             "\"two looks at the same project\"", size=12,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 4.20, 8.76, 0.28,
             "Blocks are for hands  |  Code is for machines", size=13,
             align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 4.55, 8.76, 0.68, [
        "You don't need to read it all — today is about one feeling: CODE IS "
        "NOT MYSTERIOUS. Find one match, and you graduate."], size=11.5)
    set_notes(s, "All eyes on the big screen. I'm lifting the floor. (switch "
                 "to code view) This is what AI has been writing for you all "
                 "along. From the first time you said 'show my name on "
                 "screen,' it has been writing this every time. Today, we "
                 "look at what it looks like. Then one correspondence: look "
                 "at this pair — this one block is these few lines. Blocks "
                 "and code are two looks at the same project — blocks are for "
                 "hands, code is for machines. You don't need to read it all "
                 "— today is about one feeling: code is not mysterious. Find "
                 "one match, and you graduate. This is the visual-contrast "
                 "peak of the lesson — the code's first full-screen "
                 "appearance. A student scared off by the code — 'You don't "
                 "need to read it all — one match and you graduate' (step one "
                 "only; steps two and three optional). The page stays "
                 "minimal — no task list, no code box; the contrast image "
                 "carries it. [Asset: block ⇄ code side-by-side screenshot — "
                 "captured on the teacher machine at rehearsal; live "
                 "'drag a block and point' is the static base's stand-in]")

    # ---------------------------------------------------------------- 10 three steps (RED 2)
    s = page(prs, 10)
    add_title_bar(s, "Three Steps — Follow Me, Then Walk Alone")
    add_card(s, 0.62, 1.10, 8.76, 0.80, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 1.16, 8.40, 0.24, "STEP 1 · FIND THE MATCH", size=12,
             bold=True)
    add_text(s, 0.80, 1.42, 8.40, 0.44,
             "Back to the blocks view, drag one block — watch what changed "
             "over here in the code. One \"this block = these lines\" — you "
             "graduate.", size=10.5, line_spacing=1.15)
    add_card(s, 0.62, 1.98, 8.76, 0.80, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 2.04, 8.40, 0.24, "STEP 2 · ASK AI", size=12, bold=True)
    add_text(s, 0.80, 2.30, 8.40, 0.44,
             "Select a chunk you don't understand, send it to your AI. From "
             "today, AI has a new job: not just doing the work for you — "
             "teaching you to read it.", size=10.5, line_spacing=1.15)
    grey_card(s, 0.62, 2.86, 8.76, 0.60)
    add_multiline(s, 0.80, 2.92, 8.40, 0.48, [
        ("(select a code chunk, send in the conversation you already have)",
         {"size": 10, "mono": True}),
        ("What's this code doing? Explain in plain language I can understand "
         "— two or three sentences max.", {"size": 10, "mono": True}),
    ], line_spacing=1.2)
    add_card(s, 0.62, 3.54, 8.76, 0.62, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 3.60, 8.40, 0.24, "STEP 3 · CHANGE ONE LINE", size=12,
             bold=True)
    add_text(s, 0.80, 3.86, 8.40, 0.28,
             "Find the line that shows your name — change only the letters "
             "inside the quotes to your nickname. Run it.", size=10.5)
    add_text(s, 0.62, 4.22, 8.76, 0.22,
             "Ask in the conversation you already have — no new windows. It "
             "knows your project, so its answers fit your code.", size=10)
    add_text(s, 0.62, 4.46, 8.76, 0.22,
             "Write in your workbook — the two-views cheat sheet: one block "
             "= which lines?", size=10)
    add_rect(s, 0.62, 4.74, 0.07, 0.50, fill=RED, border=None)
    add_oval(s, 0.86, 4.80, 0.12, fill=RED, border=None)
    add_text(s, 1.12, 4.76, 8.26, 0.26,
             "CHANGE ONLY THE LETTERS INSIDE THE QUOTES — DON'T TOUCH THE "
             "QUOTES OR BRACKETS", size=12.5, bold=True, color=RED)
    add_text(s, 1.12, 5.02, 8.26, 0.20,
             "(broke it? go back to the last version — that's why engineers "
             "save constantly)", size=9.5)
    set_notes(s, "Three steps, follow me. Step one: find the match. Go back "
                 "to the blocks view, drag one block — watch: what changed "
                 "over here in the code? (wait for someone to point) Right — "
                 "this one block is these few lines. Step two: ask AI. Select "
                 "a chunk of code you don't understand, send it to your AI "
                 "(project the prompt): 'What's this code doing?' Have it "
                 "explain in plain language. From today, AI has a new job: "
                 "not just doing the work for you — teaching you to read it. "
                 "Old rule: ask in the conversation you already have. No new "
                 "windows. Step three: change one line. Find the line that "
                 "shows your name — change only the letters inside the quotes "
                 "to your nickname. Run it. (wait) See that? You just touched "
                 "code with your own hands — and you didn't break it. "
                 "Changing a letter can't break it. That's your first time. "
                 "The red line is the deck's second red — the boundary of the "
                 "first-ever hand-touch of code. They break a line (deleted a "
                 "quote or bracket) — teach the save, on the spot: no panic — "
                 "go back to the last version. See? This is why engineers "
                 "save constantly. Someone wants to change logic (numbers, "
                 "conditions) — 'Today, letters only. The fire to change "
                 "logic — hold it until the marathon starts, when you have "
                 "your requirements sheet.' New window opened — point at the "
                 "reminder line. Stand-still during the students' solo walk; "
                 "the instructor circulates.")

    # ---------------------------------------------------------------- 11 three layers
    s = page(prs, 11)
    add_title_bar(s, "Why Did You Just Do All This?")
    add_golden_line(s, 0.62, 1.55, 8.76, "It's yours.", size=32, h=0.62)
    add_golden_line(s, 0.62, 2.35, 8.76, "You're not afraid of it.", size=32,
                    h=0.62)
    add_golden_line(s, 0.62, 3.15, 8.76, "The door opened.", size=32, h=0.62)
    yellow_box(s, 0.62, 4.20, 8.76, 0.75, [
        "Just now you READ what AI wrote.",
        "Next, you'll DIRECT AI to write something brand new."], size=14)
    set_notes(s, "One point, then we move: why did you just do all this? "
                 "Three reasons — it's yours (your project, your folder, your "
                 "house); you're not afraid of it (from black box to clear "
                 "box); the door opened (competitions, final projects, the "
                 "real engineer's world — this is where you walk in). The "
                 "door's open — now step through it. Just now you read what "
                 "AI wrote. Next, you'll direct AI to write something brand "
                 "new. No code box, no task list — the page is deliberately "
                 "set apart from the operation pages (same energy as slide "
                 "02).")

    # ---------------------------------------------------------------- 12 loop
    s = page(prs, 12)
    add_title_bar(s, "The Engineer's Loop")
    add_subtitle(s, "every lap of the marathon runs it", y=1.00, size=13)
    stations = ["say it", "AI builds", "check", "upload", "verify"]
    for i, st in enumerate(stations):
        sx = 0.62 + i * 1.72
        add_card(s, sx, 1.40, 1.5, 0.62, fill=WHITE, border=INK, border_w=1.5)
        add_text(s, sx, 1.40, 1.5, 0.62, st, size=12, bold=True,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < 4:
            add_text(s, sx + 1.5, 1.40, 0.22, 0.62, "→", size=15, bold=True,
                     color=YELLOW, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, wrap=False)
    add_rect(s, 0.90, 2.22, 7.70, 0.02, fill=INK, border=None)
    add_text(s, 0.62, 2.28, 8.76, 0.24,
             "wrong? say the need more clearly, run another lap", size=10.5,
             align=PP_ALIGN.CENTER)
    boxes3 = ["what it senses (input)",
              "what it does under what condition (logic)",
              "how it shows itself (output)"]
    for i, b in enumerate(boxes3):
        bx = 0.62 + i * 2.96
        add_card(s, bx, 2.66, 2.84, 0.55, fill=WHITE, border=INK,
                 border_w=1.5)
        add_text(s, bx, 2.66, 2.84, 0.55, b, size=11.5, bold=True,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    yellow_box(s, 0.62, 3.36, 8.76, 1.50, [
        ("Today's first new project: THE NIGHT-LIGHT — Grove Beginner Kit,",
         {"size": 12.5, "bold": True}),
        ("light sensor + LED built into the board, NOT A SINGLE WIRE to "
         "connect — short code, fast upload, verdict in two minutes.",
         {"size": 11.5}),
        ("Leave the number in brackets blank — you'll read the real value on "
         "the serial monitor and fill it in yourself.", {"size": 10.5}),
    ], line_spacing=1.2)
    set_notes(s, "Engineers working in a local tool run on this loop (point, "
                 "read the five stations): say it → AI builds → check → "
                 "upload → verify. Verification fails? Back to the first "
                 "station — say the need more clearly, run another lap. This "
                 "loop is the motion of every lap of the marathon — today we "
                 "get fluent on a small project. How do you say a need "
                 "clearly? You already know — the three boxes: what it "
                 "senses (input), what it does under what condition (logic), "
                 "how it shows itself (output). The first new project: the "
                 "night-light. Uses the Grove Beginner Kit in your hand — "
                 "light sensor and LED are built into the board, not a "
                 "single wire to connect, short code, fast upload, verdict "
                 "in two minutes. Dark — light on. Bright — light off. Use "
                 "the prompt on screen; leave the number in brackets blank — "
                 "what the sensor actually reads, you'll see on the serial "
                 "monitor in a moment, and fill in yourself. Then cut to "
                 "slide 14 to hand out the 6.4 prompt (3 min), then to slide "
                 "13 as the solo base. The loop diagram returns on demand "
                 "when a student asks 'what do I do next?' — the loop is the "
                 "map.")

    # ---------------------------------------------------------------- 13 solo
    s = page(prs, 13)
    add_title_bar(s, "Today's Four Steps — Run Solo")
    add_subtitle(s, "from your workbook", y=1.00, size=13)
    add_card(s, 0.62, 1.30, 8.76, 2.20, fill=WHITE, border=INK, border_w=1.5)
    solo_rows = [
        (1.42, "1", "Send the 6.4 prompt with your need → read what AI "
                     "explains first; point to the light sensor and LED on "
                     "your board before you build", 0.52),
        (2.02, "2", "Build + upload (paste errors back verbatim, one step "
                     "at a time)", 0.32),
        (2.42, "3", "Open the serial monitor: normal ___ / hand over it ___ "
                     "→ put the threshold back into your need, have AI use "
                     "your number", 0.52),
        (3.02, "4", "Iterate one lap: change the threshold / add \"when "
                     "dark, the buzzer also beeps\" (pick one)", 0.36),
    ]
    for ry, num, txt, rh in solo_rows:
        num_block(s, 0.80, ry, num, size=0.32)
        add_text(s, 1.26, ry - 0.02, 7.9, rh, txt, size=11,
                 line_spacing=1.15)
    yellow_box(s, 0.62, 3.65, 8.76, 0.58, [
        "Paste errors back verbatim — one step at a time. Don't guess and "
        "fiddle on your own."], size=12.5)
    yellow_box(s, 0.62, 4.32, 8.76, 0.68, [
        "Done? Upgrade the need — \"when it's dark, the buzzer also beeps "
        "once\"; or play acceptance-tester: cover your neighbor's sensor — "
        "does their light obey?"], size=10.5)
    add_text(s, 0.62, 5.06, 8.76, 0.22,
             "Workbook — the loop record: my need took ___ tries to say "
             "clearly; light reading: normal ___ / hand over it ___ → my "
             "threshold is ___.", size=9.5)
    set_notes(s, "Solo base — stand-still; the instructor circulates only. "
                 "The single whole-class call at 15:35 — 'Time to open the "
                 "serial monitor — take the number you measured with your "
                 "hand over it and put it back into your need.' Circulate, "
                 "three things: the conversation (is the need getting more "
                 "specific, or are they re-pasting the same sentence?) / the "
                 "serial (did the number come out?) / the LED (cover the "
                 "sensor — does the light obey?). Intervention red line: "
                 "ask, don't fix — 'What number is dark in your need? How do "
                 "you know?' Errors go back to AI verbatim (old rule: one "
                 "step at a time). No serial data — students run their own "
                 "three-check out loud: did it upload? is the monitor open? "
                 "is the sensor reading? Whole class stuck on the serial — "
                 "demo once on the teacher machine: open the monitor, cover "
                 "the sensor, read the number — 30 seconds, then back to "
                 "solo running. AI didn't get it on the first try — teaching "
                 "point, not an incident: 'See — this is iteration. "
                 "Engineers saying a need three times is normal.' Output "
                 "anchor: at least one solo lap of the loop (say → build → "
                 "upload → measure → fill the threshold → iterate) + the "
                 "loop record in the workbook. The discipline line is not "
                 "red — it's the old course-wide rule, bold black on "
                 "yellow.")

    # ---------------------------------------------------------------- 14 night-light prompt
    s = page(prs, 14)
    add_title_bar(s, "Send This to AI")
    add_subtitle(s, "in the conversation you already have", y=1.00, size=13)
    add_card(s, 0.62, 1.38, 8.76, 2.62, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.86, 1.50, 8.28, 2.38, [
        (t, {"size": 10.5, "mono": True}) for t in [
            "I'm using aily-blockly, with a Grove Beginner Kit for Arduino",
            "(Seeeduino Lotus, with an onboard light sensor and LED — no "
            "wiring needed).",
            "Make me a new project: a night-light —",
            "input: light sensor reading; logic: reading below ___ counts "
            "as \"dark\";",
            "output: LED on when dark, off when bright.",
            "First tell me where the light sensor and LED are on the board "
            "and which pins they use,",
            "then give me the code, one step at a time.",
            "Leave the threshold number blank — I'll read the real value on "
            "the serial",
            "monitor and fill it in myself.",
        ]
    ], line_spacing=1.3)
    add_rect(s, 0.62, 4.14, 0.07, 0.95, fill=YELLOW, border=None)
    add_multiline(s, 0.90, 4.18, 8.30, 0.88, [
        ("All three boxes are in there — input, logic, output.",
         {"size": 10.5, "bold": True}),
        ("Leave the threshold blank: the number in your need is measured",
         {"size": 10.5}),
        ("by your own hand, not made up by AI.", {"size": 10.5}),
    ], line_spacing=1.25)
    set_notes(s, "The prompt is on screen — copy it into the conversation you "
                 "already have. All three boxes are in there: input, logic, "
                 "output. Leave the threshold blank — the number in your need "
                 "is measured by your own hand, not made up by AI. Send it. "
                 "Cut out once to hand out the prompt, students copy it, "
                 "return to slide 13 (the solo base). 6.4 verbatim — shared "
                 "text with the Teacher's Guide and the workbook; any edit "
                 "must sync all three.")

    # ---------------------------------------------------------------- 15 dusk alarm
    s = page(prs, 15)
    add_title_bar(s, "The Dusk Alarm Station")
    add_subtitle(s, "two boards, two programs, one wire linking them",
                 y=1.00, size=13)
    add_card(s, 0.62, 1.20, 4.10, 1.10, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.78, 1.28, 3.78, 0.95, [
        ("THE LOOKOUT — Grove Beginner Kit", {"size": 11.5, "bold": True}),
        ("light sensor watches the sky → when dark: lights its own LED + "
         "\"raises its hand\" on the signal pin (HIGH)", {"size": 10}),
    ], line_spacing=1.2)
    add_card(s, 5.28, 1.20, 4.10, 1.10, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 5.44, 1.28, 3.78, 0.95, [
        ("THE ALARM POST — Wio Terminal", {"size": 11.5, "bold": True}),
        ("watches the signal pin: sees the hand → screen \"It's dark!\" + "
         "beep; no signal → screen \"All clear\"", {"size": 10}),
    ], line_spacing=1.2)
    add_rect(s, 1.20, 2.56, 7.60, 0.02, fill=INK, border=None)
    add_rect(s, 2.20, 2.40, 5.60, 0.34, fill=YELLOW, border=None)
    add_text(s, 2.20, 2.44, 5.60, 0.26,
             "ONE GROVE CABLE: signal + ground, agreed pin → agreed pin",
             size=10.5, bold=True, align=PP_ALIGN.CENTER)
    add_card(s, 0.62, 2.85, 8.76, 1.30, fill=WHITE, border=INK, border_w=1.5)
    joint_rows = [
        (2.95, "1", "Send part one: split the job, ask for the wiring "
                     "explanation (no code yet)", 0.28),
        (3.33, "2", "Send parts two and three: generate and flash each "
                     "program separately — run each board solo first", 0.28),
        (3.71, "3", "Link and verify: cover the light sensor, watch the "
                     "alarm post — dead link? run the three checks (did each "
                     "board run solo? / is the signal wire on the agreed "
                     "pins? / is the ground shared?)", 0.42),
    ]
    for ry, num, txt, rh in joint_rows:
        num_block(s, 0.80, ry, num, size=0.32)
        add_text(s, 1.26, ry - 0.02, 7.9, rh, txt, size=10.5,
                 line_spacing=1.15)
    yellow_box(s, 0.62, 4.24, 8.76, 0.55, [
        "NINE DEAD LINKS OUT OF TEN ARE A WRONG PORT OR A LOOSE CABLE — is "
        "it CLICKED IN FIRMLY?"], size=10.5)
    add_text(s, 0.62, 4.84, 8.76, 0.20,
             "Fast lane: Wio shows the current light reading · press the Wio "
             "button to clear the alarm · flip it (Wio becomes the lookout)",
             size=9)
    add_text(s, 0.62, 5.04, 8.76, 0.20,
             "Workbook — the lookout's hand pin is ___; the alarm post knows "
             "because ___; our link's first failure was because ___.",
             size=9)
    set_notes(s, "Just now, one board worked alone. Now, upgrade: two boards "
                 "work together — and that's what the real world looks like: "
                 "a doorbell — one button outside, one speaker inside, each "
                 "doing its own job, one wire between them. The joint "
                 "project: the dusk alarm station. The Beginner Kit is the "
                 "lookout: when it's dark, it lights its own LED and 'raises "
                 "its hand' on a signal pin. The Wio Terminal is the alarm "
                 "post: when it sees the hand go up, the screen says 'It's "
                 "dark!' and the buzzer beeps once. Two boards, two programs, "
                 "each minding its own job, linked by one wire. The need also "
                 "splits into two parts — first have AI sort out the division "
                 "and the wiring (prompt part one), then ask for the two "
                 "programs (part two, part three). Same conversation window "
                 "— AI remembers the whole picture. The two whole-class "
                 "calls — 16:15: 'Both programs flashed? Run each board solo "
                 "first — then link them'; 16:30: 'Linking check, two things "
                 "— is the Grove cable in the right port? Is it clicked in "
                 "firmly?' Circulate, three things: the division (can they "
                 "say who senses and who performs?) / solo-run first (each "
                 "end runs alone before linking — no skipped steps) / the "
                 "Grove cable (nine dead links out of ten are a wrong port "
                 "or a loose cable). Intervention red line: ask, don't fix "
                 "— 'Which pin is the lookout's hand? How does the alarm post "
                 "know?' Wiring questions go to AI for a diagram (it was "
                 "asked in the prompt) — the teacher doesn't check wires for "
                 "them. Link dead → the three checks: did each board run "
                 "solo? is the signal wire on the agreed pins at both ends? "
                 "is it clicked in firmly? Still dead: unplug and re-seat, or "
                 "swap in a fresh Grove cable; if it persists, demo one "
                 "working pair on the teacher machine. One board 'occupied' "
                 "by the computer, the other won't flash → normal: flash the "
                 "two boards alternately on one computer, or split across "
                 "the pair's two machines.")

    # ---------------------------------------------------------------- 16 three parts
    s = page(prs, 16)
    add_title_bar(s, "Three Parts, Same Window — Send in Order")
    p1 = [
        "PART ONE — SPLIT THE JOB FIRST",
        "I have two boards: a Grove Beginner Kit for Arduino (Seeeduino "
        "Lotus,",
        "with onboard light sensor and LED) and a Wio Terminal (with screen "
        "and buzzer).",
        "I want to build a \"dusk alarm station\": the Beginner Kit is the "
        "lookout —",
        "when it's dark it lights its LED and \"raises its hand\" (outputs "
        "HIGH) on one",
        "digital pin; the Wio Terminal is the alarm post — when it reads "
        "that signal,",
        "the screen shows \"It's dark!\" and the buzzer beeps once.",
        "First help me sort this out: what does each end do? How do the "
        "signal wire",
        "and ground connect (which two pins)? Draw me a wiring explanation "
        "I can",
        "understand. Don't write code yet.",
    ]
    p2 = [
        "PART TWO — ASK FOR THE LOOKOUT PROGRAM",
        "Division's clear. Now give me the program for the Beginner Kit "
        "(the lookout):",
        "read the light sensor; when it's dark, LED on + signal pin raises "
        "its hand;",
        "when bright, the reverse. Use the threshold I measured: ___. One "
        "step at a time.",
    ]
    p3 = [
        "PART THREE — ASK FOR THE ALARM POST PROGRAM",
        "Now the program for the Wio Terminal (the alarm post): watch the "
        "signal pin —",
        "when it sees the hand go up, the screen shows \"It's dark!\" and "
        "the buzzer",
        "beeps once; when it doesn't, the screen shows \"All clear.\" One "
        "step at a time.",
    ]
    for i, part in enumerate([p1, p2, p3]):
        y = 1.05 + i * 1.42
        h = 0.12 + len(part) * 0.205
        add_card(s, 0.62, y, 8.76, h, fill=WHITE if i else WHITE,
                 border=INK, border_w=1.5)
        add_multiline(s, 0.84, y + 0.06, 8.32, h - 0.10, [
            (part[0], {"size": 8.5, "mono": True, "bold": True}),
        ] + [(t, {"size": 8.5, "mono": True}) for t in part[1:]],
            line_spacing=1.25)
    set_notes(s, "Three parts, send them in order, all in the conversation "
                 "you already have. Notice part one says 'don't write code "
                 "yet' — first have AI sort out the division and the wiring, "
                 "and read it before you go on. Then ask for the two programs "
                 "separately — generate and flash each one, run each board "
                 "solo first, then link them. The 'don't write code yet' "
                 "opener is itself the teaching point — the order is the "
                 "lesson. Text volume is licensed on this page (three full "
                 "prompt blocks must be copyable). 6.8 verbatim — shared "
                 "text; any edit must sync all three documents.")

    # ---------------------------------------------------------------- 17 calls
    s = page(prs, 17)
    add_title_bar(s, "Three Whole-Class Calls")
    calls = [
        ("CALL 1 · 15:35",
         "Time to open the serial monitor — write down your normal number "
         "and your hand-over number.",
         "PUT YOUR NUMBER BACK INTO YOUR NEED."),
        ("CALL 2 · 16:15",
         "Both programs flashed?",
         "RUN EACH BOARD SOLO FIRST — THEN LINK THEM."),
        ("CALL 3 · 16:30",
         "Linking check, two things — is the Grove cable in the right port?",
         "IS IT CLICKED IN FIRMLY?"),
    ]
    cy_ = 1.35
    for tag, body, big in calls:
        add_card(s, 0.62, cy_, 8.76, 1.0, fill=WHITE, border=INK,
                 border_w=1.5)
        add_rect(s, 0.62, cy_, 0.07, 1.0, fill=YELLOW, border=None)
        add_text(s, 0.90, cy_ + 0.10, 8.3, 0.24, tag, size=11.5, bold=True)
        add_text(s, 0.90, cy_ + 0.38, 8.3, 0.28, body, size=11)
        add_text(s, 0.90, cy_ + 0.66, 8.3, 0.28, big, size=11.5, bold=True)
        cy_ += 1.2
    set_notes(s, "The instructor flips to this page at each clock time, reads "
                 "the call out loud, and immediately returns to the current "
                 "solo base (13 or 15). The current call is highlighted with "
                 "a yellow light fill behind its card. Timings follow the EN "
                 "Teacher's Guide (15:35 for the serial call; 16:15 / 16:30 "
                 "for the joint calls). Big-type single lines — a rhythm "
                 "page, not a task page.")

    # ---------------------------------------------------------------- 18 summary
    s = page(prs, 18)
    add_title_bar(s, "Three Sentences — and How Big Projects Run")
    for i, t in enumerate(["It's yours.", "You're not afraid of it.",
                            "The door opened."]):
        add_golden_line(s, 0.62, 1.30 + i * 0.55, 8.76, t, size=21, h=0.45)
    add_text(s, 0.62, 3.15, 8.76, 0.24, "HOW BIG PROJECTS RUN", size=10.5,
             bold=True)
    method = [
        (0.62, "SET THE SPEC FIRST", "(the standard)"),
        (3.64, "BUILD ONE FUNCTION AT A TIME", "(each board runs its own "
                                               "loop)"),
        (6.66, "LINK THEM INTO A SYSTEM", "(one signal wire)"),
    ]
    for i, (mx, head, sub) in enumerate(method):
        add_card(s, mx, 3.45, 2.72, 0.95, fill=WHITE, border=INK,
                 border_w=1.5)
        add_text(s, mx + 0.1, 3.55, 2.52, 0.5, head, size=11, bold=True,
                 align=PP_ALIGN.CENTER, line_spacing=1.1)
        add_text(s, mx + 0.1, 4.05, 2.52, 0.28, sub, size=10,
                 align=PP_ALIGN.CENTER)
        if i < 2:
            add_text(s, mx + 2.72, 3.45, 0.3, 0.95, "→", size=18, bold=True,
                     color=YELLOW, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, wrap=False)
    add_text(s, 0.62, 4.60, 8.76, 0.28,
             "Today's alarm station did exactly this — and it's how your "
             "three marathon legs will run.", size=12,
             align=PP_ALIGN.CENTER)
    set_notes(s, "Three sentences to close: it's yours; you're not afraid of "
                 "it; the door opened. Two more from today: you can loop — "
                 "say it, build, check, upload, verify, and if it's wrong, "
                 "say it again; and you can link — today's alarm station is "
                 "the proof: set the spec first (the standard), build one "
                 "function at a time (each board runs its own loop), then "
                 "link them into a system (one signal wire). That's how "
                 "engineers take on big projects — and that's how your "
                 "three marathon legs will run.")

    # ---------------------------------------------------------------- 19 NLHD
    s = page(prs, 19)
    add_title_bar(s, "The New Home's Manual")
    grey_card(s, 0.62, 1.30, 8.76, 1.30)
    add_multiline(s, 0.82, 1.42, 8.36, 1.06, [
        ("The new home's manual: Natural-Language Hardware Development "
         "(NLHD, 15 chapters)", {"size": 11.5, "mono": True}),
        ("https://github.com/ailyProject/Natural-Language-Hardware-"
         "Development", {"size": 11.5, "mono": True}),
        ("— every chapter drills today's loop. You don't need to read it "
         "today — open it when you're stuck.", {"size": 10.5, "mono": True}),
    ], line_spacing=1.3)
    yellow_box(s, 0.62, 2.90, 8.76, 1.05, [
        "Log time — four lines as usual; the \"done\" line is required:",
        "TODAY I BUILT ___ WITH AI GUIDING ME, AND I LINKED IT TO ANOTHER "
        "BOARD;",
        "OUR LINK'S FIRST FAILURE WAS BECAUSE ___."], size=12)
    set_notes(s, "This is the new home's manual — Natural-Language Hardware "
                 "Development, 15 chapters, from lighting your first project "
                 "to full systems, and every chapter drills today's loop. "
                 "It's going to the class group; put it in your workbook. "
                 "You don't need to read it today — open it when you're "
                 "stuck. Log time. Four lines as usual — the 'done' line is "
                 "required: today I built ___ with AI guiding me, and I "
                 "linked it to another board; our link's first failure was "
                 "because ___. A student can't write the log — point at "
                 "their cheat sheet: 'Five stations of the loop — where were "
                 "you stuck, and how did you get past it? Write that. One "
                 "sentence is enough.' 'I want to play with it at home' — "
                 "that's exactly what it was installed for — it's on your "
                 "computer, play all you want. And the manual's in your "
                 "hands. The link goes to the class group + workbook.")

    # ---------------------------------------------------------------- 20 close
    s = page(prs, 20)
    add_title_bar(s, "Today You Moved From Tenant to Owner")
    wins = [
        "Your project moved off someone else's server and into YOUR OWN "
        "COMPUTER — you're the owner",
        "You READ a piece of code for the first time — and changed one line "
        "by hand; nothing broke",
        "You DIRECTED AI to build a new project from zero — you ran the "
        "engineer's loop",
        "You made TWO BOARDS COOPERATE — one senses, one performs, one "
        "wire, one system",
    ]
    wy = 1.25
    for t in wins:
        add_golden_line(s, 0.62, wy, 8.76, t, size=12, h=0.45)
        wy += 0.55
    add_card(s, 0.62, 3.55, 8.76, 1.30, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.82, 3.65, 8.36, 1.10, [
        ("NEXT TIME — Lesson 7: give your project a brief.",
         {"size": 12, "bold": True}),
        ("Good topics grow from your own experience, not from the internet.",
         {"size": 10.5}),
        ("You'll write a requirements sheet: input, logic, output — only "
         "one core function survives. Brief done, the marathon starts.",
         {"size": 10.5}),
    ], line_spacing=1.25)
    add_text(s, 0.62, 5.00, 8.76, 0.22,
             "Project folders stay where they are. Boards in the box.",
             size=10)
    set_notes(s, "Look back at today — four things done. One: your project "
                 "moved off someone else's server and into your own computer "
                 "— you're the owner. Two: you read a piece of code for the "
                 "first time, and changed one line by hand — nothing broke. "
                 "Three: you directed AI to build a new project from zero — "
                 "you ran the engineer's loop. Four: you made two boards "
                 "cooperate — one senses, one performs, one wire, one "
                 "system. Next session preview: give your project a brief. "
                 "Good topics grow from your own experience, not from the "
                 "internet. You'll write a requirements sheet: input, logic, "
                 "output — and only one core function survives. Brief done, "
                 "the marathon starts — today you said 'I want to build'; "
                 "soon you'll say 'I'm building.' Project folders stay "
                 "where they are. Boards in the box. No ability-card "
                 "lighting ceremony today — the ceremony peaks were slide "
                 "02 (the close-the-tab demo) and slide 08 (the ownership "
                 "ritual); this close lands the four wins and previews "
                 "Lesson 7.")

    prs.save(OUT)
    print(f"Saved: {OUT} slides: {len(prs.slides._sldIdLst)}")


if __name__ == "__main__":
    main()
