# Teacher's Guide ｜ Lesson 8 · Run the First Lap

_Build Your Project's MVP · The Marathon's First Leg ｜ Chaihuo Maker Academy · M0 Hardware Foundation · Smart Hardware Fundamentals ｜ 10-session term ｜ 3 hours (no scheduled break)_

> **Source:** 中文版 v4（M0_教师课件_CFG-5_第8课_跑通第一圈_v2.md，文件名写 v2，文末修订说明含 v3/v4：MVP 主轴、三幕节奏、站会弹性化、Brandy 完整案例附录 42 页 PPT）
> **Localized edition** — same blocks, same minutes, same teaching intent; classroom language rewritten for an English-speaking teacher to pick up and teach from.

---

## The one-sentence brief

Today is **the marathon's first leg — build your project's MVP.** No new knowledge: students bring the requirements sheet they briefed in Lesson 7, check out parts, start building, and spend 135 minutes making **the MVP** (minimum viable product: the smallest closed loop that can be demonstrated). The last 30 minutes bring **AI as reviewer** on stage for the first time: the **Picky User** picks **3 faults**, Quinn opens a **5-item list**, and students judge each one **Accept or Reject** and fill the **baton handoff sheet**. The opener uses the Brandy case page (slide 4) to give MVP professional weight (a 1-minute hook); the end-of-lesson appendix (slides 18–42) is the full Brandy share, used flexibly per 3.9.

**The whole lesson runs in three acts** (the rhythm skeleton — keep this map in your head all day):

| Act | Blocks | Total |
| --- | --- | --- |
| **Act 1 · The start** | Opening (MVP + three rules) → first stand-up → check out parts | 25 min |
| **Act 2 · The build** | Build, first half → mid-way stand-up → build, second half (close the loop) | 120 min |
| **Act 3 · Review & handoff** | AI as reviewer → decide & execute → baton handoff sheet → close | 35 min |

Each act boundary has one explicit **gear-change move**: Act 1→2 is the word "start"; Act 2→3 is "hands off — review time." Whatever's done, you shift gears on time. **That rhythm itself is part of what today teaches.**

**When they leave, students can** (three things):

1. Run one full iteration cycle — **stand-up → build → review → decide** — the rhythm they'll run two more times in Lessons 9 and 10;
2. **State what their project can demo right now** — one verifiable sentence, not "half done";
3. Take AI's review faults, make an Accept-or-Reject call **with a reason**, and name the **first thing next leg**.

**Not yet, don't worry** (three things):

1. A first version that implements the whole requirements sheet — today's goal is the **smallest closed loop** (sense → think → act, once, end to end), not every feature;
2. Not getting stuck — stuck is the marathon's normal state; the rule is **"15 minutes with no progress = raise your hand"**;
3. Digesting every review item — whatever can't be fixed goes in the handoff sheet under "first thing next leg." That's the system, not failure.

**When things go wrong:** swap (hardware), cut to backup (tool / account / network), ask AI (knowledge).

**Today's two iron laws:**
1. **The AI review can never be squeezed out by progress pressure** — it's the institutional floor of the whole process; squeezing it once is a major backfill event;
2. **You answer direction only; TAs rescue the stuck only** — code questions go to AI first. Every line you write for a student is a bit of growth they don't get.

---

## 🎯 Learning Objectives

*By the end of this session, students will be able to…*

1. **Run** one full iteration cycle — stand-up → build → review → decide — and name the rhythm they'll run again in Lessons 9–10 (*Bloom: Apply*).
2. **State** what their project can demo right now in one verifiable sentence, and what it can't yet (*Bloom: Explain*).
3. **Decide** Accept or Reject on each review fault with a reason, and write the first thing next leg as a concrete, verifiable action (*Bloom: Evaluate*).

---

## Page One — read this before class starts

### What today produces (three student outputs)

1. **One running MVP** — a demonstrable "sense → act" loop, at minimum one complete segment;
2. **One review record** — the Picky User's 3 faults + Quinn's 5-item list, 2 items actually tested, every fault judged with a reason;
3. **One baton handoff sheet** — where the leg ended (a verifiable sentence), the one review fault that matters most + the decision, and the first thing next leg.

### Three things you need to do

1. **Follow the clock.** Work down the timeline; every block says how many minutes and what to do. Shift gears on time — the gear-change *is* the lesson.
2. **Read the lines.** Every 🗣️ line is pre-written classroom speech — read it as-is, don't improvise. The AI prompts are all in Section 6 — project them.
3. **Circulate, don't teach.** From the "start" word on, your job is the circulation rhythm: one lap every 15 minutes, three looks each lap (screen / requirements sheet / face).

### Three things you do NOT need to do

1. **You don't need to write code.** "Fix the logic / fix the threshold" is all sent to AI by the student. The triage three-liners on the whiteboard are your whole playbook.
2. **You don't need to complete anyone's requirements sheet.** Today is the smallest closed loop, not the full sheet. The rest sleeps on the "later" list.
3. **You don't need to think up solutions or make decisions for students.** Your question is always "what does your requirements sheet say?" The veto stays theirs.

