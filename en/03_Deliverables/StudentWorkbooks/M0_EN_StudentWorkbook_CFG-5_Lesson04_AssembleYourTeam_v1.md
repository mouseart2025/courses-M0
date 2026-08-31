# Lesson 4 · Assemble Your Team: Build a Smart Pomodoro Timer (Student Workbook)

_Chaihuo Maker Academy · M0 — Zero-to-Hero Smart Hardware_

---

## 1. What You Walk Out With

Last lesson, your project got a face and hands. Today, you give AI a team — from "one sentence does it" to a whole crew that carries you from start to finish through one complete project.

By the end of class, you'll have five things:

1. **A running Pomodoro timer** — on your Wio, with focus, break, and reminders all working, and **one thing different from everyone else's**;
2. **A set of five-round relay phrases** — PM, designer, architect, developer, tester: all five opening lines are in this document, ready to copy;
3. **A method: BMAD** — open source, free, used by developers worldwide. Today it runs through your head once, end to end;
4. **An archive folder** — screenshots of the five rounds: the full record of the first complete project of your life;
5. **One AI log** — four sentences as usual, and today one line is mandatory: **where is my clock different?**

How this class works: **teacher guidance + this document + AI conversation → your own work and your own record.** Everything the teacher asks you to write, write here (in an md doc if you're on a computer, on paper if you're handwriting) — it's handed in at the end of class, and the next lessons build on it.

---

## 2. Before Class: Hand In Last Lesson's Work

Two things, done before class starts:

1. **Hand in your work:** md doc → send the teacher the link; handwriting → send a photo. Not handed in? It gets noted — catch up before you leave today.
2. **Keep your project manifesto and three-box design sheet within reach** — they matter today: at the tester round, the real person from your design sheet makes an appearance.

**Write here — check the box:**

- ☐ My last lesson's work is handed in (md link / photo of handwriting)

---

## 3. Why BMAD: Write-It-Direct vs Plan-First

You already know how to make AI build something from one sentence — fine for small projects. But these three things have probably happened to you:

- The code keeps growing; you want to add one feature and don't know where to tell AI to change;
- Halfway through, you realize you never thought it through at the start;
- You want a different color scheme and have no idea where the color lives.

That's not your fault — it's the ceiling of the "one sentence does it all" approach. In class we compared two ways:

| | Way A: let AI write directly | Way B: plan first, then write |
| --- | --- | --- |
| Result | It runs — and that's about it | The screen is designed, the structure is clear |
| Adding features | Gets messy fast, no idea where | You know where things go |

**Way B isn't a few extra tedious steps — it's letting AI help you think it through, in stages.**

### Meet BMAD: an open-source, free, professional way of working

This approach has a real name: **BMAD** (an AI-driven agile development method). Remember three things:

1. **Open source and free** — all its docs and code are public on GitHub; anyone can use it, zero cost;
2. **Developers worldwide use it** — a method professional teams maintain and keep updating, with a dozen-plus roles and thirty-plus ready workflows inside;
3. The one core move: **don't let AI do everything in one sentence — have it play different roles and think it through step by step before you build.**

The address is right here — check it yourself: https://github.com/bmad-code-org/BMAD-METHOD

**BMAD is not software to install. It's a method. Methods don't get installed — learn it, and it's yours.**

Later, when you want a full AI team set up inside a project on your own computer, no commands to memorize — **let AI install it**. Say:

```
Read the documentation at https://github.com/bmad-code-org/BMAD-METHOD
and configure the BMAD workflow in my project.
```

AI visits the GitHub repo and runs the install itself (needs a Node.js environment). Not today, though — today we use only the first way: install nothing, and run the five rounds below.

---

## 4. Your Team: Five Roles, All with Names

| Role | Name | Owns |
| --- | --- | --- |
| PM (Product Manager) | John | "what problem we're solving, who it's for" |
| Designer | Sally | "what it looks like, how you use it" |
| Architect | Winston | "how it's split into pieces, what states it has" |
| Developer | Amelia | "writing it" |
| Tester | Quinn | "finding what's wrong" |

