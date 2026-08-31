"""
Build the English Lesson 0 deck (Before the First Light, 13 slides, 45 min)
from M0_EN_PPTPlan_CFG-5_Lesson00_BeforeFirstLight_v1.md (brand rebuild).

Output: 交付物_EN/03_Deliverables/PPTX/M0_EN_Deck_CFG-5_Lesson00_BeforeFirstLight_v1.pptx
Layout verified against chaihuo-ppt-brand.md: white 70 / yellow 15 / ink 10 / red 5,
960x540, no gradients/shadows, red only on slide 6 (house rule).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder_lib import *

TOTAL = 13
DECK_LABEL = "Before the First Light"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson00_BeforeFirstLight_v1.pptx")

def page(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(s)
    add_footer(s, n, TOTAL, DECK_LABEL)
    return s

def main():
    prs = new_deck()

    # ---------------------------------------------------------------- 01 cover
    s = page(prs, 1)
    add_text(s, 0.6, 1.05, 8.8, 0.35,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) · The Kickoff",
             size=14, align=PP_ALIGN.CENTER)
    add_text(s, 0.6, 1.75, 8.8, 0.95, "Before the First Light",
             size=44, bold=True, align=PP_ALIGN.CENTER)
    add_rect(s, 4.4, 2.72, 1.2, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.6, 3.05, 8.8, 0.4,
             "Instructor: ____________ · one-line bio [FILL]",
             size=18, align=PP_ALIGN.CENTER)
    add_text(s, 0.6, 3.55, 8.8, 0.4,
             "The Lesson-1 outcome — your name, glowing on the board's screen",
             size=18, align=PP_ALIGN.CENTER)
    add_text(s, 0.6, 4.0, 8.8, 0.3, "(live photo taken by a real instructor)",
             size=13, align=PP_ALIGN.CENTER)
    set_notes(s, "Cover — loops before class. The one-line bio must be filled before "
                 "class (a blank cover line is a credibility leak). Point at the "
                 "Lesson-1 outcome image in the first 30 seconds — \"That's a student "
                 "from the last cohort, end of their first lesson. Next session, "
                 "that's you.\"")

    # ---------------------------------------------------------------- 02 meet
    s = page(prs, 2)
    add_title_bar(s, "Meet Your Instructor")
    add_subtitle(s, "Who I am, and why I'm teaching this course")
    add_card(s, 6.4, 1.5, 3.2, 3.1, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 6.4, 2.9, 3.2, 0.4, "[ FILL: your photo ]", size=14,
             align=PP_ALIGN.CENTER)
    lines = [
        ("· Name: ____________ (from ____________)", {}),
        ("· At Chaihuo Makerspace: ____________ (your role)", {}),
        ("· Things I've done / courses I've taught: ____________", {}),
        ("· The best thing I've built with AI: ____________ (that's the next slide)", {}),
    ]
    add_multiline(s, 0.62, 1.55, 5.5, 2.9, lines, size=18, line_spacing=1.35)
    set_notes(s, "1 min — keep it to one sentence per line. Never read this page "
                 "aloud line by line — say your name, where you're from, and one "
                 "reason you're teaching, then flip to slide 3 fast. The slide "
                 "exists so latecomers can catch up on their own. Do not linger.")

    # ---------------------------------------------------------------- 03 example
    s = page(prs, 3)
    add_title_bar(s, "A Real Example — you can do it too")
    add_subtitle(s, "Zero code, and I still built something real")
    add_card(s, 0.62, 1.5, 4.6, 2.5, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 0.62, 2.55, 4.6, 0.32,
             "[ FILL: screenshots of your own", size=14, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.87, 4.6, 0.32,
             "complete AI-built project ]", size=14, align=PP_ALIGN.CENTER)
    add_text(s, 5.42, 1.72, 4.0, 0.35, "__ weeks to build", size=17, bold=True)
    add_rect(s, 5.42, 2.18, 4.0, 0.02, fill=YELLOW, border=None)
    add_text(s, 5.42, 2.5, 4.0, 0.35, "0 lines of hand-written code", size=17, bold=True)
    add_rect(s, 5.42, 2.96, 4.0, 0.02, fill=YELLOW, border=None)
    add_text(s, 5.42, 3.28, 4.0, 0.35, "1 complete project", size=17, bold=True)
    add_text(s, 5.42, 3.85, 4.0, 0.55,
             "I didn't write a single line — but every line was generated from "
             "what I asked for.", size=13, line_spacing=1.25)
    add_golden_line(s, 0.62, 4.3, 8.8,
                    "The build itself is worth nothing. What's worth something is "
                    "that I now believe I can take on any \"can you make a…\" question.",
                    size=13.5, h=None)
    set_notes(s, "4 min — center of gravity. Tell it as a story, never read the "
                 "specs. Three beats: 1) What I was trying to solve (one specific "
                 "annoyance); 2) Zero lines of code — but every line came from what "
                 "*I* asked for. Show how you talked to the AI; 3) How it felt the "
                 "day it worked. Land it: \"The build itself is worth nothing. "
                 "What's worth something is that I now believe I can take on any "
                 "'can you make a…' question.\" HARD PREP (the only hard prep of "
                 "the deck): this page is empty until you fill it. No project "
                 "handy? Spend two evenings making one now. If you genuinely can't, "
                 "teach slide 4 (the Brandy case) as your main story instead, and "
                 "never let students see an empty placeholder.")

    # ---------------------------------------------------------------- 04 brandy
    s = page(prs, 4)
    add_title_bar(s, "Engineers Do It Too — and I'm not the only one")
    rows = [
        ("1", "a real annoyance: typing breaks her flow.",
         "Chatting with AI, her thoughts kept getting cut off by the keyboard.\n"
         "She thought: can I just hold a button and talk?"),
        ("0", "lines of hand-written code.",
         "She did three things: said what she needed, made demands, checked the work.\n"
         "The AI wrote all the code."),
        ("1", "a working voice keyboard. Hold to talk, release to send.",
         "The first version had exactly one key — pressed 20 times in a row\n"
         "before she moved on."),
    ]
    y = 1.32
    for num, head, body in rows:
        add_card(s, 0.62, y, 8.8, 1.02, fill=WHITE, border=INK, border_w=1.0)
        add_text(s, 0.9, y + 0.14, 0.5, 0.6, num, size=30, bold=True)
        add_text(s, 1.5, y + 0.1, 7.8, 0.4, head, size=16.5, bold=True)
        add_multiline(s, 1.5, y + 0.5, 7.8, 0.48, body.split("\n"),
                      size=12, line_spacing=1.08)
        y += 1.14
    add_text(s, 0.62, 4.82, 8.8, 0.3,
             "Brandy Li · Application Engineer at Seeed Studio — the company that "
             "makes our boards.", size=13)
    set_notes(s, "2 min — the case is already on the slide; just tell it. The two "
                 "beats that matter: 1) How she worked — first version = exactly "
                 "one key, tested 20 times without a miss before adding anything. "
                 "\"A professional engineer's first version was small enough to be "
                 "one key. That's how we work in this course — and when you build "
                 "your MVP in Lesson 8, you'll meet her again.\" 2) The close: "
                 "\"This isn't a kids' way of doing things. This is how engineers "
                 "work. Ten sessions from now, you'll work this way too.\"")

    # ---------------------------------------------------------------- 05 why now
    s = page(prs, 5)
    add_title_bar(s, "Why Now — AI is redefining what's valuable")
    add_subtitle(s, "AI can already write, draw, translate, and look things up — and it's getting faster.",
                 y=1.0, size=14)
    add_text(s, 0.62, 1.42, 8.8, 0.4, "So what's left for YOU?", size=22, bold=True)
    items = [
        ("Spot the problem", "AI can solve problems; asking the right one is on you"),
        ("Judge the result", "AI gives you a hundred answers; choosing is on you"),
        ("Understand real people", "what people want, and what annoys them: AI doesn't know, you do"),
        ("Make the call", "trade-offs and owning the outcome: that's you"),
    ]
    y = 1.95
    for head, body in items:
        add_oval(s, 0.62, y + 0.06, 0.11, fill=YELLOW, border=None)
        add_text(s, 0.88, y, 8.4, 0.34, head, size=18, bold=True)
        add_text(s, 0.88, y + 0.34, 8.4, 0.3, body, size=14)
        y += 0.62
    add_golden_line(s, 0.62, 4.52, 8.8, "This course trains all four.",
                    size=17, h=0.45)
    set_notes(s, "5 min — walk the four one at a time, each with a 30-second beat "
                 "from your own build story. Land it: \"Programming? That's the "
                 "AI's job.\" CFU (pair-share): \"Turn to your neighbor: name one "
                 "of the four, the one you already feel good at. Ten seconds each "
                 "way.\"")

    # ---------------------------------------------------------------- 06 role (red page)
    s = page(prs, 6)
    add_title_bar(s, "Your Role — you're the director, AI is the programmer")
    add_card(s, 0.62, 1.32, 4.25, 2.45, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 0.9, 1.47, 3.7, 0.4, "YOU (the director)", size=19, bold=True)
    add_multiline(s, 0.9, 1.97, 3.7, 1.7, [
        "· What to build — you set the brief",
        "· What \"good\" means — you set the standard",
        "· Whether it passes — you accept the work",
    ], size=16, line_spacing=1.3)
    add_card(s, 5.15, 1.32, 4.25, 2.45, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 5.43, 1.47, 3.7, 0.4, "AI (the programmer)", size=19, bold=True)
    add_multiline(s, 5.43, 1.97, 3.7, 1.7, [
        "· Writes the code, builds the structure",
        "· Fixes the bugs, runs the tests",
        "· Always on call, never gets tired",
    ], size=16, line_spacing=1.3)
    add_red_rule_box(s, 0.62, 4.02, 8.8, 1.0, "House rule",
                     ["You do not write code by hand.",
                      "Your job is three things: say it clearly, watch what happens, tell it to change."],
                     body_size=14)
    set_notes(s, "5 min — the only red page. Announce the house rule with a light "
                 "tone, frame it as good news. We Do — point at the screen and "
                 "read the three things together, once: \"Say it clearly — watch "
                 "what happens — tell it to change.\" CFU: \"Thumbs up if your job "
                 "is writing code. … Good — you're all wrong. Thumbs up if your "
                 "job is saying it clearly, watching what happens, telling it to "
                 "change.\" Parent/open-house note (add one line here for adult "
                 "audiences): \"If you're wondering 'but aren't they supposed to "
                 "learn to code?' — code can be learned any time. What we build "
                 "first is the ability to *direct* code — the part you can't catch "
                 "up on later.\"")

    # ---------------------------------------------------------------- 07 tools
    s = page(prs, 7)
    add_title_bar(s, "Your Three Tools")   # long deck title split: subtitle carries the rest
    add_text(s, 0.62, 0.78, 8.9, 0.3, "— everything you'll make, made with these",
             size=15)
    tools = [
        ("Grove Beginner Kit", "Lessons 1–2, and from Lesson 6 on",
         "10 sensors + OLED screen, plug in USB and it works.\nYour first board — the gateway to sensing the world."),
        ("Wio Terminal", "Lessons 3–4, 6",
         "Color screen + joystick and buttons. A pocket-sized interaction\nprototype — this one gives your project a face."),
        ("XIAO ESP32S3 Sense", "Lesson 5",
         "A thumbnail-sized vision AI board with a camera — this one\nteaches your hardware to see."),
    ]
    for i, (name, tag, body) in enumerate(tools):
        x = 0.62 + i * 3.05
        add_card(s, x, 1.42, 2.85, 2.85, fill=WHITE, border=INK, border_w=1.0)
        add_text(s, x + 0.22, 1.62, 2.4, 0.75, name, size=18, bold=True, line_spacing=1.05)
        add_rect(s, x + 0.22, 2.32, 0.9, 0.05, fill=YELLOW, border=None)
        add_text(s, x + 0.22, 2.45, 2.4, 0.4, tag, size=13)
        add_multiline(s, x + 0.22, 2.9, 2.45, 1.3, body.split("\n"), size=12.5,
                      line_spacing=1.25)
    add_golden_line(s, 0.62, 4.5, 8.8,
                    "From Lesson 7 on, all three work together for your project.",
                    size=15.5, h=0.45)
    set_notes(s, "5 min — hold up a real kit if you have one (a board beats a "
                 "picture), otherwise point at the screen. Give each board its "
                 "one-liner: \"plug in USB, and it works\" / \"gives your project "
                 "a face\" / \"teaches your hardware to see.\" CFU "
                 "(call-and-response): \"Which one gives your project a face? — "
                 "Wio. Which one teaches it to see? — XIAO. Nice.\"")

    # ---------------------------------------------------------------- 08 map
    s = page(prs, 8)
    add_title_bar(s, "Ten Sessions, One Map")
    groups = [
        ("Sessions 1–2 · Light up + find your problem",
         ["1  Light up your first piece of hardware with AI",
          "2  Find a problem worth solving"]),
        ("Sessions 3–6 · Team up with AI, learn skills",
         ["3  Give your project a screen",
          "4  Team up with AI — build a pomodoro timer",
          "5  Teach your hardware to see",
          "6  Move your project to your own computer"]),
        ("Sessions 7–10 · The Marathon: build your project",
         ["7  Claim your project",
          "8  Marathon · Leg 1",
          "9  Marathon · Leg 2 (call in reinforcements)",
          "10  My project, my showcase"]),
    ]
    y = 1.22
    for gi, (head, rows) in enumerate(groups):
        add_oval(s, 0.62, y + 0.05, 0.11, fill=YELLOW, border=None)
        add_text(s, 0.88, y - 0.02, 8.6, 0.3, head, size=14.5, bold=True)
        y += 0.3
        for r in rows:
            add_text(s, 1.05, y, 8.3, 0.28, r, size=12.5)
            y += 0.235
        if gi < 2:
            y += 0.08
    add_card(s, 0.62, 4.5, 8.8, 0.34, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 0.85, 4.57, 8.3, 0.25,
             "Lesson 7 — you claim your own project. From then on, you're solving a problem you chose.",
             size=12.5)
    add_card(s, 0.62, 4.9, 8.8, 0.34, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 0.85, 4.97, 8.3, 0.25,
             "Lesson 10 — you stand on stage and present your project to the room.",
             size=12.5)
    set_notes(s, "5 min — students don't memorize it; *you* must be able to walk "
                 "it off script, one sentence per lesson. Read the word AI out "
                 "loud on \"team up with AI\": the team here is AI roles, not "
                 "student groups. Emphasize only the two milestones. Any detail "
                 "question → \"We'll cover that at the start of each lesson. "
                 "Nothing to remember today.\"")

    # ---------------------------------------------------------------- 09 loop
    s = page(prs, 9)
    add_title_bar(s, "One Project, Eight Steps — the full journey")
    steps = ["Frame the problem", "Find the user", "Prototype", "Code",
             "Make trade-offs", "Test & judge", "Document", "Share the value"]
    for i, st in enumerate(steps):
        col, row = i % 4, i // 4
        x = 0.62 + col * 2.22
        y = 1.4 + row * 0.82
        add_card(s, x, y, 2.1, 0.74, fill=WHITE, border=INK, border_w=1.0)
        add_rect(s, x + 0.16, y + 0.14, 0.34, 0.22, fill=YELLOW, border=None)
        add_text(s, x + 0.21, y + 0.16, 0.26, 0.18, f"{i+1:02d}", size=10, bold=True,
                 align=PP_ALIGN.CENTER)
        add_text(s, x + 0.16, y + 0.44, 1.8, 0.26, st, size=12.5, bold=True)
    add_golden_line(s, 0.62, 3.35, 8.8,
                    "Most courses only teach step 4 — writing code. This course "
                    "walks all eight, and at every step AI is your partner.",
                    size=14, h=None)
    add_text(s, 0.62, 4.25, 8.8, 0.6,
             "Every step you complete, light up a square in your log — the "
             "progress bar stays in your own hands.", size=13, line_spacing=1.25)
    set_notes(s, "2 min (flexible) — read the eight steps once, pointing at each — "
                 "no elaboration. Land the one line: \"Most courses only teach "
                 "step 4 — writing code. This course walks all eight steps, and at "
                 "every step, AI is your partner.\" This page and slide 10 are the "
                 "only compressible pages in the deck.")

    # ---------------------------------------------------------------- 10 two things
    s = page(prs, 10)
    add_title_bar(s, "Two Things That Carry You Through All Ten Sessions")
    add_card(s, 0.62, 1.4, 4.25, 2.85, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 0.9, 1.58, 3.7, 0.4, "Six skill cards", size=19, bold=True)
    add_multiline(s, 0.9, 2.05, 3.7, 0.7, [
        "· Spot a problem · Find the user · Build it",
        "· Make trade-offs · Judge quality · Tell the story",
    ], size=14, line_spacing=1.25)
    add_text(s, 0.9, 2.9, 3.7, 1.2,
             "Every time you do one, you light up a square in your log. "
             "By the end, all six are lit.", size=13.5, line_spacing=1.3)
    add_card(s, 5.15, 1.4, 4.25, 2.85, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 5.43, 1.58, 3.7, 0.6, "A full set of\nAI-prompting phrases",
             size=17, bold=True, line_spacing=1.1)
    add_multiline(s, 5.43, 2.25, 3.7, 1.9, [
        "· How to tell AI what you need, how to correct it, how to handle errors",
        "· Each phrase unlocks as we use it — read off the screen together, saved in your Student Workbook",
        "· At the end of the course, you take the whole set with you",
    ], size=13, line_spacing=1.3)
    add_golden_line(s, 0.62, 4.45, 8.8,
                    "Phrases are scaffolding, not a boss — what you build, and "
                    "whether it's good, is always your call.", size=15.5, h=None)
    set_notes(s, "2 min (flexible) — the six skills get a glance (they'll touch "
                 "all of them later); the phrases get the one-liner about the "
                 "Student Workbook. Land the closing line about scaffolding — it "
                 "is the course's philosophy in one sentence.")

    # ---------------------------------------------------------------- 11 takeaways
    s = page(prs, 11)
    add_title_bar(s, "When You Finish, You Take Away")
    items = [
        ("A project that's yours", "You choose the topic. It demos live. Not homework — a project."),
        ("Its growth story", "One AI log per session, gathered into a project README — the whole \"how it got made\" is on record."),
        ("Your showcase", "Lesson 10: you stand on stage and present it to the room."),
        ("A method you can reuse", "Six skills + the full phrase set — for any project, from here on."),
    ]
    y = 1.32
    for head, body in items:
        add_card(s, 0.62, y, 8.8, 0.7, fill=WHITE, border=INK, border_w=1.0)
        add_rect(s, 0.62, y, 0.05, 0.7, fill=YELLOW, border=None)
        add_text(s, 0.9, y + 0.08, 8.2, 0.3, head, size=16, bold=True)
        add_text(s, 0.9, y + 0.4, 8.2, 0.28, body, size=12)
        y += 0.8
    add_golden_line(s, 0.62, 4.62, 8.8,
                    "For competitions, for interviews, for showing family and "
                    "friends — the growth story is worth more than the build itself.",
                    size=13, h=None)
    set_notes(s, "3 min — four items, quickly. Land it: \"For competitions, for "
                 "interviews, for showing your family and friends — the growth "
                 "story is worth more than the build itself.\" Open-house parent "
                 "note: \"What you'll see after ten sessions is not a homework "
                 "assignment. It's a working project they can demo live, a README "
                 "that records how it grew, and two minutes on stage where they "
                 "explain it clearly.\"")

    # ---------------------------------------------------------------- 12 question
    s = page(prs, 12)
    add_title_bar(s, "Your Project Starts With a Question")
    add_text(s, 0.62, 1.42, 8.8, 1.2,
             "What's one small thing in your daily life that annoys you?",
             size=30, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.05)
    add_text(s, 0.62, 2.70, 8.8, 0.34,
             "At home, at school, on the way —", size=15.5, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.96, 8.8, 0.34,
             "something that needs running after, something that needs watching.",
             size=15.5, align=PP_ALIGN.CENTER)
    add_card(s, 1.35, 3.38, 7.3, 0.92, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 1.53, 3.48, 6.94, 0.72,
                  ["the classroom light nobody turns off |",
                   "the pills grandma keeps forgetting |",
                   "plants that never get watered"],
                  size=13.5, font=MONO, line_spacing=1.2)
    add_text(s, 0.62, 4.38, 8.8, 0.7,
             "You don't need to answer now. Remember it — in Lesson 2, we turn it "
             "into your project.", size=17, align=PP_ALIGN.CENTER, line_spacing=1.2)
    set_notes(s, "4 min — the memory point of the whole lesson. Slow your pace. "
                 "Read the three examples, then stay silent for 30 seconds and let "
                 "them actually think: [Wait time: 30 s — do not fill the silence. "
                 "Let it sit.] Land it: \"You don't need to answer now. Just "
                 "remember it — better yet, jot it down in your phone notes "
                 "tonight. In Lesson 2, we turn it into your project.\" Someone "
                 "blurts an answer mid-silence? Smile, take one sentence, say "
                 "\"Remember it — we'll use it in Lesson 2\", and keep the silence "
                 "going. TA note: watch who is actually thinking (2–3 names — you "
                 "can call on them at the start of Lesson 2).")

    # ---------------------------------------------------------------- 13 next
    s = page(prs, 13)
    add_title_bar(s, "Next Lesson: Light Up Your First Piece of Hardware")
    add_text(s, 0.62, 1.5, 8.8, 1.35,
             "You say one sentence, AI writes the instruction, and the board comes "
             "alive in three minutes.\nBy the end of the lesson, your name will be "
             "glowing on the screen.", size=17.5, line_spacing=1.3)
    add_card(s, 2.4, 3.0, 5.2, 1.0, fill=WHITE, border=INK, border_w=1.0)
    add_text(s, 2.4, 3.2, 5.2, 0.4, "Your new partner: Grove Beginner Kit",
             size=19, bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 4.35, 8.8, 0.5,
             "The kickoff ends here — bring your problem. See you then.",
             size=18, align=PP_ALIGN.CENTER)
    set_notes(s, "2 min — read it almost verbatim as the send-off: \"Next lesson: "
                 "light up your first piece of hardware with AI. You say one "
                 "sentence, AI writes the instruction, and the board comes alive "
                 "in three minutes. By the end of the lesson, your name will be "
                 "glowing on the screen. Bring your problem. See you then.\"")

    prs.save(OUT)
    print("SAVED:", os.path.abspath(OUT))
    print("slides:", len(prs.slides._sldIdLst))

if __name__ == "__main__":
    main()
