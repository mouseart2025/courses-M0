# Lesson 8 · Run the First Lap (Student Workbook)

_Chaihuo Maker Academy · M0 — Zero-to-Hero Smart Hardware_

---

## 1. What You Walk Out With

Last lesson you briefed your project — requirements sheet in hand; the lesson before, you moved it home into your own computer and ran the engineer's loop end to end. From today, **the marathon starts** — three legs, three lessons, building the project on your sheet for real.

Today is **Leg One**, and the lesson is called **"Run the First Lap"** — the lap means three things: leg one of the marathon, the "smallest but complete" lap of your project's MVP, and lap one of Neil's spiral development. By the end of class, you'll have three things:

1. **Your project's MVP** — the smallest version you can demo: not necessarily complete, but it genuinely sensed something and genuinely reacted — the first lap, run through;
2. **A review report card** — your project got picked apart by two "reviewers," you're still standing, and you made Accept or Reject calls;
3. **A baton handoff sheet** — three lines saying "where I got to, the fault and decision that mattered most, and the first thing next leg" — Lesson 9 starts with it the moment you walk in.

Today, for the first time, you run a **complete iteration**: build → review → decide → hand off. An engineer's real work is exactly this loop, turning lap after lap.

---

## 2. A 30-Second Review

- Lesson 7, you wrote the brief: the requirements sheet spells out input, logic, output — plus the "later" list;
- Lesson 6, you moved home: aily-blockly lives in your computer, you've commanded AI to build a project from zero, and you've changed a line of code with your own hands;
- You've also practiced linking: two boards, two programs, one wire.

Today's question: **the sheet is written, the tools are installed — start building. Today, run the first lap of your requirements sheet.**

---

## 3. Today's New Words (in plain language)

**MVP (minimum viable product)** — today's goal, in engineer's slang: **the smallest version you can demo.** Note: it isn't a half-done thing ("half of it built") — it's a **smallest-but-complete lap**: pick the core "sense → react" stretch from your requirements sheet, and get it genuinely running end to end. Everything else on the sheet waits — the rest is sleeping soundly on the "later" list.

**The stand-up** — the marathon's first thing every day: one sentence per person stating today's goal (verifiable). Small class — everyone stands and says it in turn; big class — pair up and say it to each other + write it at the top of your requirements sheet. Then get to work.

**The parts pool** — the modules and materials on the tables are shared. Mark a piece "in use" the moment you take it; return everything not in use at the end of each leg — leaving the road open for others is leaving it open for you.

**The reviewers** — AI's new job today: the Picky User and the test engineer, there to pick your project apart. **A reviewer who praises you = a reviewer who didn't show up for work.**

**The baton handoff sheet** — three lines: where you got to / the fault and decision that mattered most / the first thing next leg. The marathon's relay baton — and the comeback anchor for anyone who misses a class.

---

## 4. Today's Flow

> The lesson runs three acts: **Act 1 · The start** (Step 1) → **Act 2 · The build** (Steps 2–4) → **Act 3 · Review & handoff** (Steps 5–7).

### Step 1: Stand-up + check out the parts (25 min) 【Act 1 · The start】

Stand-up, one sentence each: today I will first get ___ working (verifiable). Small class — everyone stands and says it in turn; big class — pair up, and write that sentence **at the top of your requirements sheet**; the teacher will pick a few to share with the class. Then check out parts against your sheet — **only what the smallest closed loop needs.**

### Step 2: Build, first half (~60 min) 【Act 2 · The build】

Before starting, lay the requirements sheet out on the table and run the **check-in ritual**: point at which stretch is your smallest closed loop, and tell yourself "today, only this."

Then cut the goal into two steps: **first get "sensing has readings"** (the sensor is genuinely reading, and you can see it), **then get "reacting actually happens"** (the output truly moves). Both steps working = the smallest closed loop, closed.

### Step 3: The mid-way stand-up (5 min) 【Act 2 · The build】

Again, 30 seconds each: which step is working / where you're stuck. Being stuck isn't shameful — see the three rules below.

### Step 4: Build, second half + close-out (~55 min) 【Act 2 · The build】

