# Teacher's Guide ｜ Lesson 7 · Brief Your Project

_From the Project Wall to a Requirements Sheet · Vision Wrap-up + The Big Brief ｜ Chaihuo Maker Academy · M0 Hardware Foundation · Smart Hardware Fundamentals ｜ 10-session term ｜ 3 hours (no scheduled break)_

> **Source:** 中文版 v4（M0_教师课件_CFG-5_第7课_为我的作品立项_v2.md，文件名写 v2，文末修订说明含 v4：2026-08-06 PPT 18→19 页、Brandy 契约对照页、Final Project 口径清理）
> **Localized edition** — same blocks, same minutes, same teaching intent; classroom language rewritten for an English-speaking teacher to pick up and teach from.

---

## The one-sentence brief

Today is the **milestone session of the whole term.** The first half finishes the Lesson 5 vision-to-action project — **AI as tester** opens a **trouble list**, classmates test each other's boards, and every fault gets an **Accept or Reject** call. The second half is the **big brief**: starting from the sentence each student pinned on the Project Wall in Lesson 2, going through the **PM talk**, the **UX talk**, and the **Scope Killer**, they write a **requirements sheet** that can actually be built from (requirements.md). The last half hour is the **parts-pool tour**, calibrating the brief against the hardware they actually have. The core experience is one line: **teacher questions + the student's own real information + AI deepening → the student's own requirements sheet.** Every block's output lands in the student's own record — the student workbook or notebook.

The session runs three big arcs: **morning arc · vision wrap-up** (~70 min: opening → self-check → AI's trouble list → peer test → Accept or Reject + fix → share-out & log) → **afternoon arc · the big brief** (~61 min: the Project Wall segment — Neil's line, the directions page, the four notes, the re-topic lane → PM talk → UX talk → the requirements sheet → the Scope Killer) → **parts-pool tour + briefing ceremony** (~49 min: tour briefing → the tour → buffer → ceremony close). Students use the bathroom on their own during hands-on time.

**Today's iron law: the topic is the student's, not yours.** In the brief arc you only ask questions; you never give answers. Choosing a topic *for* a student is this lesson's biggest teaching accident — more hidden, and more damaging, than canceling the class.

---

## 🎯 Learning Objectives

*By the end of this session, students will be able to…*

1. **Run** a peer test on a classmate's vision project, recording pass/fail per item on their trouble list (*Bloom: Apply*).
2. **Decide** Accept or Reject for each fault found, and fix at least one using one of the three fix paths — fix the data / fix the logic / fix the threshold (*Bloom: Evaluate*).
3. **Write** a requirements sheet for their own project through the PM and UX talks — three sections (input / logic / output, ≤3 lines each), exactly one core feature, a "later" list of ≥1 item, hardware row signed after the tour (*Bloom: Create*).
4. **Justify** the trade-off they made — what they cut and why — in their own words (*Bloom: Evaluate*).

---

## Page One — read this before class starts

### What today produces (four student outputs)

1. **One tested trouble-list record** — AI opens the list, a classmate tests it for real, every item has a result (passed ✓ / how it broke);
2. **One Accept-or-Reject decision record** — every fault judged; what was rejected got fixed on the spot (data / logic / threshold); what was accepted carries an acceptance note;
3. **One requirements sheet** — three sections (input / logic / output, ≤3 lines each), exactly one core feature, a "later" list of ≥1 item, hardware row signed;
4. **One explainable trade-off** — "what I cut and why," sayable in their own words.

### Three things you need to do

1. **Follow the clock.** Work down the timeline; every block says how many minutes and what to do.
2. **Read the lines.** Every 🗣️ line is pre-written classroom speech — read it as-is, don't improvise. The AI prompts are all in Section 6 — project them and have students send them as-is.
3. **Ask, don't answer.** In the brief arc, your whole job is questions — "Who did you say you're making it for? When does that person actually hit this problem?" However ordinary the answer, it's the student's topic.

### Three things you do NOT need to do

1. **You don't need to write code.** In the fix round, "fix the logic / fix the threshold" is all sent to AI by the student — you just name the three paths.
2. **You don't need to know requirements engineering.** A requirements sheet is a piece of paper with three sections: what it senses, what it does under what condition, how it shows itself. Can't fit it in three lines = not thought through — cut. That ruler is all you need.
3. **You don't need to think of topics for students, or cut their scope.** The Scope Killer is an AI persona; the veto always stays with the student. If a student hasn't cut a single thing, sit with them and cut one — but *which* one is their call.

### When things go wrong

- **Live demo fails:** switch to the backup within 30 seconds (pre-rehearsal screenshots / pre-trained model), using Section 5's speed sheet. **This is not an incident — the plan is designed for it.**
- **Student device fails:** swap the device or the cable. Don't repair (swap-don't-repair is a course rule).
- **Network fails:** this lesson depends little on the vision platform (the model is already on the board) — SenseCraft down ≠ this lesson downgrades; Codecraft down follows the 4.3 downgrade (teacher reads the list aloud, peer questioning, a human Scope Killer).
- **You're stumped:** smile, and say *"Let's ask AI together."*
- One-liner: **swap, cut to backup, ask AI.**

---

## Before Class

### 1.1 A week ahead (once)

- [ ] Confirm **student:TA ratio ≤ 6:1** — the brief arc has the highest question density of the course; 5:1 is even better.
- [ ] Carry over Lesson 5's three-gates T-7 conclusion for SenseCraft; **today only needs the same-day re-check** (see 1.2). **If Lesson 5 already triggered a full-lesson downgrade, this lesson's vision half adjusts per 4.3 — the brief and tour arcs are unaffected (they barely touch the vision platform).**
- [ ] **Parts pool (Grove 40-in-1) split into 4 tables:** sense / output / actuation / mixed — sorted casually while setting up; **no table tents** — the four-table sort stays projected (see 3.13).
- [ ] **Collect the Lesson 2 Project Wall** (or photos of it) — the opener returns to it.
- [ ] **Have 3 backup topics ready** (defaults: a drink reminder / a posture checker / a pet-feeding timer; local swap-ins in Section 7) — written in your own notebook, not printed.
- [ ] Teacher rehearsals (see 1.3).
- [ ] **Day-before reminder** to the class group (copy-paste): *"Next session, two big things: your project is about to get 'harassed,' and your big project is about to get its brief. Bring your board and every project record — md doc or handwritten photos, either works."*

