# Teacher's Guide ｜ Lesson 4 · Assemble Your Team: Build a Smart Pomodoro Timer

_BMAD's Five Roles · Your First Complete Project ｜ Chaihuo Maker Academy · M0 Hardware Foundation · Smart Hardware Fundamentals ｜ 10-session term ｜ 3 hours (no scheduled break)_

> **Source:** 中文版 v2.4（M0_教师课件_CFG-5_第4课_组团队做番茄钟_v2.md，修订至 v2.4）
> **Localized edition** — same blocks, same minutes, same teaching intent; classroom language rewritten for an English-speaking teacher to pick up and teach from.

---

## The one-sentence brief

Today is a **method session + project session**. You introduce **BMAD** — five AI roles (PM, designer, architect, developer, tester) — then run that whole team through **one complete project**: a smart Pomodoro timer on the Wio Terminal with a personal **differentiator**. The core experience is one line: **teacher guidance + student workbook + AI conversation → the student's own conclusions and results.** Every block's output lands in the student's own record — an online md doc if possible, handwriting in a notebook if not.

The session runs five segments: **assemble the team** (30 min) → **the five-round relay** (90 min) → **wrap-up** (15 min) → **the 25-min buffer** (not free time — see 2.1) → **close** (15 min). **No scheduled break** — students use the bathroom on their own during hands-on time.

**Today's iron law:** the testing round's **15 minutes are untouchable** — the loop closing matters more than feature completeness. That is the baseline of this "showcase lesson."

---

## 🎯 Learning Objectives

*By the end of this session, students will be able to…*

1. **Explain** why "write-it-direct" hits a ceiling and what "plan-first" adds (*Bloom: Explain*).
2. **Run** a five-round relay in **one** conversation, handing each role the previous round's conclusion (*Bloom: Apply*).
3. **Draw** the state circles of their timer — at least WORK and BREAK, with what triggers the switch (*Bloom: Create*).
4. **Evaluate** their finished timer against a break-it list, making an **Accept or Reject** call on each fault (*Bloom: Evaluate*).

---

## Page One — read this before class starts

### What today produces (six student outputs + the relay log)

1. **One problem definition** — PM round: "3 things my clock must do," and one of them is the differentiator;
2. **One screen design** — two screens + the three-button split, differentiator visible on screen;
3. **One set of state circles** — "how many looks does my clock have, and what action moves it," drawn on paper;
4. **One working timer** — at least two states + timing + reminder;
5. **One break-it list** — 5 ways to break it, tested one by one, each judged **Accept or Reject**;
6. **One AI log** — *did __ / stuck at __ / then __ / next time __* — and today, one line must be written clearly: **where is my clock different?**

Plus the **five-round relay screenshot archive** — the full record of the student's first complete project. **This session has the strictest record-completeness bar in the whole course.** Delivery: md doc or handwriting, handed to the teacher after class (link or photo).

### Three things you need to do

1. **Follow the clock.** Work down the timeline; every block says how many minutes and what to do.
2. **Read the lines.** Every 🗣️ line is pre-written classroom speech — read it as-is, don't improvise.
3. **Guard the handoff chain.** Today is a relay: every round opens with *"based on the previous round's conclusion."* Today's mantra: **"What was the last round's conclusion? Hand it to the new role."**

### Three things you do NOT need to do

1. **You don't need to write code.** AI writes it all; you never read a line of it. Whatever the state circles look like, AI confirms them.
2. **You don't need to teach "state machines."** One 8-minute whole-class talk, prop = a traffic light — "one light at a time, it changes when time's up." Draw it on the board.
3. **You don't need to invent differentiators.** They grow out of students' own lives. You only ask one question: **"The moment you space out — what should the clock do?"**

### When things go wrong

- **Live demo fails:** switch to the backup screenshot within 30 seconds, using Section 5's speed sheet. **This is not an incident — the plan is designed for it.**
- **Student device fails:** swap the device or the cable. Don't repair.
- **You're stumped:** smile, and say *"Let's ask AI together."*
- One-liner: **swap, cut to backup, ask AI.**

---

## Before Class

### 1.1 A week ahead (once)

- [ ] **Network check:** walk codecraft.seeed.cc end-to-end once; every institution LLM account valid — today each student runs **5+ long conversations**, more than double last session's usage.
- [ ] **Wio Terminal count** (by actual headcount, plus 2 spares), all pre-flashed, **each one tested: press A → screen changes color + buzzer sounds** (we push it to the limit today). Re-stick any loose flash-mode stickers from Lesson 3.
- [ ] **USB-C cables:** 1 per kit + spares in the box.
- [ ] **Circulating plan:** today has the highest circulation intensity in the course. A TA is preferred (split in 2.3); solo works — just slow the pace.
- [ ] **Zero printing.** Everything is shown on screen — the BMAD compare page, the one-line role cards, the five round openers, the 8-step map (text in Section 6). No table tents, no cards, no printed workbooks. Student output lives in their own md doc or notebook.
- [ ] **Sticky notes:** 3 per student + thick pens; wall space cleared (for the "where I got stuck" wall at the end).
- [ ] **Whiteboard:** draw the empty **8-step map** (eight empty boxes in one or two rows); keep Lesson 2's **Project Wall** up (we look back at it in the opener).
- [ ] **Day-before reminder** to the class group (copy-paste): *"Next session we give AI a team and build one complete project — your own smart Pomodoro timer. Bring your project manifesto and three-box design sheet — md link or a photo is fine. Laptop as usual."*
- [ ] **Review the follow-up list**; decide pairings for students who need them (if Wio count is short, pair two to one kit and alternate roles — a plus, not a downgrade).

### 1.2 On the day (arrive ~1 hour early)

One person needs ~50 minutes — **arrive 1 hour early**. With a TA: the TA does the device check and table setup; you do the screen, whiteboard, and 1.3 rehearsals. If time is really tight, **Rehearsal 1 (the full five-round run) is mandatory**; cut the rest.

