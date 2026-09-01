# Teacher's Guide ｜ Lesson 5 · Teach Your Hardware to See

_XIAO ESP32S3 Sense · Edge AI Vision Board ｜ Chaihuo Maker Academy · M0 Hardware Foundation · Smart Hardware Fundamentals ｜ 10-session term ｜ 3 hours (no scheduled break)_

> **Source:** 中文版 v3（M0_教师课件_CFG-5_第5课_教硬件学会看_v3.md，2026-08-05，含附录加餐使用说明）
> **Localized edition** — same blocks, same minutes, same teaching intent; classroom language rewritten for an English-speaking teacher to pick up and teach from.

---

## The one-sentence brief

Today is a **"new AI + new hardware"** combination session. First half: every student gets a thumb-sized board with a camera — the **XIAO ESP32S3 Sense** — and, on **SenseCraft AI**, hand-trains an image-classification model that recognizes **rock-paper-scissors** gestures and deploys it onto the board. Second half: the recognition result **drives hardware** — rock turns on an LED, scissors makes the buzzer sound. The core experience stays the same line: **teacher guidance + student workbook + AI → the student's own conclusions and results.** Every block's output lands in the student's own record — an online md doc if possible, handwriting in a notebook if not.

Students produce **four things**:

1. **A self-trained vision model** — collected, trained, and deployed by their own hands; recognizes their own three gestures;
2. **One attribution note** — "my model gets it wrong when ___", written in the log, the more specific the better;
3. **One three-box sheet (vision edition)** — sense (what the camera recognizes) / logic (what to do for each class) / output (light / buzzer / servo), with one extra column in the logic box: **"what if it can't recognize it?"**;
4. **One working vision-to-action project** — ≥1 recognized class triggers ≥1 action, recorded in md or handwriting.

The session runs in two big halves: **First half · teach your hardware to see** (~106 min) → **Second half · make seeing turn into action** (~64 min) → **buffer** (9 min) → **close** (10 min). Students use the bathroom on their own during hands-on time.

**Today's iron law: training must be hands-on.** If the network collapses, use the whole-lesson downgrade plan — but **never** switch to "watch the teacher demo" version. A student watching training on a screen from across the room means this lesson didn't happen for them.

---

## 🎯 Learning Objectives

*By the end of this session, students will be able to…*

1. **Explain** how a vision model learns, in plain words: photos in, experience out — and why "you show it, it learns" differs from "you tell it, it builds" (*Bloom: Explain*).
2. **Train and deploy** a three-class image model by hand — collect data, label it, train, deploy to the board, and test it (*Bloom: Apply*).
3. **Diagnose** why their model makes mistakes and write a specific attribution ("it fails in low light" ✓, "it's not accurate" ✗) (*Bloom: Analyze*).
4. **Build** a vision-to-action project: one recognized class triggers at least one output, with an explicit "what if it can't recognize it" decision (*Bloom: Create*).

---

## Page One — read this before class starts

### What today produces

1. **A self-trained vision model** — your own three gestures, recognized on your own board, no internet needed;
2. **One attribution note** — the exact situation where your model fails, in your log;
3. **One three-box sheet (vision edition)** — sense / logic / output, plus the "what if it can't recognize it?" column;
4. **A working vision-to-action project** — ≥1 recognized class → ≥1 action, recorded in md or handwriting.

### Three things you need to do

1. **Follow the clock.** Every block says how many minutes and what to do.
2. **Read the lines.** Every 🗣️ line is pre-written classroom speech — read it as-is.
3. **Guard the three gates.** SenseCraft is the lifeline of this session: test it at T-7 (one week before), test it again on the day, and the last gate is within the first 15 minutes of class. Each gate has a pre-written action (see 1.1 and 4.1) — no on-the-spot improvisation.

### Three things you do NOT need to do

1. **You don't need to write code.** AI writes it all. The second-half vision-to-action prompt is pre-written for you (Section 6) — read it, students send it.
2. **You don't need to understand machine learning.** "Training", "label", "confidence" get plain-English classroom versions ("teach it", "the answer name", "how sure it is"). The technical words stay in your prep notes.
3. **You don't need to photograph or train for students.** Data is collected and trained by the students themselves. Your roles: demonstrate, keep pace, stick their attribution sticky notes on the board. A wrong recognition is not your problem to fix — it's the teaching material.

### When things go wrong

- **Live demo fails:** switch to the backup screenshot within 30 seconds, per Section 5's speed sheet. **Not an incident — the plan is designed for it.**
- **Student device fails:** swap the device or cable. Don't repair — that's this course's rule.
- **SenseCraft is down:** run the three gates (4.1) — fails at T-7 → swap the lesson; fails on the day → hotspot; still down 15 minutes into class → downgrade on the spot. **Never switch to the demo version.**
- **You're stumped:** smile and say *"Let's ask AI together."*
- One-liner: **swap, cut to backup, ask AI.**

---

## Before Class

### 1.1 A week ahead (incl. the hard SenseCraft gate)

- [ ] ⭐ **SenseCraft network test (hard gate for this lesson):** on a classroom student machine, open https://sensecraft.seeed.cc/ai/home/ and walk the full path: log in → enter a project → see the training button. **If inaccessible → report to the teaching group the same day and start the downgrade plan (4.1): Lessons 5–6 are replaced wholesale; no XIAO, no accounts.** Decide a week ahead — don't gamble live.
- [ ] Also test codecraft.seeed.cc compile-flash end-to-end (both platforms must work; the second half uses Codecraft for vision-to-action).
- [ ] Confirm the student-to-TA ratio is ≤ 6:1.
- [ ] Apply for SenseCraft accounts with the institution (one per student, by actual headcount); **pre-create one empty three-class "rock-paper-scissors" project inside each account** — students don't build projects from zero on the spot.
- [ ] Pre-run the full flow yourself (1.3), and save: ① your own trained RPS model (rescue model); ② a sign-in demo model trained on the school badge/logo, deployed on the teacher machine.
- [ ] **Day-before reminder** to the class group (copy-paste): *"Next session your hardware learns a new skill — to see. Bring the records of your earlier projects — md link or a photo is fine. Laptop as usual."*

