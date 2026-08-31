# Teacher's Guide ｜ Lesson 6 · Move Your Project Home

_The Big Move: from the Web into Your Own Computer ｜ Chaihuo Maker Academy · M0 Hardware Foundation · Smart Hardware Fundamentals ｜ 10-session term ｜ 3 hours (no scheduled break)_

> **Source:** 中文版 v3（M0_教师课件_CFG-5_第6课_把作品搬回自己的电脑_v2.md，文件名写 v2，文末修订说明含 v3：2026-08-07 对齐同事扩充版 PPT 19→51 页、自检四勾改三勾、Grove 单线口径更新）
> **Localized edition** — same blocks, same minutes, same teaching intent; classroom language rewritten for an English-speaking teacher to pick up and teach from.

---

## The one-sentence brief

Today is the **biggest pivot of the whole course**: students move their projects out of the browser (Codecraft) and into a new tool installed on their own computer (**aily-blockly**). **Installing is homework done before class** — class time only checks it off. Three main courses: ① **the two-views moment** — the floor gets lifted for the first time as students *read* the code AI has been writing for them all along (blocks view ⇄ code view); ② **a brand-new local project built under AI guidance** — the **night-light** (Grove Beginner Kit, onboard light sensor + LED, zero wiring); ③ **the joint project "dusk alarm station"** — Grove Beginner Kit and Wio Terminal each run their **own program** and **link through one signal wire**: the Beginner Kit is the **lookout** (senses darkness), the Wio is the **alarm post** (shows and sounds the alarm). The house is set up — next session, the marathon starts.

The session runs ten blocks: **ceremony opener** (8 min) → **install checkpoint** (10 min) → **meet the new home** (12 min) → **unpack your old project** (15 min) → **the two-views moment** (30 min) → **bridge** (5 min) → **night-light project** (40 min) → **dusk alarm station** (45 min) → **wrap-up** (10 min) → **close** (5 min). **No scheduled break** — students use the bathroom on their own during hands-on time. Devices stay on; conversations stay open.

**Today's iron laws:**
1. **Installation is settled before class — never gamble on the spot.** T-7 trial install + the class-group install assignment 3 days out + the 30-minute pre-class **install window**. In class, the **install checkpoint** closes the door at minute 18 — anyone not installed pairs up (commander mode).
2. **The two-views moment's 30 minutes are untouchable** — it is one of the reasons this lesson exists.

---

## 🎯 Learning Objectives

*By the end of this session, students will be able to…*