Keep pushing on the second stretch. **15 minutes before review, the teacher circulates table by table to remind you to close out**: hands off the keyboard, save whatever currently runs — **a running 60 beats a non-running 100.**

### Step 5: Two paragraphs + the AI review (15 min — the floor, never squeezed) 【Act 3 · Review & handoff】

First, write two paragraphs (one minute): **My project can now ___; it still can't ___.** — no bragging, the true current state. That's your ticket into the review.

Then, in the **conversation you already have** (don't open a new one!), send the two review prompts in order:

**Prompt one · the Picky User's 3 faults:**

```text
You are now my real user (name: ___; their situation: ___ — copy the real
person from my requirements sheet).
My project currently does: ___ (current real state, no bragging).
It still can't: ___.
You are not allowed to praise me. As them, pick 3 faults:
the one they'd care about most, the one most likely to make them not use it,
the one most confusing. One sentence per fault.
```

**Prompt two · Quinn's 5-item list:**

```text
Quinn, still you. Based on the current state: my project can ___ now, and can't ___ yet.
You're a test engineer. Give me a 5-item list of "how to break or fail it,"
specific to how I operate it and what I watch for.
```

⚠️ **Quinn has an entrance condition:** Quinn is the BMAD team's test engineer — the conversation needs the team in it for Quinn to appear. Your project conversation running since Lesson 4's team build? Send it directly. **A fresh conversation?** Add the background line first, then the prompt above:

```text
This conversation has a BMAD team: John (PM), Sally (UX designer),
Winston (architect), Amelia (developer), Quinn (test engineer).
Remember them — I'll call on them directly from now on.
```

⚠️ AI started praising? Push back: **"No praising. Faults only — 3, one sentence each."**

### Step 6: Decide (10 min) 【Act 3 · Review & handoff】

For every fault dragged out, make a call: **Accept or Reject — each with one written reason.** Accepting everything doesn't make you a good student — **rejecting is a professional decision too.** Pick 2 items off Quinn's list and test them for real; note whether they passed or broke.

### Step 7: The baton handoff sheet + close (10 min) 【Act 3 · Review & handoff**

Fill in the baton handoff sheet (template in Part 5), then wrap up: return everything not in use to the pool, main kits boxed, Brief Wall stickies stay where they are.

---

## 5. Workbench · My Record (keep it in your own notebook)

> This document is shared and read-only — the blanks below, **record them in your own notebook, or say them out loud to your neighbor.**

```text
# Baton Handoff Sheet · Leg 1
Name: ______  Date: ______

## Where this leg ended (one verifiable sentence: what it can demo)
## The review fault that matters most + my decision (accept/reject + reason)
## The first thing next leg (specific, verifiable)
```

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

## 6. When You're Stuck

First, memorize **the three rules** (projected all day):

```text
The three rules of build time
One. Check against your requirements sheet — changing it is allowed, cross it out, don't erase.
Two. 15 minutes with no progress = raise your hand — stuck is not shameful; toughing it out silently is.
Three. Code questions go to your AI first — "one step at a time."
```

| Stuck here | What to do |
| --- | --- |
| Don't know which stretch to build first | The smallest closed loop = the core "sense → react" stretch of your sheet. Unsure? Raise your hand; the teacher settles it in 30 seconds. |
| 15 minutes, no progress | **Raise your hand.** It's a rule, not weakness — stuck isn't shameful; toughing it out is. |
| Upload error | Paste the error back to AI verbatim, one step at a time — no silent trial-and-error. |
| Want to add a new feature | Ask first: does it serve the core feature? No → write it on the "later" list and keep working. |
| The whole project crashed | Crash protocol: tell the teacher; within 15 minutes you get a shrink plan (cut down to what can live). A shrunken version is still a first version. |
| The AI review says I did great | Push back: "No praising. Faults only — 3, one sentence each." A reviewer who praises you = a reviewer who didn't show up. |
| Tempted to accept every review note | Stop. Keep the 3 that matter most; reject the rest with written reasons — you're the one in charge. |
| The module I need is all taken | Queue at the pool, or run the substitute three-questions: can another piece stand in / can the logic change / can it run solo first. |
| Finished early | The fast-lane ladder: build the first item on the "later" list → be your neighbor's live tester → write a one-page user manual. |

---

## 7. Classmates Often Ask

**"What if I can't finish?"**
The first version builds only the smallest closed loop. Everything else sleeps soundly on the "later" list.

**"AI says I did well — no changes needed?"**
Make it stop praising and pick faults only. A reviewer who praises you = a reviewer who didn't show up for work.

**"Can I change the requirements sheet?"**
Yes. Cross it out — don't erase — let everyone see you changed your mind. But ask first: does it serve the core feature?

**"Everyone else's project is better than mine."**
Being one thing better than yesterday is the win. Is your closed loop running? Running = today's 100.**

---

## 8. Today's AI Log

As always, four lines:

```text
Today I made:
I got stuck on:
then:
next time I want:
```

Today the "made" line is mandatory, exactly: **My project's first version can ___; the review picked ___ faults; I accepted ___ and rejected ___.**

The old truth: AI will invent things with a straight face — proofreading is your job. Today it holds two new posts: Picky User + test engineer — but whether the faults are real, only you, the actual user, can say.

---

## 9. After-Class Bonus · The Full Case in the Appendix (strongly recommended)

At the open you met Brandy — Li Shiwen, Seeed application engineer, the one who **built a voice keyboard with zero code**. In class we only covered her first version (1 key, 20 presses without a miss); **the last 25 pages of the deck (pages 18–42) are her complete method** — two real projects, start to finish. Flip through them at home, and you'll see:

- How her annoyance became a requirement (the **input/output contract**: input / constraints / output / success criteria);
- How she chose the first lap (**being explicit about what this round won't build** matters more than what it will);
- The pits she fell into (AI's enclosure render looked cool but couldn't be held by a human hand — **don't trust the render; trust your own hand**);
- How she debugged (**the photo where "the logic is wrong" is the most precious one** — change one rule at a time).

**Two things worth photographing or copying straight out:**

**① The four-line spec** (answer before building anything): 1. What's the input? 2. What's the output? 3. What's the smallest verifiable version? 4. What phenomenon means success? — Map it: your requirements sheet = 1+2, today's MVP = 3, your acceptance line = 4. **You're already working like an engineer.**

**② The hardware prompt template** (use it directly next lesson, when you call for reinforcements):

> I want to use [board] and [components] to achieve [goal].
> Input is [action / data], output is [observable result].
> Do only [minimal verification] for now; skip [later features].
> Give me, in order: ① modules and how they connect ② a wiring table ③ minimal test code ④ verification steps and success criteria ⑤ common errors and the order to check them

---

## 10. Next Lesson Preview

**The Marathon · Leg Two: Call in Reinforcements.** Bring your **baton handoff sheet** and your **two-views cheat sheet** — take on new modules, new libraries, and grow your MVP new abilities.

Today you said "I'm building"; next lesson you say "**it's better**."

---

_Chaihuo Maker Academy M0 · Student Workbook v1 (EN) ｜ 2026-08-26_

_Derivation note: localized from the Chinese student workbook v2 (M0_学员文档_CFG-5_第8课_跑通第一圈_v2.md, internal revisions through v3.2), structure and anchors mirrored 1:1. All verbatim prompts (three rules, Picky User's 3 faults, Quinn's 5-item list, BMAD background line, push-back prompt, baton handoff sheet, review record) copied word-for-word from the English teacher guide M0_EN_TeacherGuide_CFG-5_Lesson08_RunTheFirstLap_v1.md Section 6. Terminology: Run the First Lap / the smallest closed loop / the three acts / the stand-up / the parts pool / the 15-minute hand-raise rule / the crash protocol (the shrink plan) / the fast-lane ladder / the baton handoff sheet (the comeback anchor) / "a running 60 beats a non-running 100". Section 9 (Brandy appendix guide, four-line spec, hardware prompt template) localized from the Chinese workbook — the template matches the deck's page-40 hardware prompt, ready for Lesson 9 reuse._
