# M0 Student Workbook ｜ CFG-5 Semester Course · Lesson 3: Give Your Project a Screen (v1)

_Wio Terminal · HMI (Human-Machine Interface) board ｜ Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) ｜ Source: 中文版学员文档 v2（`交付物/学员文档/M0_学员文档_CFG-5_第3课_给作品装上屏幕_v2.md`）_

---

## 1. What You Walk Out With Today

Last session you found your topic. Today, new gear — from today on, your project has a **real interface**.

By the end of the session, you'll have four things:

1. **A "my Wio tour sheet"** — a walk around the new board + 5 "light-it-up" micro-experiments; however many you lit up with your own hands, that's how many boxes you tick here;
2. **Two new phrases** — one standard opener for making the board do things, one pro phrase for describing a screen — full text right here in this workbook;
3. **A screen-based interactive build** — the follow-along button counter + a two-screen switching project, plus one proud line describing your screen to AI;
4. **An AI learning log** — the same four sentences, but today's "stuck on" must be specific: was it position, size, or color?

Today's skill is still **build it** — except this time, the thing you build has a face and hands.

How today works: **the teacher guides + this workbook + conversations with AI → your own builds and records.** Everything the teacher asks you to write goes into this workbook (online doc or paper). It gets handed in after class, and it gets used in the lessons ahead.

---

## 2. Before Class: Hand In Last Session's Work

Two things, done before we start:

1. **Hand in your outputs**: online doc — send the teacher the link; handwritten — send a photo. Not in yet? It gets noted, and you finish before you leave today.
2. **Look at the Project Wall**: your manifesto is up there — it's the **north star** for every big project ahead. Keep your manifesto and three-box design sheet at hand. We won't touch them today, but don't lose them.

**Write here: tick the box**

- ☐ My last-session outputs are in (online doc link / photo of handwriting)

---

## 3. New Gear: The Wio Terminal, a Handheld Little Computer

It's called the **Wio Terminal** — think of it as a handheld little computer:

- **Big color screen** — your project's face: interfaces, numbers, graphics all live here;
- **Three buttons + a five-way joystick** — the human's hand: press, nudge — that's how people give your project commands;
- **Sensors built in** — it has its own ears and body.

### One thing different from the old board: the flash-mode switch

Before you flash, slide the switch on the side — **slide, slide** — that's how you tell the board "get ready for new instructions."

The mantra is one line, keep it on your desk: **No response? Slide it.**

### Warm-up: old flow, old line

Switch the board type in Codecraft — choose Wio Terminal, same old flow. Then send the line you've known since your first lesson (fill in your own name, pinyin or English):

```
I'm using the Wio Terminal. Please make this work: display in large text on the
screen: HELLO and my name (pinyin or English): ___
```

Wait for your screen to light up — **new hardware, and everything you already know still works. Nothing is wasted. And the letters are prettier now.**

