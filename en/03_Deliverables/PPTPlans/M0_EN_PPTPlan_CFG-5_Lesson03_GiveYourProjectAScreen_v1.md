# M0 English PPT Plan ｜ CFG-5 Semester Course · Lesson 3: Give Your Project a Screen (v1)

_Wio Terminal · HMI (Human-Machine Interface) board ｜ Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) ｜ 3 hours (sample 14:00–17:00, no scheduled break) ｜ Source: CN deck plan v2 (v2.1 "no more number-reporting" update applied, `课程策划与规划/PPT策划/M0_PPT策划_CFG-5_第3课_给作品装上屏幕_v2.md`, 19 slides) + EN Teacher's Guide L03 v1 (all 🗣️ lines match) ｜ This plan is the English blueprint — every on-screen line and every script line below is final English copy. The visual system follows the Chaihuo brand spec unchanged; only text is localized. Terms locked to the EN Glossary + EN Teacher's Guide L03 (Wio Terminal / handheld / micro-experiments / the screen lesson / position-size-color / the drift gallery / the 30-minute buffer)._

> **Deck-level note (internal, never on screen)**: 19 pages in four beats plus the buffer — Meet the New Gear (01–12) → Use It Well: The Screen Lesson + Build (13–17) → The 30-Minute Buffer (18) → Wrap (19). Timings align with the EN Teacher's Guide timetable: 14:00–14:50 / 14:50–16:20 / 16:20–16:50 / 16:50–17:00. **This is the gear lesson**: the main line is meeting the Wio Terminal and using it well; the team-building content (originally part of Lesson 3) moved to Lesson 4 — this deck never shows the five-role content, only a preview line on slide 19. **The non-negotiables: the micro-experiment round (the main line of "getting to know the gear" — cut it and the lesson is gone), the screen-comparison experiment (this lesson's soul teaching point), and the standard-line wrap before the buffer.** Flexible (can compress): the walk-around talk (10 → 6 min), the free round (40 → 30 min), the drift gallery (2 cases → 1), the buffer (everyone clears the bar → start show & tell 10 minutes early). Priority discipline: if micro-experiments run over, keep button / joystick / microphone — light and accelerometer become a teacher demo — **but at least three must be sent by students' own hands**. Two mantras carry the hardware: *"slide the switch twice = telling the board 'get ready for new instructions'"* and *"no response? slide it."* The session catchphrase: **"Don't just watch me — send a line and try it yourself."** Red appears exactly once in this deck — slide 17's proofreading warning; micro-experiment "success" labels use yellow fills, not red. **Nothing Chinese ever goes on screen in the EN deck** — today's on-screen display is English / numbers / graphics by design (the board's Chinese font library is unreliable; no font roulette)._

---

## Design Principles

- **A gear lesson means pictures first**: board photos, annotated diagrams and interface screenshots beat text — students see first, understand second. Slide 05 (the walk-around) is the deck's cover-grade page: the annotated board photo carries the page, text is cut to one plain sentence per part.
- **Knowing is hands-on**: every hardware point gets a micro-experiment, and a student has only "lit it up" when they've sent the line themselves. Slides 08–12 are one page per hardware point — big instruction + big success screenshot + one closing line. The round's rhythm must not collapse: one experiment stuck over 2 minutes is too long.
- **Inputs do things, they don't report numbers** (the v2.1 update): every micro-experiment is a mini toy with an image/sound/game feel — the three-key piano, push the ball, blow out the candle, the board afraid of the dark, the balance ball. And every one of them IS an interface — the seed for the screen lesson ahead (at the comparison, point back: "everything we just lit up was an interface").
- **One skill owns this lesson**: describing a screen to AI with **position, size and color** (slide 13 — the soul page, a real live comparison sent twice, never faked). The "how to describe a screen" phrase extends Lesson 2's Five Rules onto this color screen: Rule 2 runs logic, today's phrase runs appearances. Land the line: *"Logic says 'do this when that happens.' Screens say 'what something is, where it sits, what it looks like.' Two ways of speaking — you need both."*
- **The five inputs carry over**: slide 12 collects the round's anchor (tick the boxes + "what surprised me most"), slide 15's free round offers all five inputs as an icon row — button, joystick, microphone, light, accelerometer.
- **The buffer has three exits**: finish to standard (everyone crosses the line) → challenge tasks (electronic dice / balance-ball hole-in-one, rehearsed ones only) → help a neighbor + add a sensor link. **Standard first, then fast** — the buffer is part of the lesson, not early dismissal.
- **Output anchors everywhere**: slides 02 / 06 / 12 / 15 / 17 / 18 each carry a 📝 "write it in your workbook (or notebook)" action box.
- **Stand-still pages**: during hands-on time the projected page stays fixed — the screen is the students' working reference, not the instructor's teleprompter. Stand-still pages: 08–12 (micro-experiments), 14 (follow-along), 15 (free round), 18 (buffer).
- **Zero print**: the micro-experiment lines and the screen phrase are NOT handed out — they live in the Student Workbook; project and read together when they debut, point students to the book when they forget.

### Colors / Type / Icons / Layout

