# M0 Student Workbook ｜ CFG-5 Semester Course · Lesson 1: Sense and Respond (v1)

_Grove Beginner Kit · IoT Starter Board ｜ Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) ｜ Source: 中文版学员文档 v2（`交付物/学员文档/M0_学员文档_CFG-5_第1课_会感知会应答_v2.md`）_

---

## 1. What You Walk Out With Today

Today is the first time you make hardware obey you. By the end of the session, you'll have four things:

1. **A board with your name on it** — your name on the screen, lit by your own hands;
2. **Three little sense-and-respond builds** — one you made following the teacher, two you chose yourself;
3. **Your first AI learning log** — one photo, thirty seconds of talking, done in 30 seconds;
4. **A first look at the six skills this course trains** — spot a problem, find the user, build it, make trade-offs, judge quality, tell the story. Today we practice two: build it, and tell the story of how you built it.

One thing to be clear about up front: **today, all the code is written by AI. You write zero lines.**

Your job is only three moves: say it clearly, watch what happens, tell it to change.

---

## 2. Meet Your Board (Three Minutes)

The board on your desk is called the Grove Beginner Kit — its formal name is a **development board**. Think of it as a tiny computer. It's much dumber than your phone, but it can do one thing your phone can't: give it one job, and it'll do it all day, for a year, without complaining. It comes with a bunch of little parts already on it — no soldering, just plug in a USB cable and it works.

Meet it in plain words:

- 🧠 **The board in the middle** — its brain. Everything you say (through AI) becomes its to-do list.
- 📺 **The screen (OLED)** — its face. It can show text and numbers.
- 💡 **The LED** — it glows. The simplest kind of "expressing itself".
- 🔊 **The buzzer** — its voice. It goes "beep beep".
- 🌗 **The light sensor** — one of its eyes. It feels how bright or dark it is around it.
- 🎤 **The sound sensor** — its ears. It hears how loud it is.
- 🌡️ **The temperature & humidity sensor** — it feels hot and cold, dry and damp.
- 🏃 **The accelerometer** — it feels whether the board is being tapped or shaken.
- 🎈 **The barometer** — it feels tiny changes in air pressure. Pressure changes with altitude and weather, so it can "know" how many floors you climbed holding the board — and feel a weather change coming.
- 🔘 **The button and the knob** — the parts you operate it with.

Remember just this: **the top half of the board does the sensing, the bottom half does the expressing, and the brain in the middle does the deciding.** The one who decides what to do — is you.

One rule for today: the little modules on the board can be snapped off and used separately later — but not today. Snap nothing until the teacher says so.

---

## 3. The Three-Step Way of Working with AI

Everything you build today follows the same rhythm:

```
say it clearly → watch what happens → tell it to change
```

The teacher will lead the class in reading **two spells** out loud — they're printed on this page. Come back here whenever you forget them.

**Step 1: Say it clearly.**
Open Codecraft — it's a website. It's where you talk to AI, and where AI writes the instructions for your board. In the input box, tell AI what you want in one sentence. (That sentence has a name: a **prompt**.)

> **Spell 1: One thing at a time.**

This template is the safest way to say it:

```
I'm using the Grove Beginner Kit. Please do one thing for me: ________ (just one).
It counts as done when ________. Please don't add other features yet.
```

**Step 2: Watch what happens.**
AI turns your sentence into instructions the board understands — three words will run across your screen: **Generate** — AI is writing the instructions. **Compile** — it's translating them into what the board understands. **Flash** — moving the translated instructions down the USB cable into the board (once they're in, the board remembers — unplug it, still remembers). Then you look: is what the board did what you asked for?

**Step 3: Tell it to change.**

> **Spell 2: If it's wrong, add one more line.**

Don't delete the conversation, don't restart — just **add one more line** in the same conversation. AI remembers what you talked about.

### Small tips for writing prompts

