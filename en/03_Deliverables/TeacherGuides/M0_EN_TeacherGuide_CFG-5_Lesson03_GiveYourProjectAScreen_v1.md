# M0 Teacher's Guide ｜ CFG-5 Semester Course · Lesson 3: Give Your Project a Screen (v1)

_Wio Terminal · HMI (Human-Machine Interface) board ｜ Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) ｜ 10-session term ｜ 3 hours ｜ Source: 中文版 v2（`交付物/教师课件/M0_教师课件_CFG-5_第3课_给作品装上屏幕_v2.md`）_

> **The one-sentence brief**: This is the "new gear" session. Students receive the **Wio Terminal** — a handheld with a color screen — get to know it with their hands (at least three hardware points lit up by their own messages), learn the one skill this lesson lives on — **describing a screen to AI with position, size and color** — and build their first two-screen interactive project plus an AI learning log. You don't need to know Wio's technical details, and you don't need to cover its full feature list — today's cast is the screen, the buttons, the joystick and three sensors. Your catchphrase all session: *"Don't just watch me — send a line and try it yourself."*

---

## 🎯 Learning Objectives

_By the end of this session, students will be able to…_

1. **Identify** the parts of the Wio Terminal (screen, buttons, joystick, light sensor, microphone, accelerometer, buzzer) and **compare** it with the previous board — "that one senses the world, this one lets people interact with your project." *(Bloom: Identify, Compare)*
2. **Demonstrate** at least three of the five "light-it-up" micro-experiments on their own Wio — hands on, not watched. *(Bloom: Apply)*
3. **Describe** a screen layout to AI using **position, size and color**, and **distinguish** "describing logic" from "describing looks." *(Bloom: Describe, Distinguish)*
4. **Produce** a two-screen interactive build switched by a button or the joystick, and **complete** a four-sentence AI learning log that names exactly what was unclear — position, size, or color. *(Bloom: Produce)*

---

## 📋 Page One: The Last Look Before You Walk In

### What today produces

Four things, every student:

1. **A "my Wio tour sheet"** — the walk-around plus the 5 "light-it-up" micro-experiments, leaving three lines in the workbook: "Wio has ___ more than the old board (at least 3)" / "I lit up: ☐ button ☐ joystick ☐ microphone ☐ light ☐ accelerometer" / "What surprised me most was ___ because ___";
2. **One skill for describing screens** — the screen-comparison experiment plus the "how to describe a screen" phrase (position / size / color). This is the soul of the lesson;
3. **A screen-based interactive build** — the follow-along button counter plus a two-screen switching project, with one proud line of their own describing how they talked to AI;
4. **An AI learning log** — made ___ / stuck on ___ / then ___ / next time ___. Today's "stuck on" must say exactly what was unclear: position, size, or color.

Delivery: their workbook (online doc or handwriting), handed in after class (link or photo).