Chaihuo brand spec (`chaihuo-ppt-brand.md`): white 70 / yellow F3D230 15 / black 10 / red D84144 5; no gradients, no shadows, no complex illustrations; 2 px black-stroke line icons; Source Han Sans; 16:9 (960×540 px); title zone 100 px top, content 110–490 px, footer 40 px. **Red appears exactly once in this deck — slide 17's proofreading warning** (one red element, strictly capped). Micro-experiment "success" labels use yellow fills, not red. Slide 05's annotation leaders and dots must stay line-style (2 px black stroke, yellow as accent only) — it is the deck's densest label page but never an illustration page. Script/quote boxes: the one permitted fifth color — light grey `#F5F5F5` fill + 1 px black border + monospace 14–16 pt.

### On-Screen Text Rules

- All on-screen text is final English copy (below, verbatim). Digits for all numbers.
- Student-typed prompt lines are shown in monospace boxes; the part students must swap in is marked with an underline `___`.
- **Today's on-screen display is English / numbers / graphics by design** — the Wio's Chinese font library is unreliable. If garbled glyphs still appear, tell AI *"change all on-screen text to English"* — don't debug the font library.
- During hands-on segments the page stays fixed; instructors read from the Teacher's Guide, not from the slide.

---

## Slide Map

| # | On-screen title | Type | Beat | Time |
| --- | --- | --- | --- | --- |
| 01 | Give Your Project a Screen | Title page | Cover | Loops before class |
| **Part 1 · Meet the New Gear (14:00–14:50, 11 slides)** | | | | |
| 02 | First, Let's Collect Last Session's Work | Interaction page | Frame | 8 min |
| 03 | New Gear: From Board to Handheld | Demo guide page | Handover | 5 min |
| 04 | Switch the Board Type — Same Old Flow, Same Old Line | Demo guide page | Warm-up | 5 min |
| 05 | Walk Around — Meet Your New Partner | Core concept (cover-grade annotated board) | Tool | 7 min |
| 06 | Why New Gear? Your Project Has a Face and Hands | Core concept (compare) | Tool | 3 min |
| 07 | Touching Isn't Knowing — Lighting It Up Is | Operation page (fast flip) | Turn | 2 min |
| 08 | Micro-Experiment 1/5 · Buttons — The Three-Key Piano | Operation page (big picture, stand-still) | Hands-on | 4 min |
| 09 | Micro-Experiment 2/5 · Joystick — Push the Ball | Operation page (big picture, stand-still) | Hands-on | 4 min |
| 10 | Micro-Experiment 3/5 · Microphone — Blow Out the Candle | Operation page (big picture, stand-still) | Hands-on | 4 min |
| 11 | Micro-Experiment 4/5 · Light — The Board Afraid of the Dark | Operation page (big picture, stand-still) | Hands-on | 4 min |
| 12 | Micro-Experiment 5/5 · Accelerometer — The Balance Ball | Operation page (big picture, stand-still) | Hands-on | 4 min |
| **Part 2 · Use It Well: The Screen Lesson + Build (14:50–16:20, 5 slides)** | | | | |
| 13 | One Idea, Two Ways of Saying It | Demo guide page — **the soul of the lesson** | Skill | 10 min |
| 14 | Follow-Along: The Button Counter — Two Steps on Purpose | Operation page (stand-still) | Do | 20 min |
| 15 | Free Round: Make Something With Two Screens | Task page (stand-still) | Do | 40 min |
| 16 | Whole Room — Come Look at a Treasure | Interaction page | Reflect | 10 min |
| 17 | Three Takeaways for Using It Well + Your AI Log | Operation page | Log — **red** | 10 min |
| **The 30-Minute Buffer (16:20–16:50, 1 slide)** | | | | |
| 18 | 30 Minutes — Standard First, Then Fast | Task page (big-type, stand-still) | Buffer | 30 min |
| **Wrap (16:50–17:00, 1 slide)** | | | | |
| 19 | Flash Show & Tell + Next Time | Call-to-action | Close | 10 min |

> 19 pages, ~180 minutes (includes stand-still time), matches the 3-hour session (±10%). **The three non-negotiables: the micro-experiment round (08–12), the screen-comparison experiment (13), and the standard-line wrap before the buffer (the buffer gate inside 18).**

---

## Slide by Slide

### Slide 01 | Give Your Project a Screen — Title page

**Type**: Title · **Time**: loops before class

**On screen** (verbatim):

```text
Give Your Project a Screen

Wio Terminal · HMI (Human-Machine Interface) board · Chaihuo Maker Academy · M0 Lesson 3

From today, your builds have a real interface.
```

**Instructor notes**: open with one welcome line and go straight to slide 02 — the cover is not a talking page. Wio Terminal photo on the right (screen lit, 45° angle), yellow rule under the subtitle. Footer: `Chaihuo Maker Academy · M0 · Give Your Project a Screen | 03 / 19`.

**Assets**: IMG Wio Terminal handheld photo (`L3_Wio掌机实拍.png`, screen lit).

---

### Slide 02 | First, Let's Collect Last Session's Work — Interaction page

**Type**: Interaction · **Time**: 8 min (collection hard-timeboxed at 5 min)

**On screen** (verbatim):

```text
First, Let's Collect Last Session's Work

① Hand in your work — online doc? send the link.
   Handwritten? send a photo. Not in yet? Note it down — finish before you leave today.
② Look at the Project Wall — everyone's manifesto is up there.
   It's the north star for every big project after this.

(small) Open your Student Workbook (or notebook) —
everything produced today continues in your own document.
```

