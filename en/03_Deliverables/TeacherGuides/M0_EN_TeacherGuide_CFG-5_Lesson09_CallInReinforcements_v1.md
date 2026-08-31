# Teacher's Guide ｜ Lesson 9 · Call In Reinforcements

_Give Your MVP a New Power · The Marathon's Second Leg ｜ Chaihuo Maker Academy · M0 Hardware Foundation · Smart Hardware Fundamentals ｜ 10-session term ｜ 3 hours (no scheduled break)_

> **Source:** 中文版 v2（M0_教师课件_CFG-5_第9课_给作品请外援_v2.md，文件名即 v2；文末修订说明含 v2 滚动修订：三幕节奏、全套去钟面时刻、删统一休息、零打印、MVP 口径、评审人设递进、站会弹性化沿用第 8 课）
> **Localized edition** — same blocks, same minutes, same teaching intent; classroom language rewritten for an English-speaking teacher to pick up and teach from.
> **Localization notes:** ① 反馈页时长按总览表统一为 98/45/37（中文版反馈页遗留 v1 的 85/55/40，此处以总览表与分段流程为准，已在 Section 8 注明）；② 全课零打印——三看口径、全部句式、交接单、评审记录全部投屏，学员写进学员文档；③ 评审人设递进保留：第一棒挑剔用户 3 刺为主 → 本棒 Quinn 结实度 5 条逐条实测为主、挑剔用户降为 1 刺。

---

## The one-sentence brief