You run four segments: **Meet the new gear** (50 min — collect last session's work, walk-around, micro-experiments) → **Use it well: the screen lesson + build** (90 min — comparison experiment → counter → free round → the drift gallery → takeaways + log) → **The 30-minute buffer** (flex time — how to use it in 2.1; **not free time**) → **Wrap & preview** (10 min — flash show & tell, preview Lesson 4). No scheduled break — students use the restroom whenever they like while they work.

### The three things you need to know how to do

1. **Run the flow**: follow the timetable in this guide, segment by segment. Every segment says how long and what to do.
2. **Say the scripts**: every 🗣️ line in this guide is written out word-for-word. Read them as-is; don't improvise.
3. **Make "getting to know it" hands-on**: the walk-around never becomes a manual read — every hardware point gets a 30-second-to-2-minute micro-experiment, and a student has only "lit it up" when they've sent the line themselves. Your catchphrase: *"Don't just watch me — send a line and try it yourself."*

### The three things you do NOT need to know

1. **You do not need to know how to code.** All the code is written by AI — including your students'. You don't need to read a single line.
2. **You do not need to know Wio's technical details.** The new gear has two mantras only: *"slide the switch twice = telling the board 'get ready for new instructions'"* and *"no response? slide it again."* A device misbehaves? Swap it — swap, don't fix.
3. **You do not need to cover all of Wio's features.** SD card slot, wireless, Grove port — one sentence each, "just know it exists" is enough. Today's cast is the screen, the buttons, the joystick and three sensors.

### When something goes wrong

- Your live demo fails: **cut to the backup screenshot within 30 seconds** and keep going (speed sheet in Section 5). **This is not an incident — the plan already accounts for it.**
- A student's device fails: swap the machine or the cable, don't fix.
- You're stumped: smile and say *"Let's ask AI together."*
- The speed sheet is in Section 5. One-line version: **swap, cut to backup, ask AI — the three moves.**

---

## 一、Before Class

### 1.1 One Week Before (do it once)

- [ ] **Re-test the classroom internet**: run the full `codecraft.seeed.cc` loop once on any student machine (lab restore images can reset the environment back to zero).
- [ ] **Count the Wio Terminals** for your actual enrollment (+ 2 spare units). **Stick a flash-mode sticker on every unit** ("Slide, slide = flash mode"), then power each one on once and confirm the screen lights.
- [ ] **Count USB-C cables**: one per unit + the spare box (note: Wio uses USB-C — the cables from the first two lessons may not fit).
- [ ] **Materials (zero-print — everything on screen)**: the mantra *"No response? Slide it."* projected and read aloud twice — students who forget will ask each other; Student Workbook as a shared online doc (link before class) — no online doc? notebooks, every step's output lands in their own record.
- [ ] **The "how to describe a screen" phrase and the micro-experiment lines are NOT printed** — they're in the Student Workbook (full text in Section 6); project and read them together in class.
- [ ] **One day before, post to the class group** (copy-paste ready): "Next session we hand out the new gear — a 'handheld' (color screen). Your project gets a real interface from today. Bring last session's project manifesto and three-box design sheet — online doc link or a photo of your handwriting, either works. Same computers as always."
- [ ] Review the **follow-up list**; settle pairing arrangements for those students before class.

### 1.2 Same Day (arrive 1 hour early recommended)

One person needs ~50 minutes for the checklist below, so arrive an hour early. With a TA: hand them device checks and desk setup; you handle projection, the whiteboard, and the Rehearsal-1 demo. If time is really tight, **Rehearsal 3 (screen-comparison experiment) is mandatory**; the rest can go.

- [ ] Projection test: open Codecraft on your machine — can log in, can chat.
- [ ] Wio check: plug each unit into USB-C, confirm the screen lights, put it back; re-stick any loose flash-mode stickers.
- [ ] Each desk: 1 Wio, 1 USB-C cable, 1 mantra card, markers.
- [ ] Whiteboard: mark the spot for the **Wio tour map** (draw an empty frame for the board; you'll label it as you talk). **Keep Lesson 1's 8-step map and Lesson 2's Project Wall exactly as they are** — you'll point at both today, and the buffer block uses the wall.
- [ ] Screen-comparison screenshots, micro-experiment success screenshots, and the drift-gallery case saved on the instructor machine, in order.

### 1.3 Demo Rehearsals (leave 25 minutes; click through all 5 demos yourself)

You have **5 live demos / demo assets** today. Run each one fully on your own machine before class — not just watch it, click it through. **Anything that puts text on screen gets rehearsed in English/numbers/graphics — no gambling on font rendering (course-wide rule from Lesson 1).**

**Rehearsal 1 ｜ Warm-up "HELLO on screen" (used 14:13)**
On your instructor Wio: switch board type to Wio Terminal → reconnect → send *"Display in large text on the screen: HELLO and my name (pinyin or English): ___"* → flash and check. While you're at it, practice the flash-mode "slide, slide" until you can do it in under 5 seconds.
Backup: a spare instructor machine logged in and standing by + a working project kept on your instructor machine for instant re-flash.

**Rehearsal 2 ｜ The 5 "light-it-up" micro-experiments (used 14:28)**
Send each of the five micro-experiment lines from Section 6 for real, and run each to success: the three-key piano, push the ball, blow out the candle, the board afraid of the dark, the balance ball. Screenshot one successful screen per line. **Any line that won't run in rehearsal: fall back to the original "number-report" versions in Section 6's downgrade note and use those in class — don't gamble live.**
Backup: the 5 screenshots are the fallback — a line fails live? Resend the rehearsal-proven wording; still fails? Project the screenshot and talk through it; students move to the next one. **The round's rhythm must not collapse — one experiment stuck for more than 2 minutes is too long.**

**Rehearsal 3 ｜ The screen-comparison experiment (used 14:50 — the soul of this lesson)**
In the same conversation, send it twice for real: first *"Make a counter screen."*, then *"Show a number in the largest text in the center of the screen; show COUNTER in small text at the top-left; make the number red."* **You must really send both and get real results** — AI's free play on the vague line differs every time, and live authenticity can't be faked. Screenshot each result once as backup.
If AI does well both times: reuse the old line — *"Today it guessed your mind right — but your project is ten times more complex. You can't afford the wrong guess."*

**Rehearsal 4 ｜ The button-counter demo (used 15:00)**
Run the two-step talk once: first the screen line — *"Show the number 0 in the largest text in the center of the screen, and COUNTER in small text at the top-left."* — flash and look; then add one line — *"When I press button A, add one to the number; when I press B, reset to zero."* — reflash and press buttons into the air; finally add a third line — *"Every time the count reaches 10, the buzzer beeps once to celebrate."* — demoing "if it's wrong, add one more line," and press the button 10 times yourself to hear the beep.
Backup: same as Rehearsal 1.

**Rehearsal 5 ｜ The drift-gallery case + buffer challenge tasks (used 16:00 and the buffer block)**
① **Pre-made drift case**: send *"Make a nice-looking clock screen."*, screenshot whatever odd thing AI freely produces (text too small to read, colors smeared together), and write the three-line annotation: "He said ___ → AI made ___ → which sentence went wrong?" If a student volunteers their own case, drop the pre-made one; if not, use it — **the volunteer is the hero, not the joke**.
② **Buffer challenge tasks** — "electronic dice" (shake it — the screen shows a random 1–6) and "balance-ball hole-in-one" (micro-experiment 5 plus a target hole; the buzzer beeps when the ball drops in): run both through successfully yourself. **Only rehearsed tasks go into the buffer; if one won't run, swap in "shake for a message" (shake — a random encouraging line on screen + a beep); if neither runs, the buffer keeps only "finish to standard" and "help your neighbor."**

### 1.4 Materials, in Three Buckets

**📦 In the starter kit (just count, nothing to buy)**

- Wio Terminal per student (+ 2 spare units), USB-C cables, 1 instructor demo unit
- Flash-mode operation stickers (come with the kit)

**🛒 You bring (one stationery run, nothing printed)**

- No printing: the mantra "No response? Slide it." projected and read aloud; Student Workbook as a shared online doc — no online doc? notebooks
- Markers (for the whiteboard tour map)

**✨ Nice-to-have (zero impact if skipped)**

- 3–5 photos of previous cohorts' screen projects (more convincing shown during the warm-up; spoken examples work fine)

Budget note: everything you bring is one stationery run. Cheap.

---

## 二、Session Map

Sample timetable 14:00–17:00 — **shift the whole thing to your actual start time** (a morning class becomes 9:00–12:00; segment lengths don't change). **No scheduled break** — students use the restroom whenever they need, no reporting; device checks and work-collection registration happen quietly at the start of each segment.

| Clock time | Segment | Students do | You do |
| --- | --- | --- | --- |
| 14:00–14:50 | Meet the new gear | hand in last session's work, get the gear, drill the switch, walk around the board, light up hardware with 5 micro-experiments | collect work (note it down), hand out gear, lead the switch drill, keep the micro-experiment rhythm |
| 14:50–16:20 | Use it well: the screen lesson + build | watch the comparison, follow the counter, build a two-screen project, watch the drift gallery, write the log | lead the comparison, lead the two-step talk, host the drift gallery, land the three takeaways |
| 16:20–16:50 | The 30-minute buffer (usage in 2.1) | per today's plan: finish to standard / take a challenge / help a neighbor | circulate as the safety net, hold the line "standard first, then fast" |
| 16:50–17:00 | Wrap: flash show & tell + preview | show each other's projects, hear the preview | lead the show & tell, preview Lesson 4 |

### 2.1 How to use the 30-minute buffer (set the tone first — not free time)

The buffer is flex time: **before class you decide which exit this session plays**, and you announce it to the whole class at 16:20. Three exits, in priority order:

1. **Finish to standard (most common)**: keep building what the free round didn't finish — today's bar is "counter runs + one two-screen project," and everyone must clear it;
2. **Challenge tasks (fast students — you describe them aloud)**: **electronic dice** — shake it (or flick the joystick once) and the screen shows a random 1–6; or **a direction pointer** — wherever the joystick points, the on-screen arrow points. Only the ones you rehearsed; unrehearsed tasks don't go out. Once a challenge is done, steer toward one line: *"You've got the joystick down — later it becomes a controller for your computer, the board acting as the peripheral. That's the road ahead."*
3. **Help a neighbor + bring back old-board skills**: add a sensor link to the two-screen project (e.g., auto-switch to a night screen when it gets dark) — reaching back to the skills from the first two lessons.

**The only rule: get everyone over the line first, then let the fast ones run.** The buffer is not an early dismissal — you're circulating, and the TA is watching the slow ones.

### 2.2 Time Buffer (Flexible / Non-negotiable)

- **Non-negotiable**: the micro-experiment round (the main line of "getting to know the gear" — cut it and the lesson is gone), the screen-comparison experiment (this lesson's soul teaching point), and the standard-line wrap before the buffer.
- **Flexible** (can compress): the walk-around talk (10 min → 6 min; the SD card slot and Grove port get one sentence each), the free round (40 min → 30 min), the drift gallery (2 cases → 1), the buffer (if everyone clears the bar, start the show & tell 10 minutes early).
- **Priority discipline**: if the micro-experiments run over, keep the button, joystick and microphone ones; the light and accelerometer ones become a teacher demo with students watching the result — **but at least three must be sent by students' own hands.**

### 2.3 TA Split (if you have TAs; no TAs? You can carry it alone, just circulate slower)

| Segment | TA A | TA B |
| --- | --- | --- |
| Meet the new gear | register who's handed in last session's work; watch the flash-mode switch (the #1 trouble spot) | one-on-one with students stuck on a micro-experiment; photograph successful micro-experiment screens |
| Screen lesson + build | watch flashing and wiring; one-on-one with slow students | collect drift cases; take build photos (hands only, no faces) |
| Buffer | watch the slow students clear the bar | lead fast students through challenges; take build photos |
| Wrap | organize log and work archiving | sort photos; update the follow-up list |

---

## 三、Segment-by-Segment Scripts

### Segment 1 ｜ Meet the new gear (14:00–14:50)

> Goal: students can say what's on the Wio, what it does better than the old board, and have lit up at least 3 hardware points with their own hands. Deeper: "getting to know the gear" becomes a feel-based experience — daring to press, shake and send commands; the new gear stops feeling foreign.

**14:00–14:08 ｜ Collect last session's work + revisit the Project Wall** [We Do]

**Say this:** *"Before we start, let's collect last session's work: if you used an online doc, send me the link; if you wrote by hand, send a photo — if it's not in yet, make a note of it and finish before you leave today. (point at the Project Wall) Look — last session's wall: everyone's manifesto is up there. Last time you set your topic and learned the five rules; today we hand out new gear — your project gets a real interface from today. Keep your manifesto and three-box design sheet at hand — we won't touch them today, but they're the north star for every big project after this."*

**Watch for:** the collection gets a hard 5-minute timebox — no per-item feedback; the not-yet-in list goes to the TA to register, don't haggle. Everything produced today goes into students' own workbooks (online doc or handwriting), same deal as Lesson 2.

📌 **Output anchor:** last session's four outputs (manifesto / three-box design sheet / review & trade-off / log) are in — online docs by link, handwriting by photo.

**14:08–14:13 ｜ The new-gear ceremony: from board to handheld** [I Do]

**Say this:** (hold up the Wio Terminal) *"New gear. It's called the Wio Terminal — think of it as a handheld little computer: a color screen, three buttons, a five-way joystick, and sensors built in. One thing is different from the old board: (hold it up, point at the switch) before you flash, slide the switch on the side — slide, slide — that's how you tell the board 'get ready for new instructions.' Everyone: drill it with me twice."*

**Watch for:** the switch drill happens NOW, and the problems surface NOW — that saves 20 minutes of rescue attempts during coding. The mantra card goes on every desk: *"No response? Slide it."*

**14:13–14:18 ｜ Connect + static warm-up** [I Do] → [You Do]

**Say this:** *"Switch the board type in Codecraft — choose Wio Terminal, same old flow. Then send the line you've known since your first lesson: 'Display in large text on the screen: HELLO and my name (pinyin or English): ___.' (wait for the room to light up) See — new hardware, and everything you already know still works. Nothing is wasted."*

**Watch for:** why English on screen — this board's Chinese font library is unreliable; **all screen display today is English / numbers / graphics** — don't let display problems hijack a gear lesson (course-wide rule from Lesson 1). "Switching hardware costs zero learning" is today's confidence anchor — point at the color screen and add: *"and the letters are prettier now."* Serial-port problems follow the old plan: swap cable → swap machine → pair up.

**14:18–14:28 ｜ The walk-around: meet the board + compare with the old one** [I Do]

**Say this:** (hold up the Wio; label the whiteboard frame as you go, one sentence each) *"Let's walk around and meet your new partner. The color screen — your project's face: interfaces, numbers, graphics all live here. Three buttons plus a five-way joystick — the human's hand: press, nudge — that's how people give your project commands; game consoles and menus run on these. The light sensor — it knows light from dark: a light that turns on by itself at night. The microphone — it hears things: clap to switch, a sound-level meter. The accelerometer — it knows whether it's moving and which way it's tilted: shake detection, step counting, fall alarms. The buzzer — it can make sound: reminders, alarms. Two small things over here, ears only today: the SD card slot — it can store things; the Grove port — the door for adding new modules later. These two, just know they exist. (pause) Now compare with the old board: the old one's strength is sensing the world — sensors soldered on, plug and play. This one adds a color screen, a joystick and wireless — its strength is letting people interact with your project. One sentence: why did we change gear? From today, your project has a face and hands."*

**Watch for:** the walk-around never becomes a manual read — every time you name a part, students find it on their own board with a finger and touch it. SD card slot, Grove port, wireless: one "just know it exists" sentence each, no expansion. A student presses on internet? *"It can — that's a later lesson. Today, just remember it exists."*

📌 **Output anchor:** two lines written in the workbook — "Wio has ___ more than the old board (at least 3)" and "the first thing I want to make with it is ___."

**14:28–14:50 ｜ The "Light It Up" micro-experiment round: get to know it by doing, not by listening** [I Do] → [You Do]

**Say this:** *"Touching isn't knowing — lighting it up is. Five micro-experiments, one line each, watch it come alive. The lines are printed in your Student Workbook — follow me on the screen. The rhythm: I send mine first, then you send yours — don't just watch me, send a line and try it yourself."*

The five micro-experiments (each ~4 minutes: 30-sec teacher demo + 2 min students send their own + 30 sec show results). **Design principle: inputs do things, they don't report numbers** — every micro-experiment is a mini toy with an image/sound/game feel, not a sensor reading out a value; all-graphics + English display, no font roulette; and every one of them IS an interface — the seed for the screen lesson ahead (when you reach the comparison, point back: "everything we just lit up was an interface"), so the anchor line "what surprised me most" has real content:

1. **The three-key piano (buttons)**: *"Press buttons A/B/C to play do, mi, sol. Show DO / MI / SOL in large text on the screen."* — press it, and it answers you.
2. **Push the ball (joystick)**: *"Draw a small ball in the center of the screen. Push the joystick and the ball moves that way."* — nudge it, and the ball listens.
3. **Blow out the candle (microphone)**: *"Draw a lit candle in the center of the screen. Blow at the microphone and the flame goes out; after 2 seconds it lights again."* — one blow, the candle goes out.
4. **The board afraid of the dark (light)**: *"Draw two open eyes on the screen. When the light gets dim, close the eyes and show ZZZ; when it gets bright, open them again."* — cover it, and it falls asleep.
5. **The balance ball (accelerometer)**: *"Draw a square frame with a small ball inside. Tilt the board and the ball rolls toward the low side."* — tilt it, and the ball rolls downhill.

Students send their lines wrapped in the standard frame (printed in the workbook): *"I'm using the Wio Terminal. Please make this work: …"*

> **Downgrade note (applies to all):** the new lines count only if they ran in your rehearsal; a line that won't run falls back to the original "number-report" versions — ① *"When I press button A, the buzzer beeps once and the screen shows the letter A."* ② *"When I push the joystick up, show UP; down, show DOWN; left, LEFT; right, RIGHT."* ③ *"Show the sound level in large numbers in the center of the screen."* ④ *"Show the light level in large numbers in the center of the screen."* ⑤ *"Show the X-axis value on the screen; tilt the board left and right and watch the number go positive and negative."*

**Watch for:**
- This is today's main line — **knowing is hands-on**. Everyone sends their own lines; watching instead of doing doesn't count.
- A line fails: resend your rehearsal-proven wording, or fall back to the number-report version above; a single dead unit gets swapped, not fixed. One experiment stuck for more than 2 minutes is too long — the rhythm must not collapse.
- Fast students add a free line on top of the current experiment (*"make the ball a different color" / "beep when the ball touches the edge"*); slow students pass by keeping the first three.
- The Five Rules stay in the background: one thing at a time — one line lights up one hardware point.

**Pitfalls:**
- A student asks "how does it know I blew / tilted it?": one sentence is enough — *"Blow hard enough and it counts as blowing out the candle; the board can feel which way it's tilted. The exact units don't matter."*
- A student discovers the joystick also presses in (the five-way joystick has a button): affirm the discovery — it goes on the list of usable inputs for the free round.

📌 **Output anchor:** ticks plus one line in the workbook — "I lit up: ☐ buttons ☐ joystick ☐ microphone ☐ light ☐ accelerometer; what surprised me most was ___ because ___."

**CFU:** *"Cover the light sensor with your hand — what should the screen do? (wait) Without looking at your workbook — which line lights up the microphone? Point at it. Good — that's what 'lit up by you' means."*

---

### Segment 2 ｜ Use it well: the screen lesson + build (14:50–16:20)

> Goal: students can state a screen requirement to AI (position / size / color / button behavior) and make one screen-based project with button interaction. Core realization: **"describing logic" and "describing looks" are two different ways of speaking** — logic says cause and effect; screens say how something appears.

**14:50–15:00 ｜ The comparison experiment: this is how you describe a screen (the soul of the lesson)** [I Do]

**Say this:** (project) *"Hardware's all lit up — now lesson one of using it well: how do you get AI to give you a good screen? An experiment, one idea two ways of saying it. First way: (send) 'Make a counter screen.' — see what it gives you. (show the result) Second way: (send) 'Show a number in the largest text in the center of the screen; show COUNTER in small text at the top-left; make the number red.' — now see what it gives you. (project side by side) What's the difference? Describing a screen means saying three things clearly: position, size, color. The phrase is printed in your Student Workbook — 'how to describe a screen': at [position], show [content] in [size/color]; when [action], [change]."*

**Watch for:** this extends last lesson's Five Rules onto this color screen — Rule 2 (say the input & output) runs logic; today's phrase runs appearances. Land the line: *"Logic says 'do this when that happens.' Screens say 'what something is, where it sits, what it looks like.' Two ways of speaking — you need both."*

**15:00–15:20 ｜ Follow-along: the button counter** [I Do] → [You Do]

**Say this:** *"Follow along, and we say it in two steps on purpose. Step one, the screen only: 'Show the number 0 in the largest text in the center of the screen, and COUNTER in small text at the top-left.' Flash it, look at it. Step two, the behavior: 'When I press button A, add one to the number; when I press B, reset to zero.' Flash again — then one more line to the whole class: 'Every time the count reaches 10, the buzzer beeps once to celebrate.' (the room fills with button presses; count to 10 and hear the beep) See? First describe the looks, then the actions — two ways of speaking, two separate lines, and it doesn't get confused. Wrong? Add one more line. That's also the old Five-Rules rule: one thing at a time."*

**Watch for:** the #1 reason buttons don't respond: flash mode never exited — the mantra *"No response? Slide it (back to run mode)."* The TA checks this first.

**Pitfalls:**
- Text overflowing the screen / color not showing: don't teach parameter concepts — one sentence: *"This is exactly the precision problem of 'describing looks' — add one more line of description and have it change."*
- Someone is already making a game with the joystick: don't forbid — set the boundary: *"Fine to play — but the two-screens requirement stays."* Game impulse is the best driver there is; guide it, don't dam it.

**15:20–16:00 ｜ Free round: a small two-screen switcher** [You Do]

**Say this:** *"Free build, one-line brief: make something with two screens, and switch between them with a button or the joystick. A clock / a mood display / a stopwatch / a menu of your own / a reaction tester (the screen turns green, you press A, it shows your milliseconds — naturally two screens)… anything works (screen content in English, numbers or graphics). You now have five inputs in your hands — button, joystick, microphone, light, accelerometer — pick what's comfortable. Old discipline: tell your neighbor what your two screens each look like BEFORE you touch the keyboard — position, size, color, said clearly — then talk to AI."*

**Watch for:**
- Collect 1–2 cases of "described unclearly → AI drifted off" (the drift gallery needs them next).
- Fast students: add a sensor link to the two-screen project (an input just lit up in the micro-experiments, reaching back into the build — e.g., auto-switch to a night screen when it gets dark).
- Slow students' bar: the counter + one custom change.

**Pitfalls:**
- A student dumps the whole job on AI at once (*"make me something with a clock and a stopwatch and a menu"*): the old line — *"Directors shoot one scene at a time. Get the first screen described beautifully, then the second, and only at the end how to switch."*
- The two screens won't come together and it degrades to one screen: lower the bar to "counter + one custom change" and have them write into the log "where I got stuck trying to make two screens."
- Someone's screen looks great and people gather: invite them to project it — but push one question: *"What exactly did you say to AI?"* — let the whole class hear that description; the wow has to land on a reusable way of saying it.

📌 **Output anchor:** everyone copies one line into the workbook — "the sentence I said to AI about my screen" — their proudest description.

**16:00–16:10 ｜ The drift gallery (this lesson's signature segment)** [We Do]

**Say this:** (project the drift case) *"Whole room, come look at a treasure. (project) See: they said ___, AI made ___. Which sentence went wrong? (lead the class to find it) There — they forgot to say where. Thank this student — they stepped in the pit so the whole class doesn't have to. A crash isn't a joke; it's teaching material."*

**Watch for:** the volunteer is always voluntary; no volunteer → use the pre-made case from Rehearsal 5; once someone volunteers, the pre-made case is dropped. The tone of this segment is set — the volunteer is the hero; anyone snickering, take the line back on the spot: *"They stepped in the pit for the whole class. That's a hero."*

**16:10–16:20 ｜ Wrap: three takeaways for using it well + the AI log** [I Do]

**Say this:** *"Last question: what's different between describing a screen to AI and describing logic? (lead them to: logic says 'do this when that happens'; screens say 'what something is, where it sits, what it looks like') — so, three takeaways for using this handheld well. First: describe a screen with position, size and color — you saw it with your own eyes; say the three things or don't, and you get two different things. Second: make state visible — the board has a screen; have it show you where it is in its steps, so you always know what it's doing. Third: with many inputs, try combinations — button, joystick, microphone, light, accelerometer — the best projects often come from trying 'which input feels most natural.' — Now today's log: take a photo of your screen project, say thirty seconds, the same four sentences: made ___ / stuck on ___ / then ___ / next time ___. Today's 'stuck on' — a lot of you will say 'I didn't describe the screen clearly' — make it specific: was it position, size, or color? Send it to AI: 'Tidy this into a log — only what I said, nothing I didn't say.' When it's done, read it. AI will make things up with a straight face. Proofreading is your job — nobody can do it for you."*

**Watch for:** the TA takes extra build photos (hands only, no faces); students without phones get photos taken by the TA, filed by table number.

📌 **Output anchor:** ① circle one of the three takeaways — "the one I used most today was #___"; ② the log's four sentences (proofread version) go into the workbook — today's "stuck on" must name position, size or color.

---

### The 30-minute buffer (16:20–16:50)

**Say this** (set the tone at the start, per the exit you chose before class): *"Next 30 minutes work like this: if your two-screen project isn't done, finish it — that's the line everyone must cross today. Crossed it? [announce today's plan: take a challenge task / help your neighbor / add a sensor link to your project]."*

**Watch for:** circulation order — first sweep who hasn't crossed the line (the TA watches these), then lead the fast ones through challenges. Challenge tasks (described aloud; only the ones you rehearsed): **electronic dice** — shake it or flick the joystick once, the screen shows a random 1–6; **balance-ball hole-in-one** — micro-experiment 5 plus a target hole; the buzzer beeps when the ball drops in. Challenge done? Steer toward one line: *"You've got the joystick down — later it becomes a controller for your computer. That's the road ahead."*

**Pitfalls:**
- A student says "I'm done, can I leave / can I play on my phone?": no leaving — point to the three exits: *"Help a neighbor, take a challenge, or add a sensor link to your project."* The buffer is part of the lesson, not early dismissal.
- The whole class clears the bar with 20 minutes left: don't drag — move into the show & tell early and finish the wrap at a relaxed pace.

📌 **Output anchor** (for students who did a challenge): one line in the workbook — "I used ___ (which input) to make ___ (what little thing)."

---

### Wrap ｜ Flash show & tell + next-lesson preview (16:50–17:00)

**Say this:** *"In your table, 30 seconds each: demo your project, say one line — 'which input I used, and how I switch screens.' (after the show & tell) Last two minutes — take stock. One: you met the new gear — the Wio has a screen, buttons, a joystick and three sensors, and you lit every one of them up yourself. Two: you learned lesson one of using it: describe a screen — position, size, color — and your project has a real interface from today. Next session is a big day: we give AI a team — so it's more than one person working for you — and build one complete project end to end: your own smart Pomodoro timer. It runs on this very color screen, so today's screen skills get used all the way through. Bring your topic. Class dismissed!"*

**Watch for:** after class, collect today's work — online docs by link, handwriting by photo; whether you got it all, make a note. Leave the mantra cards on the desks (collect them — they're reusable next session).

---

## 四、Live Demo Backup Plan at a Glance

| Demo | Used at | Rehearse | Backup asset | If it goes wrong live |
| --- | --- | --- | --- | --- |
| Warm-up "HELLO on screen" | 14:13 | Rehearsal 1 | Spare machine + a working project for instant re-flash | Swap to the spare machine; flash-mode trouble → whole-class self-check with the mantra card |
| The 5 "light-it-up" micro-experiments | from 14:28 | Rehearsal 2 | One success screenshot per line | Resend the rehearsal-proven wording; still fails → project the screenshot and talk through it, students jump to the next line — the rhythm must not collapse |
| Screen-comparison experiment (really sent twice) | 14:50 | Rehearsal 3 | One screenshot of each result | Compare via screenshots; if AI did well both times, use the old line to land the point |
| Button-counter demo | 15:00 | Rehearsal 4 | Spare machine + a working project for instant re-flash | Swap to the spare machine |
| Drift-gallery case | 16:00 | Rehearsal 5 | Pre-made drift case (with the three-line annotation) | No volunteer → use the pre-made case; the teaching point stays |

---

## 五、Pitfall Speed Sheet

Remember the three moves first: **swap, cut to backup, ask AI.** Today's fourth: knowing is hands-on — stuck on a line? Send a different line and keep going, never lecture.

| Situation | What you do |
| --- | --- |
| ⭐ Flash-mode confusion (Wio-specific) | The sticker + the whole-class drill at the start are built in; still happens mid-class → the mantra card on the desk: *"No response? Slide it."* |
| ⭐ A micro-experiment line stalls for the whole room (AI's code won't run) | Resend your rehearsal-proven wording; a single dead unit gets swapped, not fixed; one experiment stuck more than 2 minutes is too long — protect the round's rhythm |
| ⭐ The buffer turns into free time | Set the tone at the start by announcing the exits; circulation rule "standard first, then fast"; someone wandering → hand them a challenge: *"Electronic dice — want to try?"* |
| Screen text overflows / colors smear | *"That's exactly the precision problem of describing looks — add one more line of description and have it change."* No parameter concepts |
| Chinese display garbles / tofu blocks on screen | Today's display is English/numbers/graphics by design; if it appears anyway, tell AI *"change all on-screen text to English"* — don't debug the font library |
| A student is obsessed with the joystick game | Don't forbid: *"Fine — but the two-screens requirement stays."* Guide, don't dam — the joystick is one of today's stars anyway |
| Drift gallery: nobody volunteers | The pre-made case is the fallback; someone mocks the volunteer → take the line back on the spot: *"They stepped in the pit for the whole class. That's a hero."* |
| A student presses on internet / SD card / more features | *"It can — that's a later lesson. Today, just remember it exists."* No expansion |
| Internet dies during build time | If it's not back within 15 minutes: micro-experiments and screen descriptions finish on paper first (lines written out, neighbor reviews the description); flashing practice defers |
| Log becomes empty fluff | "Stuck on" is required; today's "stuck on" must be specific — position, size, or color |
| Student has no phone for the log | TA photographs everything, filed by table number; the spoken part stays |

### Bonus: student questions and how to catch them

| Student asks | You say |
| --- | --- |
| "Which board do I use from now on — Wio or the first one?" | "Both. The first one is strong at sensing the world; this handheld is strong at letting people interact with your project. When your big project needs someone to press buttons and look at a screen, that's when you use it." |
| "Can the joystick work like a mouse? Can it control the computer?" | "It can — the board becomes a computer peripheral, controlling things on the screen. That's the road ahead. First, get good at the interfaces on the board itself." |
| "Do I need the SD card slot now?" | "Not today. Knowing it can store things is enough — when your project needs to remember data, that's when it steps in." |
| "Can the Wio connect to the internet?" | "It can — it has wireless. Connecting is a later lesson. Today, just remember it exists." |
| "I don't know which of the five inputs to use." | "Work backward from what you want to solve: needs a hand pressing → button or joystick; needs to hear something → microphone; needs light and dark → light sensor; needs to know if it's moving or tilted → accelerometer." |
| "AI keeps getting my screen description wrong — am I dumb?" | "No. Describing screens is a separate craft, and today is day one. Remember three things: position, size, color — next time, just say all three and watch." |

---

## 六、Prompt Phrase Library (instructor reference)

Today's phrases: the 5 micro-experiment lines + the "how to describe a screen" phrase. Full text below — read before class, project when you need them. **These are not printed or handed out** — they're in the Student Workbook; project and read together when they debut, point students to the book when they forget. If the workbook wording differs slightly from here, either works; the meaning is the same.

### The "Light It Up" micro-experiment lines (for the gear round — one line lights one hardware point)

Students wrap every line in the standard frame: *"I'm using the Wio Terminal. Please make this work: …"* The five toys:

1. **Three-key piano (buttons)**: *"Press buttons A/B/C to play do, mi, sol. Show DO / MI / SOL in large text on the screen."*
2. **Push the ball (joystick)**: *"Draw a small ball in the center of the screen. Push the joystick and the ball moves that way."*
3. **Blow out the candle (microphone)**: *"Draw a lit candle in the center of the screen. Blow at the microphone and the flame goes out; after 2 seconds it lights again."*
4. **The board afraid of the dark (light)**: *"Draw two open eyes on the screen. When the light gets dim, close the eyes and show ZZZ; when it gets bright, open them again."*
5. **The balance ball (accelerometer)**: *"Draw a square frame with a small ball inside. Tilt the board and the ball rolls toward the low side."*

- Usage rule: one line lights one hardware point (Five Rules: one thing at a time); students may read the line as-is or swap in their own play (*"beep twice when I press B"*) — **lit up counts as lit up**.
- Downgrade fallback (the original "number-report" versions — use when a new line won't run in rehearsal): ① *"When I press button A, the buzzer beeps once and the screen shows the letter A."* ② *"When I push the joystick up, show UP; down, show DOWN; left, LEFT; right, RIGHT."* ③ *"Show the sound level in large numbers in the center of the screen."* ④ *"Show the light level in large numbers in the center of the screen."* ⑤ *"Show the X-axis value on the screen; tilt the board left and right and watch the number go positive and negative."*

### The "how to describe a screen" phrase (for stating a screen requirement)

> At [position], show [content] in [size/color]; when [action], [change].

- Example: *"Show a number in the exact center of the screen in the largest red text; when I press button A, add one."*
- Today's on-screen content is always English / numbers / graphics (the board's Chinese font library is unreliable — no font roulette).

---

## 七、Localization Slots

| Slot | Original | Swap in |
| --- | --- | --- |
| 14:13 warm-up display content | [HELLO and my name (pinyin or English)] | words your students feel more strongly: their team name, their game character's name — lights up faster |
| 14:28 micro-experiment lines | [UP/DOWN/LEFT/RIGHT etc.] | local flavor is fine (a slang "up/down" word in the direction line) — keep the display in English |
| 15:20 free-round examples | [clock / mood display / stopwatch / menu of your own] | add local hooks — "a countdown to market day," "a scoreboard for the big match" |
| 16:50 closing preview project | [smart Pomodoro timer] | don't swap it (Lesson 4's design is already set), but localize the explanation: "a Pomodoro = a focus timer — 25 minutes focused, 5 minutes off, that kind of thing" |

---

## 八、Teacher Reflection Page (10 minutes after class — every line becomes the next version's saved pitfall)

1. Which segment went best? Which one do you most want a do-over on?
2. Any 🗣️ line that felt stiff to say aloud — not like a human? Cross it out, write what you actually said.
3. After the walk-around, how much did students actually remember? Which part was the favorite?
4. Which of the five micro-experiments worked best, which stalled? Did the round's rhythm ever collapse?
5. How many flash-mode fumbles happened? Were the stickers and the drill enough?
6. How did you actually use the 30-minute buffer? How many challenge tasks went out, and what share ran successfully? Did it turn into free time?
7. Timing: which segment ran over, which ran short?

Write it up, photo it, send it to the teaching group, or tuck it back in the courseware. **Every line you fill in is a pitfall some other teacher doesn't have to step in.**

---

_Source: 中文版 v2 ｜ English v1 (2026-08-25) ｜ Design base: B1 v1 / X6 v1 / CFG-5 spec v1.0 ｜ Timetable: sample 14:00–17:00, shift to your actual start time ｜ Note: this is the "gear lesson" — the main line is meeting the Wio Terminal and using it well; team-building content (originally Lesson 3) moved to Lesson 4_
