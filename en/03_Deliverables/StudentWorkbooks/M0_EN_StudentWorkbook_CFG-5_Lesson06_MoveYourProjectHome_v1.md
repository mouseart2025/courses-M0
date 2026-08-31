# Lesson 6 · Move Your Project Home (Student Workbook)

_Chaihuo Maker Academy · M0 — Zero-to-Hero Smart Hardware_

---

## 1. What You Walk Out With

From Lesson 1 until now, your works have come one after another — but they all live in the same place: someone else's server. Soon you'll give your project a charter and run a marathon — before that, today, one big piece of business: **the move.**

By the end of class, you'll have four things:

1. **A work living inside your own computer** — built with a new tool installed on your machine (aily-blockly), one project running, one you can touch with your own hands inside a folder: "it's here, and it's here to stay";
2. **A first taste of "reading code"** — you identified "this one block = these few lines," and you changed one line of code with your own hands (without breaking it);
3. **A brand-new project you commanded AI to build from zero** — the night-light, with the engineer's loop (state the need → build → check → upload → verify) run through end to end;
4. **A two-board linked system** — the dusk alarm station: the Beginner Kit as lookout, the Wio Terminal as alarm post, one signal wire joining them.

Plus a **new-home manual** (NLHD — link to a 15-chapter textbook) — from now on, when you hit something you don't know, open it.

---

## 2. A 30-Second Review

- In Lesson 5 you taught your hardware to see: first you ran a ready-made model, then trained one of your own;
- Your works used to live inside the Codecraft web page — you said it, it wrote the instructions for you;
- Five lessons in, your works keep coming and keep getting better.

Today's question: **close the browser — where is your work?**

Right at the open, the teacher runs a demo — watch closely:

- **Act one:** close the Codecraft tab — where's your work? With someone else. The site goes away, it goes away.
- **Act two:** open a folder — after class today, your work will be here. Unplug the internet, it's here. The site shuts down, it's here. Years from now, still here.

That's today's theme: **from tenant to owner.**

---

## 3. Today's New Words (in plain language)

**The move** — carrying your work out of the web page and into a new tool on your own computer. **Moving isn't a step backward — it's buying the house.**

**aily-blockly** — the name of the new home. Three sentences to know it: ① **open source and free**, official site yiyu.pro; ② **universal** — it welcomes 100+ different boards; switch boards later and it's still your home; ③ **AI-native** — state needs, wiring diagrams, code, error fixes — AI is in there the whole way. One line: **the old home helped you dare to build fast; the new home helps you truly finish.**

**A project (project folder)** — what a work looks like in the new home: a folder. Copy it away and you've taken it with you; send it to someone and you've shared it.

**The two views** — **two appearances of the same work.** The block view is for hands (drag and drop); the code view is for machines to read (lines of text).

**The archive** — broke something? Go back to the last version. That's why engineers archive all day long.

**The engineer's loop** — state the need → AI builds → check → upload → verify. Wrong? Say the need more clearly, run another lap. Every lap of the marathon runs it.

**The Grove cable** — the 4-wire cable used when two boards work together: yellow/white = signal, red = power, black = ground (GND). **One cable carries both signal and ground** — right port, seated firmly, and it works. Don't add a second ground wire.

---

## 4. Today's Flow

### Step 1: Installation close-out (homework, done before class)

The tool install is **homework** (installer + screen-recording tutorial sent to the class group). The first 10 minutes close it out:

```text
# Install self-check (check out loud)
□ Installed (double-click the icon, it opens)
□ Opens (the interface shows up)
□ Found the projects folder
□ Tried connecting a board and flashing
```

⚠️ Not installed? **When close-out time is up, the class moves on — no on-the-spot installs.** Pair up with your neighbor directly: they drive, you command. Give your name to a TA — 10 minutes after class, guaranteed taught. **Failing to install isn't embarrassing; toughing it out alone is.**

### Step 2: Tour the new home (12 minutes)

First, one glance at the new tool's board-picker — **the Grove Beginner Kit and the Wio Terminal are both in there**, plus 100+ more boards waiting for you to pick later. That's "universal."

Follow the teacher through three "rooms":

| Room | What it is | What you'll use it for |
| --- | --- | --- |
| The folder in the file manager | Where works live | Copy it = take it |
| The block view | Where dragging happens | Building features |
| The code view | Lines of text | Today's main course |

Whatever buttons there are, remember two today:

```text
① AI coding — tell it what you need in plain language; it writes code and fixes errors (today runs on it)
② Flash — click, and the program goes into the board (know what the "upload" button looks like)
Every other button — ask AI when you need it. It knows them better than you.
```

### Step 3: Put an old favorite on the shelf (15 minutes)

First thing after moving in: set out the most precious old thing — **redo "show your name on screen" on the Wio Terminal.**

Don't roll your eyes. How long did it take you in Lesson 1? Today we time it — the teacher bets you won't need half. **This isn't repetition — it's watching, with your own eyes, how much better you've gotten.**

Then the most important step (the ritual is called **"confirming ownership"**):

> **Save → open the folder → see with your own eyes that "it's there."**

From today on, every work of yours goes through this step.

### Step 4: The two views, three moves (30 minutes)

**① Find a match:** go back to the block view, drag one block — what changed on the code side? **This one block is those few lines.** Find one match, and you graduate today.

**② Ask AI:** select a chunk of code you don't understand (not the whole file), send it in the **conversation you already have**:

```text
(select a code chunk, send in the conversation you already have)
What's this code doing? Explain in plain language I can understand — two or three sentences max.
```

**③ Change one line:** find the line that displays your name, **change only the text inside the quotes** — make it your nickname — and run it.

⚠️ The boundary: **only the text inside the quotes — don't touch the quotes or the brackets ❌.** Broke it anyway? Don't panic: go back to the previous version (that's the "archive").

### Step 5: The new project — the night-light (30 minutes, run it solo)

Today's new project uses the **Grove Beginner Kit**: the light sensor and the LED are both already on the board — **zero wiring.**

Send this to AI (**the conversation you already have — don't open a new one**):

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

**Today's four steps** (run them solo — the teacher circulates, doesn't lead):

```text
1. Send the 6.4 prompt with your need → read what AI explains first; point to the light sensor and LED on your board before you build
2. Build + upload (paste errors back verbatim, one step at a time)
3. Open the serial monitor: normal ___ / hand over it ___ → put the threshold back into your need, have AI use your number
4. Iterate one lap: change the threshold / add "when dark, the buzzer also beeps" (pick one)
```

⚠️ Discipline: **paste errors back to AI verbatim, one step at a time — no silent trial-and-error on your own.**

Done early? Speed challenge: upgrade the need — "when dark, the light fades in slowly (a breathing effect)"; or read ahead to the joint project and think about how the two boards connect.

### Step 6: The joint project — the dusk alarm station (45 minutes, run it solo)

One board understands nightfall. Now make **two boards** work together:

```text
The dusk alarm station: two boards, two programs, one wire linking them

  Grove Beginner Kit (the lookout)            Wio Terminal (the alarm post)
  light sensor watches the sky → when dark:   watches the signal pin:
  · lights its own LED                        · sees the hand → screen "It's dark!" + beep
  · "raises its hand" on the signal pin (HIGH)· no signal → screen "All clear"
         │                                        ▲
         └──── signal wire (agreed pin → agreed pin) ────┘
              + shared ground (GND → GND — no shared ground, no link)

Joint three steps (run solo):
1. Send part one: split the job, ask for the wiring explanation (no code yet)
2. Send parts two and three: generate and flash each program separately — run each board solo first
3. Link and verify: cover the light sensor, watch the alarm post — dead link? run the three checks
   (did each board run solo? / is the signal wire on the agreed pins? / is the ground shared?)
```

**The three checks:** did each end run solo ｜ is the Grove cable on the agreed ports at both ends ｜ **is it seated firmly**

The three-part prompt (send in order — **still the same conversation window**):

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

⚠️ Link not working? **Run the three checks:** did each end run solo ｜ is the Grove cable on the agreed ports at both ends ｜ **is it seated firmly**

### Step 7: Wrap-up + collect your manual

Four sentences to sum up today:

1. **It's yours** — the work lives inside your computer;
2. **You're not afraid of it anymore** — you identified one match and changed one line with your own hands;
3. **You know the loop** — state the need, build, check, upload, verify;
4. **And you can chain them** — two boards, two programs, one wire connecting them.

How a big project runs (the marathon's three legs): **get the requirement sheet standing first → grow it feature by feature → link it all up at the end.** Today's alarm station was built exactly that way.

Collect the **NLHD manual link** — the new home's manual, 15 chapters:

```text
The new home's manual: Natural-Language Hardware Development (NLHD, 15 chapters)
https://github.com/ailyProject/Natural-Language-Hardware-Development
— every chapter drills today's loop. You don't need to read it today — open it when you're stuck.
```

---

## 5. Workbench · My Record (keep it in your own notebook)

> This document is shared and read-only — the blanks below, **record them in your own notebook, or say them out loud to your neighbor.**

```text
# My two-views cheat sheet
The match I found: this block ______ = these lines of code (copy a few words) ______
The clearest thing I got from "What's this code doing?": ______
The line I changed: was ___ → now ___ → result ___

# New-project record
Light reading on the serial: normal ___ / hand over it ___ → my threshold is ___
My need took ___ tries to say clearly

# Joint-project record
The lookout's hand pin is ___ | the alarm post knows because: ______
Our link's first failure was because: ______
```

---

## 6. When You're Stuck

| Stuck here | What to do |
| --- | --- |
| Tool not installed | After close-out, pair up: the neighbor drives, you command. Name to a TA — 10 minutes after class, guaranteed taught. |
| Can't find the projects folder | Click where the teacher clicks; found it — raise your hand. Paired students: the neighbor drives, you point things out. |
| "Redoing the first work is boring" | Time it: how long in Lesson 1, how long today? The difference is how much you've grown. |
| A screen full of English — scary | You don't need all of it. Find one "this block = these lines," and you graduate today. |
| Broke it changing the text | Go back to the previous version. Changing text can't really break it — be bold. |
| Upload error | Paste the error back to AI verbatim, one step at a time — no silent trial-and-error. |
| No serial data | Three checks: did the upload succeed / is the serial monitor open / is the sensor reading. |
| Link not working | Three checks: did each end run solo / Grove cable on the agreed ports both ends / seated firmly. |
| I want to change the logic (conditions, judgments) | Hold it in. Let it out when the marathon starts — by then you'll have the requirement sheet as your map. |

---

## 7. Classmates Often Ask

**"Can I still use the web version later?"**
Sure. The old home is a hotel for quick stops; the new home is your own house — know how to live in both.

**"Can I copy my work to a USB drive and take it home?"**
Of course — that's the whole point of the move. But hold off today; there'll be plenty of time before the demo day.

**"AI's wiring explanation — I can't read it. What now?"**
First ask it to "draw me a wiring explanation I can understand" (that line is already in the prompt); still lost, follow up with "which port sits next to which port" — ask until you understand, then wire.

**"Why run each end solo first, then link?"**
Because if two boards fail at once, you can't tell whose fault it is. Both running solo leaves only the wire — and the three checks catch that every time.

**"Is not being able to install it dumb?"**
No. Nine times out of ten it's a computer permissions problem, not a you problem. Pair up, learn everything anyway, catch up after class.

**"The new home's manual has 15 chapters — read them all?"**
No. It's a dictionary, not a textbook — when you're stuck, open the right chapter. Today you only need to know: you have it.

---

## 8. Today's AI Log

As always, four lines:

```text
Today I made:
I got stuck on:
then:
next time I want:
```

Today the "made" line is mandatory, exactly: **Today, guided by AI, I built ___, and linked it to another board.**

The old truth: AI will invent things with a straight face — proofreading is your job. Today it has a new title: your code translator + wiring advisor — but whether the translation is right and the wiring is correct, you still verify by hand.

---

## 9. Next Lesson Preview

**Give my project a charter.** A good topic grows out of your own experience — it isn't copied off the internet. You'll write a **requirement sheet**: input, logic, output — and the core feature cut down to one.

Charter in place, the marathon starts — today you said "I want to build"; soon you'll be saying "**I'm building**."

One last check before you walk out: the project folder is still in the computer — it sleeps there tonight, waiting for you to come back. That's what being the owner feels like.

---

_Chaihuo Maker Academy M0 · Student Workbook v1 (EN) ｜ 2026-08-26_

_Derivation note: localized from the Chinese student workbook v2 (M0_学员文档_CFG-5_第6课_把作品搬回自己的电脑_v2.md), structure and anchors mirrored 1:1. All verbatim prompts and projected blocks (what's-this-code-doing prompt, night-light prompt, three-part dusk alarm station prompt + division-of-labor diagram, two-buttons block, install self-check, NLHD link) copied word-for-word from the English teacher guide M0_EN_TeacherGuide_CFG-5_Lesson06_MoveYourProjectHome_v1.md Section 6. Terminology: aily-blockly / yiyu.pro / "from tenant to owner" / the two views / confirming ownership / the engineer's loop / the three checks / "It's dark!" + "All clear" on-screen text (English by design). Chinese links dropped; GitHub NLHD link kept._
