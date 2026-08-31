"""
Build the English Lesson 5 deck (Teach Your Hardware to See, 20 slides)
from M0_EN_PPTPlan_CFG-5_Lesson05_TeachYourHardwareToSee_v1.md (brand rebuild).

Output: 交付物_EN/03_Deliverables/PPTX/M0_EN_Deck_CFG-5_Lesson05_TeachYourHardwareToSee_v1.pptx
Layout per chaihuo-ppt-brand.md: white 70 / yellow 15 / ink 10 / red 5, 960x540.
Red budget: slide 08 (hands-only imaging rule) + slide 15 (required-question column).
Slide 07's demo LED dots use desaturated graphic red/green (NOT brand red).
XIAO photos not yet shot -> xiao_art line art + placeholder cards (plan allows).
No CJK / full-width / emoji on screen.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from builder_lib import *
from pptx.util import Inches
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR

TOTAL = 20
DECK_LABEL = "Teach Your Hardware to See"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "M0_EN_Deck_CFG-5_Lesson05_TeachYourHardwareToSee_v1.pptx")
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


def xiao_art(s, x, y, w=2.5, h=1.75, labels=False):
    """XIAO ESP32S3 Sense line art: board + camera + mic + 2 buttons + slots."""
    add_card(s, x, y, w, h, fill=WHITE, border=INK, border_w=2.0)
    d = min(w, h) * 0.24
    cx = x + w / 2 - d / 2
    cy = y + h * 0.12
    add_oval(s, cx, cy, d, fill=WHITE, border=INK)
    add_oval(s, cx + d * 0.28, cy + d * 0.28, d * 0.44, fill=INK, border=None)
    add_oval(s, x + w * 0.10, cy + d * 0.35, d * 0.22, fill=YELLOW, border=INK)
    add_oval(s, x + w * 0.80, cy + d * 0.35, d * 0.22, fill=YELLOW, border=INK)
    bw_, bh_ = w * 0.17, h * 0.08
    add_rect(s, x + w * 0.18, y + h * 0.58, bw_, bh_, fill=WHITE, border=INK)
    add_rect(s, x + w * 0.65, y + h * 0.58, bw_, bh_, fill=WHITE, border=INK)
    add_rect(s, x + w * 0.18, y + h * 0.80, w * 0.32, h * 0.07, fill=WHITE,
             border=INK)
    add_rect(s, x + w * 0.60, y + h * 0.80, w * 0.20, h * 0.07, fill=WHITE,
             border=INK)
    if labels:
        add_text(s, cx - 0.5, cy - 0.24, d + 1.0, 0.2, "CAMERA", size=8,
                 bold=True, align=PP_ALIGN.CENTER)
        add_text(s, x + w * 0.18 - 0.16, y + h * 0.58 + bh_ + 0.01, bw_ + 0.32,
                 0.18, "RST", size=7.5, align=PP_ALIGN.CENTER)
        add_text(s, x + w * 0.65 - 0.18, y + h * 0.58 + bh_ + 0.01, bw_ + 0.36,
                 0.18, "BOOT", size=7.5, align=PP_ALIGN.CENTER)
        add_text(s, x + w * 0.18 - 0.2, y + h * 0.87 + 0.02, w * 0.32 + 0.4,
                 0.18, "SD CARD", size=7.5, align=PP_ALIGN.CENTER)
        add_text(s, x + w * 0.60 - 0.24, y + h * 0.87 + 0.02, w * 0.20 + 0.48,
                 0.18, "CHARGE", size=7.5, align=PP_ALIGN.CENTER)
        add_text(s, x - 0.1, cy + d * 0.35 - 0.09, w * 0.10 + 0.7, 0.18,
                 "MIC", size=7.5, align=PP_ALIGN.RIGHT)
        add_text(s, x + w * 0.80 - 0.3, cy + d * 0.35 - 0.09, w * 0.10 + 0.7,
                 0.18, "LED", size=7.5)


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
    add_text(s, 0.62, 1.20, 6.6, 0.3,
             "Chaihuo Maker Academy · Smart Hardware Fundamentals (M0)",
             size=13)
    add_text(s, 0.62, 1.55, 8.76, 0.75, "Teach Your Hardware to See",
             size=38, bold=True)
    add_rect(s, 0.62, 2.50, 1.6, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 2.68, 6.4, 0.55,
             "Hand-Train Your First Vision Model · Chaihuo Maker Academy · "
             "M0 Lesson 5", size=14)
    add_text(s, 0.62, 3.50, 6.4, 0.45,
             "Today your board learns a brand-new skill.", size=18, bold=True)
    xiao_art(s, 7.0, 3.35, w=2.3, h=1.6)
    add_text(s, 7.0, 5.00, 2.3, 0.2, "XIAO ESP32S3 Sense", size=9.5,
             align=PP_ALIGN.CENTER)
    set_notes(s, "Cover — loops before class. Open with one welcome line — "
                 "'Welcome to Lesson 5. Last session you built a complete "
                 "Pomodoro timer with the BMAD five roles — today your hardware "
                 "learns a brand-new skill: to see.' — then go straight to "
                 "slide 02; the cover is not a talking page. XIAO photo on the "
                 "right (thumb-size, camera side up, next to a thumb for "
                 "scale — line-art placeholder until the rehearsal photo), "
                 "yellow rule under the subtitle.")

    # ---------------------------------------------------------------- 02 see
    s = page(prs, 2)
    add_title_bar(s, 'How Does a Machine "See"?')
    add_card(s, 0.62, 1.30, 2.5, 0.70, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.62, 1.30, 2.5, 0.70, "PHOTO IN", size=15, bold=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, 3.22, 1.32, 0.5, 0.66, "→", size=26, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_card(s, 3.80, 1.30, 2.40, 0.70, fill=CODEBG, border=INK, border_w=1.5)
    add_text(s, 3.80, 1.30, 2.40, 0.70, "algorithm", size=14, mono=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, 6.30, 1.32, 0.5, 0.66, "→", size=26, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_card(s, 6.88, 1.30, 2.50, 0.70, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 6.88, 1.30, 2.50, 0.70, "EXPERIENCE OUT", size=14, bold=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    cards = [
        ("TESLA", "eight cameras, a full 360° of road"),
        ("PANDA WATCH", "one camera over one mountain; spots a panda, "
                        "reports the location"),
        ("HUMMINGBIRD FEEDER", "recognizes a hummingbird, notes when it came "
                               "to eat"),
    ]
    for i, (head, body) in enumerate(cards):
        cx = 0.62 + i * 2.96
        add_card(s, cx, 2.35, 2.84, 1.70, fill=WHITE, border=INK,
                 border_w=1.5)
        add_text(s, cx + 0.16, 2.47, 2.52, 0.28, head, size=12.5, bold=True)
        add_text(s, cx + 0.16, 2.82, 2.52, 1.10, body, size=10.5,
                 line_spacing=1.2)
    add_grey_box(s, 0.62, 4.30, 8.76, 0.62,
                 "None of them talks or writes. They see.", size=15)
    set_notes(s, "To open today — let's see how it 'sees'. (point at the flow) "
                 "A camera captures an image and turns it into numbers — the "
                 "photo goes in, 'experience' comes out. The algorithm in the "
                 "middle has a big name — you don't need to memorize it. "
                 "(point at the three cards) Tesla runs eight cameras looking "
                 "at a full 360° of road. In a huge forest, one camera watches "
                 "over one mountain — when it spots a panda, it reports the "
                 "location. A hummingbird feeder — when it recognizes a "
                 "hummingbird, it notes what time it came to eat. Spot the "
                 "common thread? None of them talks or writes. They see. "
                 "Today, your board learns to do the same. Skim the example "
                 "cards — don't linger. 'What is feature extraction / CNN?' — "
                 "an algorithm that finds patterns in photos. You don't need "
                 "the name — just remember: photo in, experience out. Three "
                 "examples dragging — only the hummingbird; Tesla and panda "
                 "get one line each.")

    # ---------------------------------------------------------------- 03 eyes
    s = page(prs, 3)
    add_title_bar(s, "Your Third Board — The Eyes")
    add_subtitle(s, "(and the second kind of AI)", y=1.00, size=14)
    left_cards = [
        (1.40, 0.72, "GROVE KIT = SKIN", "feels hot, cold, motion"),
        (2.42, 0.72, "WIO = FACE", "has a screen and buttons"),
        (3.44, 0.95, "XIAO = EYES",
         "has a camera (and a microphone): it can see and hear"),
    ]
    for cy_, ch_, head, body in left_cards:
        add_card(s, 0.62, cy_, 4.15, ch_, fill=WHITE, border=INK,
                 border_w=1.5)
        add_multiline(s, 0.77, cy_ + 0.09, 3.85, ch_ - 0.16, [
            (head, {"size": 13, "bold": True}),
            (body, {"size": 11}),
        ], line_spacing=1.2)
    add_text(s, 2.45, 2.13, 0.5, 0.3, "↓", size=17, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER)
    add_text(s, 2.45, 3.15, 0.5, 0.3, "↓", size=17, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER)
    add_card(s, 5.05, 1.40, 4.33, 1.40, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 5.20, 1.50, 4.03, 1.20, [
        ("YOU TELL IT, IT BUILDS", {"size": 13, "bold": True}),
        ("(the AI you've been using)", {"size": 10}),
        ("tell Codecraft what you want → it writes the instructions",
         {"size": 11}),
    ], line_spacing=1.25)
    add_card(s, 5.05, 2.92, 4.33, 1.55, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 5.20, 3.00, 4.03, 1.42, [
        ("YOU SHOW IT, IT LEARNS", {"size": 13, "bold": True}),
        ("(new today)", {"size": 10}),
        ("say nothing; show it photos, lots of them → it learns to recognize "
         "on its own", {"size": 10.5}),
        ("the website: SenseCraft AI — where you teach boards to recognize "
         "things", {"size": 9.5}),
    ], line_spacing=1.2)
    add_grey_box(s, 0.62, 4.62, 8.76, 0.52,
                 "First half of today: no typing. You talk with photos.",
                 size=14)
    set_notes(s, "This is your third board. The first one, the Grove kit — "
                 "that's skin: it feels hot, cold, motion. The second one, the "
                 "Wio — that's the face: it has a screen and buttons. This "
                 "thumb-sized little board is the eyes — it has a camera, and "
                 "a microphone too. It can see and hear. So far you've used "
                 "one kind of AI: you tell it, it builds — you tell Codecraft "
                 "what you want and it writes the instructions for you. Today "
                 "you meet a second kind: you show it, it learns — you don't "
                 "say a word; you show it photos, lots of them, and it learns "
                 "to recognize on its own. The website is called SenseCraft "
                 "AI — it's where you teach boards to recognize things. First "
                 "half of today: no typing. You talk with photos. 'Is this the "
                 "same AI as ChatGPT?' — both learn from lots of examples, but "
                 "one learns text and the other learns images. Want the deep "
                 "version, find me at break.")

    # ---------------------------------------------------------------- 04 xiao
    s = page(prs, 4)
    add_title_bar(s, "Meet the XIAO — the Little Eye Board")
    add_subtitle(s, "XIAO ESP32S3 Sense · anatomy", y=1.00, size=12)
    xiao_art(s, 0.90, 1.45, w=3.30, h=2.50, labels=True)
    parts = [
        (1.55, "Camera — its eye"),
        (2.20, "Microphone — its ear"),
        (2.85, "Two little buttons — reset and boot (you'll use them when "
               "flashing)"),
        (3.62, "Tiny LED · SD card slot · charging port (just know they "
               "exist)"),
    ]
    for py_, txt in parts:
        add_yellow_dot_item(s, 4.60, py_, 4.78, txt, size=12.5,
                            line_spacing=1.15)
    yellow_box(s, 0.62, 4.30, 8.76, 0.85, [
        "The most special thing: AI lives inside the board. Once the trained "
        "model is loaded in, it recognizes your gestures with NO internet at "
        "all."], size=13)
    set_notes(s, "Its name is XIAO ESP32S3 Sense — you don't need to memorize "
                 "it; call it the little eye board. It has a whole family of "
                 "siblings, all different models; today we use the one with "
                 "the camera. (point at the anatomy diagram, walk the class "
                 "around it) What's on it: this is the camera — its eye. This "
                 "is the microphone — its ear. These two little buttons — "
                 "reset and boot; you'll use them when flashing. And here: a "
                 "tiny LED, an SD card slot, the charging port. Don't memorize "
                 "all of it — just recognize the eye and the two little "
                 "buttons. The most special thing: AI lives inside the board. "
                 "Once the trained model is loaded in, it recognizes your "
                 "gestures with no internet at all. Students pass a XIAO "
                 "around; find the camera and the two buttons on the anatomy "
                 "diagram. [Assets: XIAO thumb-size photo + anatomy diagram — "
                 "line-art placeholder until re-crop from the V3 deck]")

    # ---------------------------------------------------------------- 05 pros/cons
    s = page(prs, 5)
    add_title_bar(s, "Three Pros, Three Cons")
    add_subtitle(s, "you'll hit them all today", y=1.00, size=14)
    yellow_box(s, 0.62, 1.45, 4.30, 2.65, [
        "SMALL — thumb-size, fits anywhere",
        "CHEAP — about the price of a lunch",
        "AI RUNS ON THE BOARD — no internet; your photos never leave this "
        "little board"], title="PROS", size=12)
    add_card(s, 5.08, 1.45, 4.30, 2.65, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.26, 1.57, 3.94, 0.32, "CONS", size=15, bold=True)
    add_multiline(s, 5.26, 1.93, 3.94, 2.05, [
        ("SMALL COMPUTING POWER — it 'thinks' half a second slower; normal",
         {"size": 12}),
        ("IT MAKES MISTAKES — 'what to do when it can't recognize' is part "
         "of your design", {"size": 12}),
        ("NO SCREEN — it talks through lights, buzzers, or the computer",
         {"size": 12}),
    ], line_spacing=1.25)
    add_grey_box(s, 0.62, 4.35, 8.76, 0.60, "Small computer, small jobs.",
                 size=16)
    set_notes(s, "Three pros. One: it's small. Two: it's cheap — about the "
                 "price of a lunch. Three: the AI runs on the board — no "
                 "internet needed, and your photos never leave this little "
                 "board. Three cons — and you'll hit all of them today. One: "
                 "small computing power — it 'thinks' about half a second "
                 "slower; normal. Two: it makes mistakes — 'what to do when "
                 "it can't recognize' is part of your design. Three: no screen "
                 "— it talks through lights, buzzers, or the computer. Remember "
                 "one line: small computer, small jobs. 'How is this different "
                 "from photo recognition on my phone?' — the phone sends the "
                 "photo to a faraway computer to recognize it. This board "
                 "recognizes it on itself — slower, but no internet, and it "
                 "doesn't hand your photos to anyone. 'No screen is weak' — "
                 "right, that's why it usually teams up with the Wio: one "
                 "sees, one shows. Today, lights and buzzers speak for it.")

    # ---------------------------------------------------------------- 06 tool
    s = page(prs, 6)
    add_title_bar(s, "Today's Tool + the Sign-In Demo")
    add_grey_box(s, 0.62, 1.35, 4.20, 0.60, "sensecraft.seeed.cc/ai", size=15)
    add_text(s, 0.62, 2.10, 4.20, 0.60,
             "don't write it down; the tabs are already open on every machine "
             "once the boards go out.", size=10.5, line_spacing=1.2)
    add_card(s, 5.08, 1.35, 4.30, 1.75, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 5.24, 1.50, 3.98, 0.35,
             "[ sign-in demo screenshot — camera at the badge ]", size=10,
             mono=True, align=PP_ALIGN.CENTER)
    add_text(s, 5.24, 2.05, 3.98, 0.55, "SIGNED IN", size=24, bold=True,
             align=PP_ALIGN.CENTER, color=G_GREEN)
    add_text(s, 5.24, 2.68, 3.98, 0.25, "what the board shows", size=9.5,
             align=PP_ALIGN.CENTER)
    lines = [
        "Not face-recognition — someone taught it",
        "How? By showing it lots and lots of photos",
        "Today, each of you teaches one with your own hands — your own "
        "gestures",
    ]
    ly = 3.35
    for t in lines:
        add_yellow_dot_item(s, 0.62, ly, 8.76, t, size=13)
        ly += 0.5
    add_text(s, 0.62, 4.95, 8.76, 0.24,
             "Collecting Lesson 4: Pomodoro timer record — md link or photo.",
             size=10.5)
    set_notes(s, "Here's today's weapon: sensecraft.seeed.cc/ai — don't write "
                 "it down; the tabs are already open on every machine once "
                 "the boards go out. Collecting last session's work: last "
                 "time, you took a complete project — your Pomodoro timer — "
                 "from requirements, to screens, to code, to breaking it, with "
                 "the BMAD five roles. (pick up the teacher machine; point "
                 "the camera at the badge on screen — it shows SIGNED IN; "
                 "point at something else — nothing.) How does it know the "
                 "badge? It's not face-recognizing. It's that someone taught "
                 "it. Not by writing, not by talking — by showing it lots and "
                 "lots of photos. Today, each of you teaches one with your own "
                 "hands — teaching it to recognize your own gestures. If the "
                 "demo model gets it wrong live — don't panic, that's today's "
                 "lesson: 'See? It makes mistakes too — by the end of class "
                 "you'll know why it does.' No badge — project any "
                 "high-contrast, stable image (logo / course mark / big "
                 "English word — CHAIHUO / M0). Collecting: hard 5-minute "
                 "timer; no individual feedback; note who's missing, due "
                 "before class ends. [Asset: sign-in demo screenshot — "
                 "placeholder card until rehearsal capture]")

    # ---------------------------------------------------------------- 07 blink
    s = page(prs, 7)
    add_title_bar(s, "Experience 1 — The AI Blink")
    add_subtitle(s, "use a model someone else taught", y=1.00, size=13)
    steps = [
        ("1", "Assemble & connect — cable pushed all the way in; 'connect "
              "device', see your board's name"),
        ("2", "Pick FACE DETECTION in SenseCraft → click DEPLOY — the model "
              "travels down the cable into the board"),
        ("3", "Give it a trigger: FACE DETECTED → TURN ON THE ONBOARD LED — "
              "point at it, it lights up"),
    ]
    sy = 1.45
    for num, txt in steps:
        num_block(s, 0.62, sy, num, size=0.4)
        add_text(s, 1.2, sy - 0.02, 7.9, 0.55, txt, size=12,
                 line_spacing=1.2)
        sy += 0.62
    add_card(s, 0.62, 3.35, 8.76, 0.62, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 3.35, 6.9, 0.62,
             "[ LIVE DEMO — point at the teacher's face: LED on · point at "
             "something else: off ]", size=11, mono=True,
             anchor=MSO_ANCHOR.MIDDLE)
    add_oval(s, 7.95, 3.57, 0.18, fill=G_GREEN, border=None)
    add_oval(s, 8.45, 3.57, 0.18, fill=G_RED, border=None)
    yellow_box(s, 0.62, 4.15, 8.76, 0.80, [
        "Congratulations — you just deployed an AI-driven automation system.",
        "Not one line of code. The vision model drives the peripheral "
        "directly."], size=12.5)
    add_text(s, 0.62, 5.02, 8.76, 0.2,
             "The demo recognizes the teacher's face or an on-screen photo — "
             "nobody photographs anyone's face.", size=9.5)
    set_notes(s, "Boards out. Assemble and plug in first — both ends of the "
                 "cable pushed all the way in. Connect to the computer, click "
                 "'connect device', see your board's name. Once connected, "
                 "don't rush to photograph. First, load a model someone else "
                 "already taught into the board. In SenseCraft, pick face "
                 "detection, click 'deploy' — it travels down the cable into "
                 "the board. Now give it a 'trigger': face detected → turn on "
                 "the onboard LED. Watch the LED's spot — point at my face — "
                 "on! Congratulations — you just deployed an AI-driven "
                 "automation system. And watch this: add the Grove expansion "
                 "board, plug in a light strip — target recognized, the strip "
                 "lights up directly. Not one line of code. The vision model "
                 "drives the peripheral directly. That's 'recognized → "
                 "moves'. You'll build one of these yourselves in the second "
                 "half. This is the class's #1 failure-prone block: all three "
                 "TAs push in. One student can't connect in 3 minutes — swap "
                 "board, swap cable, don't linger (swap, don't repair). Login "
                 "fails — TA A hands over a spare account on the spot. "
                 "Black/blurry image — first question 'is the lens film "
                 "off?', second move swap the board. Compliance: face "
                 "detection recognizes only the teacher's own face or the "
                 "on-screen photo — students don't photograph each other's "
                 "faces. State the rule now: 'When you collect your own data "
                 "later — hands and objects only. No faces.' Short on time — "
                 "trigger config becomes a teacher demo; students only get "
                 "'deployed + recognized.' Output anchor: every board runs a "
                 "ready-made model — recognized target lights the onboard "
                 "LED. [Asset: AI Blink trigger-config screenshot — live demo "
                 "is primary]")

    # ---------------------------------------------------------------- 08 collect (RED 1)
    s = page(prs, 8)
    add_title_bar(s, "Experience 2 — Collect Data")
    add_subtitle(s, "25 to 30 photos per gesture · hands only", y=1.00,
                 size=13)
    add_yellow_dot_item(s, 0.62, 1.45, 8.76,
                        "Hand straight on — then further away, different "
                        "angle, other hand", size=13)
    add_multiline(s, 0.78, 2.00, 8.6, 0.62, [
        ("For every photo, give the gesture its \"answer name\" — the formal "
         "word is a LABEL:", {"size": 12, "bold": True}),
        ("the standard answer for each photo. When it learns, it's checking "
         "its answers.", {"size": 12}),
    ], line_spacing=1.25)
    add_text(s, 0.62, 2.82, 8.76, 0.24, "CLASS NAMES — English only",
             size=10.5, bold=True)
    add_card(s, 0.62, 3.10, 4.30, 0.62, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.62, 3.10, 4.30, 0.62, "scissors · rock · paper", size=22,
             bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_rect(s, 0.62, 3.98, 0.07, 0.85, fill=RED, border=None)
    add_oval(s, 0.86, 4.08, 0.12, fill=RED, border=None)
    add_text(s, 1.12, 4.02, 8.26, 0.30,
             "HANDS AND OBJECTS ONLY — NO FACES.", size=15, bold=True,
             color=RED)
    add_text(s, 1.12, 4.40, 8.26, 0.28,
             "Not yours, not anyone's. If a face sneaks in — delete it on "
             "the spot.", size=11.5)
    add_text(s, 0.62, 4.98, 8.76, 0.24,
             "Write in your workbook — the data collection record: how many "
             "per class, what angles / lighting.", size=10.5)
    set_notes(s, "Now — teach it your gestures: scissors, rock, paper. For "
                 "each one, take 25 to 30 photos with your board. (teacher "
                 "demonstrates, on screen) Watch me — this one, hand straight "
                 "on. Next, further away. Another, different angle. Another, "
                 "other hand. — For every photo, give the gesture its 'answer "
                 "name': this is 'rock', this is 'scissors'. That answer name "
                 "has a formal word — a label. It's the standard answer for "
                 "each photo. When it learns, it's checking its answers. "
                 "(deliberately demonstrate bad data, don't explain yet) Now a "
                 "few more — background switched to the window, half a hand, "
                 "ten shots all at the same angle. Done. Are these photos "
                 "good? Not saying yet. We'll see. Rule repeated: hands and "
                 "objects only — no faces. Not yours, not anyone's. If a "
                 "face sneaks in, delete it on the spot. Chaotic collection "
                 "(unsure how many / wrong labels) — TA circulation, three "
                 "questions: 'How many do you have?' 'Label correct?' "
                 "'Changed the angle?' A student wants to train after only "
                 "10 — let them! Don't say a word — when it fails later, it's "
                 "the teaching material (designed contrast). A face gets "
                 "photographed — TA C watches it get deleted, restates the "
                 "rule once, no scolding. Output anchor: everyone's "
                 "three-class photo dataset (in the workbook's 'data "
                 "collection record' zone).")

    # ---------------------------------------------------------------- 09 train
    s = page(prs, 9)
    add_title_bar(s, "Train + Deploy")
    add_subtitle(s, "you're the teacher, it's the student", y=1.00, size=13)
    flow = [
        (0.62, "100+ PHOTOS", None),
        (3.64, "click TRAIN", "it finds the common ground, stores it as an "
                              "EXPERIENCE BOOK"),
        (6.66, "click DEPLOY", "the experience book travels down the USB "
                               "cable into the board"),
    ]
    for fx, head, body in flow:
        add_card(s, fx, 1.40, 2.72, 1.30, fill=WHITE, border=INK,
                 border_w=1.5)
        if body:
            add_multiline(s, fx + 0.15, 1.50, 2.42, 1.10, [
                (head, {"size": 13, "bold": True}),
                (body, {"size": 10.5}),
            ], line_spacing=1.2)
        else:
            add_text(s, fx, 1.40, 2.72, 1.30, head, size=15, bold=True,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, 3.36, 1.75, 0.28, 0.6, "→", size=20, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, 6.38, 1.75, 0.28, 0.6, "→", size=20, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_grey_box(s, 0.62, 2.95, 8.76, 1.00,
                 "Training = it turns your photos into \"experience\": what do "
                 "rock photos have in common, what do scissors photos have "
                 "in common. Unplug the cable — it still remembers.",
                 size=12)
    add_multiline(s, 0.62, 4.15, 8.76, 0.62, [
        ("Training queues — whoever collected first trains first.",
         {"size": 11, "bold": True}),
        ("While you wait: what kind of student would my weird photos "
         "produce?", {"size": 11}),
    ], line_spacing=1.3)
    set_notes(s, "Collected enough? Click 'train'. What's it doing? "
                 "Plain-English version: it's turning your hundred-plus "
                 "photos into 'experience' — what do rock photos have in "
                 "common, what do scissors photos have in common; it figures "
                 "that out itself and stores it as an experience book. That "
                 "process is called training — you're the teacher, it's the "
                 "student. (during the wait) Training queues — whoever "
                 "collected first trains first. While you wait, think: what "
                 "kind of student would my weird photos from earlier produce? "
                 "Trained? Click 'deploy' — the experience book travels down "
                 "the USB cable into your board. Once it's in, it remembers "
                 "— unplug the cable, still remembers. Now — show your board "
                 "a scissors. See if it recognizes its teacher. Queue jam — "
                 "TA A batches (collectors first); anyone waiting over 5 "
                 "minutes goes to the board and sticks a 'when I predict it "
                 "will get it wrong' sticky (warms up the attribution talk). "
                 "Platform slow — run the two-track 'batch + teacher rescue "
                 "model': anyone who can't finish trains deploys the "
                 "teacher's pretrained model, keeps their data, retrains "
                 "after class (rescue only). A student recognizes nothing — "
                 "check 'did it deploy?' first, then data size — odds are "
                 "it's the 10-photo student; keep them as discussion "
                 "material. Output anchor: self-trained model deployed on "
                 "the board; record in md or handwriting (how many classes, "
                 "how many photos each, how long the wait). [Asset: "
                 "training/deploy interface screenshot — optional, live demo "
                 "is primary]")

    # ---------------------------------------------------------------- 10 swap
    s = page(prs, 10)
    add_title_bar(s, "The Swap Test")
    add_subtitle(s, "does it know your neighbor's hand?", y=1.00, size=13)
    rules = [
        "Only scissors-rock-paper — and vary it: further, faster, other hand",
        "Recognized = 1 point",
        "Got it wrong = ... write it down too. That's treasure.",
        "We'll tally the class failure rate in a minute.",
    ]
    ry = 1.45
    for t in rules:
        add_yellow_dot_item(s, 0.62, ry, 8.76, t, size=14)
        ry += 0.58
    add_grey_box(s, 0.62, 3.85, 8.76, 0.75,
                 "\"Breaking\" is limited to showing it things — no touching "
                 "hardware, no covering the lens, no pulling cables.",
                 size=12)
    yellow_box(s, 0.62, 4.75, 8.76, 0.50, [
        "Write in your workbook — under which move did your neighbor's model "
        "fail?"], size=12.5)
    set_notes(s, "Now the fun part: swap boards with your neighbor. Your "
                 "model — does it recognize their hand? Rules: only "
                 "scissors-rock-paper, and vary it — further, faster, other "
                 "hand. Recognized = 1 point. Got it wrong = ... write it "
                 "down too. That's treasure. We'll tally the class failure "
                 "rate in a minute. Widespread failure is designed, not an "
                 "accident — the teacher never 'rescues': only 'Write it down "
                 "— under which move did your model fail?' Rare class with "
                 "too-high accuracy — the teacher becomes the trap: gloved "
                 "hand, toy scissors, back of hand to the lens — manufacture "
                 "attribution material. The test turns into roughhousing — "
                 "boards back to owners; switch to 'test your own, in three "
                 "different lighting conditions.' Output anchor: swap-test "
                 "score + the specific failing situation noted.")

    # ---------------------------------------------------------------- 11 attribution
    s = page(prs, 11)
    add_title_bar(s, "The Attribution")
    add_subtitle(s, "it's not dumb — you taught it too little", y=1.00,
                 size=13)
    add_text(s, 0.62, 1.42, 8.76, 0.26,
             "Failure-rate tally — hands up if your model got it wrong more "
             "than 3 times.", size=12)
    add_text(s, 0.62, 1.80, 8.76, 0.62, "IT'S NOT DUMB.", size=40, bold=True)
    add_text(s, 0.62, 2.42, 8.76, 0.62, "YOU TAUGHT IT TOO LITTLE.", size=40,
             bold=True)
    add_rect(s, 0.62, 3.10, 2.2, 0.06, fill=YELLOW, border=None)
    add_text(s, 0.62, 3.28, 8.76, 0.30,
             "Want it smarter? Feed it more — and more different — examples.",
             size=15, bold=True)
    add_grey_box(s, 0.62, 3.72, 8.76, 0.72,
                 "For an AI that recognizes things, the examples ARE "
                 "everything. Telling it isn't enough. You have to show it.",
                 size=13)
    yellow_box(s, 0.62, 4.55, 8.76, 0.62, [
        "One sticky per person: \"my model gets it wrong when ___\" — "
        "specific beats vague:",
        "'low light' passes; 'it's not accurate' doesn't. Stick it on the "
        "left side of the board."], size=11.5)
    set_notes(s, "Failure-rate tally — hands up if your model got it wrong "
                 "more than 3 times. (a sea of hands) Congratulations. You "
                 "just earned today's most important textbook. One sticky per "
                 "person: write when your model gets it wrong — the more "
                 "specific the better. 'Low light' passes. 'It's not "
                 "accurate' doesn't. Stick it on the left side of the board. "
                 "(read the stickies, group them) Light changed, background "
                 "changed, someone else's hand, only a dozen photos… see the "
                 "pattern? It's not dumb. You taught it too little. Want it "
                 "smarter? Feed it more, more different examples. Remember my "
                 "weird photos from before class — one angle only, messy "
                 "background? A student taught by that teacher only knows how "
                 "to sit in the front row. One loop back: you've learned that "
                 "talking to AI needs examples. Today you saw it — for an AI "
                 "that recognizes things, the examples ARE everything. "
                 "Telling it isn't enough. You have to show it. If it goes "
                 "cold — call on someone who raised their hand: 'Which move "
                 "got it wrong for you?' Two or three of those warms it up. A "
                 "student writes 'the board is dumb' — throw it back to the "
                 "class: 'Same board — why did it recognize YOUR rock?' — let "
                 "them answer 'the data.' Output anchor: the attribution "
                 "sticky up on the board + one line in the log.")

    # ---------------------------------------------------------------- 12 log
    s = page(prs, 12)
    add_title_bar(s, "First-Half Log — Four Lines, As Usual")
    log_items = [
        (1.40, "Today I made ___",
         "today: I trained a model that recognizes rock-paper-scissors"),
        (2.10, "I got stuck at ___",
         "required today: WHEN DOES MY MODEL GET IT WRONG?"),
        (2.80, "Then ___", None),
        (3.25, "Next time I want ___",
         "e.g. feed it more data / change the angles"),
    ]
    for ly_, main, hint in log_items:
        add_yellow_dot_item(s, 0.62, ly_, 8.76, main, size=14, bold=True)
        if hint:
            add_text(s, 0.78, ly_ + 0.30, 8.6, 0.26, f"({hint})", size=10.5)
    yellow_box(s, 0.62, 4.15, 8.76, 0.90, [
        "Photograph your board — hands and board only.",
        "Leave the model on the board — second half, it does something after "
        "it recognizes."], size=12.5)
    set_notes(s, "Log time — four lines as usual. For 'did', write: I trained "
                 "a model that recognizes rock-paper-scissors. 'Stuck at' is "
                 "required today: when does my model get it wrong. Leave the "
                 "model on the board — second half, it does something after "
                 "it recognizes. Output anchor: the four-line log in the "
                 "workbook (md or handwriting).")

    # ---------------------------------------------------------------- 13 sensor output
    s = page(prs, 13)
    add_title_bar(s, "Sensor Output — Where Does the Result Go?")
    add_text(s, 0.62, 1.14, 8.76, 0.28,
             "A deployed XIAO is a VISION AI SENSOR —", size=13.5, bold=True)
    add_text(s, 0.62, 1.46, 8.76, 0.28,
             "like the light sensor and buttons you've used — except what "
             "it \"senses\" is a picture.", size=12)
    add_card(s, 0.62, 1.95, 4.32, 1.00, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.78, 2.03, 2.70, 0.26, "UART — the serial port", size=12.5,
             bold=True)
    add_text(s, 0.78, 2.32, 3.98, 0.55,
             "when it's connected to a computer, the recognition results you "
             "see on screen travel over it", size=10.5, line_spacing=1.15)
    add_rect(s, 3.86, 2.03, 0.98, 0.24, fill=YELLOW, border=None)
    add_text(s, 3.86, 2.05, 0.98, 0.20, "TODAY'S ONE", size=8, bold=True,
             align=PP_ALIGN.CENTER)
    add_card(s, 5.04, 1.95, 4.32, 1.00, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 5.20, 2.03, 4.00, 0.85, [
        ("I2C", {"size": 12.5, "bold": True}),
        ("boards talking to boards", {"size": 10.5}),
    ], line_spacing=1.2)
    add_card(s, 0.62, 3.05, 4.32, 1.00, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.78, 3.13, 4.00, 0.85, [
        ("SPI", {"size": 12.5, "bold": True}),
        ("the same idea, a few jumper wires: \"eyes\" and \"hands\" split "
         "apart", {"size": 10.5}),
    ], line_spacing=1.2)
    add_card(s, 5.04, 3.05, 4.32, 1.00, fill=CODEBG, border=INK, border_w=1.5)
    add_multiline(s, 5.20, 3.13, 4.00, 0.85, [
        ("WiFi/MQTT", {"size": 12.5, "bold": True}),
        ("the networking lessons, later", {"size": 10.5}),
    ], line_spacing=1.2)
    add_grey_box(s, 0.62, 4.25, 8.76, 0.85,
                 "recognized → output → something else catches it and does "
                 "the work. The build in a minute is making that output "
                 "light your LED and ring your buzzer.", size=12.5)
    set_notes(s, "First half done. Your board is no longer an ordinary board "
                 "— a deployed XIAO is a vision AI sensor. Just like the "
                 "light sensor and the buttons you've used — except what it "
                 "'senses' is a picture. Once a sensor recognizes something, "
                 "the result needs an exit. It speaks several 'languages': "
                 "UART — the serial port; when it's connected to a computer, "
                 "the recognition results you see on screen travel over it. "
                 "I2C and SPI — for boards talking to boards. WiFi/MQTT — we "
                 "play with that in the networking lessons, later. Look — "
                 "two boards joined by I2C: this one watches, that one "
                 "works. SPI's the same idea — a few jumper wires, and the "
                 "'eyes' and the 'hands' split apart. We don't run two boards "
                 "today — but hold onto this feeling: recognized → output → "
                 "something else catches it and does the work. The build in a "
                 "minute is making that output light your LED and ring your "
                 "buzzer. 'What's the difference between I2C and SPI?' — "
                 "both are ways boards talk to each other — you don't need "
                 "to tell them apart today. Remember UART — the serial port "
                 "— that's what we use in a minute. Pure cognition, no "
                 "hands-on; a student itching to wire — 'Note it down. "
                 "Today's output runs through the serial port; two-board "
                 "play is a later lesson.' [Asset: serial-port output "
                 "screenshot — optional, live demo is primary]")

    # ---------------------------------------------------------------- 14 brief
    s = page(prs, 14)
    add_title_bar(s, "Second-Half Brief")
    add_subtitle(s, "recognize it → make it move", y=1.00, size=14)
    add_text(s, 0.62, 1.48, 3.9, 0.6, "RECOGNIZE IT", size=30, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 4.55, 1.48, 0.9, 0.6, "→", size=30, bold=True, color=YELLOW,
             align=PP_ALIGN.CENTER)
    add_text(s, 5.48, 1.48, 3.9, 0.6, "MAKE IT MOVE", size=30, bold=True,
             align=PP_ALIGN.CENTER)
    add_card(s, 0.62, 2.40, 8.76, 0.80, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 0.80, 2.50, 8.40, 0.62, [
        ("scissors → red light on  ·  rock → buzzer beeps  ·  paper → all "
         "off", {"size": 13, "mono": True}),
        ("(that's my demo — your rules are yours to set)", {"size": 10}),
    ], line_spacing=1.25)
    yellow_box(s, 0.62, 3.35, 8.76, 0.80, [
        "MEANING-SWAP — scissors = my sister's secret signal:",
        "recognized, play the song she likes. Your model, your call."],
        size=12.5)
    add_card(s, 0.62, 4.30, 8.76, 0.62, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 4.38, 8.40, 0.48,
             "OUTPUT HARDWARE — LED + buzzer: every table's base. Servo + "
             "light strip: two per table, first-come-first-served.",
             size=11.5, line_spacing=1.2)
    add_text(s, 0.62, 5.00, 8.76, 0.20,
             "It \"thinks\" half a second slower — normal. Today: it watches, "
             "and takes care of this one thing.", size=9.5)
    set_notes(s, "Second-half brief, one sentence: recognize it → make it "
                 "move. Scissors → red light on. Rock → buzzer beeps. Paper → "
                 "all off. That's my demo — your rules are yours to set. "
                 "Change the meaning if you want: scissors = my sister's "
                 "secret signal — recognized, play the song she likes. Your "
                 "model, your call. (hand out output hardware) Every table "
                 "gets LED and buzzer as base pieces. Servo and light strip: "
                 "only two per table, first-come-first-served. Didn't grab "
                 "one? Don't sweat it — making the light and the buzzer do "
                 "something interesting is just as much of a skill. Set "
                 "expectations now: it 'thinks' on a thumbnail-sized board — "
                 "half a second of lag is normal. Making it fast and smart "
                 "enough to run a building is a later lesson. Today: it "
                 "watches, and takes care of this one thing. 'I want it to "
                 "recognize my Gundam model and fire!' — great idea — put it "
                 "on the 'later' list. Today, use what your board already "
                 "knows — rock-paper-scissors. That recognition step already "
                 "won; don't re-fight it. Actuator argument — "
                 "first-come-first-served + the agreement 'if nobody's using "
                 "it after 16:20, it rotates.'")

    # ---------------------------------------------------------------- 15 three-box (RED 2)
    s = page(prs, 15)
    add_title_bar(s, "Three-Box Sheet — One New Member Today")
    boxes = [
        (0.62, "SENSE", "the class the camera recognizes (scissors / rock / "
                        "paper)"),
        (3.58, "LOGIC", "recognized what, do what"),
        (6.54, "OUTPUT", "the light, the buzzer, or the servo you grabbed"),
    ]
    for bx, head, body in boxes:
        add_card(s, bx, 1.30, 2.84, 1.05, fill=WHITE, border=INK,
                 border_w=1.5)
        add_text(s, bx, 1.40, 2.84, 0.30, head, size=14, bold=True,
                 align=PP_ALIGN.CENTER)
        add_text(s, bx + 0.15, 1.74, 2.54, 0.55, body, size=10.5,
                 align=PP_ALIGN.CENTER, line_spacing=1.15)
    add_rect(s, 4.99, 2.35, 0.02, 0.38, fill=INK, border=None)
    add_rect(s, 2.20, 2.73, 0.07, 1.18, fill=RED, border=None)
    add_oval(s, 2.44, 2.85, 0.12, fill=RED, border=None)
    add_text(s, 2.70, 2.80, 6.6, 0.30,
             "WHAT IF IT CAN'T RECOGNIZE IT — OR ISN'T SURE?", size=16,
             bold=True, color=RED)
    add_multiline(s, 2.70, 3.18, 6.6, 0.62, [
        ("THIS COLUMN IS REQUIRED. Writing \"do nothing\" is a valid "
         "answer —", {"size": 12}),
        ("but it has to be YOUR decision, not its accident.",
         {"size": 12}),
    ], line_spacing=1.2)
    add_grey_box(s, 0.62, 4.15, 8.76, 1.00,
                 "It reports how confident it is — a percentage (its "
                 "CONFIDENCE).\nYour rule: below 70% confidence, treat it as "
                 "not recognized.\nShow a TA your three boxes before you "
                 "build.", size=11.5)
    set_notes(s, "Before building — the usual three-box sheet: sense, logic, "
                 "output. Today's three boxes have a new member. Sense: the "
                 "class the camera recognizes (scissors / rock / paper). "
                 "Logic: recognized what, do what. Output: the light, the "
                 "buzzer, or the servo you grabbed. The new member lives in "
                 "the logic box, one more column: 'What if it can't recognize "
                 "it — or isn't sure?' Earlier projects never had this "
                 "situation — a button is either pressed or not. But 'seeing' "
                 "hesitates: it might say 'I'm not sure if that's scissors or "
                 "paper.' This column must be filled. Writing 'do nothing' is "
                 "a valid answer — but it has to be your decision, not its "
                 "accident. The 'can't recognize' column left blank — send it "
                 "back: 'That column is today's required question.' 'How sure "
                 "is sure?' — good question, one line: every time, it reports "
                 "how confident it is — a percentage. That number is its "
                 "confidence. Your rule: below 70% confidence, treat it as "
                 "not recognized. Output anchor: the three-box sheet (vision "
                 "edition), with the 'can't recognize' column filled; shown "
                 "to a TA before building.")

    # ---------------------------------------------------------------- 16 prompt
    s = page(prs, 16)
    add_title_bar(s, "Vision → Action — You're the Boss of Two AIs")
    add_rect(s, 0.62, 0.98, 8.76, 0.44, fill=YELLOW, border=None)
    add_text(s, 0.80, 1.05, 8.40, 0.30,
             "The model SenseCraft taught handles \"recognize\" — the "
             "program Codecraft runs handles \"do\".", size=11.5, bold=True)
    prompt_card(s, [
        "My XIAO ESP32S3 Sense has an image-classification model deployed on "
        "it",
        "that recognizes three classes: scissors, rock, paper.",
        "The recognition result and its confidence come out of the serial "
        "port.",
        "Please write me a program:",
        "1. When the result is \"scissors\" AND confidence is above 70% → "
        "turn on the LED;",
        "2. When the result is \"rock\" AND confidence is above 70% → make "
        "the buzzer beep once;",
        "3. When the result is \"paper\", or confidence is below 70% → turn "
        "everything off",
        "   (this is the \"what if it can't recognize it\" handling).",
        "Implement only item 1 first. Once it runs, I'll ask for items 2 and "
        "3.",
    ], y=1.52, h=2.78, size=10.5)
    add_rect(s, 0.62, 4.42, 0.07, 0.75, fill=YELLOW, border=None)
    add_multiline(s, 0.90, 4.46, 8.30, 0.68, [
        ("The old discipline: one thing at a time. Item 1 running, then "
         "items 2 and 3.", {"size": 10, "bold": True}),
        ("Error? Paste the error back — it fixes it.", {"size": 10}),
        ("Left tab: SenseCraft. Right tab: Codecraft. Don't merge them. "
         "Class names stay English.", {"size": 10}),
    ], line_spacing=1.25)
    set_notes(s, "Watch how I plug the 'recognition result' into a "
                 "conversation. Note this prompt — you're now the boss of "
                 "two AIs: the one SenseCraft taught handles 'recognize', the "
                 "one Codecraft runs handles 'do'. (type on screen, read it "
                 "line by line — or point at this page) See — the old "
                 "discipline: one thing at a time. Get 'scissors → light on' "
                 "running first, then rock, then paper. In 30 minutes I'll "
                 "call across the room and check your three-box sheets. "
                 "'It's slow / doesn't work' — point back to the "
                 "expectation-setting: 'Half a second of lag is normal. "
                 "Actually wrong? Think back to the first half — what makes "
                 "it wrong? Write that situation down — it's the first item "
                 "on next lesson's trouble list.' After moving / changing "
                 "light, everything fails — teach on the spot: 'This is a "
                 "scenario the data never saw. Quick rescue: back to "
                 "SenseCraft, re-shoot 10 photos in the current light, "
                 "retrain (the change-the-data route, demo live); OR write "
                 "on your three-box sheet: this model only works at the "
                 "window desk — that's a professional answer too.' It works "
                 "but the action is too weak (a blink you barely see) — "
                 "upgrade sheet on the board: LED → RGB strip; one beep → "
                 "rhythm pattern; one servo swing → continuous waving. Lost "
                 "between the two platforms — 'Left SenseCraft, right "
                 "Codecraft. Don't merge them.' TAs correct it class-wide. At "
                 "16:31, some still have nothing running — TA B hands out the "
                 "fallback prompt (slide 17); continue from the fallback. At "
                 "16:41, everyone stops and moves to the buffer. Output "
                 "anchor: working vision-to-action project (at least 1 class "
                 "→ at least 1 action); log progress update ('did' = I made "
                 "my model ___ after recognizing ___).")

    # ---------------------------------------------------------------- 17 fallback
    s = page(prs, 17)
    add_title_bar(s, "Not Running? Start With the Board's Own LED")
    prompt_card(s, [
        "My XIAO ESP32S3 Sense has an image-classification model deployed on "
        "it",
        "that recognizes three classes: scissors, rock, paper.",
        "The recognition result comes out of the serial port.",
        "Please write me the simplest program:",
        "when the result is \"scissors\" → turn on the onboard LED.",
    ], y=1.30, h=1.75, size=11.5)
    add_card(s, 0.62, 3.25, 8.76, 1.55, fill=WHITE, border=INK, border_w=1.5)
    err_items = [
        (3.40, "Error? Paste the error back to AI, verbatim.", True),
        (3.90, "Image black or blurry? Is the lens film off? → swap the "
               "board, don't repair.", False),
        (4.40, "Once the fallback runs, extend from there — add the light, "
               "the buzzer, the servo.", False),
    ]
    for ey_, txt, bold_ in err_items:
        add_yellow_dot_item(s, 0.80, ey_, 8.4, txt, size=12.5, bold=bold_)
    set_notes(s, "Used at the 16:31 check: 'Not running yet — raise your "
                 "hand. TA, start with the fallback prompt. Running? Keep "
                 "going — extend rock and paper, or upgrade your output.' The "
                 "fallback does only the onboard LED — no extra wiring: first "
                 "build confidence, then add the light and buzzer. Output "
                 "anchor: the fallback version running (one class → onboard "
                 "LED).")

    # ---------------------------------------------------------------- 18 buffer
    s = page(prs, 18)
    add_text(s, 0.62, 0.95, 3.0, 1.80, "9", size=96, bold=True,
             align=PP_ALIGN.CENTER)
    add_text(s, 0.62, 2.78, 3.0, 0.5, "minutes", size=26, bold=True,
             align=PP_ALIGN.CENTER)
    yellow_box(s, 3.90, 1.05, 5.48, 0.95, [
        "EXIT 1 · FINISH TO STANDARD (everyone crosses this line)",
        "One recognized class → one action."], size=11)
    add_card(s, 3.90, 2.12, 5.48, 1.00, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 4.06, 2.22, 5.16, 0.82, [
        ("EXIT 2 · RUNNING? Try your neighbor's project once.",
         {"size": 11, "bold": True}),
        ("Then log progress: \"I made my model ___ after recognizing ___.\"",
         {"size": 10.5}),
    ], line_spacing=1.25)
    add_card(s, 3.90, 3.24, 5.48, 1.10, fill=WHITE, border=INK, border_w=1.5)
    add_multiline(s, 4.06, 3.34, 5.16, 0.92, [
        ("EXIT 3 · SPARE TIME? On the back of your three-box sheet,",
         {"size": 11, "bold": True}),
        ("write \"three scenarios where I'll try to break my own project "
         "next lesson.\"", {"size": 10.5}),
    ], line_spacing=1.25)
    add_multiline(s, 0.62, 4.55, 8.76, 0.55, [
        ("Not finished? No extensions — TA keeps you on the main build.",
         {"size": 10, "bold": True}),
        ("The buffer is part of the lesson, not early dismissal.",
         {"size": 10}),
    ], line_spacing=1.3)
    set_notes(s, "The buffer is not free time. Not running yet: TA B "
                 "concentrates on getting them to 'one class → one action' "
                 "(the acceptance floor). Running: (1) try your neighbor's "
                 "project once; (2) log progress; (3) spare time: the "
                 "'three scenarios' line on the back of the three-box sheet. "
                 "The teacher: tally acceptance (running / total), fill the "
                 "reflection page sections A and B. Output anchor (running "
                 "students): the log progress line; the 'three scenarios' "
                 "note for next lesson.")

    # ---------------------------------------------------------------- 19 golden
    s = page(prs, 19)
    add_title_bar(s, "Today You Did Two Things")
    add_subtitle(s, "nobody ever walked you through", y=1.00, size=14)
    num_block(s, 0.62, 1.65, "1", size=0.4)
    add_text(s, 1.2, 1.63, 7.9, 0.32,
             "You taught a board to know the world with your own hands —",
             size=15, bold=True)
    add_text(s, 1.2, 1.98, 7.9, 0.28,
             "collecting photos, training a model, deploying it to the board",
             size=12.5)
    num_block(s, 0.62, 2.55, "2", size=0.4)
    add_text(s, 1.2, 2.53, 7.9, 0.32,
             "You made the knowing decide for you —", size=15, bold=True)
    add_text(s, 1.2, 2.88, 7.9, 0.28,
             "your gesture turns on a light, rings a buzzer", size=12.5)
    add_golden_line(s, 0.62, 3.80, 8.76,
                    "In the whole course, this is the only time you touch "
                    "\"how AI gets made.\"", size=17, h=None)
    set_notes(s, "Today you did two things nobody ever walked you through: "
                 "you taught a board to know the world with your own hands — "
                 "collecting photos, training a model, deploying it to the "
                 "board. Then you made the knowing decide for you — your "
                 "gesture makes a light turn on, a buzzer ring. In the whole "
                 "course, this is the only time you touch 'how AI gets "
                 "made.'")

    # ---------------------------------------------------------------- 20 close
    s = page(prs, 20)
    add_title_bar(s, "Next Time — Bring Your Model Back")
    preview = [
        "First, AI becomes your tester and hands you a TROUBLE LIST.",
        "Then you and your neighbor try to wreck each other's projects.",
        "Today you said \"not recognized → do nothing.\"",
        "Next time you'll answer: that decision — accept or reject?",
    ]
    py_ = 1.40
    for t in preview:
        add_yellow_dot_item(s, 0.62, py_, 8.76, t, size=13.5)
        py_ += 0.60
    add_card(s, 0.62, 3.85, 8.76, 1.32, fill=WHITE, border=INK, border_w=1.5)
    add_text(s, 0.80, 3.93, 8.4, 0.26, "PACK-UP LIST", size=12.5, bold=True)
    add_oval(s, 0.84, 4.36, 0.11, fill=YELLOW, border=None)
    add_text(s, 1.10, 4.28, 8.1, 0.26,
             "Board into the bag with your name on it · output hardware back "
             "in place", size=11)
    add_oval(s, 0.84, 4.86, 0.11, fill=YELLOW, border=None)
    add_text(s, 1.10, 4.70, 8.1, 0.44,
             "Three-box sheet + log go with you (md or handwriting — hand to "
             "the teacher after class: link or photo)", size=11,
             line_spacing=1.15)
    set_notes(s, "Next lesson preview: bring your model back. First, AI "
                 "becomes your tester and hands you a trouble list; then you "
                 "and your neighbor try to wreck each other's projects. Today "
                 "you said 'not recognized → do nothing.' Next time you'll "
                 "answer: that decision — accept or reject? Boards into the "
                 "bag with your name on it. Output hardware back in place. "
                 "Three-box sheet and log go with you (md or handwriting — "
                 "hand to the teacher after class: link or photo). 'Can I "
                 "take my model home?' — the model lives in the board, and "
                 "the board lives here. Missing it? Read your log — first "
                 "thing next lesson, we use it.")

    prs.save(OUT)
    print(f"Saved: {OUT} slides: {len(prs.slides._sldIdLst)}")


if __name__ == "__main__":
    main()