### When things go wrong

- **Live demo fails:** switch to the backup within 30 seconds (pre-rehearsal screenshots / pre-trained model), using Section 5's speed sheet. **This is not an incident — the plan is designed for it.**
- **Student device fails:** swap the device or the cable. Don't repair.
- **Network fails:** aily-blockly is local and runs offline; Codecraft (web) is the backup. AI chat needs the network — T-1 and same-day tests each once. Full offline → the build becomes "pure hardware + handwritten logic," the review proceeds with human peers. A whole-lesson reschedule is the last resort (the three marathon legs are continuous; rescheduling costs more than downgrading).
- **You're stumped:** smile, and say *"Let's ask AI together."*
- One-liner: **swap, cut to backup, ask AI.**

---

## Before Class

### 1.1 A week ahead

- [ ] Confirm **student:TA ratio ≤ 6:1** — **this lesson has the tightest TA staffing in the whole course**; 3 TAs split per 2.2; borrow a 4th if you can.
- [ ] **Collect Lesson 7's Brief Wall** (the sticky notes) — the stand-up refers to them today; list absentees and prepare the comeback flow (see 3.1 ⚠️).
- [ ] **Parts pool (Grove 40-in-1) set up in the Lesson 7 four-table sort;** against last lesson's hardware-check rows, **estimate the hot parts** (which modules will be fought over) and coordinate supply for anything short.
- [ ] Teacher rehearsals (see 1.3) — especially the "review persona" prompts and the crash-protocol lines.

### 1.2 On the day (arrive ~1 hour early)

