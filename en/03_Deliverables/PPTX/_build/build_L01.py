"""
Build the English Lesson 1 deck (Sense and Respond, 28 slides, 3 h)
from M0_EN_PPTPlan_CFG-5_Lesson01_SenseAndRespond_v1.md (brand rebuild).

Output: 交付物_EN/03_Deliverables/PPTX/M0_EN_Deck_CFG-5_Lesson01_SenseAndRespond_v1.pptx
Layout per chaihuo-ppt-brand.md: white 70 / yellow 15 / ink 10 / red 5, 960x540.
Red budget: slide 17 (BAD example) and slide 27 (proofreading warning) only.
No CJK / full-width / emoji glyphs on screen — ASCII-only screen text.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder_lib import *
from pptx.util import Inches

TOTAL = 28
DECK_LABEL = "Sense and Respond"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson01_SenseAndRespond_v1.pptx")
KIT_PHOTO = "/Users/leonfeng/Baiduyun/M0/M0-V2/素材/L1_板子全貌图_Grove Beginner Kit.png"


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
        add_multiline(s, tx, ty, tw, th, lines, size=size, line_spacing=line_spacing)


def kit_map(s, x, y, w, h, hl):
    """Grove Beginner Kit board schematic; hl = set of zone names to highlight (yellow)."""
    add_card(s, x, y, w, h, fill=WHITE, border=INK, border_w=1.5)
    zones = [
        ("GROVE PORTS", 0.05, 0.06, 0.90, 0.12),
        ("SENSING x5",  0.05, 0.26, 0.90, 0.16),
        ("INTERACTING", 0.05, 0.55, 0.26, 0.36),
        ("BRAIN",       0.36, 0.55, 0.28, 0.36),
        ("SPEAKING",    0.67, 0.55, 0.28, 0.36),
    ]
    for name, rx, ry, rw, rh in zones:
        zx, zy, zw, zh = x + rx * w, y + ry * h, rw * w, rh * h
        fill = YELLOW if name in hl else WHITE
        add_rect(s, zx, zy, zw, zh, fill=fill, border=INK, border_w=1.0)
        add_text(s, zx + 0.04, zy + 0.03, zw - 0.08, zh - 0.06, name, size=9,
                 bold=True, align=PP_ALIGN.CENTER)


def main():
    prs = new_deck()

    # ---------------------------------------------------------------- 01 cover
    s = page(prs, 1)
    add_text(s, 0.62, 1.35, 5.8, 0.35,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0)",
             size=14, align=PP_ALIGN.LEFT)
    add_text(s, 0.62, 1.72, 5.8, 0.85, "Sense and Respond",
             size=44, bold=True, align=PP_ALIGN.LEFT)
    add_rect(s, 0.62, 2.62, 1.6, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 2.95, 5.8, 0.4,
             "Grove Beginner Kit · IoT Starter Board · M0 Lesson 1",
             size=15, align=PP_ALIGN.LEFT)
    add_text(s, 0.62, 3.5, 5.8, 0.5,
             "Can't write code? Good. This course doesn't need it.",
             size=18, bold=True, align=PP_ALIGN.LEFT)
    s.shapes.add_picture(KIT_PHOTO, Inches(6.6), Inches(1.5), Inches(3.2),
                         Inches(2.4))
    add_text(s, 6.6, 4.0, 3.2, 0.3, "Grove Beginner Kit for Arduino",
             size=12, align=PP_ALIGN.CENTER)
    set_notes(s, "Cover — loops before class. Open with silence, then one welcome "
                 "line and go straight to the live demo — the cover is not a talking "
                 "page. Board render on the right (existing kit asset).")

    # ---------------------------------------------------------------- 02 demo
    s = page(prs, 2)
    add_title_bar(s, "Three Sentences, and the Board Sends a Distress Signal")
    add_rect(s, 0.62, 1.35, 8.76, 2.35, fill=INK, border=None)
    add_multiline(s, 0.92, 1.5, 8.16, 2.05,
                  ['Round 1  "Write a program that makes the Beginner Kit LED '
                   'blink every 500 ms."',
                   "",
                   'Round 2  "While the LED is on, the buzzer beeps; when the LED '
                   'is off, stop."',
                   "",
                   'Round 3  "Use Morse code to send a repeating sound-and-light '
                   'SOS."'],
                  size=11.5, color=YELLOW, font=MONO, line_spacing=1.35)
    add_text(s, 0.62, 3.85, 8.76, 0.35,
             "SOS = ... --- ... (three short, three long, three short)",
             size=17, bold=True, font=MONO, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 4.3, 8.76, 0.55,
             "Watch closely: he's typing plain English, not code — and all three "
             "lines go in the SAME conversation.", size=14, align=PP_ALIGN.CENTER)
    set_notes(s, "The projector is background; the star is the instructor typing "
                 "live in front of the class, slowly, so everyone sees plain "
                 "language going in. Three rounds build in the same conversation "
                 "(this is the silent first demo of 'add one more line'). Say "
                 "nothing until the board sends SOS; the laughter and the 'ohhhh' "
                 "are the point. Nothing Chinese goes on screen — the demo was "
                 "chosen exactly for this. Demo fails -> cut to the backup "
                 "recording (video asset on the asset checklist, slide 02) within "
                 "30 seconds: 'The board in this video is identical to the ones on "
                 "your desks — you'll do the real thing yourselves in a minute.' "
                 "Not an incident.")

    # ---------------------------------------------------------------- 03 what happened
    s = page(prs, 3)
    add_title_bar(s, "What Just Happened?")
    steps = [
        ("01", "I said it in plain English", "(a website called Codecraft)"),
        ("02", "AI wrote it as instructions", "(that stuff is called code)"),
        ("03", "The instructions moved into the board", "(that step is called flashing)"),
        ("04", "The board remembered", "(three sentences, and it's sending SOS)"),
    ]
    y = 1.42
    for num, main, sub in steps:
        num_block(s, 0.62, y, num)
        add_text(s, 1.22, y + 0.02, 4.9, 0.4, main, size=16, bold=True)
        add_text(s, 6.2, y + 0.02, 3.2, 0.55, sub, size=13.5)
        y += 0.62
    add_golden_line(s, 0.62, 4.45, 8.76,
                    "This isn't magic — it's the exact path you'll walk yourself "
                    "in a minute.", size=13.5, h=None)
    set_notes(s, "The most important 30-second 'landing' of the whole session. Say "
                 "it once, hot off the demo (verbatim from the Teacher's Guide): "
                 "'I'm on a website called Codecraft. I told AI in three plain "
                 "sentences what I wanted. AI wrote it out as instructions the "
                 "board understands — that stuff is called code. Once, a person "
                 "had to type every line by hand; today it typed them for me. Then "
                 "the computer moved the instructions through this cable into the "
                 "board — that step is called flashing. Once it's in, the board "
                 "remembers — even unplugged. I wrote zero lines of code. Three "
                 "sentences, and it's sending a distress signal.' Without this "
                 "page, students remember 'the teacher does magic'; with it, they "
                 "remember 'I can do this too.'")

    # ---------------------------------------------------------------- 04 three questions
    s = page(prs, 4)
    add_title_bar(s, "Three Questions")
    qs = [
        (1.75, "Did I just write any code?"),
        (2.55, "Who in this room knows how to code?"),
    ]
    for y, q in qs:
        add_oval(s, 1.5, y + 0.02, 0.42, fill=YELLOW, border=None)
        add_text(s, 1.5, y + 0.06, 0.42, 0.34, str(qs.index((y, q)) + 1),
                 size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        add_text(s, 2.1, y, 6.4, 0.5, q, size=22, bold=True)
    add_oval(s, 1.5, 3.37, 0.42, fill=YELLOW, border=None)
    add_text(s, 1.5, 3.41, 0.42, 0.34, "3", size=15, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER)
    add_multiline(s, 2.1, 3.35, 6.4, 0.95,
                  ["Without knowing a single line of code,",
                   "could you make that thing I just made?"],
                  size=22, bold=True)
    set_notes(s, "The pauses are the soul of this bit. Pause two seconds after "
                 "each; let the 'yes' come out of their mouths: 'Number one: did "
                 "I just write any code? (pause) Number two: who in this room "
                 "knows how to code? (pause — probably no hands) Number three: "
                 "without knowing a single line of code, could you make that thing "
                 "I just made? (pause) Yes. That's this course.' Don't rush; "
                 "don't answer for them.")

    # ---------------------------------------------------------------- 05 kickoff
    s = page(prs, 5)
    add_title_bar(s, "The Kickoff in 30 Seconds")
    cards = [
        ("YOUR ROLE", [
            "Not a programming class — you're the director, AI is the programmer.",
            "House rule: no hand-written code. Say it clearly, watch what "
            "happens, tell it to change."]),
        ("THE WHOLE MAP", [
            "A project takes eight steps: frame the problem, find the user, "
            "prototype, code, make trade-offs, test and judge, document, share "
            "the value.",
            "Today we take steps 3 and 4."]),
        ("WHAT WE PRACTICE TODAY", [
            "Two skills: build it — and tell the story of how you built it."]),
    ]
    x = 0.62
    for title, lines in cards:
        add_card(s, x, 1.45, 2.8, 2.75, fill=WHITE, border=INK, border_w=1.0)
        add_rect(s, x, 1.45, 2.8, 0.34, fill=YELLOW, border=None)
        add_text(s, x, 1.49, 2.8, 0.28, title, size=11, bold=True,
                 align=PP_ALIGN.CENTER)
        add_multiline(s, x + 0.15, 1.93, 2.5, 2.15, lines, size=12,
                      line_spacing=1.25)
        x += 3.0
    add_text(s, 0.62, 4.45, 8.76, 0.4,
             "Missed the kickoff? Remember these three lines and you'll keep up "
             "today.", size=13, align=PP_ALIGN.CENTER)
    set_notes(s, "Walk the three cards fast (about 3 min), then the three house "
                 "rules (30 s, verbatim): 'One: you don't need to understand the "
                 "code AI writes — your job is to say it clearly, watch what "
                 "happens, and tell it to change. Two: no hand-written code — not "
                 "because code doesn't matter, but because this course trains "
                 "something more valuable than code. Three: when you're stuck, "
                 "say so — ask your AI first, then your neighbor, then raise your "
                 "hand.' Then point at the 8-step map on the whiteboard (2 min, "
                 "names only, no expansion): 'Most people think AI only helps "
                 "with step four — the code. Not this course: all eight steps, "
                 "you learn to make AI your partner. Today we take steps three "
                 "and four.' Hard time-box: 5 min total for map + rules.")

    # ---------------------------------------------------------------- 06 six skills
    s = page(prs, 6)
    add_title_bar(s, "What This Course Trains")
    add_subtitle(s, "Today we practice two: Build it — and Tell the story of how "
                    "you built it.", size=15.5)
    skills = [
        ("Spot a problem", False), ("Find the user", False), ("Build it", True),
        ("Make trade-offs", False), ("Judge quality", False), ("Tell the story", True),
    ]
    x, y = 0.62, 1.75
    for name, hot in skills:
        fill = YELLOW if hot else WHITE
        add_card(s, x, y, 2.8, 0.9, fill=fill, border=INK, border_w=1.0)
        add_text(s, x, y + 0.24, 2.8, 0.4, name, size=15, bold=True,
                 align=PP_ALIGN.CENTER)
        x += 3.0
        if x > 9.0:
            x = 0.62
            y += 1.12
    add_text(s, 0.62, 4.15, 8.76, 0.5,
             "AI writes the code — these six, it can't do for you.",
             size=16, bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "'This course trains six skills: spot a problem, find the user, "
                 "build it, make trade-offs, judge quality, tell the story. AI "
                 "writes the code — these six, it can't do for you. Today we "
                 "practice two: build it, and tell the story of how you built "
                 "it.' Keep it light; all six come back by doing. Two cells "
                 "highlighted (build it / tell the story) — the pair today's "
                 "session actually trains.")

    # ---------------------------------------------------------------- 07 icebreaker
    s = page(prs, 7)
    add_title_bar(s, "The One Thing I'd Most Like AI to Do for Me")
    add_text(s, 0.62, 2.15, 8.76, 0.5, "With your neighbor: 15 seconds each.",
             size=20, bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.85, 8.76, 0.4,
             "The smaller and more real, the better.", size=15,
             align=PP_ALIGN.CENTER)
    add_rect(s, 4.4, 3.5, 1.2, 0.05, fill=YELLOW, border=None)
    set_notes(s, "Self-disclose first, one real small thing of your own (I want "
                 "AI to remind my mom to drink water — swap in your own; the "
                 "smaller, the better): 'With your neighbor, 15 seconds each — "
                 "'the one thing I'd most like AI to do for me'. I'll go first — "
                 "...' Dead silence? Self-disclose one more, even smaller ('I "
                 "want AI to remind me to grab my keys when I leave'), then call "
                 "directly on the student you know best. Never let silence run "
                 "past 10 seconds. TA notes the gold answers — reusable in later "
                 "sessions.")

    # ---------------------------------------------------------------- 08 login
    s = page(prs, 8)
    add_title_bar(s, "Everyone Logs In")
    yellow_box(s, 0.62, 1.35, 8.76, 1.1, [
        "A website — where you talk to AI, and where AI writes",
        "the instructions for your board. That's the site you just saw me use."],
        title="What is Codecraft?", size=13)
    add_text(s, 0.62, 2.55, 8.76, 0.45, "codecraft.seeed.cc", size=24, bold=True,
             font=MONO, align=PP_ALIGN.CENTER)
    y = 3.1
    for num, line in [
        ("1", "Open your browser, go to the address above"),
        ("2", "Log in with the account on your seat card — just log in, don't "
              "click around yet"),
    ]:
        num_block(s, 1.5, y + 0.02, num)
        add_text(s, 2.1, y, 6.4, 0.5, line, size=15.5)
        y += 0.62
    add_rect(s, 0.62, 4.45, 8.76, 0.55, fill=YELLOW, border=None)
    add_text(s, 0.8, 4.55, 8.4, 0.35,
             "The address and your account details are on your seat card.",
             size=14, bold=True)
    set_notes(s, "'Now — open your browser, go to codecraft.seeed.cc — the site I "
                 "used in the demo. It's called Codecraft. It's where you talk to "
                 "AI, and where AI writes the instructions for your board. Log in "
                 "with the account on your seat card. Just log in — don't click "
                 "around yet.' Before the next segment starts, login problems "
                 "must be at zero — TA circulates fixing against the paper seat "
                 "map.")

    # ---------------------------------------------------------------- 09 section cover
    s = page(prs, 9)
    add_rect(s, 0.62, 1.35, 8.76, 2.7, fill=INK, border=None)
    add_text(s, 0.62, 2.05, 8.76, 0.8, "Name Lighting", size=40, bold=True,
             color=YELLOW, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.0, 8.76, 0.5, "Put Your Name on the Screen", size=20,
             color=WHITE, align=PP_ALIGN.CENTER)
    set_notes(s, "'Demo seen, ideas explained. Next thirty minutes are yours — "
                 "every single board in this room lights up your own name. No "
                 "exceptions.' Clean section page — no timing, no handout info.")

    # ---------------------------------------------------------------- 10 meet your board
    s = page(prs, 10)
    add_title_bar(s, "Meet Your Board")
    s.shapes.add_picture(KIT_PHOTO, Inches(0.62), Inches(1.35), Inches(4.27),
                         Inches(3.2))
    add_multiline(s, 5.05, 1.4, 4.3, 1.7, [
        "The main board in the middle — its brain (AI has the ideas; you make "
        "the decisions)",
        "Screen, light, little speaker — its face and voice",
        "Sensors — its eyes and ears: feels light, feels sound, feels "
        "temperature",
        "Button and knob — how you operate it",
        "USB port — plug in here today",
    ], size=12.5, line_spacing=1.22)
    yellow_box(s, 5.05, 3.15, 4.3, 1.45, [
        "a tiny computer. Dumber than",
        "your phone, but give it one job",
        "and it'll do it all day, for a year,",
        "without complaining."],
        title="It's called a development board —", size=12)
    add_rect(s, 5.05, 4.55, 4.3, 0.65, fill=YELLOW, border=None)
    add_multiline(s, 5.23, 4.63, 3.94, 0.5, [
        "The little modules can be snapped off and",
        "used separately later — not today.",
        "Today nothing snaps.",
    ], size=11, line_spacing=1.2)
    set_notes(s, "90 seconds max, no theory. Hold up a real board and point as "
                 "you go (verbatim from the Teacher's Guide). End with: 'Today "
                 "you're going to make it speak your name. Now — plug in the USB "
                 "cable, one end in the computer, one end in the board.'")

    # ---------------------------------------------------------------- 11-15 kit tour
    kit_notes = [
        (11, "The Grove Beginner Kit (Overview)", "GROVE_PORTS,SENSING x5,INTERACTING,BRAIN,SPEAKING",
         ["This board's full name: the Grove Beginner Kit for Arduino — in "
          "class, just 'the starter kit'.",
          "One of the best Arduino starter kits out there: no soldering, no "
          "complicated wiring — your only job is making it do what you say.",
          "Next four pages: meet its parts, fast."],
         "'This board's full name: the Grove Beginner Kit for Arduino — in "
         "class, just 'the starter kit'. One of the best Arduino starter kits "
         "out there: no soldering, no complicated wiring — your only job is "
         "making it do what you say. Next four pages: meet its parts, fast.'"),
        (12, "The Kit — Sensing (its eyes and ears)", "SENSING x5",
         ["light", "sound", "temperature and humidity", "barometer",
          "accelerometer",
          "The dark-detecting light uses that eye — the light sensor."],
         "'Its eyes and ears.' — 'This one feels light, this one feels sound, "
         "this one feels heat and moisture, this one feels air pressure, this "
         "one can feel being touched or shaken. The dark-detecting light in a "
         "minute uses that 'eye' — the light sensor.'"),
        (13, "The Kit — Speaking (its voice and face)", "SPEAKING",
         ["the screen shows words", "the light glows", "the buzzer beeps",
          "Your name lights up on this little screen today."],
         "'Its face and voice.' — 'The screen shows words, the light glows, "
         "the buzzer beeps. Your name lights up on this little screen today.'"),
        (14, "The Kit — Interacting (how you operate it)", "INTERACTING",
         ["a button", "a knob",
          "Press, twist — the board can feel both. Build 3 puts them to work."],
         "'Where you operate it.' — 'These two are for you: a button and a "
         "knob. Press, twist — the board can feel both. Build 3 will put them "
         "to work.'"),
        (15, "The Kit — The Brain and the Grove Ports", "BRAIN,GROVE PORTS",
         ["The instructions AI writes all live here.",
          "This row of Grove ports is for later: snap a module off, plug it "
          "out, build something bigger. Not today — today nothing snaps."],
         "'Last, the brain — the main board in the middle. The instructions AI "
         "writes all live here. This row of Grove ports around the edge is for "
         "later: snap a module off, plug it out, build something bigger. Not "
         "today — today nothing snaps.'"),
    ]
    for n, title, hl, right_lines, note in kit_notes:
        s = page(prs, n)
        add_title_bar(s, title)
        kit_map(s, 0.62, 1.45, 5.3, 3.3, set(hl.split(",")))
        add_multiline(s, 6.25, 1.6, 3.15, 2.9, right_lines, size=13,
                      line_spacing=1.25)
        set_notes(s, note)

    # ---------------------------------------------------------------- 16 connect
    s = page(prs, 16)
    add_title_bar(s, "Connect Codecraft — five steps to lit")
    steps16 = [
        ("1", "Pick your board — click Grove Beginner Kit"),
        ("2", "Type your request in the box, click send"),
        ("3", "Click the green button: Connect and Flash"),
        ("4", "Pick the serial port, then Connect"),
        ("5", "It flashes automatically — watch the board"),
    ]
    y = 1.4
    for num, line in steps16:
        num_block(s, 0.62, y + 0.02, num)
        add_text(s, 1.22, y, 7.8, 0.45, line, size=16)
        y += 0.6
    yellow_box(s, 0.62, 4.4, 8.76, 0.78, [
        "Which serial row? The one with CP2102N / USB — not the Bluetooth row. "
        "No popup? Clicked Cancel by accident? Click Connect and Flash again — "
        "still stuck, raise your hand: a TA will fix it in 2 minutes."],
        size=12)
    set_notes(s, "Project and lead the whole class in lockstep; don't let fast "
                 "students run ahead (a fast one connects early — have them "
                 "wait; don't let the pack scatter). 'This step is called "
                 "connecting. What's it for? Getting the computer and the board "
                 "talking — the instructions AI wrote need to travel down this "
                 "USB cable into the board.' TA watches two things: popup never "
                 "appearing (browser problem) and accidental Deny clicks (just "
                 "click connect again). Serial list empty? Nine times out of ten "
                 "the cable carries power but no data — swap the cable. Fix "
                 "within 2 minutes, else swap to a spare machine.")

    # ---------------------------------------------------------------- 17 spell 1 (red)
    s = page(prs, 17)
    add_title_bar(s, "Spell 1 | One Thing at a Time")
    add_grey_box(s, 0.62, 1.3, 8.76, 0.9,
                 "I'm using the Grove Beginner Kit. Please do one thing for me: "
                 "___ (just one).  It counts as done when ___. Please don't add "
                 "other features yet.", size=12.5)
    add_rect(s, 0.62, 2.45, 1.0, 0.3, fill=YELLOW, border=None)
    add_text(s, 0.62, 2.5, 1.0, 0.24, "GOOD", size=12, bold=True,
             align=PP_ALIGN.CENTER)
    add_card(s, 0.62, 2.78, 8.76, 0.62, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 0.8, 2.9, 8.4, 0.4,
             '"Display in large text on the screen: Hello, I\'m Sam."',
             size=13, font=MONO)
    add_rect(s, 0.62, 3.62, 1.0, 0.3, fill=RED, border=None)
    add_text(s, 0.62, 3.67, 1.0, 0.24, "BAD", size=12, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER)
    add_card(s, 0.62, 3.95, 8.76, 0.85, fill=WHITE, border=RED, border_w=1.5)
    add_multiline(s, 0.8, 4.05, 8.4, 0.65, [
        '"Set up the lights, the screen and the speaker, make it cool."',
        '— three jobs plus "cool" — AI can only guess.',
    ], size=12.5, font=MONO, line_spacing=1.2)
    set_notes(s, "'One more pass at spell one: one thing at a time. Not 'set up "
                 "the lights, screen and speaker'. Say 'display my name in large "
                 "text on the screen'. One thing, said clearly, and it gets it "
                 "right.' Write that sentence in a corner of the whiteboard and "
                 "leave it there all session.")

    # ---------------------------------------------------------------- 18 two spells
    s = page(prs, 18)
    add_title_bar(s, "The Two Spells for Talking to AI")
    add_rect(s, 0.62, 1.4, 0.55, 0.55, fill=YELLOW, border=None)
    add_text(s, 0.62, 1.5, 0.55, 0.4, "1", size=18, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER)
    add_text(s, 1.35, 1.38, 8.0, 0.6, "One thing at a time.", size=34, bold=True)
    add_text(s, 1.35, 2.02, 8.0, 0.62,
             "Not \"set up the lights, the screen and the speaker\" — one thing, "
             "said clearly, and it gets it right.", size=14.5)
    add_rect(s, 0.62, 2.95, 0.55, 0.55, fill=YELLOW, border=None)
    add_text(s, 0.62, 3.05, 0.55, 0.4, "2", size=18, bold=True, color=WHITE,
             align=PP_ALIGN.CENTER)
    add_text(s, 1.35, 2.93, 8.0, 0.6, "If it's wrong, add one more line.",
             size=34, bold=True)
    add_text(s, 1.35, 3.57, 8.0, 0.62,
             "Don't delete the conversation, don't restart — add one line in the "
             "same conversation. AI remembers what you talked about.", size=14.5)
    add_text(s, 0.62, 4.5, 8.76, 0.4,
             "Both spells are in your Student Workbook — check them whenever you "
             "forget.", size=13.5, align=PP_ALIGN.CENTER)
    set_notes(s, "The largest type of the deck (36 pt class). Read each spell "
                 "once, then have the class read it back with you — the standard "
                 "posture for all of today's conversations. The lines match the "
                 "Teacher's Guide verbatim (14:30 'The two spells').")

    # ---------------------------------------------------------------- 19 first task
    s = page(prs, 19)
    add_title_bar(s, "Your First Task — Light Your Name")
    steps19 = [
        ("1", "Type this sentence (swap in your own name)"),
        ("2", "Click Generate, then wait for compile"),
        ("3", "Click Flash — watch the screen"),
    ]
    x = 0.62
    for num, line in steps19:
        add_card(s, x, 1.4, 2.8, 0.8, fill=WHITE, border=INK, border_w=1.0)
        num_block(s, x + 0.12, 1.52, num, size=0.34)
        add_text(s, x + 0.56, 1.56, 2.16, 0.55, line, size=12.5,
                 line_spacing=1.15)
        x += 3.0
    add_grey_box(s, 0.62, 2.4, 8.76, 0.6,
                 "Display in large text on the screen: Hello, I'm [your name].",
                 size=13)
    add_multiline(s, 0.62, 3.2, 8.76, 0.9, [
        "generate = AI writes the instructions",
        "compile = translated into what the board understands",
        "flash = moved down the USB cable into the board — unplug it, it still "
        "remembers",
    ], size=12.5, line_spacing=1.15)
    add_text(s, 0.62, 4.4, 8.76, 0.4,
             "Raise your hand — a TA will put a flag on your desk.",
             size=15, bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "Three new words first (20 s): 'Generate — AI is writing the "
                 "instructions. Compile — it's translating them into what the "
                 "board understands. Flash — moving the translated instructions "
                 "down the USB cable into the board. Once they're in, the board "
                 "remembers. Unplug it — still remembers.' Then demo once "
                 "slowly, then hand over: your name in English letters (Chinese "
                 "glyphs are unreliable on this board — light English first, "
                 "guaranteed; want to try Chinese? If it won't display, switch "
                 "back to English and teach it Chinese later). You never type "
                 "for a student — their hands, their success. 10 minutes without "
                 "lighting up — swap to a spare board, don't fix. TA hands out "
                 "'LIT' flags one by one as boards light.")

    # ---------------------------------------------------------------- 20 celebration
    s = page(prs, 20)
    add_title_bar(s, "Hold Up Your Boards!")
    add_multiline(s, 0.62, 1.85, 8.76, 1.2,
                  ["From this moment, you're people who",
                   "can make hardware do what you say."],
                  size=26, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.15)
    add_rect(s, 4.4, 3.3, 1.2, 0.05, fill=YELLOW, border=None)
    add_text(s, 0.62, 3.6, 8.76, 0.5, "(look at the camera —)", size=17,
             align=PP_ALIGN.CENTER)
    set_notes(s, "'Everyone — hold up your boards! (wait for the whole room) "
                 "From this moment, you're people who can make hardware do what "
                 "you say. Look at the camera —' TA sweeps first: anyone still "
                 "dark gets lit before joining the photo — nobody photographs a "
                 "dark board. Photo is also log material and the end-of-course "
                 "comparison shot: one landscape, one portrait. Compose around "
                 "raised boards and screens; backs of heads and hands are fine.")

    # ---------------------------------------------------------------- 21 free round
    s = page(prs, 21)
    add_title_bar(s, "Free Round — It's Yours Now")
    add_text(s, 0.62, 1.3, 8.76, 0.5,
             "Add an effect you want — blinking, a beep, an emoji, scrolling. "
             "Your pick.", size=16, align=PP_ALIGN.CENTER)
    opts = [
        "Make the name blink once per second",
        "Make a sound when the name shows",
        "Make the name scroll from right to left",
    ]
    x = 0.62
    for t in opts:
        add_card(s, x, 2.0, 2.8, 1.0, fill=WHITE, border=INK, border_w=1.0)
        add_text(s, x + 0.15, 2.22, 2.5, 0.6, t, size=13, font=MONO,
                 line_spacing=1.2)
        x += 3.0
    add_golden_line(s, 0.62, 3.55, 8.76,
                    "Spell 2 | If it's wrong, add one more line — don't delete, "
                    "don't restart. AI remembers what you said before.",
                    size=14, h=None)
    set_notes(s, "'It's yours now. Add an effect you want — blinking name, a "
                 "beep when it appears, an emoji, make it scroll. Your pick. ... "
                 "Effect not right? Don't delete, don't restart — add one line "
                 "in the same conversation, like 'no, I want it to blink "
                 "faster'. AI remembers what you said before.' After about 3 "
                 "min, table show and tell: 30 seconds each — what effect did "
                 "you add, and how did you tell AI? Project the 'broke it, then "
                 "fixed it' conversations, not the flashiest — the class needs "
                 "to see that fixing it back is the normal everyday move. "
                 "Student dumps everything on AI at once? 'Nice appetite. But "
                 "directors shoot one scene at a time — pick one effect and "
                 "make it solid, then shoot the next scene.'")

    # ---------------------------------------------------------------- 22 3-box model
    s = page(prs, 22)
    add_title_bar(s, "Sense → Logic → Output")
    add_subtitle(s, "(the only mental model of the whole course)", size=15)
    boxes = [("SENSE", 0.62), ("LOGIC", 3.74), ("OUTPUT", 6.86)]
    for name, bx in boxes:
        fill = YELLOW if name in ("SENSE", "OUTPUT") else WHITE
        add_card(s, bx, 1.5, 2.5, 0.95, fill=fill, border=INK, border_w=1.0)
        add_text(s, bx, 1.66, 2.5, 0.6, name, size=20, bold=True,
                 align=PP_ALIGN.CENTER)
    add_text(s, 3.24, 1.6, 0.4, 0.6, "→", size=20, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 6.36, 1.6, 0.4, 0.6, "→", size=20, bold=True,
             align=PP_ALIGN.CENTER)
    add_multiline(s, 0.62, 2.75, 8.76, 1.5, [
        "The automatic door: it sees someone → decides whether to open → the "
        "door opens",
        "The air conditioner: it measures the temperature → compares → cools",
        "Your mom: she sees you on your phone → decides whether to yell → she "
        "calls you",
    ], size=13.5, line_spacing=1.35)
    add_text(s, 0.62, 4.35, 8.76, 0.6,
             "Your board: eyes and ears on this side, face and voice on this "
             "side. The logic in the middle — that's your call.", size=14,
             bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "Examples only, no jargon; give these 5 minutes their full "
                 "due. Have the class read the six words back with you: 'sense, "
                 "logic, output.' Keep the 'mom' example — the room laughs "
                 "every time. Optional local swap: replace the first two "
                 "examples with something everyone in town has seen (the sensor "
                 "light at the corner shop, the rice cooker at home); keep "
                 "'mom.'")

    # ---------------------------------------------------------------- 23 build 1
    s = page(prs, 23)
    add_title_bar(s, "Build 1 | Follow-Along — The Dark-Detecting Light")
    add_grey_box(s, 0.62, 1.3, 8.76, 0.85,
                 "When the light gets dim, turn on the LED; when it gets bright, "
                 "turn it off.", size=14)
    steps23 = [
        ("1", "Type the sentence"),
        ("2", "Generate, compile, flash"),
        ("3", "Cover the light sensor with your hand"),
    ]
    x = 0.62
    for num, line in steps23:
        add_card(s, x, 2.35, 2.8, 0.75, fill=WHITE, border=INK, border_w=1.0)
        num_block(s, x + 0.12, 2.47, num, size=0.32)
        add_text(s, x + 0.54, 2.5, 2.18, 0.5, line, size=12.5,
                 line_spacing=1.1)
        x += 3.0
    add_text(s, 0.62, 3.3, 8.76, 0.55,
             "All together — three, two, one, cover!", size=22, bold=True,
             align=PP_ALIGN.CENTER)
    fills = [("SENSE = light", 0.62), ("LOGIC = dark means on", 3.74),
             ("OUTPUT = the LED", 6.86)]
    for t, fx in fills:
        add_card(s, fx, 4.05, 2.5, 0.6, fill=YELLOW, border=None)
        add_text(s, fx, 4.16, 2.5, 0.4, t, size=13.5, bold=True,
                 align=PP_ALIGN.CENTER)
    set_notes(s, "'Build one, we do it together: a light that turns on when "
                 "it's dark. Tell AI — 'When the light gets dim, turn on the "
                 "LED; when it gets bright, turn it off.' Send, flash. Now — "
                 "everyone, cover the light sensor on your board with your "
                 "hand — (lights come on across the room, one after another) — "
                 "look at that. A room full of night lights.' Make the "
                 "cover-test a moment: 'Three, two, one — cover!' Sluggish "
                 "light = teaching point, loud enough for the room: 'It thinks "
                 "your spot isn't dark enough. What do you do? Tell AI — 'make "
                 "it more sensitive.'' — spell two in action, live. Then fill "
                 "the 3 boxes back in (15:25–15:30): 'What did we just do? "
                 "Sense — the light. Logic — dark means on. Output — the LED. "
                 "Fill the boxes, that simple. Now you're going to fill the "
                 "boxes yourselves — whatever you fill, you build.'")

    # ---------------------------------------------------------------- 24 build 2
    s = page(prs, 24)
    add_title_bar(s, "Build 2 | Semi-Free — Pick One Sensor + One Output")
    add_text(s, 0.62, 1.28, 8.76, 0.45,
             "Pick one sensor and one output from the table card. Your "
             "combination.", size=15.5, align=PP_ALIGN.CENTER)
    cards24 = [
        ("Clap light", "hears a sound → decides it's loud enough → light on"),
        ("Shake alarm", "feels a shake → decides it's moving → buzzer beeps"),
        ("Heat alert", "measures temperature → decides it's too hot → screen "
         "warns"),
    ]
    x = 0.62
    for t, sub in cards24:
        add_card(s, x, 1.9, 2.8, 1.7, fill=WHITE, border=INK, border_w=1.0)
        add_text(s, x + 0.15, 2.05, 2.5, 0.4, t, size=15, bold=True)
        add_text(s, x + 0.15, 2.5, 2.5, 0.95, sub, size=12.5,
                 line_spacing=1.25)
        x += 3.0
    yellow_box(s, 0.62, 3.85, 8.76, 0.9, [
        "Can't say it, can't code it.",
        "(Your three boxes, out loud, before you touch the keyboard.)"],
        title="Tell your neighbor your 3 boxes BEFORE you touch the keyboard.",
        size=12.5)
    set_notes(s, "The first question you ask while circulating is always: 'What "
                 "are your three boxes?' Can't answer? Use the analogy: 'In your "
                 "build, which part is the automatic door's eye?' Student only "
                 "stacks outputs with no sensor? 'Cool — now make it perform "
                 "only when [some condition] happens.' The moment the class's "
                 "first error appears — stop the whole room for 1 minute and "
                 "switch to slide 25.")

    # ---------------------------------------------------------------- 25 error
    s = page(prs, 25)
    add_title_bar(s, "The Right Way to Handle an Error")
    add_text(s, 0.62, 1.75, 8.76, 0.7,
             "An error isn't a broken thing — it's AI talking to you.",
             size=22, bold=True, align=PP_ALIGN.CENTER)
    y = 2.9
    for num, line in [
        ("1", "Copy the full error text"),
        ("2", "Add \"here's what I just changed\" and throw it all back to AI"),
    ]:
        num_block(s, 1.5, y + 0.02, num)
        add_text(s, 2.1, y, 6.6, 0.5, line, size=17)
        y += 0.7
    set_notes(s, "Deliberately no red on this page: the point is to "
                 "de-dramatize errors. Stop the room for 1 minute, project that "
                 "student's screen, walk them through the move together: 'See? "
                 "An error isn't a broken thing. It's AI talking to you. It "
                 "wrote the problem out — you just forward it back.' Backup if "
                 "the class somehow produces no error: project the prepared "
                 "'make the board fly' conversation from Rehearsal 4 and teach "
                 "the point anyway.")

    # ---------------------------------------------------------------- 26 build 3
    s = page(prs, 26)
    add_title_bar(s, "Build 3 | Fully Free — Make Something That Reacts")
    add_text(s, 0.62, 1.28, 8.76, 0.45,
             "One-line brief: make something that reacts. What it reacts to, "
             "how it reacts — all yours.", size=15.5, align=PP_ALIGN.CENTER)
    cards26 = [
        ("Clap light", "one clap on, one clap off"),
        ("Mini alarm", "shakes → beeps; hold the button 2 seconds to disarm"),
        ("Desk weather station", "screen shows temperature, humidity, light — "
         "too dark → light on; too hot → beep"),
    ]
    x = 0.62
    for t, sub in cards26:
        add_card(s, x, 1.85, 2.8, 1.8, fill=WHITE, border=INK, border_w=1.0)
        add_text(s, x + 0.15, 2.0, 2.5, 0.4, t, size=15, bold=True)
        add_text(s, x + 0.15, 2.45, 2.5, 1.05, sub, size=12.5,
                 line_spacing=1.25)
        x += 3.0
    add_golden_line(s, 0.62, 3.85, 8.76,
                    "Done and bored? Two directions — 1 Tiny game: whack-a-mole "
                    "/ reaction-timer (buttons score, screen shows the score) | "
                    "2 Board as controller: the board's buttons and knob drive a "
                    "little game on the screen.",
                    size=12.5, h=None)
    add_text(s, 0.62, 4.7, 8.76, 0.4,
             "Done means: it reacts to the thing you chose — and you can say "
             "its three boxes.", size=13, bold=True, align=PP_ALIGN.CENTER)
    set_notes(s, "'Last build. One-line brief: make something that reacts. What "
                 "it reacts to, how it reacts — all yours. Wanted to upgrade "
                 "your earlier build instead? Go for it.' Fast students: only "
                 "release challenge directions you've rehearsed and run yourself "
                 "— a fast student crashing with no one to catch them is on "
                 "you. Still fast? Make them the teacher: they explain their "
                 "build to a neighbor in 3 boxes; next lesson they officially "
                 "TA. Build only 'displays' instead of 'reacts'? 'It can "
                 "already talk. Now give it an eye — it only speaks when ___.'")

    # ---------------------------------------------------------------- 27 log (red)
    s = page(prs, 27)
    add_title_bar(s, "Flash Show and Tell + Your Full AI Log")
    add_text(s, 0.62, 1.28, 8.76, 0.4,
             "Show and tell: in your table, 30 seconds each — demo your build, "
             "say its three boxes.", size=14, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 1.8, 8.76, 0.35, "Your log, four sentences:",
             size=14, bold=True)
    add_multiline(s, 0.62, 2.18, 8.76, 0.85, [
        "·  Today I made ___",
        "·  I got stuck on ___",
        "·  Then ___",
        "·  Next time I want ___",
    ], size=13.5, line_spacing=1.18)
    add_grey_box(s, 0.62, 3.2, 8.76, 0.8,
                 "Say it to your phone, then send it to AI with one more line: "
                 "\"Tidy this into a learning log — only what I said, nothing I "
                 "didn't say.\"", size=12)
    add_red_rule_box(s, 0.62, 4.2, 8.76, 0.85, "Warning",
                     ["AI will make things up with a straight face. "
                      "Proofreading is your job."], body_size=15)
    set_notes(s, "First log ever: you model it first with your own four "
                 "sentences, including where YOU got stuck — you show weakness "
                 "first, and they'll tell the truth. 'I got stuck on ___' is a "
                 "required field; 'I didn't get stuck' → 'Went too smoothly? "
                 "Then write down what you're worried about.' Someone accepts "
                 "AI's log wholesale? Project the prepared 'AI got caught "
                 "making stuff up' screenshot and teach the proofreading "
                 "responsibility on the spot — today's hidden bonus teaching "
                 "point. Project 2 builds: the cleverest combination + one "
                 "rescued after a crash.")

    # ---------------------------------------------------------------- 28 next time
    s = page(prs, 28)
    add_title_bar(s, "Next Time")
    yellow_box(s, 0.62, 1.45, 8.76, 0.95, [
        "By the end of the course, it's worth more than the builds themselves."],
        title="Your logs are saved — that's the growth story of your builds.",
        size=13.5)
    add_text(s, 0.62, 2.8, 8.76, 0.6, "Lesson 2: Find a Problem Worth Solving",
             size=28, bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.6, 8.76, 0.8,
             "Start thinking on the way home — what's one small thing in your "
             "daily life that annoys you?", size=17, align=PP_ALIGN.CENTER,
             line_spacing=1.3)
    set_notes(s, "Wrap fast, preview then dismiss: 'Today's logs are all saved "
                 "— that's the growth story of your builds. By the end of the "
                 "course it'll be worth more than the builds themselves. Next "
                 "time, we do something even more important: find the problem "
                 "worth building all the way to the end. Start thinking on the "
                 "way home — what's one small thing in your daily life that "
                 "annoys you? Class dismissed!' Leaving them wanting more is "
                 "the best way to end.")

    prs.save(OUT)
    print("SAVED:", OUT)
    print("slides:", len(prs.slides.__iter__.__self__._sldIdLst))


if __name__ == "__main__":
    main()