**Instructor notes** (verbatim): *"Before we start, let's collect last session's work: if you used an online doc, send me the link; if you wrote by hand, send a photo — if it's not in yet, make a note of it and finish before you leave today. (point at the Project Wall) Look — last session's wall: everyone's manifesto is up there. Last time you set your topic and learned the five rules; today we hand out new gear — your project gets a real interface from today. Keep your manifesto and three-box design sheet at hand — we won't touch them today, but they're the north star for every big project after this."* Hard 5-minute timebox on the collection — no per-item feedback; the not-yet-in list goes to the TA to register, don't haggle. **Output anchor**: last session's four outputs are in (manifesto / design sheet / review & trade-off / log).

**Assets**: IMG Project Wall photo (`L3_选题墙.png`, from Lesson 2's TA shot — wall only, no faces).

---

### Slide 03 | New Gear: From Board to Handheld — Demo guide page

**Type**: Demo guide · **Time**: 5 min

**On screen** (verbatim):

```text
New Gear — From Board to Handheld
Meet the Wio Terminal: a handheld little computer

· Color screen
· Three buttons + a five-way joystick
· Sensors built in

BEFORE YOU FLASH: slide the switch on the side — slide, slide.
That tells the board: "get ready for new instructions."

(notice, yellow) No response? Slide it. — Everyone, drill it with me twice.
```

**Instructor notes** (verbatim): (hold up the Wio) *"New gear. It's called the Wio Terminal — think of it as a handheld little computer: a color screen, three buttons, a five-way joystick, and sensors built in. One thing is different from the old board: (hold it up, point at the switch) before you flash, slide the switch on the side — slide, slide — that's how you tell the board 'get ready for new instructions.' Everyone: drill it with me twice."* **The switch drill happens NOW, and the problems surface NOW** — that saves 20 minutes of rescue attempts during coding. The mantra card goes on every desk: *"No response? Slide it."*

**Assets**: IMG flash-mode switch close-up (`L3_烧录开关特写.png`, yellow circle marking the switch) · IMG Wio handheld photo (second angle, optional).

---

### Slide 04 | Switch the Board Type — Same Old Flow, Same Old Line — Demo guide page

**Type**: Demo guide · **Time**: 5 min

**On screen** (verbatim):

```text
Switch the Board Type — Same Old Flow, Same Old Line

(monospace instruction card, large)
Display in large text on the screen: HELLO and my name (pinyin or English): ___

[success screenshot: the screen showing HELLO]

(confidence anchor, yellow) New hardware — and everything you already know still works.
Nothing is wasted. And the letters are prettier now.
```

**Instructor notes** (verbatim): *"Switch the board type in Codecraft — choose Wio Terminal, same old flow. Then send the line you've known since your first lesson: 'Display in large text on the screen: HELLO and my name (pinyin or English): ___.' (wait for the room to light up) See — new hardware, and everything you already know still works. Nothing is wasted."* Why English on screen — this board's Chinese font library is unreliable; **all screen display today is English / numbers / graphics** (course-wide rule from Lesson 1). "Switching hardware costs zero learning" is today's confidence anchor — point at the color screen and add: *"and the letters are prettier now."* Serial-port problems follow the old plan: swap cable → swap machine → pair up.

**Assets**: IMG warm-up success screen (`L3_热身_HELLO.png`, Rehearsal-1 backup).

---

### Slide 05 | Walk Around — Meet Your New Partner — Core concept (cover-grade annotated board)

**Type**: Core concept (cover-grade annotated board) · **Time**: 7 min

**On screen** (verbatim):

```text
Walk Around — Meet Your New Partner

[annotated Wio Terminal photo — the board fills ~2/3 of the page, nine 2 px black-stroke leader lines with yellow dots, one plain sentence each:]

· Color screen — your project's face: interfaces, numbers, graphics live here
· Three buttons — the human's hand: press, and give your project commands
· Five-way joystick — the human's hand: nudge, and game consoles & menus run on it
· Microphone — it hears things: clap to switch, a sound-level meter
· Light sensor — it knows light from dark: a light that turns on by itself at night
· Accelerometer — it knows moving & tilting: shake detection, fall alarms
· Buzzer — it makes sound: reminders, alarms
· SD card slot (grey, small) — it can store things; just know it exists
· Grove port (grey, small) — the door for new modules later; just know it exists

(small) Every time I name a part, find it on your board with your finger — and touch it.
```

**Instructor notes** (verbatim, hold up the Wio and label as you go, one sentence each): *"Let's walk around and meet your new partner. The color screen — your project's face… Three buttons plus a five-way joystick — the human's hand… The light sensor — it knows light from dark… The microphone — it hears things… The accelerometer — it knows whether it's moving and which way it's tilted… The buzzer — it can make sound… Two small things over here, ears only today: the SD card slot — it can store things; the Grove port — the door for adding new modules later. These two, just know they exist."* **The walk-around never becomes a manual read** — every time you name a part, students find it on their own board with a finger and touch it. SD card slot, Grove port, wireless: one "just know it exists" sentence each, no expansion. A student presses on internet? *"It can — that's a later lesson. Today, just remember it exists."*

**Assets**: IMG annotated Wio Terminal tour diagram (`L3_Wio导览标注图.png`, 720×460) — **to be made**: base = a top-down photo of the Wio (screen lit, flat on the desk); nine 2 px black leader lines + yellow dots; each label one plain sentence (as above); SD card slot & Grove port labels in grey small type. Brand spec: white base, no gradients/shadows, Source Han Sans 14–16 pt labels.

---

### Slide 06 | Why New Gear? Your Project Has a Face and Hands — Core concept (compare)

**Type**: Core concept (compare) · **Time**: 3 min

**On screen** (verbatim):

```text
Why New Gear? Your Project Has a Face and Hands From Today

[left board photo → yellow arrow → right handheld photo:]
OLD BOARD (Grove Beginner Kit)     NEW HANDHELD (Wio Terminal)
Strong at sensing the world —       Adds a color screen, joystick and wireless —
sensors soldered on, plug and play  strong at letting people interact with your project

Use both boards — that one senses the world; this one lets people interact with your project.

📝 Write in your workbook:
"Wio has ___ more than the old board (at least 3)"
"the first thing I want to make with it is ___"
```

**Instructor notes** (verbatim): *"Now compare with the old board: the old one's strength is sensing the world — sensors soldered on, plug and play. This one adds a color screen, a joystick and wireless — its strength is letting people interact with your project. One sentence: why did we change gear? From today, your project has a face and hands."* Then the two workbook lines. **Output anchor**: the two lines written in everyone's workbook.

**Assets**: IMG Grove Beginner Kit board photo (existing local asset `assets/L1_板子全貌图_Grove Beginner Kit.png`) · IMG Wio Terminal photo (reuse IMG-01-01 or a second angle).

---

### Slide 07 | Touching Isn't Knowing — Lighting It Up Is — Operation page (fast flip)

**Type**: Operation · **Time**: 2 min (fast flip into the micro-experiments)

**On screen** (verbatim):

```text
Touching Isn't Knowing — Lighting It Up Is

[five cells, each: line icon + name + empty tick box]
Buttons ☐  ·  Joystick ☐  ·  Microphone ☐  ·  Light ☐  ·  Accelerometer ☐

Five micro-experiments, one line each —
I send mine first, then you send yours.

(small) The lines are printed in your Student Workbook — follow me on the screen.
Lit one up? Tick the box in your workbook.
```

**Instructor notes** (verbatim): *"Touching isn't knowing — lighting it up is. Five micro-experiments, one line each, watch it come alive. The lines are printed in your Student Workbook — follow me on the screen. The rhythm: I send mine first, then you send yours — don't just watch me, send a line and try it yourself."* Flip fast — this page is the round's instructions, not a talking page.

---

### Slide 08 | Micro-Experiment 1/5 · Buttons — The Three-Key Piano — Operation page (big picture)

**Type**: Operation (stand-still) · **Time**: 4 min

**On screen** (verbatim):

```text
Micro-Experiment 1/5 · Buttons
The Three-Key Piano

(monospace instruction card, large)
I'm using the Wio Terminal. Please make this work:
Press buttons A/B/C to play do, mi, sol.
Show DO / MI / SOL in large text on the screen.

[success screenshot, yellow label "this is what success looks like": DO in large text]

Press it, and it answers you — A, B, C: a little piano.
```

**Instructor notes**: *"The first one, the three-key piano. Watch me send it — (send) press A: DO; press B: MI; press C: SOL. Your turn — send it, try it. Can play a little tune? Raise your hand."* New line counts only if it ran in rehearsal — a line that won't run falls back to the original "number-report" version (see Teacher's Guide Section 6 downgrade note); a single dead unit gets swapped, not fixed. **One experiment stuck more than 2 minutes is too long — protect the round's rhythm.**

