# Lesson 5 · Teach Your Hardware to "See" (Student Workbook)

_Chaihuo Maker Academy · M0 — Zero-to-Hero Smart Hardware_

---

## 1. What You Walk Out With

Last lesson you commanded an AI team and built a Pomodoro timer. Today, your hardware learns a brand-new skill: **seeing.** You won't write it a single instruction — you show it photos, and it learns to recognize on its own.

By the end of class, you'll have four things:

1. **A vision model you trained yourself** — collected, trained, and deployed to the board by your own hands; it recognizes your own scissors, rock, and paper;
2. **An attribution record** — "under what conditions my model gets it wrong," written in your log; the more specific, the better;
3. **A three-box sheet (vision-to-action edition)** — sense, logic, output — with a new field in the logic box: "what to do when it can't recognize";
4. **A working vision-to-action work** — recognize ≥1 gesture → trigger ≥1 action (light on, buzzer sounds).

How this class works: **teacher guidance + this document + AI conversation → your own work and your own record.** Everything the teacher asks you to write goes here (in an md doc if you're on a computer, on paper if you're handwriting) — it's handed in at the end of class, and next lesson's very first thing uses your model.

---

## 2. Before Class: Hand In Last Lesson's Work

md doc → send the teacher the link; handwriting → send the teacher a photo. Not handed in? It gets noted — catch up before you leave today.

**Write here — check the box:**

- ☐ My Pomodoro timer record is handed in (md link / photo of handwriting)

---

## 3. Meet the New Gear: XIAO ESP32S3 Sense

Your third board. The first one, the Grove kit, is **skin** (it feels hot, cold, motion); the second one, the Wio, is the **face** (it has a screen and buttons); this thumb-sized little board is the **eyes** — it carries a camera, plus a built-in microphone: it can see and it can hear.

| Spec | Details |
| --- | --- |
| Size | Thumb-sized (21×17.5mm) |
| Camera | OV2640, 2 megapixels |
| Microphone | Digital mic, can record |
| Storage | microSD card slot |
| Wireless | WiFi + Bluetooth |
| AI capability | The AI model runs on the board itself — **no internet needed** |

The teacher walked you around the anatomy diagram in class. No need to memorize it all — just recognize three things: the **camera** (its eyes), the **reset button**, and the **boot button** (needed for flashing).

**Three strengths:** tiny — it fits anywhere; cheap — about the price of a lunch; AI runs on the board — no internet, and your photos never leave that board.

