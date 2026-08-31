# Lesson 7 · Brief Your Project (Student Workbook)

_Chaihuo Maker Academy · M0 — Zero-to-Hero Smart Hardware_

---

## 1. What You Walk Out With

Last lesson you moved your project into your own computer — from tenant to owner; in Lesson 5 you taught the board to recognize scissors, rock, and paper, and made it work once it recognized. Today, two big things: first half — hand your project to AI and your neighbor to "wreck as hard as they can," drag every fault into the open, and make a call on each one; second half — **your big project gets its official brief** — starting from the topic you put on the wall back in Lesson 2, written up as a requirements sheet you can start building from.

By the end of class, you'll have four things:

1. **A field-tested trouble list** — AI wrote the items, your neighbor tested them one by one; passed gets a tick, failed gets a note on exactly how it failed;
2. **A page of verdicts** — for every fault, Accept or Reject — your call — and the rejected ones you fixed on the spot;
3. **A requirements sheet for your project** — who it helps with what problem, the usage scenario, input/logic/output, exactly 1 core feature, and a "later" list with ≥1 item;
4. **A sticky note on the Brief Wall** — project name + one sentence of core feature, read out loud to the whole class.

Same way of working: **teacher asks + your real information + AI deepens → your own stuff.** Everything the teacher asks you to write goes in this document (md doc if you're on a computer, paper if you're handwriting) — handed in at the end — and the requirements sheet travels with you: Lesson 8's marathon starts with it.

---

## 2. Before Class: Hand In Last Lesson's Work

md doc → send the teacher the link; handwriting → send the teacher a photo. Not handed in? It gets noted — catch up before you leave today.

**Write here — check the box:**

- ☐ My Lesson 5 record is handed in (three-box sheet + log, md link / photo of handwriting)

---

## 3. First Half · Vision-to-Action Wrap-Up

### Step 1: Warm-up self-check — does it still know you?

Plug in your little eyes board, throw scissors. Recognized? Sit tight and wait for the next step. Not recognized? Think back to Lesson 5's attribution: light changed? seat moved? — quick rescue: in the light you have now, take 10 more photos and retrain. That's "fixing the data" — you all know how.

Didn't finish the link-up last lesson? Five minutes with a TA and the fallback prompt gets "scissors recognized → LED on" running, then join the cross-test as normal — **today's point isn't how pretty the work is; it's whether you can find faults.**

### Step 2: AI plays the tester — Quinn opens the trouble list

Remember Quinn — the tester who broke your Pomodoro timer in Lesson 4. This is Quinn's visual highlight moment. Send this to AI (replace the brackets with your own project):

```text
Quinn, my project: a board with a camera that can recognize scissors, rock, and paper.
When it sees scissors it lights the LED; when it sees rock the buzzer beeps; when it can't
recognize anything, everything stays off.
You're a picky test engineer. Give me 5 tests for "how to make it misjudge or fail,"
each one specific: what I should do, and what I expect to see.
For example: hand gesture in backlight? Hand only half-visible? Switching gestures fast?
```

Got the list? Don't rush to test — **curate it once:** too vague ("might be inaccurate") goes back for a concrete scene; unrelated to your project gets struck off. Keep at least 3 items you can actually try, and write them down.

The return prompt:

```text
Please rewrite item X as a concrete test: what action I do, in what environment, what I watch for.
```

**Write here:**

- ☐ My trouble list has ≥3 items, each one states "what I do, what I expect to see"

### Step 3: Testers for each other — swap projects, sabotage item by item

In your hands: your neighbor's board + the trouble list they wrote. Test each item for real; results go on their list: passed gets a tick, failed gets a note on exactly how.

Three rules:

1. Sabotage is **limited to "what you show it"** — no touching wires, no disassembling, nothing covered beyond the lens;
2. Found a problem — don't laugh at them; what you handed over is both a knife and a medal;
3. After you test theirs, they test yours — both sides must be written full.

### Step 4: Take the list back — verdicts, one by one: Accept, or Reject

Everything above is your project's list of sins. Now judge them one by one.

**Rejected? Fix it now. Three paths:**

- **Fix the data** — back to SenseCraft, photograph the scene where it broke;
- **Fix the logic** — have Codecraft change a condition, like "only counts if it recognizes it twice in a row";
- **Fix the threshold** — raise the confidence line from 70% to 85%.

Not sure which path? Send the failure to AI (advice is advice — **which path is still your call**):

```text
My model misjudges in ___ situation. Fix the data, fix the logic, or fix the threshold — which do you recommend, and why?
```

**Accepted? Write one line:**

> I know it fails when ______, and I accept it.

You made this call in Lesson 2 — today you make it more professionally.

