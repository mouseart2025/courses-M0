# Lesson 9 · Call in Reinforcements (Student Workbook)

_Chaihuo Maker Academy · M0 — Zero-to-Hero Smart Hardware_

---

## 1. What You Walk Out With

Last lesson you ran the first lap: the MVP demos, it got picked apart in review, you made your calls, and the baton handoff sheet is in your pocket. Today is marathon **Leg Two**, and the lesson is called **"Call in Reinforcements."** Reinforcements come in two kinds: **code reinforcements** (go to the "hardware store" and bring in a ready-made library — don't build wheels someone already built) and **looks reinforcements** (cardboard boxes, tape, and markers from around you, giving your MVP a first look). Second-half sprint: **finish the core feature** on your requirements sheet + a quick shell.

By the end of class, you'll have three things:

1. **One reinforcement brought through the door (or one clear-eyed "no import" decision)** — your project gained an external library, the example runs; or you thought through "why not" and wrote the reason down plainly (both roads equally right);
2. **A finished core feature + a first look** — not "everything you imagine," but the thing written on your requirements sheet genuinely working, and at a glance, anyone can tell what it is;
3. **The Leg-2 baton handoff sheet** — "where I got to, who I called in, the fault and decision that mattered most, the first thing next leg" — the final leg starts with it.

Today you also take away two ideas: **an engineer's strength isn't writing everything alone — it's knowing someone in the world has already written it, and knowing how to pick, install, and adapt it into your own.** And: **an MVP has two faces — it works (the inside) + it looks like something (the outside).** On demo day, people see the outside first; only then do they get to the inside.

---

## 2. A 30-Second Review

- Lesson 8, you ran the first lap: picked the smallest closed loop out of your requirements sheet and built a demoable MVP;
- Two reviewers picked it apart, and you made Accept or Reject calls on each — **you're the one in charge**;
- You filled in the Leg-1 baton handoff sheet: "where I got to / the fault and decision that mattered most / the first thing next leg."

Today's question: **the MVP runs, but it's still thin — call in a reinforcement, then finish the core feature.**

---

## 3. Today's New Words (in plain language)

**Library** — a toolkit someone else wrote, tested, and gives you for free. Making an LED blink three times doesn't need one; driving a complex sensor is inseparable from it. Engineers worldwide hand each other toolkits — that's **open source**.

**The hardware store** — where libraries live (the library manager). Whatever your project needs, someone here has probably already built it.

**The three checks** — the health inspection before calling in a reinforcement: ① when was it last updated ② does it have examples ③ is the documentation complete. **Two of three pass — bring it in.**

**The tool room** — every project has its own private shelf for reinforcements. The Pomodoro timer's library and your project's library each live in their own room — they never fight.

**The translator** — one of AI's new jobs today: example code "demonstrates what the library can do" — it wasn't written for you. Can't read it? Have AI translate, then have it reshape it to your need.

**Looks reinforcements** — reinforcements aren't only code. Cardboard boxes, takeout boxes, old toy shells, tape, markers — **trash is the hardware store for looks**; pick, don't buy.

**The "look like something" four moves** — ① **give it a shell** (it is what it is, so first make it look like what it is) ② **hold it still** (wires that don't wobble, demos that don't shake) ③ **label it** (marker the button names, so strangers dare to touch) ④ **hide the mess** (only the "face" shows). One rule: **looks serve the demo** — never more than a third of build time.

**The reviewers (upgraded this leg)** — last leg's judges checked "does it look the part"; this leg's judges check "**is it sturdy**": Quinn delivers a 5-point sturdiness checklist, **tested item by item**; the Picky User picks only 1 fault — the most lethal one.

---

## 4. Today's Flow

> The lesson runs three acts: **Act 1 · The hardware store** (Steps 1–5) → **Act 2 · Leg-two sprint** (Steps 6–7) → **Act 3 · Review & handoff** (Steps 8–10).

### Step 1: Why libraries (10 min) 【Act 1 · The hardware store】

One comparison: the same complex sensor — without a reinforcement, a hundred lines scrolling three screens; with one, a three-line call. Those hundred lines were written, tested, and gifted to you long ago — that's open source, and that toolkit is called a **library**.

### Step 2: The whole class installs one library (15 min) 【Act 1 · The hardware store】

The class brings in the same reinforcement together, one full pass of four steps:

```text
① Search — find it in the hardware store
② Check — the three checks (projected the whole time, look up anytime)
③ Install — bring it into this project's tool room
④ Run — run the example it ships with
```

When the example runs and the compile flies — pause one second: what you brought in is a **pre-compiled, ready-made product** — the second benefit of reinforcements.

**Three checks before calling in a library (2 of 3 pass — bring it in):**

```text
① When was it last updated? (Nothing in three years — think twice.)
② Does it have examples? (No examples = no manual.)
③ Is it documented completely?
(Fourth check, for when something breaks: is my board on the
supported-hardware list?)
```

### Step 3: The tool room + the import trade-off (20 min) 【Act 1 · The hardware store】

Every project has its own **tool room**: one room catches fire, the one next door doesn't.

Then the most important lesson of the day: **importing a library is a trade-off decision — not a default move.**

- Case one: a complex sensor, a hundred lines to write yourself — **import**;
- Case two: blink an LED three times, three lines done — **don't import**.

Unsure? Ask three questions: **① does it help the core feature ② can I get it working today ③ what happens if I don't.**

**Two disciplines: circle exactly 1** (greed is this lesson's most common disease); **not importing is as right as importing** (write the reason clearly, pass review the same way).

Then send the **selection advisor prompt** (the conversation you already have — don't open a new one):

```text
This is my requirements sheet's core function: ______.
The board I'm using: ______.
Be my selection advisor: recommend 3 external libraries that might help,
one line each — what it does and why it fits me — ranked by fit.
Reminder: only recommend libraries that really exist and support my board.
```

It lists candidates; **you circle 1.** Watch out: AI will invent things with a straight face — only what the hardware store actually has counts.

### Step 4: Wire it into the project (25 min) 【Act 1 · The hardware store】

The hardest step: **example code is not your feature.** An example = "a demo of what the library can do"; what you want = "my core feature." Two moves:

1. Ask AI "what's this code doing" — it's your **translator**, specialist in code not written for you;
2. Have AI reshape it to your need — send the **minimal-change prompt**:

```text
Building on our last round: I installed the library ______; its example
can ___ (one line).
My core function is: ______.
Reshape the example into my feature: change only the smallest piece first —
let it run, then I'll ask for the next piece.
```

**The pass line: installed + example running.** Anyone not done carries it into the second-half build.

Share-out close (one sentence each): which library I brought in, what it saved me; anyone not importing says "why I didn't" — **equal applause**. Big class: pair up, the teacher picks a few for the whole room.

### Step 5: The looks upgrade — make it look like something (20 min) 【Act 1 · The hardware store**

The code reinforcement is in the door, but your project is still "undressed." **An MVP has two faces: it works (the inside), and it looks like something (the outside).** Looks cost nothing and get printed nowhere — trash is the hardware store for looks. Four moves:

```text
① Give it a shell — a cardboard box, a takeout box, an old toy shell: it is what it is, so make it look like what it is
② Hold it still — tape, rubber bands, zip ties: wires don't dangle, demos don't wobble
③ Label it — marker the button names, tape an arrow: someone can touch it without reading a manual
④ Hide the mess — tuck the wiring into the box; only the "face" shows
```

One rule: **looks serve the demo** — it exists for a 30-second demonstration, never more than a third of build time. Scissors and knives live with the teacher — take on demand, return when done. Think one minute first: what could my project look like?

### Step 6: Leg-two stand-up (5 min) 【Act 2 · Leg-two sprint】

First read your **baton handoff sheet** — what did last leg say the first thing this leg is? Then one sentence:

> **Today I'll get the core function to ______.**

Definition check: "done" is not everything you can imagine — it's **the core function on your requirements sheet**; anything beyond it gets pulled back. You may add half a sentence: "…and give it a ___ (shell/label)" — looks are optional; function is the required question. Small class — everyone stands and says it in turn; big class — pairs say it to each other + write it at the top of the sheet.

### Step 7: Build sprint + the quick shell (40 min) 【Act 2 · Leg-two sprint】

Rules carry over from leg one:

```text
One. Check against your requirements sheet — changing it is allowed, cross it out, don't erase.
Two. 15 minutes with no progress = raise your hand — stuck is not shameful; toughing it out silently is.
Three. Code questions go to your AI first — "one step at a time."
```

One addition today: **aily rusty? Flip your two-views cheat sheet** — it was written for exactly today.

**The last 10 minutes are the quick shell**: once the function runs, then the scissors — shell, still, label, hide; land as many of the four moves as you can.

**15 minutes before review, hands off everywhere** — prepare two lines: my project can now ___; it still can't ___.

### Step 8: AI review — this leg checks "sturdy" (15 min — the floor, never squeezed) 【Act 3 · Review & handoff】

Last leg's judges checked "does it look the part"; this leg's judges check "is it sturdy." The lead is an old friend — **Quinn**. Send this (the conversation you already have):

```text
Quinn, still you. Based on the current state: my project can ___ now,
and can't ___ yet.
You're a test engineer. Give me a 5-point "sturdiness checklist":
use it 10 times in a row? leave it alone 5 minutes, then touch it?
a different person tries it? press fast, press slow, press randomly?
— make each one specific: exactly how to operate it, and what to watch for.
```

⚠️ **Entrance condition: the conversation needs the BMAD team in it** — windows that already sent the background line in Lesson 8, send directly; a fresh window sends the background line first, then the prompt above:

```text
This conversation has a BMAD team: John (PM), Sally (UX designer),
Winston (architect), Amelia (developer), Quinn (test engineer).
Remember them — I'll call on them directly from now on.
```

All 5 items, **tested one by one** — note passed or broke.

Then the Picky User takes the stage (this leg: only 1 fault):

```text
You are now my real user (___). My project currently does: ___,
and still can't: ___.
No praise allowed. As them, pick only 1 fault — the single most lethal one.
```

⚠️ AI started praising? Push back: **"No praise. Faults only."**

### Step 9: Decide (12 min) 【Act 3 · Review & handoff】

Decide item by item: Accept or Reject, each with a written reason. Remember: **next leg is the sprint leg — fix only, add nothing** — whatever doesn't get fixed today goes onto the handoff sheet's "first thing next leg" with eyes open: that's your last chance to fix it. Accepting everything? The teacher will come talk — having no opinions is more dangerous than not changing.

### Step 10: The baton handoff sheet + the capstone close (10 min) 【Act 3 · Review & handoff】

Fill in the Leg-2 baton handoff sheet (template in Part 5). Then the capstone ceremony: nine lessons — light your first LED, find a topic, get a screen, get an AI team, teach hardware to see, move it home, brief the project, run the first lap, **and today — reinforcements called in: code and looks.** Your project's function is capped off, and for the first time, it has a look. Pause one second, and look at it.

---

## 5. Workbench · My Record (keep it in your own notebook)

> This document is shared and read-only — the blanks below, **record them in your own notebook, or say them out loud to your neighbor.**

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

## 6. When You're Stuck

| Stuck here | What to do |
| --- | --- |
| Library install error | Paste the error verbatim back to AI, one step at a time; AI can't solve it — raise your hand, escalate to the teacher. |
| Too many candidates, want them all | Stop — **circle exactly 1**. Anyone circling 3 gets sent back to re-circle. |
| AI's recommended library isn't in the store | It invents. Only searchable counts; can't find it — move to the next candidate. |
| No suitable library at all | Take the "no import" road: write clearly "why not," pass review the same way — as right as importing. |
| Example runs, breaks when reshaped to my feature | Fall back to minimal change: one smallest piece at a time; when it runs, ask for the next. |
| 15 minutes, no progress | **Raise your hand.** Stuck isn't shameful; toughing it out is. |
| Addicted to the looks, function not done | Stop — function first, looks after. Quick shell only in the last 10 minutes; past a third of build time, the teacher pulls you back. |
| No materials / good shells all taken | Trash is the hardware store: the requirements sheet's box works / tape two cardboards together / even just tidying the wires counts. |
| The whole project crashed | Crash protocol: tell the teacher; within 15 minutes you get a shrink plan (cut to what can live). |
| The 15-minutes-before-review call | Hands off immediately, save the running state, prepare your two lines. |

---

## 7. Classmates Often Ask

**"What exactly is a library?"**
A toolkit someone wrote, tested, and gives you free. Bring it into your tool room — three lines of calls beat a hundred lines of code.

**"If I use someone else's library, is the project still mine?"**
Yes. An engineer's strength isn't writing everything alone — it's picking, installing, and adapting into your own. And every decision you command is yours.

**"I didn't import a library — am I behind?"**
No. Not importing is as right as importing — review checks the reason. "Why I didn't" written clearly earns the same applause.

**"AI says I did great — no changes needed?"**
Make it stop praising and pick faults only. A reviewer who praises you = a reviewer who didn't show up for work.

**"My project is ugly — what now?"**
Ask first: in a 30-second demo, can people tell what it is? If they can, that's enough — "looks like something" isn't pretty; it's "at a glance you know what it is, and you dare to touch it."**

---

## 8. Today's AI Log

As always, four lines:

```text
Today I made:
I got stuck on:
then:
next time I want:
```

Today the "made" line is mandatory, exactly: **I called in the reinforcement ___, it saved me ___; for looks I used ___ (material); the sturdiness checklist passed ___ items.**

The old truth: AI will invent things with a straight face — proofreading is your job. Today it holds two new posts: selection advisor + translator — whether the candidates are real and the changes are right, only you, the one in charge, can say.

---

## 9. Next Lesson Preview

**The final leg + the demo: My Project, My Story.** The sprint discipline is four words: **fix only, add nothing.** Bring your baton handoff sheet, your project, and the side of it you most want to show.

Today you said "it's better"; next lesson you say "**let me tell you about it**."

---

_Chaihuo Maker Academy M0 · Student Workbook v1 (EN) ｜ 2026-08-26_

_Derivation note: localized from the Chinese student workbook v2.1 (M0_学员文档_CFG-5_第9课_给作品请外援_v2.md), structure and anchors mirrored 1:1. All verbatim prompts (three checks, selection advisor, minimal-change, Quinn's sturdiness checklist, Picky User one-fault, BMAD background line, push-back prompt, Leg-2 baton handoff sheet, Leg-2 review record) copied word-for-word from the English teacher guide M0_EN_TeacherGuide_CFG-5_Lesson09_CallInReinforcements_v1.md Section 6. Terminology: Call in Reinforcements / the hardware store / the tool room / the three checks / the translator / trash is the hardware store for looks / the four moves (shell · still · label · hide) / looks serve the demo / sturdiness checklist / fix-only. Brandy's four-line spec and hardware prompt template from Lesson 8's workbook are referenced back implicitly through "the two-views cheat sheet"._