**Three weaknesses** (you'll hit all of them today): small compute — it "thinks" with half a second of lag, that's normal; it makes mistakes — which is why "what to do when it can't recognize" is part of your design; no screen — you rely on lights, buzzers, or a computer display.

One line to remember: **a small computer does small jobs** — having it watch over this one thing for you is exactly the right size of work for it.

---

## 4. Experience 1: The AI Blink — start with someone else's training

Today's armory: **sensecraft.seeed.cc/ai** (SenseCraft AI — the place where you teach boards to recognize things).

Step one: no photos, no training — first load a **model someone else already trained** onto your board, and see what "recognizing" looks like:

1. Connect the XIAO to your computer with the USB-C cable (both ends all the way in);
2. Open SenseCraft, click "Connect Device," and see your board's name;
3. Pick a pretrained model (face detection), click "Deploy," and wait for the flash to finish;
4. Configure the "trigger": **face recognized → the board's LED lights up**;
5. Aim at the target and verify — it lights!

**Success marker:** target recognized, LED on. The one doing the recognizing isn't your home WiFi, and it isn't some distant server — **it's the board in your hand, by itself.** Unplug the cable, kill the network — it still recognizes.

> The teacher also demoed the advanced version: Grove expansion board plus an LED strip — target recognized, the strip lights up directly. **Not one line of code written** — the vision model driving peripherals straight away. That's today's命题 in preview: recognize it → make it move.

Someone else's training book works great — **but it doesn't know you.** Next step: train one of your own.

**Write here:**

- ☐ My board is connected, the ready-made model deployed, target recognized, LED on

---

## 5. Experience 2: Teach It Your Hand Gestures

Now, teach it your gestures: scissors, rock, paper.

### Step 1: Set up the station (the teacher walks you through)

Pick the board (XIAO ESP32S3 Sense) → pick the serial port → name your three classes. **Class names in English:** `scissors`, `rock`, `paper` (what shows on screen never gambles on Chinese rendering).

### Step 2: Collect — for each class, take 25 to 30 photos

- Vary your shots: hand straight-on, a bit farther away, from another angle, with the other hand;
- For every photo, pick the right "answer name" — its learning is exactly answer-checking. The formal name for the answer name is the **label**: the standard answer for each photo.

> ⛔ **The rule: hands and objects only — no faces.** Not yours, not anyone else's. A face gets in the frame — delete it on the spot.

### Step 3: Train + deploy

Click "Train" — it turns your hundred-odd photos into "experience": what rocks have in common, what scissors have in common — it summarizes by itself and saves it all as a "training book." Trained? Click "Deploy," and it moves down the USB cable into your board. Unplug it and it still remembers.

> Training queues up — first done shooting, first to train. While you wait, one question: **that pile of "weird photos" the teacher showed before class (single angle, messy background) — what kind of student would those teach?**

After deploying successfully, take a photo of "the model running on my board," and note down:

- I trained ___ classes, ___ photos each, and waited about ___ minutes for training.

### Step 4: Swap and cross-test — does your model recognize someone else's hand?

Swap boards with your neighbor. Rules:

1. Scissors, rock, paper only — vary how you throw: farther away, faster, other hand;
2. One correct recognition = 1 point;
3. **One wrong recognition… write that down too — that's treasure** (under which throw it got it wrong).

> Sabotage is limited to "what you show it" — no touching the hardware, no covering the lens, no unplugging.

### Step 5: Attribution — why did it get it wrong

The whole class tallies up the "wreck rate." Then everyone writes one sticky note for the whiteboard:

> **My model gets it wrong when ______.**
> ("In dim light it fails" ✅ passes; "it's inaccurate" ❌ fails — the more specific, the better.)

The landing line: **it's not dumb — you taught it too little.** Want it smarter? Feed it more, and more varied, examples. For an AI that recognizes things, examples are everything — saying so doesn't help; you have to show it.

**Write here:**

- ☐ My model recognizes all three of my own gestures
- My model gets it wrong when ______ (copy the exact line you put on the whiteboard)

---

## 6. First-Half Log (four sentences, as usual)

> Made: I trained a model that recognizes scissors, rock, and paper;
> Stuck on (mandatory): my model gets it wrong when ______;
> Then: ______;
> Next time I want: with more data / other angles fed in, ______.

Leave the model on the board, untouched — the second half makes it "do something once it recognizes."

---

## 7. Second Half: Recognize It → Make It Move

### First, one concept: your board is already a "vision AI sensor"

A XIAO with a deployed model is a sensor — same as a light sensor, same as a button — except what it "senses" is the picture in front of it. Once it recognizes something, the result needs an exit:

- **Serial port (UART)** — what you see on screen when it's plugged into the computer runs through it (today's link-up uses exactly this);
- **I2C, SPI** — how boards talk to other boards (the two-board game, in a later lesson);
- WiFi/MQTT — for the internet lesson.

Remember this feeling: **recognize → output → some other device catches it and does the work.**

### The brief

Scissors recognized → red LED on; rock recognized → buzzer sounds; paper recognized → everything off — that's the teacher's demo, **your rules are yours to make.** Want different meanings? Go ahead: scissors = my little sister's secret signal — recognized, it plays her favorite song. Your model, your call.

Output pieces: LED + buzzer for everyone; servos / LED strips are two per table, first come first served. It "thinks" with half a second of lag — normal.

### The three-box sheet (with a new member today)

| Box | What goes in | Your answer |
| --- | --- | --- |
| Sense | The class the camera recognized (scissors / rock / paper) | |
| Logic | Which class recognized → do what | |
| Output | Light, buzzer, or the servo you grabbed | |
| ⭐ Can't recognize | **When it can't recognize, or isn't sure — what happens?** | |

The new member is a mandatory question. "Do nothing" counts as an answer — but it must be **your decision**, not its accident.