1. **Run** a project in a local tool and **find it** in its folder ("it's here, and it's always here"); explain the difference between the old home and the new home (*Bloom: Apply*).
2. **Point to** one place where a block and a line of code correspond, and **change one line** (the first time they touch code by hand — and it doesn't break) (*Bloom: Apply*).
3. **Complete** one full lap of the engineer's loop — *say it → AI builds → check → upload → verify* — the motion every lap of the marathon will use (*Bloom: Apply*).
4. **Explain** how two boards share one system — who senses, who performs, and how the signal wire connects them — their first time linking two functions into one whole (*Bloom: Explain*).

---

## Page One — read this before class starts

### What today produces (four student outputs)

1. **One local project that runs** — and it lives in a folder they can point to; the ownership ritual completed (save → open the folder → see it's there);
2. **One block ⇄ code correspondence** — found, pointed at, and one line changed (the "change one line" experiment);
3. **One complete lap of the engineer's loop** — say it → AI builds → check → upload → verify, on the night-light project;
4. **One two-board system explained** — who senses (the lookout), who performs (the alarm post), and how the signal wire links them.

### Three things you need to do

1. **Follow the clock.** Work down the timeline; every block says how many minutes and what to do.
2. **Read the lines.** Every 🗣️ line is pre-written classroom speech — read it as-is, don't improvise.
3. **Guard the two iron laws.** The install checkpoint closes at minute 18 — after that, no more installing, everyone pairs up. And the two-views 30 minutes are never squeezed.

### Three things you do NOT need to do

1. **You don't need to install anything for students.** Installation is homework (T-3 class-group assignment) plus the pre-class install window. In class you only *check off* — the three-check self-test.
2. **You don't need to read code.** The two-views moment only asks students to *find one match* between a block and a line — one correspondence is a pass. Nobody reads the whole program today.
3. **You don't need to fix students' machines.** Swap, cut to backup, ask AI — in that order. Permissions problems follow the downgrade playbook in 4.1.

### When things go wrong

- **Live demo fails:** switch to the backup within 30 seconds (T-7 recording or the teacher machine's pre-installed aily-blockly), using Section 4's speed sheet. **This is not an incident — the plan is designed for it.**
- **Student device fails:** swap the device or the cable. Don't repair.
- **You're stumped:** smile, and say *"Let's ask AI together."*
- One-liner: **swap, cut to backup, ask AI.**

---

## Before Class

### 1.1 A week ahead (T-7 — the biggest flip-risk point in the whole configuration)

> Each item maps to config spec §5.2. Check them off one by one; every red light has a prescribed action.

- [ ] **Re-confirm two permissions with the IT office, in writing:** software installation permission + USB serial-port permission (school lab restore images / domain policies may block them — written confirmation required).
- [ ] **Full trial install on one lab machine:** install aily-blockly from the installer → open it → connect a board → flash successfully. **Record the whole thing on video** (it becomes the class-group install tutorial + the on-day fallback screen).
- [ ] ⭐ **T-7 decision point:** trial install fails and can't be solved today → **report to the teaching lead immediately and start the fallback "Codecraft deepening track":** this lesson becomes a "Codecraft polish round + the two-views concept demonstrated on the teacher machine"; Lesson 8's marathon proceeds as planned (Codecraft as the build platform); Lessons 9–10 unchanged. **Decide a week out. Never gamble on the spot. If we've fallen back, this guide stays in the drawer — don't force it.**
- [ ] **3 days before, send the install assignment to the class group** (text in 6.6): installer link + the T-7 recording tutorial + the three-check self-test — installed before class; parents may do it for them; the student themselves only needs to be able to open it and connect a board.
- [ ] **30 minutes before class, open the install window:** students who didn't finish / have no computer at home arrive early; TAs install with them. Distribution method is your call — USB drive, cloud link, AirDrop — **but keep at least one offline option** (e.g. a USB stick with both Win and macOS versions).
- [ ] Confirm **student:TA ratio ≤ 6:1**.
- [ ] **NLHD link ready** (projected at wrap-up + sent to the class group); the "two buttons that matter," install self-test, two-views cheat sheet, and new-project prompt all queued for projection (Section 6) — **this lesson prints nothing**.
- [ ] Teacher rehearsals (see 1.3).

### 1.2 On the day (arrive ~1 hour early)

- [ ] **Install window set up:** installers in place by your chosen method (e.g. USB sticks split across several machines); double-click each one to confirm it launches.
- [ ] **Re-check USB serial permission** — night policies sometimes change things: plug in a board and trial-flash once.
- [ ] **Grove Beginner Kit: 1 per student + 2 spares; Wio Terminal: 1 per student + 2 spares** (the joint project needs it); **Grove cables: 2 per student + spares** (signal wire + shared ground).
- [ ] Screen queue ready: the T-7 recording (backup) ／ your own pre-installed aily-blockly (demo + fallback) ／ all Section 6 screens.
- [ ] **Whiteboard: today's route map** — *checkpoint → tour the new home → unpack the old project → lift the floor → build something new with AI*.

### 1.3 Rehearsals (run it yourself before class)

1. **Full walk:** open the tool → redo "show your name on screen" → save → find the project folder in the file manager → close and reopen (confirm "it's there");
2. **The two-views three-step:** drag a block and watch where the code changes → select a code snippet and ask AI "what's this doing?" → change one display line and run it;
3. **Run the night-light end to end with the 6.4 prompt on a Grove Beginner Kit:** say the need → AI builds → upload → read the light value on the serial monitor (A6) → deliberately cover the sensor to verify. **Time it — over 15 minutes means you're not fluent; practice more;**
4. **Run the dusk alarm station end to end with the 6.8 three-part prompt:** flash both programs → connect signal wire + shared ground → cover the sensor and watch the link. **Deliberately step on the "no shared ground" pitfall once** and note what you see (live teaching material for class);
5. **Break a line of code on purpose, then rescue it with "go back to the last version"** (real footage for the save-talk).

### 1.4 Supplies: three buckets

**📦 In the kit (count only, nothing to buy)**
- Computers (the lab); Grove Beginner Kit (1 + 2 spares each); **Wio Terminal (1 + 2 spares each)**; Grove cables (2 + spares each); USB data cables; circulating tablet; projector; whiteboard; teacher machine (pre-installed with aily-blockly).

**🛒 You buy**
- **Nothing.** Installer distribution needs no purchase — USB drive / cloud link / AirDrop, whatever's on hand (**keep one offline option as the safety net**).

**🖨️ Printing**
- **None. This lesson prints nothing.** The install assignment goes through the class group; the two buttons, self-test, cheat sheet, new-project prompt, and NLHD link are all on screen (the student workbook is shared read-only — nothing gets written in it today).

---

## Session Map (14:00–17:00 — shift the whole clock to your actual time, e.g. 9:00–12:00; block lengths stay. No scheduled break.)

| Clock | Block | Students are… | You are… |
| --- | --- | --- | --- |
| 14:00–14:08 | Ceremony opener | watching the close-the-tab demo, hearing the tenant→owner pitch | doing the 30-second look-back + the close-the-tab demo |
| 14:08–14:18 | Install checkpoint (**red line at 14:18**) | running the three-check self-test; unpairing if not installed | closing the door at 14:18, pairing the rest (commander mode) |
| 14:18–14:30 | Meet the new home | hearing the three facts, building an empty house (4 steps), touring the 3 rooms | leading the tour, screening the board-picker photo |
| 14:30–14:45 | Unpack your old project | rebuilding "show my name" in the new tool, timing themselves | running the "I bet you finish in half the time" pitch; guarding the ownership ritual |
| 14:45–15:15 | **The two-views moment (main course 1 — untouchable 30 min)** | find the match → ask AI → change one line, all together | running the only whole-class led segment of the lesson |
| 15:15–15:20 | Bridge: three layers of value | hearing the point | pointing: it's yours / you're not afraid of it / the door opened |
| 15:20–16:00 | New project 1: the night-light (main course 2) | running the engineer's loop solo from the workbook | one whole-class call at 15:35; circulating: watch the chat / the serial / the LED |
| 16:00–16:45 | Joint project: the dusk alarm station (main course 3) | splitting the job, flashing both ends, linking with one wire | two whole-class calls; circulating: division / solo-run / the Grove cable |
| 16:45–16:55 | Wrap-up | writing the 4-line log, noting the NLHD link | running the three-sentence summary + the spec→function→system line |
| 16:55–17:00 | Close | packing up, log finish | reviewing the four wins, previewing Lesson 7 (project briefing) |

> No clock-face minutes are printed in the source — you start whenever class starts and work down the lengths above. **No unified break all session.** The new 51-page deck has each step split into its own page with screenshots and build-along notes — just follow the pages.

### 2.1 Time flexibility

- **Most compressible:** unpack the old project (15→10 min, keeping only the save→confirm ritual); the bridge (5→2 min).
- **Next compressible:** the joint project (45→35 min — release once both programs are flashed and the signal wire has linked once; the Wio's display flourishes are after-class play); the night-light (40→32 min — slow students release on "one example need runs through").
- **Never cut:** **the two-views 30 minutes**; **the install-checkpoint red line** (the three checks must pass before you move on); the 30-second look-back.

### 2.2 TA split (three TAs is today's design; two works — merge C into B)

| When | TA A (install officer) | TA B (tech officer) | TA C (pace & record officer) |
| --- | --- | --- | --- |
| Pre-class install window | the main force in the window | permission cases one by one | — |
| Install checkpoint | circulating the three-check self-test; pairing the uninstalled + logging the after-class follow-up list | — | holding the red line at 14:18 |
| Night-light project | — | wiring checks (which port is the sensor in), upload-failure cases; permission cases per 4.1 | keeping time; collecting student one-liners ("what did I understand" / "how many tries until my need was clear") for the showcase |
| Joint project | — | same + the Grove cable: is it in the right port, is it **clicked in firmly** (signal and ground are both inside this one cable — don't add a second ground wire) | same |
| **Both project blocks: all three TAs on the floor** — the highest TA density of the course. | | | |

---

## Section 3 · Segment-by-segment script

### Segment 1 ｜ The ceremony opener (14:00–14:08)

> Goal: 30-second look-back, set the tenant→owner pitch, demo the close-the-tab moment, preview the five steps on the board. Deeper goal: this is a celebration, not a chore — the teacher's own energy is half of this lesson's success.

🗣️ **Say this** (the tone-setter, read as-is):

> "30-second look-back: last session, you taught your hardware to see — you ran a ready model, then trained a model that's entirely yours. From Lesson 1 to now, your projects keep coming, and they keep getting better."
>
> "Today we don't create. Today we do one big thing: **until now, your projects have lived on someone else's server — close the browser, and they're gone. Today, you move from tenant to owner.**"
>
> *(demo: close the Codecraft tab)* "See? Closed. Where's your project? — At someone else's house. *(open a local folder)* Now look here: after class today, your project will live in this folder. Unplug the internet — it's there. Shut down the website — it's there. Ten years after graduation — it's still there. **Moving isn't a step back — it's buying the house.**"
>
> "The install assignment — most of you did it. Didn't finish? You'll pair up in a minute; nothing to be ashamed of. Once the house is set up, what's next? — Next session, you **give your project a brief**: the topic grows out of your own experience, not copied from the internet. Brief done, the marathon starts. Today's five steps *(point at the whiteboard)*: checkpoint → tour the new home → unpack the old project → lift the floor → **build something new with AI.**"

👀 **Students do:** watch the close-the-tab demo; listen.

⚠️ **Pitfalls:**
- "Why move if the web version works fine?" → "The web version isn't retiring — during the marathon you'll use both. But the feeling of owning it — you have to taste that once today."
- Flat energy → this is a celebration, not moving day: over-act the opener if you have to. Your energy is half the lesson.

---

### Segment 2 ｜ The install checkpoint (14:08–14:18 — the red-line transition)

🗣️ **Say this:**

> "Finished your install homework? Open the tool, fill in the self-test on screen (it's in your workbook too): three checks — it's installed ／ it opens ／ I can reach the main screen."
>
> "Not done — raise your hand. No more installing now; you pair up on the spot: share one computer with your neighbor, you're the **commander** — you say what to do, they press the buttons. Give your name to a TA; we'll make sure you're set up within 10 minutes after class."

👀 **Students do:** the three-check self-test; the uninstalled pair up and split roles.

⚠️ **Pitfalls:**
- **More than 1/3 not installed** → the homework pipeline broke: extend this block 5 minutes for a focused group install (all TAs on it); whoever still isn't done pairs up; note it on the reflection page (review the assignment copy / timing).
- Installed but the board won't connect → TA B handles one-on-one (cable, port, permission); not fixed in 5 minutes → pair up.
- Whole-room permission block (a night policy change) → execute the 4.1 downgrade.

---

### Segment 3 ｜ Meet the new home: aily-blockly + build an empty house + tour (14:18–14:30)

🗣️ **Say this** (first 4 minutes — the tool intro, read as-is):

> "Every house needs a name — this one is **aily-blockly**. Three facts, and that's it. **One: it's open source and free** — the site is yiyu.pro, anyone can install it. **Two: it's universal** — not some one-board companion app; it takes 100+ development boards, so when you change boards later, it's still your home. **Three: it's AI-native** — say what you need, get a wiring diagram, get code, get errors fixed — AI is there the whole way."
>
> "The third one matters most: the people who built it set out to break the line between professional and amateur — to let anyone make hardware with plain language. **It was built for you.** The old home got you daring quickly; the new home gets you finishing properly."

🗣️ **Say this** (2 minutes, screen the board-picker photo):

> "Words are cheap — look at the real thing (point at the screen). This is the first screen aily-blockly shows: pick your board. Look for it: **Grove Beginner Kit is in there — and so is Wio Terminal.** That's what 'universal' means. Whatever board you use next, it's got a place here."

🛠️ **Build-along** (the four-step build; the deck splits it into its own pages with screenshots — follow the pages):

> "Intro done — time to build your first empty house. Four steps: new project (pages 6–7) → pick the board: today, **Wio Terminal** (page 8) → name it: **use English**, and point the save path at your projects folder (page 9) → create (page 10). The sign it worked: you're in the blocks screen, and the folder already has it."

🗣️ **Say this** (then the three-room tour):

> "Tour the new house — three rooms. First room (open the file manager): **this is where your projects live from now on.** This folder *is* your project — copy it out and it's portable, send it and it's shared. Second room (back to the tool): **this is the blocks view** — drag and drop, same graphical feel you already know. Third room (click the code view): **this is the code view** — one of today's main courses; we lift that floor in a few minutes."
>
> "Whatever buttons there are, remember just two today. **One: AI coding** — tell it what you need in plain language, it writes your code and fixes your errors; today runs on it. **Two: flash** — click, and the program goes into the board; know what the 'upload' button looks like. Every other button — ask AI when you need it. It knows them better than you."

👀 **Students do:** follow the tour; point to where "AI coding" and "flash (upload)" live in the interface.

⚠️ **Pitfalls:**
- Can't find the project folder in the file manager → whole-class sync: "Where I click, you click — found it? Hands up." Paired groups: the installed partner operates, the other points.
- "Can I copy it to a USB stick and take it home?" → "Of course — that's the whole point of moving. But not today — there's plenty of time before the Lesson 10 showcase."

---

### Segment 4 ｜ Unpack your old project (14:30–14:45)

🗣️ **Say this** (the anti-"boring" frame):

> "First thing after moving in: put out your most precious old thing — **your very first project: showing your name on screen.**"
>
> "Don't roll your eyes. In Lesson 1, how long did it take you? (wait for answers) Timer starts now — I bet you finish in half the time. This isn't repetition; it's watching yourself grow in real time."
>
> "The one step that matters most when you're done: **save, then open the folder and see it with your own eyes.** That ritual has a name — the **ownership ritual**. From today, every project you make takes this step."

👀 **Students do:** rebuild "show my name" in the new tool (AI-coding entry + the flash five-step, pages 14/16 — the rule: **pick the right port first, then click upload**); compare the time; save → folder → confirm.

⚠️ **Pitfalls:**
- "This is boring" → the frame is built in; if they still resist, let them redo *any* old project (not just the first) — but **the ownership ritual is never skipped**; fast students go straight into the 3.7 night-light block (give them the prompt early).
- Paired groups → **both students must do the save→folder→confirm run themselves** (acceptance: each partner operates independently).

---

### Segment 5 ｜ The two-views moment (14:45–15:15 — main course 1, the untouchable 30)

> This is the lesson's **only whole-class led segment** — everyone synchronized.

🗣️ **Say this:**

> "All eyes on the big screen. I'm lifting the floor. (switch to code view) **This is what AI has been writing for you all along.** From the first time you said 'show my name on screen,' it has been writing this every time. Today, we look at what it looks like."
>
> "Three steps, follow me. **Step one: find the match.** Go back to the blocks view, drag one block — watch: what changed over here in the code? (wait for someone to point) Right — this one block is these few lines. Blocks and code are **two looks at the same project** — blocks are for hands, code is for machines."
>
> "**Step two: ask AI.** Select a chunk of code you don't understand, send it to your AI (project the prompt): **'What's this code doing?'** Have it explain in plain language. From today, AI has a new job: not just doing the work for you — **teaching you to read it.** Old rule: ask in the conversation you already have open. No new windows."
>
> "**Step three: change one line.** Find the line that shows your name — change only the letters inside the quotes to your nickname. Run it. (wait) See that? **You just touched code with your own hands — and you didn't break it.** Changing a letter can't break it. That's your first time."

👀 **Students do:** the three steps; paired groups alternate.

⚠️ **Pitfalls:**
- The code view scares someone off → "You don't need to read it all — today is about one feeling: *code is not mysterious.* Find one match, and you graduate." Still scared? Step one only; steps two and three optional.
- They break a line (deleted a quote or bracket) → teach the save, on the spot: "No panic — go back to the last version. See? This is why engineers save constantly: when you break it, you can go back."
- Someone wants to change *logic* (numbers, conditions) → stop them: "Today, letters only. The fire to change logic — hold it until the marathon starts, when you have your requirements sheet."

---

### Segment 6 ｜ Bridge: three layers of value (15:15–15:20)

🗣️ **Say this:**

> "One point, then we move: why did you just do all this? Three reasons — **it's yours** (your project, your folder, your house); **you're not afraid of it** (from black box to clear box); **the door opened** (competitions, final projects, the real engineer's world — this is where you walk in)."
>
> "The door's open — now step through it. Just now you *read* what AI wrote. Next, you'll *direct* AI to write something **brand new**."

---

### Segment 7 ｜ New project 1: the night-light (15:20–16:00 — main course 2)

🗣️ **Say this** (method frame, project the loop diagram):

> "Engineers working in a local tool run on this loop (point, read the five stations): **say it → AI builds → check → upload → verify.** Verification fails? Back to the first station — say the need more clearly, run another lap. **This loop is the motion of every lap of the marathon** — today we get fluent on a small project."
>
> "How do you say a need clearly? You already know — the three boxes: what it senses (input), what it does under what condition (logic), how it shows itself (output). Say the three boxes in plain language, and that's a good need."
>
> "The first new project: **the night-light.** Uses the Grove Beginner Kit in your hand — light sensor and LED are built into the board, **not a single wire to connect**, short code, fast upload, verdict in two minutes. Dark — light on. Bright — light off. Use the prompt on screen (6.4); **leave the number in brackets blank** — what the sensor actually reads, you'll see on the serial monitor in a moment, and fill in yourself."

**Students run solo** (steps in the workbook, the loop diagram stays projected, teacher circulates only):

- **The single whole-class call** (about 15 minutes in): "Time to open the serial monitor — take the number you measured with your hand over it and put it back into your need."
- **Circulate, three things:** the conversation (is the need getting more specific, or are they re-pasting the same sentence?) ／ the serial (did the number come out?) ／ the LED (cover the sensor — does the light obey?).
- **Intervention red line: ask, don't fix** — "What number is 'dark' in your need? How do you know?" Errors go back to AI verbatim (old rule: one step at a time). No serial data? Students run their own three-check out loud: did it upload? is the monitor open? is the sensor reading?
- **Fast-lane challenge:** upgrade the need to "when it's dark, the buzzer also beeps once"; or play acceptance-tester for each other: "Cover your neighbor's sensor — does their light obey?"

👀 **Students do:** at least one solo lap of the loop from the workbook (say → build → upload → measure → fill the threshold → iterate); note in the cheat sheet "my need took ___ tries to say clearly."

⚠️ **Pitfalls:**
- What AI built is incomprehensible → normal; reach for the two-views prompt: "Select the part you don't recognize, ask 'what's this doing?' — build and understand at the same time."
- AI didn't get it on the first try → teaching point, not an incident: "See — this is iteration. Engineers saying a need three times is normal. Read your second try to the class — what got more specific?"
- Whole class stuck on the serial → demo once on the teacher machine: open the monitor, cover the sensor, read the number — 30 seconds, then back to solo running.

---

### Segment 8 ｜ Joint project: the dusk alarm station (16:00–16:45 — main course 3)

🗣️ **Say this** (system frame, project the division-of-labor diagram):

> "Just now, one board worked alone. Now, upgrade: **two boards work together** — and that's what the real world looks like: a doorbell — one button outside, one speaker inside, each doing its own job, one wire between them."
>
> "The joint project: **the dusk alarm station.** The Beginner Kit is the **lookout**: when it's dark, it lights its own LED and 'raises its hand' on a signal pin. The Wio Terminal is the **alarm post**: when it sees the hand go up, the screen says 'It's dark!' and the buzzer beeps once. **Two boards, two programs, each minding its own job, linked by one wire.**"
>
> "The need also splits into two parts — first have AI sort out the division and the wiring (prompt 6.8, part one), then ask for the two programs (part two, part three). **Same conversation window — AI remembers the whole picture.**"

**Students run solo** (steps in the workbook, teacher circulates only):

- **The two whole-class calls** (about 15 and 30 minutes in): "Both programs flashed? Run each board solo first — then link them"; "Linking check, two things — is the Grove cable in the right port? **Is it clicked in firmly?** (signal and ground are both inside this one cable)."
- **Circulate, three things:** the division (can they say who senses and who performs?) ／ solo-run first (each end runs alone before linking — no skipped steps) ／ the Grove cable (**nine dead links out of ten are a wrong port or a loose cable**).
- **Intervention red line: ask, don't fix** — "Which pin is the lookout's hand? How does the alarm post know?" Wiring questions go to AI for a diagram (it was asked in the prompt) — the teacher doesn't check wires for them.
- **Fast-lane challenge:** upgrade the alarm — the Wio screen shows the current light reading; or add "press the Wio button to manually clear the alarm"; or flip it: the Wio becomes the lookout (it has a light sensor too), the Beginner Kit's buzzer becomes the alarm post.

👀 **Students do:** the joint three steps from the workbook (split the job → generate and flash both programs separately → link and verify); note in the cheat sheet "our link's first failure was because ___."

⚠️ **Pitfalls:**
- Link dead → the three checks: did each board run solo? is the signal wire on the agreed pins at both ends? **is it clicked in firmly?** Still dead: unplug and re-seat, or swap in a fresh Grove cable; if it persists, demo one working pair on the teacher machine.
- One board is "occupied" by the computer, the other won't flash → normal: flash the two boards alternately on one computer, or split across the pair's two machines.
- "Why not just use one board?" → "One board could do it — but in real engineering, sensing and performing often don't live in the same box. Today, between two wires, you saw a *system* for the first time."

---

### Segment 9 ｜ Wrap-up (16:45–16:55)

🗣️ **Say this:**

> "Three sentences to close (point at the whiteboard): **it's yours; you're not afraid of it; the door opened.**"
>
> "Two more from today: you can **loop** — say it, build, check, upload, verify, and if it's wrong, say it again; and you can **link** — today's alarm station is the proof: **set the spec first (the standard), build one function at a time (each board runs its own loop), then link them into a system (one signal wire).** That's how engineers take on big projects — and that's how your three marathon legs will run."
>
> *(project the NLHD link)* "This is the new home's manual — *Natural-Language Hardware Development*, 15 chapters, from lighting your first project to full systems, and every chapter drills today's loop. It's going to the class group; put it in your workbook. You don't need to read it today — open it when you're stuck."
>
> "Log time. Four lines as usual — the 'done' line is required: **today I built ___ with AI guiding me, and I linked it to another board; our link's first failure was because ___.**"

👀 **Students do:** note the link; write the log (four-line template, same wording as always); the cheat sheet stays in the workbook.

⚠️ **Pitfalls:**
- A student can't write the log → point at their cheat sheet: "Five stations of the loop — where were you stuck, and how did you get past it? Write that. One sentence is enough."
- "I want to play with it at home" → "That's exactly what it was installed for — it's on your computer, play all you want. And the manual's in your hands."

---

### Segment 10 ｜ Close (16:55–17:00)

🗣️ **Say this:**

> "Look back at today — four things done. One: your project moved off someone else's server and into **your own computer** — you're the owner. Two: you **read a piece of code** for the first time, and changed one line by hand — nothing broke. Three: you **directed AI to build a new project from zero** — you ran the engineer's loop. Four: you made **two boards cooperate** — one senses, one performs, one wire, one system."
>
> "Next session preview: **give your project a brief.** Good topics grow from your own experience, not from the internet. You'll write a requirements sheet: input, logic, output — and only one core function survives. Brief done, the marathon starts — today you said 'I want to build'; soon you'll say 'I'm building.'"
>
> "Project folders stay where they are. Boards in the box."

👀 **Students do:** pack up; finish the log.

---

## Section 4 · Live demo backup plan

| Demo | Used in | Rehearsal | Backup material | If it goes wrong live |
| --- | --- | --- | --- | --- |
| Close-the-tab opener | 14:00 | full walk | the local project folder pre-opened on the teacher machine | just do the folder side: "it lives here now" — the tab-close can be narrated |
| Install self-test / board picker | 14:08 / 14:18 | full walk | T-7 recording + the board-picker screenshot | play the recording; follow the pages |
| Four-step empty house | 14:18 | full walk | T-7 recording (build-along) | students follow the recording; teacher adds narration |
| Two-views three-step | 14:45 | rehearsal 2 | a pre-made "one block = these lines" screenshot + the "what's this code doing?" prompt | teach from the screenshot; students still do their own ask-AI step |
| Night-light loop (incl. serial reading) | 15:20 | rehearsal 3 | the night-light prompt text + a finished threshold number | if the serial is dead → use the teacher machine's measured value; verification becomes a demo |
| Dusk alarm station link | 16:00 | rehearsal 4 | one working pair demoed on the teacher machine | demo one working pair; if the signal wire runs short → two boards share one desk demo |
| "Go back to the last version" | 14:45+ | rehearsal 5 | the broken-code screenshot | play the screenshot; have students do the rescue on their own project |

### 4.1 Permission / fallback playbook (maps to config §5.2)

- **USB serial disabled on the day (T-7 missed it)** → this lesson downgrades to "two-views (teacher-machine interactive projection) + paper walk-through of the new-project loop": needs still written, AI builds still watched, wiring diagrams still drawn — just nothing flashes. Value kept ≈ 60%, better than canceling; the flash step is deferred until the permission is fixed.
- **T-7 fallback already decided** → this guide is not used; take the "Codecraft deepening track" instead (this lesson becomes a Codecraft polish round + two-views on the teacher machine; Lesson 8's marathon proceeds with Codecraft as the platform; Lessons 9–10 unchanged). **Don't force it, don't half-run it.**
- **Paired students** → install for them within a week (coordinate with the IT office); 10 minutes after install, they do the ownership ritual to catch up.

---

## Section 5 · Pitfall speed sheet

Three lines first: **swap, cut to backup, ask AI.** Today's fourth: **installation is settled before class — the checkpoint closes at minute 18, no exceptions.**

| Situation | What you do |
| --- | --- |
| ⭐ Homework install mostly missing | no in-class rework — the 18-minute red line pairs them up (commander mode); note it on the reflection page (assignment copy / timing review) |
| ⭐ USB serial permission blocked on site | downgrade to "teacher-machine interactive projection + paper walk-through," flash deferred (4.1) |
| "Moving is a step back / such a hassle" | "Moving isn't a step back — it's buying the house" + replay the close-the-tab demo |
| "Redoing my old project is boring" | the frame is built in; still resisting → any old project, but the ownership ritual is never skipped; fast students go to the night-light early |
| Code view scares someone | step one (find the match) only; steps two and three optional |
| A changed line breaks | teach the save: "broken? go back to the last version — that's why engineers save constantly" |
| The urge to change *logic* | "hold the fire until the marathon" — today, letters only |
| Whole class can't say needs clearly | not an incident, a teaching point: have a student read their *second* try aloud — where did it get more specific? |
| Serial shows nothing | the three-check: did it upload? is the monitor open? is the sensor reading? TAs don't operate for them |
| ⭐ Link dead (alarm doesn't sound) | the three checks: did each board run solo? is the signal wire on the agreed pins? **is the ground shared?** (nine dead links out of ten — no shared ground) |
| One board holds the computer, the other won't flash | normal — flash both boards alternately on one computer, or split across the pair's machines |
| New window opened to ask about code | the old rule: "ask in the window you already have — it knows your project, so its answer fits your code" |

### Appendix: student questions and how to answer them

| Student asks | You say |
| --- | --- |
| "Can I still use the web version?" | "Yes — in the marathon you'll use both. The old home is a hotel room; the new home is your own house — worth knowing how to live in both." |
| "What's different from Codecraft?" | "Three things: it lives on your computer (close the window and it's still there); you can see the code; it's built for projects that grow — the old home got you daring quickly, the new home gets you finishing properly." |
| "I can't read all this English." | "You don't need to. Find one 'this block = these lines' and you've graduated today." |
| "I broke it — what do I do?" | "Go back to the last version. Changing a letter can't break it — change boldly." |
| "AI got it right on the first try — do I still need to verify?" | "The most dangerous thing is 'looks right.' Open the serial monitor and cover the sensor with your own hand — seeing is believing." |
| "Why does it take two boards? One could do it." | "One board could — but in real projects, sensing and performing rarely live in the same box. Between two wires today, you saw a system." |

---

## Section 6 · Prompt phrase library (teacher reference)

> All of today's prompts and templates are maintained here — every reference in the segments matches this section word for word; the student workbook carries the same text. **When projecting, put the whole block on screen so students can copy it straight into AI. Discipline restated: ask about code and state needs in the conversation you already have — it knows your project, so its answers fit your situation.**

### 6.1 The engineer's loop (Segment 7 — keep projected)

```text
The engineer's loop (run it every lap of the marathon)
say it → AI builds → check → upload → verify
   ↑_________ wrong? say the need more clearly, run another lap _________↓
The need's three boxes: what it senses (input) | what it does under what condition (logic) | how it shows itself (output)

Today's four steps (same in your workbook — run solo):
1. Send the 6.4 prompt with your need → read what AI explains first; point to the light sensor and LED on your board before you build
2. Build + upload (paste errors back verbatim, one step at a time)
3. Open the serial monitor: normal ___ / hand over it ___ → put the threshold back into your need, have AI use your number
4. Iterate one lap: change the threshold / add "when dark, the buzzer also beeps" (pick one)
```

### 6.2 The two buttons that matter (Segment 3 — projection)

```text
Whatever buttons there are, remember two today
① AI coding — tell it what you need in plain language; it writes code and fixes errors (today runs on it)
② Flash — click, and the program goes into the board (know what the "upload" button looks like)
Every other button — ask AI when you need it. It knows them better than you.
```

### 6.3 The "what's this code doing?" prompt (Segment 5 — projection)

```text
(select a code chunk, send in the conversation you already have)
What's this code doing? Explain in plain language I can understand — two or three sentences max.
```

### 6.4 The new-project prompt: the night-light (Segment 7 — projection)

```text
I'm using aily-blockly, with a Grove Beginner Kit for Arduino
(Seeeduino Lotus, with an onboard light sensor and LED — no wiring needed).
Make me a new project: a night-light —
input: light sensor reading; logic: reading below ___ counts as "dark";
output: LED on when dark, off when bright.
First tell me where the light sensor and LED are on the board and which pins they use,
then give me the code, one step at a time.
Leave the threshold number blank — I'll read the real value on the serial monitor and fill it in myself.
```

### 6.5 The two-views cheat sheet (Segments 5/7 — identical to the workbook)

```text
# My two-views cheat sheet
Name: ______

| This block (what it does) | The code that matches it (copy a few words) |
| 1. | |
| 2. | |
| 3. | |

## The clearest thing I got from "What's this code doing?":
code (a few words): ______ | in plain language: ______

## The line I changed: was ___ → now ___ → result ___

## New-project loop record: my need took ___ tries to say clearly;
light reading on the serial: normal ___ / hand over it ___ → my threshold is ___

## Joint-project record: the lookout's hand pin is ___ | the alarm post knows because: ______
Our link's first failure was because: ______
```

### 6.6 The class-group install assignment (send 3 days before — copy-paste)

```text
[HOMEWORK] Next session we're moving your projects "home" — into a new tool installed on your own computer.
Please install it before class (~15 minutes; parents can help):
1. Download the installer (pick the right version: Win / macOS): ______ (cloud link)
2. Follow the recording: ______ (link)
3. Three-check self-test: it opens ✓ I recognize the interface ✓ connecting a board and flashing works ✓
Didn't finish / no computer at home? Come 30 minutes early on the day — a TA installs it with you. Nothing to be ashamed of.
```

### 6.7 The NLHD link (Segment 9 — projection + class group)

```text
The new home's manual: Natural-Language Hardware Development (NLHD, 15 chapters)
https://github.com/ailyProject/Natural-Language-Hardware-Development
— every chapter drills today's loop. You don't need to read it today — open it when you're stuck.
```

### 6.8 The three-part prompt: the dusk alarm station (Segment 8 — projection, send in order)

```text
[PART ONE: split the job first]
I have two boards: a Grove Beginner Kit for Arduino (Seeeduino Lotus,
with onboard light sensor and LED) and a Wio Terminal (with screen and buzzer).
I want to build a "dusk alarm station": the Beginner Kit is the lookout — when it's dark
it lights its LED and "raises its hand" (outputs HIGH) on one digital pin; the Wio Terminal is the alarm post —
when it reads that signal, the screen shows "It's dark!" and the buzzer beeps once.
First help me sort this out: what does each end do? How do the signal wire and ground connect
(which two pins)? Draw me a wiring explanation I can understand. Don't write code yet.

[PART TWO: ask for the lookout program]
Division's clear. Now give me the program for the Beginner Kit (the lookout):
read the light sensor; when it's dark, LED on + signal pin raises its hand; when bright, the reverse.
Use the threshold I measured: ___. One step at a time.

[PART THREE: ask for the alarm post program]
Now the program for the Wio Terminal (the alarm post): watch the signal pin —
when it sees the hand go up, the screen shows "It's dark!" and the buzzer beeps once;
when it doesn't, the screen shows "All clear." One step at a time.
```

### 6.9 The division-of-labor diagram (Segment 8 — keep projected)

```text
The dusk alarm station: two boards, two programs, one wire linking them

  Grove Beginner Kit (the lookout)            Wio Terminal (the alarm post)
  light sensor watches the sky → when dark:   watches the signal pin:
  · lights its own LED                        · sees the hand → screen "It's dark!" + beep
  · "raises its hand" on the signal pin (HIGH)· no signal → screen "All clear"
         │                                        ▲
         └──── signal wire (agreed pin → agreed pin) ────┘
              + shared ground (GND → GND — no shared ground, no link)

Joint three steps (same in your workbook — run solo):
1. Send 6.8 part one: split the job, ask for the wiring explanation (no code yet)
2. Send parts two and three: generate and flash each program separately — run each board solo first
3. Link and verify: cover the light sensor, watch the alarm post — dead link? run the three checks
   (did each board run solo? / is the signal wire on the agreed pins? / is the ground shared?)
```

**Usage rules:** the prompts give structure — **you fill in the content** (blank brackets can't be sent); **all asks happen in the same conversation** — AI remembers the whole picture across the three-part prompt; opening a new conversation loses it; the Five Rules still apply (one thing at a time, paste errors verbatim, explain on request).

---

## Section 7 · Localization slots

| Where | Original | Swap-in suggestion |
| --- | --- | --- |
| New project 1 | night-light (Beginner Kit onboard light sensor + LED, zero wiring) | any sensor your class's main kit has onboard: sound-triggered buzzer, button-controlled light — must satisfy "input is measurable, threshold can be filled by hand" |
| Joint project | dusk alarm station (Beginner Kit lookout + Wio alarm post, signal wire + shared ground) | flipped roles: Wio as the lookout (onboard light sensor), Beginner Kit's buzzer as the alarm post; or a button alarm station (press one, the other rings) — must satisfy "one program per end, one signal wire" |
| The old project to unpack | showing your name on screen (Lesson 1 project) | whatever your class actually built in Lesson 1 (same sentiment works) |
| The change-one-line experiment | name → nickname | a local in-joke: class slogan, a local greeting — anything that's just the letters inside the quotes |
| Fast-lane challenge | dark-buzzer / Wio shows the reading | per class pace: "Wio button clears the alarm manually" or "screen shows the current light reading" |
| The hotel-vs-own-house line | hotel room vs. your own house | any local pair: rented storage vs. your own room, school locker vs. your desk — the point is "close the tab ≠ it stays" |

---

## Section 8 · Teacher reflection page

Take 10 minutes after class. Anything counts — even one line.

1. Did the install checkpoint hold at 18 minutes? Where did the homework pipeline leak (assignment copy? timing? the window)?
2. On average, how many tries until students' needs were clear? Best "second try" (quote it verbatim): ______
3. Best student proof of "I understood something" (quote it verbatim): ______
4. How many ran one full lap of the engineer's loop including the serial-measured threshold? ___ / ___ students
5. How many pairs got the link working (both solo runs + signal connected)? ___ / ___ pairs; how many first failures were "no shared ground"? ___
6. Which block overran, which came up short? Did the two-views 30 minutes survive?
7. Did any 🗣️ line sound awkward out loud? Cross it out; write what you actually said.
8. Student one-liner for the record ("what did I understand" / "how many tries") — collect the best ones for the showcase.

Photograph the page and send it to the teaching group, or tuck it back in the course folder. **Every line you write becomes a pitfall another teacher won't hit in the next edition.**

---

_Version: EN v1 ｜ 2026-08-25 ｜ Source: CN 讲师版 v3（2026-08-07；文件名标注 v2，修订说明含 v3：51 页 PPT 对齐、自检四勾改三勾、Grove 单线口径） ｜ 依据设计版：CFG-5 配置说明书 v1.0 §5.2 转折课专项预案_

_Localization notes: aily-blockly / Grove Beginner Kit / Wio Terminal 等专名保留原文；「从租户到主人」→ from tenant to owner（"Moving isn't a step back — it's buying the house."）；「确认归属仪式」→ the ownership ritual；「双视图时刻」→ the two-views moment（blocks view ⇄ code view）；「工程师的循环」→ the engineer's loop（say it → AI builds → check → upload → verify）；「天黑自动亮灯」→ the night-light project；「天黑警报站」→ the dusk alarm station（the lookout / the alarm post）；「信号线＋共地」→ the signal wire + shared ground（"no shared ground, no link"）；「补装窗」→ the install window；「收口转场」→ the install checkpoint（minute-18 red line）。信源修订决策已全部吸收：安装为课前作业（T-3 班级群＋T-7 录屏＋自检三勾＋课前 30 分钟补装窗）、14:18 铁律转场、双视图 30 分钟不可压、NLHD 循环为新主菜、零打印、去卡片化、无统一休息、问代码/说需求同窗接力、Grove 单线口径（信号和地都在一根线里，不另插地线）。「不赌中文渲染」规则天然满足——一切屏幕内容为英文/数字/图形。_
