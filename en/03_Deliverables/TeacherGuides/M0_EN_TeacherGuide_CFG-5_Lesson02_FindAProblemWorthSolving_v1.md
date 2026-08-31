# M0 Teacher's Guide ｜ CFG-5 Semester Course · Lesson 2: Find a Problem Worth Solving (v1)

_Grove Beginner Kit · IoT Starter Board ｜ Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) ｜ 10-session term ｜ 3 hours ｜ Source: 中文版 v2.2（`交付物/教师课件/M0_教师课件_CFG-5_第2课_找到值得做的题目_v1.md`）_

> **The one-sentence brief**: This is your second session. By the end, every student has (1) **their own one-line project manifesto** on the Project Wall — no exceptions, (2) **a three-box design sheet** naming a real user, (3) **their first ≥2-module linked build** plus one recorded accept-or-reject decision, and (4) **an AI learning log**. You don't write code, you don't fix hardware, and you never pick a topic for a student — you run the flow, say the scripts, and hold one red line all session: *"Tell me why that one is good."*

---

## 🎯 Learning Objectives

_By the end of this session, students will be able to…_

1. **Frame** one problem worth solving and state it as a one-line manifesto: "I'm making a ___ for ___ because ___." *(Bloom: Create)*
2. **Classify** any project idea onto the Three Kinds of Projects map, and **justify** why their chosen topic survives the Tough Reviewer's three questions. *(Bloom: Analyze, Evaluate)*
3. **Apply** the Five Rules for talking to AI — *one thing at a time / say the input & output / give it an example / if it's wrong, add a line / ask it to explain* — to make their board do what they want. *(Bloom: Apply)*
4. **Produce** a first ≥2-module linked build, **record** an accept-or-reject decision with a reason, and **complete** a four-sentence AI learning log. *(Bloom: Produce)*

---

## 📋 Page One: The Last Look Before You Walk In

### What today produces

Four things, every student:

1. **A one-line project manifesto** — "I'm making a ___ for ___ because ___" — on the Project Wall *and* copied into their workbook (everyone, no exceptions);
2. **A three-box design sheet** — their design document: project name, a real user, Sense → Logic → Output;
3. **A working project aimed at their own topic** — at least 2 modules working together, plus one record of a "change it or not" decision after feedback;
4. **An AI learning log** — made ___ / stuck on ___ / then ___ / next time ___.

Delivery: their workbook (online doc or handwriting), handed in after class (link or photo).

You run four segments: **Finding a problem** (51 min — talk your way to a topic worth building) → **The Five Rules** (26 min — five rules for talking to AI) → **Build time** (96 min — build toward your own topic) → **Wrap & preview** (7 min). No scheduled break — students use the restroom whenever they like while they work.

Today's skills: **spot a problem** (10 ideas converge into 1, and you can say who it's for), **build it** (the first ≥2-module linked build), **make trade-offs** (the first "change it or not" decision) — three of the six skills, in one session.

### The three things you need to know how to do

1. **Run the flow**: follow the timetable in this guide, segment by segment. Every segment says how long and what to do.
2. **Say the scripts**: every 🗣️ line in this guide is written out word-for-word. Read them as-is; don't improvise.
3. **Hold one red line**: when a student lets AI pick their topic, you ask exactly one question: *"Tell me why that one is good."* — the sentence you'll say most all session.

### The three things you do NOT need to know

1. **You do not need to know how to code.** All the code is written by AI — including your students'. You don't need to read a single line.
2. **You do not need to fix hardware, and you don't need to know wiring.** Wiring has one mantra: *"One end into the module, the other into the socket on the edge of the board. Plug it in wrong and nothing burns — just flip it around."* A module misbehaves? Swap it — swap, don't fix.
3. **You never make decisions for students.** Whether a topic is good, whether the feedback gets accepted — that's their call. Your job is to ask questions, not give answers.

### When something goes wrong

- Your live demo fails: **cut to the backup screenshot/video within 30 seconds** and keep going (speed sheet in Section 5). **This is not an incident — the plan already accounts for it.**
- A student's device fails: swap the board or the module, don't fix.
- You're stumped: smile and say *"Let's ask AI together."*
- The speed sheet is in Section 5. One-line version: **swap, cut to backup, ask AI — the three moves.**

---

## 一、Before Class

### 1.1 One Week Before (do it once)

- [ ] **Re-test the classroom internet**: run the full `codecraft.seeed.cc` loop once on any student machine (even if Lesson 1 passed — lab restore images can reset the environment back to zero).
- [ ] **Count the 40-in-1 kit delivery (if you have it)**: sort the "parts boxes" per table — 6–8 modules each (pick from: ultrasonic, servo, RGB LED strip, vibration sensor, water level sensor, MP3 module), enough Grove cables per box. **One spare of each module per box** — broken ones get swapped, not fixed. **No kit? The lesson runs on onboard modules only — it works exactly the same.**
- [ ] **Materials (zero-print — everything on screen)**: the three starter-brief pages (Reminder / Night Light / Alarm, full text in 1.4) saved on the instructor machine for projection; the three-box design sheet format (1.4) to project so students copy it into their notebooks or workbooks; "annoyances" sticky notes, 3 per student + 1 big sticky per student for the Project Wall (stationery, not printouts).
- [ ] **Prompt phrases are NOT printed** — the two phrase sets are already in the Student Workbook (full text in Section 6); project and read them together in class.
- [ ] **Student Workbook** is a shared online document (link to the class group / QR at the door); classes without online docs: students use notebooks — every step's output lands in their own record.
- [ ] Optional: if your class can manage it, pre-make a class online document/form so students submit their workbook links; otherwise: handwriting, photographed after class or brought next time.
- [ ] **Project Wall ready**: an empty wall or a big whiteboard, one large sheet of paper, title written by hand: "Our Project Wall".
- [ ] **TA collects 2 real conversations from Lesson 1** (one that worked first try, one that took five rounds) — the rules segment opens with them; if they weren't collected, use your own comparison conversations from Rehearsal 2 instead.
- [ ] Review Lesson 1's **catch-up list**; arrange how those students will catch up this session (pairing, or TA one-on-one).