**Write here:**

- ☐ At least 1 item rejected and fixed on the spot (the path I took: ______)
- ☐ Acceptance notes written for the rest

### Step 5: Log, first line

> Made: I had AI write the trouble list, my neighbor helped me find ___ faults; I fixed ___ and accepted ___.

---

## 4. Second Half · Briefing the Big Project

### First, listen to someone: Neil and Fab Academy

In class the teacher told an MIT story. Neil, the founder of Fab Academy, said:

> Learning to make is not about building what you can buy in a store — it's about building what you **can't** buy: for yourself, for people you care about. **A good topic grows out of your own experience** — it isn't copied off the internet.

Fab Academy students set their Final Project in week one, and for the next twenty weeks everything they do each week is another module for it — today, that's exactly what you're doing.

Past students, with skills close to what's in your hands, have built protective gear, homemade oscilloscopes, mountain communication links, educational satellites, soft robots, drones, hydroponic systems, homemade instruments — **not one of them a copied "cool idea"; every single one a real problem out of the maker's own experience.**

Neil's four notes — just remember them:

1. **A masterpiece means skilled, not grand** — a finished ordinary project beats an unfinished grand vision;
2. **Spiral development** — every lap ends with a running version; core feature first, then lap by lap;
3. **Modular** — cut it into small pieces; build and test each separately;
4. **Document as you go** — the documentation grows with the project. Your requirements sheet today is the first line of your project's documentation.

### Step 1: Back to the Project Wall — do you still love this topic?

In Lesson 2 you stuck up one sentence: I'm making a ___ for ___, because ___. Four weeks later, look at your own sentence.

Still love it? Back to your seat. Don't — or wavering? **You may change it. Changing today costs nothing; carrying a topic you don't love to Lesson 10 — that costs.** A new topic passes the three-question gate:

1. Do I truly not love it anymore, or am I just stuck?
2. **Does the new topic come out of my own experience** — who's it for? Can I say a real name, and name a time they were genuinely annoyed?
3. Can the boards in my hands build it?

All three answered — change. Can't answer — back to the original topic; if you're stuck, raise your hand and a TA walks you through. **Changing topics doesn't mean swapping in "a cool copied idea"** — if you change, change to a real problem from your own experience. Still undecided after 5 minutes? Come get a backup topic — ready-made, no shame in it.

**Write here:**

- My topic (confirmed or changed): I'm making a ______ for ______, because ______.

### Step 2: The PM talk — John takes the topic deeper

Summon your product manager John — a role you know. The opener **must carry your Lesson 2 real user's name** — a need without a real name is a fake need:

```text
John, my topic is "I'm making a (what) for (a real person's name),
because (the real problem they have)."
You're my product manager. Interview me and go deep:
1. In what situation does this problem happen? When did it last happen?
2. Without this thing, how do they get by right now?
3. When and where will they use the thing I make?
When you're done asking, organize my answers into three sentences.
```

Note John's first follow-up question: "When did this last happen?" — **a specific day means a real experience**; no day means the topic is still just an idea.

**Old discipline: keep going in the conversation you already have — no new windows.** One new conversation and every conclusion so far is gone.

**Write here:**

- John's three sentences (copy them down):
  1. ______
  2. ______
  3. ______

### Step 3: The UX talk — Sally writes the usage scenario

```text
Sally, based on the previous round: (paste John's three sentences).
You're my experience designer. Write me a "usage scenario":
who uses it, where, how they use it, and how it reacts. Use a specific
person and place, no more than four sentences. Then tell me:
what does this thing look like, and where does it live?
```

The teacher's example looks like this: "Mom walks past the coffee table; it's been two hours since the water cup moved, so it flashes three times and gives one soft ding." — **a person, a place, an action, a reaction.** Write yours in that shape.

**Write here:**

- My usage scenario: ______

### Step 4: Fill the requirements sheet — your building permit

The sheet on screen is your big project's **building permit** — formal name, the requirements sheet (requirements.md). Before you build, "what it does" gets written down and locked. Three rules for filling it:

1. **Anti-drift** — from the marathon's start, check against it first, every time;
2. **It's alive** — changing it later is allowed, but strike through, never delete, so everyone can see you changed your mind;
3. **Three lines per section at most** — if it doesn't fit, it isn't thought through.

AI can help polish the wording, but the facts must come from your two talks just now — copy what AI invents, and you've given your project a fake household registration.

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

> 💡 **The engineer's same sheet:** professional engineers write this paper before starting too — Brandy (Seeed application engineer, built a voice keyboard with zero code) calls it the **input/output contract**: input / constraints / output / success criteria — four lines. Map it against your sheet: your real user = who it's for; your usage scenario = her use case; your input·logic·output = her input and output; your core feature + what counts as success = her success criteria. **She calls it a contract; you call it a requirements sheet — it's the same thing.** Every new module you take on from now on can start with those four lines.

