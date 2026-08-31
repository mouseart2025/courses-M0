# M0 English PPT Plan ｜ CFG-5 Semester Course · Lesson 5: Teach Your Hardware to See (v1)

_XIAO ESP32S3 Sense · Edge AI Vision Board ｜ Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) ｜ 3 hours (sample 14:00–17:00, no scheduled break) ｜ Source: CN deck plan v2 as structural archive (v2.1/v2.2 revisions noted; the v2.3 47-page user hand-edit is the CN deck's final form — the EN deck is a brand rebuild from the V3 teaching structure, NOT a copy of the 47-page file) + EN Teacher's Guide L05 v1 (all 🗣️ lines match) ｜ This plan is the English blueprint — every on-screen line and every script line below is final English copy. The visual system follows the Chaihuo brand spec unchanged; only text is localized. Terms locked to the EN Glossary + EN Teacher's Guide L05 (the little eye board / photo in, experience out / you tell it, it builds / you show it, it learns / the answer name = label / the experience book / training / deploy / the AI Blink / the swap test / the attribution / the three-box sheet (vision edition) / confidence / the vision-to-action prompt / the fallback prompt / UART·I2C·SPI / scissors·rock·paper / hands and objects only — no faces / SIGNED IN / small computer, small jobs)._

> **Deck-level note (internal, never on screen)**: 20 pages in five beats — Vision AI & the New Gear (01–06) → First Half · Teach It to See (07–12) → Second Half · Make Seeing Turn Into Action (13–17) → Buffer (18) → Close (19–20). Timings align with the EN Teacher's Guide L05 timetable (the V3 structure): 14:00–14:28 / 14:28–15:46 / 15:46–16:41 / 16:41–16:50 / 16:50–17:00. **This is a "new AI + new hardware" session**: the first half does NOT use conversational AI — "teaching it to recognize" runs on data, not prompts — so this deck has only ONE sentence page (slide 16, the vision-to-action prompt, stand-still); the rest of the first half is concept pages and rules pages. **The non-negotiables: today's iron law — training must be hands-on, never a teacher demo (this lives in the instructor's script, NOT on screen); the hands-only imaging rule (slide 08 — faces get deleted on sight, the deck's first red); the "what if it can't recognize it" column is a required question (slide 15 — the deck's second red); and the attribution landing line (slide 11 — "it's not dumb, you taught it too little" is the first-half payoff).** Flexible (can compress): the swap test (9→6 min), the AI Blink (22→15 min, trigger config becomes a teacher demo), sensor output & protocols (14→7 min, UART only), the buffer (9→5 min). Never compress: data collection (under 15 min of data = collapse), train + deploy, the attribution's one landing line, collecting Lesson 4 output. Red appears exactly twice — slide 08's imaging-compliance warning and slide 15's required-question column; the AI Blink's face-detection demo (slide 07) recognizes only the teacher's own face or an on-screen photo (compliance, stated verbally, not red). **Nothing Chinese ever goes on screen in the EN deck** — class names are English (scissors / rock / paper), on-screen display text is English / numbers / graphics (SIGNED IN, confidence percentages) as a course-wide rule. Note on the prompt page: the V3 deck removed the prompt page (the teacher types it on screen from Teacher's Guide Section 6); the EN deck restores it as a stand-still sentence page — the formalized version of "typed on screen," consistent with the English edition's "the screen is the teleprompter" strategy. Prompt text is verbatim from Teacher's Guide Section 6._

---

## Design Principles

- **A "new AI + new hardware" session means concept pages and rules pages share the weight**: the two-kinds-of-AI contrast, the XIAO pros/cons, the collection rules, the attribution landing and the sensor-output block are the concept spine; the one sentence page (16) carries the build. Graphic-heavy pages are kept minimal — board photos + short lines (slides 03, 04).
- **The first half runs on data, not prompts**: "teaching it to recognize" = showing it photos, not typing instructions. No sentence pages in the first half — the rules pages (08, 10) stand still while students work; the screen is the students' working reference, not the instructor's teleprompter.
- **The "two kinds of AI" contrast is the soul of the lesson**: slide 03 — "you tell it, it builds" (the AI students have used for four lessons) vs "you show it, it learns" (new today). The hook: "First half of today: no typing. You talk with photos."
- **The AI Blink is the first "it works!" moment**: slide 07 — deploy a ready-made face-detection model, configure the trigger "face detected → LED on," then drive a light strip directly through the Grove expansion board — **not one line of code**. Compliance: face detection is demonstrated on the teacher's own face or an on-screen photo only; the imaging rule is stated here once: "hands and objects only — no faces."
- **Bad data is designed, not an accident**: slide 08's collection demo deliberately includes "bad photos" (one angle, messy background, half a hand) that the teacher does NOT explain yet — they become the attribution lesson's textbook. A student training on only 10 photos is allowed through silently — their failure later is teaching material.
- **The attribution landing line closes the first half**: slide 11 — failure-rate tally → sticky wall ("my model gets it wrong when ___", specific beats vague) → the landing: **"It's not dumb. You taught it too little."** The loop-back: "for an AI that recognizes things, the examples ARE everything — telling it isn't enough, you have to show it."
- **The second half adds a professional decision**: slide 15's new column — "what if it can't recognize it, or isn't sure?" is a required answer (writing "do nothing" is valid — but it must be *your* decision, not its accident); the confidence threshold (below 70% = treat as not recognized) is the operating rule.
- **The vision-to-action build keeps the old discipline**: slide 16 — "one thing at a time": scissors → LED runs first, then rock, then paper. The prompt names the student "the boss of two AIs" (SenseCraft's model recognizes, Codecraft's program acts).
- **Output anchors everywhere**: slides 08 / 09 / 10 / 11 / 12 / 15 / 16 / 18 each carry a 📝 "write it in your workbook (or notebook)" action box.
- **Stand-still pages**: 08 (collection), 16 (vision-to-action build), 18 (buffer). Slide 17 (fallback + errors) is a fast-flip inserted inside the build block — no separate timing.
- **Zero print**: the three-box sheet and the prompt text are shown on screen (prompt text verbatim in slide 16) — students draw their own three boxes in the workbook; account info is verbal or on screen.

### Colors / Type / Icons / Layout

Chaihuo brand spec (`chaihuo-ppt-brand.md`): white 70 / yellow F3D230 15 / black 10 / red D84144 5; no gradients, no shadows, no complex illustrations; 2 px black-stroke line icons; Source Han Sans; 16:9 (960×540 px); title zone 100 px top, content 110–490 px, footer 40 px. **Red appears exactly twice in this deck — slide 08's imaging-compliance warning (hands and objects only — no faces) and slide 15's required-question column (what if it can't recognize it)** (two red elements, strictly capped). The AI Blink's graphic lights use graphic colours (green `#7FB069` / red `#D84144` outside the quota when showing LED states), consistent with the L4 traffic-light convention. Sentence-page structure: role line (yellow light fill) + large monospace prompt box (white fill, black border) + one reminder; stand-still during the build. Script/quote boxes: the one permitted fifth colour — light grey `#F5F5F5` fill + 1 px black border + monospace 14–16 pt.

### On-Screen Text Rules

- All on-screen text is final English copy (below, verbatim). Digits for all numbers.
- Student-typed prompt lines are shown in monospace boxes; the part students must swap in is marked with an underline `___`.
- **On-screen display is English / numbers / graphics by design** — class names stay English (scissors / rock / paper); on-board display text (SIGNED IN, percentages) is English as a course-wide rule. If garbled glyphs still appear, tell AI *"change all on-screen text to English"* — don't debug the font library.
- During hands-on segments the page stays fixed; instructors read from the Teacher's Guide, not from the slide.

---

## Slide Map

| # | On-screen title | Type | Beat | Time |
| --- | --- | --- | --- | --- |
| 01 | Teach Your Hardware to See | Title page | Cover | Loops before class |
| **Part 1 · Vision AI & the New Gear (14:00–14:28, 5 slides)** | | | | |
| 02 | How It "Sees": Photo In, Experience Out | Core concept (concept + three examples) | Concept | 8 min |
| 03 | Your Third Board: The Eyes + Two Kinds of AI | Core concept (compare) | Concept | 5 min |
| 04 | Meet the XIAO: The Little Eye Board | Photo page (board anatomy) | Gear | 8 min |
| 05 | Three Pros, Three Cons — You'll Hit Them All Today | Core concept (pros/cons) | Gear | part of 04's block* |
| 06 | Today's Tool + the Sign-In Demo | Demo guide page | Demo | 7 min |
| **Part 2 · First Half · Teach It to See (14:28–15:46, 6 slides)** | | | | |
| 07 | Experience 1: The AI Blink — Deploy Someone Else's Model | Demo guide page | Hands-on | 22 min |
| 08 | Experience 2 · Collect Data: 25–30 Per Gesture, Hands Only | Rules page (stand-still) — **red (1/2)** | Hands-on | 22 min |
| 09 | Train + Deploy: Photos Become Experience | Demo guide page | Hands-on | 10 min |
| 10 | The Swap Test: Does It Know Your Neighbor's Hand? | Rules page | Hands-on | 9 min |
| 11 | The Attribution: It's Not Dumb — You Taught It Too Little | Core concept (landing page) | Reflect | 10 min |
| 12 | First-Half Log: My Model Gets It Wrong When ___ | Operation guide page | Log | 5 min |
| **Part 3 · Second Half · Make Seeing Turn Into Action (15:46–16:41, 5 slides)** | | | | |
| 13 | Sensor Output: Where Does the Result Go? | Core concept | Concept | 14 min |
| 14 | The Brief: Recognize It → Make It Move | Task page | Frame | 10 min |
| 15 | Three-Box Sheet: One New Column — "What If It Can't Recognize It?" | Operation step page — **red (2/2)** | Plan | 10 min |
| 16 | The Vision-to-Action Prompt: One Class Running, Then Extend | Sentence page (stand-still) | You Do | 21 min |
| 17 | Fallback + Error Handling | Operation guide (fast flip, inside the build) | You Do | no separate time |
| **Buffer (16:41–16:50, 1 slide)** | | | | |
| 18 | 9 Minutes — Three Exits, Pick One | Task page (big-type, stand-still) | Buffer | 9 min |
| **Close (16:50–17:00, 2 slides)** | | | | |
| 19 | Today You Touched How AI Gets Made | Core concept (golden-line page) | Close | 5 min |
| 20 | Bring Your Model Back + Pack-Up | Call-to-action | Close | 5 min |

> 20 pages, ~180 minutes (includes stand-still time), matches the 3-hour session (±10%). *Slide 05 runs inside slide 04's 8-min block (Meet the XIAO + pros/cons are one teaching beat, pages 08–10 of the V3 deck). **The non-negotiables: training is hands-on, never a teacher demo (iron law — instructor-side, not on screen); slide 08's hands-only imaging rule; slide 15's required "can't recognize" column; slide 11's attribution landing line.**

---

## Slide by Slide

### Slide 01 | Teach Your Hardware to See — Title page

**Type**: Title · **Time**: loops before class

**On screen** (verbatim):

```text
Teach Your Hardware to See

Hand-Train Your First Vision Model · Chaihuo Maker Academy · M0 Lesson 5

Today your board learns a brand-new skill.
```

**Instructor notes**: open with one welcome line — *"Welcome to Lesson 5. Last session you built a complete Pomodoro timer with the BMAD five roles — today your hardware learns a brand-new skill: to see."* — then go straight to slide 02; the cover is not a talking page. XIAO photo on the right (thumb-size, camera side up, next to a thumb for scale), yellow rule under the subtitle. Footer: `Chaihuo Maker Academy · M0 · Teach Your Hardware to See | 05 / 20`.

**Assets**: IMG XIAO thumb-size photo (`L5_XIAO拇指对比.jpg`, camera up, thumb for scale).

---

### Slide 02 | How It "Sees": Photo In, Experience Out — Core concept (concept + three examples)

**Type**: Core concept · **Time**: 8 min

**On screen** (verbatim):

```text
How Does a Machine "See"?

[FLOW, yellow arrows: PHOTO IN → [algorithm] → EXPERIENCE OUT]

[THREE EXAMPLE CARDS, quick-skim]
TESLA — eight cameras, a full 360° of road
PANDA WATCH — one camera over one mountain; spots a panda, reports the location
HUMMINGBIRD FEEDER — recognizes a hummingbird, notes when it came to eat

(quote box) None of them talks or writes. They see.
```

**Instructor notes** (verbatim): *"To open today — let's see how it 'sees'. (point at the flow) A camera captures an image and turns it into numbers — the photo goes in, 'experience' comes out. The algorithm in the middle has a big name — you don't need to memorize it. (point at the three cards) Tesla runs eight cameras looking at a full 360° of road. In a huge forest, one camera watches over one mountain — when it spots a panda, it reports the location. A hummingbird feeder — when it recognizes a hummingbird, it notes what time it came to eat. Spot the common thread? None of them talks or writes. They **see**. Today, your board learns to do the same."* **Skim the example cards — don't linger.** "What is feature extraction / CNN?" → *"An algorithm that finds patterns in photos. You don't need the name — just remember: photo in, experience out."* Three examples dragging → only the hummingbird; Tesla and panda get one line each.

---

### Slide 03 | Your Third Board: The Eyes + Two Kinds of AI — Core concept (compare)

**Type**: Core concept (compare) · **Time**: 5 min

**On screen** (verbatim):

```text
Your Third Board — The Eyes
(and the second kind of AI)

[THREE-BOARD STORY, yellow arrows]
① GROVE KIT = SKIN — feels hot, cold, motion
② WIO = FACE — has a screen and buttons
③ XIAO = EYES — has a camera (and a microphone): it can see and hear

[RIGHT: two kinds of AI, side by side]
YOU TELL IT, IT BUILDS     YOU SHOW IT, IT LEARNS
(the AI you've been using) (new today)
tell Codecraft what you want →    say nothing; show it photos, lots of them →
it writes the instructions          it learns to recognize on its own
                                   (the website: SenseCraft AI — where you teach
                                    boards to recognize things)

(bottom, quote box) First half of today: no typing. You talk with photos.
```

**Instructor notes** (verbatim): *"This is your third board. The first one, the Grove kit — that's **skin**: it feels hot, cold, motion. The second one, the Wio — that's the **face**: it has a screen and buttons. This thumb-sized little board is the **eyes** — it has a camera, and a microphone too. It can see and hear. So far you've used one kind of AI: **you tell it, it builds** — you tell Codecraft what you want and it writes the instructions for you. Today you meet a second kind: **you show it, it learns** — you don't say a word; you show it photos, lots of them, and it learns to recognize on its own. The website is called SenseCraft AI — it's where you teach boards to recognize things. First half of today: no typing. You talk with photos."* "Is this the same AI as ChatGPT?" → the standard line: *"Both learn from lots of examples — but one learns text and the other learns images. Want the deep version, find me at break."*

---

### Slide 04 | Meet the XIAO: The Little Eye Board — Photo page (board anatomy)

**Type**: Photo page · **Time**: part of the 8-min block (with slide 05)

**On screen** (verbatim):

```text
Meet the XIAO ESP32S3 Sense — call it "the little eye board"

[ANNOTATED XIAO PHOTO, 2 px black-stroke leader lines + yellow dots:]
· Camera — its eye
· Microphone — its ear
· Two little buttons — reset and boot (you'll use them when flashing)
· Tiny LED · SD card slot · charging port (just know they exist)

(highlight, yellow light fill) The most special thing: AI lives inside the board.
Once the trained model is loaded in, it recognizes your gestures with NO internet at all.
```

**Instructor notes** (verbatim, hold up a XIAO; pass it around the aisles): *"Its name is XIAO ESP32S3 Sense — you don't need to memorize it; call it **the little eye board**. It has a whole family of siblings, all different models; today we use the one with the camera. (point at the anatomy diagram, walk the class around it) What's on it: this is the camera — its eye. This is the microphone — its ear. These two little buttons — reset and boot; you'll use them when flashing. And here: a tiny LED, an SD card slot, the charging port. Don't memorize all of it — just recognize the eye and the two little buttons. The most special thing: **AI lives inside the board.** Once the trained model is loaded in, it recognizes your gestures with no internet at all."* Students pass a XIAO around; find the camera and the two buttons on the anatomy diagram.

**Assets**: IMG XIAO anatomy diagram (from V3 deck pages 08–09 — family chart + anatomy; re-crop for the EN deck).

---

### Slide 05 | Three Pros, Three Cons — You'll Hit Them All Today — Core concept (pros/cons)

**Type**: Core concept · **Time**: part of the 8-min block (with slide 04)

**On screen** (verbatim):

```text
Three Pros, Three Cons — You'll Hit Them All Today

[LEFT, yellow light fill — PROS]
SMALL — thumb-size, fits anywhere
CHEAP — about the price of a lunch
AI RUNS ON THE BOARD — no internet; your photos never leave this little board

[RIGHT, white fill — CONS]
SMALL COMPUTING POWER — it "thinks" half a second slower; normal
IT MAKES MISTAKES — "what to do when it can't recognize" is part of your design
NO SCREEN — it talks through lights, buzzers, or the computer

(quote box, bottom) Small computer, small jobs.
```

**Instructor notes** (verbatim): *"Three pros. One: it's **small**. Two: it's **cheap** — about the price of a lunch. Three: **the AI runs on the board** — no internet needed, and your photos never leave this little board. Three cons — and you'll hit all of them today. One: **small computing power** — it 'thinks' about half a second slower; normal. Two: **it makes mistakes** — 'what to do when it can't recognize' is part of your design. Three: **no screen** — it talks through lights, buzzers, or the computer. Remember one line: **small computer, small jobs.**"* "How is this different from photo recognition on my phone?" → *"The phone sends the photo to a faraway computer to recognize it. This board recognizes it on itself — slower, but no internet, and it doesn't hand your photos to anyone."* "No screen is weak" → *"Right — that's why it usually teams up with the Wio: one sees, one shows. Today, lights and buzzers speak for it."*

---

### Slide 06 | Today's Tool + the Sign-In Demo — Demo guide page

**Type**: Demo guide · **Time**: 7 min (includes collecting Lesson 4 output, hard-timeboxed at 5 min)

**On screen** (verbatim):

```text
Today's Tool + It Can "See" Because Someone Taught It

[LEFT: tool card]
sensecraft.seeed.cc/ai — don't write it down; the tabs are already open
on every machine once the boards go out.

[RIGHT: demo screenshot — camera pointing at the badge on screen; the board shows:]
SIGNED IN

[THREE LINES]
· Not face-recognition — someone taught it
· How? By showing it lots and lots of photos
· Today, each of you teaches one with your own hands — your own gestures

(small, footer) Collecting Lesson 4: Pomodoro timer record — md link or photo.
```

**Instructor notes** (verbatim): *"Here's today's weapon: sensecraft.seeed.cc/ai — don't write it down; the tabs are already open on every machine once the boards go out. Collecting last session's work: last time, you took a complete project — your Pomodoro timer — from requirements, to screens, to code, to breaking it, with the BMAD five roles. (pick up the teacher machine; point the camera at the badge on screen — it shows **SIGNED IN**; point at something else — nothing.) How does it know the badge? It's not face-recognizing. It's that **someone taught it.** Not by writing, not by talking — by showing it lots and lots of photos. Today, each of you teaches one with your own hands — teaching it to recognize your own gestures."* **If the demo model gets it wrong live** → don't panic, that's today's lesson: *"See? It makes mistakes too — by the end of class you'll know why it does."* No badge → project any high-contrast, stable image (logo / course mark / big English word — CHAIHUO / M0). Collecting: hard 5-minute timer; no individual feedback; note who's missing, due before class ends.

**Assets**: IMG sign-in demo screenshot (`L5_签到SIGNED-IN.jpg`, from rehearsal — SIGNED IN banner; 1 wrong-recognition backup).

---

### Slide 07 | Experience 1: The AI Blink — Deploy Someone Else's Model — Demo guide page

**Type**: Demo guide · **Time**: 22 min (14:28–14:50)

**On screen** (verbatim):

```text
Experience 1 — The AI Blink: Use a Model Someone Else Taught

[THREE STEPS, yellow numbered dots]
① Assemble & connect — cable pushed all the way in; "connect device", see your board's name
② Pick FACE DETECTION in SenseCraft → click DEPLOY — the model travels down the cable into the board
③ Give it a trigger: FACE DETECTED → TURN ON THE ONBOARD LED — point at it, it lights up

[LIVE DEMO SPOT: point at the teacher's face — the LED lights; point at something else — off]

(quote box, yellow light fill) Congratulations — you just deployed an AI-driven automation system.
Not one line of code. The vision model drives the peripheral directly.

(small, compliance) The demo recognizes the teacher's face or an on-screen photo — nobody photographs anyone's face.
```

**Instructor notes** (verbatim): *"Boards out. Assemble and plug in first — both ends of the cable pushed all the way in. Connect to the computer, click 'connect device', see your board's name. Once connected, don't rush to photograph. First, load a model **someone else already taught** into the board. In SenseCraft, pick face detection, click 'deploy' — it travels down the cable into the board. Now give it a 'trigger': face detected → turn on the onboard LED. Watch the LED's spot — point at my face — on! Congratulations — you just deployed an AI-driven automation system. And watch this: add the Grove expansion board, plug in a light strip — target recognized, the strip lights up directly. **Not one line of code.** The vision model drives the peripheral directly. That's 'recognized → moves'. You'll build one of these yourselves in the second half."* ⭐ **This is the class's #1 failure-prone block: all three TAs push in.** One student can't connect in 3 minutes → swap board, swap cable, don't linger (swap, don't repair). Login fails → TA A hands over a spare account on the spot. Black/blurry image → first question *"is the lens film off?"*, second move swap the board. **Compliance:** face detection recognizes only the teacher's own face or the on-screen photo — students don't photograph each other's faces. State the rule now: *"When you collect your own data later — **hands and objects only. No faces.**"* Short on time → trigger config becomes a teacher demo; students only get "deployed + recognized." **Output anchor**: every board runs a ready-made model — recognized target lights the onboard LED.

**Assets**: IMG AI Blink trigger-config screenshot (V3 deck pages 13–22 — trigger screen with LED spot; re-crop for EN).

---

### Slide 08 | Experience 2 · Collect Data: 25–30 Per Gesture, Hands Only — Rules page — **RED (1/2)**

**Type**: Rules (stand-still) · **Time**: 22 min (14:50–15:12)

**On screen** (verbatim):

```text
Experience 2 — Collect Data: 25 to 30 Photos Per Gesture

[DEMO POINTS]
· Hand straight on — then further away, different angle, other hand
· For every photo, give the gesture its "answer name" — the formal word is a LABEL:
  the standard answer for each photo. When it learns, it's checking its answers.

[CLASS NAMES, English only]
scissors  ·  rock  ·  paper

(warning, red left border) HANDS AND OBJECTS ONLY — NO FACES.
Not yours, not anyone's. If a face sneaks in — delete it on the spot.

📝 Write in your workbook — the data collection record: how many per class, what angles / lighting.
```

**Instructor notes** (verbatim): *"Now — teach it your gestures: scissors, rock, paper. For each one, take 25 to 30 photos with your board. (teacher demonstrates, on screen) Watch me — this one, hand straight on. Next, further away. Another, different angle. Another, other hand. — **For every photo, give the gesture its 'answer name':** this is 'rock', this is 'scissors'. That answer name has a formal word — a **label**. It's the standard answer for each photo. When it learns, it's checking its answers. (deliberately demonstrate bad data, don't explain yet) Now a few more — background switched to the window, half a hand, ten shots all at the same angle. Done. Are these photos good? Not saying yet. We'll see. Rule repeated: **hands and objects only — no faces.** Not yours, not anyone's. If a face sneaks in, delete it on the spot."* Chaotic collection (unsure how many / wrong labels) → TA circulation, three questions: *"How many do you have?" "Label correct?" "Changed the angle?"* A student wants to train after only 10 → **let them! Don't say a word** — when it fails later, it's the teaching material (designed contrast). A face gets photographed → TA C watches it get deleted, restates the rule once, no scolding. **Output anchor**: everyone's three-class photo dataset (in the workbook's "data collection record" zone).

---

### Slide 09 | Train + Deploy: Photos Become Experience — Demo guide page

**Type**: Demo guide · **Time**: 10 min (15:12–15:22)

**On screen** (verbatim):

```text
Train + Deploy — You're the Teacher, It's the Student

[FLOW, yellow arrows:]
100+ PHOTOS → click TRAIN → it finds the common ground, stores it as an EXPERIENCE BOOK
→ click DEPLOY → the experience book travels down the USB cable into the board

(quote box, plain English) Training = it turns your photos into "experience":
what do rock photos have in common, what do scissors photos have in common.
Unplug the cable — it still remembers.

(small, footer) Training queues — whoever collected first trains first.
While you wait: what kind of student would my weird photos produce?
```

**Instructor notes** (verbatim): *"Collected enough? Click 'train'. What's it doing? Plain-English version: **it's turning your hundred-plus photos into 'experience'** — what do rock photos have in common, what do scissors photos have in common; it figures that out itself and stores it as an experience book. That process is called **training** — you're the teacher, it's the student. (during the wait) Training queues — whoever collected first trains first. While you wait, think: what kind of student would my weird photos from earlier produce? Trained? Click 'deploy' — the experience book travels down the USB cable into your board. Once it's in, it remembers — unplug the cable, still remembers. Now — show your board a scissors. See if it recognizes its teacher."* Queue jam → TA A batches (collectors first); anyone waiting over 5 minutes goes to the board and sticks a "when I predict it'll get it wrong" sticky (warms up the attribution talk). Platform slow → run the two-track "batch + teacher rescue model": anyone who can't finish trains deploys the teacher's pretrained model, keeps their data, retrains after class (rescue only). A student recognizes nothing → check "did it deploy?" first, then data size — odds are it's the 10-photo student; keep them as discussion material. **Output anchor**: self-trained model deployed on the board; record in md or handwriting (how many classes, how many photos each, how long the wait).

**Assets**: IMG training/deploy interface screenshot (`L5_训练部署.jpg`, V3 deck pages 32–33; optional — live demo is primary).

---

### Slide 10 | The Swap Test: Does It Know Your Neighbor's Hand? — Rules page

**Type**: Rules · **Time**: 9 min (15:22–15:31)

**On screen** (verbatim):

```text
The Swap Test — Swap Boards With Your Neighbor

[RULES, large]
Only scissors-rock-paper — and vary it: further, faster, other hand
Recognized = 1 point
Got it wrong = …write it down too. That's treasure.
We'll tally the class failure rate in a minute.

(reminder) "Breaking" is limited to showing it things —
no touching hardware, no covering the lens, no pulling cables.

📝 Write in your workbook — under which move did your neighbor's model fail?
```

**Instructor notes** (verbatim): *"Now the fun part: **swap boards with your neighbor.** Your model — does it recognize their hand? Rules: only scissors-rock-paper, and vary it — further, faster, other hand. Recognized = 1 point. Got it wrong = …write it down too. That's treasure. We'll tally the class failure rate in a minute."* ⭐ **Widespread failure is designed, not an accident** — the teacher never "rescues": only *"Write it down — under which move did your model fail?"* Rare class with too-high accuracy → the teacher becomes the trap: gloved hand, toy scissors, back of hand to the lens — manufacture attribution material. The test turns into roughhousing → boards back to owners; switch to "test your own, in three different lighting conditions." **Output anchor**: swap-test score + the specific failing situation noted.

---

### Slide 11 | The Attribution: It's Not Dumb — You Taught It Too Little — Core concept (landing page)

**Type**: Core concept (landing) · **Time**: 10 min (15:31–15:41)

**On screen** (verbatim):

```text
The Attribution — It's Not Dumb. You Taught It Too Little.

(small, top) Failure-rate tally — hands up if your model got it wrong more than 3 times.

(landing line, extra-large, bold) IT'S NOT DUMB.
YOU TAUGHT IT TOO LITTLE.

(one more line) Want it smarter? Feed it more — and more different — examples.

(loop-back line) For an AI that recognizes things, the examples ARE everything.
Telling it isn't enough. You have to show it.

📝 One sticky per person: "my model gets it wrong when ___"
— specific beats vague: "low light" ✓, "it's not accurate" ✗. Stick it on the left side of the board.
```

**Instructor notes** (verbatim): *"Failure-rate tally — hands up if your model got it wrong more than 3 times. (a sea of hands) Congratulations. You just earned today's most important textbook. One sticky per person: write **when your model gets it wrong** — the more specific the better. 'Low light' passes. 'It's not accurate' doesn't. Stick it on the left side of the board. (read the stickies, group them) Light changed, background changed, someone else's hand, only a dozen photos… see the pattern? **It's not dumb. You taught it too little.** Want it smarter? Feed it more, more *different* examples. Remember my weird photos from before class — one angle only, messy background? A student taught by that teacher only knows how to sit in the front row. One loop back: you've learned that talking to AI needs examples. Today you saw it — for an AI that recognizes things, **the examples ARE everything.** Telling it isn't enough. You have to show it."* If it goes cold → call on someone who raised their hand: *"Which move got it wrong for you?"* Two or three of those warms it up. A student writes "the board is dumb" → throw it back to the class: *"Same board — why did it recognize YOUR rock?"* — let them answer "the data." **Output anchor**: the attribution sticky up on the board + one line in the log.

---

### Slide 12 | First-Half Log: My Model Gets It Wrong When ___ — Operation guide page

**Type**: Operation guide · **Time**: 5 min (15:41–15:46)

**On screen** (verbatim):

```text
First-Half Log — Four Lines, As Usual

· Today I made ___  (today: I trained a model that recognizes rock-paper-scissors)
· I got stuck at ___  (required today: WHEN DOES MY MODEL GET IT WRONG?)
· Then ___
· Next time I want ___  (e.g. feed it more data / change the angles)

📝 Photograph your board — hands and board only.
Leave the model on the board — second half, it does something after it recognizes.
```

**Instructor notes** (verbatim): *"Log time — four lines as usual. For 'did', write: I trained a model that recognizes rock-paper-scissors. 'Stuck at' is required today: **when does my model get it wrong.** Leave the model on the board — second half, it does something after it recognizes."* **Output anchor**: the four-line log in the workbook (md or handwriting).

---

### Slide 13 | Sensor Output: Where Does the Result Go? — Core concept

**Type**: Core concept · **Time**: 14 min (15:46–16:00)

**On screen** (verbatim):

```text
Sensor Output — Where Does the Result Go?

[CONCEPT] A deployed XIAO is a VISION AI SENSOR —
like the light sensor and buttons you've used — except what it "senses" is a picture.

[LANGUAGES, three cards + one greyed]
UART — the serial port: when it's connected to a computer,
the recognition results you see on screen travel over it  ★ today's one
I2C — boards talking to boards
SPI — the same idea, a few jumper wires: "eyes" and "hands" split apart
WiFi/MQTT — the networking lessons, later

(quote box) recognized → output → something else catches it and does the work.
The build in a minute is making that output light your LED and ring your buzzer.
```

**Instructor notes** (verbatim): *"First half done. Your board is no longer an ordinary board — a deployed XIAO is a **vision AI sensor.** Just like the light sensor and the buttons you've used — except what it 'senses' is a picture. Once a sensor recognizes something, the result needs an exit. It speaks several 'languages': **UART** — the serial port; when it's connected to a computer, the recognition results you see on screen travel over it. **I2C** and **SPI** — for boards talking to boards. **WiFi/MQTT** — we play with that in the networking lessons, later. Look — two boards joined by I2C: this one watches, that one works. SPI's the same idea — a few jumper wires, and the 'eyes' and the 'hands' split apart. We don't run two boards today — but hold onto this feeling: **recognized → output → something else catches it and does the work.** The build in a minute is making that output light your LED and ring your buzzer."* "What's the difference between I2C and SPI?" → *"Both are ways boards talk to each other — you don't need to tell them apart today. Remember UART — the serial port — that's what we use in a minute."* Pure cognition, no hands-on; a student itching to wire → *"Note it down. Today's output runs through the serial port; two-board play is a later lesson."*

**Assets**: IMG serial-port output screenshot (recognition result + confidence on screen; optional — live demo is primary).

---

### Slide 14 | The Brief: Recognize It → Make It Move — Task page

**Type**: Task · **Time**: 10 min (16:00–16:10)

**On screen** (verbatim):

```text
Second-Half Brief — Recognize It → Make It Move

[THE RULE, large, yellow arrow between]
RECOGNIZE IT  →  MAKE IT MOVE

[MY DEMO] scissors → red light on · rock → buzzer beeps · paper → all off
(that's my demo — your rules are yours to set)

[MEANING-SWAP] scissors = my sister's secret signal — recognized, play the song she likes.
Your model, your call.

[OUTPUT HARDWARE] LED + buzzer: every table's base. Servo + light strip: two per table, first-come-first-served.

(expectation line, small) It "thinks" half a second slower — normal.
Today: it watches, and takes care of this one thing.
```

**Instructor notes** (verbatim): *"Second-half brief, one sentence: **recognize it → make it move.** Scissors → red light on. Rock → buzzer beeps. Paper → all off. That's my demo — your rules are yours to set. Change the meaning if you want: scissors = my sister's secret signal — recognized, play the song she likes. Your model, your call. (hand out output hardware) Every table gets LED and buzzer as base pieces. Servo and light strip: only two per table, first-come-first-served. Didn't grab one? Don't sweat it — making the light and the buzzer do something interesting is just as much of a skill. Set expectations now: it 'thinks' on a thumbnail-sized board — **half a second of lag is normal.** Making it fast and smart enough to run a building is a later lesson. Today: it watches, and takes care of this one thing."* *"I want it to recognize my Gundam model and fire!"* → *"Great idea — put it on the 'later' list. Today, use what your board already knows — rock-paper-scissors. That recognition step already won; don't re-fight it."* Actuator argument → first-come-first-served + the agreement *"if nobody's using it after 16:20, it rotates."*

---

### Slide 15 | Three-Box Sheet: One New Column — "What If It Can't Recognize It?" — Operation step page — **RED (2/2)**

**Type**: Operation step · **Time**: 10 min (16:10–16:20)

**On screen** (verbatim):

```text
Three-Box Sheet — One New Member Today

[THREE BOXES, horizontal]
SENSE — the class the camera recognizes (scissors / rock / paper)
LOGIC — recognized what, do what
OUTPUT — the light, the buzzer, or the servo you grabbed

[NEW COLUMN, red left border, hanging off the LOGIC box]
WHAT IF IT CAN'T RECOGNIZE IT — OR ISN'T SURE?
THIS COLUMN IS REQUIRED. Writing "do nothing" is a valid answer —
but it has to be YOUR decision, not its accident.

(small, footer) It reports how confident it is — a percentage (its CONFIDENCE).
Your rule: below 70% confidence, treat it as not recognized.
Show a TA your three boxes before you build.
```

**Instructor notes** (verbatim): *"Before building — the usual three-box sheet: sense, logic, output. Today's three boxes have a new member. **Sense:** the class the camera recognizes (scissors / rock / paper). **Logic:** recognized what, do what. **Output:** the light, the buzzer, or the servo you grabbed. The new member lives in the logic box, one more column: **'What if it can't recognize it — or isn't sure?'** Earlier projects never had this situation — a button is either pressed or not. But 'seeing' hesitates: it might say 'I'm not sure if that's scissors or paper.' This column must be filled. Writing 'do nothing' is a valid answer — but it has to be *your* decision, not its accident."* The "can't recognize" column left blank → send it back: *"That column is today's required question."* "How sure is sure?" → good question, one line: *"Every time, it reports how confident it is — a percentage. That number is its **confidence**. Your rule: below 70% confidence, treat it as not recognized."* **Output anchor**: the three-box sheet (vision edition), with the "can't recognize" column filled; shown to a TA before building.

---

### Slide 16 | The Vision-to-Action Prompt: One Class Running, Then Extend — Sentence page (stand-still)

**Type**: Sentence page (stand-still) · **Time**: 21 min (16:20–16:41)

**On screen** (verbatim):

```text
Vision → Action — You're the Boss of Two AIs

(role line, yellow light fill) The model SenseCraft taught handles "recognize" —
the program Codecraft runs handles "do".

(monospace instruction card, large)
My XIAO ESP32S3 Sense has an image-classification model deployed on it
that recognizes three classes: scissors, rock, paper.
The recognition result and its confidence come out of the serial port.
Please write me a program:
1. When the result is "scissors" AND confidence is above 70% → turn on the LED;
2. When the result is "rock" AND confidence is above 70% → make the buzzer beep once;
3. When the result is "paper", or confidence is below 70% → turn everything off
   (this is the "what if it can't recognize it" handling).
Implement only item 1 first. Once it runs, I'll ask for items 2 and 3.

(reminder, yellow left border) The old discipline: one thing at a time.
Item 1 running, then items 2 and 3. Error? Paste the error back — it fixes it.

(small, footer) Left tab: SenseCraft. Right tab: Codecraft. Don't merge them. Class names stay English.
```

**Instructor notes** (verbatim, first 10 min demo, Codecraft on screen): *"Watch how I plug the 'recognition result' into a conversation. Note this prompt — you're now the **boss of two AIs**: the one SenseCraft taught handles 'recognize', the one Codecraft runs handles 'do'. (type on screen, read it line by line — or point at this page) See — the old discipline: **one thing at a time.** Get 'scissors → light on' running first, then rock, then paper. In 30 minutes I'll call across the room and check your three-box sheets."* ⭐ *"It's slow / doesn't work"* → point back to the expectation-setting: *"Half a second of lag is normal. Actually wrong? Think back to the first half — what makes it wrong? Write that situation down — it's the first item on next lesson's trouble list."* After moving / changing light, everything fails → teach on the spot: *"This is a scenario the data never saw. Quick rescue: back to SenseCraft, re-shoot 10 photos in the current light, retrain ('change the data' route, demo live); OR write on your three-box sheet: 'this model only works at the window desk' — that's a professional answer too."* It works but the action is too weak (a blink you barely see) → upgrade sheet on the board: LED → RGB strip; one beep → rhythm pattern; one servo swing → continuous waving. Lost between the two platforms → *"Left SenseCraft, right Codecraft. Don't merge them."* TAs correct it class-wide. At 16:31, some still have nothing running → TA B hands out the fallback prompt (slide 17); continue from the fallback. **At 16:41, everyone stops and moves to the buffer.** **Output anchor**: working vision-to-action project (≥1 class → ≥1 action); log progress update ("did" = I made my model ___ after recognizing ___).

---

### Slide 17 | Fallback + Error Handling — Operation guide (fast flip, inside the build)

**Type**: Operation guide (fast flip) · **Time**: no separate timing (inserted inside the 16:20–16:41 block)

**On screen** (verbatim):

```text
Not Running? Start With the Board's Own LED

(monospace fallback box, verbatim)
My XIAO ESP32S3 Sense has an image-classification model deployed on it
that recognizes three classes: scissors, rock, paper.
The recognition result comes out of the serial port.
Please write me the simplest program:
when the result is "scissors" → turn on the onboard LED.

[ERROR BOX]
Error? Paste the error back to AI, verbatim.
Image black or blurry? Is the lens film off? → swap the board, don't repair.
Once the fallback runs, extend from there — add the light, the buzzer, the servo.
```

**Instructor notes** (verbatim, used at the 16:31 check): *"Not running yet — raise your hand. TA, start with the fallback prompt. Running? Keep going — extend rock and paper, or upgrade your output."* The fallback does only the onboard LED — no extra wiring: first build confidence, then add the light and buzzer. **Output anchor**: the fallback version running (one class → onboard LED).

---

### Slide 18 | 9 Minutes — Three Exits, Pick One — Task page (big-type, stand-still)

**Type**: Task (big-type, stand-still) · **Time**: 9 min (16:41–16:50)

**On screen** (verbatim):

```text
9
minutes

EXIT 1 · FINISH TO STANDARD (everyone crosses this line)
One recognized class → one action.

EXIT 2 · RUNNING? Try your neighbor's project once.
Then log progress: "I made my model ___ after recognizing ___."

EXIT 3 · SPARE TIME? On the back of your three-box sheet, write
"three scenarios where I'll try to break my own project next lesson."

(small, footer) Not finished? No extensions — TA keeps you on the main build.
The buffer is part of the lesson, not early dismissal.
```

**Instructor notes** — the buffer is **not free time**. Not running yet: TA B concentrates on getting them to "one class → one action" (the acceptance floor). Running: ① try your neighbor's project once; ② log progress; ③ spare time: the "three scenarios" line on the back of the three-box sheet. The teacher: tally acceptance (running / total), fill the reflection page sections A and B. **Output anchor (running students)**: the log progress line; the "three scenarios" note for next lesson.

---

### Slide 19 | Today You Touched How AI Gets Made — Core concept (golden-line page)

**Type**: Core concept (golden line) · **Time**: 5 min (16:50–16:55)

**On screen** (verbatim):

```text
Today You Did Two Things Nobody Ever Walked You Through

① You taught a board to know the world with your own hands —
   collecting photos, training a model, deploying it to the board
② You made the knowing decide for you —
   your gesture turns on a light, rings a buzzer

(quote box, yellow light fill) In the whole course, this is the only time
you touch "how AI gets made."
```

**Instructor notes** (verbatim): *"Today you did two things nobody ever walked you through: you taught a board to know the world with your own hands — collecting photos, training a model, deploying it to the board. Then you made the knowing decide for you — your gesture makes a light turn on, a buzzer ring. In the whole course, this is the only time you touch 'how AI gets made.'"*

---

### Slide 20 | Bring Your Model Back + Pack-Up — Call-to-action

**Type**: Call-to-action · **Time**: 5 min (16:55–17:00)

**On screen** (verbatim):

```text
Next Time — Bring Your Model Back

First, AI becomes your tester and hands you a TROUBLE LIST.
Then you and your neighbor try to wreck each other's projects.
Today you said "not recognized → do nothing."
Next time you'll answer: that decision — accept or reject?

[PACK-UP LIST]
· Board into the bag with your name on it · output hardware back in place
· Three-box sheet + log go with you (md or handwriting — hand to the teacher after class: link or photo)
```

**Instructor notes** (verbatim): *"Next lesson preview: bring your model back. First, AI becomes your tester and hands you a trouble list; then you and your neighbor try to wreck each other's projects. Today you said 'not recognized → do nothing.' Next time you'll answer: that decision — accept or reject? Boards into the bag with your name on it. Output hardware back in place. Three-box sheet and log go with you (md or handwriting — hand to the teacher after class: link or photo)."* "Can I take my model home?" → *"The model lives in the board, and the board lives here. Missing it? Read your log — first thing next lesson, we use it."*

---

## Asset & Placeholder Checklist (from the CN plan + V3 deck, localized notes)

| Slide | Asset | Size | Status |
| --- | --- | --- | --- |
| 01 / 04 | XIAO thumb-size photo `L5_XIAO拇指对比.jpg` (camera up, thumb for scale; shared by cover / anatomy) | 420×360 | To photograph at rehearsal |
| 04 | XIAO family chart + anatomy diagram (from V3 deck pages 08–09 — re-crop, English labels) | 640×360 | Reuse from V3 deck |
| 06 | Sign-in demo screenshot `L5_签到SIGNED-IN.jpg` (SIGNED IN banner; 1 wrong-recognition backup) | 400×300 | To capture at rehearsal |
| 07 | AI Blink trigger-config screenshot (V3 deck pages 13–22 — trigger screen with LED spot) | 400×300 | Reuse from V3 deck |
| 08 | Collection sample wall screenshot (V3 deck — class names in English) | 400×300 | Reuse from V3 deck (optional) |
| 09 | Training/deploy interface screenshot `L5_训练部署.jpg` (optional — live demo is primary) | 400×260 | To capture at rehearsal (optional) |
| 13 | Serial-port output screenshot (recognition result + confidence; optional) | 400×260 | To capture at rehearsal (optional) |
| 14 / 16 | Vision-to-action result photo (scissors → LED on, optional corner shot) | 400×300 | To photograph at rehearsal (optional) |

**Downgrade**: sign-in demo screenshot missing → slide 06 keeps only the three short lines (the live demo carries the page); XIAO photos missing → line-outline art + the instructor holds the real unit; all screenshots missing (extreme case) → the deck stands as pure text — concept and rules pages carry this lesson; the big screen shows "what to look at / what to say", the detail lives in the instructor's hands and mouth; **the training-flow screenshots are backups only — training must be hands-on, never a teacher demo (the iron law lives in the instructor, not the slide).**

---

## Backup & Downgrade

- SenseCraft down on the day → run the three gates (Teacher's Guide 4.1: T-7 / on-the-day / first-15-min); the 15-minute rule; **downgrade ≠ demo version — training must be hands-on, that's today's iron law** (total offline = Lesson 5 slides to next week; today becomes "combined creation").
- Slide 06 sign-in demo fails live → the pre-recorded demo video (Rehearsal-1 backup); no badge → project any high-contrast stable image.
- Slide 07 AI Blink trigger config fails → pure demo: students only get "deployed + recognized"; short on time → trigger config = teacher demo.
- Slide 08 collection collapses entirely → import a teacher pre-collected dataset (rescue only); two students share one board (gestures in turn).
- Slide 09 train queue jam / platform slow → batch training (collectors first); teacher rescue model for those who can't finish (keeps data, retrains after class — rescue only).
- Slide 10 swap test turns into roughhousing → boards back to owners; "test your own, in three different lighting conditions."
- Slide 13 sensor protocols overrunning → UART only (7 min), verbal pass on the rest; cut entirely if needed — doesn't affect the build.
- Slide 16 build collapses → the fallback prompt (slide 17) + onboard LED = acceptance; **at 16:41 everyone stops and moves to the buffer**; collapse ladder: acceptance = "one recognized class triggers one action."
- Slide 18 buffer turns into free time → set the exits at the start; someone wandering → hand them an exit.
- Offline mid-class → phone hotspot first (Gate 2); still down 15 min in → on-the-spot downgrade (Gate 3), never the demo version.

---

## Localization Slots

| Slot | Default | Swap in |
| --- | --- | --- |
| Slide 02 concept examples | [Tesla 360° / panda watch / hummingbird feeder] | local "machine seeing" stories: traffic cameras, factory sorting, campus security — keep it to three quick lines each |
| Slide 06 sign-in target | [school badge/logo on screen] | the course mark or a big English word (CHAIHUO / M0) — anything high-contrast and stable, projected, not printed |
| Slide 08 collection scenes | [hand straight on / further / angle / other hand] | local gesture meanings are fine in spoken lines — **keep class names English: scissors / rock / paper** |
| Slide 14 meaning-swap example | [scissors = my sister's secret signal → play the song she likes] | your students' real scenes: a piano-practice cue, a vocab-flashcard timer, a jump-rope counter — the recognized class is still scissors/rock/paper |
| Slide 16 build upgrade sheet | [LED → RGB strip; one beep → rhythm; one swing → continuous] | keep upgrades output-based; on-screen text stays English |
| Slide 20 next-lesson preview | [AI hands you a trouble list; wreck each other's projects] | don't swap the activity (Lesson 6's design is set) — localize the wording of "wreck each other's projects" if it sounds harsh: "try to break each other's projects" |

---

_English PPT Plan · Lesson 5 · Teach Your Hardware to See v1 ｜ 2026-08-26 ｜ Source: CN deck plan v2 as structural archive (v2.1/v2.2 noted; v2.3 47-page user hand-edit = CN final form) + EN Teacher's Guide L05 v1 (2026-08-25, based on CN 讲师版 v3) ｜ Terms locked to EN Glossary + EN Teacher's Guide L05 ｜ Red count: 2 (slides 08 and 15) ｜ Note: this EN deck is a brand rebuild from the V3 teaching structure, not a copy of the 47-page CN file — the Session Map of Teacher's Guide L05 maps each beat to V3 page ranges for asset sourcing ｜ Next: build the EN .pptx from this plan (brand rebuild, Chaihuo spec; re-capture SenseCraft/Codecraft UI screenshots in English where possible)_