### 1.2 Same Day (arrive 1 hour early recommended)

One person needs ~50 minutes for the checklist below, so arrive an hour early. With a TA: hand them device checks and desk setup; you handle projection, the whiteboard, and the Rehearsal-1 demo. If time is really tight, **Rehearsal 1 (idea-generation demo) is mandatory**; the other four can go.

- [ ] Projection test: open Codecraft on your machine — can log in, can chat.
- [ ] Device check: plug in every board once — powers up, screen lights; parts boxes (if any) on the tables, one module pulled from each box and wired once (see Rehearsal 3).
- [ ] Each desk: 1 board, 1 USB cable, 1 parts box (if you have it — one per table), sticky notes, 2 design sheets, markers.
- [ ] Whiteboard, written before you open the door: **the five rule titles only** (content gets revealed while you do them): ① one thing at a time ② say the input & output ③ give it an example ④ if it's wrong, add a line ⑤ ask it to explain.
- [ ] Project Wall area cleared, tape ready.
- [ ] If Lesson 1's 3-box diagram and 8-step map are still on the wall, **keep them** — you'll point at them today.

### 1.3 Demo Rehearsals (leave 25 minutes; click through all 5 demos yourself)

You have **5 live demos** today. Run each one fully on your own machine before class — not just watch it, click it through. **Anything that puts text on screen gets rehearsed in English/numbers/graphics — no gambling on font rendering (course-wide rule from Lesson 1).**

**Rehearsal 1 ｜ Idea-generation demo "Turn my annoyances into ideas" (used at 14:19)**
Open the Codecraft chat → fill the phrase template with your own 3 real annoyances → send → get 10 ideas → circle 2 → practice the comment line: *"What it gives you is candidates. Which one is buildable and who'd really use it — it doesn't know. You know."*
Backup: screenshot the successful conversation **3 times** (filled template / the 10 ideas / your 2 circled) onto the instructor machine. AI stalls live? Project the screenshots and keep going — **not an incident**.

**Rehearsal 2 ｜ Five-Rules comparison experiments (used 14:56–15:11)**
Run the Rule 1 and Rule 2 comparisons once each:
- Rule 1: first send *"turn on the LED, beep the buzzer, and show something on the screen, all at once"* (likely a mess), then split it into three separate messages (steady);
- Rule 2: first *"make a reminder"* (see what absurd thing it hands you), then *"if no movement is detected for 1 minute, make the LED blink"* (precise).
Screenshot both comparisons as backup. And grab the absurd "make a reminder" result — **students' own absurd results project best; your screenshots are the fallback.**

**Rehearsal 3 ｜ Parts-box wiring demo (used 15:17, only if you have the kit)**
Only rehearse this with the kit: from the parts box take a servo (or RGB LED strip) + one Grove cable — one end into the module, the other into the socket on the edge of the board — then tell AI *"sweep the servo side to side once"*. Run it. **No kit? Rehearse an onboard-module example instead** (e.g., onboard light sensor + LED: tell AI *"turn the light on when it gets dark"*) and use it for the 15:17 demo.
Backup: one pre-wired "demo set" left on the podium untouched; take **3 wiring close-up photos** (socket alignment, both cable ends) onto the instructor machine — room can't see? Project the photos. (No kit: the backup becomes screenshots of the successful onboard example.)

**Rehearsal 4 ｜ The Picky User review demo (used 16:26)**
Invent a fictional project description (e.g., *"a water reminder for my mom: it beeps if she hasn't touched her cup for an hour"*) → send to AI: *"Please play my mom, someone who's not great with electronics. Find exactly ONE flaw in my project. Just one."* See what it picks.
Backup: screenshot this conversation — it's both the 16:26 projection demo *and* the fallback if nobody dares to go first.

**Rehearsal 5 ｜ Project-map kind ② example (used 14:03)**
The "computer's partner" category needs a real example. Before class, run the kind-② example you'll present — e.g., the board's button/knob controlling a little game on the computer screen, or a button that flips PPT pages. **Only rehearsed examples go in the lesson; if it doesn't run, kind ② gets concepts only — no promised demo** — fall back to a spoken example ("a student from last term made…"). Keep it under 3 minutes.

### 1.4 Materials, in Three Buckets

**📦 In the starter kit (just count, nothing to buy)**

- Grove Beginner Kit per student (carry over from Lesson 1) + 1 instructor demo kit
- Spare USB cable box

**🛒 You bring (one stationery run, nothing printed)**

- No printing: the three starter briefs + the three-box design sheet format projected (students copy into notebooks/workbooks); Student Workbook as a shared online doc — no online doc? notebooks
- Sticky notes ("annoyances" small slips + Project Wall big slips), markers, tape
- Large paper or whiteboard (five-rule titles), whiteboard pens
- Hourglass or phone timer (the 5-minute thinking countdown — a projected countdown works too)

**✨ Nice-to-have (zero impact if skipped)**

- Grove 40-in-1 extension kit (sorted into per-table "parts boxes": 6–8 curated modules + Grove cables) — **optional: have it → wiring play; don't have it → onboard modules only, the lesson works exactly the same**
- Project Wall decorative border; one small sticker per student (to stick on their manifesto)
- 3–5 photos of previous cohorts' projects (more convincing shown; spoken examples work fine)

Budget note: everything you bring is one stationery run. Cheap.

**The three starter briefs** (projected — three pages or one page in three columns; reveal the reference combos on the back after students pick):