Today is **leg two of the marathon — your MVP grows a new power.** The first half is a trip to **the hardware store**: students learn what **a library** is (someone else's well-tested, free toolbox), run one **class-wide install** end to end (search → **the three checks** → install → run the example → **the lightning moment**), learn **the tool room** idea, make **the import decision** (a trade-off decision, not a default move — **pick exactly one library**, or write a reasoned **"why not import" note**), **wire it in** (AI as translator turns sample code into their own core function), and finish with **the looks upgrade** — the second kind of help, four moves (**shell / still / label / hide**) so the MVP finally *looks like something*. The second half is the leg-two sprint: **finish the core function** against the requirements sheet, last 10 minutes the **quick shell**. The last act is review & handoff: **Quinn's sturdiness checklist** (5 points, tested one by one — no more picking two) plus the **Picky User** down to a single most-lethal fault, then Accept-or-Reject decisions and the **leg-two baton handoff sheet**.

**The whole lesson runs in three acts** (the rhythm skeleton — keep this map in your head all day):

| Act | Blocks | Total |
| --- | --- | --- |
| **Act 1 · The hardware store** | Opening (why libraries) → class-wide install → the tool room → the import decision → wire it in → share & close → the looks upgrade | 98 min |
| **Act 2 · Leg-two sprint** | Leg-two stand-up → build: finish the core function (last 10 min: the quick shell) | 45 min |
| **Act 3 · Review & handoff** | AI review (sturdiness) → decide & execute → baton handoff sheet → the capstone close | 37 min |

Each act boundary has one explicit **gear-change move**: Act 1→2 is "stand-up, go"; Act 2→3 is "hands off — review time" — the same rhythm as leg one, and leg three (Lesson 10) will run it once more.

**When they leave, students can** (four things):

1. Say what a library is and when to call in help — **importing is a trade-off decision, not a default move**;
2. Judge a library with **the three checks** (last update / examples / documentation) and get **≥1 library** running in their own project — or write a reasoned "why not import" note;
3. Use AI as **a translator** to read example code that wasn't written for them and reshape it into their own feature;
4. Give the MVP a first look with stuff from around the house — **shell / hold still / label / hide the mess** — under the rule **looks serve the demo**.

**Not yet, don't worry** (four things):

1. Writing your own library — today you call in help; you don't reinvent the wheel;
2. Solving version conflicts and other ecosystem errors — that's the teacher's job (that's exactly why today needs a **T3** teacher);
3. Getting every feature done — "done" means the **core function on your requirements sheet**, not everything imaginable;
4. A polished, product-grade shell — today is "looks like something" (a 20-minute quick shell); 3D printing and structural design are for later courses.

**When things go wrong:** swap (hardware) → cut to backup (tool / account / network) → ask AI (knowledge).

**Today's three iron laws:**
1. **The one-library rule** — greed is today's most common failure; three picks gets sent back to re-pick;
2. **Not importing is just as valid** — the review looks at your reasoning, not the result;
3. **The AI review can never be squeezed out by progress pressure** — the marathon's institutional floor; in force for leg two exactly as it was for leg one.

---

## 🎯 Learning Objectives

*By the end of this session, students will be able to…*

1. **Explain** what a library is and when to call one in, and judge any candidate library with the three checks before installing (*Bloom: Understand*).
2. **Apply** the import decision: pick exactly one library (or write a "why not import" note) and get it installed with its example running in their own project (*Bloom: Apply*).
3. **Apply** AI as translator to reshape sample code — code not written for them — into their own core function, one minimal change at a time (*Bloom: Apply*).
4. **Apply** the four moves to give the MVP a first look — shell / still / label / hide — under the discipline that looks serve the demo (*Bloom: Apply*).

---

## Page One — read this before class starts

### What today produces (four student outputs)

1. **One library decision** — ≥1 library installed and running in the project, **or** a written "why not import" note (both score equally);
2. **One wired-in feature** — sample code reshaped into the core function (minimum bar: installed + example runs);
3. **A first look** — the MVP got at least one of the four moves (shell / still / label / hide);
4. **One leg-two baton handoff sheet + review record** — the sturdiness checklist, **all 5 points tested**, + 1 Picky User fault, each judged with a reason.

### Three things you need to do

1. **Follow the clock.** Work down the timeline; every block says how many minutes and what to do. Shift gears on time — the gear-change *is* the lesson, same rhythm as leg one.
2. **Read the lines.** Every 🗣️ line is pre-written classroom speech — read it as-is, don't improvise. All prompts are in Section 6 — project them.
3. **Run the triage board.** The whiteboard's three columns (**won't install / example won't run / logic's a mess**) are today's core organ — TA A owns them; every stuck student gets sorted, not soothed.

### Three things you do NOT need to do

1. **You don't debug installs.** Version conflicts, mirrors, dependencies — that's the T3 lane. Over 10 minutes on one install → swap to the runner-up candidate library. (No T3 today → run the downgrade clause, 4.3. Don't force it.)
2. **You don't explain sample code for students.** The translator prompt does that — "what is this code doing?" is a student-to-AI line. The library notes (annotated example) are the fast-lane treat, not your job to produce.
3. **You don't make the import call for students.** Picking one library (or none) is their trade-off decision. Three picks gets sent back; "no library fits" is a valid answer with a written reason.

### When things go wrong

- **Install error (the high-frequency segment):** the standard move — student pastes the error verbatim to AI: "I tried to install this library and got this error. What does it mean? What do I do?"; AI can't → teacher; still stuck past 10 minutes → swap to the runner-up candidate.
- **Network slow:** mirrors are pre-configured (checklist, 1.1); still slow → the offline-package USB.
- **No T3 teacher:** today changes course — Act 1 becomes a double build round + a 15-minute projector demo of the library idea; the capstone close becomes a leg-two completion summary (see 4.3). **Never let a T1/T2 teacher gamble on the install ecosystem.**
- **You're stumped:** smile, and say *"Let's ask AI together."*
- One-liner: **swap, cut to backup, ask AI.**

---

## Section 1 · Before class

### 1.1 A week out (T-7)

- [ ] ⭐ **Confirm today's teacher is T3** — library-ecosystem issues (version conflicts / mirrors / dependencies) exceed what a script can cover. **No T3 → run the downgrade clause (4.3), don't force it.**
- [ ] **Mirror configuration:** set up on every lab machine in advance (instructions in the institutional knowledge base) — test one install per machine.
- [ ] T-1 stocking: **pre-download 3–5 common libraries' offline packages to a USB** (OLED graphics library, common sensor libraries — pick by the Lesson-7 requirements-sheet survey of project directions).
- [ ] Survey requirements-sheet directions; rehearse 2–3 "rank the candidates" dialogs (predict what AI will recommend; install each yourself first).
- [ ] Confirm the student:TA ratio ≤ 6:1; every machine opens aily-blockly normally (Lesson-8 paired catch-up students confirmed caught up).

### 1.2 Same day (arrive 1 hour early)

- [ ] Boot test: aily opens → open your own project → install one library (verifies the mirror works).
- [ ] External-network test (installs need the internet); offline USB within reach.
- [ ] Main kits + per-project components (the 40-in-1 pool by the requirements-sheet hardware column; continue Lesson-8's white-sheet check-out per table).
- [ ] Projector ready: the class-wide install demo project, including the "complex sensor without a library" hundred-line code vs. "with a library" three-line call comparison.
- [ ] Whiteboard in three columns: **won't install / example won't run / logic's a mess** (the triage board).
- [ ] Brief Wall + baton handoff sheets in place (the stand-up needs them). **Zero printing today** — the three checks, every prompt, the handoff sheet, the review record: all projected; students write them into their student documents.

### 1.3 Teacher rehearsal (run it once before class)

1. Walk the full class-wide install once: search → three checks on the page → install → run the example; time it (in class, budget ×2 for guided installs);
2. Run one "rank the candidates" dialog (6.2); check the AI's recommended libraries actually exist and support your boards;
3. Rehearse one "install error → paste error to AI → solved" chain end to end; screenshot it as class material;
4. Rehearse the **lightning moment**: find the pause where the example compiles and runs — that's where you stop the class;
5. In a fresh chat window, re-check Quinn's entrance condition (6.6): students review with Quinn again this leg — windows that already got the team background line in Lesson 8 send the prompt directly; new windows send the background line first.

### 1.4 Materials

**📦 The institution has:** computers (aily installed); main kits + per-project components; the 40-in-1 parts pool; cables; the roving tablet; projector; whiteboard + markers; the Brief Wall; baton handoff sheets (leg 1, students bring); hourglass / timer; the offline USB; **the looks-up materials pool: clean cardboard boxes / takeout boxes, tape, markers, rubber bands / zip ties, scissors & craft knives (knives teacher-held, dispensed on demand)**.

**🛒 To buy: none.** (The offline USB carries over from Lesson 8; hot-part gaps run the "queue + substitute" line — no purchase promises.) **No looks materials bought either** — three days before, the class group asks students to bring clean junk from home (boxes, bottle caps, old toy shells). Trash is the hardware store for looks.

**🖨️ Printing: none.** Zero-print lesson — everything on screen; the check-out record is one white sheet per table (TA draws the columns before class); the library notes live in a whiteboard corner (fast-lane output, spoken or on screen, never printed).

---

## Section 2 · Session map

| Act | Time | Block | What's happening |
| --- | --- | --- | --- |
| **Act 1 · The hardware store** | 10 min | Opening + why libraries | 30-second recap + the hundred-lines-vs-three comparison |
| | 15 min | Class-wide install | search → three checks → install → run the example (the lightning moment) |
| | 8 min | The tool room | every project has its own tool room; they don't fight |
| | 15 min | The import decision | two real cases × the three questions → rank the candidates → pick exactly one (today's teaching anchor) |
| | 25 min | Wire it in | install the pick → run the example → read it → reshape it into your own feature |
| | 5 min | Share & close | "what I imported, what it saved me" / "why I didn't" |
| | 20 min | The looks upgrade | help isn't only code — the four moves (shell / still / label / hide) |
| **Act 2 · Leg-two sprint** | 5 min | Leg-two stand-up | read the baton sheet → one-sentence goal (against the core function) |
| | 40 min | Build: finish the core + the quick shell | finish the core; last 10 minutes the quick shell |
| **Act 3 · Review & handoff** | 15 min | AI review (sturdiness) | Quinn's 5-point sturdiness checklist, every one tested + the Picky User's 1 fault |
| | 12 min | Decide & execute + handoff | accept/reject one by one; fill the leg-two baton sheet + log |
| | 10 min | The capstone close | the nine-lesson journey recap + the capstone line + Lesson-10 preview |

> **No clock times in this table** — start whenever you start; run by minutes. Build blocks get whole, unbroken time; the room only hears relative nodes ("15 minutes before review"), never clock readings. **No scheduled break:** students use the restroom during build as they please; devices stay on; AI chat windows stay open.
>
> Act 1 98 + Act 2 45 + Act 3 37 = 180 min, aligned with the configuration spec's Lesson-9 row ("90+75" after dropping the scheduled break).

### 2.1 The time elastic band

- **Most compressible:** share & close (5→3 min); the tool room (8→5 min); the looks upgrade (20→12 min — keep the four moves projected, cut the live demo). The slack all lands before the build.
- **Next compressible:** class-wide install (15→12 min — close the moment the example runs); the build sprint (40→35 min — keep the core function).
- **Never cut:** **the AI review's 15 minutes (the institutional floor)**; the import decision (today's teaching anchor); the capstone close; the 30-second recap.
- **If wire-it-in collapses:** the bar drops to "installed + example runs"; the wiring moves into the build block.

### 2.2 TA split (the triage board is today's core organ)

- **TA A (the triage officer):** roams with the board, sorting every stuck student — **won't install** (mirror / version) → teacher; **example won't run** (board fit) → teacher; **logic's a mess after wiring it in** (an AI-dialog problem) → TA A handles it: guide "one step at a time," cut the reshape request small, **never hand over code**.
- **TA B (parts & hardware officer):** the check-out record (white sheet per table); wiring cases; the hot-parts queue.
- **TA C (rhythm & record officer):** guards the review's no-squeeze red line; takes "hand close-ups" (hands only, never faces); collects the **library notes** (fast-lane output, whiteboard corner); watches for the three-picks send-back.

---

## Section 3 · Segment-by-segment script

### Segment 1 ｜ Opening + why libraries (10 min) 【Act 1 · The hardware store】

🗣️ **Say this:**

> "30-second recap: last session you ran the first lap — your project has an MVP. It can be demonstrated, two judges picked at it, and you made Accept-or-Reject calls. Did you bring your baton handoff sheet? Put it on the desk — we read it at the opening of the build."
>
> *(switch to the comparison demo)* "Look at this complex sensor. No help from anyone — ask AI to write the driver from scratch — *(scroll three screens)* over a hundred lines. Three screens of scrolling. Can you read it? By now, yes, you can read it — **but being able to read it doesn't mean you should write it.** *(switch to the library version)* Now: three lines. That hundred-line thing was already written, tested, and given away free — that's **open source**: engineers all over the world send each other toolboxes. This toolbox is called **a library**."
>
> "Today you learn to shop **the hardware store**: whatever your project needs, someone on earth has probably already built the wheel. First half: call in the help. Second half: finish your core function — let your MVP grow a new power."

👀 **Students do:** watch the comparison; baton handoff sheet on the desk.

⚠️ **Pitfalls:**
- "If it's free, why does anyone write code at all?" → one line of open-source culture and stop: "Because people send you theirs too. Chaihuo grew out of exactly this kind of giving." Don't turn it into a lecture.
- A student missed Lesson 8 (no baton sheet, no MVP) → the comeback flow: TA A spends 5 minutes helping them rebuild a mini handoff sheet from the Lesson-8 student document (a shrunk backup-topic first version counts); they join the rotation normally.
- A student missed Lesson 6 (no aily installed) → those who arrived early get TA-installed (Lesson-6 USB); anyone else pairs up after the opening, same comeback flow as Lesson 6.

📌 **Output anchor:** baton handoff sheet on the desk, ready to read.

---

### Segment 2 ｜ Class-wide install (15 min) 【Act 1 · The hardware store】

🗣️ **Say this:**

> "Let's call in the same reinforcement together and walk the whole process once. Step one, search — find it in the hardware store. Step two, **read the page and judge it: the three checks** *(projected)*: ① when was it last updated? (nothing in three years — think twice); ② does it have examples? (no examples = no manual); ③ is it documented completely? **Two of three pass — bring it in.**"
>
> "Step three, install — that's taking the toolbox into **your project's tool room**. Step four, run its built-in example."
>
> *(the example compiles and runs — fast)* "…stop. How many seconds did that compile take? *(wait for the shout)* Right — **the reinforcement you called in is already compiled. That's the second reason to call in help.**"

👀 **Students do:** install along → three checks → install → example runs.

⚠️ **Pitfalls:**
- ⭐ **Install errors (the high-frequency segment):** the standard move — paste the error verbatim to AI: "I tried to install this library and got this error. What does it mean? What do I do?"; AI can't solve it → teacher (version / mirror). Teacher past 10 minutes → swap to the runner-up candidate (this is exactly when candidate #2 earns its keep).
- Network slow → mirrors pre-configured; still slow → hand out the offline USB.

📌 **Output anchor:** one library installed class-wide; the example runs (the lightning moment marked).

---

### Segment 3 ｜ The tool room (8 min) 【Act 1 · The hardware store】

🗣️ **Say this** *(open two projects' dependency folders side by side on the projector)*:

> "See this — this project's tool room, and that project's tool room: **two separate rooms.** Why design it this way? One sentence: **one room on fire doesn't burn the next one.** The library your tomato clock called in and the library your project called in each live in their own room — they don't fight."
>
> "Write the three checks into your student document *(point at the projection)* — anywhere you ever see 'should I install this library?', run the three checks first."

👀 **Students do:** find their own project's tool room; write the three checks into the student document.

⚠️ **Pitfalls:**
- A student digs into package-management theory → one line back: "That's a whole university course. Today, remember 'each in its own room'." (Term gate: no new concepts beyond "dependency management.")

📌 **Output anchor:** the three checks in the student document.

---

### Segment 4 ｜ The import decision (15 min — today's teaching anchor) 【Act 1 · The hardware store】

🗣️ **Say this:**

> "The hardware store is fun to browse — but **importing is a trade-off decision, not a default move.** Two real cases *(projected)*:"
>
> "Case one: your project drives a complex sensor; writing the driver yourself is a hundred lines — **import it.** Case two: you want a light to blink three times; three lines does it — and you go hunting for a 'blink library' — **don't.** What's the difference? Three questions: **Is it core? Can we get it working today? What happens if we don't import it?**"
>
> "Now, against your requirements sheet, let AI be your **selection advisor** *(project the prompt)* — it lists candidates; **you pick exactly one**, and that's the one we install today. Three picks gets sent back — greed is today's most common failure."

The projected prompt is 6.2.

👀 **Students do:** run the rank-the-candidates dialog → pick exactly one (run the three questions); if no good library exists, write the "why not import" note (why you don't need one).

⚠️ **Pitfalls:**
- The whole room wants the flashy library (light effects / music) → the one-library rule + check against the requirements sheet; genuinely want to play → it goes on the "later" list.
- No suitable library → the **no-import route is a valid trade-off**: a written "why not import" note in the student document counts as the day's output; the teacher publicly affirms this route once (so it never feels second-class).
- AI recommends a library that doesn't exist (it invents) → the teaching point: "Search whether it's real — **AI will confidently invent libraries. The hardware store only stocks real ones.**"

📌 **Output anchor:** one library picked — or the "why not import" note written.

---

### Segment 5 ｜ Wire it in (25 min) 【Act 1 · The hardware store】

🗣️ **Say this:**

> "The last step is the hardest: **example code is not your feature.** The example demonstrates what the library can do; what you want is your core function. Two steps: one, ask AI **'what is this code doing?'** — it's your translator, built for code that wasn't written for you; two, have AI **reshape** it to your need *(project prompt 6.3)*."
>
> "The bar: installed + example runs. If you don't finish the wiring, it moves into the build block this afternoon — that's fine."

👀 **Students do:** install the pick → run the example → read it → make the minimal change.

⚠️ **Pitfalls:**
- The example doesn't match your board → teach **the fourth check** live: "Is your board on the supported-hardware list?" — the flip becomes the teaching point; if it really doesn't match, back to Segment 4 for the runner-up candidate.
- Fast/slow split (today's widest natural gap) → fast students: write an annotated-example explainer — **the library notes** (whiteboard corner, credited to the author, a gift to the whole class); slow students: hold the bar.

📌 **Output anchor:** ≥1 library running in the project (or the bar: installed + example runs).

---

### Segment 6 ｜ Share & close (5 min) 【Act 1 · The hardware store】

🗣️ **Say this:**

> "One line each: **what I imported, and what it saved me.** No-import students report: **why I didn't** — and they get the same applause."
>
> "The code reinforcement is in the door. But help isn't only one kind — your project is still wearing nothing. Next twenty minutes: the second reinforcement — **a look.**"

*(Large class: desk-pairs report to each other; you call 3–4 to the whole room — and always call at least one no-import student.)*

📌 **Output anchor:** one line per student (import or why-not), heard by the room.

---

### Segment 7 ｜ The looks upgrade: make it look like something (20 min — today's second anchor) 【Act 1 · The hardware store】

🗣️ **Say this:**

> "Help isn't only code. Look at your project — the function runs, but it's still a table of loose parts and a nest of wires. **An MVP has two faces: it works (the inside), and it looks like something (the outside).** On demo day, people see the outside first — then they get to the inside."
>
> "The look costs nothing and gets printed nothing — **trash is the hardware store for looks.** Four moves *(projected)*: one, **give it a shell** — a cardboard box, a takeout box, an old toy shell; it is what it is, so make it look like what it is. Two, **hold it still** — tape, rubber bands, zip ties; wires don't dangle, demos don't wobble. Three, **label it** — marker the button names, tape an arrow; someone can touch it without reading a manual. Four, **hide the mess** — tuck the wiring into the box; only the 'face' shows."
>
> "One rule: **looks serve the demo** — it exists for a 30-second demonstration. Looks take no more than a third of your build time; if you disappear into it, I'll pull you back. Scissors and knives live with me — take them on demand, return them when done."

👀 **Students do:** 1 minute of "what could my project look like"; pick a shell from your brought-from-home junk and the public pool (pick, don't buy); write the four moves into the student document.

⚠️ **Pitfalls:**
- A student disappears into the looks (half an hour of scissor work) → pull back: "Function first — the last 10 minutes are the quick shell. Go write code now."
- No materials brought / the pool is picked clean → three substitutes: can the box on your requirements sheet be the shell directly? / two cardboards taped together? / no shell at all — tidying the wires: does that count? *(Yes, it counts.)*
- "Can I 3D-print it? Laser-cut it?" → one line: "That's product-shell work — there's a course for it later. Today is a 20-minute quick shell; the target is *looks like something*."

📌 **Output anchor:** the four moves in the student document; a shell picked (or a deliberate "no shell yet").

---

### Segment 8 ｜ Leg-two stand-up (5 min) 【Act 2 · Leg-two sprint】

**Two ways to run it, as leg one** (small room: everyone stands and says one line; big room: pairs say it to each other + write the sentence at the top of the requirements sheet + you call 3–4).

🗣️ **Say this:**

> "Stand-up. First read your baton sheet — what did last leg say is the first thing this leg? Then one sentence: **'Today I'll get the core function to ___.'**"
>
> "Definition check: **'done' is not everything you can imagine — it's the core function on your requirements sheet.** Say it against the sheet; anything beyond it gets pulled back. You may add half a sentence: '…and give it a (shell/label)' — no fit, skip it. **Looks are optional; function is the required question.**"

👀 **Students do:** read the handoff sheet → one verifiable one-line goal.

⚠️ **Pitfalls:**
- The goal comes out as "finish everything" → pull back to the sheet: "Which line is your core function? Today, that line."
- Handoff sheet lost → it's posted on the Brief Wall — re-read it on the spot and copy it back.

📌 **Output anchor:** one verifiable one-line goal per student.

---

### Segment 9 ｜ Build: finish the core + the quick shell (40 min) 【Act 2 · Leg-two sprint】

🗣️ **Say this:**

> "Go. Rules as leg one *(point at the projected three rules)*: check against your requirements sheet; **15 minutes no progress = raise your hand**; code questions go to AI first. One thing new today: aily unsure? Flip your two-views cheat sheet — it was written for today."
>
> "**The last 10 minutes are the quick shell**: once the function runs, *then* the scissors — shell, still, label, hide; land as many of the four as you can. Not getting one in is no shame — function is always the required question."
>
> "**15 minutes before review**, table by table: get ready with two lines — 'right now it can ___; it still can't ___.' Review starts on time — nobody squeezes it out."

**Your circulation rhythm:** same as Lesson 8 — one lap per 15 minutes, three looks per lap (screen / requirements sheet / face); intervention red lines as before (**direction only, no writing code, no making decisions**); triage runs through the whiteboard's three columns.

⚠️ **Pitfalls:**
- aily still rusty → the cheat sheet is the warm bridge (already on the desk); still stuck → TA 30-second pointer, no doing it for them.
- Project crash → the crash protocol (the 15-minute shrink plan); this leg's crash line adds: "**Next leg is the sprint leg — cut smaller today, and Lesson 10 gets steadier.**"
- Fast-finishers → the fast-lane ladder + the library notes.

📌 **Output anchor:** core function done (or shrunk to a verifiable slice); the quick shell begun.

---

### Segment 10 ｜ AI review: sturdiness (15 min — never squeezed) 【Act 3 · Review & handoff】

🗣️ **Say this:**

> "Hands off. Review time — last leg's reviewer asked 'does it look right?'; **this leg's reviewer checks 'how sturdy is it?'** The lead is old friend Quinn: **a 5-point sturdiness checklist, tested one by one** (this leg upgrades: no more picking two — all five). The Picky User drops to a single most-lethal fault. Prompts up *(project them)*, same old rules: **feed the real current state, no bragging; and keep going in the same chat window — don't open a new one.**"

Prompts: 6.4 (Quinn's sturdiness checklist), 6.5 (the Picky User, one fault); Quinn's entrance condition at 6.6.

👀 **Students do:** the two-part review → test all five sturdiness checks for real → record in the student document.

⚠️ **Pitfalls:**
- AI starts praising → the push-back prompt (projected): "No praise. Faults only."
- All five pass → "Congratulations, it's sturdy — have your desk-mate try it the barbarian way."
- Network down → human review (desk-mate as tester, same framework) — **the review can't be canceled, only its executor changes.**

📌 **Output anchor:** 5 sturdiness checks tested + 1 Picky fault, all recorded with results.

---

### Segment 11 ｜ Decide & execute + the leg-two baton handoff sheet (12 min) 【Act 3 · Review & handoff】

🗣️ **Say this:**

> "One by one: **accept or reject — and both need a reason.** Heads-up: **next leg is the sprint leg — fix-only, no adding.** Anything you can't finish today, think hard before you write it as 'first thing next leg': that's your last chance to fix it."
>
> "Fill the leg-two baton handoff sheet *(template projected, 6.7 — into the student document)*. Log, four lines as usual — 'did' reads: I called in ___ and it saved me ___; the look used ___ (materials); sturdiness passed ___ checks."

👀 **Students do:** decide + reason → fix what's fixable right now → handoff sheet into the student document → log.

📌 **Output anchor:** the leg-two baton handoff sheet + the four-line log.

---

### Segment 12 ｜ The capstone close (10 min) 【Act 3 · Review & handoff】

🗣️ **Say this** *(the ritual carries weight — pause one minute):*

> *(project the nine-lesson journey, point at it line by line)* "Lesson one, you lit your first lamp; two, you found a question worth doing; three, your project grew a screen; four, you got an AI team; five, you taught hardware to see; six, you moved your project home; seven, you briefed it; eight, you ran the first lap; today, you called in reinforcements — code help and look help — **from daring, to reading, to calling in help.** Your project's function has capped out, and it has a face for the first time. *(Pause one second — look at it.)* This is what nine lessons look like."
>
> "Next lesson: **the last leg + the roadshow.** Sprint discipline in four words: **fix-only, no adding.** Bring your baton sheet, your project, and the side of it you most want to show."

👀 **Students do:** pack up; return modules not in use (main kit to its box; the Brief Wall sticky notes stay); log closed.

📌 **Output anchor:** the nine-lesson journey seen; the log closed.

---

## Section 4 · The double-insurance matrix

| Block | Time short (compress) | Goes wrong live (substitute) | Can't happen at all (fallback) |
| --- | --- | --- | --- |
| Class-wide install | 15→12 min | hand out the offline USB | projector demo from the teacher machine + install after class |
| The import decision | 15→12 min | runner-up candidate goes straight in | run the no-import route (still reviewed normally) |
| Wire it in | hold "installed + example runs" | wiring moves into the build block | the bar is the acceptance |
| The looks upgrade | 20→12 min (keep the four moves projected) | fold into the build's last 10 minutes, teach as you go | cut it; send the four-moves image to the class group for after class |
| Build sprint | 40→35 min (the quick shell can give way entirely) | lower the target, keep the core function | the crash protocol (15-minute shrink) |
| AI review | **never cut (institutional floor)** | offline → human peer review | the desk-mate barbarian test |
| The capstone close | don't cut (even 1 minute is a ritual) | — | — |

### 4.3 The downgrade clause (the brick-card downgrade)

- **No T3 teacher:** today reroutes — Act 1 becomes **a double build round + a 15-minute projector demo of the library idea** (teacher machine); the capstone close becomes a leg-two completion summary (per the configuration spec's variant). **Don't force it; never let a T1/T2 teacher gamble on the install ecosystem.**
- **Network down:** mirrors and the offline USB only cure slowness, not a dead connection — the import block moves out of today; the lesson becomes the double build round (review runs as usual); imports happen before next lesson, teacher-installed.

---

## Section 5 · Pitfall speed sheet

Three lines first: **swap, cut to backup, ask AI.** Today's fourth: **the review is never squeezed.**

| Situation | What you do |
| --- | --- |
| ⭐ Install network slow / timeout | mirrors pre-configured (checklist); still failing → the offline USB |
| Version conflict / dependency error | T3 teacher on-site; past 10 minutes → swap to the runner-up candidate |
| Library example doesn't match the board | teach the fourth check live (supported-hardware list) → flip becomes the teaching point → swap candidate |
| AI recommends a library that doesn't exist | the teaching point: "Search whether it's real — AI invents; the hardware store doesn't." |
| Three picks (greed) | send back to re-pick; only one allowed |
| Everyone wants the flashy library | check against the requirements sheet; wants go on the "later" list |
| No student needs a library at all (rare) | the whole class installs the OLED graphics library to "add a face to your project"; the trade-off lesson becomes a group discussion |
| Extreme fast/slow split | fast: library notes (annotated example, whiteboard corner); slow: hold "installed + example runs" |
| aily still rusty | two-views cheat sheet on the desk; TA 30-second pointer, no doing it for them |
| Hooked on looks, squeezing function time | pull back: "function first"; looks ≤ 1/3 of build time; the quick shell only in the last 10 minutes |
| No looks materials / pool picked clean | trash is the hardware store: the requirements-sheet box directly / two cardboards taped / tidying the wires counts |
| Scissors / craft-knife injury risk | knives teacher-held, dispensed on demand; cutting actions done by teacher or TA |
| "Done" definition dispute | always pull back to the requirements-sheet core function |
| ⭐ Review squeezed by progress pressure | not an option — remind table by table at 15 minutes to review; the review opens on time; one squeeze = a major backfill event |
| New chat window for the review | the discipline: "Keep going in the window you have — the review has to catch your trade-off history too"; Quinn's condition at 6.6 |

### Appendix: student questions and how to answer them

| Student asks | You say |
| --- | --- |
| "What is a library?" | "A toolbox someone else wrote, tested, and gives away free. Whatever you need, someone on earth has probably already built the wheel." |
| "If I import a library, is it still mine?" | "Of course. A chef doesn't grow their own vegetables — but you ordered the dish, you mind the heat, you made the calls." |
| "AI says this library is great, but I can't find it?" | "It invents things. What's searchable in the hardware store is what counts." |
| "I don't need any library — am I behind?" | "Not importing is a valid trade-off. Write your reason clearly — it scores the same as importing." |
| "My project is so ugly." | "First ask: in a 30-second demo, can someone tell what it is? If yes, that's enough — *looks like something* isn't 'beautiful'; it's 'you can tell at a glance, and you'd dare to touch it.'" |

---

## Section 6 · Prompt phrase library (teacher reference)

> All of today's prompts and templates are maintained here — every reference in the segments matches this section word for word; the student document carries the same text. Project the whole block so students can copy it straight into AI. **Discipline restated: both review rounds run in the same conversation — change roles without changing windows; a new window = a dropped baton.**

### 6.1 The three checks for a library (Segments 2–3 — keep projected)

```text
Three checks before calling in a library (2 of 3 pass — bring it in):
① When was it last updated? (Nothing in three years — think twice.)
② Does it have examples? (No examples = no manual.)
③ Is it documented completely?
(Fourth check, for when something breaks: is my board on the
supported-hardware list?)
```

### 6.2 The selection advisor prompt (Segment 4)

```text
This is my requirements sheet's core function: ______.
The board I'm using: ______.
Be my selection advisor: recommend 3 external libraries that might help,
one line each — what it does and why it fits me — ranked by fit.
Reminder: only recommend libraries that really exist and support my board.
```

### 6.3 The minimal-change prompt (Segment 5)

```text
Building on our last round: I installed the library ______; its example
can ___ (one line).
My core function is: ______.
Reshape the example into my feature: change only the smallest piece first —
let it run, then I'll ask for the next piece.
```

### 6.4 Review prompt one: Quinn's sturdiness checklist (Segment 10 — this leg's lead, test every one)

```text
Quinn, still you. Based on the current state: my project can ___ now,
and can't ___ yet.
You're a test engineer. Give me a 5-point "sturdiness checklist":
use it 10 times in a row? leave it alone 5 minutes, then touch it?
a different person tries it? press fast, press slow, press randomly?
— make each one specific: exactly how to operate it, and what to watch for.
```

### 6.5 Review prompt two: the Picky User, one fault (Segment 10 — this leg, downgraded)

```text
You are now my real user (___). My project currently does: ___,
and still can't: ___.
No praise allowed. As them, pick only 1 fault — the single most lethal one.
```

> Push-back prompt when AI praises (projected): **"No praise. Faults only."**

### 6.6 Quinn's entrance condition (Segment 10 — same as Lesson 8)

Quinn is the BMAD team's test engineer — this conversation needs the team in it for Quinn to appear. The project conversation has run continuously since Lesson 8 (the background line was already sent) → send 6.4 directly; a fresh conversation sends the background line first, then 6.4:

```text
This conversation has a BMAD team: John (PM), Sally (UX designer),
Winston (architect), Amelia (developer), Quinn (test engineer).
Remember them — I'll call on them directly from now on.
```

### 6.7 The baton handoff sheet template · Leg 2 (Segment 11 — identical to the student document)

```text
# Baton Handoff Sheet · Leg 2
Name: ______  Date: ______

## Where this leg ended (one verifiable sentence: what it can demo)
## I called in ___ (no library? write: "I didn't import, because ___")
## What the look is now (one line: what it looks like now; no shell?
   write: "still loose parts")
## The review point that matters most + my decision (accept/reject + reason)
## The first thing next leg (specific, verifiable — next leg is fix-only,
   think it through)
```

### 6.8 The review record template · Leg 2 (Segments 10–11 — identical to the student document)

```text
# Review Record · Leg 2
## Quinn's 5-point sturdiness checklist (test every one, note the result)
1. ______ tested: passed/broke ______
2. ______ tested: passed/broke ______
3. ______ tested: passed/broke ______
4. ______ tested: passed/broke ______
5. ______ tested: passed/broke ______

## The Picky User's 1 fault
______ → my decision: accept/reject, reason: ______
```

---

## Section 7 · Localization slots

| Where | Original | Swap-in suggestion |
| --- | --- | --- |
| Class-wide install demo library | whatever you rehearsed | the most common project direction in *this* class (by the requirements-sheet survey) |
| The two import cases | complex-sensor driver (import) / blink-three-times (don't) | two real cases from this class's projects — more persuasive |
| Offline pre-downloaded packages | OLED graphics + common sensors | 3–5 picked by this class's requirements-sheet directions |
| The library notes format | annotated example, whiteboard corner | photograph and post to the class group, credited by name (open-source culture landing) |

---

## Section 8 · Teacher reflection page

Take 10 minutes after class. Anything counts — even one line.

**A. Time record**

| Block | Designed | Actual | Gap |
| --- | --- | --- | --- |
| Act 1 · The hardware store | 98 min | | |
| Act 2 · Leg-two sprint | 45 min | | |
| Act 3 · Review & handoff | 37 min | | |

> Note: totals aligned to the session map (98+45+37=180). The Chinese source's feedback page still shows the v1 leftovers (85/55/40) — the session map and segment-by-segment minutes are authoritative.

**B. The four quality numbers**

1. ≥1 library installed and its example running: ___ / ___ students (no-import route with a written reason: ___ students)
2. The one-library rule: send-backs for three picks ___ times
3. Ask 3 students "how do you judge whether a library is trustworthy" — answered 2 of 3 checks: ___ / 3
4. AI review started on time: yes/no; sturdiness checklist tested one by one, all five: ___ / ___ students

**C. Three questions** (required)

1. How many install errors today? Did the mirror / offline USB get used: ______
2. Quality of the no-import students' reasons: ______
3. Keep this session next time: ______; change: ______

**D. Best student one-liner from the review round** (collect for the showcase): ______

Photograph the page and send it to the teaching group, or tuck it back in the course folder. **Every line you write becomes a pitfall another teacher won't hit in the next edition.**

---

_Version: EN v1 ｜ 2026-08-25 ｜ Source: CN 讲师版 v2（2026-08-05；修订说明含 v2：三幕节奏 85+55+40→98+45+37 口径重排、去钟面时刻、删统一休息、零打印、MVP 口径、评审人设递进） ｜ 依据设计版：CFG-5 配置说明书 v1.0 "马拉松 · 第二棒"行（X8(90)+X4 aily 轮(75)，取消统一休息后重排为 180）；积木卡《npm 工程化 + 自定义库》（T3 门槛与降级条款）、《自由创作/马拉松 + AI 评审官》（第二棒 aily 轮变体 + 评审人设递进）、《AI 辅助记录》_

_Localization notes: 「给作品请外援」→ Call In Reinforcements（副题 Give Your MVP a New Power；马拉松第二棒 leg two）；「建材市场」→ the hardware store（配套 don't reinvent the wheel 习语）；「库」→ a library；「开源」→ open source；「三看」→ the three checks（第四看 the fourth check：支持的硬件列表）；「工具间」→ the tool room（金句 "One room on fire doesn't burn the next one."）；「引库取舍课」→ the import decision（教学落点；"引不引库是取舍决定不是默认动作" → importing is a trade-off decision, not a default move；三问 the three questions）；「选型顾问」→ the selection advisor prompt（候选排序 ranked by fit；候选第二名 the runner-up）；「圈定只许 1 个库」→ the one-library rule；「不引库同等正确」→ not importing is just as valid（"为什么不引"说明 a "why not import" note）；「接入工程」→ wire it in（AI 当翻译官 AI as your translator；最小改造 the minimal change）；「闪电编译时刻」→ the lightning moment；「库锦囊」→ the library notes；「外观外援」→ the looks upgrade（MVP 有两张脸 an MVP has two faces：it works / it looks like something；外观服从演示 looks serve the demo）；「像模像样四招」→ the four moves（give it a shell / hold it still / label it / hide the mess；垃圾就是外观的建材市场 trash is the hardware store for looks）；「外观快装」→ the quick shell；「第二棒冲刺目标」→ finish the core function；「结实度清单」→ the sturdiness checklist（Quinn 5 条逐条实测 test every one——本棒升级不只抽 2 条）；「挑剔用户降级」→ the Picky User, one fault；「只修不加」→ fix-only（第 10 课冲刺纪律预告）；「野蛮人测试」→ the barbarian test；「分诊三栏」→ the triage board；「装库报错标准姿势」→ the error-to-AI move；「降级条款」→ the downgrade clause（双倍创作轮 the double build round）；「九次课旅程」→ the nine-lesson journey（封顶仪式）；兜底「给作品加表盘」→ add a face to your project。BMAD 五角色与 Quinn 前提沿用第 8 课口径；「评审不可取消只可换执行者」→ "The review can't be canceled — only its executor changes."；「不赌中文渲染」规则天然满足——一切屏幕内容为英文/数字/图形。_