### 1.2 On the day (arrive ~1 hour early)

One person needs ~60 minutes — **arrive 1 hour early**. With a TA: the TA does the device check and table setup; you do the projection and 1.3 rehearsals. If time is really tight, **Rehearsal 2 (the full brief flow) is mandatory**; cut the rest.

- [ ] Re-test the codecraft.seeed.cc conversation end-to-end + sensecraft.seeed.cc reachable (if down, see 4.3 — most of this lesson barely touches the vision platform, no full-lesson downgrade).
- [ ] **XIAO ESP32S3 Sense: 1 per actual headcount + a few spares** (the models students trained in Lesson 5 should still be on the boards — spot-check 3); lens films peeled.
- [ ] **A-kit LED/buzzer: 1 set per table; the 40-in-1 parts pool: 4 tables sorted.**
- [ ] **Project Wall back in place; leave an empty wall next to it = the Brief Wall.**
- [ ] Every computer: **two browser tabs — SenseCraft on the left, Codecraft on the right.**
- [ ] **Sticky notes: 1 per student + thick pens** (briefing ceremony: "project name + core feature" on the Brief Wall).

### 1.3 Rehearsals (allow 40 minutes — play the student first)

One principle today: **you play the student first, end to end.**

**Rehearsal 1 ｜ the AI-tester list (used at 14:15)**
Run the 3.3 prompt on your own teacher-machine model; check the list is specific enough (too vague → use the ⚠️ return prompt). Save one "what a list looks like" screenshot for the in-class demo.