> Brief 1 ｜ **Reminder**: remind one specific person of something they always forget. Back: accelerometer + buzzer (remind them to get up after sitting too long); button + screen (pill check-in).
> Brief 2 ｜ **Night light**: a considerate light that doesn't glare. Back: light sensor + LED (fades on at dusk); sound + LED (tap to light on a midnight trip to the bathroom).
> Brief 3 ｜ **Alarm**: keep watch over one thing for you. Back: accelerometer + buzzer (shouts when touched); ultrasonic + RGB LED strip (changes color when someone approaches).

**The three-box design sheet** (projected; students copy the format into their notebook or workbook and fill it in):

> My project is called: ________
> Who it's for (write a real person's name): ________
> Sense: ________ → Logic: ________ → Output: ________
> Modules I'll use (tick the onboard ones; circle the parts-box extras if you have one): ________

---

## 二、Session Map

Sample timetable 14:00–17:00 — **shift the whole thing to your actual start time** (a morning class becomes 9:00–12:00; segment lengths don't change). **No scheduled break** — students use the restroom whenever they need, no reporting; device checks and sticky-note sorting happen quietly at the start of build time.

| Clock time | Segment | Students do | You do |
| --- | --- | --- | --- |
| 14:00–14:51 | Finding a problem worth solving | see the project map, write annoyances, get the new phrases, diverge ideas, converge, pair interviews, manifestos on the wall | demo the phrases, hold the red line, lead the manifesto round |
| 14:51–15:17 | The Five Rules for talking to AI | run comparison experiments on their own boards, rewrite challenge | demo the comparisons, circulate collecting absurd results |
| 15:17–16:53 | Build time: toward your own project | fill design sheets, build, AI review, make a decision, show & tell, write the log | launch the briefs, wiring fallback, lead the first review |
| 16:53–17:00 | Wrap: recap + preview | recap three takeaways, hear the preview | lead the recap, preview Lesson 3 |

### 2.1 Time Buffer (Flexible / Non-negotiable)

- **Non-negotiable**: the manifesto round (the whole point of today — every person says theirs), build time (today's main hands-on work), and the end-of-session log.
- **Flexible** (can compress): the Five Rules — at most cut the Rule 3 and Rule 5 experiments (house rule: **no experiments, no rules** — cut the experiment and you cut the rule with it; never teach a rule lecture-only); pair interviews from 4 to 2 minutes; show & tell projects only 2.
- **Can defer**: if the class is generally slow in build time, the review's "pick one flaw" is NOT optional, but the "fix it" part can move to the start of next session — the decision (accept or reject + the reason) must happen today, in class.

### 2.2 TA Split (if you have TAs; no TAs? You can carry it alone, just circulate slower)

| Segment | TA A | TA B |
| --- | --- | --- |
| Finding a problem | watch the "AI picks the topic" red line; drop prompt words to tables stuck on annoyances | check lists for real names; photograph the Project Wall (wall only, no faces) |
| Five Rules | collect absurd experiment results; one-on-one with slow students | handle device/network issues |
| Build time | review design sheets (free-choice topics must pass a look); wiring support | challenge tasks for fast students; extra build photos (hands only, no faces) |
| Wrap | organize log archiving | sort today's photos; update the catch-up list |

---

## 三、Segment-by-Segment Scripts

### Segment 1 ｜ Finding a problem worth solving (14:00–14:51)

> Goal: by the end of this segment, every student has a one-line manifesto plus a list of real names. Deeper: students taste for the first time "AI helps me think, but I hold the decision" — the most important relationship of the whole term.

**14:00–14:03 ｜ Import: last time you made it light up — today you decide who it lights up for** [I Do]

**Say this:** *"Take 30 seconds to look back: you put your name on the screen, and you taught the board Sense → Logic → Output. Last session you proved 'I can make things.' From today, the question changes: make things for who? Look at two topics from last term: a water reminder — made for a mom who always forgets to drink; a night light — made for a little brother afraid of the dark. See the pattern? Neither is a big invention. Both are real annoyances from real life. Today, you find yours."*

**Watch for:** previous-cohort examples can be swapped for local ones (see Section 7). Write *"who does it light up for?"* on the whiteboard — you'll point at it all session. The import is only 3 minutes — two examples, then move on.

**14:03–14:11 ｜ What this board can make: Three Kinds of Projects** [I Do]

**Say this:** *"Before you hunt for a topic, look at what kinds of things this board can actually make. Get the map in your head first, so your topics don't fly off everywhere. There are three kinds. Kind one: a standalone device — the board is the whole thing. Last session's dark-detecting light: it senses, decides, reacts — all by itself, nothing else attached. An alarm, a desk weather station, a pomodoro timer, a whack-a-mole game — all kind one. Kind two: the computer's partner — the board and the computer make something together: the board is the hands and the ears, the computer is the screen. Like turning the board into a game controller — buttons, knob, shake — controlling a game on the screen. Or a presentation clicker: press a button, the slide on the computer turns. Kind three: the outside world — if you have them, the parts box on your desk is the door in: the modules on your board can snap off and recombine, and later you can add new modules, even the internet. Today, just know the road exists. (point at the map) Your topic can land in any of the three — what matters isn't how advanced it is, it's whose annoyance it solves."*

**Watch for:**
- Project the Three Kinds of Projects page (until the deck exists, three columns on the whiteboard work fine).
- The kind-② example must be one you rehearsed (see 1.3, Rehearsal 5) — unrehearsed examples don't go in the lesson.
- One or two examples per kind, no parameters, **8-minute hard timebox**.
- Kind three: one sentence, no promises. A student presses on the internet? *"There's a dedicated lesson later — today, just remember it exists."*

**Pitfalls:**
- A student locks onto a topic beyond the board (needs internet, needs a camera): don't reject — land them on the map: *"That idea lives in kind three — today we build its core with kinds one and two; the internet step comes later."*

**CFU:** *"Point at the map. Which kind is a flashlight that turns on when it's dark? (wait) Which kind is a controller for a computer game? (wait) One-word answers — go."*

**14:11–14:16 ｜ The annoyances free-write** [You Do]

**Say this:** *"Open your Student Workbook (or notebook), find the 'annoyances' box. Two minutes. Write three small things that annoy you — at least three, in your own document. Yours, your family's, your friends' — all fine. The smaller the better: 'my mom always forgets her pills' is worth a hundred 'world peace's. I'll go first: [one from home: I always forget my keys when I leave / one from work: I stare at the screen until my eyes hurt — swap for your own two real ones]."*

**Watch for:** tables stuck? TAs drop prompt words: *"waking up in the morning / your backpack / pets / grandparents / rainy days"*. Solving for someone else is allowed — the most moving topics last term were made for family. Students with no record carrier: remind them to write in their notebook — every later step needs it.

📌 **Output anchor:** at least 3 annoyances written in everyone's workbook.

**14:16–14:19 ｜ Two new phrase sets appear (projected, read together)** [I Do] → [We Do]

**Say this:** *"New weapons. Last session you learned two spells — one thing at a time, and if it's wrong, add one more line. Today, two more phrase sets: the topic set, four phrases — they help you think about WHAT to make; and the user set, three phrases — they help you think about WHO it's for. These phrases are printed in your Student Workbook — forget them, flip to the page. First, remember these two: 'turn my annoyances into ideas' and 'the Tough Reviewer'. (project Section 6's phrases, read them once together)"*

**Watch for:** set the rule before anything else: **the blanks in a phrase must be filled with your own stuff — a phrase sent with blanks doesn't count.** That sentence is the gate for today's red line.

**14:19–14:28 ｜ Diverge: "Turn my annoyances into ideas"** [I Do] → [You Do]

**Say this:** *"Watch me once. (project, fill the template) My annoyances: [your three real annoyances]. Send it to AI — (send) see, 10 ideas. (circle 2) Notice: what it gives you is candidates. Which one is buildable, who'd really use it — it doesn't know. You know. Your turn: fill your three annoyances into the phrase, send it — then copy your 3 favorite ideas back into your workbook."*

**Watch for:**
- **Red-line patrol** (the TA's main job): a student who sends the blank template without their own annoyances — send it back to be refilled: *"The blanks are for you to fill — AI doesn't know how old your sister is."*
- Everyone must get ≥10 ideas before this counts as done. Few ideas? Push: *"give me 5 weirder ones."*

📌 **Output anchor:** the idea list stays in their own AI conversation; the 3 favorites are copied into the workbook.

**Pitfalls:**
- AI/network stalls here: don't wait — use the 40-in-1 module chart (or the parts box, if you have one) as the inspiration pool; students think of ideas against the modules; the AI divergence moves to the start of the rules segment for 10 minutes. **The manifesto round is non-negotiable.**

**14:28–14:36 ｜ Converge: "The Tough Reviewer"** [I Do]

**Say this:** *"Ten is too many — you can only build one. Meet today's bluntest phrase: the Tough Reviewer — AI plays the rudest, most honest advisor who still wants you to win. Throw your ideas at it, and it grills you, idea by idea, with three questions: can it be done in 3 hours? do you have the hardware? would you really use it every day? (demo once) See? Getting grilled isn't shameful — it kills the ideas that can't stand up, before you've spent half a day on them. Go."*

**Watch for:**
- **Today's number-one pitfall lives here**: AI says pick X, the student picks X. The TA's standard move is to walk over and ask: *"Tell me why that one is good."* — they can answer, let them through; they can't, have them run the three questions themselves.
- A student whose ideas all get rejected: no panic — take the one they're most attached to, run "how else could this idea work?" once, then screen again.
- Topic too big ("I want to build a robot"): the three questions are the first gate; still too big? Demo the cut on the spot: *"You can't build the robot today — but a robot head that greets people? That you can start today."*

**Pitfalls:**
- A student copies the neighbor's topic: don't call it out — just push on the "because": *"Tell me — why are you building it for them?"* No reason of their own? The manifesto doesn't go on the wall; back to the Tough Reviewer for one more round.
- Someone's crushed after screening (their favorite got rejected): *"Getting grilled isn't shameful — it's killing the ideas that can't stand up, before you find out halfway through."*

📌 **Output anchor:** the 2 surviving ideas + one line on "why I kept it", written into the workbook — open the doc (or notebook), fill in the blanks.

**14:36–14:44 ｜ "Who would use it" + pair interviews** [We Do]

**Say this:** *"Topic set — next question: who'll use it? Use the 'who would use it' phrase and let AI make a list — but there's a hard rule: real names only. 'My mom', 'my classmate Liam' — pass. 'All students', 'everyone' — fail. Then interview your neighbor, two at a time, 4 minutes each: you introduce your topic, your neighbor plays your user and asks you the questions from the 'help me make an interview script' phrase."*

**Watch for:**
- Two new words today, first time clearly (write them in a corner of the whiteboard): **user** — the real person who'll actually use your project; **interview** — going to ask that person a few questions. Point and say: *"These aren't exam words — you'll use them today."*
- Interviews drifting into small talk: the interview questions are in the phrase — reading them out loud counts.
- A list without real names — send it back: *"A project written for 'everyone' ends up used by no one."*

**Pitfalls:**
- A student embarrassed to interview their neighbor (afraid the topic will be judged): swap roles — the neighbor interviews them first; when it's their turn, they just read the questions from the phrase.
- Their "user" is themselves: fine — but make them write a second real name: *"Besides you — who's most annoyed by this?"*

📌 **Output anchor:** a one-line user picture in the workbook — "My project is for ___ because ___."

**14:44–14:51 ｜ The manifesto round + the Project Wall** [We Do]

**Say this:** *"Last thing: one sentence each, announce your topic to the class. The format: I'm making a ___ for ___ because ___. I'll go first: I'm making a [pill reminder] for [my mom], because [she always forgets her blood-pressure meds]. — One by one. When you've said it, write it on a big sticky and put it on the Project Wall; then open your workbook (or notebook) and copy the same sentence in — it's the north star for every lesson after this one."*

**Watch for:**
- After each manifesto, one line of feedback — **praise only the highlight** (*"that 'because' hits hard" / "so specific about who it's for"*).
- A manifesto missing a part? Push with questions: *"For who?" "Why them?"* — complete it before it goes on the wall.
- TA photographs the Project Wall (wall only, no faces) — it's the anchor you'll return to in later lessons, and log material.
- When everyone's up: *"This wall does not come down. Lesson 6, we plan around it; Lesson 10, we present around it — we keep coming back to this wall."*

📌 **Output anchor:** the one-line manifesto on a sticky on the wall AND copied into the workbook — the wall and the workbook must match.

**CFU:** *"Everyone, point at your manifesto on the wall. (wait) Now read your own 'because' clause silently. If you can say it to your neighbor in five seconds, you're done here — go."*

---

### Segment 2 ｜ The Five Rules for talking to AI (14:51–15:17)

> Goal: students can rewrite a vague request into a clear one that AI gets right the first time. House rule: **no experiments, no rules** — every rule must have been run on their own board to count.

**14:51–14:56 ｜ Replay the crashes: it's not luck, it's how you say it** [I Do]

**Say this:** (project Lesson 1's two real conversations: one that worked first try, one that took five rounds) *"Look at two real conversations from last session. This one — worked first try. This one — five rounds of back and forth. Same AI, same classroom. What's the difference? (pause — wait time, let them guess) Not luck. It's how you say it. Talking to AI isn't magic — it's a craft you can practice. The next 15 minutes: five rules, and we verify every single one on your own board. First, a picture: talking to AI is like briefing a new colleague — they're smart, but they don't know what's in your head."*

**Watch for:** students claiming their own crash conversations — the laughter is good, let it happen. New word, first time clearly: **requirement** — the sentence that says clearly what you want your project to do. Write it in a corner of the whiteboard.

**14:56–15:11 ｜ The Five Rules, 3 minutes each (30 sec talk + 2 min experiment + 30 sec show result)** [I Do] → [You Do]

**Say this** (opening line for each rule; the experiment steps are projected as you go):

- **Rule 1 · One thing at a time**: *"Stuff three wishes into one sentence and it falls apart. First send this — 'turn on the LED, beep the buzzer, and show something on the screen, all at once' — see what you get; then split it into three sentences, one at a time. See the difference yourself."*
- **Rule 2 · Say the input & the output**: *"Say two things clearly: when (the input) and what happens (the output). First send 'make a reminder' — look at the absurd thing it hands you; then send 'if no movement is detected for 1 minute, make the LED blink'. Which one is precise?"*
- **Rule 3 · Give it an example**: *"When you can't describe it, give a comparison. Try this: 'show numbers on the screen like an elevator does' — one comparison beats ten descriptions. Find a comparison for your own effect."*
- **Rule 4 · If it's wrong, add a line — don't restart**: *"The old rule from last session: don't delete the conversation, don't restart — add one more line. Now break it on purpose: mess up the effect you just made, then add a line to fix it. Time it — see how much faster it is than starting over."*
- **Rule 5 · Ask it to explain**: *"AI is a teacher too. Throw the code it just wrote back at it: 'what is this doing? in plain words.' Not understanding isn't shameful — not asking is the real loss."*

**Watch for:**
- **Rule 2's experiment is the easiest teaching moment** — a vague request produces an absurd result; circulate, collect the most absurd one, project it, let the class laugh, then land the point: *"It's guessing. Your project is ten times more complex than this — you can't afford the wrong guess."*
- Fast/slow split: fast students add the "Rule 3 advanced" (use one comparison to make AI show something flashier); slow students only need Rules 1, 2 and 4 to pass.

**Pitfalls:**
- Both sides of a comparison come out equally well (AI too clever — got the vague one right too): *"Today it guessed your mind right — but your real project is ten times more complex. You can't afford the wrong guess."* Then add a two-condition request (*"only light up when it's dark AND there's sound"*) and run it again.
- Short on time: cut the Rule 3 and 5 experiments — and the rules don't get expanded either; point at the whiteboard and say *"try these two at home"*, don't force it.

**15:11–15:16 ｜ The rewrite challenge** [You Do]

**Say this:** (project a deliberately bad request) *"Final exam: 'make something that reminds my little sister to stop playing on her phone.' What's wrong with that sentence? Rewrite it with the Five Rules, send it, test it. Anyone whose version works within a try or two — read it to the class."*

**Watch for:** someone who got it working — have them read their version, then name the rule they used (*"you specified the input and the output — that's Rule 2"*). That's what mastery looks like; no test needed.

**15:16–15:17 ｜ Wrap the segment** [I Do]

**Say this:** *"Last session's two spells — 'one thing at a time' and 'if it's wrong, add one more line' — they're today's Rule 1 and Rule 4. Plus the error move. All of it is printed in your Student Workbook — forget it, flip to the page. Thirty seconds with your neighbor: which rule hit you hardest today? — Next: the big build."*

**CFU:** (the 30-second pair share doubles as the check — then one student reports their pair's answer: *"Which rule, and why?"*)

---

### Segment 3 ｜ Build time: toward your own project (15:17–16:53)

> Goal: everyone completes their first ≥2-module linked build and lives through the first full "got feedback → made a decision" loop. Today teaches no new tech — it teaches combining last session's stuff to hold up a bigger intent.

**15:17–15:25 ｜ Launch the briefs + (if you have the kit) parts-box unboxing** [I Do]

**Say this:** *"You just set your topic — now make its first working piece. Two options: one, cut a small slice out of your topic and build it (recommended); two, no direction yet? Pick one of the three starter briefs — Reminder, Night Light, Alarm — reference combos on the back."*

**Say this** (with the kit): *"Now look at the new thing on your table: the parts box. Last session the parts on your board were soldered on — today these modules you wire yourself. First wiring, one rule only: one end into the module, the other into the socket on the edge of the board; plug it in wrong and nothing burns — just flip it around. Watch once. (use the Rehearsal-3 servo demo)"*

**Say this** (no kit): *"Today we use the modules already on your board — last session's friends: light, sound, button, LED, buzzer, screen. Two linked modules, no problem. Straight to the design sheet."*

**Watch for:**
- (with kit) wiring is today's new thing — name the modules before hands touch them: *"This is the servo — a little motor that turns its head; this is the RGB LED strip — a light bar that changes color…"* (point at the real things, 30 seconds, don't expand).
- A student whose topic really can't be sliced small: the TA maps it "near enough" onto a starter brief against the design sheet: *"This is the practice piece for your topic."*
- The TA uses the opening minutes for three quiet jobs: ① device check, parts-box placement (if any); ② sort the manifesto stickies by seating order so design-sheet reviews go fast; ③ flag students who missed the Five-Rules experiments — they get priority during build time.

**15:25–15:30 ｜ Paper thinking (5-minute hourglass)** [You Do]

**Say this:** *"Hands off the keyboard. Design sheet, 5-minute hourglass: what's your project called, who's it for (a real name), Sense ___ → Logic ___ → Output ___, which modules. When the hourglass runs out, you build — start, and the build becomes yours as you go. Writing 'who it's for'? Look at the wall once. This design sheet is your design document — building, review, log: everything checks against it."*

**Watch for:** free-choice design sheets must pass the TA's eye before building starts (keeps them on-track and in-scale); starter-brief sheets start right away. Still hesitating at 5 minutes? Pull a starter brief and start with the reference combo.

**15:30–16:21 ｜ Build, 51 minutes** [You Do]

**Say this** (the start signal): *"Go. Three rules: one thing at a time; if it's wrong, add a line; stuck? Ask your AI first, then your neighbor, then raise your hand."*

**Watch for:**
- Midway (around 16:00), one whole-room callout: *"Stop, 10 seconds — check against your design sheet: are you still building the thing you wrote?"* Anyone drifting pulls themselves back — the lightest anti-drift move there is.
- Circulate watching for **the link**: two modules doing their own separate things doesn't count. Script: *"make the one on the left tell the one on the right something"* — e.g., *"when the light dims, it tells the LED strip: time to light up."*
- A student dumps the whole job on AI at once: the old line — *"directors shoot one scene at a time: get the link working first, then decorate."*
- (with kit) wiring problems chain-reacting across a table: project the Rehearsal-3 wiring close-ups, everyone checks "socket alignment" together; one module misbehaves — swap, don't fix.

**Pitfalls:**
- The link won't come together and it degrades into two separate projects: first, the minimal definition — *"make the one on the left tell the one on the right something"*; still stuck? Lower the bar to "one project + one record of the linking attempt" — write the sticking point into the log, it still counts as done.
- Someone badly behind (16:10 and still no successful flash): move them to the instructor demo spot to follow a starter brief; the target drops to "one linked build runs" — no self-chosen topic to chase.
- Fast student done before 16:00: no early review — give a challenge task (only ones you rehearsed; unrehearsed ones don't go out), or send them to help a slow student (mouth only, hands off the other person's keyboard).

**16:21–16:26 ｜ Wiring check call-out (everyone, with kit)** [I Do]

**Say this:** *"Hands up, everyone — wiring check: modules facing the right way? Cables pushed all the way in at both ends? Sockets matched? 30 seconds, check your neighbor's once."*

**Watch for:** these 5 minutes underwrite the review segment — reviews demo the builds, and loose connections exploding mid-demo is chaos. The TA circulates, re-seats anything obviously loose on the spot. **No kit? Skip the call-out** — the 5 minutes become: TA circulates checking progress and nudging slow students to wrap up; students keep building.

**16:26–16:38 ｜ AI review: the Picky User, first time (pick exactly one flaw)** [I Do] → [You Do]

**Say this:** *"Keep your builds out. Today, a new segment for the first time: review — asking someone to find the flaws in your project. Today's reviewer is AI, but it plays a real person. Watch the demo. (project the Rehearsal-4 conversation) I had it play my mom — someone who's not great with electronics — and it found one flaw. Your turn: send your project description to AI, starting with 'please play ___' — the real name on your design sheet — 'find exactly ONE flaw in my project. Just one.' Note: review isn't abstract fault-finding — it's finding flaws for that one real person."*

**Watch for:**
- One flaw is a designed dose — the first review experience must be "useful and painless". A student asking AI for more flaws: hold them back — *"one at a time, you can't eat more than that."*
- "The Picky User" and "Accept or Reject" get expanded in Lesson 4 — today the phrases are projected and used; that's enough.
- The first time AI's flaw lands too harshly or too absurdly, handle it in public: *"AI's opinion gets reviewed too — do you think it's right?"* — that sets the review culture once.

**Pitfalls:**
- A student gets upset by the flaw: catch the feeling first — *"getting a flaw pointed out isn't shameful — it wants your project to be worthy of the person who'll use it."* Strong emotions → talk privately, not in public.
- Someone's build doesn't run when review time comes: review it anyway — let AI find flaws in the **design**, not the bug; "not running yet" is itself the best "stuck on" for the log.

**16:38–16:48 ｜ Accept or Reject: your first trade-off decision** [We Do]

**Say this:** *"You've got the flaw. Now make a decision: change it, or not. Change it — do it right now. Don't change it — tell your neighbor why. Say it clearly: accepting earns credit, and so does rejecting — as long as the reason is yours."*

**Watch for:**
- Actively find one well-reasoned rejection and praise it out loud: *"They turned down AI's suggestion, because ___ — that reason stands. Knowing how to refuse is what real trade-offs look like."*
- The decision and the reason must go into today's log (the spoken line includes *"AI said ___, I decided ___, because ___"*).
- Fast student already done changing: give the "reverse challenge" — hand their project to their neighbor to review; they play the person being reviewed, practicing the mindset.

**Pitfalls:**
- The whole class accepts (nobody dares to reject): you model a rejection live — *"AI also found a flaw in my demo project — said the reminder sound is too soft. I'm not changing it, because my mom's hearing is fine; a louder sound would just wake her from her nap. See? A rejection with a reason counts the same."*
- Someone can't say why ("I just want to change it"): squeeze the reason out — *"did it hit the mark, or are you changing it because you don't know what else to do?"* The first stands; the second goes back to think for one minute.

📌 **Output anchor:** everyone writes one line into their workbook — "I accepted/rejected AI's suggestion, because ___" — their proof of being the director.

**16:48–16:53 ｜ Flash show & tell + the AI log** [You Do] → [Share-out]

**Say this:** *"In your table, 30 seconds each: demo your build, say one line — 'what AI found, and whether I changed it'. Then today's log — take one photo: your build and your design sheet together, two pieces of paper, one board — all made by you. Say thirty seconds, the usual four sentences: today I made ___ / I got stuck on ___ / then ___ / next time I want ___ — and for today's 'then', include how you handled the flaw."*

**Watch for:** the TA takes extra build photos and the Project Wall (hands only, no faces); the design-sheet + build photo is today's most valuable material — everyone must have one.

---

### Wrap ｜ Recap + next-lesson preview (16:53–17:00)

**Say this:** *"Last two minutes — take stock. One: from 10 ideas you fixed your own topic and said who it's for — that's spotting a problem. Two: you directed AI to make your first combination build — building it, one step further. Three: you made the first 'change it or not' decision of your life — that's making trade-offs. Six skills, and today you practiced three. Next session, new gear: a handheld with a color screen — the Wio Terminal. We're going to give your project a screen — from today, your builds have a real interface. Bring your topic. Class dismissed!"*

**Watch for:** have students look at the Project Wall once — this wall anchors the next several lessons, and today everyone's name is on it. After class: collect the outputs — online docs get links, handwritten gets photographed; whether you got them all — make a note, you'll need it at the start of Lesson 3.

---

## 四、Live Demo Backup Plan at a Glance

| Demo | Used at | Rehearse | Backup asset | If it goes wrong live |
| --- | --- | --- | --- | --- |
| Idea generation "turn my annoyances into ideas" | 14:19 | Rehearsal 1 | 3 screenshots of the successful run (filled template / 10 ideas / your 2 circled) | Project the screenshots and keep going — **not an incident** |
| Five-Rules comparison experiments | from 14:56 | Rehearsal 2 | Rule 1 & 2 comparison screenshots + the absurd "make a reminder" result | Instructor machine switches to screenshots; students' own experiments are unaffected |
| Parts-box wiring + servo demo (with kit) | 15:17 | Rehearsal 3 | Pre-wired demo set on the podium + 3 wiring close-up photos | Swap to the pre-wired set; AI unresponsive → teach wiring only, the demo slips into build time. **No kit: row not applicable — use the onboard-module example** |
| The Picky User review demo | 16:26 | Rehearsal 4 | The rehearsal conversation screenshot (doubles as the projection demo) | Project the screenshot and read it through; students send their own as usual |

---

## 五、Pitfall Speed Sheet

Remember the three moves first: **swap, cut to backup, ask AI.** Today's fourth: students' decisions — you ask, you never decide for them.

| Situation | What you do |
| --- | --- |
| ⭐ Student lets AI pick the topic | The one standard question: *"Tell me why that one is good."* Can't answer → run the Tough Reviewer's three questions again. No criticism — just keep asking |
| ⭐ Topic too big ("I want to build a robot") | The three questions are the first gate; still too big? Demo the cut live: robot → "a robot head that greets people" — start with that today |
| ⭐ Student copies the neighbor's topic | Don't call it copying — push on the "because": *"Why are you building it for them?"* No reason of their own → the manifesto doesn't go on the wall — back to the Tough Reviewer for one more round |
| ⭐ Interviews become a formality / small talk | The interview questions are in the phrase — reading them aloud counts; finished early? Add one: *"Did they mention a use you hadn't thought of?"* |
| ⭐ The rules become a lecture | House rule: no experiments, no rules. A rule you don't have time to experiment — cut the whole rule, never teach it lecture-only |
| Comparison comes out equally well both ways (AI too clever) | *"Today it guessed right — but your real project is ten times more complex. You can't afford the wrong guess."* Add a two-condition request and re-run |
| Can't write annoyances | Prompt words (waking up / backpack / pets / grandparents / rainy days) + "solving for someone else" is allowed |
| Design sheet over — still not building | The 5-minute hourglass is law; still hesitating? Pull a starter brief and start with the reference combo: *"Start, and the build becomes yours as you go"* |
| The link won't come together, degrades into two projects | *"Make the one on the left tell the one on the right something"*; still stuck? Lower the bar to "one project + one record of the attempt", log the sticking point |
| (with kit) wiring errors chain-reacting | Project the wiring close-ups, everyone checks "socket alignment" together; single module dead → swap, don't fix; same type exhausted → fall back to onboard modules |
| AI review's flaw lands too harsh / too absurd | Handle the first one in public: *"AI's opinion gets reviewed too — do you think it's right?"* |
| Student upset by the flaw | Catch the feeling first: *"Getting a flaw pointed out isn't shameful — it wants your project to be worthy of the person who'll use it."* Strong emotions → private talk |
| Build-time AI/network stalls | Same as Lesson 1: swap to the spare machine; whole-class outage past 15 minutes → design sheet and review proceed as usual (paper + neighbor reviews), the build moves to the start of next session |
| Student has no phone for the log | TA photographs everything, filed by table number; the spoken part stays |
| Log becomes empty fluff | "Stuck on" is required; today's "then" must include how the flaw was handled |

### Bonus: student questions and how to catch them

| Student asks | You say |
| --- | --- |
| "Why not just let AI pick my topic? It's smarter than me." | "It's smart, but it doesn't know how old your sister is, or what time your mom takes her pills. A topic = one person you care about + one thing they care about. Only you know those two." |
| "Is my topic too simple?" | "A simple topic done all the way beats a big topic abandoned. Last term's favorite project was 'remind mom to drink water' — small? Small enough to use every day." |
| "Why do we need real names? Why can't I write 'everyone'?" | "A project written for 'everyone' ends up used by no one. Write a name and you know who you're finding flaws for, and who you're changing things for." |
| "AI found a flaw and I don't want to change it — am I lazy?" | "Not necessarily. Say the reason — if it's 'my user doesn't need it', that's judgment; if it's 'I don't feel like it', you know it yourself. Say it to your neighbor — they'll hear the difference." |
| "Will wiring burn my board?" (with kit) | "These cables can't burn it. Plug it in wrong and it just doesn't work — pull it out and flip it. The only forbidden move is forcing it." |

---

## 六、Prompt Phrase Library (instructor reference)

All seven phrase sets from today, full text — read before class, project when you need them. **These are not printed or handed out** — they're printed in the Student Workbook; project and read together when they debut, point students to the book when they forget. If the workbook wording differs slightly from here, either works; the meaning is the same.

### The "topic" set (four phrases)

**Phrase 1 ｜ Turn my annoyances into ideas** (after you have an annoyances list — diverge)
> I have three real annoyances: 1. ________ 2. ________ 3. ________. Give me 10 ideas that small hardware (sensors) could solve, the more specific the better. Just list ideas — don't choose for me.

- Rule: the three annoyances must be yours — a phrase sent with blanks doesn't count.

**Phrase 2 ｜ How else could this idea work?** (when an idea gets rejected, or you want to reshape it)
> I have an idea: ________. Help me think of 3 different ways to make it, and say how each differs from the original. Don't make it bigger — each one must be something I can try today.

**Phrase 3 ｜ The Tough Reviewer** (converge from 10 ideas to 1)
> You are the bluntest advisor who still wants me to succeed. Here are my ideas: ________. Grill me with three questions, one by one: Can it be done in 3 hours? Do I have the hardware? Would I really use it every day? Then point out the one that stands up best — but the choice is mine.

**Phrase 4 ｜ Why I chose it** (after choosing — say the reason clearly)
> I chose: ________. My reason: ________ (must be your own words). Help me polish this into a one-line manifesto: "I'm making a ___ for ___ because ___." Don't invent a reason for me.

- Memory hook: AI produces the quantity, you produce the decision. Can't say "why I chose it"? You haven't chosen.

### The "user" set (three phrases)

**Phrase 5 ｜ Who would use it** (after choosing — list real users)
> My project is: ________. List 2–3 specific, named people who would really use it (like "my mom" or "my classmate Liam"), and say why each would use it. Don't write "all students" or "everyone".

- Rule: real names only — "everyone" is not a user.

**Phrase 6 ｜ Help me make an interview script** (before talking to a real person)
> I'm going to ask ________ (a real person) about this: ________. Write me 5 questions. Rules: don't lead them into flattery ("do you like my idea" is a bad question) — ask about their real habits and their real annoyances.

**Phrase 7 ｜ Pretend to be my user** (practice when no real person is available — real people first)
> Play ________ (a specific person, traits: ________). Answer my interview the way they would — with their habits, their complaints. At the end, tell me: which of my questions were good, and which one was bad.

- Memory hook: real people > AI. This is the substitute, not the main move.

---

## 七、Localization Slots

| Slot | Original | Swap in |
| --- | --- | --- |
| 14:11 teacher-model annoyances | [I always forget my keys when I leave / I stare at the screen until my eyes hurt] | your own real annoyances — the more specific and mundane the better: "the coop gate keeps getting left open" beats any impressive example |
| 14:00 previous-cohort topics | [water reminder for mom / night light for little brother] | use last term's projects if you have them; otherwise use local ones everyone can feel — "a bell that tells grandpa at the shop someone came in" |
| 14:44 your manifesto demo | [a pill reminder for my mom, because she forgets her blood-pressure meds] | something you genuinely want to make — the one that lights your own eyes up |
| 16:26 Picky User persona | [my mom, someone who's not great with electronics] | someone you know well — "my dad, who drives a truck, thick fingers, bad at small buttons" — the more vivid the picture, the better |

---

## 八、Teacher Reflection Page (10 minutes after class — every line becomes the next version's saved pitfall)

1. Which segment went best? Which one do you most want a do-over on?
2. Any 🗣️ line that felt stiff to say aloud — not like a human? Cross it out, write what you actually said.
3. The "AI picks the topic" red line: how many times did it actually happen today, and how did you handle it?
4. Which Five-Rules experiment landed best, which got no response? Roughly what share of the class passed the rewrite challenge?
5. (with kit) Did the parts-box wiring stay calm? Were 6–8 modules too many or too few?
6. Timing: which segment ran over, which ran short?

Write it up, photo it, send it to the teaching group, or tuck it back in the courseware. **Every line you fill in is a pitfall some other teacher doesn't have to step in.**

---

_Source: 中文版 v2.2 ｜ English v1 (2026-08-25) ｜ Design base: X9 v1 / X1 v1 / A3 v1 / X6 v1 / CFG-5 spec v1.0 ｜ Timetable: sample 14:00–17:00, shift to your actual start time ｜ Note: "The Picky User" and "Accept or Reject" debut today as projected phrases; they get expanded in Lesson 4_