(Why English on screen? This board's Chinese font library is unreliable — all screen display today is English, numbers, or graphics.)

### Walk around: meet your new partner

Follow the teacher: each time a part gets named, find it on your own board with a finger and touch it:

| Part | One sentence |
| --- | --- |
| Big color screen | your project's face: interfaces, numbers, graphics all live here |
| Three buttons | the human's hand: press, give commands |
| Five-way joystick | the human's hand: game consoles and menus run on it |
| Microphone | it hears things |
| Light sensor | it knows light from dark |
| Accelerometer | it knows whether it's moving, and which way it's tilted |
| Buzzer | it can make sound: reminders, alarms |
| SD card slot | it can store things — just know it exists |
| Grove port | the door for adding new modules later — just know it exists |

The last two are ears-only today. Can it go online? Yes — that's a later lesson; today just remember it exists.

Want to dig deeper after class? The official wiki is here (optional — not understanding it is fine):

- https://wiki.seeedstudio.com/Wio-Terminal-Getting-Started/

### Compare with the old board: a face and hands

The old board (Grove Beginner Kit) is good at **sensing the world** — sensors soldered on, plug and play. The new handheld adds a color screen, a joystick and wireless — it's good at **letting people interact with your project**. You'll use both boards — one to sense the world, one for people and projects to interact.

One sentence: **why change gear? From today, your project has a face and hands.**

**Write here (both lines):**

> Wio has ______________ more than the old board (at least three things)
>
> The first thing I want to make with it is ______________________

---

## 4. Light It Up: Five Micro-Experiments

Touching isn't knowing — **lighting it up is.** Five micro-experiments, one line each, watch it come alive. The rhythm: the teacher sends first, then you send — don't just watch, send a line and try it yourself.

Wrap every line in the standard frame (full text here — copy it as-is):

```
I'm using the Wio Terminal. Please make this work: …
```

### Micro-experiment 1 ｜ The three-key piano (buttons)

```
I'm using the Wio Terminal. Please make this work: press buttons A/B/C to play
do, mi, sol. Show DO / MI / SOL in large text on the screen.
```

Press it, and it answers you — buttons A, B and C are a little piano. Play a little tune? Raise your hand.

### Micro-experiment 2 ｜ Push the ball (joystick)

```
I'm using the Wio Terminal. Please make this work: draw a small ball in the
center of the screen. Push the joystick and the ball moves that way.
```

Nudge it, the ball obeys — see who can park the ball steadily in a corner. **Easter egg: the joystick presses down like a button too.** Whoever finds it, raise your hand.

### Micro-experiment 3 ｜ Blow out the candle (microphone)

```
I'm using the Wio Terminal. Please make this work: draw a lit candle in the
center of the screen. Blow at the microphone and the flame goes out;
after 2 seconds it lights again.
```

Blow on it, the candle goes out — the sound doesn't need to report numbers; getting the job done is enough.

### Micro-experiment 4 ｜ The board afraid of the dark (light)

```
I'm using the Wio Terminal. Please make this work: draw two open eyes on the
screen. When the light gets dim, close the eyes and show ZZZ; when it gets
bright, open them again.
```

Cover it, and it falls asleep — last session's dark-detecting light skill, played a new way.

### Micro-experiment 5 ｜ The balance ball (accelerometer)

```
I'm using the Wio Terminal. Please make this work: draw a square frame with a
small ball inside. Tilt the board and the ball rolls toward the low side.
```

Tilt it, the ball rolls downhill — shake detection and fall alarms both live here.

**Rhythm reminders**: one line lights one hardware point (the old rule: one thing at a time); a line won't run? Raise your hand, get another one — don't grind. Fast finishers: add one free line to the current toy ("change the ball's color", "beep when the ball hits the edge"); falling behind? Keep the first three solid — that's a pass.

**Write here: I lit up (one tick each) + one surprise**

- ☐ buttons　☐ joystick　☐ microphone　☐ light　☐ accelerometer

> What surprised me most was ______________, because ______________________.

---

## 5. Describing a Screen So It Comes Out Right: The Comparison Experiment

All the hardware is lit. Now the first lesson in using it well: **how to get a good screen out of AI.**

In class the teacher ran a little experiment — one request, two ways of saying it:

- Way one: just "make a counter screen" — AI plays freely;
- Way two: describe the looks — "show a number in the largest text in the center of the screen; show COUNTER in small text at the top-left; make the number red."

The difference? **When you describe a screen, say three things clearly: position, size, color.**

The screen phrase, full text right here — flip back whenever you forget:

```
At [position], show [content] in [size/color]; when [action], [change].
```

Example: show a number in the exact center of the screen in the largest red text; when I press button A, add one.

One more line, to keep it separate from last session: **describing logic** is "under what condition, do what"; **describing looks** is "what thing, in what place, looking like what." Two kinds of talking — learn both.

---

## 6. Follow-Along: The Button Counter (said in two steps — on purpose)

**Step 1 · Describe the screen only:**

```
Show the number 0 in the largest text in the center of the screen,
and COUNTER in small text at the top-left.
```

Flash. Look at it.

**Step 2 · Then describe the behavior:**

```
When I press button A, add one to the number; when I press B, reset to zero.
Every time the count reaches 10, the buzzer beeps once to celebrate.
```

Flash again. Count to 10 presses, and hear it applaud you.

**Looks first, then actions — two kinds of talking, sent in two steps, and it doesn't get confused.** Not right? Don't restart — add one more line and it learns. Buttons not responding? Remember the mantra on your desk — **No response? Slide it.**

---

## 7. Free Round: Make Something With Two Screens

The brief, one line:

```
Make something with two screens, switched by a button or the joystick.
```

Candidate topics: a clock / a mood display / a stopwatch / a custom menu / a reaction test (the screen turns green, you press A, it shows your milliseconds — naturally two screens). On-screen content in English, numbers, or graphics.

You now have five inputs — buttons, joystick, microphone, light, accelerometer — pick whichever feels right. Every toy you just lit up can move straight into your project.

**The old discipline**: first, **describe out loud to your neighbor** what each of your two screens looks like — position, size, color, all clear — then talk to AI. The sentence you can't say clearly is the exact sentence you'll be sending later.

Three reminders:

- **Directors shoot one scene at a time** — get screen one described beautifully, then screen two, and only then how they switch. Don't make AI do it all in one line;
- A dead button, text overflowing, a color that won't show — all of these are "add one more descriptive line" problems;
- Really can't get two screens? The passing bar drops to "the counter + one modification of your own" — write where you got stuck into the log, and it still counts as done.

**Today's bar (everyone must clear it)**: counter running + one two-screen project.

**Write here: the line I used to describe my screen to AI** (copy the one you're proudest of):

```
____________________________________________________________
```

---

## 8. The Drift Gallery: A Crash Isn't a Joke, It's Teaching Material

In class we all looked at one "treasure": an interface that drifted because of one badly-said line.

- He said: ___　→　AI made: ___　→　which sentence went wrong?

Finding the one wrong sentence is worth more than making a pretty screen — **a crash isn't a joke, it's teaching material.** The student who stepped in that pit for the whole class is a hero.

If the drifted screen was yours: no embarrassment — you already paid the class's tuition (the teacher's included).

---

## 9. Wrap-Up: Three Takeaways + Today's Log

Three takeaways for using this handheld well:

1. **Describe screens with position, size, color** — with or without those three, you get two different things;
2. **Make the state visible** — have the screen show "which step are we on", so you always know what it's doing;
3. **You have many inputs — try combinations** — good projects are often found by testing "which input feels most natural".

**Write here: circle one**

> The one I used most today was #___.

**Today's log — the four sentences don't change**, but today's "stuck on" must be specific: was it position, size, or color?

Step 1: **Take one photo** of your screen project (hands and board only).

Step 2: **Talk for thirty seconds — all four sentences**:

```
I made ________;
I got stuck on ________ (be specific: position, size, or color?);
then ________;
next time I want ________.
```

Step 3: **Let AI tidy it up — you proofread.** Send what you said to AI:

```
Tidy this into a learning log — only what I said, nothing I didn't say.
```

When it's tidied, **you must read it once before you confirm** — AI will make things up with a straight face. Proofreading is your job, and nobody can do it for you.

**Write here: today's log (after proofreading)**

____________________________________________________________
____________________________________________________________

---

## 10. Buffer Time: Clear the Bar First, Then Fly

The end of class has flex time — listen for which exit the teacher announces today:

1. **Finish to standard (everyone must clear it)**: haven't finished "counter + two-screen project" yet? Keep going and finish it;
2. **Challenge tasks (for those who cleared the bar)**:
   - **Electronic dice** — shake it (or flick the joystick), and the screen shows a random 1–6;
   - **Balance-ball hole-in-one** — add a target hole to micro-experiment 5; when the ball drops in, the buzzer beeps;
3. **Help your neighbor + add a link**: help your neighbor clear the bar (mouth only, hands off their keyboard); or add a sensor link to your two-screen project — e.g., when it gets dark, auto-switch to a night screen.

One iron rule: **everyone over the line first, then let the fast ones fly.**

**Write here (challenge-takers only):**

> I used ______________ (which input) to make ______________________ (what little thing).

---

## 11. Flash Show & Tell + Today's Takeaways + Handing It In

**Show & tell**: in your table, 30 seconds each — demo your project, and say one line: "which input I used, and how it switches screens."

Both of today's wins are real skills:

1. **You know your new gear** — the Wio has a screen, buttons and a joystick, and three sensors — and you lit every one of them up with your own hands;
2. **You learned to describe a screen** — position, size, color, all clear: your project has a real interface from today.

**Next session: Lesson 4 · Assemble Your Team** — AI stops being one helper and becomes a whole team working for you, and you run a complete project from end to end: your own smart pomodoro timer. The timer lives on this color screen — everything you practiced today gets used right away. **Bring your topic.**

**Today's outputs get handed in (pick one):**

- Kept in an online doc — send the link to the teacher;
- Handwritten — photograph it and send it.

Light-up checklist, two comparison lines, proud screen line, takeaways circle, log — collected or not, the teacher makes a note, and the lessons ahead will use them. Don't lose it.

---

_Source: 中文版学员文档 v2 ｜ English v1 (2026-08-27) ｜ Same terminology and phrase set as the Lesson 3 English Teacher's Guide (standard instruction frame / five micro-experiment lines / screen phrase / two-step counter)_

_Revision note: v1 (2026-08-27) derived from the Chinese workbook v2 and the Lesson 3 English Teacher's Guide — four-block structure kept (meet the gear → five micro-experiments → screen lesson + build → buffer + wrap), all prompt lines copied verbatim from the teacher guide's phrase library (directly copyable), flash-mode mantras kept ("slide, slide" / "No response? Slide it."), nine-point board tour (SD card slot and Grove port "just know it exists"), English wiki link only, six output anchors (hand-in tick / two comparison lines / light-up checklist + surprise / proud screen line / takeaway circle + log / challenge line), buffer's three exits and the standard bar (counter running + one two-screen project), screen display always English/numbers/graphics._
