"""
Build the English Lesson 4 deck (Assemble Your Team — Pomodoro Timer, 20 slides)
from M0_EN_PPTPlan_CFG-5_Lesson04_AssembleYourTeam_v1.md (brand rebuild).

Output: 交付物_EN/03_Deliverables/PPTX/M0_EN_Deck_CFG-5_Lesson04_AssembleYourTeam_v1.pptx
Layout per chaihuo-ppt-brand.md: white 70 / yellow 15 / ink 10 / red 5, 960x540.
Red budget: slide 07 (differentiator rule) + slide 17 (proofreading warning).
Slide 11's traffic light uses desaturated graphic red/green (NOT brand red).
Sentence pages 09-14 share one uniform structure. No CJK / full-width / emoji.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder_lib import *
from pptx.util import Inches
from pptx.dml.color import RGBColor

TOTAL = 20
DECK_LABEL = "Assemble Your Team"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson04_AssembleYourTeam_v1.pptx")
G_RED = RGBColor(0xC4, 0x8A, 0x8A)    # desaturated graphic red (not brand)
G_GREEN = RGBColor(0x8A, 0xA8, 0x8A)  # desaturated graphic green


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


def wio_art(s, x, y, w=2.2, h=1.55, lit=None):
    add_card(s, x, y, w, h, fill=WHITE, border=INK, border_w=2.0)
    sw, sh = w * 0.62, h * 0.52
    sx, sy = x + (w - sw) / 2, y + 0.12
    add_rect(s, sx, sy, sw, sh, fill=WHITE, border=INK, border_w=1.5)
    if lit:
        add_text(s, sx, sy + sh / 2 - 0.16, sw, 0.32, lit, size=11, bold=True,
                 mono=True, align=PP_ALIGN.CENTER)
    by = y + h - 0.34
    for i in range(3):
        add_oval(s, x + 0.28 + i * 0.42, by, 0.16, fill=YELLOW, border=INK)
    add_oval(s, x + w - 0.5, by - 0.07, 0.26, fill=WHITE, border=INK)


def role_header(s, round_no, role, person, owns):
    """Yellow role label strip — sentence pages 09-14 uniform."""
    add_rect(s, 0.62, 1.18, 8.76, 0.72, fill=YELLOW, border=None)
    add_text(s, 0.8, 1.26, 8.4, 0.3,
             f"ROUND {round_no}/5 · {role}  |  {person}", size=15, bold=True)
    add_text(s, 0.8, 1.58, 8.4, 0.26, f'owns "{owns}"', size=11.5)


def prompt_card(s, lines, y=2.05, h=None, size=12.5):
    """Big monospace prompt box (white fill, black border)."""
    if h is None:
        h = 0.25 + len(lines) * 0.32
    add_card(s, 0.62, y, 8.76, h, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.86, y + 0.13, 8.28, h - 0.26,
                  [(t, {"size": size, "mono": True}) for t in lines],
                  line_spacing=1.35)


def main():
    prs = new_deck()

    # ---------------------------------------------------------------- 01 cover
    s = page(prs, 1)
    add_text(s, 0.62, 1.30, 6.6, 0.35,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0)",
             size=14)
    add_multiline(s, 0.62, 1.68, 6.6, 1.3, [
        ("Assemble Your Team,", {"size": 34, "bold": True}),
        ("Build a Pomodoro Timer", {"size": 34, "bold": True}),
    ], line_spacing=1.1)
    add_rect(s, 0.62, 3.05, 1.6, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 3.3, 6.6, 0.4,
             "BMAD's Five Roles · Your First Complete Project · M0 Lesson 4",
             size=14)
    add_text(s, 0.62, 3.85, 6.6, 0.5,
             "From today, you're the boss of a team.",
             size=18, bold=True)
    wio_art(s, 6.9, 3.3, w=2.4, h=1.7, lit="WORK 25:00")
    add_text(s, 6.9, 5.05, 2.4, 0.26, "Pomodoro timer on the Wio",
             size=10, align=PP_ALIGN.CENTER)
    set_notes(s, "Cover — loops before class. Open with one welcome line — "
                 "'Welcome to Lesson 4. Last session your project got a face "
                 "and hands — today we go further: we give AI a team, and "
                 "build one complete project end to end.' — then straight to "
                 "slide 02; the cover is not a talking page. Pomodoro timer "
                 "photo on the right (Wio screen showing the WORK countdown — "
                 "line-art placeholder until the rehearsal photo), yellow rule "
                 "under the subtitle.")

    # ---------------------------------------------------------------- 02 collect
    s = page(prs, 2)
    add_title_bar(s, "First, Let's Collect Last Session's Work")
    num_block(s, 0.62, 1.4, "1", size=0.4)
    add_multiline(s, 1.2, 1.4, 7.9, 0.85, [
        ("Hand in your work — online doc? send the link.", {"size": 14,
                                                            "bold": True}),
        ("Handwritten? send a photo. Not in yet? Note it down — finish before "
         "you leave today.", {"size": 12.5}),
    ], line_spacing=1.3)
    num_block(s, 0.62, 2.45, "2", size=0.4)
    add_multiline(s, 1.2, 2.45, 7.9, 0.85, [
        ("Keep your project manifesto and three-box design sheet at hand —",
         {"size": 14, "bold": True}),
        ("they're about to do a lot of work.", {"size": 12.5}),
    ], line_spacing=1.3)
    yellow_box(s, 0.62, 3.6, 8.76, 0.85, [
        "Remember the three things for describing a screen?",
        "Position, size, color — you'll use all of it today."], size=13)
    set_notes(s, "Before we start, let's collect last session's work: if you "
                 "used an md doc, send me the link; if you wrote by hand, "
                 "photograph it and send it — missed it? note it down, due "
                 "before today ends. (point at the Project Wall) Look — it's "
                 "still up. Everyone's manifesto is on it. Last session you "
                 "met your new gear; your project got a face and hands. And "
                 "you learned how to describe a screen clearly — what were "
                 "the three things again? (guide to: position, size, color) "
                 "Right — you'll use all of it today. Keep your project "
                 "manifesto and three-box design sheet at hand — they're "
                 "about to do a lot of work. Hard 5-minute timebox on the "
                 "collection — no per-item feedback; the not-yet-in list goes "
                 "to the TA to register, don't chase. Output anchor: Lesson "
                 "3's outputs are in (my Wio tour sheet / screen designs / "
                 "log) — md link or photo.")

    # ---------------------------------------------------------------- 03 compare
    s = page(prs, 3)
    add_title_bar(s, "Two Ways — Same Idea")
    add_text(s, 0.62, 1.1, 8.76, 0.28,
             "(one small line, for the show of hands)", size=10.5)
    add_text(s, 0.62, 1.38, 8.76, 0.3,
             "Raise your hand if you've ever hit any of these:", size=13,
             bold=True)
    add_text(s, 0.62, 1.72, 8.76, 0.3,
             "don't know where to add a feature  /  never thought it through "
             "at the start  /  don't know where the color lives", size=11.5)
    add_card(s, 0.62, 2.2, 4.3, 1.6, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.8, 2.32, 3.94, 0.28, "WAY A · WRITE-IT-DIRECT", size=12.5,
             bold=True)
    add_multiline(s, 0.8, 2.66, 3.94, 1.05, [
        "It runs, and that's about it:",
        "layout is whatever happened",
        "adding features gets messy",
        "recoloring is guesswork",
    ], size=11, line_spacing=1.25)
    add_rect(s, 5.08, 2.2, 4.3, 1.6, fill=YELLOW, border=None)
    add_text(s, 5.26, 2.32, 3.94, 0.28, "WAY B · PLAN-FIRST", size=12.5,
             bold=True)
    add_multiline(s, 5.26, 2.66, 3.94, 1.05, [
        "The screen is designed:",
        "the structure is clear",
        "you know where new things go",
    ], size=11, line_spacing=1.25)
    add_golden_line(s, 0.62, 4.05, 8.76,
                    "BMAD — an open-source method used by developers "
                    "worldwide: have AI play different roles, and think it "
                    "through step by step before you build.", size=14,
                    h=None)
    set_notes(s, "Quick talk. You already know how to get AI to make you "
                 "something in one sentence — fine for small stuff. But three "
                 "questions — raise your hand if you've hit any: first, the "
                 "code's getting long, you want to add a feature, and you "
                 "don't know where to tell AI to change it? Second, you're "
                 "halfway through and realize you never thought it through at "
                 "the start? Third, you want to change the color scheme and "
                 "have no idea where the color lives? (pause, watch the hands) "
                 "— That's not your problem. That's the ceiling of the "
                 "one-sentence approach. (screen: the compare page) Two ways. "
                 "Way A, write-it-direct: it runs, and that's about it — the "
                 "layout is whatever happened, adding features gets messy, "
                 "recoloring is guesswork. Way B, plan-first: think through "
                 "what you want, what it looks like, how it's split — then "
                 "build. The screen is designed. The structure is clear. You "
                 "know where new things go. This isn't extra busywork — it's "
                 "having AI think it through with you, a few steps at a time. "
                 "THE PAGE IS STATIC — no live AI demo, ever. If someone "
                 "raises a hand, ask 'where were you stuck?' — 30 seconds of "
                 "empathy beats explaining. BMAD in three sentences only. "
                 "CFU: 'Thumbs up if plan-first sounds like more work right "
                 "now. Middle if you can see the point. Keep it honest — no "
                 "right answer.'")

    # ---------------------------------------------------------------- 04 BMAD
    s = page(prs, 4)
    add_title_bar(s, "Meet BMAD — Open Source, Free, Professional")
    add_text(s, 0.62, 1.02, 8.76, 0.26,
             "(small) Breakthrough Method for Agile AI-Driven Development",
             size=10.5)
    cards = [
        ("1", "OPEN SOURCE & FREE",
         "everything is public on GitHub, anyone can use it, zero cost"),
        ("2", "USED BY DEVELOPERS WORLDWIDE",
         "a method professional teams maintain and keep updating: 12+ roles, "
         "30+ ready workflows inside"),
        ("3", "THE ONE CORE MOVE",
         "don't let AI do everything in one sentence; have it play different "
         "roles and think it through step by step before you build"),
    ]
    cy = 1.35
    for num, head, body in cards:
        num_block(s, 0.62, cy, num, size=0.38)
        add_text(s, 1.14, cy - 0.02, 7.9, 0.28, head, size=13, bold=True)
        add_text(s, 1.14, cy + 0.26, 7.9, 0.55, body, size=11.5,
                 line_spacing=1.15)
        cy += 0.92
    add_grey_box(s, 0.62, 4.18, 8.76, 0.45,
                 "github.com/bmad-code-org/BMAD-METHOD   —   open source, you "
                 "can check every word I just said", size=11.5)
    add_text(s, 0.62, 4.78, 8.76, 0.3,
             "BMAD is not software to install. It's a method. Methods don't "
             "get installed — learn it, and it's yours.", size=12, bold=True,
             align=PP_ALIGN.CENTER)
    set_notes(s, "This approach has a real name — BMAD. AI-driven agile "
                 "development. Three things to remember. One: open source and "
                 "free — all its docs and code are public on GitHub; anyone "
                 "can use it, zero cost. Two: developers worldwide use it — "
                 "this isn't something I invented; it's a method professional "
                 "teams maintain and keep updating, with a dozen-plus roles "
                 "and thirty-plus ready workflows inside. Three: the one core "
                 "move — don't let AI do everything in one sentence; have it "
                 "play different roles and think it through step by step "
                 "before you build. (point at the screen) The address: "
                 "github.com/bmad-code-org/BMAD-METHOD — open source, so you "
                 "can check every word I just said. Note: BMAD is not "
                 "software to install. It's a method. Methods don't get "
                 "installed — learn it, and it's yours. Today you learn its "
                 "one core move. Three sentences and move on — no framework "
                 "deep-dive. 'Is it really free?' -> 'Open source means the "
                 "code is public and free forever — it says so on GitHub.' "
                 "The full name is on screen; don't read it aloud. CFU: 'Turn "
                 "to your neighbor: one sentence — what is BMAD, to a total "
                 "beginner?' (wait time ~15 s, then two random shares)")

    # ---------------------------------------------------------------- 05 two ways
    s = page(prs, 5)
    add_title_bar(s, "How to Use It — Two Ways, Today the First One")
    add_rect(s, 0.62, 1.32, 4.3, 2.6, fill=YELLOW, border=None)
    add_text(s, 0.8, 1.44, 3.94, 0.55,
             "WAY ONE · RIGHT HERE IN CLASS — INSTALL NOTHING", size=12,
             bold=True, line_spacing=1.1)
    add_multiline(s, 0.8, 2.08, 3.94, 1.35, [
        "The five round-openers you're about to get are BMAD's core usage —",
        "PM -> designer -> architect -> developer -> tester, in a relay "
        "inside one conversation.",
        "The method lives in your head — that's the valuable part.",
    ], size=11, line_spacing=1.3)
    add_card(s, 5.08, 1.32, 4.3, 2.6, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.26, 1.44, 3.94, 0.55,
             "WAY TWO · OPTIONAL, AFTER CLASS — LET AI INSTALL IT", size=12,
             bold=True, line_spacing=1.1)
    add_text(s, 5.26, 2.08, 3.94, 0.26, "No commands to memorize. Just say:",
             size=11)
    add_grey_box(s, 5.26, 2.38, 3.94, 0.85,
                 "Read the documentation at https://github.com/bmad-code-org/"
                 "BMAD-METHOD and configure the BMAD workflow in my project.",
                 size=9)
    add_text(s, 5.26, 3.32, 3.94, 0.52,
             "AI visits the repo, runs the install, drops the whole set of "
             "roles and workflows into your project. (Needs a Node.js "
             "environment — not today.)", size=9.5, line_spacing=1.2)
    add_golden_line(s, 0.62, 4.2, 8.76,
                    "Today's one goal: run this method once, in your head. "
                    "Tools can be installed anytime — the method in your head "
                    "stays with you.", size=14, h=None)
    set_notes(s, "How do you use it? Two ways — today, only the first. Way "
                 "one, right here in class: install nothing. The five "
                 "round-openers you're about to get are BMAD's core usage — "
                 "PM, designer, architect, developer, tester, in a relay inside "
                 "one conversation. The method lives in your head — that's "
                 "the valuable part. Way two, optional, after class: later, "
                 "when you want a full AI team set up inside a project on "
                 "your own computer — no commands to memorize, let AI install "
                 "it. Just say: 'Read the documentation at "
                 "https://github.com/bmad-code-org/BMAD-METHOD and configure "
                 "the BMAD workflow in my project.' AI visits the GitHub "
                 "repo, runs the install, and drops the whole set of roles "
                 "and workflows into your project. That needs a Node.js "
                 "environment — not today. Want to try it? Find me or a TA "
                 "after class. Today's one goal: run this method once, in "
                 "your head. Tools can be installed anytime; the method in "
                 "your head stays with you. No live install, no software "
                 "setup of any kind — if students push for it, note their "
                 "names, follow up after class.")

    # ---------------------------------------------------------------- 06 role map
    s = page(prs, 6)
    add_title_bar(s, "Your AI Team — What You Used to Do Alone, Five Experts "
                    "Now Share")
    add_text(s, 0.62, 1.08, 8.76, 0.3, "You are the boss of this team.",
             size=15, bold=True)
    roles = [
        ("1", "PM", "John", 'owns "what problem we\'re solving, who it\'s '
         'for"'),
        ("2", "DESIGNER", "Sally", 'owns "what it looks like, how you use '
         'it"'),
        ("3", "ARCHITECT", "Winston", 'owns "how it\'s split into pieces, '
         'what states it has"'),
        ("4", "DEVELOPER", "Amelia", 'owns "writing it"'),
        ("5", "TESTER", "Quinn", 'owns "finding what\'s wrong"'),
    ]
    cw = 1.66
    for i, (num, role, person, owns) in enumerate(roles):
        x = 0.62 + i * (cw + 0.14)
        add_card(s, x, 1.5, cw, 2.15, fill=WHITE, border=INK, border_w=1.5)
        num_block(s, x + 0.12, 1.62, num, size=0.34)
        add_text(s, x + 0.12, 2.04, cw - 0.24, 0.3, role, size=12.5, bold=True)
        add_text(s, x + 0.12, 2.34, cw - 0.24, 0.28, person, size=12)
        add_text(s, x + 0.12, 2.66, cw - 0.24, 0.9, owns, size=9,
                 line_spacing=1.2)
        if i < 4:
            add_text(s, x + cw - 0.02, 2.4, 0.18, 0.4, "->", size=13,
                     bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.85, 8.76, 0.28,
             "They all have names — call them by name, like assigning work to "
             "colleagues.", size=11)
    add_text(s, 0.62, 4.16, 8.76, 0.28,
             "Five roles = five rounds of relay in ONE conversation.", size=11)
    add_text(s, 0.62, 4.47, 8.76, 0.28,
             "Same Five Rules every round — change roles by calling the name.",
             size=11)
    set_notes(s, "(screen the role cards; point at the five names already on "
                 "the board, one sentence each) BMAD's team is five people. "
                 "PM — owns what problem we're solving and who it's for. "
                 "Designer — owns what it looks like and how you use it. "
                 "Architect — owns how it's split into pieces and what states "
                 "it has. Developer — owns writing it. Tester — owns finding "
                 "what's wrong. (point at the 8-step map from Lesson 1) Look: "
                 "framing the problem and finding the user — that's PM. "
                 "Prototyping — designer and architect. Writing code — "
                 "developer. Trade-offs and judging — architect and tester. "
                 "What you used to do alone is now five experts sharing the "
                 "work. And you — you're the boss of this team. Don't worry: "
                 "it's not five real people. It's five rounds of relay inside "
                 "one conversation. Each round still runs on the Five Rules. "
                 "What changes: each round has a clear job. Change roles "
                 "without changing windows — just call the name. They all "
                 "have names — PM is John, designer Sally, architect Winston, "
                 "developer Amelia, tester Quinn — like assigning work to "
                 "colleagues. And these five roles aren't my invention — "
                 "professional developers put them together and shared them "
                 "openly. Today you use the professional team, in one "
                 "conversation, five rounds. Draw the connecting lines on the "
                 "board as you talk (board connections = handoff chain); "
                 "photograph the finished board (student log material). CFU: "
                 "'Point at the board — which role owns what it looks like?' "
                 "(one random call)")

    # ---------------------------------------------------------------- 07 kickoff (RED 1)
    s = page(prs, 7)
    add_title_bar(s, "Kickoff — Build a Pomodoro Timer")
    add_text(s, 0.62, 1.15, 8.76, 0.35,
             "The rule: 25 minutes of focus, 5-minute break, repeat.",
             size=16, bold=True, align=PP_ALIGN.CENTER)
    add_red_rule_box(s, 0.62, 1.7, 8.76, 1.3, "The rule:",
                     ["YOUR TIMER MUST HAVE ONE THING DIFFERENT FROM "
                      "EVERYONE ELSE'S —",
                      "AND IT HAS TO GROW OUT OF YOUR LIFE."], body_size=17)
    add_text(s, 0.62, 3.25, 8.76, 0.28,
             "(three candidate directions)", size=10.5)
    add_text(s, 0.62, 3.55, 8.76, 0.55,
             "Do you space out doing homework?  ·  Need to time your piano "
             "practice?  ·  Building one for your little sister?", size=13,
             align=PP_ALIGN.CENTER, line_spacing=1.15)
    yellow_box(s, 0.62, 4.25, 8.76, 1.0, [
        "AI gives everyone the same default answer.",
        "The details of your life are the part it can't give you — that's "
        "what makes your clock worth something."], size=12.5)
    set_notes(s, "Pomodoro: 25 minutes of focus, 5-minute break, repeat. That "
                 "simple. Today everyone builds one — on your Wio, with this "
                 "team. But there's a rule — your timer must have one thing "
                 "different from everyone else's. Not 'mine is blue' — that's "
                 "not it. It has to grow out of your life: do you space out "
                 "doing homework? Do you need to time your piano practice? "
                 "Are you building one for your little sister? Here's a "
                 "secret: AI gives everyone the same default answer. The "
                 "details of your life are the part it can't give you — "
                 "that's what makes your clock worth something. Students: "
                 "listen; start thinking 'what is my focus problem.' "
                 "Pitfalls: 'I want one like a game console!' -> 'Good — then "
                 "today we get the timing part running, and the game part "
                 "goes on the later list.' (Not rejecting — into the list. "
                 "That's the first live trade-off.) Student missed Lesson 3 / "
                 "never used Wio -> TA runs a 5-minute refresher (the switch "
                 "mantra: 'slide it, slide it = flash mode', 'no response? "
                 "slide it'), then one warm-up: show HELLO in big letters on "
                 "screen, then rejoin. CFU: 'Turn to your neighbor: one real "
                 "focus problem in your life. Fifteen seconds — go.'")

    # ---------------------------------------------------------------- 08 relay rules
    s = page(prs, 8)
    add_title_bar(s, "Relay Rules — Don't Drop the Baton")
    num_block(s, 0.62, 1.45, "1", size=0.4)
    add_multiline(s, 1.2, 1.45, 7.9, 1.0, [
        ('Every round opens with the same first line:', {"size": 14,
                                                         "bold": True}),
        ('"based on the previous round\'s conclusion" — hand the last result '
         'to the new role.', {"size": 13}),
    ], line_spacing=1.35)
    num_block(s, 0.62, 2.75, "2", size=0.4)
    add_multiline(s, 1.2, 2.75, 7.9, 1.0, [
        ("All five rounds happen in ONE conversation.", {"size": 14,
                                                          "bold": True}),
        ("Switch roles by calling the name — opening a new window loses "
         "everything.", {"size": 13}),
    ], line_spacing=1.35)
    add_text(s, 0.62, 4.3, 8.76, 0.3,
             "The lines are in your Student Workbook — follow me on the "
             "screen.", size=12, align=PP_ALIGN.CENTER)
    set_notes(s, "Two rules before we start. One: every round today opens "
                 "with 'based on the previous round's conclusion' — hand the "
                 "last conversation's result to the new role. It's a relay — "
                 "don't drop the baton. Two: all five rounds happen in ONE "
                 "conversation. Don't open a new one — the moment you do, "
                 "every conclusion so far is gone. Change roles without "
                 "changing windows: just call the name — 'Sally, based on "
                 "the previous round...'. Flip fast — this page is the "
                 "round's instructions, not a talking page.")

    # ---------------------------------------------------------------- 09 PM
    s = page(prs, 9)
    add_title_bar(s, "Round 1/5 · PM — The 3 Things My Clock Must Do")
    role_header(s, 1, "PM", "John",
                "what problem we're solving, who it's for")
    prompt_card(s, [
        "John, I want to build a Pomodoro timer for this problem:",
        "(one real thing from your life — e.g. I pick up my phone within 10 "
        "minutes of starting homework)",
        "First ask me 5 questions to understand what I need, then help me "
        "write down:",
        "the 3 things this clock must do. Don't write code yet.",
    ], y=2.05, h=1.75)
    add_text(s, 0.62, 3.95, 8.76, 0.55,
             '(reminder)  Of the 3 things he gives you, one must be your '
             'differentiator. Not there? Push back: "I haven\'t told you my '
             'special requirement —"', size=11.5, line_spacing=1.2)
    yellow_box(s, 0.62, 4.6, 8.76, 0.62, [
        'Write in your workbook: "the 3 things my clock must do" — star your '
        'differentiator.'], size=12)
    set_notes(s, "Round one — PM on. The PM doesn't build; the PM asks first. "
                 "Today the person you ask is yourself: what is my real focus "
                 "problem? Open your workbook (or notebook) to the PM opener "
                 "— it's on screen too. Round one has no previous round, so "
                 "you start from your problem. Vague differentiator ('mine "
                 "is blue', 'make it cuter') — the main battleground of "
                 "today's success line: push to behavior — 'Does blue fix "
                 "your spacing out? The moment you space out, what should "
                 "the clock do?' TA circulation focuses here first. Student "
                 "copies AI's default 'standard timer features' -> 'That's "
                 "everyone's clock. Where's yours?' AI's list is bloated -> "
                 "the one professional line: 'Too much. Keep only P0.' (P0 = "
                 "must-have, P1 = nice-to-have, P2 = bonus; first version = "
                 "P0 only — don't explain the concept, one use and it "
                 "sticks.) Student still not in the conversation at 5 "
                 "minutes (stuck choosing a problem) -> teacher offers two "
                 "candidates; pick one in 30 seconds. Output anchor: "
                 "workbook — '3 things my clock must do,' with one starred — "
                 "that's my differentiator. Stays fixed while students send "
                 "their conversation.")

    # ---------------------------------------------------------------- 10 designer
    s = page(prs, 10)
    add_title_bar(s, "Round 2/5 · Designer — Two Screens + Three Buttons")
    role_header(s, 2, "DESIGNER", "Sally", "what it looks like, how you use it")
    prompt_card(s, [
        "Sally, based on the previous round: my clock must do these 3 "
        "things: (copy them).",
        "Design: 1. what the focusing screen looks like; 2. what the break "
        "screen looks like;",
        "3. what buttons A, B, C each do.",
        "My special requirement: (your differentiator) — it must show on "
        "the screens.",
        "Don't write code yet.",
    ], y=2.05, h=1.95)
    add_text(s, 0.62, 4.15, 8.76, 0.3,
             "(reminder)  Describing a screen — the three things from last "
             "session: position, size, color.", size=11.5)
    yellow_box(s, 0.62, 4.55, 8.76, 0.62, [
        "Write in your workbook: focusing screen ___ / break screen ___ / "
        "A ___ B ___ C ___."], size=12)
    set_notes(s, "Round two — designer on. First line as usual: based on the "
                 "previous round. Last session you practiced 'how to "
                 "describe a screen': position, size, color. Today the "
                 "scaffolding is gone — you organize the language yourself. "
                 "The sentences are in your workbook — forgetting how is "
                 "normal. Look, then speak. Student stuck describing the "
                 "screen -> point at the workbook sentence: 'Three things "
                 "from last session — position, size, color.' Point at the "
                 "scaffold; don't say it for them. AI's design misses the "
                 "differentiator -> 'Ask it: Which screen shows my special "
                 "requirement?' On-screen text: English / numbers / graphics "
                 "only — never gamble on Chinese rendering. Output anchor: "
                 "workbook — 'focusing screen: ___ / break screen: ___ / "
                 "A ___, B ___, C ___.' Stays fixed.")

    # ---------------------------------------------------------------- 11 architect
    s = page(prs, 11)
    add_title_bar(s, "Round 3/5 · Architect — The Traffic Light & State Circles")
    role_header(s, 3, "ARCHITECT", "Winston",
                "how it's split into pieces, what states it has")
    # LEFT: traffic light (desaturated graphic colors)
    add_card(s, 0.62, 2.05, 4.3, 1.25, fill=WHITE, border=INK, border_w=1.5)
    add_oval(s, 1.5, 2.2, 0.5, fill=G_RED, border=INK)
    add_oval(s, 2.5, 2.2, 0.5, fill=WHITE, border=INK)
    add_text(s, 1.2, 2.8, 3.2, 0.28, "one light at a time", size=10.5,
             bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 1.2, 3.05, 3.2, 0.24, "what changes it? time runs out",
             size=10, align=PP_ALIGN.CENTER)
    # RIGHT: state circles
    add_card(s, 5.08, 2.05, 4.3, 1.25, fill=WHITE, border=INK, border_w=1.5)
    add_oval(s, 5.5, 2.35, 0.75, fill=WHITE, border=INK)
    add_text(s, 5.5, 2.6, 0.75, 0.25, "focus", size=10.5, bold=True,
             align=PP_ALIGN.CENTER)
    add_oval(s, 7.9, 2.35, 0.75, fill=WHITE, border=INK)
    add_text(s, 7.9, 2.6, 0.75, 0.25, "break", size=10.5, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 6.28, 2.52, 1.6, 0.28, "->  ->", size=13, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 6.25, 2.85, 1.66, 0.22, "press A / time's up", size=9,
             align=PP_ALIGN.CENTER)
    add_text(s, 5.26, 3.05, 3.94, 0.22,
             "two circles = a complete timer", size=9.5, align=PP_ALIGN.CENTER)
    prompt_card(s, [
        "Winston, your turn.",
        "Based on the requirements and design above, make a technical plan "
        "for the timer —",
        "keep it simple, Amelia will write the code from it.",
    ], y=3.45, h=1.05, size=11.5)
    yellow_box(s, 0.62, 4.62, 8.76, 0.62, [
        "Draw your state circles on paper (or in your workbook: my states "
        "___ -> ___, what changes it ___)."], size=11.5)
    set_notes(s, "(whole class, traffic light on the board) Everyone, eyes on "
                 "the board. These 8 minutes are the only time I teach today. "
                 "A traffic light — red, green, one light at a time. What "
                 "changes it? Time runs out. — Your timer is the same kind of "
                 "thing: it has several 'looks', it's in one look at a time, "
                 "and an action moves it to another look. This thing has a "
                 "name — a state. Now, everyone draw the state circles of "
                 "your clock on paper: at least two circles — focus, break — "
                 "and on the arrow write what changes it, like 'press A' or "
                 "'time's up'. Can't make three circles? Two circles are a "
                 "complete Pomodoro timer. 'Paused' is the most common third "
                 "circle — add it if you want. (about 4 minutes in) Drawn? "
                 "Round three — architect on. Winston takes the requirements "
                 "and the design and produces the technical plan. You don't "
                 "need to understand the details — it's not for you, it's for "
                 "Amelia, who writes the code next. Can't draw the circles "
                 "(today's #1 pitfall) -> first, let them copy the two-state "
                 "starter (focus -> break, A switches) drawn for them; after "
                 "copying, add their own circle. Still stuck after copying -> "
                 "skip the architecture conversation, go straight to the dev "
                 "round with the two-state default; the architecture "
                 "understanding gets picked up at Lesson 8. Don't burn time "
                 "here. 'Why draw circles, why not just build?' -> 'This is a "
                 "map for the program. At Lesson 8 you'll see the actual "
                 "code — and the circles live inside it.' (one-line teaser; "
                 "don't expand.) Output anchor: state circles on paper (or "
                 "two lines in the workbook). NON-NEGOTIABLE: the 8-minute "
                 "whole-class lecture — today's only one.")

    # ---------------------------------------------------------------- 12 developer
    s = page(prs, 12)
    add_title_bar(s, "Round 4/5 · Developer — Build It Whole, In One Pass")
    role_header(s, 4, "DEVELOPER", "Amelia", "writing it")
    steps = ["Generate the complete code", "Upload to the Wio", "Run it",
             "Iterate your differentiator"]
    sx = 0.62
    sw = 2.05
    for i, st in enumerate(steps):
        num_block(s, sx, 2.05, str(i + 1), size=0.34)
        add_text(s, sx + 0.44, 2.07, sw - 0.44, 0.55, st, size=11, bold=True,
                 line_spacing=1.05)
        if i < 3:
            add_text(s, sx + sw - 0.04, 2.05, 0.2, 0.3, "->", size=12,
                     bold=True)
        sx += sw + 0.12
    add_text(s, 0.62, 2.7, 8.76, 0.3,
             "The requirements, the design and the plan are all in this "
             "conversation — Amelia builds the whole timer from them, in one "
             "pass.", size=11.5)
    prompt_card(s, [
        "Amelia, based on the requirements, design and technical plan above, "
        "build the complete timer",
        "and give me code I can use directly.",
        "For easy testing, set the work time to 1 minute and the break to 30 "
        "seconds first.",
    ], y=3.1, h=1.25, size=11.5)
    add_golden_line(s, 0.62, 4.5, 8.76,
                    "Error? Paste the error back to Amelia verbatim — it "
                    "wrote the code, it fixes it.", size=13)
    set_notes(s, "Round four — developer on. PM's requirements, Sally's "
                 "design, Winston's plan are all sitting in this conversation "
                 "— Amelia builds the whole timer from them. Build it, upload "
                 "it, run it. Error? Paste the error back verbatim — it "
                 "wrote the code, it fixes it. Once it runs, make one change "
                 "of your own — a background color, a transition — that's "
                 "iteration. At 15:35, one whole-class check — call: 'Whose "
                 "clock is running?' Not running by 35 minutes (the most "
                 "common tech stall) -> the TA hands out the lifeline "
                 "prompt, to be pasted verbatim: 'My timer has two states: "
                 "WORK and BREAK. Pressing A switches between them: WORK "
                 "shows a red background and WORK; BREAK shows a green "
                 "background and BREAK. For now, only do this switching — no "
                 "timing — using a simple if/else on the current state.' "
                 "(The lifeline is the guaranteed minimum: get the screen "
                 "glowing first, then Amelia adds the full features back on "
                 "top — the differentiator is unaffected.) Upload failure -> "
                 "flip the side switch twice into bootloader mode and retry. "
                 "'This is harder than the other lessons' -> the standing "
                 "line: 'Right. This is your first real project. Before, you "
                 "were learning moves. Today, you step on the field for the "
                 "first time.' At 15:30, most still not running -> "
                 "whole-class announcement: 'Not running yet — raise your "
                 "hand. TA first, with the lifeline. Running? Move on — add "
                 "your differentiator.' (No waiting; tiered release.) Output "
                 "anchor: the timer running on the Wio; the differentiator "
                 "visible on screen. Stays fixed.")

    # ---------------------------------------------------------------- 13 tester
    s = page(prs, 13)
    add_title_bar(s, "Round 5/5 · Tester — Break It")
    role_header(s, 5, "TESTER", "Quinn", "finding what's wrong")
    add_text(s, 0.62, 2.05, 8.76, 0.35,
             "A tester's job has one word: BREAK IT.", size=17, bold=True)
    prompt_card(s, [
        "Quinn, my timer is done.",
        'Help me find fault: give me 5 ways to "break it", like rapid '
        'presses, or mashing buttons mid-timer.',
        "I'll try each one myself.",
    ], y=2.5, h=1.25, size=12)
    add_text(s, 0.62, 3.9, 8.76, 0.28,
             "(break-it examples, short words)", size=10.5)
    add_text(s, 0.62, 4.18, 8.76, 0.3,
             "rapid repeated presses · mashing buttons mid-timer · holding a "
             "button down", size=12.5)
    add_golden_line(s, 0.62, 4.68, 8.76,
                    "Try each one by hand — for every fault, make a call: "
                    "Accept, or Reject?", size=13)
    set_notes(s, "Last relay round — tester on. A tester's job has one word: "
                 "break it. Ask AI for the whole break-it list: rapid "
                 "repeated presses, mashing buttons mid-timer, holding a "
                 "button down... then you try each one, by hand. Can't break "
                 "anything (rare) -> 'Swap with your neighbor — you'll have "
                 "no mercy on someone else's clock.' (Swapping is also a "
                 "hidden anti-sameness check: you see how their clock is "
                 "different.) Student fixing forever -> 'Fix the most "
                 "important one. The rest goes on the later list.' UNDER NO "
                 "CIRCUMSTANCES does this block end early or get squeezed — "
                 "even if earlier rounds collapsed, protect the full 15 "
                 "minutes from here (with the Picky User page). THE IRON "
                 "LAW. Output anchor: workbook — the 5-item break-it list, "
                 "each with Accept / Reject + one reason.")

    # ---------------------------------------------------------------- 14 picky user
    s = page(prs, 14)
    add_title_bar(s, "One More Special Reviewer — The Picky User")
    prompt_card(s, [
        "Play ___ (the real person from your design sheet) and use my "
        "Pomodoro timer.",
        "Pick 1 fault. Only 1.",
    ], y=1.35, h=0.95, size=13)
    add_card(s, 0.62, 2.5, 4.3, 1.1, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.8, 2.62, 3.94, 0.3, "REJECT", size=14, bold=True)
    add_text(s, 0.8, 2.98, 3.94, 0.5,
             "-> have AI fix it — fix the most important one", size=12)
    add_card(s, 5.08, 2.5, 4.3, 1.1, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.26, 2.62, 3.94, 0.3, "ACCEPT", size=14, bold=True)
    add_text(s, 5.26, 2.98, 3.94, 0.5,
             '-> write it down: "I know it has this small flaw" — a '
             'professional decision too', size=12)
    yellow_box(s, 0.62, 3.85, 8.76, 1.0, [
        "Write in your workbook: the 5-item break-it list, each marked "
        "Accept/Reject + one reason;",
        "the Picky User's one fault, noted separately."], size=12.5)
    set_notes(s, "List tried — one more special reviewer on stage: the Picky "
                 "User. You met it in Lesson 2: AI plays the real person from "
                 "your design sheet, and it picks exactly one fault. Today it "
                 "accepts your clock. Every test you try, every fault you "
                 "hear — make a call: Accept or Reject? Reject -> have AI "
                 "fix it. Accept -> write down 'I know it has this small "
                 "flaw' — that's a professional decision too. In Lesson 2 we "
                 "accepted one, remember: it still stopped after a few extra "
                 "presses — we accepted it. Output anchor: workbook — the "
                 "5-item break-it list with Accept/Reject + one reason each; "
                 "the Picky User's one fault noted separately.")

    # ---------------------------------------------------------------- 15 archive
    s = page(prs, 15)
    add_title_bar(s, "The Archive Ceremony — Your First Complete Project")
    steps = [
        ("1", "Screenshot each of the five relay rounds"),
        ("2", "Put all five into one folder — name it with your name and "
              "date"),
        ("3", 'Missed a round? Backfill it after class and stick a note in '
              'the folder: "backfilled"'),
    ]
    sy = 1.5
    for num, txt in steps:
        num_block(s, 0.82, sy, num, size=0.4)
        add_text(s, 1.4, sy + 0.03, 7.7, 0.55, txt, size=14,
                 line_spacing=1.1)
        sy += 0.78
    yellow_box(s, 0.62, 4.05, 8.76, 0.95, [
        "The folder is treasure: later, when you want to know what a "
        "complete project looks like — this is it."], size=13)
    set_notes(s, "Stop. Next 15 minutes — three things more important than "
                 "easter eggs. One: archive. Screenshot each of the five "
                 "relay rounds — five screenshots into one folder, named with "
                 "your name and date. This folder is treasure — the full "
                 "record of your first complete project. Later, when you want "
                 "to know what a complete project looks like, this is it. "
                 "Missed a round? Backfill it after class and stick a note in "
                 "the folder: 'backfilled.' Mark missing rounds on the spot "
                 "for backfill + sticky note (completeness target >=90%). "
                 "Output anchor: the five-round screenshot folder, complete. "
                 "[Archive example photo: teacher's rehearsal folder with "
                 "naming convention — to capture at rehearsal.]")

    # ---------------------------------------------------------------- 16 golden
    s = page(prs, 16)
    add_title_bar(s, "Does This Only Work for Hardware?")
    add_golden_line(s, 0.62, 1.5, 8.76,
                    "BMAD's five roles are not a method for hardware. "
                    "They're a method for anything — today you just "
                    "practiced it on hardware.", size=19, h=None)
    add_text(s, 0.62, 2.75, 8.76, 0.3,
             "(small prompt)  Where else could you use this method? Who "
             "would be the PM there? — one use case per table.", size=11.5)
    tl = [("10 YEARS AGO", "lighting an LED was an entry-level project"),
          ("5 YEARS AGO", "connecting to WiFi was advanced"),
          ("TODAY", "complete beginners finished a full project with five "
           "roles in one session")]
    tx = 0.62
    for head, body in tl:
        add_card(s, tx, 3.2, 2.84, 1.0, fill=WHITE, border=INK, border_w=1.5)
        add_text(s, tx + 0.12, 3.3, 2.6, 0.26, head, size=11, bold=True)
        add_text(s, tx + 0.12, 3.58, 2.6, 0.55, body, size=10,
                 line_spacing=1.1)
        tx += 2.96
    add_text(s, 0.62, 4.4, 8.76, 0.3,
             "The project is as big as the team it needs. Small projects "
             "can merge roles.", size=12, bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "Two — a big question: does this method only work for "
                 "hardware? (two seconds) Here's one from me: I wrote this "
                 "course's lesson plans with these five people — PM decided "
                 "what problem each session solves; tester found the holes "
                 "in my plan. Your turn: writing a research report? Who's "
                 "the PM? (guide: choosing the question) The architect? (the "
                 "outline) The tester? (finding each other's mistakes) One "
                 "use case per table. Three — one line to close: BMAD — "
                 "that's the English team name of these five roles — BMAD's "
                 "five roles are not a method for hardware. They're a method "
                 "for anything — today you just practiced it on hardware. "
                 "(Say this line as-is — don't change it.) The five roles "
                 "aren't a ceremony. Small projects can merge roles — the "
                 "project is as big as the team it needs. Now look at the "
                 "road you've walked: 10 years ago, lighting an LED was an "
                 "entry-level project; 5 years ago, connecting to WiFi was "
                 "advanced; today, complete beginners finished a full "
                 "project with five roles in one session. Lesson 1 and 2 — "
                 "your hardware learned to sense the world. Lesson 3 — your "
                 "project got a face and hands. Today — you got the method. "
                 "Transfer talk goes cold -> offer your own ('I use it to "
                 "plan family trips'); 'why not just build it directly' -> "
                 "point at the compare page: 'One-sentence-all-in-one saves "
                 "effort, but you get a clone you can't edit. Is the gap "
                 "speed — or thinking?' Output anchor: one line in the "
                 "workbook — 'I could use this method for ___, and the PM "
                 "there would be ___.'")

    # ---------------------------------------------------------------- 17 log (RED 2)
    s = page(prs, 17)
    add_title_bar(s, "Your Log — Four Lines As Usual, Today One Line Must Be "
                    "Clear")
    ly = 1.3
    for line in ["Today I made ___", "I got stuck on ___", "Then ___",
                 "Next time I want ___"]:
        add_yellow_dot_item(s, 0.72, ly, 8.4, line, size=13)
        ly += 0.34
    add_text(s, 0.62, 2.75, 8.76, 0.35,
             "— and today, write it clearly: WHERE IS MY CLOCK DIFFERENT?",
             size=15, bold=True)
    add_grey_box(s, 0.62, 3.25, 8.76, 0.45,
                 'Help me turn this into a log — only what I said, nothing I '
                 "didn't.", size=12)
    add_red_rule_box(s, 0.62, 3.9, 8.76, 0.95, "Warning",
                     ["AI will confidently invent things.",
                      "Proofreading is your job — nobody can do it for you."],
                     body_size=13)
    add_text(s, 0.62, 5.0, 8.76, 0.28,
             'Workbook: the proofread log + one line — "I could use this '
             'method for ___ (where), and the PM there would be ___."',
             size=10, align=PP_ALIGN.CENTER)
    set_notes(s, "Last thing: today's log, four lines as usual — and today "
                 "one line must be written clearly: where is my clock "
                 "different? Write it, then send it to AI: 'Help me turn "
                 "this into a log — only what I said, nothing I didn't.' Then "
                 "read what it writes — AI will confidently invent things. "
                 "Proofreading is your job; nobody can do it for you. "
                 "Output anchor: (1) the proofread four-line log in the "
                 "workbook, with the 'where is my clock different' line "
                 "clear; (2) the transfer line ('I could use this method "
                 "for ___, and the PM there would be ___').")

    # ---------------------------------------------------------------- 18 buffer
    s = page(prs, 18)
    add_text(s, 0.62, 1.05, 3.0, 1.75, "25", size=96, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.88, 3.0, 0.5, "minutes", size=26, bold=True,
             align=PP_ALIGN.CENTER)
    yellow_box(s, 3.9, 1.2, 5.5, 0.85, [
        "EXIT 1 · FINISH TO STANDARD (everyone crosses this line)",
        "Two states + timing + reminder running. Missing relay rounds? "
        "Backfill the screenshots."], size=11.5)
    add_card(s, 3.9, 2.2, 5.5, 1.55, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 4.08, 2.3, 5.14, 1.35, [
        ("EXIT 2 · EASTER EGG CHALLENGE (fast lane)", {"size": 11.5,
                                                       "bold": True}),
        ("Flip timer (turn the board over and it starts timing — it feels "
         "itself flip)", {"size": 10}),
        ("Victory jingle (a tune after 3 completed rounds)", {"size": 10}),
        ("Rest-screen joke (an English one-liner on the break screen)",
         {"size": 10}),
        ("First decide do-or-skip — two minutes. Doesn't work out? Today's "
         "pass is unaffected.", {"size": 9.5}),
    ], line_spacing=1.22)
    add_card(s, 3.9, 3.9, 5.5, 0.95, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 4.08, 4.0, 5.14, 0.78, [
        ("EXIT 3 · 8-STEP MAPPING", {"size": 11.5, "bold": True}),
        ("Go through your relay log; against the 8-step map on the board, "
         "write one line per box: \"what I did in this step\" (\"not yet\" "
         "for boxes you didn't visit).", {"size": 9.5}),
    ], line_spacing=1.22)
    add_golden_line(s, 0.62, 3.62, 3.0,
                    "Standard first, then fast.", size=13)
    add_text(s, 0.62, 4.35, 3.0, 0.75,
             "The buffer is part of the lesson, not early dismissal.",
             size=10.5, line_spacing=1.15)
    set_notes(s, "Set the tone at the start (announce today's exit per your "
                 "pre-class choice): 'Next 25 minutes: timer not running — "
                 "keep going, that's today's line. Past the line — [announce "
                 "today's pick: try an easter egg / map your relay log "
                 "against the 8 steps / help a neighbor]. Two egg rules: "
                 "one, decide do-or-skip in two minutes — don't dither; two, "
                 "if the egg doesn't work out, today's pass is unaffected.' "
                 "Circulation order: first sweep who hasn't crossed the line "
                 "(the TA watches these), then lead the fast ones through "
                 "eggs. Egg candidates (verbal; rehearsal-proven only): the "
                 "flip timer / the victory jingle / the rest-screen joke. "
                 "Below-the-line students skip eggs; the TA keeps them on the "
                 "main build (state switching > timing > reminder). Egg "
                 "stuck over 8 minutes -> 'Eggs done. Make the later list "
                 "beautiful — that counts too.' 'I'm done — can I leave / "
                 "play on my phone?' — No. Point at the three exits. Whole "
                 "class done early with 15 minutes left -> don't drag; move "
                 "into the close and do the mapping review properly. Output "
                 "anchor (egg students): one line in the workbook — 'the egg "
                 "I added was ___, it worked / it didn't, so it's on the "
                 "later list.' Stays fixed during the buffer.")

    # ---------------------------------------------------------------- 19 8-step map
    s = page(prs, 19)
    add_title_bar(s, "The 8-Step Map — Today You Walked the First Six")
    boxes = [
        ("1+2", "Who it's for + what problem it solves — PM", True),
        ("3", "Say clearly what you want and how it looks — designer + "
              "architect", True),
        ("4", "Build it with AI — developer", True),
        ("5", "Try it, find faults — tester", True),
        ("6", "Fix it or live with it, keep it or cut it — your Accept/Reject "
              "calls, your egg do-or-skip", True),
        ("7", "Show it to someone — you'll do that in a minute", False),
        ("8", "Look back at it when it's done — that's happening right now",
         False),
    ]
    bw, bh = 4.32, 0.78
    positions = [(0.62, 1.22), (5.04, 1.22), (0.62, 2.00), (5.04, 2.00),
                 (0.62, 2.78), (5.04, 2.78), (0.62, 3.56)]
    for (num, txt, walked), (x, y) in zip(boxes, positions):
        add_card(s, x, y, bw, bh, fill=YELLOW if walked else WHITE,
                 border=INK, border_w=1.5)
        add_text(s, x + 0.12, y + 0.07, 0.5, 0.26, num, size=11, bold=True)
        add_text(s, x + 0.62, y + 0.09, bw - 0.74, 0.62, txt, size=10,
                 line_spacing=1.1)
    add_text(s, 5.04, 3.56, 4.32, 0.78,
             "(yellow = walked today  ·  white = just started)", size=9.5)
    yellow_box(s, 0.62, 4.44, 8.76, 0.72, [
        'Against the map, write one line per box in your workbook: "what I '
        'did in this step" — then take a sticky: "where I got stuck", one '
        'per step, sign it, put it on the wall.'], size=10)
    set_notes(s, "(at the 8-step map on the board) Last 20 minutes — no "
                 "building. Something more important: seeing the road you "
                 "walked today. Eight boxes on this map — the complete map "
                 "of making a project. Today you walked the first six — "
                 "we'll stick them up round by round: you figured out who "
                 "it's for and what problem it solves — PM, steps one and "
                 "two. You said clearly what you want and how it looks — "
                 "designer, step three. You split it into pieces and ordered "
                 "them — architect, also step three, and you grazed step "
                 "five. You built it with AI — developer, step four. You "
                 "tried it and found faults — tester, step five. You fixed "
                 "it or lived with it, kept it or cut it — your Accept/Reject "
                 "calls, your egg do-or-skip — step six. Steps seven and "
                 "eight only started today: show it to someone — you'll do "
                 "that in a minute; and look back at it when it's done — "
                 "that's happening right now. Then the workbook mapping + "
                 "the sticky wall (one sticky per step, 'where I got "
                 "stuck,' signed, on the wall). Output anchor: (1) the "
                 "8-step mapping written out in the workbook; (2) the "
                 "'where I got stuck' sticky on the wall (photographed).")

    # ---------------------------------------------------------------- 20 close
    s = page(prs, 20)
    add_title_bar(s, "Look at the Wall + Share + Next Time")
    add_text(s, 0.62, 1.18, 8.76, 0.3, "THE STICKY WALL:", size=11.5,
             bold=True)
    add_text(s, 0.62, 1.48, 8.76, 0.3,
             "Which step has the most stickies?", size=14, bold=True)
    add_text(s, 0.62, 1.8, 8.76, 0.3,
             "Getting fully stuck and fully unstuck today — next time you "
             "get stuck, you won't panic.", size=11.5)
    add_text(s, 0.62, 2.25, 8.76, 0.3, "THE SHARE RULE:", size=11.5, bold=True)
    add_text(s, 0.62, 2.55, 8.76, 0.3,
             "Across your table, 30 seconds: what's different about their "
             "clock compared to yours?", size=12.5)
    add_text(s, 0.62, 3.1, 8.76, 0.3, "NEXT TIME · LESSON 5 — TEACH YOUR "
             "HARDWARE TO SEE", size=15, bold=True)
    add_rect(s, 0.62, 3.45, 1.6, 0.05, fill=YELLOW, border=None)
    add_text(s, 0.62, 3.65, 8.76, 0.35,
             'It will recognize your face and your hand.', size=16)
    add_text(s, 0.62, 4.3, 8.76, 0.55,
             "Keep your timer — it's your first complete project, not your "
             "last. Take home (or photograph): your five-screenshot folder, "
             "your state-circles paper, your workbook.", size=11,
             align=PP_ALIGN.CENTER, line_spacing=1.2)
    set_notes(s, "Look at the wall. Which step has the most stickies? (count; "
                 "name one or two) 'Tell us how stuck you were, and how you "
                 "got past it. Remember this wall. Today you got fully stuck "
                 "and fully unstuck — next time you get stuck, you won't "
                 "panic. Last look across your table: what's different about "
                 "their clock compared to yours? (30 seconds) Next session, "
                 "your hardware learns to see — it will recognize your face "
                 "and your hand. Keep your timer — it's your first complete "
                 "project, not your last. Devices in the box. Your "
                 "five-screenshot folder, your state-circles paper, your "
                 "workbook — take them home, or photograph them. Class "
                 "dismissed!' All stickies piling on 'developer' is normal — "
                 "say it honestly: 'Look — the hardest part is making the "
                 "thing. That's exactly why the steps before it matter: "
                 "think it through, and the building goes smoother.' Short "
                 "on time -> cut the share-out, but keep the mapping writing "
                 "and the sticky wall. After class: collect today's outputs "
                 "(md links / handwriting photos) and note completeness.")

    prs.save(OUT)
    print("Saved:", OUT, "slides:", len(prs.slides.__iter__.__self__._sldIdLst))


if __name__ == "__main__":
    main()