**Assets**: IMG micro-experiment 1 success screen (`L3_微实验1_按键.png`, Rehearsal-2 backup).

---

### Slide 09 | Micro-Experiment 2/5 · Joystick — Push the Ball — Operation page (big picture)

**Type**: Operation (stand-still) · **Time**: 4 min

**On screen** (verbatim):

```text
Micro-Experiment 2/5 · Joystick
Push the Ball

(monospace instruction card, large)
I'm using the Wio Terminal. Please make this work:
Draw a small ball in the center of the screen.
Push the joystick and the ball moves that way.

[success screenshot, yellow label: the ball pushed off-center]

Nudge it, and the ball listens.
The joystick presses in too — found it? Raise your hand.
```

**Instructor notes**: *"The second one, push the ball. Push the joystick and the ball runs that way. (demo) Your turn — see who can park the ball steadily in the corner."* A student discovers the joystick also presses in (it has a button)? **Affirm the discovery** — it goes on the list of usable inputs for the free round. Line won't run → fall back to the number-report version (UP / DOWN / LEFT / RIGHT).

**Assets**: IMG micro-experiment 2 success screen (`L3_微实验2_摇杆.png`).

---

### Slide 10 | Micro-Experiment 3/5 · Microphone — Blow Out the Candle — Operation page (big picture)

**Type**: Operation (stand-still) · **Time**: 4 min

**On screen** (verbatim):