> Every recognition comes with a "how sure am I" percentage (the number is called **confidence**) — you can set a rule: below 70%, treat it as "can't recognize." Fill the sheet in, show a TA, then start building.

### The vision-to-action prompt (copy it, send it to Codecraft)

```text
My XIAO ESP32S3 Sense has an image-classification model deployed on it
that recognizes three classes: scissors, rock, paper.
The recognition result and its confidence come out of the serial port.
Please write me a program:
1. When the result is "scissors" AND confidence is above 70% → turn on the LED;
2. When the result is "rock" AND confidence is above 70% → make the buzzer beep once;
3. When the result is "paper", or confidence is below 70% → turn everything off
   (this is the "what if it can't recognize it" handling).
Implement only item 1 first. Once it runs, I'll ask for items 2 and 3.
```

**Old discipline: one thing at a time** — item 1 runs first; only then send items 2 and 3. Never all three at once. Got an error? Paste the error message back verbatim and let it fix its own code. Upload not responding? The mantra: **slide it.** (slide the side switch once, slide again, into flash mode).

SenseCraft on the left, Codecraft on the right — keep the two tabs separate. Class names stay English.

### Nothing running at all? The fallback prompt

```text
My XIAO ESP32S3 Sense has an image-classification model deployed on it
that recognizes three classes: scissors, rock, paper.
The recognition result comes out of the serial port.
Please write me the simplest program:
when the result is "scissors" → turn on the onboard LED.
```

The fallback uses only the onboard LED — no extra wiring — get it running to build confidence, then wire on the lights and buzzers.

**Write here:**