- Say two things clearly: **when** (the condition) + **what** (the action).
  - Unclear ❌: "make me a light"
  - Clear ✅: "when the light gets dim, turn on the LED"
- One thing per prompt. Want three effects? Ask three times, one at a time.
- Effect not right? Follow up. Too sensitive, say "make it less sensitive"; not sensitive enough, say "make it more sensitive".
- AI is **guessing** what you mean — the clearer you say it, the better it guesses. It also guesses wrong, so Step 2, watching the result, is always your job.

---

## 4. Task 1: Light Your Name

**Goal**: get your name onto the screen.

**Prompt** (swap in your own name, send it to AI):

```
Display in large text on the screen: Hello, I'm ________.
```

Use your name in English letters — some boards show Chinese characters unreliably, so English lights up first, guaranteed. Want to try your name in Chinese? Go ahead — if it won't display, switch back to English. Nothing embarrassing about that; we'll teach it Chinese later.

**After sending**: wait for AI to generate → compile → flash. Hold up your board and look.

✅ **Your name on the screen — that's what "lit" means.** When yours is lit, raise your hand — the teacher will put a little flag on your desk.

**Want to play more?** Add one effect you want — blinking name, a beep when it appears, an emoji, make it scroll. One at a time, for example:

```
Make the name blink once per second.
```

```
Make the name scroll from right to left.
```

```
Make the buzzer beep once when the name shows.
```

Effect not right? Add one more line, like:

```
No — I want it to blink faster.
```

---

## 5. Mini-Lesson: Sense → Logic → Output

All of hardware, this whole semester, is one picture:

```
Sense → Logic → Output
```

- **Sense**: what it feels (the eyes, the ears)
- **Logic**: how it decides (this is your territory — your call)
- **Output**: what it does (the light, the beep, the screen)

Three examples:

| Thing | Sense | Logic | Output |
| --- | --- | --- | --- |
| Automatic door | sees someone coming | decides whether to open | door opens |
| Air conditioner | measures the temperature | compares — is it too hot? | cools, or stops |
| Your mom | sees you on your phone | decides whether to say something | calls you |

Your turn — think of anything around you that senses and reacts, and fill in its boxes:

| My example: ________ | Sense: ________ | Logic: ________ | Output: ________ |
| --- | --- | --- | --- |

The two tasks below both require you to say your own three boxes. **Say the boxes first, then build** — think it clear, say it clear, then it comes out built.

---

## 6. Task 2: The Dark-Detecting Light

**Goal**: make a little night light that turns itself on when it's dark.

First, tell your neighbor the three boxes: Sense = the light sensor, Logic = dark means on, Output = the LED.

**Prompt**:

```
When the light gets dim, turn on the LED; when it gets bright, turn it off.
```

**Play with it**: once it's flashed, cover the light sensor on your board with your hand — did the light come on? Let go — did it go off?

**Tune it**: the light in this classroom isn't the light at home, so yours might be too touchy or too slow. You don't need to change anything — just tell AI:

```
It's turning on too easily now — make it less sensitive.
```

```
It's not sensitive enough — make it more sensitive.
```

Tune until you like it. Every real-world sensor needs its "temperament adjusted" like this — it's normal operation, not a fault.

---

## 7. Task 3: Pick Your Own Sensor Combo

**Goal**: pick any one "sense" and any one "output" on the board, and combine them into your own build.

**Hard rule**: tell your neighbor your three boxes BEFORE you touch the keyboard. Can't say it? Then no keyboard.

**No ideas? Three ready-made options:**

1. **Clap light** — one clap, LED on; another clap, off.
   ```
   Use the sound sensor to detect a clap: one clap, the LED turns on; another clap, the LED turns off.
   ```

2. **Mini alarm** — the board beeps when shaken; only you know how to disarm it.
   ```
   Use the accelerometer to detect the board being shaken: when it shakes, the buzzer alarms and the LED blinks; hold the button for 2 seconds to disarm.
   ```