- [ ] **Test aily-blockly on every machine** (the main build platform; installed in Lesson 6 — any missing/broken installs follow 3.1 ⚠️ pairing or TA-assisted install); codecraft.seeed.cc tested as backup (policy in 4.3).
- [ ] **Grove Beginner Kit: 1 per headcount; XIAO ESP32S3 Sense: 2 spares** (students' vision modules may need them).
- [ ] **Parts pool: 4 tables ready; a blank sheet of paper on each table as the check-out register** (TA draws four columns before class: module / name / time / return ✓); a corner of the whiteboard reserved as the hot-parts queue area.
- [ ] **Brief Wall in place; the three rules projected and kept on** (slide; Section 6 — nothing printed):
  1. Check against your requirements sheet — changing it is allowed, cross it out, don't erase;
  2. **15 minutes with no progress = raise your hand** — stuck is not shameful; toughing it out silently is;
  3. Code questions go to your AI first ("one step at a time" is the first-order help discipline).
- [ ] Whiteboard: **three-column triage board** (tech-stuck / direction-drift / morale-drained).
- [ ] **One hourglass or timer** (for the stand-ups); "15-minute hand-raise" is announced, no physical signs needed.
- [ ] **Baton handoff sheet + review record templates queued for projection** (Section 6) — **this lesson prints nothing**; everything goes in the student workbook.

### 1.3 Rehearsals (run it yourself before class)

1. Take one backup-topic requirements sheet and send both Section 6 review prompts to AI: the Picky User's 3 faults + Quinn's 5-item list — **check whether AI "praises"** (if it does, push back per 3.7 ⚠️ and keep this dialogue as the in-class demo material); **also verify Quinn's entrance condition in a fresh window** — what happens calling Quinn with no background, and with the background sentence — mention this contrast in one line in class;
2. **Rehearse the stand-up:** hold the hourglass and say 3 fake student goals aloud; practice pushing "keep working" into "make ___ run";
3. **Rehearse the crash protocol:** pretend a student's project can't be built; walk them to a shrink plan in 15 minutes — run the lines once;
4. **Fill one sample baton handoff sheet** (for in-class projection).

### 1.4 Supplies: three buckets

**📦 In the kit (count only, nothing to buy)**
- Grove Beginner Kit (1 per student); XIAO ESP32S3 Sense (2 spares); Grove 40-in-1 parts pool (4 tables); USB cables; computers; circulating tablet; projector; whiteboard + pens; Brief Wall (from Lesson 7); hourglass/timer.

**🛒 You buy**
- **Nothing** (hot-part gaps run on "queue + substitute" — no purchase promises).

**🖨️ Printing**
- **None. This lesson prints nothing** — the three rules, review prompts, baton handoff sheet, and review record are all projected; students write in their workbook. The check-out register is one blank sheet per table (TA draws the columns before class).

---

## Session Map (no clock-face minutes — start whenever class starts and work down the lengths. Hands-on blocks get whole chunks; you only call relative nodes: "half of the first half done" / "15 minutes to review." No scheduled break.)

| Act / Block | Length | Students are… | You are… |
| --- | --- | --- | --- |
| **Act 1 · The start** | 25 min | | |
| Opening | 10 min | hearing the 30-sec look-back + the three legs + MVP + the three rules | running the Brandy 1-key hook; projecting the three rules |
| First stand-up | 5 min | saying one verifiable sentence: "today I'll first make ___" | holding the hourglass; pushing "keep working" into "make ___ run" |
| Check out parts | 10 min | checking out per the hardware row, registering | TA B calling tables in batches; hot parts → queue area |
| **Act 2 · The build** | 120 min | | |
| Build, first half | 60 min | splitting the loop: sense first, then act; AI first for code; hand up at 15 min stuck | the circulation rhythm — 15-min laps, three looks; triage by the whiteboard |
| Mid-way stand-up | 5 min | one line: where I am / where I'm stuck / next step | hourglass; noting who can't say "next step" — rescue them first in the second half |
| Build, second half | 55 min | closing the loop; fast-lane ladder | the "hands off at 15 min to review" call; two-liners reminder |
| **Act 3 · Review & handoff** | 35 min | | |
| AI as reviewer (**never cut**) | 15 min | two review conversations; 2 items tested for real | screening the prompts; Quinn's entrance background; the push-back demo if AI praises |
| Decide & execute | 10 min | Accept/Reject each with a reason; fix what can be fixed now | watching for accept-everything (30-second one-on-one) |
| Baton handoff sheet | 5 min | filling the sheet in the workbook + log | projecting the template; returning "keep going" answers |
| Close | 5 min | returning unused modules; log finish | the three-wins recap + Lesson 9 preview |

> Build leg total = 135 min (stand-up 5 + parts 10 + build 115 + mid-way stand-up 5); review & decide etc. = 30 min; opening = 10 min — matching the config spec's "135+30."

### 2.1 Time flexibility

- **Most compressible:** check out parts (10→7 min, TAs pre-sort); the mid-way stand-up (5→3 min).
- **Next compressible:** build second half (55→45 min — close the smallest loop and release); the baton sheet (5→3 min, template copied from screen).
- **Never cut:** **the AI review 15 min + decide 10 min (the institutional floor)**; the first stand-up; the 30-second look-back.
- **Crash-protocol deadline:** a single student's project crashes → a shrink plan must exist within 15 minutes. No long engagements.

### 2.2 TA split & briefing (this lesson's standard)

**A 5-minute TA briefing before class** covers one page:

- **TA A (direction officer):** watches for **direction drift** — students drifting off the requirements sheet (adding features, switching topics) → pull back: "What's your core feature? Does this step serve it?"
- **TA B (tech officer + parts register):** rescues only the **stuck** — goes only when the 15-minute hand-raise triggers; first question on arrival: "Have you asked AI? Did you paste the error to it?" — guides "one step at a time" to cut the problem small, **never hands over code**; also runs each table's check-out sheet and the hot-parts queue.
- **TA C (pace officer):** keeps time (stand-up hourglass, the 15-minute rule, the review can't be squeezed); watches for morale-drained students → lower the target and cut smaller steps ("today we only hold one segment of the loop"); hands out the fast-lane ladder.
- **The triage three-liners** (on the whiteboard): tech-stuck → ask AI first, one step at a time; direction drift → back to the requirements sheet; morale-drained → lower the target, cut smaller steps.

---

## Section 3 · Segment-by-segment script

### Segment 1 ｜ Opening: MVP + the three rules (10 min) 【Act 1 · The start】

🗣️ **Say this:**

> "30-second look-back: last session, your project got its brief — the requirements sheet is in your workbook, the core feature is down to one, and what got cut keeps its name. The session before, your project moved into your own computer — from tenant to owner — and for the first time you saw what lives inside the code AI writes."
>
> "From today, the course shifts gear. Before, you followed me; from today, **I only circulate. I don't teach.** What comes next is the marathon — three legs. **Leg one (today): build your project's MVP. Leg two (Lesson 9): bring in the help** — new modules, new libraries, and the MVP grows new abilities. **Leg three (Lesson 10): the final polish — out to the showcase to meet people.** Every leg runs the same rhythm: stand-up → build → AI review → decide → handoff. Run all three legs, and your project has grown up."
>
> "What's an MVP? It's engineer slang for **minimum viable product** — **the smallest version you can put on the table and demonstrate.** Careful: it's not a half-finished thing. Half-finished is 'made half of it.' MVP is '**minimal but one complete loop**' — it senses something, then it reacts, start to finish, once. All the features on your requirements sheet? Not today. Today is only the smallest loop. Remember Neil's spiral development? Today is lap one."
>
> *(switch to the Brandy case page)* "Remember Brandy from the kickoff session? Li Shiwen, Seeed's application engineer — the one who built a voice keyboard with zero code. Look at her first version — **it had one key.** One. And the acceptance standard was a single line: **20 presses in a row, not one missed.** Doesn't pass? No new features. Passes? Then the second key goes in. She uses that keyboard every day now. That's a professional engineer's MVP: minimal, but a complete loop, with an acceptance standard stated out loud. **Minimal is not crude — it's professional.** Your first loop is the same: don't grab for more. Walk it through once. Twenty presses, not one missed."
>
> *(point at the three rules, read them one by one)* "Three rules. One: check against your requirements sheet — changing it is allowed, cross it out, don't erase. Two: **15 minutes with no progress = raise your hand.** Stuck is not shameful; toughing it out silently is. Three: code questions go to your AI first. I and the TAs answer direction only and rescue the stuck only."

👀 **Students do:** listen; open the requirements sheet in their workbook (handwritten books open; md docs on screen).

⚠️ **Pitfalls:**
- A student missed Lesson 7 (no requirements sheet) → the comeback flow: pick one backup topic (2 minutes) → TA A writes a mini requirements sheet with them in 5 minutes (three sections, one line each) → join the rotation normally; the review record is still written.
- A student missed Lesson 6 (no aily-blockly) → those who arrived early get TA-installed via the offline USB stick; anyone else pairs up with a neighbor after the opening, same as the Lesson 6 comeback; installed after class. Nothing to be ashamed of.
- "What if I don't finish?" → "The first version is only the smallest closed loop. Everything else on the sheet is sleeping soundly on the 'later' list."
- "Does one key really count as a project?" → "Yes. She verified the hardest segment first — your first loop verifies your hardest segment first, too."

---

### Segment 2 ｜ The first stand-up (5 min) 【Act 1 · The start】

**Two ways to run it — pick by headcount** (one purpose only: everyone says today's goal as one verifiable sentence):

- **Small class (a full circle fits in 5 minutes):** everyone stands — really standing, that's the stand-up's dignity — and says it one by one; you hold the hourglass; "you first."
- **Large class (a full circle is chaos):** don't go around — pair up and say it to each other, then **write the sentence at the top of the requirements sheet** (that's the stand-up's trace); you call 3–4 people at random to stand and say it to the class; the rest get a glance at their page as you circulate.

🗣️ **Say this:**

> "The stand-up — the first thing every marathon work session does. The rule: one sentence each, no more: **'Today I'll first make ___ run.'** It has to be verifiable — 'keep working' doesn't count; 'make the button light the LED when pressed' counts."

👀 **Students do:** say / write the one-sentence goal; sit down and get ready to start.

⚠️ **Pitfalls:**
- Vague goal ("keep working on my project") → push on the spot: "The moment you finish — what will I be able to see?" Push until it's one verifiable action.
- The stand-up turns into a report (someone talks over 30 seconds) → raise the hourglass: "Noted. Details are for build time, one-on-one."

---

### Segment 3 ｜ Check out the parts (10 min) 【Act 1 · The start】

🗣️ **Say this:**

> "Check-out rules: take only what your requirements sheet's hardware row says; register everything you take — name on the sheet on your table. **No taking parts you don't need** (everything you eyed during the tour waits until the sheet changes). Hot part already gone? Write it in the queue area on the board — then find a substitute. Remember? An engineer's first lesson: solve the problem with what you have."
>
> "At the end of every leg, parts you're not using go back. It's a shared pool — you'll need it next leg."

👀 **Students do:** check out modules per the hardware row, register; main kits (Grove boards) in place.

⚠️ **Pitfalls:**
- Check-out bottleneck → TA B calls tables in batches (tables 1 and 3 first); whoever's checked out starts building.
- A hot part runs out and there's an argument → register in the queue area + the "make it or not" three questions to coordinate substitutes; **no purchase promises.**
- A student's sheet lists something not in the pool → change the need on the spot (cross out, don't erase, write the substitute); TA A helps in 2 minutes.

---

### Segment 4 ｜ Build, first half (60 min) 【Act 2 · The build】

🗣️ **Say this** (one opening line — after this, the whole lesson is "circulate"):

> "Start. First move: cut the smallest loop into two steps — first make **it sense** (the sensor has a reading), then make **it react** (light / buzzer / screen). One step at a time. I do one lap every 15 minutes; raise your hand and I'm there. Water and bathroom — your call. Devices stay on; AI conversation windows stay open."

**Your circulation rhythm (this lesson's core skill — the shift from teaching to circulating):**

- **One lap every 15 minutes**, three looks per lap: the screen (chatting with AI, or staring off / browsing?), the requirements sheet (is it on the table? are they building to it?), the face (a frown past 5 minutes — stop and ask one question).
- **Intervention red line:** direction only ("Back to your sheet — what's the core feature?"); no writing code, no thinking up solutions, no making decisions; a student asks "which should I do?" → "What does your requirements sheet say?"
- **The 15-minute hand-raise triggers:** TA B arrives first, a three-step triage — ① Have you asked AI? (no → ask first) ② Did you paste the error to AI? (yes → guide "one step at a time," cut the problem small) ③ Still stuck → a direction, not an answer ("What's another way to say the goal of this step?").
- **At the half of the first half, one whole-class call** (no one interrupted): "Half of the first half done — pause and think: which step of your loop are you on?"

👀 **Students do:** build in pieces; stuck → AI first; 15 minutes no progress → hand up; requirements sheet on the table.

⚠️ **Pitfalls:**
- A student quietly changes the sheet and adds features → no scolding; point at the projected rule: "Change is allowed — cross it out, don't erase. But ask first: does it serve the core feature? No? It goes on the 'later' list."
- **Fast student done in 40 minutes** → the three-rung ladder in order: ① build the "later" list's first item; ② be your neighbor's human tester; ③ write a one-page user manual for the project (the kind anyone could read and understand).
- **Project crash** (the technical path is dead, e.g. "recognize 10 hand gestures at once") → start the crash protocol: you arrive; within 15 minutes define the shrink plan — "Back to the Scope Killer: which cut lets it live? Cut to 'recognize 2 gestures and light the LED' — can you do that? Then that's what we build." Cross-and-keep on the sheet.
- **The 15-minute rule never triggered all lesson** → note on the reflection page (a quality metric — it means students are toughing it out or the goals are too timid).

---

### Segment 5 ｜ The mid-way stand-up (5 min) 【Act 2 · The build】

- No unified break; the mid-way stand-up is done standing (a stretch too), hourglass timed.
- 🗣️ "One line: where I am / where I'm stuck / what I do next. Anyone who can't say 'next' — the TA notes your name, and you get rescued first when the second half starts."

---

### Segment 6 ｜ Build, second half (55 min) 【Act 2 · The build】

🗣️ **Say this:**

> "Second half's job: **close the loop.** Whatever segment the loop is still broken on — that's what you fix. **15 minutes before review, everyone stops.** Wherever you are, the review starts on time. Remember: the review isn't something you earn by finishing — **a half-finished thing deserves the faults even more.**"

- Circulation rhythm same as 3.4; **from "15 minutes to review" onward**, remind table by table: "Save your progress. Prepare two lines: my project can ___ now; it still can't ___."
- The two lines are the review's **feeding lines** — **the review conversation must be fed the current real state**; anyone feeding the old brief description gets sent back to rewrite.

⚠️ **Pitfalls:**
- A student begs "give me 10 more minutes" at the stop → warm but firm: "The review 15 is the institutional floor — nobody squeezes it, including me. Write your 'can't yet' clearly — that's the review's first material."
- Morale-drained ("everyone else's is so good") → TA C: "One thing more than yesterday is a win. Is your loop closed? Closed = today's 100."

---

### Segment 7 ｜ AI as reviewer (15 min — never squeezed) 【Act 3 · Review & handoff】

🗣️ **Say this:**

> "Hands off. Review time. Before, you had AI as a colleague. Today, it's a **judge** — its job is finding faults, not praising you. Two judges: first, the real person from your requirements sheet (the Picky User); second, an old friend — Quinn. A sizing note: in Lesson 3's group build, the Picky User picked one fault. From today it's the full edition — **3 faults + a 5-item list** — and every leg from here runs this size."
>
> "Two review prompts, on screen; **keep going in the conversation you already have — no new windows.** Note: you must feed the **current real state** — 'it can do this now, it can't do that' — a bragging review is no review at all."

**Prompt one on screen (the Picky User, 3 faults):**

```text
You are now my real user (name: ___; their situation: ___ — copy the real
person from my requirements sheet).
My project currently does: ___ (current real state, no bragging).
It still can't: ___.
You are not allowed to praise me. As them, pick 3 faults:
the one they'd care about most, the one most likely to make them not use it,
the one most confusing. One sentence per fault.
```

**Prompt two on screen (Quinn, 5-item list):**

```text
Quinn, still you. Based on the current state: my project can ___ now, and can't ___ yet.
You're a test engineer. Give me a 5-item list of "how to break or fail it,"
specific to how I operate it and what I watch for.
```

> ⚠️ **Quinn has an entrance condition:** this conversation needs the BMAD team in it — Quinn is the team's test engineer; in a fresh window it doesn't know the name. Two cases:
>
> - Your project conversation has run continuously since Lesson 4's team build (or BMAD was already configured for the project per Lesson 4) → send it directly;
> - A fresh project conversation → **send one background line first, then prompt two** (small print on screen):
>
> ```text
> This conversation has a BMAD team: John (PM), Sally (UX designer),
> Winston (architect), Amelia (developer), Quinn (test engineer).
> Remember them — I'll call on them directly from now on.
> ```
>
> (The full installed BMAD — `npx bmad-method install` — stays an after-class, voluntary thing, per the Lesson 4 line; this one background line is all class needs.)

> "List in hand — pick 2 items and actually test them. Record the results in the review record in your workbook."

👀 **Students do:** the two review conversations → record 3 faults + 5 items → test 2 for real.

⚠️ **Pitfalls:**
- ⭐ **The AI review turns into AI praise** ("your project is great, may I suggest some features…") → the student pushes back (projected): "No praising. Faults only — 3, one sentence each." Project your own pre-rehearsed "AI praised → I pushed back" demo conversation once.
- A review item contradicts the requirements sheet (AI pushing a cut feature) → a teaching point: "It doesn't know your trade-off history. Flip to your 'later' list — this one's already slept there. Original verdict stands."
- Offline → human peer review instead (the same 3-faults-5-items frame, executed by the neighbor, swapped) — **the review is never canceled, only its executor changes.**

---

### Segment 8 ｜ Decide & execute + the baton handoff sheet (15 min) 【Act 3 · Review & handoff】

🗣️ **Say this:**

> "Old rule, item by item: **Accept or Reject — and both need a reason.** One reminder: rejecting with a reason scores the same as accepting — but if you accept everything, I'm coming to talk to you (no backbone is more dangerous than no changes)."
>
> "Accepted and fixable now — fix it (anything under 5 minutes). Can't finish? Into the handoff sheet under 'first thing next leg' — not 'later,' the **first action of next leg's build time.**"
>
> "Fill the baton handoff sheet (template on screen, into your workbook). It's your marathon baton — the moment you walk into Lesson 9, it's how you find today's feeling again. It's also the comeback anchor for anyone who missed class."

**Baton handoff sheet template (projected; identical to the workbook):**

```text
# Baton Handoff Sheet · Leg 1
Name: ______  Date: ______

## Where this leg ended (one verifiable sentence: what it can demo)
## The review fault that matters most + my decision (accept/reject + reason)
## The first thing next leg (specific, verifiable)
```

👀 **Students do:** decide each with a reason → fix what's fixable → sheet into the workbook → log (four-line template; "done" reads: "my project's first version can ___; the review picked ___ faults; I accepted ___ and rejected ___").

⚠️ **Pitfalls:**
- Accept-everything → 30-second one-on-one: "Eight items all in? Can you even finish them? Take the 3 most important; reject the rest — rejecting is a professional decision too."
- The sheet's "first thing next leg" says "keep going" → send it back: "Write it as a verifiable action — 'make ___ work even when ___.'"

---

### Segment 9 ｜ Close (5 min) 【Act 3 · Review & handoff】

🗣️ **Say this:**

> "Look back at this leg — three things done. One: from a requirements sheet, you made a **demonstrable first version** — it really sensed something, it really reacted. Two: you took a full round of faults from two judges, and you're still standing. Three: you made Accept-or-Reject calls with reasons, and you know the first thing next leg. That's one complete engineer's iteration — today, you really ran a whole lap."
>
> "Next session preview: the marathon's second leg — **both homes at once** (aily and the web version), and your project grows new abilities. Bring your baton handoff sheet and your two-views cheat sheet."
>
> "Return modules you're not using; main kits in the box; the Brief Wall stickies stay."

👀 **Students do:** return modules; pack up; log finish.

**📎 Appendix (slides 18–42 — the full Brandy case, used flexibly):**

- **Where it sits:** slide 4 is the 1-minute hook; the appendix is Brandy's full share, remade in Chaihuo style (25 pages): who she is → look beyond the finished product → the big-picture before/after → 90% of attention interrupted → two devices, one method → where to start → the method overview (four tools) → a live mini-exercise (can be played with the class) → the voice keyboard end to end (breaking the problem / mind map / I/O contract / the one-key first loop / final interaction / enclosure pitfalls / sketch to 3D / the demo checklist) → the digital hourglass end to end (breaking the problem / wiring & SOP / decomposing "like sand" / the photo where the logic is wrong) → the two key "translations" → a reusable hardware prompt → the five-step loop → closing on the four-line spec.
- **How to use it:** ① time left after the close → pick pages (suggest 19/22/26/30/34/38/42, ~10–15 min, each page's notes carry a script); ② a full walkthrough is ~25 min — good for after-school extension or the next lesson's opening; ③ no time → one line: "The appendix is in the deck — flip through it at home."
- **Reusable bits:** page 26's live mini-exercise works straight as class interaction; page 34's demo checklist is the pre-showcase check template for Lesson 10; page 40's hardware prompt template — have students photograph it; Lesson 9 applies it directly to new modules; page 42's four-line spec is referenced back in Lesson 9.

---

## Section 4 · Live demo backup plan

| Block | Time short (compress) | Goes wrong live (substitute) | Can't happen at all (fallback) |
| --- | --- | --- | --- |
| First stand-up | 5→4 min (by table) | two parallel stand-ups | written one-liners (TA collects) |
| Check out parts | 10→7 min (pre-sorted) | tables called in batches | start on the main kit; modules arrive later |
| Build, first half | keep only "sense has a reading" | offline → pure hardware + handwritten logic | minimum target: "wiring correct + reading visible" |
| Build, second half | 55→45 min | lower the target: loop keeps one segment | crash protocol: shrink plan in 15 min |
| AI as reviewer | **never cut (institutional floor)** | offline → human peer review (same frame) | the review is never postponed — the executor changes, not the review |
| Decide & execute | 10→8 min | decide only the 3 most important | decisions go in the handoff sheet; changes move to next leg |
| Baton handoff sheet | 5→3 min | dictated, TA writes | filled after class; workbook screenshot as proof |

### 4.1 Network policy this lesson

- **aily-blockly is the main build platform** — installed locally, runs offline; Codecraft (web) is the backup. AI chat needs the network: test T-1 and same-day, once each.
- **AI chat down and the hotspot dead** → the build becomes "pure hardware + handwritten logic" (progress recorded in the handoff sheet), **the review proceeds** (human peer review); aily itself runs offline, so programming help pauses but the platform doesn't. A whole-lesson reschedule is the last resort — the three marathon legs are continuous, and rescheduling costs more than downgrading.
- When offline, the AI review runs as human peer review (the same 3-faults-5-items frame, neighbors swapped); once the network returns, a real AI review round can be made up next leg.

---

## Section 5 · Pitfall speed sheet

Three lines first: **swap, cut to backup, ask AI.** Today's fourth: **the review is never squeezed.**

| Situation | What you do |
| --- | --- |
| ⭐ Review squeezed by progress pressure | not an option — remind table by table at 15 min to review; the review opens on time no matter what; one squeeze = a major backfill event |
| AI review turns into AI praise | the push-back prompt: "No praising. Faults only — 3, one sentence each"; project your demo conversation |
| Student quietly adds features / drifts | point at the projected rule: "Cross it out, don't erase; does it serve the core feature?" |
| The 15-minute rule never triggered | note on the reflection page (quality metric: toughing it out, or goals too timid — backfill a review) |
| Project crash | the crash protocol: shrink plan in 15 min (the Scope Killer cuts until it lives); a leg-3 crash → the "honest failure" showcase route |
| Fast student wandering | the three-rung ladder: later-list item #1 → neighbor's human tester → a user manual |
| Accept-everything | one-on-one: "Take the 3 most important; reject the rest — rejecting is a professional decision" |
| Hot part runs out | queue area + the substitute three questions; unused parts returned each leg; no purchase promises |
| Stand-up turns into a report | stand for real + hourglass; over 30 seconds → one-on-one in build time |
| Requirements sheet forgotten | one of the three looks; the check-against-sheet ritual is built into the opening |
| New conversation window for the review | the old rule: "Keep going in the window you have — the review has to catch your trade-off history too" |
| Absent student returning | read the handoff sheet / backup topic in 5 min → TA fills the gaps in 2 min → join the rotation |

### Appendix: student questions and how to answer them

| Student asks | You say |
| --- | --- |
| "What if I don't finish?" | "The first version is only the smallest closed loop. Everything else is sleeping soundly on the 'later' list." |
| "AI says it's really good — do I still change it?" | "Make it stop praising and find faults. A review that praises you is a review that didn't show up to work." |
| "Can I change my requirements sheet?" | "Yes. Cross it out, don't erase — let everyone see you changed your mind. But first ask: does it serve the core feature?" |
| "Everyone else's is better than mine." | "One thing more than yesterday is a win. Is your loop closed? Closed = today's 100." |
| "Why review something unfinished?" | "Because a half-finished thing deserves the faults even more. The review isn't a reward for finishing — it's how you finish." |

---

## Section 6 · Prompt phrase library (teacher reference)

> All of today's prompts and templates are maintained here — every reference in the segments matches this section word for word; the student workbook carries the same text. Project the whole block so students can copy it straight into AI. **Discipline restated: both review rounds run in the same conversation — change roles without changing windows; a new window = a dropped baton.**

### 6.1 The three rules (Segment 1 — keep projected)

```text
The three rules of build time
One. Check against your requirements sheet — changing it is allowed, cross it out, don't erase.
Two. 15 minutes with no progress = raise your hand — stuck is not shameful; toughing it out silently is.
Three. Code questions go to your AI first — "one step at a time."
```

### 6.2 Review prompt one: the Picky User's 3 faults (Segment 7)

```text
You are now my real user (name: ___; their situation: ___ — copy the real
person from my requirements sheet).
My project currently does: ___ (current real state, no bragging).
It still can't: ___.
You are not allowed to praise me. As them, pick 3 faults:
the one they'd care about most, the one most likely to make them not use it,
the one most confusing. One sentence per fault.
```

### 6.3 Review prompt two: Quinn's 5-item list (Segment 7)

```text
Quinn, still you. Based on the current state: my project can ___ now, and can't ___ yet.
You're a test engineer. Give me a 5-item list of "how to break or fail it,"
specific to how I operate it and what I watch for.
```

> **The entrance condition (small print on screen):** Quinn is the BMAD team's test engineer — the conversation needs the team in it for Quinn to appear. Projects running since Lesson 4's team build (or already configured with BMAD) can send it directly; a fresh conversation sends the background line first:
>
> ```text
> This conversation has a BMAD team: John (PM), Sally (UX designer),
> Winston (architect), Amelia (developer), Quinn (test engineer).
> Remember them — I'll call on them directly from now on.
> ```
>
> The push-back prompt when AI praises (projected): "No praising. Faults only — 3, one sentence each."

### 6.4 The baton handoff sheet template (Segment 8 — identical to the workbook)

```text
# Baton Handoff Sheet · Leg 1
Name: ______  Date: ______

## Where this leg ended (one verifiable sentence: what it can demo)
## The review fault that matters most + my decision (accept/reject + reason)
## The first thing next leg (specific, verifiable)
```

### 6.5 The review record template (Segments 7–8 — identical to the workbook)

```text
# Review Record · Leg 1
## The Picky User's 3 faults
1. ______ → my decision: accept/reject, reason: ______
2. ______ → my decision: accept/reject, reason: ______
3. ______ → my decision: accept/reject, reason: ______

## Quinn's 5-item list (test 2 for real, note the results)
1. ______ tested: passed/broke ______
2. ______ tested: passed/broke ______
3–5. (key words only) ______
```

---

## Section 7 · Localization slots

| Where | Original | Swap-in suggestion |
| --- | --- | --- |
| Review persona | the real user from the requirements sheet | naturally local — you only check the persona is a real person, never who it is |
| Crash-protocol shrink example | "recognize 2 gestures and light the LED" | one real past precedent from your class's project types (a past shrink story) |
| Hot-part estimate | per last lesson's hardware rows | recount from this class's actual sheets before class — don't copy last term's |
| Fast-lane user manual | "a one-page manual anyone could read" | local style: a version for grandparents / a version for the neighbors' parents |
| Brandy hook example | one key, 20 presses | any local engineer's "smallest complete loop" story you can tell in one minute |

---

## Section 8 · Teacher reflection page

Take 10 minutes after class. Anything counts — even one line.

1. Did the review get squeezed? Did it open on time: ______
2. Smallest closed loop running (a complete demonstrable sense→act): ___ / ___ students
3. Review records complete (3 faults + 5 items + 2 tested): ___ / ___ students
4. Baton handoff sheets in the workbook with a verifiable "first thing next leg": ___ / ___ students
5. **Times the 15-minute hand-raise rule fired: ___ (= 0 → mandatory backfill review: toughing it out, or goals too timid?)**
6. Crash protocol cases: how many, and what were the shrink plans: ______
7. Did any 🗣️ line sound awkward out loud? Cross it out; write what you actually said.
8. Keep this session next time: ______；change: ______
9. Best student one-liner from the review round (collect for the showcase): ______

Photograph the page and send it to the teaching group, or tuck it back in the course folder. **Every line you write becomes a pitfall another teacher won't hit in the next edition.**

---

_Version: EN v1 ｜ 2026-08-25 ｜ Source: CN 讲师版 v4（2026-08-06；文件名标注 v2，修订说明含 v3/v4：MVP 主轴、三幕节奏、站会弹性化、去钟面时刻、Brandy 完整案例附录 42 页 PPT） ｜ 依据设计版：CFG-5 配置说明书 v1.0 "马拉松 · 第一棒"行（创作轮 90×1.5=135＋站会与评审 30）_

_Localization notes: BMAD 五角色（John/Sally/Winston/Amelia/Quinn）与 Brandy/Neil 等专名保留原文；「跑通第一圈」→ Run the First Lap（副题 Build Your Project's MVP）；「最小闭环」→ the smallest closed loop；「三幕节奏」→ the three acts（the start / the build / the review & handoff，换挡动作 the gear-change moves）；「站会」→ the stand-up；「领料」→ check out the parts（领用登记 the check-out sheet、热门件 the hot parts）；「15 分钟无进展必须举手」→ the 15-minute hand-raise rule；「分诊三句话」→ the triage three-liners；「崩盘协议」→ the crash protocol（缩小版 the shrink plan）；「快手三级加餐」→ the fast-lane ladder；「棒交接单」→ the baton handoff sheet（回归锚 the comeback anchor）；「挑剔用户完整版」→ the Picky User, full edition（3 faults + 5-item list）；「顶回句式」→ the push-back prompt；「投喂材料」→ the feeding lines（评审必须喂当前真实状态）；"最小不是简陋，是专业" → "Minimal is not crude — it's professional."；"评审不可取消，只可换执行者" → "The review is never canceled — only its executor changes."；Brandy 案例（第一版只接 1 个键、验收 20 次不漏）与附录弹性使用说明完整保留。课程换序上下文（第 6 课搬家→第 7 课立项→第 8 课开跑）在念稿中连贯保留。「不赌中文渲染」规则天然满足——一切屏幕内容为英文/数字/图形。_
