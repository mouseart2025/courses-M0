"""
Build the English Lesson 2 deck (Find a Problem Worth Solving, 22 slides, 3 h)
from M0_EN_PPTPlan_CFG-5_Lesson02_FindAProblemWorthSolving_v1.md (brand rebuild).

Output: 交付物_EN/03_Deliverables/PPTX/M0_EN_Deck_CFG-5_Lesson02_FindAProblemWorthSolving_v1.pptx
Layout per chaihuo-ppt-brand.md: white 70 / yellow 15 / ink 10 / red 5, 960x540.
Red budget: slide 21 (proofreading warning) ONLY — the deck's single red element.
Screenshot assets (slides 06/11/19) run live-demo track -> [FILL] placeholder cards.
No CJK / full-width / emoji glyphs on screen — ASCII-safe screen text.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder_lib import *
from pptx.util import Inches

TOTAL = 22
DECK_LABEL = "Find a Problem Worth Solving"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson02_FindAProblemWorthSolving_v1.pptx")


def page(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(s)
    add_footer(s, n, TOTAL, DECK_LABEL)
    return s


def num_block(s, x, y, num, size=0.42):
    """Yellow square number chip (brand line-icon substitute)."""
    add_rect(s, x, y, size, size, fill=YELLOW, border=None)
    add_text(s, x, y + 0.04, size, 0.34, num, size=15, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER)


def yellow_box(s, x, y, w, h, lines, title=None, size=13, title_size=15,
               line_spacing=1.25):
    """Yellow notice/definition box with optional bold title."""
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


def mini_three_box(s, x, y, w=2.4, h=0.62, label_size=10):
    """Small Sense -> Logic -> Output three-box strip (cover corner icon)."""
    bw = (w - 2 * 0.28) / 3.0
    labels = ["Sense", "Logic", "Output"]
    for i, lab in enumerate(labels):
        bx = x + i * (bw + 0.28)
        add_rect(s, bx, y, bw, h, fill=WHITE, border=INK, border_w=1.0)
        add_text(s, bx, y + 0.16, bw, 0.3, lab, size=label_size, bold=True,
                 align=PP_ALIGN.CENTER)
        if i < 2:
            add_text(s, bx + bw + 0.02, y + 0.13, 0.24, 0.36, "->", size=13,
                     bold=True, align=PP_ALIGN.CENTER)


def main():
    prs = new_deck()

    # ---------------------------------------------------------------- 01 cover
    s = page(prs, 1)
    add_text(s, 0.62, 1.30, 6.6, 0.35,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0)",
             size=14)
    add_text(s, 0.62, 1.68, 8.76, 0.85, "Find a Problem Worth Solving",
             size=38, bold=True)
    add_rect(s, 0.62, 2.62, 1.6, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 2.92, 6.6, 0.4,
             "Grove Beginner Kit · IoT Starter Board · M0 Lesson 2",
             size=15)
    add_text(s, 0.62, 3.45, 6.6, 0.5,
             "Good projects grow out of good problems.",
             size=18, bold=True)
    mini_three_box(s, 6.75, 4.35, w=2.6)
    set_notes(s, "Cover — loops before class. Open with one welcome line and go "
                 "straight to slide 02 — the cover is not a talking page. "
                 "Small 3-box icon (Sense -> Logic -> Output) bottom-right, yellow "
                 "rule under the subtitle.")

    # ---------------------------------------------------------------- 02 recap
    s = page(prs, 2)
    add_title_bar(s, "Last Time You Made It Light Up")
    add_subtitle(s, "— Today You Decide Who It Lights Up For", y=1.0, size=17)
    panels = [
        ("1", "Your name on the screen", '"I can make things."'),
        ("2", "The dark-detecting light",
         "Sense -> Logic -> Output, running for the first time"),
        ("3", "The 3-box diagram", "Sense -> Logic -> Output"),
    ]
    px = 0.62
    pw = 2.72
    for i, (num, head, sub) in enumerate(panels):
        x = px + i * (pw + 0.3)
        add_card(s, x, 1.5, pw, 1.35, fill=WHITE, border=INK, border_w=1.5)
        num_block(s, x + 0.14, 1.64, num, size=0.36)
        add_text(s, x + 0.62, 1.62, pw - 0.76, 0.42, head, size=13, bold=True,
                 line_spacing=1.05)
        add_text(s, x + 0.16, 2.18, pw - 0.32, 0.58, sub, size=11.5,
                 line_spacing=1.1)
        if i < 2:
            add_text(s, x + pw + 0.02, 1.95, 0.26, 0.5, "->", size=18, bold=True,
                     align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.1, 8.76, 0.32, "Two topics from last term:",
             size=14, bold=True)
    add_yellow_dot_item(s, 0.72, 3.48, 8.5,
                        "A water reminder — made for a mom who always forgets to drink",
                        size=13.5)
    add_yellow_dot_item(s, 0.72, 3.82, 8.5,
                        "A night light — made for a little brother afraid of the dark",
                        size=13.5)
    add_golden_line(s, 0.62, 4.35, 8.76,
                    "Neither is a big invention. Both are real annoyances from real life.",
                    size=15)
    set_notes(s, "Take 30 seconds to look back: you put your name on the screen, "
                 "and you taught the board Sense -> Logic -> Output. Last session "
                 "you proved 'I can make things.' From today, the question changes: "
                 "make things for who? Look at two topics from last term: a water "
                 "reminder — made for a mom who always forgets to drink; a night "
                 "light — made for a little brother afraid of the dark. See the "
                 "pattern? Neither is a big invention. Both are real annoyances "
                 "from real life. Today, you find yours. Write 'who does it light "
                 "up for?' on the whiteboard — point at it all session. Only 3 "
                 "minutes — two examples, then move on.")

    # ---------------------------------------------------------------- 03 map
    s = page(prs, 3)
    add_title_bar(s, "Three Kinds of Projects")
    add_subtitle(s, "Your topic can land in any of them.", y=1.0, size=17)
    cols = [
        ("1", "STANDALONE DEVICE",
         "The board is the whole thing — it senses, decides, reacts by itself.",
         ["night light", "alarm", "desk weather station", "pomodoro timer",
          "whack-a-mole game"],
         None),
        ("2", "THE COMPUTER'S PARTNER",
         "The board is the hands and ears; the computer is the screen.",
         ["game controller (buttons / knob / shake drive the screen game)",
          "presentation clicker (one press turns the slide)",
          "shake-to-vote"],
         "examples = the ones your instructor rehearsed"),
        ("3", "THE OUTSIDE WORLD",
         "The modules can snap off and recombine; later: new modules, even the "
         "internet.",
         [],
         "have a parts box? It's the door in (if you have one)"),
    ]
    cw = 2.84
    for i, (num, name, desc, ex, note) in enumerate(cols):
        x = 0.62 + i * (cw + 0.12)
        add_card(s, x, 1.38, cw, 3.06, fill=WHITE, border=INK, border_w=1.5)
        num_block(s, x + 0.14, 1.52, num, size=0.38)
        add_text(s, x + 0.62, 1.55, cw - 0.74, 0.62, name, size=13, bold=True,
                 line_spacing=1.05)
        # flat line-icon zone
        iy = 2.3
        if i == 0:
            add_rect(s, x + 1.02, iy, 0.8, 0.52, fill=WHITE, border=INK,
                     border_w=1.5)
            add_oval(s, x + 1.12, iy + 0.18, 0.12, fill=YELLOW, border=None)
            add_text(s, x + 1.3, iy + 0.14, 0.5, 0.26, "board", size=8.5)
        elif i == 1:
            add_rect(s, x + 0.52, iy, 0.66, 0.52, fill=WHITE, border=INK,
                     border_w=1.5)
            add_rect(s, x + 1.66, iy, 0.7, 0.4, fill=WHITE, border=INK,
                     border_w=1.5)
            add_rect(s, x + 1.2, iy + 0.22, 0.44, 0.05, fill=YELLOW,
                     border=None)
            add_text(s, x + 0.52, iy + 0.55, 0.66, 0.2, "board", size=8.5,
                     align=PP_ALIGN.CENTER)
            add_text(s, x + 1.66, iy + 0.43, 0.7, 0.2, "computer", size=8.5,
                     align=PP_ALIGN.CENTER)
        else:
            add_oval(s, x + 1.07, iy - 0.02, 0.56, fill=WHITE, border=INK)
            add_rect(s, x + 1.13, iy + 0.24, 0.44, 0.04, fill=INK, border=None)
            add_text(s, x + 1.07, iy + 0.58, 0.56, 0.2, "world", size=8.5,
                     align=PP_ALIGN.CENTER)
        add_text(s, x + 0.16, 3.0, cw - 0.32, 0.62, desc, size=11,
                 line_spacing=1.12)
        ey = 3.66
        if ex:
            add_multiline(s, x + 0.16, ey, cw - 0.32, 0.72,
                          ex, size=9.5, line_spacing=1.18)
        if note:
            add_text(s, x + 0.16, 4.12, cw - 0.32, 0.28,
                     "( " + note + " )", size=8.5)
    add_golden_line(s, 0.62, 4.62, 8.76,
                    "What matters isn't how advanced it is — it's whose "
                    "annoyance it solves.", size=15)
    set_notes(s, "Before you hunt for a topic, look at what kinds of things this "
                 "board can actually make. Get the map in your head first, so your "
                 "topics don't fly off everywhere. Walk the three columns: kind "
                 "one — standalone device, the board is the whole thing (the "
                 "dark-detecting light from last session is exactly this); kind "
                 "two — the computer's partner (the board and the computer make "
                 "something together); kind three — the outside world (today just "
                 "know the road exists). One or two examples per kind, no "
                 "parameters. Hard timebox: 8 minutes total, do not expand. Kind "
                 "two: only rehearsed examples go on the page — if the rehearsal "
                 "didn't run, kind two gets concepts only. A student presses on "
                 "the internet? 'There's a dedicated lesson later — today, just "
                 "remember it exists.' CFU: 'Point at the map. Which kind is a "
                 "flashlight that turns on when it's dark? (wait) Which kind is "
                 "a controller for a computer game? (wait) One-word answers — "
                 "go.'")

    # ---------------------------------------------------------------- 04 write
    s = page(prs, 4)
    add_title_bar(s, "Two Minutes — Write Three Small Annoyances")
    add_text(s, 0.62, 1.3, 8.76, 0.4, "At home  ·  At school  ·  On the way",
             size=17, bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 1.78, 8.76, 0.4,
             "What's something that needs running after, something that needs "
             "watching?", size=15, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.28, 8.76, 0.3,
             "(no ideas? prompt words)", size=11, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.58, 8.76, 0.3,
             "waking up in the morning / your backpack / pets / grandparents / "
             "rainy days", size=12, align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 3.05, 8.76, 1.0, [
        "Open your Student Workbook (or notebook) — find the \"annoyances\" box.",
        "Write at least 3, in your own document."],
        title="Write it down:", size=13.5)
    add_text(s, 0.62, 4.25, 8.76, 0.55,
             "(teacher's own, small)  one from home: I always forget my keys "
             "when I leave  ·  one from work: I stare at the screen until my "
             "eyes hurt — swap for your own two real ones", size=10.5,
             align=PP_ALIGN.CENTER)
    set_notes(s, "Open your Student Workbook (or notebook), find the "
                 "'annoyances' box. Two minutes. Write three small things that "
                 "annoy you — at least three, in your own document. Yours, your "
                 "family's, your friends' — all fine. The smaller the better: "
                 "'my mom always forgets her pills' is worth a hundred 'world "
                 "peace's. I'll go first: ... Model first with your own two real "
                 "annoyances. Tables stuck? TAs drop the prompt words. Solving "
                 "for someone else is allowed. Students with no record carrier: "
                 "remind them to write in their notebook — every later step "
                 "needs it. Output anchor: at least 3 annoyances in everyone's "
                 "workbook.")

    # ---------------------------------------------------------------- 05 phrases
    s = page(prs, 5)
    add_title_bar(s, "Two New Phrase Sets")
    add_text(s, 0.62, 1.28, 8.76, 0.3, "(read together)", size=12)
    # topic set
    add_text(s, 0.62, 1.62, 4.3, 0.3, "THE TOPIC SET — think about WHAT to make",
             size=13, bold=True)
    add_card(s, 0.62, 1.95, 4.3, 1.95, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 0.8, 2.08, 3.98, 1.7, [
        ("Turn my annoyances into ideas  (we use it today)",
         {"size": 11.5, "mono": True, "bold": True}),
        ("How else could this idea work?", {"size": 11.5, "mono": True}),
        ("The Tough Reviewer  (we use it today)",
         {"size": 11.5, "mono": True, "bold": True}),
        ("Why I chose it", {"size": 11.5, "mono": True}),
    ], line_spacing=1.5)
    # user set
    add_text(s, 5.08, 1.62, 4.3, 0.3, "THE USER SET — think about WHO it's for",
             size=13, bold=True)
    add_card(s, 5.08, 1.95, 4.3, 1.95, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 5.26, 2.08, 3.98, 1.7, [
        ("Who would use it", {"size": 11.5, "mono": True}),
        ("Help me make an interview script", {"size": 11.5, "mono": True}),
        ("Pretend to be my user", {"size": 11.5, "mono": True}),
    ], line_spacing=1.5)
    yellow_box(s, 0.62, 4.1, 8.76, 0.85, [
        "These phrases are printed in your Student Workbook — forget them, "
        "flip to the page.",
        "The blanks are for you to fill — a phrase sent with blanks doesn't "
        "count."], size=13)
    set_notes(s, "New weapons. Last session you learned two spells — one thing "
                 "at a time, and if it's wrong, add one more line. Today, two "
                 "more phrase sets: the topic set, four phrases — they help you "
                 "think about WHAT to make; and the user set, three phrases — "
                 "they help you think about WHO it's for. These phrases are "
                 "printed in your Student Workbook — forget them, flip to the "
                 "page. First, remember these two: 'turn my annoyances into "
                 "ideas' and 'the Tough Reviewer'. Project the full phrase text "
                 "and read once together. Set the gate before anything else: "
                 "the blanks in a phrase must be filled with your own stuff — a "
                 "phrase sent with blanks doesn't count. That sentence is the "
                 "gate for today's red line.")

    # ---------------------------------------------------------------- 06 diverge
    s = page(prs, 6)
    add_title_bar(s, "Turn My Annoyances into Ideas")
    add_card(s, 0.62, 1.3, 5.4, 1.75, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 0.8, 1.42, 5.04, 1.55, [
        ("I have three real annoyances:", {"size": 11.5, "mono": True}),
        ("1. ___  2. ___  3. ___.", {"size": 11.5, "mono": True, "bold": True}),
        ("Give me 10 ideas that small hardware (sensors)", {"size": 11.5,
                                                             "mono": True}),
        ("could solve, the more specific the better.", {"size": 11.5,
                                                        "mono": True}),
        ("Just list ideas — don't choose for me.", {"size": 11.5,
                                                    "mono": True}),
    ], line_spacing=1.3)
    add_card(s, 6.2, 1.3, 3.18, 1.75, fill=WHITE, border=INK, border_w=1.0)
    add_multiline(s, 6.36, 1.42, 2.86, 1.55, [
        ("[ example", {"size": 10.5, "bold": True}),
        ("conversation ]", {"size": 10.5, "bold": True}),
        ("filled template", {"size": 10}),
        ("->  10 ideas", {"size": 10}),
        ("->  2 circled", {"size": 10}),
    ], line_spacing=1.35, align=PP_ALIGN.CENTER)
    add_golden_line(s, 0.62, 3.25, 8.76,
                    "What it gives you is candidates.", size=16)
    add_text(s, 0.62, 3.85, 8.76, 0.55,
             "Which one is buildable and who'd really use it — it doesn't know. "
             "You know.", size=15, align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 4.5, 8.76, 0.62, [
        "The idea list stays in your AI conversation — copy your 3 favorites "
        "into your workbook."], size=12.5)
    set_notes(s, "Watch me once. (project, fill the template) My annoyances: "
                 "[your three real annoyances]. Send it to AI — (send) see, 10 "
                 "ideas. (circle 2) Notice: what it gives you is candidates. "
                 "Which one is buildable, who'd really use it — it doesn't know. "
                 "You know. Your turn: fill your three annoyances into the "
                 "phrase, send it — then copy your 3 favorite ideas back into "
                 "your workbook. Red-line patrol (the TA's main job): a student "
                 "sends the blank template — send it back to be refilled: 'The "
                 "blanks are for you to fill — AI doesn't know how old your "
                 "sister is.' Everyone must get 10+ ideas before this counts as "
                 "done. Few ideas? 'Give me 5 weirder ones.' AI/network stalls "
                 "here: don't wait — use the 40-in-1 module chart (or the parts "
                 "box) as the inspiration pool; the AI divergence moves to the "
                 "start of the rules segment for 10 minutes. The manifesto "
                 "round is non-negotiable. [Screenshot asset runs on the live "
                 "demo track — 30-second cut to backup is not an incident.]")

    # ---------------------------------------------------------------- 07 tough reviewer
    s = page(prs, 7)
    add_title_bar(s, "Ten Is Too Many — Keep One")
    add_subtitle(s, "The Tough Reviewer", y=1.0, size=17)
    add_card(s, 0.62, 1.38, 5.4, 2.0, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 0.8, 1.5, 5.04, 1.8, [
        ("You are the bluntest advisor who still", {"size": 11, "mono": True}),
        ("wants me to succeed. Here are my ideas: ___", {"size": 11,
                                                          "mono": True}),
        ("Grill me with three questions, one by one:", {"size": 11,
                                                        "mono": True}),
        ("Can it be done in 3 hours?  Do I have the", {"size": 11,
                                                        "mono": True}),
        ("hardware?  Would I really use it every day?", {"size": 11,
                                                         "mono": True}),
        ("Then point out the one that stands up best —", {"size": 11,
                                                           "mono": True}),
        ("but the choice is mine.", {"size": 11, "mono": True}),
    ], line_spacing=1.28)
    add_text(s, 6.2, 1.42, 3.18, 0.3, "The three questions:", size=13,
             bold=True)
    qy = 1.78
    for i, q in enumerate(["Can it be done in 3 hours?", "Do I have the hardware?",
                           "Would I really use it every day?"]):
        num_block(s, 6.2, qy, str(i + 1), size=0.34)
        add_text(s, 6.64, qy + 0.02, 2.74, 0.3, q, size=12)
        qy += 0.5
    yellow_box(s, 0.62, 3.55, 5.4, 0.75, [
        "The 2 surviving ideas + one line on \"why I kept it\" — write it into "
        "your workbook."], size=12)
    add_text(s, 0.62, 4.5, 8.76, 0.6,
             "(no panic, small)  All rejected? Take the one you're most attached "
             "to, run \"how else could this idea work?\" once, then screen "
             "again.", size=11, align=PP_ALIGN.CENTER)
    set_notes(s, "Ten is too many — you can only build one. Meet today's bluntest "
                 "phrase: the Tough Reviewer — AI plays the rudest, most honest "
                 "advisor who still wants you to win. Throw your ideas at it, and "
                 "it grills you, idea by idea, with three questions: can it be "
                 "done in 3 hours? do you have the hardware? would you really "
                 "use it every day? (demo once) See? Getting grilled isn't "
                 "shameful — it kills the ideas that can't stand up, before "
                 "you've spent half a day on them. Go. Today's number-one "
                 "pitfall lives here: AI says pick X, the student picks X. The "
                 "TA's standard move: walk over and ask — 'Tell me why that one "
                 "is good.' They can answer -> let them through; they can't -> "
                 "have them run the three questions themselves. All rejected? "
                 "Run 'how else could this idea work?' once, then screen again. "
                 "Topic too big ('I want to build a robot')? The three questions "
                 "are the first gate; still too big? Demo the cut live: 'You "
                 "can't build the robot today — but a robot head that greets "
                 "people? That you can start today.'")

    # ---------------------------------------------------------------- 08 users
    s = page(prs, 8)
    add_title_bar(s, "Who Would Use It? — Real Names Only")
    add_card(s, 0.62, 1.3, 4.3, 0.85, fill=YELLOW, border=None)
    add_text(s, 0.8, 1.4, 3.94, 0.3, "PASS", size=13, bold=True)
    add_text(s, 0.8, 1.72, 3.94, 0.35,
             '"My mom"  /  "my classmate Liam"', size=13)
    add_card(s, 5.08, 1.3, 4.3, 0.85, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.26, 1.4, 3.94, 0.3, "FAIL", size=13, bold=True)
    add_text(s, 5.26, 1.72, 3.94, 0.35,
             '"All students"  /  "everyone"', size=13)
    add_text(s, 0.62, 2.35, 8.76, 0.3, "Interview your neighbor — 4 minutes each:",
             size=14, bold=True)
    add_text(s, 0.62, 2.7, 8.76, 0.55,
             "you introduce your topic, your neighbor plays your user and asks "
             "you the questions from the \"help me make an interview script\" "
             "phrase.", size=12.5, line_spacing=1.15)
    add_grey_box(s, 0.62, 3.35, 5.4, 0.62,
                 "My project is for ___ because ___.", size=14)
    add_text(s, 6.2, 3.42, 3.18, 0.55, "Write this user picture into your "
             "workbook.", size=12)
    add_text(s, 0.62, 4.2, 8.76, 0.3, "(two new words)", size=11, bold=True)
    add_multiline(s, 0.62, 4.5, 8.76, 0.6, [
        ("user — the real person who'll actually use your project",
         {"size": 12}),
        ("interview — going to ask that person a few questions",
         {"size": 12}),
    ], line_spacing=1.3)
    set_notes(s, "Topic set — next question: who'll use it? Use the 'who would "
                 "use it' phrase and let AI make a list — but there's a hard "
                 "rule: real names only. 'My mom', 'my classmate Liam' — pass. "
                 "'All students', 'everyone' — fail. Then interview your "
                 "neighbor, two at a time, 4 minutes each: you introduce your "
                 "topic, your neighbor plays your user and asks you the "
                 "questions from the 'help me make an interview script' phrase. "
                 "Name the two new words clearly and point at them: 'These "
                 "aren't exam words — you'll use them today.' Interviews drifting "
                 "into small talk? The interview questions are in the phrase — "
                 "reading them aloud counts. A list without real names — send "
                 "it back: 'A project written for everyone ends up used by no "
                 "one.' A student embarrassed to interview? Swap roles. Their "
                 "'user' is themselves? Fine — but make them write a second real "
                 "name: 'Besides you — who's most annoyed by this?' Output "
                 "anchor: a one-line user picture in the workbook.")

    # ---------------------------------------------------------------- 09 manifesto
    s = page(prs, 9)
    add_title_bar(s, "One Sentence — Announce Your Topic to the Class")
    add_card(s, 0.62, 1.32, 8.76, 0.85, fill=CODEBG, border=INK, border_w=1.5)
    add_text(s, 0.82, 1.48, 8.36, 0.55,
             "I'm making a ___ for ___ because ___.", size=20, bold=True,
             mono=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.3, 8.76, 0.3, "Teacher's example:", size=12, bold=True)
    add_grey_box(s, 0.62, 2.62, 8.76, 0.6,
                 "I'm making a [pill reminder] for [my mom], because [she "
                 "always forgets her blood-pressure meds].", size=12)
    num_block(s, 0.62, 3.38, "1", size=0.36)
    add_text(s, 1.06, 3.4, 8.3, 0.32,
             "Write it on a big sticky  ->  put it on the Project Wall",
             size=14, bold=True)
    num_block(s, 0.62, 3.82, "2", size=0.36)
    add_text(s, 1.06, 3.84, 8.3, 0.32,
             "Open your workbook (or notebook)  ->  copy the same sentence in",
             size=14, bold=True)
    add_golden_line(s, 0.62, 4.4, 8.76,
                    "This sentence is the north star for every lesson after this "
                    "one.", size=15)
    add_text(s, 0.62, 5.0, 8.76, 0.3, "The wall and the workbook must match.",
             size=13, bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "Last thing: one sentence each, announce your topic to the "
                 "class. The format: I'm making a ___ for ___ because ___. I'll "
                 "go first: I'm making a [pill reminder] for [my mom], because "
                 "[she always forgets her blood-pressure meds]. — One by one. "
                 "When you've said it, write it on a big sticky and put it on "
                 "the Project Wall; then open your workbook (or notebook) and "
                 "copy the same sentence in — it's the north star for every "
                 "lesson after this one. After each manifesto, one line of "
                 "feedback — praise only the highlight. A manifesto missing a "
                 "part? Push with questions: 'For who?' 'Why them?' — complete "
                 "it before it goes on the wall. TA photographs the Project "
                 "Wall (wall only, no faces). When everyone's up: 'This wall "
                 "does not come down. Lesson 6, we plan around it; Lesson 10, "
                 "we present around it — we keep coming back to this wall.' "
                 "CFU: 'Everyone, point at your manifesto on the wall. (wait) "
                 "Now read your own because-clause silently. If you can say it "
                 "to your neighbor in five seconds, you're done here — go.' "
                 "NON-NEGOTIABLE round.")

    # ---------------------------------------------------------------- 10 section
    s = page(prs, 10)
    add_text(s, 0.62, 2.0, 8.76, 0.7, "The Five Rules for Talking to AI",
             size=36, bold=True, align=PP_ALIGN.CENTER)
    add_rect(s, 4.3, 2.85, 1.4, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 3.15, 8.76, 0.5, "Not magic — a craft you can practice.",
             size=18, align=PP_ALIGN.CENTER)
    set_notes(s, "Topic set. Next: a craft everyone can use — how to say things "
                 "clearly to AI. Flip straight through — no pause.")

    # ---------------------------------------------------------------- 11 compare
    s = page(prs, 11)
    add_title_bar(s, "Same AI, Same Classroom — What's the Difference?")
    add_card(s, 0.62, 1.4, 4.1, 1.3, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.8, 1.55, 3.74, 0.55, "Lesson 1, real conversation A",
             size=13.5, bold=True, line_spacing=1.1)
    add_text(s, 0.8, 2.2, 3.74, 0.35, "worked first try", size=13)
    add_text(s, 4.75, 1.85, 0.4, 0.5, "->", size=20, bold=True,
             align=PP_ALIGN.CENTER)
    add_card(s, 5.28, 1.4, 4.1, 1.3, fill=YELLOW, border=None)
    add_text(s, 5.46, 1.55, 3.74, 0.55, "Lesson 1, real conversation B",
             size=13.5, bold=True, line_spacing=1.1)
    add_text(s, 5.46, 2.2, 3.74, 0.35, "five rounds of back and forth", size=13)
    add_golden_line(s, 0.62, 2.95, 8.76, "Not luck. It's how you say it.",
                    size=17)
    add_text(s, 0.62, 3.65, 8.76, 0.7,
             "Talking to AI is like briefing a new colleague — they're smart, "
             "but they don't know what's in your head.", size=15,
             align=PP_ALIGN.CENTER, line_spacing=1.2)
    add_text(s, 0.62, 4.55, 8.76, 0.3, "(new word)", size=11, bold=True)
    add_text(s, 0.62, 4.85, 8.76, 0.3,
             "requirement — the sentence that says clearly what you want your "
             "project to do", size=12)
    set_notes(s, "Look at two real conversations from last session. This one — "
                 "worked first try. This one — five rounds of back and forth. "
                 "Same AI, same classroom. What's the difference? (pause — wait "
                 "time, let them guess) Not luck. It's how you say it. Talking "
                 "to AI isn't magic — it's a craft you can practice. The next 15 "
                 "minutes: five rules, and we verify every single one on your "
                 "own board. First, a picture: talking to AI is like briefing a "
                 "new colleague — they're smart, but they don't know what's in "
                 "your head. Students claiming their own crash conversations? "
                 "The laughter is good — let it happen. Write 'requirement' in a "
                 "corner of the whiteboard. [TA collects the two real "
                 "conversations before class; fallback: instructor's own "
                 "Rehearsal-2 comparison conversations.]")

    # ---------------------------------------------------------------- 12 rules
    s = page(prs, 12)
    add_title_bar(s, "Five Rules — Every One Verified by Hand")
    ry = 1.42
    rules = ["One thing at a time", "Say the input & the output",
             "Give it an example", "If it's wrong, add a line",
             "Ask it to explain"]
    for i, r in enumerate(rules):
        num_block(s, 0.82, ry, str(i + 1), size=0.4)
        add_text(s, 1.4, ry + 0.03, 7.9, 0.35, r, size=17, bold=True)
        ry += 0.62
    add_text(s, 0.62, 4.62, 8.76, 0.3, "(house rule, small)", size=10.5)
    add_text(s, 0.62, 4.88, 8.76, 0.3,
             "No experiments, no rules. A rule must have run on your own board "
             "to count.", size=12, bold=True)
    set_notes(s, "Five rules, meet them once. (read the titles, one by one) "
                 "Don't copy them down — the next 15 minutes, we verify every "
                 "one on your own board. Made by your own hands counts. Fast "
                 "flip to the experiments page. This page is the on-screen "
                 "mirror of the whiteboard's five titles written before class.")

    # ---------------------------------------------------------------- 13 experiments
    s = page(prs, 13)
    add_title_bar(s, "Each Rule, 3 Minutes")
    add_subtitle(s, "30 s talk  +  2 min experiment  +  30 s show the result",
                 y=1.0, size=15)
    exp = [
        ("One thing at a time",
         'first: "turn on the LED, beep the buzzer, and show something on the '
         'screen, all at once"',
         "then: split it into three sentences, one at a time — see the "
         "difference yourself"),
        ("Say the input & the output",
         'first: "make a reminder"',
         'then: "if no movement is detected for 1 minute, make the LED blink" '
         "— which one is precise?"),
        ("Give it an example",
         '"show numbers on the screen like an elevator does" — one comparison '
         "beats ten descriptions", None),
        ("If it's wrong, add a line",
         "break the effect you just made on purpose, then add one line to fix "
         "it — time it", None),
        ("Ask it to explain",
         'throw the code it just wrote back at it: "what is this doing? in '
         'plain words"', None),
    ]
    ey = 1.36
    for i, (name, first, then) in enumerate(exp):
        num_block(s, 0.62, ey + 0.01, str(i + 1), size=0.34)
        add_text(s, 1.06, ey, 8.3, 0.28, name, size=13, bold=True)
        lines = [("first:  " + first, {"size": 10.5})]
        if then:
            lines.append(("then:  " + then, {"size": 10.5}))
        add_multiline(s, 1.06, ey + 0.27, 8.3, 0.42, lines,
                      line_spacing=1.12)
        ey += 0.64
    add_text(s, 0.62, 4.64, 8.76, 0.28,
             "(fast lane)  add the Rule 3 advanced — one comparison, flashier "
             "display.", size=10.5, bold=True)
    add_text(s, 0.62, 4.94, 8.76, 0.28,
             "(slow lane)  Rules 1, 2 and 4 are enough.", size=10.5)
    set_notes(s, "The opening line for each rule is in the Teacher's Guide "
                 "(14:56-15:11); run the experiment steps projected as you go. "
                 "Rule 2's experiment is the easiest teaching moment — a vague "
                 "request produces an absurd result; circulate, collect the most "
                 "absurd one, project it, let the class laugh, then land the "
                 "point: 'It's guessing. Your project is ten times more complex "
                 "than this — you can't afford the wrong guess.' Short on "
                 "time? Cut the Rule 3 and 5 experiments — and the rules get cut "
                 "with them: point at the whiteboard and say 'try these two at "
                 "home', don't force it. Both sides of a comparison come out "
                 "equally well (AI too clever)? 'Today it guessed your mind "
                 "right — but your real project is ten times more complex. You "
                 "can't afford the wrong guess.' Then add a two-condition "
                 "request ('only light up when it's dark AND there's sound') "
                 "and run it again. Stays fixed during the experiments.")

    # ---------------------------------------------------------------- 14 exam
    s = page(prs, 14)
    add_title_bar(s, "The Final Exam")
    add_card(s, 0.62, 1.4, 8.76, 1.0, fill=CODEBG, border=INK, border_w=1.5)
    add_text(s, 0.82, 1.62, 8.36, 0.6,
             "Make something that reminds my little sister to stop playing on "
             "her phone.", size=16, mono=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.65, 8.76, 0.45, "What's wrong with that sentence?",
             size=19, bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.25, 8.76, 0.4,
             "Rewrite it with the Five Rules — send it, test it.", size=16,
             align=PP_ALIGN.CENTER)
    add_golden_line(s, 0.62, 3.95, 8.76,
                    "Works within a try or two? Read your version to the class "
                    "— and name the rule you used.", size=13)
    set_notes(s, "Final exam: 'make something that reminds my little sister to "
                 "stop playing on her phone.' What's wrong with that sentence? "
                 "Rewrite it with the Five Rules, send it, test it. Anyone whose "
                 "version works within a try or two — read it to the class. "
                 "Someone got it working? Have them read their version, then "
                 "name the rule they used ('you specified the input and the "
                 "output — that's Rule 2'). That's what mastery looks like; no "
                 "test needed. Segment wrap (no page): 'Last session's two "
                 "spells — one thing at a time, and if it's wrong, add one more "
                 "line — they're today's Rule 1 and Rule 4. Plus the error move. "
                 "All of it is printed in your Student Workbook — forget it, "
                 "flip to the page. Thirty seconds with your neighbor: which "
                 "rule hit you hardest today? — Next: the big build.'")

    # ---------------------------------------------------------------- 15 section
    s = page(prs, 15)
    add_text(s, 0.62, 2.0, 8.76, 0.7, "Build Toward Your Own Topic",
             size=36, bold=True, align=PP_ALIGN.CENTER)
    add_rect(s, 4.3, 2.85, 1.4, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 3.15, 8.76, 0.5,
             "No new tech today — combine what you know to hold up a bigger "
             "intent.", size=18, align=PP_ALIGN.CENTER)
    set_notes(s, "The big build. Look at the wall once — today we build toward "
                 "that. Flip straight through.")

    # ---------------------------------------------------------------- 16 first piece
    s = page(prs, 16)
    add_title_bar(s, "For Your Topic, Make Its First Working Piece")
    num_block(s, 0.62, 1.32, "1", size=0.36)
    add_text(s, 1.06, 1.34, 8.3, 0.3,
             "Cut a small slice out of your topic and build it (recommended)",
             size=14, bold=True)
    num_block(s, 0.62, 1.72, "2", size=0.36)
    add_text(s, 1.06, 1.74, 8.3, 0.3,
             "No direction? Pick one of the three starter briefs", size=14,
             bold=True)
    bx = 0.62
    for name in ["Reminder", "Night Light", "Alarm"]:
        add_card(s, bx, 2.15, 2.0, 0.55, fill=WHITE, border=INK, border_w=1.5)
        add_text(s, bx, 2.27, 2.0, 0.32, name, size=14, bold=True,
                 align=PP_ALIGN.CENTER)
        bx += 2.1
    add_text(s, 0.62, 2.78, 8.76, 0.28,
             "(reference combos on the back)", size=10.5, align=PP_ALIGN.CENTER)
    # two tracks
    add_text(s, 0.62, 3.15, 4.3, 0.3, "WITH THE PARTS BOX (if you have one)",
             size=12, bold=True)
    yellow_box(s, 0.62, 3.45, 4.3, 1.55, [
        "First wiring — one rule only:",
        '"One end into the module, the other into the socket on the edge of '
        'the board. Plug it in wrong and nothing burns — just flip it around."'],
        size=11.5)
    add_text(s, 5.08, 3.15, 4.3, 0.3, "NO PARTS BOX", size=12, bold=True)
    add_card(s, 5.08, 3.45, 4.3, 1.55, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 5.26, 3.58, 3.94, 1.3, [
        "Today we use the modules already on your board —",
        "light, sound, button, LED, buzzer, screen.",
        "Two linked modules, no problem.",
    ], size=11.5, line_spacing=1.3)
    set_notes(s, "You just set your topic — now make its first working piece. "
                 "Two options: one, cut a small slice out of your topic and "
                 "build it (recommended); two, no direction yet? Pick one of "
                 "the three starter briefs — Reminder, Night Light, Alarm — "
                 "reference combos on the back. With the kit: 'Now look at the "
                 "new thing on your table: the parts box. Last session the parts "
                 "on your board were soldered on — today these modules you wire "
                 "yourself. First wiring, one rule only: one end into the "
                 "module, the other into the socket on the edge of the board; "
                 "plug it in wrong and nothing burns — just flip it around. "
                 "Watch once. (use the Rehearsal-3 servo demo)' — name the "
                 "modules before hands touch them. No kit: 'Today we use the "
                 "modules already on your board — last session's friends: "
                 "light, sound, button, LED, buzzer, screen. Two linked "
                 "modules, no problem. Straight to the design sheet.' A topic "
                 "that really can't be sliced small? The TA maps it 'near "
                 "enough' onto a starter brief: 'This is the practice piece for "
                 "your topic.' [Parts-box photo asset: kit classes only — "
                 "corner label 'if you have one'.]")

    # ---------------------------------------------------------------- 17 design sheet
    s = page(prs, 17)
    add_title_bar(s, "Hands Off the Keyboard — 5 Minutes, Fill Your Design Sheet")
    add_card(s, 0.62, 1.35, 8.76, 1.9, fill=CODEBG, border=INK, border_w=1.5)
    add_multiline(s, 0.86, 1.5, 8.28, 1.65, [
        ("My project is called: ___", {"size": 13, "mono": True}),
        ("Who it's for (write a real person's name): ___", {"size": 13,
                                                             "mono": True}),
        ("Sense: ___  ->  Logic: ___  ->  Output: ___", {"size": 13,
                                                         "mono": True}),
        ("Modules I'll use (tick the onboard ones; circle the parts-box extras "
         "if you have one): ___", {"size": 13, "mono": True}),
    ], line_spacing=1.55)
    add_text(s, 0.62, 3.45, 8.76, 0.4,
             "The hourglass runs out — then you build.", size=16, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.9, 8.76, 0.35,
             "Start, and the build becomes yours as you go.", size=14,
             align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 4.45, 8.76, 0.7, [
        "This design sheet is your design document — building, review, log: "
        "everything checks against it."], size=12.5)
    set_notes(s, "Hands off the keyboard. Design sheet, 5-minute hourglass: "
                 "what's your project called, who's it for (a real name), "
                 "Sense ___ -> Logic ___ -> Output ___, which modules. When the "
                 "hourglass runs out, you build — start, and the build becomes "
                 "yours as you go. Writing 'who it's for'? Look at the wall "
                 "once. This design sheet is your design document — building, "
                 "review, log: everything checks against it. Free-choice design "
                 "sheets must pass the TA's eye before building starts; "
                 "starter-brief sheets start right away. Still hesitating at 5 "
                 "minutes? Pull a starter brief and start with the reference "
                 "combo.")

    # ---------------------------------------------------------------- 18 big build
    s = page(prs, 18)
    add_text(s, 0.62, 1.05, 3.4, 1.75, "51", size=96, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.88, 3.4, 0.5, "minutes", size=26, bold=True,
             align=PP_ALIGN.CENTER)
    ry = 1.5
    build_rules = [
        "One thing at a time",
        "If it's wrong, add one line",
        "Stuck? Ask your AI first, then your neighbor, then raise your hand",
    ]
    for i, r in enumerate(build_rules):
        num_block(s, 4.3, ry, str(i + 1), size=0.4)
        add_text(s, 4.88, ry + 0.03, 4.7, 0.6, r, size=15, bold=True,
                 line_spacing=1.05)
        ry += 0.72
    add_golden_line(s, 4.3, 3.7, 4.7,
                    "Cut a small slice and make it solid — directors shoot one "
                    "scene at a time. Get the link working first, then decorate.",
                    size=13)
    set_notes(s, "Start signal: 'Go. Three rules: one thing at a time; if it's "
                 "wrong, add a line; stuck? Ask your AI first, then your "
                 "neighbor, then raise your hand.' Circulation points (never on "
                 "screen): midway (~16:00) one whole-room callout — 'Stop, 10 "
                 "seconds — check against your design sheet: are you still "
                 "building the thing you wrote?'; watch for THE LINK — two "
                 "modules doing their own separate things doesn't count: 'make "
                 "the one on the left tell the one on the right something'; a "
                 "student dumps the whole job on AI — 'directors shoot one "
                 "scene at a time: get the link working first, then decorate.' "
                 "Someone badly behind (16:10, no successful flash)? Move them "
                 "to the instructor demo spot, target drops to 'one linked "
                 "build runs'. Fast student done before 16:00? No early review "
                 "— challenge task (rehearsed ones only) or send them to help "
                 "a slow student (mouth only, hands off the keyboard). Link "
                 "won't come together? Minimal definition first, then lower the "
                 "bar to 'one project + one record of the linking attempt' — "
                 "log the sticking point, still counts. 16:21, kit classes only "
                 "— the wiring-check callout: 'Hands up, everyone — wiring "
                 "check: modules facing the right way? Cables pushed all the "
                 "way in at both ends? Sockets matched? 30 seconds, check your "
                 "neighbor's once.' No kit? Skip the call-out — those 5 minutes "
                 "become TA circulation + nudging slow students to wrap up. "
                 "Stays fixed during the build.")

    # ---------------------------------------------------------------- 19 review
    s = page(prs, 19)
    add_title_bar(s, "Review — Ask Someone to Find the Flaws")
    add_card(s, 0.62, 1.3, 5.4, 1.35, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 0.8, 1.42, 5.04, 1.15, [
        ("Please play ___ (the real name on your", {"size": 11.5, "mono": True}),
        ("design sheet).", {"size": 11.5, "mono": True}),
        ("Find exactly ONE flaw in my project.", {"size": 11.5, "mono": True,
                                                  "bold": True}),
        ("Just one.", {"size": 11.5, "mono": True, "bold": True}),
    ], line_spacing=1.35)
    add_card(s, 6.2, 1.3, 3.18, 1.35, fill=WHITE, border=INK, border_w=1.0)
    add_multiline(s, 6.36, 1.42, 2.86, 1.15, [
        ("[ demo", {"size": 10.5, "bold": True}),
        ("screenshot ]", {"size": 10.5, "bold": True}),
        ("AI plays \"my mom, someone who's", {"size": 9.5}),
        ("not great with electronics\"", {"size": 9.5}),
        ("-> finds one flaw", {"size": 9.5}),
    ], line_spacing=1.3, align=PP_ALIGN.CENTER)
    num_block(s, 0.62, 2.85, "1", size=0.36)
    add_text(s, 1.06, 2.87, 8.3, 0.55,
             "Exactly one flaw — the first review must be \"useful and painless\"",
             size=13.5, bold=True, line_spacing=1.1)
    num_block(s, 0.62, 3.5, "2", size=0.36)
    add_text(s, 1.06, 3.52, 8.3, 0.55,
             "Review isn't abstract fault-finding — it's finding flaws for that "
             "one real person", size=13.5, line_spacing=1.1)
    add_text(s, 0.62, 4.25, 8.76, 0.55,
             "(small)  \"The Picky User\" gets expanded in Lesson 4 — today, "
             "project and use it; that's enough.", size=11,
             align=PP_ALIGN.CENTER)
    set_notes(s, "Keep your builds out. Today, a new segment for the first "
                 "time: review — asking someone to find the flaws in your "
                 "project. Today's reviewer is AI, but it plays a real person. "
                 "Watch the demo. (project the Rehearsal-4 conversation) I had "
                 "it play my mom — someone who's not great with electronics — "
                 "and it found one flaw. Your turn: send your project "
                 "description to AI, starting with 'please play ___' — the real "
                 "name on your design sheet — 'find exactly ONE flaw in my "
                 "project. Just one.' Note: review isn't abstract "
                 "fault-finding — it's finding flaws for that one real person. "
                 "One flaw is a designed dose — a student asking for more? Hold "
                 "them back: 'one at a time, you can't eat more than that.' "
                 "First flaw lands too harshly or absurdly? Handle it in "
                 "public: 'AI's opinion gets reviewed too — do you think it's "
                 "right?' A student upset by the flaw? Catch the feeling first "
                 "— strong emotions -> private talk. A build doesn't run at "
                 "review time? Review it anyway — AI finds flaws in the design, "
                 "not the bug; 'not running yet' is itself the best 'stuck on' "
                 "for the log. [Rehearsal-4 screenshot doubles as the "
                 "projection demo; missing -> live demo on the real interface.]")

    # ---------------------------------------------------------------- 20 decision
    s = page(prs, 20)
    add_title_bar(s, "You've Got the Flaw — Now Make a Decision")
    add_card(s, 0.62, 1.4, 4.1, 1.05, fill=YELLOW, border=None)
    add_text(s, 0.8, 1.55, 3.74, 0.35, "CHANGE IT", size=17, bold=True)
    add_text(s, 0.8, 1.95, 3.74, 0.35, "do it right now", size=13.5)
    add_card(s, 5.08, 1.4, 4.1, 1.05, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.26, 1.55, 3.74, 0.35, "DON'T CHANGE IT", size=17, bold=True)
    add_text(s, 5.26, 1.95, 3.74, 0.35, "tell your neighbor why", size=13.5)
    add_golden_line(s, 0.62, 2.75, 8.76,
                    "Accepting earns credit — and so does rejecting, as long as "
                    "the reason is yours.", size=16)
    yellow_box(s, 0.62, 3.5, 8.76, 0.95, [
        'Write one line in your workbook:',
        '"I accepted/rejected AI\'s suggestion, because ___."'],
        title="Write it down:", size=13.5)
    add_text(s, 0.62, 4.65, 8.76, 0.35, "Your proof of being the director.",
             size=15, bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "You've got the flaw. Now make a decision: change it, or not. "
                 "Change it — do it right now. Don't change it — tell your "
                 "neighbor why. Say it clearly: accepting earns credit, and so "
                 "does rejecting — as long as the reason is yours. Actively "
                 "find one well-reasoned rejection and praise it out loud: "
                 "'They turned down AI's suggestion, because ___ — that reason "
                 "stands. Knowing how to refuse is what real trade-offs look "
                 "like.' The decision and the reason must go into today's log. "
                 "Fast student already done? Give the reverse challenge — hand "
                 "their project to their neighbor to review. The whole class "
                 "accepts (nobody dares to reject)? You model a rejection live: "
                 "'AI also found a flaw in my demo project — said the reminder "
                 "sound is too soft. I'm not changing it, because my mom's "
                 "hearing is fine; a louder sound would just wake her from her "
                 "nap. See? A rejection with a reason counts the same.' Someone "
                 "can't say why? Squeeze the reason out: 'did it hit the mark, "
                 "or are you changing it because you don't know what else to "
                 "do?' Output anchor: the one-line accept/reject decision in "
                 "everyone's workbook.")

    # ---------------------------------------------------------------- 21 log (RED)
    s = page(prs, 21)
    add_title_bar(s, "Flash Show & Tell + Your AI Log")
    add_text(s, 0.62, 1.28, 8.76, 0.55,
             "Show & tell: in your table, 30 seconds each — demo your build, say "
             "one line: \"what AI found, and whether I changed it\"",
             size=13, line_spacing=1.15)
    add_text(s, 0.62, 1.95, 8.76, 0.3, "Your log, four sentences:", size=13.5,
             bold=True)
    ly = 2.3
    for line in ["Today I made ___", "I got stuck on ___",
                 "Then ___  (today's \"then\": include how you handled the flaw)",
                 "Next time I want ___"]:
        add_yellow_dot_item(s, 0.72, ly, 8.4, line, size=12.5)
        ly += 0.32
    add_text(s, 0.62, 3.65, 8.76, 0.3,
             'Say it, then send it to AI with one more line:', size=12)
    add_grey_box(s, 0.62, 3.95, 8.76, 0.5,
                 '"Tidy this into a learning log — only what I said, nothing I '
                 'didn\'t say."', size=12)
    add_red_rule_box(s, 0.62, 4.6, 8.76, 0.85, "Warning",
                     ["AI will make things up with a straight face. "
                      "Proofreading is your job."], body_size=13)
    add_text(s, 5.5, 1.28, 3.9, 0.5,
             "(small) Take one photo — your build and your design sheet "
             "together. Two pieces of paper, one board — all made by you.",
             size=10)
    set_notes(s, "In your table, 30 seconds each: demo your build, say one "
                 "line — 'what AI found, and whether I changed it'. Then "
                 "today's log — take one photo: your build and your design "
                 "sheet together, two pieces of paper, one board — all made by "
                 "you. Say thirty seconds, the usual four sentences: today I "
                 "made ___ / I got stuck on ___ / then ___ / next time I want "
                 "___ — and for today's 'then', include how you handled the "
                 "flaw. Then the AI-tidy line, then the proofreading duty — "
                 "'AI will make things up with a straight face. Proofreading is "
                 "your job.' (The red warning is this deck's single red "
                 "element.) The TA takes extra build photos and the Project "
                 "Wall (hands only, no faces); the design-sheet + build photo "
                 "is today's most valuable material — everyone must have one. "
                 "A student with no phone? TA photographs everything, filed by "
                 "table number.")

    # ---------------------------------------------------------------- 22 close
    s = page(prs, 22)
    add_title_bar(s, "Six Skills — Today You Practiced Three")
    sy = 1.35
    skills = [
        ("Spot a problem", "from 10 ideas you fixed your own topic and said "
         "who it's for"),
        ("Build it", "you directed AI to make your first combination build"),
        ("Make trade-offs", "the first \"change it or not\" decision of your "
         "life"),
    ]
    for i, (head, body) in enumerate(skills):
        num_block(s, 0.62, sy, str(i + 1), size=0.4)
        add_text(s, 1.2, sy - 0.02, 3.0, 0.3, head, size=15, bold=True)
        add_text(s, 1.2, sy + 0.28, 7.9, 0.3, body, size=12)
        sy += 0.72
    add_text(s, 0.62, 3.6, 8.76, 0.32, "NEXT TIME", size=13, bold=True,
             align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 3.95, 8.76, 1.1, [
        "Lesson 3: Give Your Project a Screen",
        "New gear: the Wio Terminal — a handheld with a color screen"],
        size=14)
    add_text(s, 0.62, 5.1, 8.76, 0.28,
             "Bring your topic. After class: online docs get links, "
             "handwritten gets photographed — you'll need it at the start of "
             "Lesson 3.", size=10.5, align=PP_ALIGN.CENTER)
    set_notes(s, "Last two minutes — take stock. One: from 10 ideas you fixed "
                 "your own topic and said who it's for — that's spotting a "
                 "problem. Two: you directed AI to make your first combination "
                 "build — building it, one step further. Three: you made the "
                 "first 'change it or not' decision of your life — that's making "
                 "trade-offs. Six skills, and today you practiced three. Next "
                 "session, new gear: a handheld with a color screen — the Wio "
                 "Terminal. We're going to give your project a screen — from "
                 "today, your builds have a real interface. Bring your topic. "
                 "Class dismissed! Have students look at the Project Wall once "
                 "— today everyone's name is on it. After class: collect the "
                 "outputs (links or photos); note whether you got them all — "
                 "you'll need it at the start of Lesson 3.")

    prs.save(OUT)
    print("Saved:", OUT, "slides:", len(prs.slides.__iter__.__self__._sldIdLst))


if __name__ == "__main__":
    main()