```text
Micro-Experiment 3/5 · Microphone
Blow Out the Candle

(monospace instruction card, large)
I'm using the Wio Terminal. Please make this work:
Draw a lit candle in the center of the screen.
Blow at the microphone and the flame goes out; after 2 seconds it lights again.

[success screenshot, yellow label: the flame out (or relit)]

One blow, the candle goes out.
Sound doesn't need to report a number — it just needs to do the job.
```

**Instructor notes**: *"The third one, blow out the candle. Send it — blow at the microphone, the flame goes out; after 2 seconds it lights again. Your turn."* A student asks how it knows they blew? One sentence: *"Blow hard enough and it counts as blowing out the candle; the exact units don't matter."*

**Assets**: IMG micro-experiment 3 success screen (`L3_微实验3_麦克风.png`).

---

### Slide 11 | Micro-Experiment 4/5 · Light — The Board Afraid of the Dark — Operation page (big picture)

**Type**: Operation (stand-still) · **Time**: 4 min

**On screen** (verbatim):

```text
Micro-Experiment 4/5 · Light
The Board Afraid of the Dark

(monospace instruction card, large)
I'm using the Wio Terminal. Please make this work:
Draw two open eyes on the screen.
When the light gets dim, close the eyes and show ZZZ;
when it gets bright, open them again.

[success screenshot, yellow label: eyes closed, ZZZ showing]

Cover it, and it falls asleep.
Last lesson's dark-detecting light — in a new costume.
```

**Instructor notes**: *"The fourth one, the board afraid of the dark. Send it — cover the board with your palm, the eyes close, ZZZ appears; take your hand away, it wakes up. This is last lesson's 'dark-detecting light' skill, in a new costume."* Point back to Lesson 1 as you go — the Sense → Logic → Output model is still the engine under every one of these toys.

**Assets**: IMG micro-experiment 4 success screen (`L3_微实验4_光线.png`).

---

### Slide 12 | Micro-Experiment 5/5 · Accelerometer — The Balance Ball — Operation page (big picture)

**Type**: Operation (stand-still) · **Time**: 4 min

**On screen** (verbatim):

```text
Micro-Experiment 5/5 · Accelerometer
The Balance Ball

(monospace instruction card, large)
I'm using the Wio Terminal. Please make this work:
Draw a square frame with a small ball inside.
Tilt the board and the ball rolls toward the low side.

[success screenshot, yellow label: the ball rolled to one side]

Tilt it, and the ball rolls downhill.
Shake detection, fall alarms — this is the one.

📝 Write in your workbook:
"I lit up: ☐ buttons ☐ joystick ☐ microphone ☐ light ☐ accelerometer;
what surprised me most was ___ because ___."
```

**Instructor notes**: *"The last one, the balance ball. Send it — tilt the board, and the ball rolls downhill. It can feel how you move it."* Then the anchor: *"All five tried? Open your workbook, tick the boxes, and write one line: what surprised me most, and why."* Fast students add a free line on top of the current experiment (*"make the ball a different color" / "beep when the ball touches the edge"*); slow students pass by keeping the first three. **Output anchor**: the ticks + one line in everyone's workbook.

**Assets**: IMG micro-experiment 5 success screen (`L3_微实验5_加速度计.png`).

---

### Slide 13 | One Idea, Two Ways of Saying It — Demo guide page (the soul of the lesson)

**Type**: Demo guide · **Time**: 10 min · **Non-negotiable — really send both lines live**

**On screen** (verbatim):

```text
One Idea, Two Ways of Saying It

[left screenshot ← → right screenshot (yellow-outlined):]
"Make a counter screen."            "Show a number in the largest text in the center of the screen;
→ what AI freely gives you          show COUNTER in small text at the top-left;
                                    make the number red." → the precise result

POSITION  ·  SIZE  ·  COLOR

(monospace phrase box) How to describe a screen:
At [position], show [content] in [size/color]; when [action], [change].
```