What you used to do alone is now five experts sharing the work. **And you — you're the boss of this team.**

Before you use them, three rules:

1. **All five rounds in one conversation** — change roles, not windows; just call the name and assign the work, like giving tasks to colleagues. Open a new conversation midway and the previous conclusions are all gone;
2. **Every round opens with: "based on the previous round's conclusion"** — hand the previous round's result to the new role. This is a relay race — don't drop the baton (round one has no previous round, so start from your own problem);
3. In the conversation, the same Five Rules as always: one thing at a time, say the input and output, give it an example, if it's wrong add a line, ask it to explain.

---

## 5. Kickoff: The Pomodoro + "One Thing Must Be Different"

Pomodoro: 25 minutes of focus, 5-minute break, repeat. That simple. Today everyone builds one — on the Wio in your hand, with this team.

But there's one rule — **your Pomodoro timer must have one thing different from everyone else's.**

Not "mine is blue" — that's not it. It has to grow out of your life: do you space out doing homework? Do you need to time your piano practice? Are you building one for your little sister?

A secret: AI gives everyone the same default answer. **The details of your life are the part it can't give you — that's what makes your clock worth something.**

(Whatever goes on screen: English, numbers, or graphics only — the board's Chinese font is unreliable, so we never gamble on Chinese rendering.)

---

## 6. The Five-Round Relay: Build Your Pomodoro Timer

All five opening lines are right here — copy them, fill in your own content. **The phrases give the structure — you fill in the content. Blank brackets can't be sent.**

### Round 1 ｜ PM · John: decide what you actually want

The PM doesn't rush to build — first, ask. Today the one being asked is you: what's my real focus problem?

```
John, I want to build a Pomodoro timer for this problem:
(one real thing from your life — e.g. I pick up my phone within 10 minutes of starting homework)
First ask me 5 questions to understand what I need, then help me write down:
the 3 things this clock must do. Don't write code yet.
```

John will ask you a few questions first — answer honestly, don't get impatient. This is you thinking it through, not you getting a thrown-together answer.

Three reminders:

- Among the 3 things he gives you, **your "different thing" must be one of them.** It's not? Push back: "I haven't told you my special requirement yet — what should the clock do when I space out?"
- List getting bloated (every feature wants in)? Close it with one professional line: **"Too much. Keep only P0."** (P0 = what the first version must have.)
- Torn between problems? Pick one, any one, and build it — once you've built one, you'll know how to build the second.

**Write here: the 3 things my clock must do** (star one of them — that's my differentiator)

> 1. ______________________________
>
> 2. ______________________________
>
> 3. ______________________________

### Round 2 ｜ Designer · Sally: design what it looks like

Same opening line as always — based on the previous round's conclusion. The "position, size, color" language you practiced last lesson: today you organize it into the request yourself:

```
Sally, based on the previous round: my clock must do these 3 things: (copy them).
Design:
1. what the focusing screen looks like;
2. what the break screen looks like;
3. what buttons A, B, C each do.
My special requirement: (your differentiator) — it must show on the screens. Don't write code yet.
```

Anything you don't like, tell her directly — "make the time digits bigger" "switch to a dark background."

**Write here:**

> Focusing screen: ____________________
>
> Break screen: ____________________
>
> A button ________ B button ________ C button ________

### Round 3 ｜ Architect · Winston: make the technical plan

Before we build, one thing from the teacher: **states.** You've seen a traffic light, right? Red, green — one light at a time, and it changes when time's up. Your Pomodoro timer is the same kind of thing: it has several "looks", it's in one look at a time, and an action moves it to another look.

**Now, draw your clock's state circles on paper:** at least two circles — focus, break — and on the arrow write what changes it ("press A" / "time's up"). Can't manage three circles? Two circles are a complete Pomodoro timer. "Paused" is the most common third circle — add it if you want it.

Done drawing? Ask Winston for the plan:

```
Winston, your turn.
Based on the requirements and design above, make a technical plan for the timer — keep it simple,
Amelia will write the code from it.
```

**You don't need to understand the plan's details — it's not written for you. It's written for Amelia, who writes the code.**

**Write here (state circles go on paper, or two lines here):**

> My states: ____ → ____, what changes it: ____________

### Round 4 ｜ Developer · Amelia: build it complete, in one pass

The previous three rounds — requirements, design, plan — are all inside this one conversation. Amelia builds on them and delivers the whole timer in one pass:

```
Amelia, based on the requirements, design and technical plan above,
build the complete timer and give me code I can use directly.
For easy testing, set the work time to 1 minute and the break to 30 seconds first.
```

(Short times for easy testing today — once it runs, change them to your real 25 minutes.)

Got the code? Upload it. Get it running. Three reminders:

- **Got an error? Paste the error message back to Amelia verbatim — it wrote the code, it can fix its own code.**
- Upload not responding? Remember the desk mantra — **No response? Slide it.** (slide the side switch once, slide again, into flash mode).
- It runs? Ask for one more change of your own — a different background color, a little transition animation — that's **iteration**.

**Really stuck?** Raise your hand, get the **lifeline prompt** from the teacher, and send it to AI word for word — get the screen lit first, then have Amelia build the full features back on top of it:

```
My timer has two states: WORK and BREAK. Pressing A switches between them:
WORK shows a red background and "WORK"; BREAK shows a green background and "BREAK".
For now, only do this switching — no timing — using a simple if/else on the current state.
```

### Round 5 ｜ Tester · Quinn: break it

A test engineer's job is exactly one thing: **break it.**

```
Quinn, my timer is done.
Help me find fault: give me 5 ways to "break it", like rapid presses, or mashing buttons mid-timer.
I'll try each one myself.
```

Break-it list done? Then invite one special examiner on stage — the **Picky User.** Have AI play the real person from your design sheet, and pick exactly one fault:

```
Play ___ (the real person from your design sheet) and use my Pomodoro timer.
Pick 1 fault. Only 1.
```

For every method you try, for every fault you hear: make a call. **Accept or Reject?** Rejected → have AI fix it. Accepted → write it down under "I know it has this little quirk" — that's a professional decision too. And don't fix bugs forever: **fix the most important one; the rest go on the "do later" list.**

**Write here: the 5-item break-it list, each with Accept/Reject + one reason; the Picky User's single fault gets its own line**

> 1. __________ → Accept / Reject, because __________
>
> 2. __________ → Accept / Reject, because __________
>
> 3. __________ → Accept / Reject, because __________
>
> 4. __________ → Accept / Reject, because __________
>
> 5. __________ → Accept / Reject, because __________
>
> The Picky User's fault: ____________________

---

## 7. Wrap-Up: Three Things That Matter More Than Easter Eggs

### First: the archive — the full record of the first complete project of your life

Take one screenshot of each of today's five rounds — five screenshots into one folder, with your name and date on it. This folder is a treasure: later, whenever you wonder "what does a complete project look like," this is what you look at. Missed saving a round? Re-shoot it after class, and stick a note in the folder saying "added later."

### Second: transfer — is this method only for hardware?

This course's lesson plans were written by the teacher using these five people: the PM decided what each lesson solves, the tester poked holes in the plans. Your turn: writing a research report? Who's the PM there? The architect? The tester?

**Write here:**

> I could also use this method on ______________, where the PM would be ______________.

### Third: one line to close + today's log

**These five BMAD roles aren't a hardware method — they're a method for doing anything. Today, hardware is just the practice field.** You don't need all five roles every time — merge them for small works: **the size of the team follows the size of the project.**

Take one more look at the road you've walked — 10 years ago, "make an LED light up" counted as getting started; 5 years ago, "connect it to WiFi" was advanced; today, you — a total beginner — finished a complete project in one lesson, with a five-role team.

**Today's log: four sentences as usual — and one line is mandatory: where is my clock different?**

Step 1: **take a photo** of your Pomodoro timer (hands and board only).

Step 2: **speak for thirty seconds — all four lines:**

```
Today I made ______;
I got stuck on ______;
then ______;
where my clock is different: ______.
```

Step 3: **let AI tidy it — you proofread.** When you finish, send this to AI:

```
Help me turn this into a log — only what I said, nothing I didn't.
```

When it's done, **you must read it once before confirming** — AI will invent things with a straight face. Proofreading is your job, and nobody else's.

**Write here: today's log (the proofread version)**

________________________________________________
________________________________________________

---

## 8. Buffer Time: Pass the Bar First, Then Fly

There's a block of flex time at the end — the teacher announces how to use it:

1. **Catch up to the bar (everyone must pass):** if your timer's core isn't running yet, finish it — that's today's pass line;
2. **Easter egg challenges (for those past the bar):** decide "do it or not" first — two minutes, no agonizing:
   - **Flip-to-start timer** — flip the board face-down and the timer starts (this board can feel itself being flipped);
   - **Victory jingle** — 3 rounds completed in a row, and it plays;
   - **Break-screen joke** — the break screen shows one English one-liner;
3. **Help your neighbor:** mouth only — never touch their keyboard.

If an easter egg doesn't work out, it doesn't affect passing today — put it on the "do later" list. That counts as an achievement too.

**Write here (only if you attempted an easter egg):**

> My easter egg was ____________ — it worked / it didn't; it's on the "do later" list.

---

## 9. Closing: See the Road You Walked Today

On the whiteboard there's a map — eight boxes, the complete map of building a project. Today you personally walked the first six:

1. Get clear on who it's for and what it solves — the PM's job;
2. Find the real person — your Picky User;
3. Say what you want, break it into pieces — designer and architect;
4. Build it with AI — the developer;
5. Make it, try it, find faults — the tester;
6. Fix or tolerate, cut or keep — your "Accept or Reject" calls just now, and the easter-egg "do it or not," were exactly this step.

Boxes seven and eight only got started today: who to show the finished work to — you'll show each other; looking back after it's done — that's now.

**Write here: against the map, one line per box — "what I did at this step"**

> Steps 1–2: ____________________
>
> Step 3: ____________________
>
> Step 4: ____________________
>
> Step 5: ____________________
>
> Step 6: ____________________

Then take a sticky note, write "where I got stuck" — one step per note, sign your name — **and put it on the wall.** Today you got completely stuck, and completely unstuck, all on your own. Next time you're stuck — no panic.

**Show each other:** glance across the table — their clock: what's different from yours?

---

## 10. Today's Takeaways + Delivery Instructions

Today you earned three real skills:

1. **A method** — BMAD: have AI play different roles and think it through step by step before you build; open source and free, and the address is yours to verify;
2. **A team** — John, Sally, Winston, Amelia, Quinn — call them by name, five rounds of relay in one conversation;
3. **One complete work** — your Pomodoro timer, requirements to testing, walked end to end, with one thing on it that is unique in the world.

**Next lesson: Lesson 5 · Teach Your Hardware to "See"** — it will learn to recognize your face, your hand. Keep today's timer safe: it's your first complete work — not your last.

**Today's work gets handed in (pick one):**

- md doc → send the teacher the link;
- handwriting → send the teacher a photo.

The 3-things list, two screens + buttons, state circles, break-it list, archive folder, eight-step map check, log — handed in or not, the teacher notes it all down, and the coming lessons will use it. Don't lose it.

---

_Chaihuo Maker Academy M0 · Student Workbook v1 (EN) ｜ 2026-08-26_

_Derivation note: localized from the Chinese student workbook v2 (M0_学员文档_CFG-5_第4课_组团队做番茄钟_v2.md), structure and anchors mirrored 1:1; all verbatim prompts (five round openers, lifeline, Picky User, log-cleaner, BMAD install phrase) copied word-for-word from the English teacher guide M0_EN_TeacherGuide_CFG-5_Lesson04_AssembleYourTeam_v1.md Section 6. Chinese wiki links dropped (none in source); GitHub BMAD address kept. Localization: "给妹妹用的" → "for your little sister"; classmate references kept generic; on-screen text stays English/numbers/graphics per the no-Chinese-rendering rule._