- [ ] Teacher machine screen test: Codecraft opens, logs in, chats; today's screen pages (BMAD compare, one-line role cards, round openers, 8-step map) queued in order.
- [ ] Wio check: plug USB-C, screen lights up = back in the box.
- [ ] Each table: 1 Wio, 1 USB-C cable, a marker.
- [ ] Whiteboard: five role names in a row (PM → Designer → Architect → Developer → Tester); 8-step empty boxes drawn.
- [ ] Five-round relay sample screenshots + break-it sample screenshots on the teacher machine, in order.
- [ ] **Emergency offline pack:** 1 phone hotspot + your pre-run relay screenshots. **No paper-only downgrade for this session** — total offline means reschedule (a showcase lesson doesn't "make do"); the hotspot covers it first.

### 1.3 Rehearsals (allow 40 minutes — play the student first)

One principle today: **rehearse as the student.** If the full run takes over 90 minutes, your openers are too long — cut them. **Every on-screen element must be verified in English / numbers / graphics — never gamble on Chinese rendering** (Lesson 1 rule, still in force).

**Rehearsal 1 ｜ the five-round relay (the spine — used in every relay round)**
Run the five openers from Section 6 for real, five rounds back to back in one conversation. Collect: ① the PM's "3 things my clock must do" list; ② the designer's two screens + three buttons; ③ the architect's technical plan (draw your own state circles on paper first — at least two); ④ complete code flashed and running in one pass (paste errors back verbatim); ⑤ the tester's 5 break-it methods, tested one by one — actually break at least 1 and fix it. **Save one screenshot per round — these are your samples of "what the record looks like."** Then verify the lifeline prompt (3.6): paste it verbatim into a fresh conversation and confirm the state switch runs.

**Rehearsal 2 ｜ the traffic-light talk (used at 14:55 — today's only whole-class lecture)**
Dry-run the 8-minute version at a blank board: draw the traffic light → "one light at a time, it changes when time's up" → "your timer is the same kind of thing" → assign the state circles. Time it; over 8 minutes → cut examples.

**Rehearsal 3 ｜ the buffer easter eggs**
Candidates: **the flip timer** (turn the board over and it starts timing — accelerometer), **the victory jingle** (a tune after 3 completed rounds), **the rest-screen joke** (an English one-liner on the break screen). Pick 1–2 and run them for real — **only rehearsal-proven eggs go in the buffer**; if none work, the buffer keeps only the finish-to-standard and 8-step-mapping exits.

### 1.4 Supplies: three buckets

**📦 In the kit (count only, nothing to buy)**
- Wio Terminals for actual headcount (+2 spares), USB-C cables, teacher demo kit
- Flash-mode stickers (from Lesson 3; re-stick any loose ones during the check)

**🛒 You buy (one stationery run)**
- Sticky notes ×3 per student + thick pens; whiteboard pens
- 1 phone hotspot (offline fallback)
- **Nothing printed** — every display item (BMAD compare, role cards, openers, 8-step map) is on screen

**✨ Optional (fine without)**
- 3–5 photos of past students' Pomodoro timers (nice for the kickoff; verbal works too)

Budget: everything to buy is one stationery trip.

---

## Session Map (14:00–17:00 — shift the whole clock to your actual time, e.g. 9:00–12:00; block lengths stay. No scheduled break.)

| Clock | Block | Students are… | You are… |
| --- | --- | --- | --- |
| 14:00–14:08 | Collect Lesson 3 outputs + look-back | handing in, looking at the Project Wall | taking a note of who handed in, one-point look-back |
| 14:08–14:14 | Why BMAD: write-it-direct vs plan-first | self-check by show of hands, hearing the contrast | screening the compare page |
| 14:14–14:17 | Meet BMAD: open source, free, professional | hearing three facts, noting the GitHub address | screening the "meet BMAD" page; three sentences, done |
| 14:17–14:19 | How to use BMAD: two ways | hearing the two ways | screening the two-ways page; no live install |
| 14:19–14:26 | The Five Roles map | hearing who owns what | connecting names on the board + screening the role table |
| 14:26–14:31 | Kickoff: the timer + differentiator | thinking "my focus problem" | setting the rule "one thing must be different" |
| 14:31–14:43 | Round 1: Product Manager | PM conversation with AI, writing the 3 things | leading the opener, watching the differentiator (the success line) |
| 14:43–14:55 | Round 2: Designer | designing two screens + three buttons | leading the opener, watching the differentiator land on screen |
| 14:55–15:10 | Round 3: Architect | drawing state circles, AI writes the plan | **8-min whole-class lecture (the only one)** |
| 15:10–15:45 | Round 4: Developer | building it whole: generate → upload → run → iterate | watching error-returns, handing out the lifeline |
| 15:45–16:00 | Round 5: Tester (**iron law: 15 min**) | breaking it by the list, Accept/Reject each | protecting the time, teaching the Picky User |
| 16:00–16:15 | Wrap-up: archive + transfer + BMAD | screenshotting, talking transfer, writing the log | running the archive ritual, reading the BMAD line |
| 16:15–16:40 | Buffer 25 min (see 2.1) | finishing to standard / easter egg / 8-step mapping | circulating, holding "standard first, then fast" |
| 16:40–17:00 | Close: 8-step mapping + share-out + preview | writing the mapping, sticky on the wall, sharing differences | leading the mapping review, previewing Lesson 5 |

### 2.1 The 25-min buffer — decide the exit before class, announce it at 16:15

The buffer is flexible time, **not free time**. Before class, pick today's main exit and announce it. Three exits, in priority order:

1. **Finish to standard (most common):** timer not running → keep going. Today's line: "two states + timing + reminder running" — everyone must cross it. Backfill missing relay screenshots.
2. **Easter eggs (for the fast — only the ones you rehearsed):** flip timer / victory jingle / rest-screen joke, pick one. An egg that doesn't work out doesn't affect passing. Before starting, take two minutes to decide "do or skip" — *that decision is itself today's method.*
3. **8-step mapping:** go through your own relay log; against the 8-step map on the board, write one line per box in the workbook — "what I did in this step" ("not yet" for boxes you didn't visit) — everyone can do this; it feeds the close.

**The only rule: standard first, then fast.** The buffer is not early dismissal — you circulate; the TA watches the stragglers.

### 2.2 Time flexibility (if you run long/short)

- **Never cut:** the testing round's 15 minutes (iron law), the architect round's 8-minute lecture, the developer round's "make it run" time.
- **Can compress:** the kickoff (8→5 min); the transfer talk (fold into one line in the wrap-up); the buffer (if everyone passes, start the close 15 min early); the share-out (10→5 min).
- **If time collapses in the dev round, the priority ladder is:** make it run > differentiator > easter eggs — acceptance level drops with the ladder, **but the testing 15 minutes are never borrowed.**

### 2.3 TA split (if you have one; solo works — just circulate slower)

| When | TA A (flow officer) | TA B (tech officer) |
| --- | --- | --- |
| Assemble the team | register who handed in Lesson 3 output | finish the device check, photograph the Five Roles board |
| Five-round relay | watch the handoff chain — does the opener's first line pick up the last round's conclusion? Send broken chains back to fix | station at the dev round: errors pasted back verbatim; lifeline prompt to anyone not running at 35 min |
| Wrap-up + buffer | check every student's five-round record is complete; mark gaps for after-class backfill | keep below-the-line students on the build; lead the fast ones through eggs |
| Close | run the sticky wall + share-out | photograph the builds (hands only, no faces), update the follow-up list |

---

## Section 3 · Segment-by-segment script

### Segment 1 ｜ Assemble the team (14:00–14:31)

> Goal: collect Lesson 3 outputs; make the case for BMAD with the write-it-direct vs plan-first contrast; first pass at the Five Roles; kick off the timer with the differentiator rule. Deeper goal: "assembling a team" is not a ceremony — it's the answer students earn by hitting the ceiling themselves.

**14:00–14:08 ｜ Collect outputs + Project Wall look-back** — *[I Do → We Do]*

🗣️ **Say this:** "Before we start, let's collect last session's work: md doc — send me the link; handwriting — photograph it and send it. Missed it? Note it — due before today ends. (point at the Project Wall) Look — it's still up. Everyone's manifesto is on it. Last session you met your new gear; your project got a face and hands. And you learned how to describe a screen clearly — what were the three things again? (guide to: position, size, color) Right — you'll use all of it today. Keep your project manifesto and three-box design sheet at hand — they're about to do a lot of work."

👀 **Watch for:** hard 5-minute timer on collecting; no individual feedback; give the missing list to the TA to register, don't chase. Everything produced today continues in the student's own doc (md or handwriting) — same deal as Lesson 3.

📌 **Output anchor:** Lesson 3 output ("my Wio tour sheet" / screen designs / log) submitted — md link or photo.

**14:08–14:14 ｜ Why BMAD: write-it-direct vs plan-first** — *[I Do]*

🗣️ **Say this:** "Quick talk. You already know how to get AI to make you something in one sentence — fine for small stuff. But three questions — raise your hand if you've hit any: first, the code's getting long, you want to add a feature, and you don't know where to tell AI to change it? Second, you're halfway through and realize you never thought it through at the start? Third, you want to change the color scheme and have no idea where the color lives? (pause, watch the hands) — That's not your problem. That's the ceiling of the one-sentence approach. (screen: the compare page) Two ways. **Way A, write-it-direct:** it runs, and that's about it — the layout is whatever happened, adding features gets messy, recoloring is guesswork. **Way B, plan-first:** think through what you want, what it looks like, how it's split — then build. The screen is designed. The structure is clear. You know where new things go. **This isn't extra busywork — it's having AI think it through with you, a few steps at a time.**"

👀 **Watch for:** all three questions come from the students' real situations in earlier sessions — the more hands go up, the easier the Five Roles land. If someone raises a hand, ask "where were you stuck?" — 30 seconds of empathy beats explaining. The compare page is **static** — no live AI demo. You're explaining *why*, not proving AI fails (today's AI usually gets it on the first pass — don't bet on a staged crash).

🛡️ **CFU:** "Thumbs up if plan-first sounds like more work right now. Middle if you can see the point. Keep it honest — no right answer."

**14:14–14:17 ｜ Meet BMAD: open source, free, professional** — *[I Do]*

🗣️ **Say this:** "This approach has a real name — **BMAD**. AI-driven agile development. Three things to remember. **One: open source and free** — all its docs and code are public on GitHub; anyone can use it, zero cost. **Two: developers worldwide use it** — this isn't something I invented; it's a method professional teams maintain and keep updating, with a dozen-plus roles and thirty-plus ready workflows inside. **Three: the one core move** — don't let AI do everything in one sentence; have it play different roles and think it through step by step before you build. (point at the screen) The address: **github.com/bmad-code-org/BMAD-METHOD** — open source, so you can check every word I just said. Note: BMAD is **not software to install**. It's a method. Methods don't get installed — learn it, and it's yours. Today you learn its one core move."

👀 **Watch for:** three sentences and move on — no framework deep-dive. "Is it really free?" → "Open source means the code is public and free forever — it says so on GitHub." The full name (Breakthrough Method for Agile AI-Driven Development) is on screen; don't read it aloud.

🛡️ **CFU:** "Turn to your neighbor: one sentence — what is BMAD, to a total beginner?" *(wait time ~15 s, then two random shares)*

**14:17–14:19 ｜ How to use BMAD: two ways — today we use the first** — *[I Do]*

🗣️ **Say this:** "How do you use it? Two ways — today, only the first. **Way one, right here in class: install nothing.** The five round-openers you're about to get are BMAD's core usage — PM, designer, architect, developer, tester, in a relay inside one conversation. The method lives in your head — that's the valuable part. **Way two, optional, after class:** later, when you want a full AI team set up inside a project on your own computer — no commands to memorize, **let AI install it**. Just say: *'Read the documentation at https://github.com/bmad-code-org/BMAD-METHOD and configure the BMAD workflow in my project.'* AI visits the GitHub repo, runs the install, and drops the whole set of roles and workflows into your project. That needs a Node.js environment — not today. Want to try it? Find me or a TA after class. **Today's one goal: run this method once, in your head. Tools can be installed anytime; the method in your head stays with you.**"

👀 **Watch for:** no live install, no software setup of any kind. If students push for it, note their names — follow up after class.

**14:19–14:26 ｜ The Five Roles map (board connections + screen)** — *[I Do → We Do]*

🗣️ **Say this:** (screen the one-line role cards; point at the five names already on the board, one sentence each) "BMAD's team is five people. **PM** — owns *what problem we're solving and who it's for*. **Designer** — owns *what it looks like and how you use it*. **Architect** — owns *how it's split into pieces and what states it has*. **Developer** — owns *writing it*. **Tester** — owns *finding what's wrong*. (point at the 8-step map from Lesson 1) Look: framing the problem and finding the user — that's PM. Prototyping — designer and architect. Writing code — developer. Trade-offs and judging — architect and tester. **What you used to do alone is now five experts sharing the work. And you — you're the boss of this team.** Don't worry: it's not five real people. It's five rounds of relay inside one conversation. Each round still runs on the Five Rules: one thing at a time, say the input and output, give it an example, if it's wrong add a line, ask it to explain. What changes: each round has a clear job. Change roles without changing windows — just call the name. They all have names — PM is **John**, designer **Sally**, architect **Winston**, developer **Amelia**, tester **Quinn** — like assigning work to colleagues. And these five roles aren't my invention — professional developers put them together and shared them openly. Today you use the professional team, in one conversation, five rounds."

👀 **Watch for:** draw the connecting lines on the board as you talk; photograph the finished board (student log material). Role names land as "owns ___" the first time they appear — no abbreviations, no origin story. The role table is on screen; no table tents — board + screen is enough.

🛡️ **CFU:** "Point at the board — which role owns 'what it looks like'?" *(one random call)*

**14:26–14:31 ｜ Kickoff: the timer + "one thing must be different"** — *[I Do]*

🗣️ **Say this:** "Pomodoro: 25 minutes of focus, 5-minute break, repeat. That simple. Today everyone builds one — on your Wio, with this team. But there's a rule — **your timer must have one thing different from everyone else's.** Not 'mine is blue' — that's not it. It has to grow out of your life: do you space out doing homework? Do you need to time your piano practice? Are you building one for your little sister? Here's a secret: AI gives everyone the same default answer. The details of your life are the part it can't give you — **that's what makes your clock worth something.**"

👀 **Students:** listen; start thinking "what is my focus problem."

⚠️ **Pitfalls:**
- "I want one like a game console!" → "Good — then today we get the *timing* part running, and the game part goes on the 'later' list." (Not rejecting — into the list. That's the first live trade-off.)
- Student missed Lesson 3 / never used Wio → TA runs a 5-minute refresher (the switch mantra: "slide it, slide it = flash mode", "no response? slide it"), then one warm-up: show "HELLO" in big letters on screen, then rejoin.

🛡️ **CFU:** "Turn to your neighbor: one real focus problem in your life. Fifteen seconds — go." *(wait time, then continue)*

---

### Segment 2 ｜ The five-round relay (14:31–16:00)

> Goal: each student walks their own timer through PM → designer → architect → developer → tester, and every round opens by picking up the previous round's conclusion. Deeper goal: **anti-sameness is today's success line — 20 identical timers = failure, even if they all run.**

**14:31–14:43 ｜ Round 1: Product Manager** — *[I Do → You Do]*

🗣️ **Say this:** "Round one — PM on. The PM doesn't build; the PM asks first. Today the person you ask is yourself: **what is my real focus problem?** Open your workbook (or notebook) to the PM opener — it's on screen too. Look at the first line — every round today opens with *'based on the previous round's conclusion'*, handing the last conversation's result to the new role. It's a relay — don't drop the baton. Round one has no previous round, so you start from your problem. **Important: all five rounds happen in ONE conversation.** Don't open a new one — the moment you do, every conclusion so far is gone. Change roles without changing windows: just call the name — 'Sally, based on the previous round…'."

**On screen (same as the workbook):**

```text
John, I want to build a Pomodoro timer for this problem:
(one real thing from your life — e.g. I pick up my phone within 10 minutes of starting homework)
First ask me 5 questions to understand what I need, then help me write down:
the 3 things this clock must do. Don't write code yet.
```

🗣️ **Say this (cont.):** "Of the 3 things he gives you, one must be your differentiator. Not there? Push back: *'I haven't told you my special requirement —'* (e.g. what should it do the moment I space out? My sister will use it — should the text be extra big?)"

👀 **Students do:** PM conversation; copy "the 3 things my clock must do" into the workbook (the next round needs it).

⚠️ **Pitfalls:**
- ⭐ **Vague differentiator** ("mine is blue", "make it cuter") — the main battleground of today's success line: push to behavior — "Does blue fix your spacing out? The moment you space out, what should the clock do?" **TA circulation focuses here first.**
- Student copies AI's default "standard timer features" → "That's everyone's clock. Where's yours?"
- AI's list is bloated (wants everything) → teach the one professional line: "Too much. Keep only **P0**." (P0 = must-have, P1 = nice-to-have, P2 = bonus; first version = P0 only. Don't explain the concept — one use and it sticks.)
- Student still not in the conversation at 5 minutes (stuck choosing a problem) → teacher offers two candidates; pick one in 30 seconds.

📌 **Output anchor:** workbook — "3 things my clock must do," with one starred — that's my differentiator.

**14:43–14:55 ｜ Round 2: Designer** — *[I Do → You Do]*

🗣️ **Say this:** "Round two — designer on. First line as usual: based on the previous round. Last session you practiced 'how to describe a screen': position, size, color. Today the scaffolding is gone — you organize the language yourself. The sentences are in your workbook — forgetting how is normal. Look, then speak."

**On screen:**

```text
Sally, based on the previous round: my clock must do these 3 things: (copy them).
Design: 1. what the focusing screen looks like; 2. what the break screen looks like;
3. what buttons A, B, C each do.
My special requirement: (your differentiator) — it must show on the screens.
Don't write code yet.
```

👀 **Students do:** designer conversation; add the two screens + three-button split to the workbook.

⚠️ **Pitfalls:**
- Student stuck describing the screen → point at the workbook sentence: "Three things from last session — position, size, color." Point at the scaffold; don't say it for them.
- AI's design misses the differentiator → "Ask it: *'Which screen shows my special requirement?'*"
- On-screen text: **English / numbers / graphics only** — the board's Chinese font is unreliable; never gamble on Chinese rendering.

📌 **Output anchor:** workbook — "focusing screen: ___ / break screen: ___ / A ___, B ___, C ___."

**14:55–15:10 ｜ Round 3: Architect (includes the one 8-minute lecture)** — *[I Do → You Do]*

🗣️ **Say this** (whole class, traffic light on the board):

> "Everyone, eyes on the board. These 8 minutes are the only time I teach today. A traffic light — red, green, one light at a time. What changes it? Time runs out. — Your timer is the same kind of thing: it has several 'looks', it's in one look at a time, and an action moves it to another look. This thing has a name — a **state**. Now, everyone draw **the state circles** of your clock on paper: at least two circles — focus, break — and on the arrow write what changes it, like 'press A' or 'time's up'. Can't make three circles? Two circles are a complete Pomodoro timer. 'Paused' is the most common third circle — add it if you want."

*(about 4 minutes in)*

🗣️ **Say this (cont.):** "Drawn? Round three — architect on. Winston takes the requirements and the design and produces the technical plan. You don't need to understand the details — it's not for you, it's for Amelia, who writes the code next."

**On screen:**

```text
Winston, your turn.
Based on the requirements and design above, make a technical plan for the timer — keep it simple,
Amelia will write the code from it.
```

👀 **Students do:** draw state circles on paper (this paper is collected after class with the conversation record); run the architecture conversation.

⚠️ **Pitfalls:**
- ⭐ **Can't draw the circles (today's #1 pitfall)** → first, let them copy: the **two-state starter** (focus → break, A switches) drawn for them; after copying, add their own circle. **Still stuck after copying → skip the architecture conversation, go straight to the dev round with the two-state default**; the architecture understanding gets picked up at Lesson 8's two-views session. Don't burn time here.
- "Why draw circles, why not just build?" → "This is a map for the program. At Lesson 8 you'll see the actual code — and the circles live inside it." **(one-line teaser; don't expand.)**

📌 **Output anchor:** state circles on paper (or two lines in the workbook: "my states: ___ → ___, what changes it: ___").

**15:10–15:45 ｜ Round 4: Developer (35 min)** — *[I Do → You Do]*

🗣️ **Say this:** "Round four — developer on. PM's requirements, Sally's design, Winston's plan are all sitting in this conversation — Amelia builds the whole timer from them. Build it, upload it, run it. Error? **Paste the error back verbatim** — it wrote the code, it fixes it. Once it runs, make one change of your own — a background color, a transition — that's iteration."

**On screen:**

```text
Amelia, based on the requirements, design and technical plan above, build the complete timer
and give me code I can use directly.
For easy testing, set the work time to 1 minute and the break to 30 seconds first.
```

👀 **Students do:** full code → upload to Wio → run → iterate the differentiator; at 15:35, one whole-class check — the teacher calls: **"Whose clock is running?"**

⚠️ **Pitfalls:**
- Error / upload failure → paste the error back to Amelia verbatim; if the upload fails, flip the side switch twice into bootloader mode and retry.
- ⭐ **Not running by 35 minutes (the most common tech stall) → the TA hands out the lifeline prompt**, to be pasted verbatim:

  ```text
  My timer has two states: WORK and BREAK. Pressing A switches between them:
  WORK shows a red background and "WORK"; BREAK shows a green background and "BREAK".
  For now, only do this switching — no timing — using a simple if/else on the current state.
  ```

  *(The lifeline is the guaranteed minimum: get the screen glowing first, then Amelia adds the full features back on top — the differentiator is unaffected.)*
- "This is harder than the other lessons" → the standing line (whole class or one-to-one): "Right. This is your first real project. Before, you were learning moves. Today, you step on the field for the first time."
- At 15:30, most still not running → whole-class announcement: "Not running yet — raise your hand. TA first, with the lifeline. Running? Move on — add your differentiator." (No waiting; tiered release.)

📌 **Output anchor:** the timer running on the Wio; the differentiator visible on screen.

**15:45–16:00 ｜ Round 5: Tester (15 min — iron law, never borrowed)** — *[I Do → You Do]*

🗣️ **Say this:** "Last relay round — tester on. A tester's job has one word: **break it.** Ask AI for the whole break-it list: rapid repeated presses, mashing buttons mid-timer, holding a button down… then you try each one, by hand."

**On screen:**

```text
Quinn, my timer is done.
Help me find fault: give me 5 ways to "break it", like rapid presses, or mashing buttons mid-timer.
I'll try each one myself.
```

🗣️ **Say this (cont.):** "List tried — one more special reviewer on stage: **the Picky User.** You met it in Lesson 2: AI plays the real person from your design sheet, and it picks exactly one fault. Today it accepts your clock."

**On screen:**

```text
Play ___ (the real person from your design sheet) and use my Pomodoro timer.
Pick 1 fault. Only 1.
```

🗣️ **Say this (cont.):** "Every test you try, every fault you hear — make a call: **Accept or Reject?** Reject → have AI fix it. Accept → write down 'I know it has this small flaw' — that's a professional decision too. In Lesson 2 we accepted one, remember: it still stopped after a few extra presses — we accepted it."

👀 **Students do:** get the 5-item list → test one by one → the Picky User's one fault → Accept/Reject each → actually fix at least one.

⚠️ **Pitfalls:**
- Can't break anything (rare) → "Swap with your neighbor — you'll have no mercy on someone else's clock." (Swapping is also a hidden anti-sameness check: you see how their clock is different.)
- Student fixing forever → "Fix the most important one. The rest goes on the 'later' list." (The later list is a real deliverable, not a consolation prize.)
- **Under no circumstances does this block end early or get squeezed** — even if earlier rounds collapsed, protect the full 15 minutes from here.

📌 **Output anchor:** workbook — the 5-item break-it list, each with "Accept / Reject" + one reason; the Picky User's one fault noted separately.

---

### Segment 3 ｜ Wrap-up: archive + transfer + BMAD (16:00–16:15) — *[I Do → We Do]*

🗣️ **Say this:** "Stop. Next 15 minutes — three things more important than easter eggs. **One: archive.** Screenshot each of the five relay rounds — five screenshots into one folder, named with your name and date. This folder is treasure — **the full record of your first complete project.** Later, when you want to know what a complete project looks like, this is it. Missed a round? Backfill it after class and stick a note in the folder: 'backfilled.'"

🗣️ **Say this (cont.):** "**Two — a big question: does this method only work for hardware?** (two seconds) Here's one from me: **I wrote this course's lesson plans with these five people** — PM decided what problem each session solves; tester found the holes in my plan. Your turn: writing a research report? Who's the PM? (guide: choosing the question) The architect? (the outline) The tester? (finding each other's mistakes) One use case per table."

🗣️ **Say this (cont.):** "**Three — one line to close: BMAD — that's the English team name of these five roles — BMAD's five roles are not a method for hardware. They're a method for anything — today you just practiced it on hardware.** *(Say this line as-is — don't change it.)* The five roles aren't a ceremony. Small projects can merge roles — **the project is as big as the team it needs.** Now look at the road you've walked: 10 years ago, lighting an LED was an entry-level project; 5 years ago, connecting to WiFi was advanced; today, complete beginners finished a full project with five roles in one session. Lesson 1 and 2 — your hardware learned to sense the world. Lesson 3 — your project got a face and hands. Today — you got the method. Last thing: today's log, four lines as usual — and today one line must be written clearly: **where is my clock different?** Write it, then send it to AI: *'Help me turn this into a log — only what I said, nothing I didn't.'* Then read what it writes — AI will confidently invent things. Proofreading is your job; nobody can do it for you."

👀 **Watch for:** transfer talk goes cold → offer your own ("I use it to plan family trips"); "why not just build it directly" → point at the compare page: "One-sentence-all-in-one saves effort, but you get a clone you can't edit. Is the gap speed — or thinking?" TA notes cases for next session's opener ("who actually used it"). Mark missing rounds for backfill + sticky note (completeness target ≥90%).

📌 **Output anchor:** ① five-round screenshots archived; ② one line in the workbook — "I could use this method for ___, and the PM there would be ___"; ③ the four-line log (proofread version) in the workbook.

---

### The 25-min buffer (16:15–16:40) — *[You Do]*

🗣️ **Say this** (opening, per the exit you chose before class): "Next 25 minutes: timer not running — keep going, that's today's line. Past the line — [announce today's pick: try an easter egg / map your relay log against the 8 steps / help a neighbor]. Two egg rules: one, decide 'do or skip' in two minutes — don't dither; two, if the egg doesn't work out, today's pass is unaffected."

👀 **Watch for:** circulation order — first sweep who hasn't crossed the line (TA), then lead the fast ones through eggs. Egg candidates (verbal; rehearsal-proven only): **the flip timer** (turn the board over and it starts timing — the board feels itself flip), **the victory jingle** (a tune after 3 completed rounds), **the rest-screen joke** (an English one-liner on the break screen). Below-the-line students skip eggs; the TA keeps them on the main build (state switching > timing > reminder).

⚠️ **Pitfalls:**
- Egg stuck over 8 minutes → "Eggs done. Make the 'later' list beautiful — that counts too."
- "I'm done — can I leave / play on my phone?" — No. Point at the three exits. The buffer is part of the session, not early dismissal.
- Whole class done early with 15 minutes left → don't drag; move into the close and do the mapping review properly.

📌 **Output anchor (egg students):** one line in the workbook — "the egg I added was ___, it worked / it didn't, so it's on the 'later' list."

---

### Close ｜ 8-step mapping + share-out + preview (16:40–17:00) — *[I Do → You Do → Share-out]*

🗣️ **Say this** (16:40–16:48, at the 8-step map on the board):

> "Last 20 minutes — no building. Something more important: **seeing the road you walked today.** Eight boxes on this map — the complete map of making a project. Today you walked the first six — we'll stick them up round by round: you figured out who it's for and what problem it solves — PM, steps one and two. You said clearly what you want and how it looks — designer, step three. You split it into pieces and ordered them — architect, also step three, and you grazed step five. You built it with AI — developer, step four. You tried it and found faults — tester, step five. You fixed it or lived with it, kept it or cut it — your Accept/Reject calls, your egg do-or-skip — step six. Steps seven and eight only started today: show it to someone — you'll do that in a minute; and look back at it when it's done — that's happening right now."

👀 **Students do** (16:48–16:55): open the five-round log; against the board's map, write one line per box in the workbook — "what I did in this step" (already written during the buffer? skip to the next); then take a sticky — **"where I got stuck"** — one sticky per step, sign it, put it on the wall.

🗣️ **Say this** (16:55–17:00, looking at the wall + share-out + preview):

> "Look at the wall. Which step has the most stickies?" (count; name one or two) "Tell us how stuck you were, and how you got past it. Remember this wall. Today you got fully stuck and fully unstuck — next time you get stuck, you won't panic. Last look across your table: what's different about their clock compared to yours? (30 seconds) Next session, your hardware learns to 'see' — it will recognize your face and your hand. Keep your timer — it's your first complete project, not your last. Devices in the box. Your five-screenshot folder, your state-circles paper, your workbook — take them home, or photograph them. Class dismissed!"

👀 **Watch for:** all stickies piling on "developer" is normal — say it honestly: "Look — the hardest part is making the thing. That's exactly why the steps before it matter: think it through, and the building goes smoother." Short on time → cut the share-out, but keep the mapping writing and the sticky wall. Collect today's outputs after class: md links, handwriting photos — note completeness.

📌 **Output anchor:** ① 8-step mapping written out in the workbook; ② the "where I got stuck" sticky on the wall (photographed).

---

## Section 4 · Live demo backup plan

| Demo | Used in | Rehearsal | Backup material | If it goes wrong live |
| --- | --- | --- | --- | --- |
| Five-round relay sample | every relay round | Rehearsal 1 | one screenshot per round | show that round's screenshot as the model; students keep doing their own conversations |
| Traffic-light state talk | 14:55 | Rehearsal 2 | one example state-circles photo | teach from the photo; circles stuck → follow the 3.5 plan |
| Dev round running (incl. lifeline) | from 15:10 | Rehearsal 1 | lifeline prompt text (Section 6) + running screenshot | paste the lifeline verbatim; once running, have Amelia add the full features back |
| Buffer easter eggs | from 16:15 | Rehearsal 3 | egg screenshots | unproven eggs stay out; the buffer keeps finish-to-standard + 8-step mapping |

> Note: the 14:08 "why BMAD" block is a **static compare page** — no live AI demo. With today's AI, "making AI fail on purpose" usually fails (it gets it on the first pass) — don't bet on it. Explain the contrast; done.

---

## Section 5 · Pitfall speed sheet

Three lines first: **swap, cut to backup, ask AI.** Today's fourth: the handoff chain must not break — every round's first line hands over the previous round's conclusion.

| Situation | What you do |
| --- | --- |
| ⭐ Vague differentiator ("mine is blue") | push to behavior: "The moment you space out — what should the clock do?" — today's success line; TA's #1 circulation focus |
| ⭐ Whole class stuck on the architect round | re-teach the traffic-light analogy + let them copy the two-state starter; still stuck → skip architecture, go to dev; pick it up at Lesson 8 |
| ⭐ Code error / won't flash | paste the error back to Amelia verbatim; upload fail → flip the side switch twice into bootloader; not running at 35 min → TA gives the lifeline prompt (3.6) |
| Five Roles turns into role-play theater | pull back: "What did this role help you think through?" If no answer, return to the handoff board: "PM's output is the designer's input." |
| Student skips rounds and goes straight to Amelia | return to the chain: "No requirements, no design, no plan — what does Amelia build from? Back up a few rounds." |
| Handoff chain broken (chat starts from nowhere) | TA sends back: "First line — based on the previous round's conclusion. What was it?" |
| New conversation opened when changing roles — context lost | "Don't switch windows — call the next role's name in this conversation. The baton lives in the conversation, not in the window count." |
| Time collapses in the dev round | priority ladder: state switching > timing > reminder > differentiator > easter eggs; **the testing 15 is never borrowed** |
| Student says "this is harder than before" | "Right. This is your first real project. Before was learning moves; today is the first time you step on the field." |
| Easter egg fails | pass unaffected; redirect to making the "later" list beautiful |
| Review becomes a monologue | teacher talking time hard-capped at 10 min; nobody volunteers → name the signer of the most crowded step on the wall |
| 5 random demos all identical (sameness) | teaching-quality incident: on the spot, have the 5 explain their differentiators to each other; after class, review the PM round script and note it on the reflection page |
| Missing relay rounds | backfill after class + sticky note "backfilled" in the folder; completeness target ≥90% |
| Offline | hotspot first; no paper downgrade for this session — total offline = reschedule (a showcase lesson doesn't "make do") |

### Appendix: student questions and how to answer them

| Student asks | You say |
| --- | --- |
| "Why not let AI do the whole thing alone?" | "One person doing everything is Way A on the compare page — it runs, and that's about it: the layout is random, and you don't know where to add features. Once a project gets big, someone has to own the requirements and someone has to find fault. You're the boss; they're your team." |
| "Do I have to use all five roles every time?" | "No. The project is as big as the team it needs. Building a small night light? You and the developer are enough. Your Final Project? Bring all five out." |
| "What does the architect actually do?" | "Two things: cut the project into pieces, and tell you what states it has. Look at your timer — timing, display, buzzer: three pieces; focus, break: two states." |
| "Does BMAD need to be installed?" | "No. It's a method, not software — the five-round conversation you just ran *is* BMAD. Later, if you want a full team in your own project, let AI install it: say 'Read the docs at https://github.com/bmad-code-org/BMAD-METHOD and configure the BMAD workflow in my project.' (Needs Node.js.) Come find me after class." |
| "Does a Pomodoro have to be 25 minutes?" | "Your clock, your call. But for easy testing today, start short: 1 minute of focus, 30-second break. Change it once it runs." |
| "Can I skip the easter egg?" | "Yes. Eggs don't affect passing. Just decide 'do or skip' — that's the point." |
| "I don't understand what AI gives me." | "Today we get it running. Understanding it is a Lesson 8 thing — and you'll find the circles you drew today living inside the code." |
| "My clock looks like my neighbor's — what now?" | "Go back to your life: what does yours do when *you* space out? What does theirs do when *they* space out? Guaranteed different." |

---

## Section 6 · Prompt phrase library (teacher reference)

Today's phrases: the five round openers + the lifeline + the break-it list + the Picky User + the log-cleaner. **These are not printed or handed out** — they live in the student workbook; students look them up; you lead them on screen. If the workbook wording differs slightly, either works — the meaning is the same.

### The five round openers (every round opens with "based on the previous round's conclusion")

**PM round**
> John, I want to build a Pomodoro timer for this problem: (one real thing from your life — e.g. I pick up my phone within 10 minutes of starting homework). First ask me 5 questions to understand what I need, then help me write down: the 3 things this clock must do. Don't write code yet.

**Designer round**
> Sally, based on the previous round: my clock must do these 3 things: (copy them). Design: 1. what the focusing screen looks like; 2. what the break screen looks like; 3. what buttons A, B, C each do. My special requirement: (your differentiator) — it must show on the screens. Don't write code yet.

**Architect round**
> Winston, your turn. Based on the requirements and design above, make a technical plan for the timer — keep it simple, Amelia will write the code from it.

**Developer round**
> Amelia, based on the requirements, design and technical plan above, build the complete timer and give me code I can use directly. For easy testing, set the work time to 1 minute and the break to 30 seconds first.

**Tester round**
> Quinn, my timer is done. Help me find fault: give me 5 ways to "break it", like rapid presses, or mashing buttons mid-timer. I'll try each one myself.

### The dev-round lifeline (only if not running at 35 min — paste verbatim)

> My timer has two states: WORK and BREAK. Pressing A switches between them: WORK shows a red background and "WORK"; BREAK shows a green background and "BREAK". For now, only do this switching — no timing — using a simple if/else on the current state.

### The Picky User phrase (tester-round acceptance)

> Play ___ (the real person from your design sheet) and use my Pomodoro timer. Pick 1 fault. Only 1.

### The log-cleaner phrase

> Help me turn this into a log — only what I said, nothing I didn't.

**Usage rules:** the phrases give structure — **you fill in the content** (blank brackets can't be sent); **all five rounds run in one conversation** — change roles by calling the name (John / Sally / Winston / Amelia / Quinn), like assigning work to colleagues; opening a new conversation loses the context; the Five Rules still apply in every round.

- When the feature list bloats, use the one professional line: "Too much. Keep only **P0**." (P0 = must-have, P1 = nice-to-have, P2 = bonus; first version = P0 only.)
- On-screen text: **English / numbers / graphics only** (the board's Chinese font is unreliable — never gamble on Chinese rendering).

### The one-line role cards (for the Five Roles screen)

> **PM (Product Manager)** — owns "what problem we're solving, who it's for"
> **Designer** — owns "what it looks like, how you use it"
> **Architect** — owns "how it's split into pieces, what states it has"
> **Developer** — owns "writing it"
> **Tester** — owns "finding what's wrong"

### The "why BMAD" compare page (14:08 screen)

> **Way A: write-it-direct** — it runs, and that's about it: layout left to chance / adding features gets messy / recoloring is guesswork
> **Way B: plan-first** — the screen is designed / the structure is clear / you know where new things go
> **BMAD**: an open-source method used by developers worldwide — have AI play different roles and think it through step by step before you build.

---

## Section 7 · Localization slots

| Where | Original | Swap-in suggestion |
| --- | --- | --- |
| 14:08 compare-page three questions | [don't know where to add features / never thought it through / don't know where the color lives] | collect 1–2 real "it got messier the more I edited it" stories from veteran students or the homeroom teacher before class — tell those if you have them; otherwise use the defaults |
| Kickoff / PM focus-problem examples | [spacing out on homework / timing piano practice / for my little sister] | your students' real scenes: piano, vocab flashcards, jump-rope counting, for grandparents… get 3 real examples from the homeroom teacher before class |
| Pomodoro rule intro | [25 min focus + 5 min break] | a locally familiar framing (e.g. the school's existing "focus time" rule); the numbers are flexible as long as they're self-consistent |
| Easter egg ideas | [flip timer / victory jingle / rest-screen joke] | local memes, school bell sounds… any idea that's okay to fail within one session; on-screen text stays English |
| Transfer-talk example | [writing a research report] | the real task your students face: exam prep plan, club activity, work presentation — one use case per table |
| Sticky wall | [wall space next to the board] | glass surface, notice board, clips on a line — anything where "which step has the most stickies" is visible at a glance |

---

## Section 8 · Teacher reflection page

Take 10 minutes after class. Anything counts — even one line.

1. Which block went best? Which one do you most want to redo?
2. Did any 🗣️ line sound awkward or unnatural out loud? Cross it out; write what you actually said.
3. Did the compare-page three questions get many hands? Did students really get "what BMAD is and why" (ask two students: "what does the tester own?")?
4. How did the differentiator battle go — pull 5 timers side by side: all five different? Which one was the best?
5. How many couldn't draw the state circles? How many did the two-state starter rescue?
6. Did the 15 testing minutes survive? What tried to squeeze them?
7. How did you actually use the 25-minute buffer? How many eggs went out, what was the success rate? Any free-for-all?
8. Which step had the most stickies on the wall? Enough time? Which block overran, which came up short?

Photograph the page and send it to the teaching group, or tuck it back in the course folder. **Every line you write becomes a pitfall another teacher won't hit in the next edition.**

---

_Version: EN v1 ｜ 2026-08-25 ｜ Source: CN 讲师版 v2.4（2026-07-29） ｜ 依据设计版：B2 v1 / X2 v1 / X6 v1 / CFG-5 配置说明书 v1.0_

_Localization notes: BMAD brand method and five persona names (John/Sally/Winston/Amelia/Quinn) kept in original; '防趋同' -> the sameness standard; '救生句' -> the lifeline prompt; '状态圈' -> the state circles. P0/P1/P2 priority and WORK/BREAK UI display use the Anglicized phrasing from CN version; all screen content follows the 'no gambling on Chinese rendering' rule (naturally satisfied). Source revision decisions (v2->v2.4) fully absorbed: zero printing, static comparison pages don't demo crashes, P0/P1/P2 framing, V1 quote (LED 10 years ago / WiFi 5 years ago / 5-persona project today)._