- ☐ My three-box sheet is filled in (including the "can't recognize" box), a TA has seen it
- ☐ It runs: recognized ______ → ______ (today's acceptance line)
- Three scenarios I'd use to sabotage my own work (on the back of the sheet, if you have room): ______

---

## 8. Before You Leave: Delivery Checklist

- Board in the bag with your name on it; output pieces back in place;
- Three-box sheet + log go with you — md → send the link / handwriting → photo — hand in to the teacher after class;
- Collection record, wrong-recognition attribution, link-up record — the teacher notes it all when it's in.

Today you did two things nobody had ever walked you through: **you taught a board to recognize the world with your own hands** (collect photos, train the model, deploy to the board), and **you let its recognition make decisions for you** (it recognizes your gesture — light on, buzzer sounds). Only once in this whole course do you touch "how AI gets made." This is that once.

**Next lesson preview:** bring your model back — first, AI plays the tester and writes you a "sabotage list"; then you and your neighbor try to wreck each other's projects to the fullest. Today you said "can't recognize → do nothing" — next lesson you'll have to answer, about that decision: **Accept or Reject?**

---

## 9. Bonus (Appendix): Make the Hardware Take Orders — Codecraft Output-Piece Practice

> Matches the deck appendix, pages A·01–A·23. The main session taught the board to "**recognize**"; this bonus teaches it to "**move**" — lights, buzzers, fans: its hands. These output-piece fundamentals feed straight into the Final Project.
> One tool only: **Codecraft** (open codecraft.seeed.cc in a browser — nothing to install) — you speak human to it, it writes the code for you.

### First, know your whole kit

Kit family photo against the real thing, name by name: main board, expansion board, camera, LED, buzzer, fan, knob, Grove cables — **nothing named, no work started.**

### Wiring in three steps + the mantra

1. Unplug the camera; 2. Insert the long side of the pin header into the little holes; 3. Line it up with the base below, and press down firmly.

- **The mantra:** D1 = the little LED, the port on the upper left.
- **Power check:** Type-C into the computer → watch the charging light on the board → light on = power is good; no light, swap the cable first.

> Why wiring first? Once the model recognizes something, the commands have to travel down these wires to reach the lights and buzzers — wire it wrong, and everything after is wasted work.

### Can't connect? Check in this order

1. The cable — a data-capable USB cable, not a charge-only one;
2. The connection — cable seated, right port, expansion board pressed all the way down;
3. The browser — Chrome / Edge, current version, click "Allow" on the serial popup;
4. The board model — in Codecraft you picked XIAO ESP32S3.

> **Not fixed in 2 minutes: swap cable → swap board → find a TA.** No on-the-spot repair — the time goes to making things.

### Codecraft onboarding in four steps

① Pick the board: XIAO ESP32S3 → ② connect the serial port (click "Allow" on the popup) → ③ state what you want in the chat box → ④ generate → compile → flash.

**Success marker:** the board reacts the way you said — your first "light it up" achieved. You're the director; it's the crew.

### Three tasks: light → buzzer → fan (one new piece of hardware per step)

> **One rule only: add new requirements in the SAME conversation — command AI to iterate, never restart from scratch.**

| Task | Why we do it | Your instruction | Success marker |
| --- | --- | --- | --- |
| 1 · Light the LED | The light is the cheapest, most honest piece — right program or wrong, you see it at a glance | LED module into D1 (the small tab is + → into the + row; the big tab is − → into D1); tell Codecraft "light the LED on D1" | The D1 LED does exactly what you said — on / off |
| 2 · Add the buzzer | Lights only show; buzzers sound — for when you're not looking | "Buzzer + LED in sync: the buzzer and the LED sound/stop together" | LED on + buzzer sounding; LED off + buzzer silent, in sync |
| 3 · Drive the fan | From "lit" and "loud" to "spinning" — the first step where a signal becomes physical motion | "In the same project, add a feature that makes the fan spin" | All 3 pieces working at once: LED steady on + buzzer every 2 seconds + fan randomly on/off |

> Fan spinning slowly or stuttering? It's a 5V design running on 3.3V — weak torque. **A power issue, not a code issue. It spins = task complete.**

### The final challenge: knob speed control (sense → logic → output)

Everything before, you ordered it to move; this time it gets "feelings" — the knob is the input, the fan is the output: together, the complete three-box loop.

- **Wiring:** knob sensor via a Grove cable into port **A0** on the expansion board; full wiring: D1 = fan, D2 = buzzer, A0 = knob.
- **Success marker:** turn the knob → the fan's speed follows, from stop to full; meanwhile the yellow light still blinks and the buzzer still sounds every 2 seconds.

### Advanced Debug guide

- **Fan hums but won't spin:** low PWM output + 3.3V power isn't enough to beat static friction — give the blade a gentle nudge.
- **Code errors:** some old ESP32 support packages don't have the standard `analogWrite` function — `ledcWrite` is the replacement. Don't memorize it — **paste the error back to Codecraft verbatim** and let it fix it.
- **The vibe of it:** an error isn't a failure — it's the next prompt for AI. Copy it over; it corrects itself and re-flashes.

### Bonus delivery checklist

- ☐ My Codecraft project is saved to my account (it follows the account — you can keep working on it at home)
- ☐ Hardware back in place: board, expansion board, output pieces in the bag with my name
- ☐ I saw all three tasks' success markers with my own eyes
- One idea I want to build with output pieces (one line): ______

---

## Appendix: Key Links

| Resource | Link |
| --- | --- |
| SenseCraft AI platform | https://sensecraft.seeed.cc/ai |
| XIAO ESP32S3 Sense Wiki | https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/ |
| Codecraft platform | https://codecraft.seeed.cc |

_Chaihuo Maker Academy M0 · Student Workbook v1 (EN) ｜ 2026-08-26_

_Derivation note: localized from the Chinese student workbook v3 (M0_学员文档_CFG-5_第5课_教硬件学会看_v3.md) — structure mirrored 1:1 including the Section 9 bonus appendix (aligned to the V3 deck, 47 main pages + A·01–A·23). Verbatim prompts (vision-to-action, fallback) copied word-for-word from the English teacher guide M0_EN_TeacherGuide_CFG-5_Lesson05_TeachYourHardwareToSee_v1.md Section 6. Terminology per teacher guide localization notes: "you show it, it learns" / attribution line "it's not dumb — you taught it too little" / "hands and objects only — no faces" / "half a second of lag is normal" / vision-to-action / confidence / label. Chinese wiki links dropped; English wiki kept. Localization: "妹妹的暗号" → "my little sister's secret signal"; "一顿午饭钱" → "about the price of a lunch"._
