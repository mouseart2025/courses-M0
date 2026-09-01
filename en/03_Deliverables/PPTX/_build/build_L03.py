"""
Build the English Lesson 3 deck (Give Your Project a Screen, 19 slides, 3 h)
from M0_EN_PPTPlan_CFG-5_Lesson03_GiveYourProjectAScreen_v1.md (brand rebuild).

Output: 交付物_EN/03_Deliverables/PPTX/M0_EN_Deck_CFG-5_Lesson03_GiveYourProjectAScreen_v1.pptx
Layout per chaihuo-ppt-brand.md: white 70 / yellow 15 / ink 10 / red 5, 960x540.
Red budget: slide 17 (proofreading warning) ONLY.
Wio Terminal photos not yet captured -> flat line-art placeholder cards
(brand downgrade path: instructor holds the real unit; screenshots run live).
No CJK / full-width / emoji glyphs on screen — ASCII-safe screen text.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder_lib import *
from pptx.util import Inches

TOTAL = 19
DECK_LABEL = "Give Your Project a Screen"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson03_GiveYourProjectAScreen_v1.pptx")
KIT_PHOTO = "/Users/leonfeng/Baiduyun/M0/M0-V2/assets/L1_板子全貌图_Grove Beginner Kit.png"


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


def wio_art(s, x, y, w=2.2, h=1.55, lit=None):
    """Flat line-art Wio Terminal: screen + 3 buttons + joystick."""
    add_card(s, x, y, w, h, fill=WHITE, border=INK, border_w=2.0)
    sw, sh = w * 0.62, h * 0.52
    sx, sy = x + (w - sw) / 2, y + 0.12
    add_rect(s, sx, sy, sw, sh, fill=WHITE, border=INK, border_w=1.5)
    if lit:
        add_text(s, sx, sy + sh / 2 - 0.18, sw, 0.36, lit, size=13, bold=True,
                 mono=True, align=PP_ALIGN.CENTER)
    by = y + h - 0.34
    for i in range(3):
        add_oval(s, x + 0.28 + i * 0.42, by, 0.16, fill=YELLOW, border=INK)
    add_oval(s, x + w - 0.5, by - 0.07, 0.26, fill=WHITE, border=INK)


def main():
    prs = new_deck()

    # ---------------------------------------------------------------- 01 cover
    s = page(prs, 1)
    add_text(s, 0.62, 1.30, 6.4, 0.35,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0)",
             size=14)
    add_text(s, 0.62, 1.68, 8.76, 0.85, "Give Your Project a Screen",
             size=38, bold=True)
    add_rect(s, 0.62, 2.62, 1.6, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 2.92, 8.76, 0.4,
             "Wio Terminal · HMI (Human-Machine Interface) board · M0 Lesson 3",
             size=15)
    add_text(s, 0.62, 3.45, 6.4, 0.5,
             "From today, your builds have a real interface.",
             size=18, bold=True)
    wio_art(s, 7.0, 3.3, w=2.3, h=1.6, lit="HELLO")
    add_text(s, 7.0, 4.95, 2.3, 0.28, "Wio Terminal (screen lit)",
             size=10, align=PP_ALIGN.CENTER)
    set_notes(s, "Cover — loops before class. Open with one welcome line and go "
                 "straight to slide 02 — the cover is not a talking page. Wio "
                 "Terminal photo on the right (screen lit, 45-degree angle — "
                 "line-art placeholder until the photo shoot), yellow rule "
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
        ("Look at the Project Wall — everyone's manifesto is up there.",
         {"size": 14, "bold": True}),
        ("It's the north star for every big project after this.",
         {"size": 12.5}),
    ], line_spacing=1.3)
    yellow_box(s, 0.62, 3.6, 8.76, 0.85, [
        "Open your Student Workbook (or notebook) —",
        "everything produced today continues in your own document."],
        size=13)
    set_notes(s, "Before we start, let's collect last session's work: if you "
                 "used an online doc, send me the link; if you wrote by hand, "
                 "send a photo — if it's not in yet, make a note of it and "
                 "finish before you leave today. (point at the Project Wall) "
                 "Look — last session's wall: everyone's manifesto is up there. "
                 "Last time you set your topic and learned the five rules; "
                 "today we hand out new gear — your project gets a real "
                 "interface from today. Keep your manifesto and three-box "
                 "design sheet at hand — we won't touch them today, but "
                 "they're the north star for every big project after this. "
                 "Hard 5-minute timebox on the collection — no per-item "
                 "feedback; the not-yet-in list goes to the TA to register, "
                 "don't haggle. Output anchor: last session's four outputs "
                 "are in (manifesto / design sheet / review & trade-off / "
                 "log). [Project Wall photo: select from Lesson 2's TA shot — "
                 "wall only, no faces.]")

    # ---------------------------------------------------------------- 03 new gear
    s = page(prs, 3)
    add_title_bar(s, "New Gear — From Board to Handheld")
    add_subtitle(s, "Meet the Wio Terminal: a handheld little computer",
                y=1.0, size=17)
    wio_art(s, 6.9, 1.5, w=2.4, h=1.7, lit="WIO")
    iy = 1.5
    for item in ["Color screen", "Three buttons + a five-way joystick",
                 "Sensors built in"]:
        add_yellow_dot_item(s, 0.72, iy, 5.8, item, size=15)
        iy += 0.45
    add_card(s, 0.62, 3.0, 5.9, 1.0, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 0.8, 3.12, 5.54, 0.8, [
        ("BEFORE YOU FLASH: slide the switch on the side — slide, slide.",
         {"size": 12.5, "bold": True}),
        ('That tells the board: "get ready for new instructions."',
         {"size": 12.5}),
    ], line_spacing=1.3)
    yellow_box(s, 0.62, 4.25, 5.9, 0.8, [
        "No response? Slide it. — Everyone, drill it with me twice."],
        size=13.5)
    set_notes(s, "(hold up the Wio) New gear. It's called the Wio Terminal — "
                 "think of it as a handheld little computer: a color screen, "
                 "three buttons, a five-way joystick, and sensors built in. "
                 "One thing is different from the old board: (hold it up, "
                 "point at the switch) before you flash, slide the switch on "
                 "the side — slide, slide — that's how you tell the board 'get "
                 "ready for new instructions.' Everyone: drill it with me "
                 "twice. The switch drill happens NOW, and the problems "
                 "surface NOW — that saves 20 minutes of rescue attempts "
                 "during coding. The mantra card goes on every desk: 'No "
                 "response? Slide it.' [Switch close-up photo: yellow circle "
                 "marking the switch — to photograph.]")

    # ---------------------------------------------------------------- 04 warm-up
    s = page(prs, 4)
    add_title_bar(s, "Switch the Board Type — Same Old Flow, Same Old Line")
    add_card(s, 0.62, 1.35, 5.4, 1.3, fill=CODEBG, border=INK, border_w=1.5)
    add_multiline(s, 0.8, 1.5, 5.04, 1.05, [
        ("Display in large text on the screen:", {"size": 12.5, "mono": True}),
        ("HELLO and my name (pinyin or English): ___", {"size": 12.5,
                                                        "mono": True,
                                                        "bold": True}),
    ], line_spacing=1.5)
    add_card(s, 6.2, 1.35, 3.18, 1.3, fill=WHITE, border=INK, border_w=1.0)
    add_multiline(s, 6.36, 1.47, 2.86, 1.1, [
        ("[ success", {"size": 10.5, "bold": True}),
        ("screenshot ]", {"size": 10.5, "bold": True}),
        ("the screen showing HELLO", {"size": 9.5}),
    ], line_spacing=1.35, align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 3.0, 8.76, 1.1, [
        "New hardware — and everything you already know still works.",
        "Nothing is wasted. And the letters are prettier now."],
        title="Confidence anchor:", size=14)
    set_notes(s, "Switch the board type in Codecraft — choose Wio Terminal, "
                 "same old flow. Then send the line you've known since your "
                 "first lesson: 'Display in large text on the screen: HELLO "
                 "and my name (pinyin or English): ___.' (wait for the room to "
                 "light up) See — new hardware, and everything you already "
                 "know still works. Nothing is wasted. Why English on screen — "
                 "this board's Chinese font library is unreliable; all screen "
                 "display today is English / numbers / graphics (course-wide "
                 "rule from Lesson 1). 'Switching hardware costs zero "
                 "learning' is today's confidence anchor — point at the color "
                 "screen and add: 'and the letters are prettier now.' "
                 "Serial-port problems follow the old plan: swap cable -> "
                 "swap machine -> pair up. [Warm-up success screen: "
                 "Rehearsal-1 backup.]")

    # ---------------------------------------------------------------- 05 walk-around
    s = page(prs, 5)
    add_title_bar(s, "Walk Around — Meet Your New Partner")
    wio_art(s, 0.62, 1.4, w=3.3, h=2.5, lit="WIO")
    labels = [
        ("Color screen", "your project's face: interfaces, numbers, graphics "
         "live here"),
        ("Three buttons", "the human's hand: press, and give your project "
         "commands"),
        ("Five-way joystick", "the human's hand: nudge, and game consoles & "
         "menus run on it"),
        ("Microphone", "it hears things: clap to switch, a sound-level meter"),
        ("Light sensor", "it knows light from dark: a light that turns on by "
         "itself at night"),
        ("Accelerometer", "it knows moving & tilting: shake detection, fall "
         "alarms"),
        ("Buzzer", "it makes sound: reminders, alarms"),
        ("SD card slot (small)", "it can store things; just know it exists"),
        ("Grove port (small)", "the door for new modules later; just know it "
         "exists"),
    ]
    ly = 1.35
    for head, body in labels:
        add_yellow_dot_item(s, 4.2, ly, 5.2, head, size=11, bold=True)
        add_text(s, 4.36, ly + 0.2, 5.04, 0.2, body, size=8.5)
        ly += 0.42
    add_text(s, 0.62, 4.35, 3.3, 0.3, "(line-art stand-in for the", size=10,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 4.58, 3.3, 0.3, "annotated board photo)", size=10,
             align=PP_ALIGN.CENTER)
    add_golden_line(s, 4.2, 5.0, 5.2,
                    "Every time I name a part, find it on your board with your "
                    "finger — and touch it.", size=11)
    set_notes(s, "Let's walk around and meet your new partner. (hold up the "
                 "Wio and label as you go, one sentence each) The color "
                 "screen — your project's face. Three buttons plus a "
                 "five-way joystick — the human's hand. The light sensor — it "
                 "knows light from dark. The microphone — it hears things. "
                 "The accelerometer — it knows whether it's moving and which "
                 "way it's tilted. The buzzer — it can make sound. Two small "
                 "things over here, ears only today: the SD card slot — it "
                 "can store things; the Grove port — the door for adding new "
                 "modules later. These two, just know they exist. The "
                 "walk-around never becomes a manual read — every time you "
                 "name a part, students find it on their own board with a "
                 "finger and touch it. A student presses on internet? 'It can "
                 "— that's a later lesson. Today, just remember it exists.' "
                 "[Annotated tour diagram to be made: base = top-down photo, "
                 "nine 2px leader lines + yellow dots; line-art placeholder "
                 "until then.]")

    # ---------------------------------------------------------------- 06 compare
    s = page(prs, 6)
    add_title_bar(s, "Why New Gear? Your Project Has a Face and Hands")
    add_text(s, 0.62, 1.05, 4.1, 0.3, "OLD BOARD (Grove Beginner Kit)",
             size=12.5, bold=True)
    s.shapes.add_picture(KIT_PHOTO, Inches(1.05), Inches(1.4), Inches(3.2),
                         Inches(2.4))
    add_text(s, 0.62, 3.9, 4.1, 0.7,
             "Strong at sensing the world — sensors soldered on, plug and play",
             size=12, align=PP_ALIGN.CENTER, line_spacing=1.15)
    add_text(s, 4.68, 2.4, 0.3, 0.5, "->", size=20, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 5.0, 1.05, 4.4, 0.3, "NEW HANDHELD (Wio Terminal)",
             size=12.5, bold=True)
    wio_art(s, 5.65, 1.4, w=2.6, h=1.9, lit="WIO")
    add_text(s, 5.0, 3.9, 4.4, 0.7,
             "Adds a color screen, joystick and wireless — strong at letting "
             "people interact with your project", size=12,
             align=PP_ALIGN.CENTER, line_spacing=1.15)
    add_golden_line(s, 0.62, 4.62, 8.76,
                    "Use both boards — that one senses the world; this one "
                    "lets people interact with your project.", size=14)
    add_text(s, 0.62, 1.42, 8.76, 0.28,
             "Write in your workbook:  \"Wio has ___ more than the old board "
             "(at least 3)\"  ·  \"the first thing I want to make with it is "
             "___\"", size=10.5, align=PP_ALIGN.CENTER)
    set_notes(s, "Now compare with the old board: the old one's strength is "
                 "sensing the world — sensors soldered on, plug and play. This "
                 "one adds a color screen, a joystick and wireless — its "
                 "strength is letting people interact with your project. One "
                 "sentence: why did we change gear? From today, your project "
                 "has a face and hands. Then the two workbook lines. Output "
                 "anchor: the two lines written in everyone's workbook.")

    # ---------------------------------------------------------------- 07 tick row
    s = page(prs, 7)
    add_title_bar(s, "Touching Isn't Knowing — Lighting It Up Is")
    names = ["Buttons", "Joystick", "Microphone", "Light", "Accelerometer"]
    bw = 1.62
    for i, nm in enumerate(names):
        x = 0.62 + i * (bw + 0.16)
        add_card(s, x, 1.45, bw, 0.9, fill=WHITE, border=INK, border_w=1.5)
        add_text(s, x, 1.58, bw, 0.3, nm, size=11.5, bold=True,
                 align=PP_ALIGN.CENTER)
        add_rect(s, x + bw / 2 - 0.12, 1.95, 0.24, 0.24, fill=WHITE,
                 border=INK, border_w=1.5)
    add_text(s, 0.62, 2.7, 8.76, 0.4,
             "Five micro-experiments, one line each —", size=17, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 3.15, 8.76, 0.4,
             "I send mine first, then you send yours.", size=17,
             align=PP_ALIGN.CENTER)
    add_golden_line(s, 0.62, 3.85, 8.76,
                    "Don't just watch me — send a line and try it yourself.",
                    size=16)
    add_text(s, 0.62, 4.65, 8.76, 0.55,
             "The lines are printed in your Student Workbook — follow me on "
             "the screen. Lit one up? Tick the box in your workbook.",
             size=12, align=PP_ALIGN.CENTER, line_spacing=1.2)
    set_notes(s, "Touching isn't knowing — lighting it up is. Five "
                 "micro-experiments, one line each, watch it come alive. The "
                 "lines are printed in your Student Workbook — follow me on "
                 "the screen. The rhythm: I send mine first, then you send "
                 "yours — don't just watch me, send a line and try it "
                 "yourself. Flip fast — this page is the round's "
                 "instructions, not a talking page.")

    # ------------------------------------------------------- 08-12 micro-exp
    def micro_exp(n, part, toy, instr_lines, shot_desc, closing, notes,
                  workbook=None):
        s = page(prs, n)
        add_title_bar(s, f"Micro-Experiment {n - 7}/5 · {part}")
        add_subtitle(s, toy, y=1.0, size=17)
        add_card(s, 0.62, 1.42, 5.4, 1.55, fill=CODEBG, border=INK, border_w=1.0)
        lines = [("I'm using the Wio Terminal. Please make this work:",
                  {"size": 11.5, "mono": True})]
        for t in instr_lines:
            lines.append((t, {"size": 11.5, "mono": True}))
        add_multiline(s, 0.8, 1.56, 5.04, 1.3, lines, line_spacing=1.4)
        add_card(s, 6.2, 1.42, 3.18, 1.55, fill=WHITE, border=INK, border_w=1.0)
        add_multiline(s, 6.36, 1.52, 2.86, 1.35, [
            ("[ success", {"size": 10.5, "bold": True}),
            ("screenshot ]", {"size": 10.5, "bold": True}),
            (shot_desc, {"size": 9.5}),
        ], line_spacing=1.3, align=PP_ALIGN.CENTER)
        add_text(s, 6.2, 2.72, 3.18, 0.25,
                 "this is what success looks like", size=9.5, bold=True,
                 align=PP_ALIGN.CENTER)
        if isinstance(closing, list):
            cy = 3.35
            for cl in closing:
                add_text(s, 0.62, cy, 8.76, 0.35, cl, size=14,
                         align=PP_ALIGN.CENTER)
                cy += 0.42
        else:
            add_text(s, 0.62, 3.35, 8.76, 0.35, closing, size=14,
                     align=PP_ALIGN.CENTER)
        if workbook:
            yellow_box(s, 0.62, 4.3, 8.76, 0.85, workbook, size=11.5)
        set_notes(s, notes)
        return s

    micro_exp(
        8, "Buttons", "The Three-Key Piano",
        ["Press buttons A/B/C to play do, mi, sol.",
         "Show DO / MI / SOL in large text on the screen."],
        "DO in large text",
        ["Press it, and it answers you — A, B, C: a little piano."],
        "The first one, the three-key piano. Watch me send it — (send) press "
        "A: DO; press B: MI; press C: SOL. Your turn — send it, try it. Can "
        "play a little tune? Raise your hand. New line counts only if it ran "
        "in rehearsal — a line that won't run falls back to the original "
        "'number-report' version; a single dead unit gets swapped, not fixed. "
        "One experiment stuck more than 2 minutes is too long — protect the "
        "round's rhythm.")

    micro_exp(
        9, "Joystick", "Push the Ball",
        ["Draw a small ball in the center of the screen.",
         "Push the joystick and the ball moves that way."],
        "the ball pushed off-center",
        ["Nudge it, and the ball listens.",
         "The joystick presses in too — found it? Raise your hand."],
        "The second one, push the ball. Push the joystick and the ball runs "
        "that way. (demo) Your turn — see who can park the ball steadily in "
        "the corner. A student discovers the joystick also presses in (it has "
        "a button)? Affirm the discovery — it goes on the list of usable "
        "inputs for the free round. Line won't run -> fall back to the "
        "number-report version (UP / DOWN / LEFT / RIGHT).")

    micro_exp(
        10, "Microphone", "Blow Out the Candle",
        ["Draw a lit candle in the center of the screen.",
         "Blow at the microphone and the flame goes out; after 2 seconds it "
         "lights again."],
        "the flame out (or relit)",
        ["One blow, the candle goes out.",
         "Sound doesn't need to report a number — it just needs to do the "
         "job."],
        "The third one, blow out the candle. Send it — blow at the "
        "microphone, the flame goes out; after 2 seconds it lights again. "
        "Your turn. A student asks how it knows they blew? One sentence: "
        "'Blow hard enough and it counts as blowing out the candle; the exact "
        "units don't matter.'")

    micro_exp(
        11, "Light", "The Board Afraid of the Dark",
        ["Draw two open eyes on the screen.",
         "When the light gets dim, close the eyes and show ZZZ;",
         "when it gets bright, open them again."],
        "eyes closed, ZZZ showing",
        ["Cover it, and it falls asleep.",
         "Last lesson's dark-detecting light — in a new costume."],
        "The fourth one, the board afraid of the dark. Send it — cover the "
        "board with your palm, the eyes close, ZZZ appears; take your hand "
        "away, it wakes up. This is last lesson's 'dark-detecting light' "
        "skill, in a new costume. Point back to Lesson 1 as you go — the "
        "Sense -> Logic -> Output model is still the engine under every one "
        "of these toys.")

    micro_exp(
        12, "Accelerometer", "The Balance Ball",
        ["Draw a square frame with a small ball inside.",
         "Tilt the board and the ball rolls toward the low side."],
        "the ball rolled to one side",
        ["Tilt it, and the ball rolls downhill.",
         "Shake detection, fall alarms — this is the one."],
        "The last one, the balance ball. Send it — tilt the board, and the "
        "ball rolls downhill. It can feel how you move it. All five tried? "
        "Open your workbook, tick the boxes, and write one line: what "
        "surprised me most, and why. Fast students add a free line on top of "
        "the current experiment ('make the ball a different color' / 'beep "
        "when the ball touches the edge'); slow students pass by keeping the "
        "first three. Output anchor: the ticks + one line in everyone's "
        "workbook.",
        workbook=['"I lit up:  [ ] buttons  [ ] joystick  [ ] microphone  [ ] '
                  'light  [ ] accelerometer;  what surprised me most was ___ '
                  'because ___."'])

    # ---------------------------------------------------------------- 13 soul
    s = page(prs, 13)
    add_title_bar(s, "One Idea, Two Ways of Saying It")
    add_card(s, 0.62, 1.32, 4.1, 1.8, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.8, 1.44, 3.74, 0.3, '"Make a counter screen."', size=13,
             mono=True, bold=True)
    add_text(s, 0.8, 1.9, 3.74, 0.55, "->  what AI freely gives you",
             size=11.5)
    add_text(s, 0.8, 2.5, 3.74, 0.5, "[ screenshot: vague result ]",
             size=10.5, align=PP_ALIGN.CENTER)
    add_text(s, 4.68, 2.0, 0.3, 0.5, "<-", size=20, bold=True,
             align=PP_ALIGN.CENTER)
    add_card(s, 5.0, 1.32, 4.4, 1.8, fill=CODEBG, border=YELLOW, border_w=3.0)
    add_multiline(s, 5.18, 1.44, 4.04, 1.55, [
        ('"Show a number in the largest text', {"size": 10.5, "mono": True}),
        ('in the center of the screen; show', {"size": 10.5, "mono": True}),
        ('COUNTER in small text at the top-', {"size": 10.5, "mono": True}),
        ('left; make the number red."', {"size": 10.5, "mono": True}),
        ("->  the precise result", {"size": 11.5, "bold": True}),
    ], line_spacing=1.25)
    add_text(s, 0.62, 3.3, 8.76, 0.5, "POSITION   ·   SIZE   ·   COLOR",
             size=26, bold=True, align=PP_ALIGN.CENTER)
    add_card(s, 0.62, 4.05, 8.76, 0.95, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 0.8, 4.16, 8.4, 0.75, [
        ("How to describe a screen:", {"size": 12.5, "bold": True}),
        ("At [position], show [content] in [size/color]; when [action], "
         "[change].", {"size": 12.5, "mono": True}),
    ], line_spacing=1.35)
    set_notes(s, "Hardware's all lit up — now lesson one of using it well: "
                 "how do you get AI to give you a good screen? An experiment, "
                 "one idea two ways of saying it. First way: (send) 'Make a "
                 "counter screen.' — see what it gives you. (show the result) "
                 "Second way: (send) 'Show a number in the largest text in "
                 "the center of the screen; show COUNTER in small text at the "
                 "top-left; make the number red.' — now see what it gives you. "
                 "(project side by side) What's the difference? Describing a "
                 "screen means saying three things clearly: position, size, "
                 "color. Land the extension line: 'Logic says do this when "
                 "that happens. Screens say what something is, where it sits, "
                 "what it looks like. Two ways of speaking — you need both.' If "
                 "AI does well both times: 'Today it guessed your mind right — "
                 "but your project is ten times more complex. You can't "
                 "afford the wrong guess.' NON-NEGOTIABLE: really send both "
                 "lines live in the same conversation — the screenshots are "
                 "backups only; live authenticity can't be faked.")

    # ---------------------------------------------------------------- 14 follow
    s = page(prs, 14)
    add_title_bar(s, "Follow-Along: The Button Counter — Two Steps on Purpose")
    add_text(s, 0.62, 1.18, 8.76, 0.3, "STEP 1 · The screen only:", size=14,
             bold=True)
    add_card(s, 0.62, 1.5, 8.76, 0.78, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 0.8, 1.62, 8.4, 0.58, [
        ("Show the number 0 in the largest text in the center of the screen, "
         "and COUNTER in small text at the top-left.   ->  Flash it, look at "
         "it.", {"size": 11.5, "mono": True}),
    ], line_spacing=1.3)
    add_text(s, 0.62, 2.45, 8.76, 0.3, "STEP 2 · The behavior:", size=14,
             bold=True)
    add_card(s, 0.62, 2.77, 8.76, 1.05, fill=CODEBG, border=INK, border_w=1.0)
    add_multiline(s, 0.8, 2.89, 8.4, 0.85, [
        ("When I press button A, add one to the number; when I press B, reset "
         "to zero.", {"size": 11.5, "mono": True}),
        ("-> Flash again — then one more line: \"Every time the count reaches "
         "10, the buzzer beeps once to celebrate.\"", {"size": 11.5,
                                                       "mono": True}),
    ], line_spacing=1.35)
    yellow_box(s, 0.62, 4.05, 8.76, 0.95, [
        "First describe the looks, then the actions — it doesn't get confused.",
        'Buttons not responding? "No response? Slide it."'], size=13)
    set_notes(s, "Follow along, and we say it in two steps on purpose. Step "
                 "one, the screen only: 'Show the number 0 in the largest text "
                 "in the center of the screen, and COUNTER in small text at "
                 "the top-left.' Flash it, look at it. Step two, the behavior: "
                 "'When I press button A, add one to the number; when I press "
                 "B, reset to zero.' Flash again — then one more line to the "
                 "whole class: 'Every time the count reaches 10, the buzzer "
                 "beeps once to celebrate.' (the room fills with button "
                 "presses; count to 10 and hear the beep) See? First describe "
                 "the looks, then the actions — two ways of speaking, two "
                 "separate lines, and it doesn't get confused. Wrong? Add one "
                 "more line. That's also the old Five-Rules rule: one thing at "
                 "a time. The number-one reason buttons don't respond: flash "
                 "mode never exited — 'No response? Slide it (back to run "
                 "mode).' The TA checks this first. Text overflowing / color "
                 "not showing? One sentence: 'This is exactly the precision "
                 "problem of describing looks — add one more line of "
                 "description and have it change.' Someone already making a "
                 "joystick game? Don't forbid: 'Fine to play — but the "
                 "two-screens requirement stays.' Stays fixed during "
                 "follow-along.")

    # ---------------------------------------------------------------- 15 free round
    s = page(prs, 15)
    add_title_bar(s, "Free Round — Make Something With Two Screens")
    add_text(s, 0.62, 1.12, 8.76, 0.35,
             "Switch between them with a button or the joystick.", size=15,
             bold=True, align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 1.6, 8.76, 0.28,
             "Buttons · Joystick · Microphone · Light · Accelerometer — pick "
             "what's comfortable.", size=12, align=PP_ALIGN.CENTER)
    ex = ["Clock", "Mood display", "Stopwatch", "Your own menu",
          "Reaction tester"]
    bw = 1.66
    for i, nm in enumerate(ex):
        x = 0.62 + i * (bw + 0.1)
        add_card(s, x, 2.0, bw, 0.55, fill=WHITE, border=INK, border_w=1.5)
        add_text(s, x, 2.13, bw, 0.3, nm, size=11.5, bold=True,
                 align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.65, 8.76, 0.28,
             "(screen turns green -> press A -> shows your milliseconds — "
             "naturally two screens; content in English, numbers or graphics)",
             size=10.5, align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 3.1, 8.76, 1.2, [
        "Tell your neighbor what your two screens each look like — position, "
        "size, color, said clearly — BEFORE you talk to AI."],
        title="Old discipline:", size=13)
    add_golden_line(s, 0.62, 4.45, 8.76,
                    'Write in your workbook — "the sentence I said to AI '
                    'about my screen": your proudest description.', size=13)
    set_notes(s, "Free build, one-line brief: make something with two screens, "
                 "and switch between them with a button or the joystick. A "
                 "clock / a mood display / a stopwatch / a menu of your own / "
                 "a reaction tester (the screen turns green, you press A, it "
                 "shows your milliseconds — naturally two screens) — anything "
                 "works (screen content in English, numbers or graphics). You "
                 "now have five inputs in your hands — pick what's "
                 "comfortable. Old discipline: tell your neighbor what your "
                 "two screens each look like BEFORE you touch the keyboard — "
                 "position, size, color, said clearly — then talk to AI. "
                 "Collect 1-2 'described unclearly -> AI drifted off' cases "
                 "(the drift gallery needs them next). Fast students: add a "
                 "sensor link to the two-screen project. Slow students' bar: "
                 "the counter + one custom change. A student dumps the whole "
                 "job on AI at once? 'Directors shoot one scene at a time. Get "
                 "the first screen described beautifully, then the second, and "
                 "only at the end how to switch.' Two screens degrade to one? "
                 "Lower the bar to 'counter + one custom change' and have "
                 "them log 'where I got stuck trying to make two screens.' "
                 "Someone's screen looks great and people gather? Invite them "
                 "to project it — but push one question: 'What exactly did you "
                 "say to AI?' Output anchor: everyone copies one line into "
                 "the workbook. Stays fixed during the free round.")

    # ---------------------------------------------------------------- 16 treasure
    s = page(prs, 16)
    add_title_bar(s, "Whole Room — Come Look at a Treasure")
    add_card(s, 0.62, 1.35, 4.3, 1.9, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.8, 1.5, 3.94, 1.6, [
        ("[ drift case", {"size": 11, "bold": True}),
        ("screenshot ]", {"size": 11, "bold": True}),
        ("a screen that went off the rails", {"size": 10}),
        ("(a student volunteers, or the", {"size": 9.5}),
        ("pre-made Rehearsal-5 case)", {"size": 9.5}),
    ], line_spacing=1.4, align=PP_ALIGN.CENTER)
    add_text(s, 5.08, 1.5, 4.3, 0.35, "They said ___  ->  AI made ___",
             size=15, bold=True)
    add_text(s, 5.08, 1.95, 4.3, 0.35, "->  which sentence went wrong?",
             size=15, bold=True)
    add_golden_line(s, 0.62, 3.55, 8.76,
                    "Thank this student — they stepped in the pit so the whole "
                    "class doesn't have to. A crash isn't a joke; it's "
                    "teaching material.", size=15, h=None)
    set_notes(s, "Whole room, come look at a treasure. (project) See: they "
                 "said ___, AI made ___. Which sentence went wrong? (lead the "
                 "class to find it) There — they forgot to say where. Thank "
                 "this student — they stepped in the pit so the whole class "
                 "doesn't have to. A crash isn't a joke; it's teaching "
                 "material. The volunteer is always voluntary; no volunteer -> "
                 "use the pre-made case from Rehearsal 5; once someone "
                 "volunteers, the pre-made case is dropped. The tone is set: "
                 "the volunteer is the hero — anyone snickering, take the line "
                 "back on the spot: 'They stepped in the pit for the whole "
                 "class. That's a hero.'")

    # ---------------------------------------------------------------- 17 log (RED)
    s = page(prs, 17)
    add_title_bar(s, "Three Takeaways for Using It Well")
    ty = 1.2
    takeaways = [
        "Describe a screen with position, size and color",
        "Make state visible — have the screen show where you are in its steps",
        "Many inputs? Try combinations — button, joystick, microphone, light, "
        "accelerometer",
    ]
    for i, t in enumerate(takeaways):
        num_block(s, 0.62, ty, str(i + 1), size=0.36)
        add_text(s, 1.06, ty, 8.3, 0.32, t, size=13.5, bold=True)
        ty += 0.38
    add_text(s, 0.62, 2.34, 8.76, 0.24,
             'Circle one takeaway — "the one I used most today was #___".  '
             'The log goes into your workbook proofread.', size=10)
    add_text(s, 0.62, 2.66, 8.76, 0.28, "Your log, four sentences:", size=13,
             bold=True)
    ly = 2.98
    for line in ["Today I made ___",
                 'I got stuck on ___  (today: name it — position, size, or '
                 'color?)', "Then ___", "Next time I want ___"]:
        add_yellow_dot_item(s, 0.72, ly, 8.4, line, size=11.5)
        ly += 0.27
    add_grey_box(s, 0.62, 4.1, 8.76, 0.45,
                 'Say it, then send it to AI: "Tidy this into a learning log — '
                 'only what I said, nothing I didn\'t say."', size=11)
    # compact red warning strip (this deck's single red element)
    add_rect(s, 0.62, 4.72, 0.06, 0.48, fill=RED, border=None)
    add_oval(s, 0.82, 4.86, 0.11, fill=RED, border=None)
    add_text(s, 1.04, 4.76, 8.34, 0.4,
             "Warning — AI will make things up with a straight face. "
             "Proofreading is your job.", size=13, bold=True)
    set_notes(s, "Last question: what's different between describing a screen "
                 "to AI and describing logic? (lead them to: logic says 'do "
                 "this when that happens'; screens say 'what something is, "
                 "where it sits, what it looks like') — so, three takeaways for "
                 "using this handheld well. First: describe a screen with "
                 "position, size and color — you saw it with your own eyes; "
                 "say the three things or don't, and you get two different "
                 "things. Second: make state visible — the board has a screen; "
                 "have it show you where it is in its steps, so you always "
                 "know what it's doing. Third: with many inputs, try "
                 "combinations — the best projects often come from trying "
                 "'which input feels most natural.' Then the log: take a photo "
                 "of the screen project, say thirty seconds, the usual four "
                 "sentences — today's 'stuck on' must be specific: position, "
                 "size, or color. Send to AI with the tidy line; when it's "
                 "done, read it: 'AI will make things up with a straight face. "
                 "Proofreading is your job — nobody can do it for you.' The TA "
                 "takes extra build photos (hands only, no faces); students "
                 "without phones get photos taken by the TA, filed by table "
                 "number. Output anchor: circled takeaway + the proofread "
                 "four-sentence log in the workbook.")

    # ---------------------------------------------------------------- 18 buffer
    s = page(prs, 18)
    add_text(s, 0.62, 1.05, 3.0, 1.75, "30", size=96, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.88, 3.0, 0.5, "minutes", size=26, bold=True,
             align=PP_ALIGN.CENTER)
    yellow_box(s, 3.9, 1.2, 5.5, 0.85, [
        "FINISH TO STANDARD (everyone crosses this line)",
        "Counter runs + one two-screen project."], size=12.5)
    add_card(s, 3.9, 2.2, 5.5, 1.5, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 4.08, 2.32, 5.14, 1.3, [
        ("CHALLENGE TASKS (fast lane)", {"size": 12, "bold": True}),
        ("Electronic dice — shake it (or flick the joystick once), the "
         "screen shows a random 1-6.", {"size": 10.5}),
        ("Or: balance-ball hole-in-one — micro-experiment 5 plus a target "
         "hole; the buzzer beeps when the ball drops in.", {"size": 10.5}),
    ], line_spacing=1.25)
    add_card(s, 3.9, 3.85, 5.5, 0.95, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 4.08, 3.95, 5.14, 0.78, [
        ("HELP A NEIGHBOR + ADD A SENSOR LINK", {"size": 12, "bold": True}),
        ("Give your two-screen project a sensor link (e.g., auto-switch to a "
         "night screen when it gets dark).", {"size": 10.5}),
    ], line_spacing=1.25)
    add_golden_line(s, 0.62, 3.62, 3.0,
                    "Standard first, then fast.", size=13)
    add_text(s, 0.62, 4.35, 3.0, 0.75,
             "The buffer is part of the lesson, not early dismissal.",
             size=10.5, line_spacing=1.15)
    add_text(s, 0.62, 5.02, 8.76, 0.28,
             'Did a challenge? Write in your workbook — "I used ___ (which '
             'input) to make ___ (what little thing)."', size=10.5,
             align=PP_ALIGN.CENTER)
    set_notes(s, "Set the tone at the start (announce today's exit per your "
                 "pre-class choice): 'Next 30 minutes work like this: if your "
                 "two-screen project isn't done, finish it — that's the line "
                 "everyone must cross today. Crossed it? [announce today's "
                 "plan: take a challenge task / help your neighbor / add a "
                 "sensor link to your project].' Circulation order: first "
                 "sweep who hasn't crossed the line (the TA watches these), "
                 "then lead the fast ones through challenges. Challenge tasks: "
                 "only the ones you rehearsed — unrehearsed tasks don't go "
                 "out; if none of them run, the buffer keeps only 'finish to "
                 "standard' and 'help a neighbor.' Challenge done? Steer toward "
                 "one line: 'You've got the joystick down — later it becomes a "
                 "controller for your computer. That's the road ahead.' A "
                 "student says 'I'm done, can I leave / play on my phone?' — "
                 "point to the three exits. Everyone clears the bar with 20 "
                 "minutes left? Don't drag — move into the show & tell early "
                 "and finish the wrap at a relaxed pace. Output anchor "
                 "(challenge students): the 'I used ___ to make ___' line in "
                 "the workbook. Stays fixed during the buffer.")

    # ---------------------------------------------------------------- 19 close
    s = page(prs, 19)
    add_title_bar(s, "Flash Show & Tell + Next Time")
    add_text(s, 0.62, 1.15, 8.76, 0.55,
             "In your table, 30 seconds each — demo your project, say one "
             'line: "which input I used, and how I switch screens."',
             size=13, line_spacing=1.15)
    add_text(s, 0.62, 1.85, 8.76, 0.3, "Two things you take away today:",
             size=14, bold=True)
    t2 = [
        "You met the new gear — screen, buttons, joystick, three sensors — "
        "every one lit up by your own hand",
        "You learned lesson one of using it — position, size, color — your "
        "project has a real interface from today",
    ]
    ty = 2.22
    for i, t in enumerate(t2):
        num_block(s, 0.62, ty, str(i + 1), size=0.36)
        add_text(s, 1.06, ty, 8.3, 0.55, t, size=12.5, line_spacing=1.1)
        ty += 0.62
    add_text(s, 0.62, 3.55, 8.76, 0.3, "NEXT TIME", size=13, bold=True,
             align=PP_ALIGN.CENTER)
    yellow_box(s, 0.62, 3.9, 8.76, 1.05, [
        "Lesson 4: Give AI a Team",
        "One complete project end to end: your own smart Pomodoro timer."],
        size=14)
    add_text(s, 0.62, 5.05, 8.76, 0.28,
             "It runs on this very color screen — today's screen skills get "
             "used all the way through. Bring your topic.", size=10.5,
             align=PP_ALIGN.CENTER)
    set_notes(s, "In your table, 30 seconds each: demo your project, say one "
                 "line — 'which input I used, and how I switch screens.' "
                 "(after the show & tell) Last two minutes — take stock. One: "
                 "you met the new gear — the Wio has a screen, buttons, a "
                 "joystick and three sensors, and you lit every one of them "
                 "up yourself. Two: you learned lesson one of using it: "
                 "describe a screen — position, size, color — and your project "
                 "has a real interface from today. Next session is a big day: "
                 "we give AI a team — so it's more than one person working for "
                 "you — and build one complete project end to end: your own "
                 "smart Pomodoro timer. It runs on this very color screen, so "
                 "today's screen skills get used all the way through. Bring "
                 "your topic. Class dismissed! Localize the Pomodoro "
                 "explanation if needed: 'a Pomodoro = a focus timer — 25 "
                 "minutes focused, 5 minutes off, that kind of thing.' After "
                 "class: collect today's work (links or photos), note what's "
                 "missing; leave the mantra cards on the desks and collect "
                 "them — reusable next session.")

    prs.save(OUT)
    print("Saved:", OUT, "slides:", len(prs.slides.__iter__.__self__._sldIdLst))


if __name__ == "__main__":
    main()