### Step 5: The Scope Killer — exactly 1 core feature survives

Send the sheet to AI and summon the "Scope Killer" — it may ask only one kind of question, and **the veto is always yours**:

```text
This is my requirements sheet: (paste the whole thing).
Act as the "Scope Killer": for every feature I wrote, ask me only
"Would it die without this?" — one at a time, one question each.
Don't decide for me. I make the final call on what gets cut.
Whatever gets cut, organize into a "later" list for me.
```

Goal: exactly 1 core feature left. Whatever gets cut, copy it item by item into the "later" list, with the reason it was cut — **cut things keep their names; that's what makes it a real trade-off.**

**Write here:**

- ☐ Three sections done, core feature down to exactly 1: "______"
- ☐ "Later" list has ≥1 item, each with the reason it was cut

---

## 5. The Parts-Pool Tour — can what you wrote be built with what's on hand?

The tour isn't window-shopping. The task sheet has four items (projected the whole time), four rotating groups, 7 minutes per table, whistle to change:

```text
Four-table sort: Table 1 SENSE (sensors/cameras) ｜ Table 2 OUTPUT (lights/buzzers/screens)
                Table 3 ACTUATION (servos/motors) ｜ Table 4 MIXED

□ 1. Modules my sheet needs: ______ → found the real thing? (tick)
□ 2. Not in the pool: ______ → substitute: ______ (ask a TA, check the four-table sort)
□ 3. Discovery picks: touch one module you've never seen at each table, write its name + your guess
     Table 1: ______  Table 2: ______  Table 3: ______
□ 4. Back at your seat: fill the "hardware check" row and sign
```

**Discipline: not in the pool → find a substitute, or put it on the "later" list — change the need, not the purchase.** Today is look, touch, register only — drawing materials is Lesson 8's business, when the marathon starts.

**Write here:**

- ☐ All four task-sheet boxes ticked, "hardware check" row signed on the requirements sheet

---

## 6. The Briefing Ceremony · Close

Everyone takes one sticky note and writes two things: **your project's name, and its core feature in one sentence** — line up, and stick it on the Brief Wall. Read it out loud as you stick it.

The requirements sheet itself stays in your student document — that's your building permit; every marathon start, check against it first. The stickies on the wall are the whole class's reference: they can change, but **strike through, never delete** — let everyone see you changed your mind.

Remember this line: **it isn't just a graduation project — it's the start of a life project.**

**Log, four lines (as usual):**

> Made: my big project got its brief today — it's called ___, the core feature is ___, and I cut ___;
> Stuck on (mandatory): ______;
> Then: ______;
> Next time I want: ______.

---

## 7. Before You Leave: Delivery Checklist

- Requirements sheet + log + trouble-list verdicts go with you — md → send the link / handwriting → photo — hand in to the teacher after class;
- Board in the bag with your name on it; output pieces back in place;
- Changed your topic? Tell the teacher the new one.

Today you pulled off three things: **you wrecked your project for a full round — and it's still standing; you made a call on every fault — accept or fix, your verdict; and your topic went from a wall into a requirements sheet.**

**Next lesson preview:** **The Marathon · Leg One.** Bring your **requirements sheet**: draw materials, start building, stand-ups — and the AI Reviewer appears for the first time. Your project has a home now, and the sheet is on the wall — everything's ready. Run. Today you said "I want to build"; next lesson, you start saying "**I'm building**."

---

_Chaihuo Maker Academy M0 · Student Workbook v1 (EN) ｜ 2026-08-26_

_Derivation note: localized from the Chinese student workbook v2 (M0_学员文档_CFG-5_第7课_为我的作品立项_v2.md), structure and anchors mirrored 1:1. All verbatim prompts (trouble list + return prompt, PM talk, UX talk, Scope Killer, requirements-sheet template, tour task sheet, three-roads prompt, acceptance note) copied word-for-word from the English teacher guide M0_EN_TeacherGuide_CFG-5_Lesson07_BriefYourProject_v1.md Section 6 and Segment scripts. Terminology: Brief Your Project / the requirements sheet / building permit / the Scope Killer ("Would it die without this?") / the trouble list / fix the data · fix the logic · fix the threshold / the re-topic lane / backup topics / the Brief Wall / the briefing ceremony / change the need, not the purchase. Usage-scenario example kept as the teacher's "Mom walks past the coffee table" line. Names preserved: John / Sally / Quinn / Neil / Fab Academy / Brandy._