**Rehearsal 2 ｜ the full brief flow (today's spine — clock it under 40 minutes)**
Take one backup topic all the way: John (PM) talk → Sally (UX) talk → fill the requirements sheet → the Scope Killer cuts one. All in **one conversation** (the five-round relay rule from Lesson 4: change roles, don't change windows).

**Rehearsal 3 ｜ template self-check**
Fill a requirements sheet yourself: three sections each ≤3 lines, "later" list ≥1 item. **If you can't fit it, the template is too demanding — that's a template problem, not a student problem.**

**Rehearsal 4 ｜ the tour route (can be delegated to TA B)**
Walk all 4 tables, ~7 minutes each; confirm every table has at least one module students won't recognize (the discovery-picks material). A TA walk-through is enough — you don't need to walk it yourself.

### 1.4 Supplies: three buckets

**📦 In the kit (count only, nothing to buy)**
- XIAO ESP32S3 Sense (1 per headcount + spares); USB-C cables; A-kit LED/buzzer (1 set per table); Grove 40-in-1 parts pool (4 tables); computers; circulating tablet; projector; whiteboard + pens; the Lesson 2 Project Wall.

**🛒 You buy**
- **Nothing.**

**✨ Teacher brings**

| Item | Qty | Note |
| --- | --- | --- |
| Sticky notes | 1 per student | ceremony: "project name + core feature" on the Brief Wall |
| Thick pens | several | for the sticky notes |
| 3 backup topics | in your notebook | for re-topic-lane timeouts — spoken, not printed |

> **Zero printing.** The requirements-sheet template and the tour task sheet are projected (text in Section 6); students write in their workbook or notebook. No physical cards go out. No print burden on the teacher.

---

## Session Map (14:00–17:00 — shift the whole clock to your actual time, e.g. 9:00–12:00; block lengths stay. No scheduled break.)

| Clock | Block | Students are… | You are… |
| --- | --- | --- | --- |
| 14:00–14:10 | Opening link | hearing the 30-sec look-back + today's three things; un-finished students report to TA B | running the look-back; noting who needs the fallback prompt |
| 14:10–14:15 | Warm-up self-check | flashing scissors — does it still know them? quick retrain if not | watching; not panicking if half the models fail (it's the #1 live teaching material) |
| 14:15–14:30 | AI tester's trouble list | sending the 6.1 prompt, filtering to ≥3 testable items, writing them down | screening the prompt; returning vague items for specifics |
| 14:30–14:50 | **The peer test (acceptance condition)** | swapping boards + lists, testing item by item, recording results on each other's lists | stating the three rules; watching for sabotage; "power-cycle tester" for repeat offenders |
| 14:50–15:05 | Accept or Reject + one fix round | judging each fault; rejecting ≥1 and fixing it (data/logic/threshold); writing acceptance notes | naming the three fix paths; the "ask AI which path" line |
| 15:05–15:10 | Share-out + log | one "most vicious misread + my counter" per table; log line 1 | collecting the best one-liners (showcase material) |
| 15:10–15:22 | The Project Wall: Neil's line + directions + four notes + the re-topic lane | standing at the wall, re-reading their sentence, deciding: still love it? | guarding the iron law — ask, don't answer; timing the re-topic lane (5 min) |
| 15:22–15:34 | The PM talk | John interviews them: scene, last time, workaround, use | circulating: the citation check (real names in the chat?) |
| 15:34–15:46 | The UX talk | Sally writes the usage scenario — who, where, how, reaction | circulating: no names/places → send back; "colors go on the later list" |
| 15:46–15:59 | The requirements sheet | filling the first six rows; hearing the Brandy contract | projecting the template; the 2-minute "engineer's contract" talk |
| 15:59–16:11 | The Scope Killer | AI asks "would it die without this?" one by one; student vetoes | watching for zero-cuts (sit with them) and hollow shells (rescue the core) |
| 16:11–16:15 | Tour briefing | hearing the four-task sheet + rotation rules | projecting the task sheet; setting the 7-minute bell |
| 16:15–16:45 | The parts-pool tour | 4 groups rotating: find the modules, find substitutes, 3 discovery picks, sign | TAs at the tables; the one question per table: "which task are you on?" |
| 16:45–16:50 | Buffer | stragglers finish the sheet/sign; fast students write a mini requirements sheet | counting acceptance numbers; Brief Wall ready |
| 16:50–17:00 | The briefing ceremony + close | sticky on the wall, reading the core feature aloud; log; preview | running the ceremony; the Fab Academy closing line |

> The clock above assumes a 14:00 start — shift it whole. **No unified break all session**; students use the bathroom on their own during hands-on time.

### 2.1 Time flexibility

- **Most compressible:** the share-out (5→3 min); the tour briefing (4→2 min); the AI trouble list (15→12 min).
- **Next compressible:** the fix round (15→10 min — whatever can't be fixed goes on the "later" list); the tour (30→25 min, cut station 4).
- **Never cut:** **the peer test** (this half's acceptance condition — if forced to choose, cut the AI list to protect the peer test); the Scope Killer; the briefing ceremony; the 30-second look-back.
- **If time collapses in the brief arc, the priority ladder:** protect the PM talk > protect the three template sections > protect the one cut > the UX scenario can shrink to one sentence.

### 2.2 TA split

| When | TA A (dialogue quality officer) | TA B (hardware officer) | TA C (record officer) |
| --- | --- | --- | --- |
| Vision half | — | the fallback prompt + board swaps | filming (hands only, no faces) |
| Brief arc | the circulation red line — **the citation check**: chats with no student's own topic / real user name go back to fix; users written as "everyone" go back to the Lesson 2 name list | — | — |
| The tour | — | stations at the 4 tables, coaching "nearest substitute" (four-table sort stays projected); **one consistent line: we don't promise purchases** | — |
| All arc | — | — | template-ruler check on every finished requirements sheet (three sections ≤3 lines, later list ≥1, core feature = 1); Brief Wall posting order |

---

## Section 3 · Segment-by-segment script

### Segment 1 ｜ Opening link (14:00–14:10)

> 📌 Output anchor: none (link segment)

🗣️ **Say this:**

> "30-second look-back: last session, you moved your project into your own computer — from tenant to owner. Before that, in Lesson 5, you taught your board to recognize rock, paper, scissors — and to *do* something after recognizing: light up, beep. And you found AI's biggest secret: it's not dumb — you just taught it too little."
>
> "Three things today. One: finish last session's project — AI becomes the tester, your classmate tests your board, and we drag the faults out into the open. Two — **the big one: your big project gets its brief today** — starting from the sentence you pinned on the wall in Lesson 2, and walking it all the way to 'ready to build.' Three: tour the parts pool, and stock up for your big project."
>
> "First thing first. Lesson 5's link not finished — raise your hand. (note names) No problem: in a moment, during the self-check, a TA runs you through the fallback prompt — five minutes to 'recognize scissors and light the LED.' Then you join the peer test normally. Still not working? You share your neighbor's board and test as a team — records count the same. Today isn't about how pretty the project is. **It's about whether you can find fault.**"

👀 **Students do:** listen; unfinished students report to TA B.

⚠️ **Pitfalls:**
- A student missed Lesson 5 entirely (no model) → deploy the teacher's pre-trained model on a spare board; they join the peer test straight away (the "tester" role doesn't need their own model); the vision experience is made up after class — the brief arc is unaffected.
- "How far does the big project have to go?" → "The first five lessons were learning moves. The marathon starts next session (Lesson 8) — this is what you'll run. Today, you make it official."

---

### Segment 2 ｜ Warm-up self-check (14:10–14:15)

> 📌 Output anchor: none (self-check; dead models go to 3.5)

🗣️ **Say this:**

> "Plug in your little eye board — throw a scissors. Does it still know you? Knows you: sit tight. Doesn't: think back to last session's attribution — did the light change? Did you move seats? — Quick rescue: against today's light, take 10 new photos and retrain. That's 'fix the data' — you all know how."

👀 **Students do:** self-check the model; dead ones retrain fast (or wait for the 3.5 fix round); unfinished students catch up with TA B via the fallback prompt.

⚠️ **Pitfalls:**
- Half the models dead (new room / new light — common) → don't panic; this *is* the afternoon's first live teaching material: "See — new room, and it doesn't know you. Guess what item #1 on today's trouble list is going to be. You already know it."
- Retraining over 8 minutes → stop; use the "accept" strategy: write "this model only works at my original seat" on the record, and enter the peer test.

---

### Segment 3 ｜ AI tester's trouble list (14:15–14:30)

> 📌 Output anchor ①: every student has a trouble list of ≥3 items (written in the workbook or notebook, each specific to "how to do it, what you expect to see" — it's about to be handed to a classmate)

🗣️ **Say this:**

> "At the end of last session I said: today, AI becomes the tester. Remember Quinn — the one who helped you *break* your Pomodoro timer in Lesson 4? This is Quinn's vision-edition moment."
>
> "Send this to AI (project it), and replace the brackets with your own project:"

```text
Quinn, my project: a board with a camera that can recognize scissors, rock, and paper.
When it sees scissors it lights the LED; when it sees rock the buzzer beeps; when it can't
recognize anything, everything stays off.
You're a picky test engineer. Give me 5 tests for "how to make it misjudge or fail,"
each one specific: what I should do, and what I expect to see.
For example: hand gesture in backlight? Hand only half-visible? Switching gestures fast?
```

> "Got your list? Don't test yet — **filter it first**: items too vague ('might be inaccurate') go back to AI for a specific scenario; items irrelevant to your project get crossed off. Keep at least 3 you can genuinely try."

👀 **Students do:** generate → filter → write down the final list (to be handed to a classmate in a moment).

⚠️ **Pitfalls:**
- List too vague → the return prompt: "Please rewrite item X as a concrete test: what action I do, in what environment, what I watch for."
- Time collapses against the peer test → **cut the list to protect the peer test**: 3 items are enough; the peer test's minutes are never borrowed (it's this half's acceptance condition).

---

### Segment 4 ｜ The peer test (14:30–14:50)

> 📌 Output anchor ②: the peer-test record (both lists filled with results: pass = checkmark; broke = write exactly how)

🗣️ **Say this:**

> "Swap projects. In your hands: your neighbor's board + the trouble list they wrote. Test item by item, record on their list: pass, checkmark; broke, write exactly how it broke."
>
> "Three rules. One: the harassment is **only 'show it things'** — no touching wires, no taking parts off, no covering anything except the lens. Two: if you find a fault, don't laugh at them — the list you hand over is a knife, and it's a badge of honor too: your list getting tested to the breaking point means your neighbor is a real professional. Three: after you test theirs, they test yours — both lists get filled."

👀 **Students do:** swap boards and lists; test each other's items one by one; record the results.

⚠️ **Pitfalls:**
- The peer test turns into actual sabotage (pulling wires / covering the lens) → restate the rules once; repeat offenders get promoted to **power-cycle tester** (their official test: "unplug the power and plug it back — does it recover?" — which is, genuinely, an effective test).
- One side's project doesn't run → pair up on the working one; the student without a running board takes the tester+recorder role (records are still a deliverable).
- Finished early → free-form escalation: "Forget the list. Think of the nastiest move yourself."

---

### Segment 5 ｜ Accept or Reject + one fix round (14:50–15:05)

> 📌 Output anchor ③: the decision record (≥1 rejection fixed on the spot; every accepted item carries one line: "I know it fails when ___, and I accept it")

🗣️ **Say this:**

> "Take back your own list — look at what it's become: your project's full list of sins. Now judge them one by one: **Accept or Reject.**"
>
> "Reject? Fix it now. Three paths (write on the board): **fix the data** — go back into SenseCraft and photograph the scene where it broke; **fix the logic** — have Codecraft change a condition, like 'only counts if it recognizes it twice in a row'; **fix the threshold** — raise the confidence line from 70% to 85%."
>
> "Not sure which path? Don't wait for me — send the failure to AI: *'My model misjudges in ___ situation. Fix the data, fix the logic, or fix the threshold — which do you recommend, and why?'* Advice is advice — **which path is still your call.** Fixing the logic and threshold also goes to AI; your only job is the old rule: say the input and output clearly."
>
> "Accept? Write one line: **'I know it fails when ___, and I accept it.'** You made this call in Lesson 2 — today you make it more professionally."

👀 **Students do:** judge each fault → pick one path for ≥1 rejected fault and fix it now → write acceptance notes for the rest.

⚠️ **Pitfalls:**
- Everyone chooses "accept" (too lazy to fix) → require at least one rejection: "Pick the fault you'd most hate a judge to catch live."
- Everyone chooses "reject" (perfectionism) → remind them of the time: "You can't fix 5 faults in 15 minutes. Pick the most deadly one and fix it; the rest get accepted — that's what a trade-off looks like."
- Someone fixes via "the data" → point out the loop closing: "See — you're back at last session's attribution: whatever situation breaks it is whatever data you never fed it."

---

### Segment 6 ｜ Share-out + log (15:05–15:10)

> 📌 Output anchor ④: log line 1 (the four-line template; "done" reads: "I had AI open a trouble list, my classmate found ___ faults in my project, I fixed ___ and accepted ___")

🗣️ **Say this:**

> "One pick per table: 'the most vicious misread + my counter' — 30 seconds to the class."
>
> "Then log line one. Four lines as usual; today 'done' reads: I had AI open a trouble list, my classmate found ___ faults in my project, I fixed ___ and accepted ___. "

👀 **Students do:** one share per table; write the log (four-line template, same wording as always).

---

### Segment 7 ｜ The Project Wall: Neil's line + the directions page + the four notes + the re-topic lane (15:10–15:22 — +5 min vs. the original plan, absorbed from the buffer 10→5)

> 📌 Output anchor: none (everyone settles their topic — confirmed or changed — the precondition for everything after)

🗣️ **Say this** (screen page 08, Neil's line):

> "Second half. First, listen to someone for a minute — Neil, the founder of MIT's Fab Academy."
>
> "He says: learning to make things is not about making what you can **buy in a store** — that's not yours to make. It's about making what you **can't buy** — personalized, for yourself and the people you care about. And he keeps telling students: a project idea isn't a 'good idea' you think up — **it grows out of your own experience** — the things that annoy you, the things the people you care about put up with every day. A flashy idea copied from the internet won't survive three lessons. A problem that grew out of your experience can survive four marathons."
>
> "Fab Academy students write down their Final Project in week one — and for twenty weeks, everything they do is collecting modules for it. **That's exactly what you're doing today.**"

🗣️ **Say this** (screen page 09, the directions page):

> "What does Neil's course actually teach? Sensors, circuits, embedded systems, structural design — the same family as what's in your hands. Look at what past students built with this skill set (scan down the list): during the pandemic, a lab making protective gear; homemade oscilloscopes and microscopes; someone in the mountains pulling a 10-kilometer link out of a parabolic antenna; educational satellites, soft robots, drones, hydroponic systems, homemade instruments."
>
> "Notice: **not one of them is a flashy idea copied from the internet — every one is a real problem from the maker's own experience.** Your topic can grow from these directions too."

🗣️ **Say this** (screen page 10, the four notes):

> "So what counts as a good project? Neil's four notes. One: a masterpiece means skilled, not grand — **a finished ordinary project beats an unfinished grand vision.** Two: spiral development — every lap ends with a running version. Three: modular — cut it into small pieces, build and test each separately. Four: document as you go — the documentation grows with the project."
>
> "Sound familiar? You already know all four: Lesson 4's Pomodoro timer was built lap by lap in a spiral; your four-line log *is* documentation. Today's requirements sheet is the first line of your project's document."

🗣️ **Say this** (screen page 11, the Project Wall):

> "Everyone up — walk to the Project Wall. In Lesson 2, you pinned a sentence here: I'm making a ___ for ___ because ___. Four weeks later — you've lit up hardware, led an AI team, taught a board to recognize things. Now look at your own sentence, and I ask you: **do you still love this topic?**"
>
> "Love it: sit back down; we'll deepen it in a minute. Don't love it — or you're unsure: **you can change it. Changing today is not embarrassing. Carrying something you don't love all the way to Lesson 10 — that's the embarrassing one.** Changing rules: 5 minutes, a three-question self-check (projected: ① Do I really not love it, or am I just stuck? ② Does the new topic come from my own experience — who's it for, can I name a real person and one real time they were annoyed? ③ Can the boards in my hands actually make it?) — all three answered: change. Can't answer: stay on the original, and if you're stuck, raise your hand and a TA gets you past it. **Note rule two: you can't change to a 'flashy copied idea' — change only to a real problem from your own experience.**"
>
> "Still can't decide in 5 minutes — come to me. I have three backup topics ready; done beautifully, they're still good projects. Nothing to be ashamed of."

👀 **Students do:** re-read their sentence; confirm or take the re-topic lane; sit back down.

⚠️ **Pitfalls:**
- ⭐ **The teacher's hand itches to pick a topic for a student** (this lesson's biggest teaching accident): self-check your language — you may only ask "Who did you say it's for? When does that person hit this problem?" — never "I think you should make ___ instead." However ordinary the answer, it's the student's topic.
- Re-topic rate over 30% → don't handle it live; note it on the reflection page (the Lesson 2 → today gap needs review; feed back to the design version).
- A student's topic collapses and they're genuinely lost → give a backup topic verbally: "Take one and start building; your own idea will come while you work — the requirements sheet is allowed to change. Cross it out; don't erase it."

---

### Segment 8 ｜ The PM talk (15:22–15:34)

> 📌 Output anchor ⑤: the PM's three sentences (AI's summary contains a real name and a real scene — copied into the workbook or notebook)

🗣️ **Say this:**

> "Back to your seats — summon your product manager. John — you know this role. Today we go deep. The opener (project it), and note: **it must carry your Lesson 2 real user's name** — a need without a real name is a fake need. How does Neil's 'start from personal experience' get tested here? Watch John's first question: 'When did this last happen?' — if you can answer with a specific day, it's a real experience; if you can't, the topic is still just an idea. Old discipline: keep going in the conversation you already have — no new windows. Open a new one and every conclusion so far is gone."

```text
John, my topic is "I'm making a (what) for (a real person's name),
because (the real problem they have)."
You're my product manager. Interview me and go deep:
1. In what situation does this problem happen? When did it last happen?
2. Without this thing, how do they get by right now?
3. When and where will they use the thing I make?
When you're done asking, organize my answers into three sentences.
```

👀 **Students do:** run the PM talk; copy the three sentences down.

⚠️ **Pitfalls:**
- User written as "everyone / people" → TA A sends it back: "Say one person's name. Who was on your Lesson 2 list?"
- The chat contains none of the student's own information (AI inventing needs on its own) → the circulation red line — the citation check — send it back to fill in.
- A student actually interviewed someone (asked mom/sister over the weekend) → invite a 30-second share; set the benchmark.

---

### Segment 9 ｜ The UX talk (15:34–15:46)

> 📌 Output anchor ⑥: the usage scenario (can point to all four — who, where, how, reaction — copied into the workbook or notebook)

🗣️ **Say this:**

> "Summon the experience designer. Sally. She produces one thing: the **usage scenario** — who uses it, where, how. Watch my example (project it): 'Mom walks past the coffee table; it's been two hours since the water cup moved, so it flashes three times and gives one soft ding.' — a person, a place, an action, a reaction. Write yours in that shape."

```text
Sally, based on the previous round: (paste John's three sentences).
You're my experience designer. Write me a "usage scenario":
who uses it, where, how they use it, and how it reacts. Use a specific
person and place, no more than four sentences. Then tell me:
what does this thing look like, and where does it live?
```

👀 **Students do:** run the UX talk; copy the scenario down.

⚠️ **Pitfalls:**
- The scenario has no person and no place ("it automatically detects and reminds") → send it back: "Who? Where? Say the name."
- A student starts agonizing over colors → "Colors go on the 'later' list. Today we decide what it *does*."

---

### Segment 10 ｜ The requirements sheet (15:46–15:59)

> 📌 Output anchor ⑦: the first six rows of the requirements sheet (three sections each ≤3 lines, a real name, the usage scenario, one core feature, a "later" list of ≥1 — the hardware row stays blank until after the tour)

🗣️ **Say this** (first mention of requirements.md — point at the projected template):

> "Look at this table on screen — it's your big project's **building permit.** Its proper name is the requirements sheet — on a real job site, they call it requirements.md — and it means one thing: **before you start, write down exactly what 'it does' means.**"
>
> "Why write it? Three reasons. One: the marathon starts at Lesson 8 — every time you start work, you check it first. It **keeps you from drifting.** Two: it's alive — you can change it later, but **cross it out, don't erase it**, so everyone can see you changed your mind. Three: if you still can't say it after writing three sections, you haven't thought it through. No essays — three sections only, **three lines max each.**"
>
> "Fill it in — in your workbook or notebook. AI may help you polish the wording, but the facts must come from your two conversations just now — copy what AI invented, and you've given your project a fake birth certificate."

**Template (projected; identical to the workbook):**

```text
# My Project Requirements Sheet
Name: ______  Date: ______

## Who it helps and what problem it solves (one sentence, with a real name)

## Usage scenario (who uses it, where, how — ≤4 sentences)

## Input (what it senses, ≤3 lines)
## Logic (what it does under what condition, ≤3 lines; include one: what happens with no signal / can't recognize)
## Output (how it shows itself, ≤3 lines)

## Core feature (exactly 1)

## The "later" list (what got cut lives here, ≥1 item)
1. ______ (why it was cut: ______)

## Hardware check (fill after the tour)
Modules needed: ______ ｜ in the pool / substitute: ______ ｜ signature: ______
```

👀 **Students do:** fill the first six rows (hardware row blank — filled after the tour).

🗣️ **Say this** (after they finish — switch to page 15, "The Engineer's Requirements Sheet," ~2 minutes):

> "You just filled a requirements sheet. Now look at what a professional engineer writes before starting — Brandy, Seeed's application engineer, the one who built a voice keyboard with zero code. Before she starts, she writes an *input/output contract*: input, constraints, output, success criteria — four lines."
>
> "Compare with yours: your real user = who she makes it for; your usage scenario = her use case; your input·logic·output = her input and output; your core feature + what counts as success = her success criteria. **She calls it a contract; you call it a requirements sheet — it's the same thing. You're already using an engineer's method.** Starting next session, every new module you take on can start with those four lines."

⚠️ **Pitfalls:**
- Written as an essay → TA C runs the template ruler and sends it back: three sections, ≤3 lines each — can't fit = not thought through, go cut.
- A student has AI write the whole thing → the citation check: "The names and scenes in here — yours, or invented?"

---

### Segment 11 ｜ The Scope Killer (15:59–16:11)

> 📌 Output anchor ⑧: the cut record (the core-feature row has exactly 1 item; every "later" item carries its reason)

🗣️ **Say this:**

> "Last step — bring in the **Scope Killer.** The rules: send AI your requirements sheet, and it may ask **only one question**: 'Would it die without this?' It may not say 'this feature is bad' — **the veto is always yours.**"
>
> "Goal: the core feature row holds exactly one item. Whatever gets cut goes into the 'later' list, one line each, with the reason. **Cut things keep their names — only then has a trade-off actually happened.**"

```text
This is my requirements sheet: (paste the whole thing).
Act as the "Scope Killer": for every feature I wrote, ask me only
"Would it die without this?" — one at a time, one question each.
Don't decide for me. I make the final call on what gets cut.
Whatever gets cut, organize into a "later" list for me.
```

👀 **Students do:** walk every feature past AI; transcribe the cuts into the sheet.

⚠️ **Pitfalls:**
- Not a single cut → watch closely: it's not a perfect scope, it's an unwillingness to let go. A TA sits down and cuts one *with* them.
- Cut down to a hollow shell (even the core got cut) → rescue it: "Which function, if gone, makes it not *it* anymore? That one comes back."
- AI itself starts inflating the scope ("should I add networking?") → teaching point, say it to the whole class once: "See — AI can talk a need bigger and bigger too. **It needs managing as much as anything else.** Interrupt it: 'First ask me: would it die without this?'"

---

### Segment 12 ｜ The tour briefing (16:11–16:15)

> 📌 Output anchor: none (briefing segment)

🗣️ **Say this:**

> "Requirements sheet in hand — one last question: **can the things in your hands actually make this?** — The parts pool has the answer."
>
> "The tour is not window-shopping. Four tasks (project them): ① tick the modules your sheet needs and find the physical parts; ② not in the pool — find a substitute using the four-table sort on screen; ③ the three discovery picks — touch one module you've never seen at each table, guess what it does, check with a TA; ④ back at your seat, sign the hardware row."
>
> "Four groups rotate; 7 minutes per table; the whistle moves you."

👀 **Students do:** split into groups; the task sheet stays projected; tick and note in their own books.

---

### Segment 13 ｜ The parts-pool tour (16:15–16:45)

> 📌 Output anchor ⑨: hardware row signed (the modules are accounted for — in the pool, or a clear substitute — and the student signs)

**Tour task sheet** (kept projected; identical to the workbook; the four-table sort goes up with it):

```text
Four-table sort: Table 1 SENSE (sensors/cameras) ｜ Table 2 OUTPUT (lights/buzzers/screens)
                Table 3 ACTUATION (servos/motors) ｜ Table 4 MIXED

□ 1. Modules my sheet needs: ______ → found the real thing? (tick)
□ 2. Not in the pool: ______ → substitute: ______ (ask a TA, check the four-table sort)
□ 3. Discovery picks: touch one module you've never seen at each table, write its name + your guess
     Table 1: ______  Table 2: ______  Table 3: ______
□ 4. Back at your seat: fill the "hardware check" row and sign
```

👀 **Students do:** 4 groups × 4 tables (7 min each + 1 min rotation); complete the task sheet; sign the hardware row.

⚠️ **Pitfalls:**
- The tour turns into a general-store stroll → the task sheet is the brake: TAs ask only one question per table — "Which task are you on?"
- The module they need isn't in the pool → **the iron line: change the need, not the purchase — we don't promise purchases.** "An engineer's first lesson: solve the problem with what you have. Can't buy it? It goes on the 'later' list."
- A student wants to take a module away → make it clear: today is look, touch, and register only; **checking parts out happens at the Lesson 8 marathon start.**

---

### Segment 14 ｜ Buffer (16:45–16:50)

- **Unfinished students:** finish the remaining rows / sign the hardware row (bottom-line acceptance: three sections complete + one core feature + a signature).
- **Finished students:** the fast-lane advance — write a **mini requirements sheet** for item #1 of their "later" list (not promised to build — practice); or read a neighbor's sheet and find one module use you hadn't thought of.
- **You:** count acceptance (requirements sheets done / total); fill reflection page A and B; get the Brief Wall ready.

---

### Segment 15 ｜ The briefing ceremony + close (16:50–17:00)

> 📌 Output anchor ⑩: log finish (four-line template; "done" reads: "my big project got its brief today — it's called ___, its core feature is ___, I cut ___")

🗣️ **Say this:**

> "Everyone take a sticky note. Write two things: your project's name, and its core feature in one sentence. Line up — and stick it on the Brief Wall. Say it aloud as you stick it. (one by one, stick and say)"
>
> "The requirements sheet itself stays in your workbook — it's your building permit; every marathon work session starts by checking it. The stickies on this wall are the whole class's reference. It can change — **but cross it out, don't erase it**, so everyone can see you changed your mind."
>
> "Fab Academy graduates say that on the day their Final Project finished, they realized: it wasn't just a graduation project — it was **the start of a life project.** The sentence you wrote today is that too."
>
> "Look back at today: this morning you put your project through the wringer and made Accept-or-Reject calls. This afternoon, your topic walked off a wall and into a requirements sheet — you cut things, and you can say why. That's 'making trade-offs' — and today, you really did it."
>
> "Log, four lines as usual; 'done' reads: my big project got its brief today — it's called ___, its core feature is ___, I cut ___."
>
> "Next session preview: **the marathon's first leg.** Bring your requirements sheet: check out parts, start building, the stand-up — and AI as reviewer appears for the first time. Your project already has a home on your own computer; the brief is already on the wall — everything's ready. **Run.** Today you said 'I want to build.' Next session, you'll say 'I'm building.'"

👀 **Students do:** write the sticky, stick it on the Brief Wall, read the core feature aloud; write the log; pack up.

⚠️ **Pitfalls:**
- A student's sheet isn't finished → the sticky still goes up (a name + core feature is enough); the sheet is completed after class. The ceremony doesn't wait.
- Can't say the core feature aloud → the neighbor reads it and the student nods — no skipping; named participation is part of the ceremony.

---

## Section 4 · Live demo backup plan

| Demo | Used in | Rehearsal | Backup material | If it goes wrong live |
| --- | --- | --- | --- | --- |
| AI tester's trouble list | 14:15 | Rehearsal 1 | "what a list looks like" screenshot | show the screenshot as the model; students still run their own conversations |
| Warm-up self-check | 14:10 | spot-check 3 boards | teacher's pre-trained model on spare boards | deploy the teacher model; the dead-model case itself becomes teaching material |
| PM / UX talks | 15:22 / 15:34 | Rehearsal 2 | a sample three-sentence summary + a sample scenario | show the samples; offline → peer questioning (prompts projected, human asks human) |
| Requirements sheet | 15:46 | Rehearsal 3 | your own filled sheet as the model | handwrite on the board (no network needed) |
| Scope Killer | 15:59 | Rehearsal 2 | a sample cut dialogue | the teacher plays a human Scope Killer, whole class goes public one at a time (usually livelier) |
| Parts-pool tour | 16:15 | Rehearsal 4 (TA B) | the four-table sort projected | switch to "teacher carries modules around the room" + the task sheet still gets filled |

### 4.1 Network policy this lesson (consistent with Lesson 5's three gates, but looser)

- The only network-heavy parts are the AI trouble list (Codecraft chat) and the brief talks. **SenseCraft down ≠ this lesson downgrades.**
- **SenseCraft down:** the model is already on the board — the peer test proceeds; the "fix the data" path is disabled; the fix round uses "fix the logic" and "fix the threshold" only.
- **Codecraft down (or full outage):** the trouble list is read aloud by the teacher (3 generic items); the brief arc follows the downgrade (peer questioning + handwritten template + a human Scope Killer); the tour has no network dependence and proceeds.
- **Full outage AND Lesson 5 already triggered a downgrade** → follow the teaching-group §5.3 schedule adjustment; this lesson skips the vision half; brief + tour proceed.

---

## Section 5 · Pitfall speed sheet

Three lines first: **swap, cut to backup, ask AI.** Today's fourth: **the topic is the student's, not yours.**

| Situation | What you do |
| --- | --- |
| ⭐ Teacher/TA picks a topic for a student | language self-check — "ask, don't answer"; however ordinary the answer, it's their topic |
| Topic collapse ("I don't want to do it anymore") | the 5-minute three-question self-check; on timeout, offer a backup topic verbally (3 ready) |
| Re-topic rate > 30% | don't handle live; note on the reflection page (feed back to the design version) |
| Vision model fails everything in the new room | the #1 live teaching material ("guess what item one on the list is"); quick rescue: 10 new photos |
| Peer test turns into sabotage | harassment limited to "show it things"; wire-pullers get promoted to power-cycle tester |
| AI's trouble list too vague ("might be inaccurate") | the return prompt: specific action / environment / expected result |
| Student opens a new conversation to switch roles | stop them: "The baton dropped — go back to the conversation you already have" |
| The need keeps growing bigger | the Scope Killer is the institutional brake; when AI inflates, the student interrupts it (teaching point: AI needs managing too) |
| Requirements sheet written as an essay | the three-sections-≤3-lines hard rule; TA C's template ruler |
| Zero cuts / cut to a hollow shell | zero cuts → sit with them and cut one; hollow shell → rescue the core ("which function, if gone, makes it not *it*?") |
| Hardware won't calibrate and they won't change the need | change the need, not the purchase: "can't buy it — it goes on the 'later' list" |
| The tour becomes a stroll | the four-task sheet + one question per table: "which task are you on?" |
| Fast/slow split (a fast student done in 30 min) | fast-lane advance: write a mini requirements sheet for "later" item #1 (not promised to build) |

### Appendix: student questions and how to answer them

| Student asks | You say |
| --- | --- |
| "Can I change my topic?" | "Yes. The 5-minute three-question check: really don't love it, or just stuck? Can you name the real person the new one is for? Can the boards in your hands make it? Answer all three — change." |
| "What if I mess up the requirements sheet?" | "It's alive. Cross it out, don't erase — let everyone see you changed your mind." |
| "The module I want isn't in the pool." | "An engineer's first lesson: solve the problem with what you have. Can't buy it? It goes on the 'later' list." |
| "AI says my feature is bad — should I listen?" | "It's only allowed to ask 'would it die without this?' The veto is yours. It steps out of line — interrupt it." |
| "Why do I have to write this sheet before I build?" | "Because the marathon starts next session, and every work session checks it first. It's what keeps you from drifting — and it's what a real engineer does before starting." |

---

## Section 6 · Prompt phrase library (teacher reference)

> All of today's prompts are maintained here — every reference in the segments matches this section word for word; the student workbook carries the same text. Project the whole block so students can copy it straight into AI. **Discipline restated: the PM / UX / Scope Killer rounds all happen in the same conversation — change roles without changing windows, call the name; a new window = a dropped baton.**

### 6.1 The AI-tester's trouble list (Segment 3)

```text
Quinn, my project: a board with a camera that can recognize scissors, rock, and paper.
When it sees scissors it lights the LED; when it sees rock the buzzer beeps; when it can't
recognize anything, everything stays off.
You're a picky test engineer. Give me 5 tests for "how to make it misjudge or fail,"
each one specific: what I should do, and what I expect to see.
For example: hand gesture in backlight? Hand only half-visible? Switching gestures fast?
```

> Students replace the project description with their own. The return prompt for vague items: "Please rewrite item X as a concrete test: what action I do, in what environment, what I watch for."

### 6.2 The PM talk (Segment 8)

```text
John, my topic is "I'm making a (what) for (a real person's name),
because (the real problem they have)."
You're my product manager. Interview me and go deep:
1. In what situation does this problem happen? When did it last happen?
2. Without this thing, how do they get by right now?
3. When and where will they use the thing I make?
When you're done asking, organize my answers into three sentences.
```

### 6.3 The UX talk (Segment 9)

```text
Sally, based on the previous round: (paste John's three sentences).
You're my experience designer. Write me a "usage scenario":
who uses it, where, how they use it, and how it reacts. Use a specific
person and place, no more than four sentences. Then tell me:
what does this thing look like, and where does it live?
```

### 6.4 The Scope Killer (Segment 11)

```text
This is my requirements sheet: (paste the whole thing).
Act as the "Scope Killer": for every feature I wrote, ask me only
"Would it die without this?" — one at a time, one question each.
Don't decide for me. I make the final call on what gets cut.
Whatever gets cut, organize into a "later" list for me.
```

### 6.5 The requirements-sheet template (Segment 10 — identical to the workbook)

```text
# My Project Requirements Sheet
Name: ______  Date: ______

## Who it helps and what problem it solves (one sentence, with a real name)

## Usage scenario (who uses it, where, how — ≤4 sentences)

## Input (what it senses, ≤3 lines)
## Logic (what it does under what condition, ≤3 lines; include one: what happens with no signal / can't recognize)
## Output (how it shows itself, ≤3 lines)

## Core feature (exactly 1)

## The "later" list (what got cut lives here, ≥1 item)
1. ______ (why it was cut: ______)

## Hardware check (fill after the tour)
Modules needed: ______ ｜ in the pool / substitute: ______ ｜ signature: ______
```

### 6.6 The tour task sheet (Segment 13 — identical to the workbook)

```text
Four-table sort: Table 1 SENSE (sensors/cameras) ｜ Table 2 OUTPUT (lights/buzzers/screens)
                Table 3 ACTUATION (servos/motors) ｜ Table 4 MIXED

□ 1. Modules my sheet needs: ______ → found the real thing? (tick)
□ 2. Not in the pool: ______ → substitute: ______ (ask a TA, check the four-table sort)
□ 3. Discovery picks: touch one module you've never seen at each table, write its name + your guess
     Table 1: ______  Table 2: ______  Table 3: ______
□ 4. Back at your seat: fill the "hardware check" row and sign
```

---

## Section 7 · Localization slots

| Where | Original | Swap-in suggestion |
| --- | --- | --- |
| The 3 backup topics | drink reminder / posture checker / pet-feeding timer | your students' real high-frequency scenes: piano-practice timer, grandparent med reminder, forgotten-backpack check — collect from the homeroom teacher before class |
| The usage-scenario example | "Mom walks past the coffee table; the cup hasn't moved in two hours…" | a local home scene (grandma / little brother / the desk / the hallway) — a person and a place is all it needs |
| The discovery-pick modules | regular Grove 40-in-1 modules | any signature module your institution has; keep the "touch one you've never seen + guess + verify" structure |
| Trouble-list examples | backlight / half a hand / fast switching | your classroom's real conditions (window backlight, noisy hallways, messy desks) |
| Neil's directions page | protective gear, oscilloscopes, parabolic antenna, satellites, soft robots… | any local maker/fab-lab alumni builds you can name — the point is "every one grew out of the maker's own experience" |

---

## Section 8 · Teacher reflection page

Take 10 minutes after class. Anything counts — even one line.

1. Which trouble-list item had the most teaching value? Quote it: ______
2. Acceptance numbers: peer tests completed ___/___; requirements sheets complete (three sections + one core feature + ≥1 later item) ___/___; hardware rows signed ___/___.
3. Re-topic count: ___ people (>30% → feed back to the design version). Ask 3 students "what did you cut, and why?" — how many answered?
4. Did any "teacher picks a topic for a student" moment happen in the brief arc? How did you handle it?
5. Which block overran, which came up short? Did the peer test's 20 minutes survive?
6. Did any 🗣️ line sound awkward out loud? Cross it out; write what you actually said.
7. Keep this session next time: ______；change: ______
8. Best student one-liner (the "vicious misread + my counter" shares) — collect for the showcase.

Photograph the page and send it to the teaching group, or tuck it back in the course folder. **Every line you write becomes a pitfall another teacher won't hit in the next edition.**

---

_Version: EN v1 ｜ 2026-08-25 ｜ Source: CN 讲师版 v4（2026-08-06；文件名标注 v2，修订说明含 v4：PPT 18→19 页、Brandy 契约对照页 15、Final Project 口径清理） ｜ 上游信源：CFG-5 配置说明书 v1.0（第 6 次课行 + Final Project 立项节点）；积木卡 C2 / X3 / X6 / X9；备料池巡礼依据积木池 v1_

_Localization notes: BMAD 5-personas (John/Sally/Quinn) and Neil/Fab Academy/Brandy kept in original; '为我的作品立项' -> Brief Your Project; '需求单' -> the requirements sheet / requirements.md (the building permit); '范围杀手' -> the Scope Killer (sole phrasing: 'Would it die without this?', veto power belongs to student); '刁难清单' -> the trouble list; '改数据/改逻辑/改阈值' -> fix the data / fix the logic / fix the threshold; '接受声明' -> the acceptance note; '换题通道' -> the re-topic lane; '保底题' -> the backup topics; '立项墙/立项仪式' -> the Brief Wall / the briefing ceremony; '查引用' -> the citation check; '改需求不改采购' -> change the need, not the purchase; '开眼界三选' -> the three discovery picks. This lesson's iron law: 'The topic is the student's, not yours.' Neil's creativity phrasing and Brandy's contract comparison page fully preserved. 'No gambling on Chinese rendering' rule naturally satisfied._