**Instructor notes** (verbatim, project and really send both in the same conversation): *"Hardware's all lit up — now lesson one of using it well: how do you get AI to give you a good screen? An experiment, one idea two ways of saying it. First way: (send) 'Make a counter screen.' — see what it gives you. (show the result) Second way: (send) 'Show a number in the largest text in the center of the screen; show COUNTER in small text at the top-left; make the number red.' — now see what it gives you. (project side by side) What's the difference? Describing a screen means saying three things clearly: position, size, color."* Land the extension line: *"Logic says 'do this when that happens.' Screens say 'what something is, where it sits, what it looks like.' Two ways of speaking — you need both."* If AI does well both times: *"Today it guessed your mind right — but your project is ten times more complex. You can't afford the wrong guess."* **The screenshots are backups only — the live double-send is the lesson** (live authenticity can't be faked).

**Assets**: IMG comparison · vague result (`L3_对比实验_模糊版.png`) · IMG comparison · precise result (`L3_对比实验_说清版.png`, Rehearsal-3 backups).

---

### Slide 14 | Follow-Along: The Button Counter — Two Steps on Purpose — Operation page

**Type**: Operation (stand-still) · **Time**: 20 min

**On screen** (verbatim):

```text
Follow-Along: The Button Counter — Two Steps on Purpose

STEP 1 · The screen only:
(monospace) Show the number 0 in the largest text in the center of the screen,
and COUNTER in small text at the top-left.  → Flash it, look at it.

STEP 2 · The behavior:
(monospace) When I press button A, add one to the number; when I press B, reset to zero.
→ Flash again — then one more line: "Every time the count reaches 10,
the buzzer beeps once to celebrate."

(notice, yellow) First describe the looks, then the actions — it doesn't get confused.
Buttons not responding? "No response? Slide it."
```

**Instructor notes** (verbatim): *"Follow along, and we say it in two steps on purpose. Step one, the screen only: 'Show the number 0 in the largest text in the center of the screen, and COUNTER in small text at the top-left.' Flash it, look at it. Step two, the behavior: 'When I press button A, add one to the number; when I press B, reset to zero.' Flash again — then one more line to the whole class: 'Every time the count reaches 10, the buzzer beeps once to celebrate.' (the room fills with button presses; count to 10 and hear the beep) See? First describe the looks, then the actions — two ways of speaking, two separate lines, and it doesn't get confused. Wrong? Add one more line. That's also the old Five-Rules rule: one thing at a time."* **The #1 reason buttons don't respond: flash mode never exited** — the mantra *"No response? Slide it (back to run mode)."* The TA checks this first. Text overflowing / color not showing? One sentence: *"This is exactly the precision problem of 'describing looks' — add one more line of description and have it change."* Someone already making a joystick game? Don't forbid: *"Fine to play — but the two-screens requirement stays."*

**Assets**: IMG counter step 1 (`L3_计数器_步骤一.png`) · IMG counter step 2 (`L3_计数器_步骤二.png`, Rehearsal-4 backups).

---

### Slide 15 | Free Round: Make Something With Two Screens — Task page

**Type**: Task (stand-still) · **Time**: 40 min

**On screen** (verbatim):

```text
Free Round — Make Something With Two Screens

Switch between them with a button or the joystick.

[five input icons, horizontal row] Buttons · Joystick · Microphone · Light · Accelerometer
— pick what's comfortable.

[example cards] Clock · Mood display · Stopwatch · Your own menu · Reaction tester
(screen turns green → press A → shows your milliseconds — naturally two screens;
content in English, numbers or graphics)

(old discipline, yellow) Tell your neighbor what your two screens each look like —
position, size, color, said clearly — BEFORE you talk to AI.

📝 Write in your workbook — "the sentence I said to AI about my screen":
your proudest description.
```

**Instructor notes** (verbatim): *"Free build, one-line brief: make something with two screens, and switch between them with a button or the joystick. A clock / a mood display / a stopwatch / a menu of your own / a reaction tester (the screen turns green, you press A, it shows your milliseconds — naturally two screens)… anything works (screen content in English, numbers or graphics). You now have five inputs in your hands — button, joystick, microphone, light, accelerometer — pick what's comfortable. Old discipline: tell your neighbor what your two screens each look like BEFORE you touch the keyboard — position, size, color, said clearly — then talk to AI."* Collect 1–2 "described unclearly → AI drifted off" cases (the drift gallery needs them next). Fast students: add a sensor link to the two-screen project (an input just lit up — e.g., auto-switch to a night screen when it gets dark). Slow students' bar: the counter + one custom change. A student dumps the whole job on AI at once? *"Directors shoot one scene at a time. Get the first screen described beautifully, then the second, and only at the end how to switch."* Two screens degrade to one? Lower the bar to "counter + one custom change" and have them log "where I got stuck trying to make two screens." Someone's screen looks great and people gather? Invite them to project it — but push one question: *"What exactly did you say to AI?"* — the wow must land on a reusable way of saying it.

**Output anchor**: everyone copies one line into the workbook — "the sentence I said to AI about my screen."

---

### Slide 16 | Whole Room — Come Look at a Treasure — Interaction page

**Type**: Interaction · **Time**: 10 min

**On screen** (verbatim):

```text
Whole Room — Come Look at a Treasure

[drift case screenshot — a screen that went off the rails]

They said ___  →  AI made ___  →  which sentence went wrong?

(quote box, yellow left border) Thank this student —
they stepped in the pit so the whole class doesn't have to.
A crash isn't a joke; it's teaching material.
```

**Instructor notes** (verbatim, project the drift case): *"Whole room, come look at a treasure. (project) See: they said ___, AI made ___. Which sentence went wrong? (lead the class to find it) There — they forgot to say where. Thank this student — they stepped in the pit so the whole class doesn't have to. A crash isn't a joke; it's teaching material."* The volunteer is always voluntary; no volunteer → use the pre-made case from Rehearsal 5; once someone volunteers, the pre-made case is dropped. **The tone is set: the volunteer is the hero** — anyone snickering, take the line back on the spot: *"They stepped in the pit for the whole class. That's a hero."*

**Assets**: IMG pre-made drift case (`L3_跑偏案例.png`, Rehearsal-5 backup with the three-line annotation; dropped if a student volunteers).

---

### Slide 17 | Three Takeaways for Using It Well + Your AI Log — Operation page

**Type**: Operation · **Time**: 10 min · **Red element (one on this page — the only red in the deck)**

**On screen** (verbatim):

```text
Three Takeaways for Using It Well

① Describe a screen with position, size and color
② Make state visible — have the screen show where you are in its steps
③ Many inputs? Try combinations — button, joystick, microphone, light, accelerometer

Your log, four sentences:
· Today I made ___
· I got stuck on ___ (today: name it — position, size, or color?)
· Then ___
· Next time I want ___

Say it, then send it to AI: "Tidy this into a learning log — only what I said, nothing I didn't say."

(warning, red left border) ⚠️ AI will make things up with a straight face.
Proofreading is your job.

(small) Circle one takeaway — "the one I used most today was #___".
The log goes into your workbook proofread.
```

**Instructor notes** (verbatim): *"Last question: what's different between describing a screen to AI and describing logic? (lead them to: logic says 'do this when that happens'; screens say 'what something is, where it sits, what it looks like') — so, three takeaways for using this handheld well. First: describe a screen with position, size and color — you saw it with your own eyes; say the three things or don't, and you get two different things. Second: make state visible — the board has a screen; have it show you where it is in its steps, so you always know what it's doing. Third: with many inputs, try combinations — the best projects often come from trying 'which input feels most natural.'"* Then the log: take a photo of the screen project, say thirty seconds, the usual four sentences — today's "stuck on" must be specific: position, size, or color. Send to AI with the tidy line; when it's done, read it: *"AI will make things up with a straight face. Proofreading is your job — nobody can do it for you."* The TA takes extra build photos (hands only, no faces); students without phones get photos taken by the TA, filed by table number. **Output anchor**: ① circled takeaway; ② the proofread four-sentence log in the workbook.

---

### Slide 18 | 30 Minutes — Standard First, Then Fast — Task page (big-type)

**Type**: Task (big-type, stand-still) · **Time**: 30 min (16:20–16:50)

**On screen** (verbatim):

```text
30
minutes

FINISH TO STANDARD (everyone crosses this line)
Counter runs + one two-screen project.

CHALLENGE TASKS (fast lane)
Electronic dice — shake it (or flick the joystick once), the screen shows a random 1–6.
Or: balance-ball hole-in-one — micro-experiment 5 plus a target hole; the buzzer beeps when the ball drops in.

HELP A NEIGHBOR + ADD A SENSOR LINK
Give your two-screen project a sensor link (e.g., auto-switch to a night screen when it gets dark).

(rule, yellow) Standard first, then fast. — The buffer is part of the lesson, not early dismissal.

(small) Did a challenge? Write in your workbook —
"I used ___ (which input) to make ___ (what little thing)."
```

**Instructor notes** — set the tone at the start (announce today's exit per your pre-class choice, verbatim): *"Next 30 minutes work like this: if your two-screen project isn't done, finish it — that's the line everyone must cross today. Crossed it? [announce today's plan: take a challenge task / help your neighbor / add a sensor link to your project]."* Circulation order: first sweep who hasn't crossed the line (the TA watches these), then lead the fast ones through challenges. **Challenge tasks: only the ones you rehearsed** — unrehearsed tasks don't go out; if none of them run, the buffer keeps only "finish to standard" and "help your neighbor." Challenge done? Steer toward one line: *"You've got the joystick down — later it becomes a controller for your computer. That's the road ahead."* A student says "I'm done, can I leave / play on my phone?" — point to the three exits: *"Help a neighbor, take a challenge, or add a sensor link to your project."* Everyone clears the bar with 20 minutes left? Don't drag — move into the show & tell early and finish the wrap at a relaxed pace. **Output anchor** (challenge students): the "I used ___ to make ___" line in the workbook.

**Assets**: IMG challenge success screens — electronic dice (`L3_挑战_电子骰子.png`) · balance-ball hole-in-one (`L3_挑战_平衡球进洞.png`, Rehearsal-5 backups, only if they ran).

---

### Slide 19 | Flash Show & Tell + Next Time — Call-to-action

**Type**: Call-to-action · **Time**: 10 min

**On screen** (verbatim):

```text
Flash Show & Tell + Next Time

In your table, 30 seconds each — demo your project, say one line:
"which input I used, and how I switch screens."

Two things you take away today:
① You met the new gear — screen, buttons, joystick, three sensors —
   every one lit up by your own hand
② You learned lesson one of using it — position, size, color —
   your project has a real interface from today

NEXT TIME
Lesson 4: Give AI a Team
One complete project end to end: your own smart Pomodoro timer.

(small) It runs on this very color screen — today's screen skills get used all the way through.
Bring your topic.
```

**Instructor notes** (verbatim): *"In your table, 30 seconds each: demo your project, say one line — 'which input I used, and how I switch screens.' (after the show & tell) Last two minutes — take stock. One: you met the new gear — the Wio has a screen, buttons, a joystick and three sensors, and you lit every one of them up yourself. Two: you learned lesson one of using it: describe a screen — position, size, color — and your project has a real interface from today. Next session is a big day: we give AI a team — so it's more than one person working for you — and build one complete project end to end: your own smart Pomodoro timer. It runs on this very color screen, so today's screen skills get used all the way through. Bring your topic. Class dismissed!"* Localize the Pomodoro explanation if needed: *"a Pomodoro = a focus timer — 25 minutes focused, 5 minutes off, that kind of thing."* After class: collect today's work (links or photos), note what's missing; leave the mantra cards on the desks and collect them — reusable next session.

---

## Asset & Placeholder Checklist (from the CN plan, localized notes)

| Slide | Asset | Size | Status |
| --- | --- | --- | --- |
| 01/03/06 | Wio Terminal handheld photo `L3_Wio掌机实拍.png` (screen lit; shared by cover / ceremony / compare — 2 angles if possible) | 420×360 | To photograph |
| 02 | Project Wall photo `L3_选题墙.png` (Lesson 2 TA shot — wall only, no faces) | 380×300 | Select from L2 material |
| 03 | Flash-mode switch close-up `L3_烧录开关特写.png` (yellow circle marking the switch) | 320×240 | To photograph |
| 04 | Warm-up success screen `L3_热身_HELLO.png` (Rehearsal-1 backup) | 360×270 | To capture at rehearsal |
| 05 | **Annotated Wio tour diagram `L3_Wio导览标注图.png` (to be made — build instructions in slide 05)** | 720×460 | **To make** |
| 06 | Grove Beginner Kit board photo (existing local asset `assets/L1_板子全貌图_Grove Beginner Kit.png`) | 320×240 | ✅ Local asset |
| 08–12 | Micro-experiment success screens ×5 (DO on screen / ball pushed / candle out / eyes closed ZZZ / ball rolled) `L3_微实验1_按键.png` – `L3_微实验5_加速度计.png` (Rehearsal-2 backups) | 400×300 ×5 | To capture at rehearsal |
| 13 | Comparison screenshots ×2 — vague result `L3_对比实验_模糊版.png` / precise result `L3_对比实验_说清版.png` (Rehearsal-3 backups; **live double-send is the lesson, screenshots are fallback**) | 360×270 ×2 | To capture at rehearsal |
| 14 | Counter step results ×2 `L3_计数器_步骤一.png` / `L3_计数器_步骤二.png` (Rehearsal-4 backups) | 300×220 ×2 | To capture at rehearsal |
| 16 | Pre-made drift case `L3_跑偏案例.png` (Rehearsal-5 backup with three-line annotation; dropped if a student volunteers) | 420×300 | To capture at rehearsal |
| 18 | Challenge success screens `L3_挑战_电子骰子.png` / `L3_挑战_平衡球进洞.png` (Rehearsal-5 backups — only if they ran) | 300×220 | To capture at rehearsal |

**Downgrade**: slide 05's annotated diagram missing → instructor holds the real board, labels a whiteboard frame by hand (the guide explicitly allows the whiteboard tour map), page keeps the nine-point text list only; slides 08–12 micro-experiment screenshots missing → run the live demo on the real interface (the round is dual-track by design — cutting to backup within 30 seconds is not an incident); a micro-experiment line won't run in rehearsal → fall back to the original "number-report" versions (Teacher's Guide Section 6) and swap the on-screen line accordingly; slide 13 comparison screenshots missing → **must still really send both lines live** (the live authenticity is the teaching point; screenshots are only the fallback); slides 01/03/06 Wio photos missing → line-outline art + the instructor holds the real unit; extreme case, all screenshots missing → the full deck stands as pure text — the big screen only shows "what to look at", the detail lives in the instructor's hands and mouth.

---

## Localization Slots

| Slot | Default | Swap in |
| --- | --- | --- |
| Slide 04 warm-up display content | [HELLO and my name (pinyin or English)] | words your students feel more strongly: their team name, their game character's name — lights up faster |
| Slides 08–12 micro-experiment lines | [DO / MI / SOL, UP/DOWN/LEFT/RIGHT, ZZZ…] | local flavor is fine in the spoken lines (a slang direction word); **keep the on-screen display in English** |
| Slide 15 free-round examples | [clock / mood display / stopwatch / menu of your own] | add local hooks — "a countdown to market day," "a scoreboard for the big match" |
| Slide 19 closing preview | [smart Pomodoro timer] | don't swap the project (Lesson 4's design is already set) — localize the explanation: "a Pomodoro = a focus timer — 25 minutes focused, 5 minutes off, that kind of thing" |

---

## Backup & Downgrade

- Slide 05 annotated diagram not ready → instructor holds the real board + hand-drawn whiteboard frame (guide allows); page keeps the nine-point text list.
- Slides 08–12 micro-experiment screenshots missing → live real-interface demo (30-second cut-to-backup rule; not an incident). A line won't run in rehearsal → swap in the number-report fallback line on the page.
- Slide 13 comparison screenshots missing → **must still really send both lines live** — the screenshots are only backups; live authenticity can't be faked.
- Slides 01/03/06 Wio photos missing → line-outline art + instructor holds the real unit.
- **All screenshot assets missing (extreme case)** → the whole deck stands as pure text; the projector shows only "what to look at", the instructor's hands and mouth carry the detail.
- Internet dies during build time (>15 min) → micro-experiments and screen descriptions finish on paper first (lines written out, neighbor reviews the description); flashing practice defers.
- The buffer turns into free time → set the tone at the start by announcing the exits; circulation rule "standard first, then fast"; someone wandering → hand them a challenge: *"Electronic dice — want to try?"*

---

_English PPT Plan · Lesson 3 · Give Your Project a Screen v1 ｜ 2026-08-26 ｜ Source: CN deck plan v2 (v2.1 update applied; 19 slides, 2026-07-27/28) + EN Teacher's Guide L03 v1 (2026-08-25) ｜ Terms locked to EN Glossary + EN Teacher's Guide L03 ｜ Next: build the EN .pptx from this plan (brand rebuild, Chaihuo spec; re-capture Codecraft UI screenshots in English where possible)_