### 1.2 On the day (arrive ~1 hour early)

One person needs ~60 minutes — **arrive 1 hour early**. With a TA: the TA does the device check and table setup; you do the screen and the 1.3 rehearsals. If time is really tight, **Rehearsal 3 (the full training flow) is mandatory**; cut the rest.

- [ ] ⭐ **Test https://sensecraft.seeed.cc/ai/home/ again** (once on a student machine, once on the teacher machine). Down → phone hotspot first; not recovered within 15 minutes → run the 4.1 downgrade. **Don't wait, don't gamble, don't switch to the demo version.**
- [ ] XIAO ESP32S3 Sense: one per student + a few spares. For each: **peel off the lens protective film** (failure point #1), plug into the computer, take one test photo — confirm the image isn't black or blurry.
- [ ] Account spot-check: log into a few random accounts; confirm the empty project is there.
- [ ] Cables: by actual headcount + spares (confirm they're data cables, not charging-only).
- [ ] Output hardware on tables: LED/buzzer (Kit A) as base pieces; 40-in-1 actuators (servo / RGB strip) limited to 2 per table, first-come-first-served — scarcity is a feature.
- [ ] Experience-1 demo kit: 1 Grove expansion board + 1 RGB strip (for the teacher's "recognize → drive the peripheral directly" demo); no expansion board → that demo downgrades to verbal + a real photo.
- [ ] Sign-in screen tuned: the badge/logo large on screen (teacher machine or projector); the sign-in model deployed on the teacher machine.
- [ ] Whiteboard split into two zones: the "why does it get it wrong" attribution zone / the left-SenseCraft-right-Codecraft dual-screen marker.
- [ ] Two browser tabs open on every machine: left SenseCraft, right Codecraft (the dual-platform, don't-get-lost rule).
- [ ] Imaging rule written in the whiteboard corner: **hands and objects only — no faces.**
- [ ] Sticky notes ×2 per student (for the attribution discussion) + thick pens.

### 1.3 Rehearsals (allow 40 minutes — play the student first)

One principle: **rehearse as the student.** Every on-screen element must be verified in English / numbers / graphics — never gamble on Chinese rendering.

**Rehearsal 1 ｜ the sign-in demo (used at 14:21)**
On the teacher machine, run the pre-trained model: point the camera at the badge on screen → it shows **SIGNED IN**; point at something else → nothing. Also rehearse the "it got it wrong — now what" rescue line.
Backup: a pre-recorded demo video saved on the teacher machine.

**Rehearsal 1.5 ｜ Experience 1, the AI Blink full flow (used 14:28–14:50, new)**
Walk pages 13–22: connect the XIAO → deploy the face-detection pretrained model on SenseCraft → configure the trigger "face detected → LED on" → verify → (if available) add the Grove expansion board + strip, experience "recognize → drive the peripheral directly." Time the deployment (you'll quote the number in class). Decide: your own face or a photo on screen for the face demo.
Backup: if trigger config fails, switch to pure demo — students only get to "deployed + recognized."

**Rehearsal 2 ｜ the full training flow (used 14:50–15:22, the spine of this lesson)**
1. Log in with a pre-made account; enter the empty RPS project (select board → select serial port → name the three classes in English);
2. Collect 25–30 photos per gesture (deliberately leave 5 "bad data" per class: cluttered background / single angle);
3. One-click train; time the wait (you'll quote the number);
4. Deploy to the board; test with your own hand; then let the person next to you test — note what fails (your first-hand attribution material for class);
5. Time the whole run: if it takes over 100 minutes, you collected too much demo data — cut to 25 per class.
Backup: your pretrained model can be deployed directly, in case collection collapses entirely.

**Rehearsal 3 ｜ vision-to-action (used 16:20, second half)**
Open Codecraft; use the Section 6 prompt to make "scissors → LED on" run, then extend to rock and paper. Time the AI generation + compile-flash (you'll tell the class: "compile + flash takes about X seconds — normal, don't panic"). **Note: the deck no longer has a prompt page — you type the prompt on screen or use the board; the text is in Section 6.**
Backup: save a working vision-to-action project on the teacher machine — show the compile-flash success screen.

### 1.4 Supplies

**📦 The institution already has (count only):** XIAO ESP32S3 Sense (by headcount + spares); USB-C data cables (by headcount + spares); Kit A LED/buzzer (1 per table); 40-in-1 actuators (2 per table); computers; circulating tablet; projector; whiteboard + pens.

**🛒 To buy:** nothing.

**✨ Teacher supplies:**

| Item | Amount | Note |
| --- | --- | --- |
| Badge/logo sign-in target | on screen | not printed: project the badge/logo large; the camera points at the screen. No badge? Use the course mark or a big English word (CHAIHUO / M0) — anything high-contrast and stable. Localization slot in Section 7 |
| Sticky notes | 2 per student | for the attribution discussion |
| Thick pens | a few | for the stickies |

> **Zero printing** — the three-box sheet is shown on screen (text in Section 6); students draw their own three boxes in the workbook or notebook. Account info is on screen or verbal — no printed cards.

---

## Session Map (14:00–17:00 — shift the whole clock to your actual time. No scheduled break.)

> Aligned to the V3 deck's main sequence (pages 01–47, Chaihuo style). The appendix (pages A·01–A·23) is a standalone 60-min module — see Section 9. V1 migration pages are quick-skim screenshots, don't linger; durations are inferred values, backfill with real times after the first run.

| Clock | Time | Block | What's happening | Deck pages |
| --- | --- | --- | --- | --- |
| 14:00–14:08 | 8 min | Vision AI concept + three examples | image → features → model; Tesla / panda / hummingbird | 01–05 |
| 14:08–14:13 | 5 min | The third board + two kinds of AI | the three-board story lands on "eyes"; "you tell it" vs "you show it" | 06–07 |
| 14:13–14:21 | 8 min | Meet the XIAO | family chart + hardware anatomy (buttons/camera/mic/SD) + 3 pros & 3 cons | 08–10 |
| 14:21–14:28 | 7 min | Today's tool + sign-in demo | SenseCraft URL first shown; badge sign-in SIGNED IN + collect Lesson 4 output | 11–12 |
| 14:28–14:50 | 22 min | Experience 1: the AI Blink | deploy the face-detection model → trigger config lights the LED → drive a peripheral directly | 13–22 |
| 14:50–15:12 | 22 min | Experience 2 · collect data | three-step project setup (board/serial/English names); 25–30 photos per gesture | 23–31 |
| 15:12–15:22 | 10 min | Train + deploy | one-click train → into the board → test; success screen | 32–33 |
| 15:22–15:31 | 9 min | The swap test | swap boards with your neighbor: does your model recognize their hand? | 34 |
| 15:31–15:41 | 10 min | The attribution talk | "why does it get it wrong" — the point: it's not dumb, you taught it too little | 35 |
| 15:41–15:46 | 5 min | First-half close | log line 1: "my model gets it wrong when ___" | 36 |
| 15:46–16:00 | 14 min | Sensor output & protocols | XIAO = a vision AI sensor; results travel UART / I2C / SPI — to whom? | 37–43 |
| 16:00–16:10 | 10 min | The brief | "recognize it → make it move"; hand out output hardware | 44 |
| 16:10–16:20 | 10 min | Three-box rewrite | sense / logic / output + the "can't recognize it?" column | 45 |
| 16:20–16:41 | 21 min | Vision-to-action build | teacher types the prompt on screen (deck has no prompt page — Section 6) → one class runs → extend | typed on screen |
| 16:41–16:50 | 9 min | Buffer | stragglers finish; the done pair up and watch; log progress — **not free time** | — |
| 16:50–17:00 | 10 min | Close | outcome review + preview + collect devices | 46–47 |

### 2.1 Time flexibility

- **Most compressible:** the swap test (9→6 min); Experience 1 Blink (22→15 min, trigger config becomes a teacher demo); sensor output & protocols (14→7 min, teach only UART); buffer (9→5 min).
- **Next compressible:** the attribution talk (10→7 min, stickies still go up); vision AI three examples (8→4 min, hummingbird only); the extension part of the build can go entirely.
- **Never compress:** data collection (under 15 minutes of data = collapse); train + deploy; the attribution talk's one landing line; collecting Lesson 4 output.
- **Collapse ladder:** if the vision-to-action doesn't run → acceptance is "one recognized class triggers one action"; extensions and polish get cut.

### 2.2 TA split

- **TA A (network & accounts):** helps re-test both platforms before class; during class, watches login stalls and training queues (batch: whoever collected first trains first).
- **TA B (hardware):** hands out and collects boards, swaps boards (black/blurry image → check the lens film first, then swap); watches trigger-config wiring in Experience 1 and output-hardware wiring + "recognition result won't connect into logic" stalls in the second half.
- **TA C (records & compliance):** circulating tablet for hand-close-ups (**hands only, no faces**); **watches that no faces are photographed during collection — delete on sight**; keeps order at the attribution board.
- At 1:6, each TA owns 4–5 stations; during the connection block (14:28–14:50) **all three TAs push in** — it's the #1 failure-prone block of this lesson.

---

## Section 3 · Segment-by-segment script

### 3.1 Vision AI concept + three examples (14:00–14:08, 8 min, pages 01–05)

> 📌 Output anchor: none (concept block; skim the V1 migration pages)

🗣️ **Say this:**

> "To open today — let's see how it 'sees'. (page 02) A camera captures an image and turns it into numbers — the photo goes in, 'experience' comes out. The algorithm in the middle has a big name — you don't need to memorize it.
>
> (page 03) Tesla runs eight cameras looking at a full 360° of road. (page 04) In a huge forest, one camera watches over one mountain — when it spots a panda, it reports the location. (page 05) A hummingbird feeder — when it recognizes a hummingbird, it notes what time it came to eat.
>
> Spot the common thread? None of them talks or writes. They **see**. Today, your board learns to do the same."

👀 **Students:** listen, watch.

⚠️ **If asked:** "What is feature extraction / CNN?" → "An algorithm that finds patterns in photos. You don't need the name — just remember: photo in, experience out." Three examples dragging → only the hummingbird; Tesla and panda get one line each.

### 3.2 The third board + two kinds of AI (14:08–14:13, 5 min, pages 06–07)

> 📌 Output anchor: none (bridge block)

🗣️ **Say this** (one screen open on Codecraft, one on SenseCraft):

> "This is your third board. The first one, the Grove kit — that's **skin**: it feels hot, cold, motion. The second one, the Wio — that's the **face**: it has a screen and buttons. This thumb-sized little board is the **eyes** — it has a camera, and a microphone too. It can see and hear.
>
> So far you've used one kind of AI: **you tell it, it builds** — you tell Codecraft what you want and it writes the instructions for you. Today you meet a second kind: **you show it, it learns** — you don't say a word; you show it photos, lots of them, and it learns to recognize on its own. The website is called SenseCraft AI — it's where you teach boards to recognize things. First half of today: no typing. You talk with photos."

👀 **Students:** listen, compare the two screens.

⚠️ **If asked:** "Is this the same AI as ChatGPT?" → the standard line: "Both learn from lots of examples — but one learns text and the other learns images. Want the deep version, find me at break."

### 3.3 Meet the XIAO ESP32S3 Sense (14:13–14:21, 8 min, pages 08–10)

> 📌 Output anchor: none (gear-intro block — get the pros and cons clear; the "half-second lag" and "it makes mistakes" landings depend on them)

🗣️ **Say this** (hold up a XIAO; pass it around the aisles):

> "Its name is XIAO ESP32S3 Sense — you don't need to memorize it; call it **the little eye board**. (page 08) It has a whole family of siblings, all different models; today we use the one with the camera.
>
> (page 09, pointing at the anatomy diagram, walk the class around it) What's on it: this is the camera — its eye. This is the microphone — its ear. These two little buttons — reset and boot; you'll use them when flashing. And here: a tiny LED, an SD card slot, the charging port. Don't memorize all of it — just recognize the eye and the two little buttons.
>
> The most special thing: **AI lives inside the board.** Once the trained model is loaded in, it recognizes your gestures with no internet at all.
>
> (page 10) Three pros. One: it's **small**. Two: it's **cheap** — about the price of a lunch. Three: **the AI runs on the board** — no internet needed, and your photos never leave this little board. Three cons — and you'll hit all of them today. One: **small computing power** — it 'thinks' about half a second slower; normal. Two: **it makes mistakes** — 'what to do when it can't recognize' is part of your design. Three: **no screen** — it talks through lights, buzzers, or the computer. Remember one line: **small computer, small jobs.**"

👀 **Students:** pass a XIAO around; find the camera and the two buttons on the anatomy diagram.

⚠️ **If asked:** "How is this different from photo recognition on my phone?" → "The phone sends the photo to a faraway computer to recognize it. This board recognizes it on itself — slower, but no internet, and it doesn't hand your photos to anyone." "No screen is weak" → "Right — that's why it usually teams up with the Wio: one sees, one shows. Today, lights and buzzers speak for it."

### 3.4 Today's tool + sign-in demo + collect Lesson 4 output (14:21–14:28, 7 min, pages 11–12)

> 📌 Output anchor: none (pure demo block; collecting Lesson 4 output bridges the lessons)

🗣️ **Say this:**

> (page 11) "Here's today's weapon: sensecraft.seeed.cc/ai — don't write it down; the tabs are already open on every machine once the boards go out.
>
> Collecting last session's work: last time, you took a complete project — your Pomodoro timer — from requirements, to screens, to code, to breaking it, with the BMAD five roles.
>
> (page 12 — pick up the teacher machine; point the camera at the badge on screen — it shows **SIGNED IN**; point at something else — nothing.)
>
> How does it know the badge? It's not face-recognizing. It's that **someone taught it.** Not by writing, not by talking — by showing it lots and lots of photos. Today, each of you teaches one with your own hands — teaching it to recognize your own gestures."

👀 **Students:** watch the demo; hand in Lesson 4 records (md link / handwriting photo).

⚠️ **If it fails:** the demo model gets it wrong live → don't panic, that's today's lesson: "See? It makes mistakes too — by the end of class you'll know why it does." No badge → project any high-contrast, stable image (logo / course mark / big English word). Collecting: hard 5-minute timer; no individual feedback; note who's missing, due before class ends.

### 3.5 Experience 1: the AI Blink — deploy a ready-made model (14:28–14:50, 22 min, pages 13–22)

> 📌 Output anchor: **every board runs a ready-made model — recognized target lights the onboard LED** (the first "it works!" moment of this lesson)

🗣️ **Say this:**

> "Boards out. Assemble and plug in first — both ends of the cable pushed all the way in (skim 13–14). Connect to the computer, click 'connect device', see your board's name (skim 15–16).
>
> Once connected, don't rush to photograph. First, load a model **someone else already taught** into the board. In SenseCraft, pick face detection, click 'deploy' — it travels down the cable into the board.
>
> (pages 15–18) Now give it a 'trigger': face detected → turn on the onboard LED. Watch the LED's spot (page 17) — point at my face — on! (page 19) Congratulations — you just deployed an AI-driven automation system.
>
> (pages 20–22) And watch this: add the Grove expansion board, plug in a light strip — target recognized, the strip lights up directly. **Not one line of code.** The vision model drives the peripheral directly. That's 'recognized → moves'. You'll build one of these yourselves in the second half."

👀 **Students:** assemble, connect; deploy the face-detection model; configure the trigger (face → LED on); verify with the teacher's face / the screen.

⚠️ **If things go wrong:**
- ⭐ **This is the class's #1 failure-prone block:** all three TAs push in. One student can't connect in 3 minutes → swap board, swap cable, don't linger (swap, don't repair).
- Login fails → TA A hands over a spare account on the spot; sort the stuck account after class.
- Black/blurry image → first question "is the lens film off?", second move swap the board.
- **Compliance:** face detection recognizes only the teacher's own face or the on-screen photo — students don't photograph each other's faces. State the rule now: "When you collect your own data later — **hands and objects only. No faces.**"
- Short on time → trigger config becomes a teacher demo; students only get "deployed + recognized."

### 3.6 Experience 2 · collect data: rock-paper-scissors (14:50–15:12, 22 min, pages 23–31)

> 📌 Output anchor ①: everyone's three-class photo dataset (in the workbook's "data collection record" zone: how many per class, what angles/lighting)

🗣️ **Say this:**

> "Now — teach it your gestures: scissors, rock, paper. For each one, take 25 to 30 photos with your board."
>
> (teacher demonstrates, on screen) "Watch me — this one, hand straight on. Next, further away. Another, different angle. Another, other hand. — **For every photo, give the gesture its 'answer name':** this is 'rock', this is 'scissors'. That answer name has a formal word — a **label**. It's the standard answer for each photo. When it learns, it's checking its answers."
>
> (deliberately demonstrate bad data, don't explain yet) "Now a few more — background switched to the window, half a hand, ten shots all at the same angle. Done. Are these photos good? Not saying yet. We'll see."
>
> "Rule repeated: **hands and objects only — no faces.** Not yours, not anyone's. If a face sneaks in, delete it on the spot."

👀 **Students:** photograph their three gestures, 25–30 each, choosing the label for each.

⚠️ **If things go wrong:**
- Chaotic collection (unsure how many / wrong labels) → TA circulation, three questions: "How many do you have?" "Label correct?" "Changed the angle?"
- A student wants to train after only 10 → **let them! Don't say a word** — when it fails later, it's the teaching material (designed contrast).
- A face gets photographed → TA C watches it get deleted, restates the rule once, no scolding.

### 3.7 Train + deploy (15:12–15:22, 10 min, pages 32–33)

> 📌 Output anchor ②: self-trained model deployed on the board (after success, take a photo of "the model running on the board"; md or handwriting: how many classes, how many photos each, how long the wait)

🗣️ **Say this:**

> "Collected enough? Click 'train'. What's it doing? Plain-English version: **it's turning your hundred-plus photos into 'experience'** — what do rock photos have in common, what do scissors photos have in common; it figures that out itself and stores it as an experience book. That process is called **training** — you're the teacher, it's the student."
>
> (during the wait) "Training queues — whoever collected first trains first. While you wait, think: what kind of student would my weird photos from earlier produce?"
>
> "Trained? Click 'deploy' — the experience book travels down the USB cable into your board. Once it's in, it remembers — unplug the cable, still remembers. Now — show your board a scissors. See if it recognizes its teacher."

👀 **Students:** one-click train → wait → deploy to the board → test all three gestures.

⚠️ **If things go wrong:**
- Queue jam → TA A batches (collectors first); anyone waiting over 5 minutes goes to the board and sticks a "when I predict it'll get it wrong" sticky (warms up the attribution talk).
- Platform slow → run the two-track "batch + teacher rescue model": anyone who can't finish trains deploys the teacher's pretrained model, keeps their data, retrains after class (loses the hands-on feel — rescue only).
- A student recognizes nothing → check "did it deploy?" first, then data size — odds are it's the 10-photo student; keep them as discussion material.

### 3.8 The swap test (15:22–15:31, 9 min, page 34)

> 📌 Output anchor ③: swap-test score (in the workbook: under which move did your neighbor's model fail — note the specific situation)

🗣️ **Say this:**

> "Now the fun part: **swap boards with your neighbor.** Your model — does it recognize their hand?"
>
> "Rules: only scissors-rock-paper, and vary it — further, faster, other hand. Recognized = 1 point. Got it wrong = …write it down too. That's treasure. We'll tally the class failure rate in a minute."

👀 **Students:** swap, test, score, count errors.

⚠️ **If things go wrong:**
- ⭐ **Widespread failure is designed, not an accident** — the teacher never "rescues": only "Write it down — under which move did your model fail?" Rare class with too-high accuracy → the teacher becomes the trap: gloved hand, toy scissors, back of hand to the lens — manufacture attribution material.
- The test turns into roughhousing → boards back to owners; switch to "test your own, in three different lighting conditions."

### 3.9 The attribution talk: why does it get it wrong (15:31–15:41, 10 min, page 35)

> 📌 Output anchor ④: attribution sticky (after going up, students write one line in their log: "my model gets it wrong when ___", as specific as possible — "low light" ✓, "it's not accurate" ✗)

🗣️ **Say this:**

> "Failure-rate tally — hands up if your model got it wrong more than 3 times. (a sea of hands) Congratulations. You just earned today's most important textbook."
>
> "One sticky per person: write **when your model gets it wrong** — the more specific the better. 'Low light' passes. 'It's not accurate' doesn't. Stick it on the left side of the board."
>
> (read the stickies, group them) "Light changed, background changed, someone else's hand, only a dozen photos… see the pattern? **It's not dumb. You taught it too little.** Want it smarter? Feed it more, more *different* examples. Remember my weird photos from before class — one angle only, messy background? A student taught by that teacher only knows how to sit in the front row."
>
> "One loop back: you've learned that talking to AI needs examples. Today you saw it — for an AI that recognizes things, **the examples ARE everything.** Telling it isn't enough. You have to show it."

👀 **Students:** write the sticky, put it up; listen to the grouping; add one line of attribution to their sticky.

⚠️ **If it goes cold:** call on someone who raised their hand: "Which move got it wrong for you?" Two or three of those warms it up. A student writes "the board is dumb" → throw it back to the class: "Same board — why did it recognize YOUR rock?" — let them answer "the data."

### 3.10 First-half close (15:41–15:46, 5 min, page 36)

> 📌 Output anchor ⑤: log entry (four-line template: "did" = I trained a model that recognizes rock-paper-scissors; "stuck at" = **required**: when does my model get it wrong; "then" = how I found out; "next time" = what if I feed it more data / change angles — md or handwriting)

🗣️ **Say this:**

> "Log time — four lines as usual. For 'did', write: I trained a model that recognizes rock-paper-scissors. 'Stuck at' is required today: **when does my model get it wrong.**"
>
> "Leave the model on the board — second half, it does something after it recognizes."

👀 **Students:** photograph their board + write the four-line log.

### 3.11 Sensor output & protocols (15:46–16:00, 14 min, pages 37–43)

> 📌 Output anchor: none (mind-shift block — re-understand the "board" as a "sensor", paving the way for the brief)

🗣️ **Say this:**

> (page 38) "First half done. Your board is no longer an ordinary board — a deployed XIAO is a **vision AI sensor.** Just like the light sensor and the buttons you've used — except what it 'senses' is a picture.
>
> (pages 39–40) Once a sensor recognizes something, the result needs an exit. It speaks several 'languages': **UART** — the serial port; when it's connected to a computer, the recognition results you see on screen travel over it. **I2C** and **SPI** — for boards talking to boards. **WiFi/MQTT** — we play with that in the networking lessons, later.
>
> (page 41) Look — two boards joined by I2C: this one watches, that one works. (skim 42–43) SPI's the same idea — a few jumper wires, and the 'eyes' and the 'hands' split apart.
>
> We don't run two boards today — but hold onto this feeling: **recognized → output → something else catches it and does the work.** The build in a minute is making that output light your LED and ring your buzzer."

👀 **Students:** listen; find the pins on their own board (back to the page 09 anatomy diagram).

⚠️ **If asked:** "What's the difference between I2C and SPI?" → "Both are ways boards talk to each other — you don't need to tell them apart today. Remember UART — the serial port — that's what we use in a minute." This block is pure cognition, no hands-on; a student itching to wire → "Note it down. Today's output runs through the serial port; two-board play is a later lesson."

### 3.12 The brief (16:00–16:10, 10 min, page 44)

> 📌 Output anchor: none (brief block, paves the way for the build)

🗣️ **Say this:**

> "Second-half brief, one sentence: **recognize it → make it move.** Scissors → red light on. Rock → buzzer beeps. Paper → all off. That's my demo — your rules are yours to set."
>
> "Change the meaning if you want: scissors = my sister's secret signal — recognized, play the song she likes. Your model, your call."
>
> (hand out output hardware) "Every table gets LED and buzzer as base pieces. Servo and light strip: only two per table, first-come-first-served. Didn't grab one? Don't sweat it — making the light and the buzzer do something interesting is just as much of a skill."
>
> "Set expectations now: it 'thinks' on a thumbnail-sized board — **half a second of lag is normal.** Making it fast and smart enough to run a building is a later lesson. Today: it watches, and takes care of this one thing."

👀 **Students:** listen to the brief; collect output hardware; decide their "recognize what → do what."

⚠️ **If things go wrong:** "I want it to recognize my Gundam model and fire!" → catch it: "Great idea — put it on the 'later' list. Today, use what your board already knows — rock-paper-scissors. That recognition step already won; don't re-fight it." Actuator argument → first-come-first-served + the agreement "if nobody's using it after 16:20, it rotates."

### 3.13 Three-box rewrite (16:10–16:20, 10 min, page 45)

> 📌 Output anchor ⑥: three-box sheet (sense / logic / output, with the extra logic column "what if it can't recognize it or isn't sure?" — in the workbook or notebook; show a TA before building)

🗣️ **Say this:**

> "Before building — the usual three-box sheet: sense, logic, output. Today's three boxes have a new member."
>
> "**Sense:** the class the camera recognizes (scissors / rock / paper). **Logic:** recognized what, do what. **Output:** the light, the buzzer, or the servo you grabbed."
>
> "The new member lives in the logic box, one more column: **'What if it can't recognize it — or isn't sure?'** Earlier projects never had this situation — a button is either pressed or not. But 'seeing' hesitates: it might say 'I'm not sure if that's scissors or paper.' This column must be filled. Writing 'do nothing' is a valid answer — but it has to be *your* decision, not its accident."

👀 **Students:** fill the three boxes (including the "can't recognize" column); show a TA before building.

⚠️ **If things go wrong:** the "can't recognize" column left blank → send it back: "That column is today's required question." "How sure is sure?" → good question, one line on screen: "Every time, it reports how confident it is — a percentage. That number is its **confidence**. Your rule: below 70% confidence, treat it as not recognized."

### 3.14 Vision-to-action build (16:20–16:41, 21 min — the deck has no matching page; the teacher types the prompt on screen)

> 📌 Output anchor ⑦: working vision-to-action project (≥1 class → ≥1 action; md record: recognized class, trigger condition, output action, tested result; extension record for those with energy)
> 📌 Output anchor ⑧: log progress update (four-line template, "did" = I made my model ___ after recognizing ___ — md or handwriting)

🗣️ **Say this** (first 10 min demo, Codecraft on screen):

> "Watch how I plug the 'recognition result' into a conversation. Note this prompt — you're now the **boss of two AIs**: the one SenseCraft taught handles 'recognize', the one Codecraft runs handles 'do'."
>
> (type on screen, read it line by line)

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

> "See — the old discipline: **one thing at a time.** Get 'scissors → light on' running first, then rock, then paper. In 30 minutes I'll call across the room and check your three-box sheets."

👀 **Students:** follow the prompt with Codecraft, block by block: one class runs → extend to the other two → polish if there's energy (strip / rhythm tones).

⚠️ **If things go wrong:**
- "It's slow / doesn't work" → point back to the 3.3 expectation-setting: "Half a second of lag is normal. Actually wrong? Think back to the first half — what makes it wrong? Write that situation down — it's the first item on next lesson's trouble list."
- After moving / changing light, everything fails → teach on the spot: "This is a scenario the data never saw. Quick rescue: back to SenseCraft, re-shoot 10 photos in the current light, retrain ('change the data' route, demo live); OR write on your three-box sheet: 'this model only works at the window desk' — that's a professional answer too."
- It works but the action is too weak (a blink you barely see) → upgrade sheet on the board: LED → RGB strip; one beep → rhythm pattern; one servo swing → continuous waving.
- Lost between the two platforms → point at the screen: "Left SenseCraft, right Codecraft. Don't merge them." TAs correct it class-wide.
- At 16:31, some still have nothing running → TA B hands out the fallback prompt (the on-screen prompt with the output swapped to the onboard LED; class names stay English: scissors/rock/paper); continue from the fallback. **At 16:41, everyone stops and moves to the buffer.**

### 3.15 Buffer (16:41–16:50, 9 min)

- **Not running yet:** TA B concentrates on getting them to "one class → one action" (the acceptance floor).
- **Running:** ① try your neighbor's project once; ② log progress (four-line template, "did" = I made my model ___ after recognizing ___); ③ spare time: on the back of the three-box sheet, write "three scenarios where I'll try to break my own project next lesson."
- The teacher: tally acceptance (running / total), fill reflection page sections A and B.

### 3.16 Close (16:50–17:00, 10 min, pages 46–47)

🗣️ **Say this:**

> "Today you did two things nobody ever walked you through: you taught a board to know the world with your own hands — collecting photos, training a model, deploying it to the board. Then you made the knowing decide for you — your gesture makes a light turn on, a buzzer ring. In the whole course, this is the only time you touch 'how AI gets made.'"
>
> "Next lesson preview: bring your model back. First, AI becomes your tester and hands you a trouble list; then you and your neighbor try to wreck each other's projects. Today you said 'not recognized → do nothing.' Next time you'll answer: that decision — accept or reject?"
>
> "Boards into the bag with your name on it. Output hardware back in place. Three-box sheet and log go with you (md or handwriting — hand to the teacher after class: link or photo)."

👀 **Students:** pack up; take the three-box sheet and log.

⚠️ **If asked:** "Can I take my model home?" → "The model lives in the board, and the board lives here. Missing it? Read your log — first thing next lesson, we use it."

---

## Section 4 · Backup plan overview

| Block | Short on time (compress) | Going wrong live (substitute) | Truly impossible (bottom line) |
| --- | --- | --- | --- |
| Badge demo | 6→3 min | teacher's pretrained RPS model recognizes gestures live | play the pre-recorded demo video; teach from it |
| Experience 1 Blink | 22→15 min (trigger config = teacher demo) | skip the trigger; just deploy + recognize | cut it; go straight to Experience 2 collection |
| Sensor output & protocols | 14→7 min (UART only) | verbal pass + board note "recognized → output" | cut it; doesn't affect the build |
| Data collection | 30→25 per class | two students share one board (gestures in turn) | import a teacher pre-collected dataset (rescue only) |
| Train + deploy | never compress | batch the training | distribute the teacher pretrained model; retrain data after class |
| Swap test | 9→6 min | "test your own, three lighting conditions" | cut it; the attribution talk uses teacher material |
| Attribution talk | 10→7 min | verbal attribution, no board | stickies photographed after class and posted to the group |
| Vision-to-action build | keep one class running = acceptance | fallback prompt + onboard LED | three-box sheet + pseudocode archived; first task next lesson |
| Buffer | 9→5 min | "the running ones help the stuck neighbor" | cut entirely; close runs 5 min late |

### 4.1 The SenseCraft network downgrade plan (a checklist — the teacher just follows it)

> The C-series lessons (5–6) live and die by the internet. Three gates — **every gate has a pre-written action; no live gambling.**

**Gate 1 · T-7 (one week before)**
- [ ] On a classroom student machine, open https://sensecraft.seeed.cc/ai/home/ → can you log in, enter a project, and see the training button?
  - ✅ → prepare as normal.
  - ❌ → **report to the teaching group the same day and start the wholesale replacement:** Lessons 5–6 become "combined creation (standard version) + AI review one round early" (module-pool hard rule 2, per the configuration spec 5.3); this lesson's courseware is not used, no XIAO, no accounts.

**Gate 2 · on the day, 1 hour early**
- [ ] Open SenseCraft once on a student machine and once on the teacher machine?
  - ✅ → class runs normally.
  - ❌ → switch to one shared phone hotspot across the room; retry.

**Gate 3 · within the first 15 minutes of class**
- [ ] Still unreachable on the hotspot, with no sign of recovery within 15 minutes?
  - ❌ → **announce the downgrade on the spot:** today becomes "combined creation" (Kit A + extending last session's projects — materials are standard in the room); Lesson 5 slides wholesale to next week; report to the teaching group to re-sequence per 5.3.
  - To the students: "Teaching a board to recognize things needs an outside training ground, and the training ground is closed today. No problem — we move it to next week. Today, let's add one more piece to your portfolio." **Never switch to the "watch the teacher demo" version** — training must be hands-on. That's today's iron law.

**Partially working** (SenseCraft up but slow): no downgrade — run the two-track "batch training + teacher rescue model" (see 3.7).

---

## Section 5 · Pitfall speed sheet

| Pitfall | Response |
| --- | --- |
| ⭐ SenseCraft down on the day | run the three gates (4.1); the 15-minute rule; downgrade ≠ demo version |
| Training queue / platform slow | batch (collectors first); waiting students stick "when I predict it fails" notes first |
| Camera image black/blurry | lens film first → swap the board (spares) |
| Student photographs a face | rule stated before class; delete on sight, no scolding |
| Wants to train after 10 photos | let them — failure becomes attribution material (designed contrast) |
| Accuracy too high, no failure material | teacher becomes the trap: gloved hand / toy scissors / back of hand |
| Recognition lag called "broken" | "a thumbnail-sized board thinking — half a second is normal; running a building is a later lesson" |
| Everything fails after moving positions | quick rescue: 10 new photos, retrain; or "this model only works at the window desk" |
| Action too weak | upgrade sheet on the board: LED → strip; one beep → rhythm; one swing → continuous |
| Swap test turns into roughhousing / lens blocked / cables pulled | "breaking" limited to showing it things — no touching hardware; cable-pullers promoted to "power-loss recovery testers" |
| Lost between platforms | left-SenseCraft-right-Codecraft dual tabs; TAs correct class-wide |

**Most-asked student questions:**

- "Can it recognize faces?" → "Yes, but today we only recognize gestures. The rule: hands and objects only — nobody's face."
- "What is a model?" → "An experience book — made by summarizing lots of photos. A moment ago it was someone else's; in a minute it'll be yours."
- "Why does it know my hand and not theirs?" → "Because it's only ever seen your hand. Want it to know everyone? Feed it more, more different hands."
- "Is this the same AI as ChatGPT?" → "Both learn from examples — one learns text, the other images. Both make mistakes, so both need a human to check."

---

## Section 6 · Prompts & on-screen text

> This lesson doesn't run conversational AI collaboration for the training half — a "show it, it learns" AI collaborates by feeding data, not by chatting. The following is classroom on-screen / spoken-reuse content; the workbook carries the same.

### 6.1 The vision-to-action prompt (used in 3.14 — the deck has no matching page; the teacher types it on screen; students can copy it straight to Codecraft)

```
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

> Note: class names stay in English — scissors / rock / paper — never gamble on Chinese rendering. Students can swap in their own class names; keep them English.
> "One thing at a time" discipline: item 1 runs first; items 2 and 3 come after. **Never send all three at once.**

### 6.2 The fallback prompt (3.14 pitfall — for students with nothing running; also typed on screen)

```
My XIAO ESP32S3 Sense has an image-classification model deployed on it
that recognizes three classes: scissors, rock, paper.
The recognition result comes out of the serial port.
Please write me the simplest program:
when the result is "scissors" → turn on the onboard LED.
```

> The fallback only uses the onboard LED — no extra wiring. Once this runs and confidence is back, wire the other output hardware.

### 6.3 Spoken-reuse lines

- **"One thing at a time."** (vision-to-action block; restated before every send to AI)
- **"Break your own project."** (the seed for the swap test — Lesson 6's second half makes it official)

---

## Section 7 · Localization slots

| Where | Default | Swap-in |
| --- | --- | --- |
| Opening demo | badge sign-in | no badge? project any **high-contrast, feature-stable** image: institution logo ／ course mark (big CHAIHUO / M0 text) ／ local landmark ／ a geometric shape. Principle: clearly different from the background, and identical every time it's shown. Train and deploy the matching model on the teacher machine in advance |
| Training classes | scissors / rock / paper | locally popular gestures / hand-signal gestures (thumbs-up / heart / ok) — keep three classes with clearly different appearances, English labels |
| Vision-to-action meaning examples | scissors = sister's signal, play her song | your students' real scenes: "book" recognized = posture reminder, "water bottle" recognized = drink-tracking |
| Scarce output hardware | servo / RGB strip, 2 per table | any "premium output" the institution owns — keep the structure: base pieces for everyone, premium pieces worth racing for |

---

## Section 8 · Teacher reflection page (10 minutes after class)

**A. Timing record**

| Block | Designed | Actual | Delta |
| --- | --- | --- | --- |
| Vision AI concept + three examples | 8 min | | |
| Third board + two kinds of AI | 5 min | | |
| Meet the XIAO (anatomy + pros/cons) | 8 min | | |
| Tool + sign-in demo + collect output | 7 min | | |
| Experience 1 Blink | 22 min | | |
| Data collection | 22 min | | |
| Train + deploy | 10 min | | |
| Swap test | 9 min | | |
| Attribution talk | 10 min | | |
| Sensor output & protocols | 14 min | | |
| Brief + three-box | 20 min | | |
| Vision-to-action build | 21 min | | |
| Buffer | 9 min | | |

**B. The four teaching numbers**

1. Self-trained model deployed and recognizing own gestures: ___ / ___ students
2. Vision-to-action running (≥1 class → ≥1 action): ___ / ___ students
3. Three-box sheet includes the "can't recognize it" column: ___ / ___ students
4. Log has a specific attribution ("low light" qualifies): ___ / ___ students
5. Which SenseCraft gate did you actually hit: T-7 ✅ / hotspot on the day / on-the-spot downgrade (if downgraded, describe it)

**C. Three questions (required)**

1. Rough class failure rate on the swap test? Most common attribution sticky: ______
2. Block to run exactly this way again: ______; block to change: ______
3. How long was the actual training wait? Did class management hold: ______

**D. One-line student feedback:** ______

---

## Section 9 · Appendix module (deck pages A·01–A·23, ~60 minutes)

> The V3 deck appends 23 pages after the 47-page main sequence (rebuilt from the V1 Arduino-era courseware, migrated to the Codecraft toolchain). **The main sequence teaches the board to "recognize"; the appendix teaches it to "move"** — lights, buzzers, fans — the basics that feed directly into the Final Project.

### 9.1 When to use it

- **Overtime / make-up session for the term:** run it as an extension session of Lesson 5 (~60 min);
- **Fast students hungry for more:** once the main-sequence build runs early, hand out the appendix tasks as a hidden level;
- **When not to use it:** the main 3-hour session is already full — don't thread appendix content into the main timeline; it wrecks the clock.

### 9.2 Hard prerequisites (aligned with the T-7 checklist)

- [ ] Test codecraft.seeed.cc compile-flash end-to-end in the room (the appendix's only tool; zero install, browser-only);
- [ ] Materials: per table — XIAO + Grove expansion board + LED + buzzer + fan + Grove cables; beginner-kit knob module (for the final challenge); female-to-female jumper wires as spares;
- [ ] Teacher pre-runs: the four-step onboarding (choose board → connect serial → state the need → generate/compile/flash) + three tasks + knob speed control; time the compile-flash.

### 9.3 Appendix flow

| Time | Block | Pages | Key points |
| --- | --- | --- | --- |
| 5 min | Opening + today's map | A·01–A·04 | framing question: "In the main session, what happened after the model recognized scissors?" — today we make the 'after recognizing' bigger |
| 10 min | Meet the hardware kit | A·05–A·08 | name every part (no work until all named); three wiring steps + the mantra (D1 = the little LED); power check for everyone (charging light off → swap the cable first) |
| 5 min | Pitfalls & troubleshooting | A·09–A·10 | order: cable → port → browser → board model; **the 2-minute rule: swap cable → swap board → find a TA. No on-the-spot repair** |
| 10 min | Codecraft environment | A·11–A·12 | ⭐ the serial-port popup is the #1 failure zone (no popup / clicked deny → TA handles immediately); demo the full flow on screen first, then let students go |
| 20 min | Three tasks: light → buzzer → fan | A·13–A·17 | the one methodology rule: **add new requirements in the SAME conversation — never restart**; watch the success marker per task; not lit at 10 min → swap the spare board, don't repair |
| 7 min | Final challenge + Debug | A·18–A·20 | knob speed control = the full three-box loop; fan humming but not spinning = static friction (nudge the blade); paste errors back to Codecraft |
| 3 min | Wrap-up & clean-up | A·21–A·23 | projects live with the Codecraft account; hardware back in place; preview: every output piece in your Final Project has appeared today |

### 9.4 Appendix-specific pitfalls

- Fan spins slowly / stutters → expected (5V design fed at 3.3V); the unified line: "it spins = task complete."
- Student restarts the conversation → stop it immediately, point back: "Getting it wrong? Add a line. Don't restart." (X1 rule 4.)
- Fast finisher on task 2 → extra: "two short beeps and one long"; slow student gets the full prompt to read aloud.
- Knob speed control: get it running first, then play — the whole class turns the knob max → min, listening to the fan change pitch (physical feedback is the best reward).

### 9.5 Bridge language with the main sequence

- The appendix task pages each say "why we do this" — as the teacher, state the motive before the instruction; don't fall back to describing only the steps.
- The LED/buzzer from the main second half are "base pieces" here; the fan and knob are the new members.
- All appendix AI work runs through Codecraft conversation — **no arduino-cli, no terminal, no requirements.md** (the old toolchain is retired).

---

_Version: EN v1 ｜ 2026-08-25 ｜ Source: CN 讲师版 v3（2026-08-05） ｜ 上游信源：CFG-5 配置说明书第 5 次课行 + 5.3 C 系列课次预案；积木卡 C1《机器视觉初体验》+ C2《视觉 + 逻辑联动项目》；先锋官规范 G1–G8_

_Localization notes: Proper names kept (SenseCraft AI, XIAO ESP32S3 Sense, Codecraft, rock/paper/scissors tags); "两种 AI" -> "you tell it, it builds" vs "you show it, it learns"; "归因讨论" -> the attribution talk (takeaway: it's not dumb — you taught it too little); "三道闸" -> the three gates; "视觉联动" -> vision-to-action; "只拍手不拍脸" -> hands and objects only — no faces; "慢半秒" -> half a second of lag is normal. The training segment does not use conversational AI, action segment uses Codecraft chat — structure fully aligns with CN version. All V1->V3 decisions absorbed (zero printing, 3-panel projection, compliance guidelines, appendix extension moved to a separate chapter)._