3. **Desk weather station** — the screen shows temperature and humidity live; too hot, it warns you.
   ```
   Show temperature and humidity on the screen in real time; when it gets too hot, make the buzzer give one short beep as a reminder.
   ```

**🚩 Challenge (if you're already done)**: use **two** sensors in one decision — like "only light up when it's dark AND there's a sound", or "only alarm when it's being shaken AND it's loud". Figure out your three boxes yourself first, then tell AI. Want something even bigger? Ask the teacher for a challenge card — a tiny game machine (whack-a-mole, a reaction-timer that scores), or turn your board into a game controller, using the button and knob to drive a game on the computer screen.

---

## 8. When You See Red Text

The more you build, the sooner you'll meet a wall of red text. Remember this first:

> **An error isn't a broken thing — it's AI talking to you.**

When red text shows up, do this:

1. **Copy the whole error**, all of it;
2. Paste it back into your AI conversation, with one line before it: "here's what I just changed";
3. Let AI tell you the likely cause and the first move.

**A model conversation**:

```
I just changed the LED to blink, and then compiling errored.
The full error text is pasted below:
[paste the red text here exactly as it appears]
Tell me the most likely cause, and the first thing to do.
```

Most of the time, AI can fix its own error once it sees it. What you're learning is not "never make mistakes" — it's **handing the problem to AI, precisely, after it happens**.

---

## 9. Your First AI Learning Log

From today on, every session ends with a 30-second little ritual: **one photo, thirty seconds of talking.**

**Step 1: Take one photo.**
Photograph today's build. The crash sites are worth photographing too — later on, these photos become the most precious pages of your build's growth story.

**Step 2: Talk for thirty seconds.**
Into your phone (or typed to AI), say these four sentences:

```
Today I made ________;
I got stuck on ________;
then ________;
next time I want ________.
```

"I got stuck on" is required. Didn't get stuck today? Then say: "It went too smoothly — now I'm worried about ________."

**Step 3: Let AI tidy it up — you proofread.**
Send what you said to AI:

```
Tidy this into a learning log — format: date / made / stuck on / next.
Only what I said, nothing I didn't say.
```

When it's tidied, **you must read it once before you confirm**. AI will make things up with a straight face — say things you never said, sounding perfectly real. Proofreading is your job, and nobody can do it for you.

Why bother with this? Other people graduate with one project. You graduate with a project **plus its growth story**. Competitions, interviews, reports — the growth story is worth more than the project.

---

## 10. Keep These Three Phrases — You'll Need Them Soon

No need to memorize them today — just get familiar. The next few lessons will use them one by one:

- **"What does this code do"** — want to know what AI wrote? Make it explain itself in plain language;
- **"Turn my logs into a README"** — the logs you're collecting become your project's introduction page at the end of the course;
- **"Explain it to someone who's never seen it"** — translate your project intro into words that someone who knows nothing about tech can follow.

What to build, and whether it's right — that's always your call. These phrases just help you say it clearly.

---

## 11. Next Lesson + One Small Thought

Next session, we do something even more important: **find the problem worth building all the way to the end.** Every good project grows out of a good question.

**One small thought — nothing to write down, just turn it over on your way home:**

> What small thing around you annoys you?
> At home, at school, on your way — what's something that needs someone running after it every day, or watching it every day?

Remember it. Next lesson, we start from there.

---

_Source: 中文版学员文档 v2 ｜ English v1 (2026-08-27) ｜ Same terminology and phrase set as the Lesson 1 English Teacher's Guide (spells / 3 boxes / generate-compile-flash / learning log)_

_Revision note: v1 (2026-08-27) derived from the Chinese workbook v2 and the Lesson 1 English Teacher's Guide — board module list complete (including the barometer), spells on-page, name-lighting in English letters, preview points to the "problem worth building all the way" framing._
