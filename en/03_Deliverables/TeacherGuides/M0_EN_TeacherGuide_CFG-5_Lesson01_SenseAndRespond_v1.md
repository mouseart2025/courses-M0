# M0 Teacher's Guide ｜ CFG-5 Semester Course · Lesson 1: Sense and Respond (v1)

_Grove Beginner Kit · IoT Starter Board ｜ Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) ｜ 10-session term ｜ 3 hours ｜ Source: 中文版 v1.7（`交付物/教师课件/M0_教师课件_CFG-5_第1课_会感知会应答_v1.md`）_

> **The one-sentence brief**: This is your first real session. By the end, every student has (1) their **name glowing on the board's screen** — no exceptions, (2) **three little sense-and-respond builds** (a dark-detecting light + two of their own choosing), and (3) **their first AI learning log**. You don't write code, you don't fix hardware, and you don't answer technical questions — you run the flow and say the scripts.

---

## 🎯 Learning Objectives

_By the end of this session, students will be able to…_

1. **Explain** what this course is in one sentence: "I'm the director, AI is the programmer." *(Bloom: Explain)*
2. **Describe** any smart device using the **Sense → Logic → Output** model, and name the three parts for their own build. *(Bloom: Describe, Name)*
3. **Use** the two prompting rules — *one thing at a time* and *if it's wrong, add one more line* — to make their board do what they want. *(Bloom: Apply)*
4. **Produce** a first AI learning log with four sentences, and check it for accuracy. *(Bloom: Produce)*

---

## 📋 Page One: The Last Look Before You Walk In

### What today produces

Three things, every student:

1. **Their own name on the board's screen** (everyone, no exceptions);
2. **Three sense-and-respond builds** (dark-detecting light + two self-chosen combinations);
3. **Their first AI learning log** (one photo, 30 seconds of talking).

You run four segments: **Kickoff** (30 min — what this course is) → **Name Lighting** (30 min — everyone lights their name) → **The Sensor Trio** (115 min — three builds) → **Wrap & preview** (5 min). No scheduled break — students use the restroom whenever they like while they work.

### The three things you need to know how to do

1. **Run the flow**: follow the timetable in this guide, segment by segment. Every segment says how long and what to do.
2. **Say the scripts**: every 🗣️ line in this guide is written out word-for-word. Read them as-is; don't improvise.
3. **Say one sentence when a student is stuck**: *"Ask your AI first."* — this is the sentence you'll say most all session.

### The three things you do NOT need to know

1. **You do not need to know how to code.** All the code is written by AI — including your students'. You don't need to read a single line.
2. **You do not need to fix hardware.** When a device misbehaves, there's one move: **swap it** (swap the cable → swap the board → swap the computer). Spare boards live in the box. Swap, don't fix.
3. **You do not need to answer technical questions.** When a student asks "why does it do that?", the standard reply is: *"Great question — send that exact question to your AI and let it explain."*

### When something goes wrong

- Your live demo fails: **cut to the backup video within 30 seconds** and keep going (speed sheet in Section 5). **This is not an incident — the plan already accounts for it.**
- A student's device fails: swap the board, don't fix. If they can't light up within 10 minutes, swap — that's the standing procedure.
- You're stumped: smile and say *"Let's ask AI together."* **Admitting in front of students that you don't know is the best modeling this course does.**
- The speed sheet is in Section 5. One-line version: **swap, cut to backup, ask AI — the three moves.**

---

## 1. Before Class

### 1.1 One Week Before (do it once)

- [ ] **Test the classroom internet**: on any student machine, open `codecraft.seeed.cc` and run the full loop once — type a sentence → generate → compile → flash. **This is the foundation of the whole session. Do it yourself once; if it works, every later step has a plan behind it.**
- [ ] **Confirm student browsers**: recent Chrome or Edge (Safari / Firefox don't support direct browser flashing). Ask IT to upgrade anything too old.
- [ ] **Confirm student Codecraft accounts**: accounts ship with the hardware kit, sized to your enrollment. One week out, confirm headcount, then check the account sheet has enough (round up if undecided — better too many than too few). If accounts haven't arrived, ask in the teaching group — that's a supply-side matter, not yours. Once you have the sheet, copy the passwords onto a paper seat map and carry it on you.
- [ ] **Count hardware**: Grove Beginner Kits for every student + 2 spare boards + 1 instructor demo kit + a box of spare USB cables.
- [ ] **Backup demo video ready**: check `assets/` for `L1_开场演示_备份录屏.mp4`. If it's not there, record your own successful rehearsal (see 1.3, Rehearsal 1) and drop it in.
- [ ] **Materials (zero-print — everything on screen)**: sensor table-card content saved on the instructor machine for projection (see 1.4); account passwords transcribed onto a paper seat map, carried on you, handed out one-by-one at start; one name sticker per student (handwritten is fine, sticky notes work too).
- [ ] **Backup video on your machine**: copied from `assets/`, double-click plays, volume tested.

### 1.2 Same Day (arrive 1 hour early recommended)

One person needs ~50 minutes for the checklist below, so arrive an hour early. With a TA: hand them device checks and desk setup; you handle projection, the whiteboard, and the Rehearsal-1 demo. If time is really tight, **Rehearsal 1 is mandatory**; the other three can go.

- [ ] Projection test: open Codecraft on your machine — can log in, can compile.
- [ ] Device check: plug in every board once — power LED on, screen lights up → back in the box. Tag and remove any dead board immediately; don't leave it on a desk.
- [ ] Each desk: 1 kit, 1 USB cable, 1 marker (sensor table-card content is projected, no paper).
- [ ] Whiteboard, drawn **before you open the door**: the **8-step map** (Frame the problem → Find the user → Prototype → Code → Trade-offs → Test & judge → Document → Share the value) and the **3-box diagram** (Sense → Logic → Output, three empty boxes).
- [ ] "LIT" flags by the TA (homemade: sticky note + toothpick is fine).
- [ ] Backup video loaded on your machine, paused on the first frame.

### 1.3 Demo Rehearsals (leave 20 minutes; click through all 4 demos yourself)

You have **4 live demos** today. Run each one fully on your own machine before class — not just watch it, click it through.

**Rehearsal 1 ｜ Kickoff demo "3-sentence sound-and-light SOS" (used at start)**
The opening demo must be rock solid — no gambling on Chinese font rendering. Default plan: open Codecraft, run three rounds in front of no one — Round 1: type *"write a program that makes the Beginner Kit LED blink every 500 ms"* → generate → compile → flash → LED blinks. Round 2: in the **same conversation**, add *"while the LED is on, the buzzer beeps; when the LED is off, stop"* → reflash → sound and light sync. Round 3: add *"use Morse code to send a repeating sound-and-light SOS"* → flash → the board sends SOS continuously. Whole thing under 5 minutes. This demo never puts Chinese text on screen, so there's no font problem — that's exactly why it's the opener.
Backup: `assets/L1_开场演示_备份录屏.mp4`. **If that video doesn't exist yet, record this successful rehearsal on your phone right now and save it into `assets/` — this recording IS the backup.**
Live fail? Play the backup and keep going — **not an incident.**

**Rehearsal 2 ｜ Name-lighting demo (used ~45 min in)**
Type: *"Display in large text on the screen: Hello, I'm [your name]."* → generate → compile → flash → name on screen.
Backup: a spare instructor/TA machine logged in and standing by. Note: **the lighting step has no video version** — students must light a real board themselves; watching a video doesn't count as lighting. So the backup here is **spare equipment**, not a video. Total network failure: see the Section 5 speed sheet. Rehearse the English-name flow only (default: *Hello, I'm ___*); if students may want Chinese characters, test a few common family names (Wang, Li, Zhang, Liu, Chen) so you know the answer.

**Rehearsal 3 ｜ "Dark-detecting light" demo (used ~1 hr in)**
Type: *"When the light gets dim, turn on the LED; when it gets bright, turn it off."* → flash → cover the light sensor with your hand → LED on; release → off.
Backup: as above, spare machine standing by + keep a working project saved on your instructor machine so you can re-flash on the spot.

**Rehearsal 4 ｜ Error-handling demo (used after the first real error appears)**
Don't manufacture an error — the trio segment will produce one naturally. What you rehearse is the **move**: copy the student's full error text → paste into their own AI conversation → add *"here's what I just changed"*. Before class, deliberately type a ridiculous request (e.g., *"make the board fly"*) to make the AI refuse or error once, so you're familiar with the feel of "throwing the error back at AI."
Backup: if the whole class somehow produces no error (rare), project the "make the board fly" conversation from your rehearsal and run the teaching point anyway.
One extra step: have AI turn that error conversation into a "sample log", deliberately letting it add one thing you never said — screenshot it. You'll use it at ~1h40 in to teach "proofreading is your job."

### 1.4 Materials, in Three Buckets

**📦 In the starter kit (just count, nothing to buy)**

- Grove Beginner Kit, one per student + 2 spares + 1 instructor demo kit
- Spare USB cables and adapters box

**🛒 You bring (one stationery run, nothing printed)**

- No printing: sensor table-card content (below) on your machine for projection; account passwords transcribed on a paper seat map, carried on you, given out at start
- Name stickers, one per student
- Student computers (lab or BYOD, Chrome/Edge current), power strips / extension cords if outlets are short
- Large paper or whiteboard (for the 8-step map and 3-box diagram), markers, whiteboard pens, tape (the 8-step map stays on the wall all session)
- Sticky notes + toothpicks (homemade "LIT" flags)

**✨ Nice-to-have (zero impact if skipped)**

- One small desk lamp (for the "dark-detecting light" demo — dims the local light, more dramatic)

Budget note: everything you bring is one stationery run. Cheap.

**Sensor table-card content** (projected, not printed — it's the four-box module map):

> 🎧 **Sense (its eyes and ears)**: sound sensor, light sensor, temperature & humidity sensor, accelerometer, barometer
> 📢 **Speak (its voice and face)**: LED, buzzer, OLED screen
> 🎮 **Interact (how you operate it)**: button, knob
> 🧠 **Brain**: the main board in the middle

The full board photo ships with the course: `assets/L1_板子全貌图_Grove Beginner Kit.png` — project it. **No photo? Fine.** Hold up a real board and point at it; that's even better.

---

## 2. Session Map

Sample timetable 14:00–17:00 — **shift the whole thing to your actual start time** (a morning class becomes 9:00–12:00; segment lengths don't change).

| Clock time | Segment | Students do | You do |
| --- | --- | --- | --- |
| 14:00–14:30 | Kickoff: what this course is | watch the demo, icebreaker, log in | demo, set the frame, point at the map |
| 14:30–15:00 | Name lighting: my name on screen | plug in, light their name, free play, look at each other's | guide connections, lead the follow-along, hand out flags, group photo |
| 15:00–16:55 | The sensor trio | follow-along dark-light + two self-chosen builds, mini show & tell, log | teach the 3 boxes, circulate, handle the first error, lead the log |
| 16:55–17:00 | Wrap: next-lesson preview | listen | preview Lesson 2 |

3 hours, no scheduled break — students use the restroom whenever they need, no reporting. You and the TA take turns breathing between rounds of circulating.

### 2.1 Time Buffer (Flexible / Non-negotiable)

- **Non-negotiable**: the opening magic demo (source of belief), name lighting (today's floor — cut anything else before you cut this), and the end-of-session log (the growth record is the backbone of this course).
- **Flexible** (can compress): the 8-step map (5 min → 2 min, just read the step names), the in-table show & tell in the free round (project only 1), and Build 3 (if time runs short, merge it with Build 2 into "one self-chosen build" — students still go home with 2+ builds).
- **Can end early**: the free round and Build 3 have natural finish lines — when everyone's done, move to show & tell. Don't stretch it.

### 2.2 TA Split (if you have TAs; no TAs? You can carry it alone, just circulate slower)

| Segment | TA A | TA B |
| --- | --- | --- |
| Kickoff | greet at the door, note icebreaker gold | final device check, watch for login issues |
| Name lighting | hand out "LIT" flags, handle serial-port issues | collect error-conversation screenshots, one-on-one with slow students |
| Sensor trio | circulate asking for the 3 boxes, give fast students challenge tasks | handle errors, take build photos (hands only, no faces) |
| Wrap | organize log archiving | sort today's photos, tick off the catch-up list |

---

## 3. Segment-by-Segment Scripts

### Segment 1 ｜ Kickoff: what this course is (14:00–14:30)

> Goal: by the end of these 30 minutes, students know this course is not about learning to code — it's about learning to make AI turn your ideas into real things — and they've seen "talk like a human → hardware comes alive" once, live.

**14:00–14:03 ｜ The magic demo: three sentences, sound-and-light SOS** [I Do]

**Say this:** (say nothing at first. Students sit down; you walk to the projector, open Codecraft, and type in front of the whole class so everyone sees the plain language going in —) *"Write a program that makes the Beginner Kit LED blink every 500 ms."* (Send. Wait for generate → compile → flash — the LED blinks. Don't stop. In the same conversation, add:) *"While the LED is on, the buzzer beeps; when the LED is off, stop."* (Reflash — sound and light are synced. Add one more line:) *"Use Morse code to send a repeating sound-and-light SOS."* (Flash. Pick up the board and point it at the class as it sends SOS. Wait for the recognition — the laughter and the "ohhhh" are the point of this segment.)

**Watch for:**
- The key is **plain language first, then send** — students must see the input is everyday talk. Never pre-build the project and just click run — they'll suspect it's staged.
- The three lines build **in the same conversation** — this is the silent first demo of "if it's wrong, add one more line", which students will realize the teacher did from the very start.
- Nothing Chinese ever goes on screen. No font roulette. This demo runs on any board anywhere.
- Demo fails: cut to the backup recording within 30 seconds; script in Section 5.

**Pitfalls:**
- Flash stuck/failed: glance at the clock, count to 30, then switch to the recording. As you switch: *"The board in this video is identical to the ones on your desks — you'll do the real thing yourselves in a minute."*
- A student heckles "will AI take our jobs?": one line only — *"AI replaces people who don't use AI. This course is how you become one of the people who do."* No debate, smile, move on.

**Say this (the landing explanation — 30 seconds, don't skip it):** (Sound stops; while it's hot, make sense of it.) *"What just happened? Let me say it once. I'm on a website called Codecraft. I told AI in three plain sentences what I wanted. AI wrote it out as instructions the board understands — that stuff is called code. Once, a person had to type every line by hand; today it typed them for me. Then the computer moved the instructions through this cable into the board — that step is called flashing. Once it's in, the board remembers — even unplugged. I wrote zero lines of code. Three sentences, and it's sending a distress signal."*

**Watch for:** these 30 seconds are the most important "landing" of the whole session — without them, students remember "the teacher does magic"; with them, they remember "I can do this too." Codecraft, code, and flash all appear for the first time today. They'll come back all session. First mention must be clear.

**14:03–14:06 ｜ Self-intro + three questions** [I Do]

**Say this:** *"I'm [your name — use what students call you]. I'm running this course with you from today. Three questions first. Number one: did I just write any code? (pause two seconds) Number two: who in this room knows how to code? (pause — probably no hands) Number three: without knowing a single line of code, could you make that thing I just made? (pause again — let the word 'yes' come out of their mouths) Yes. That's this course."*

**Watch for:** the pauses between the three questions are the soul of this bit. Don't rush. Let the answers come from them, not from you.

**14:06–14:11 ｜ Three "nots", one "is"** [I Do]

**Say this:** *"Let's be clear about what this course is not. One: it's not a programming class — we don't quiz syntax, and you never have to memorize a line of code. Two: it's not an assembly class — there's no step-by-step diagram to follow; what you build, you decide. Three: it's not AI doing everything for you — what to build, who it's for, whether it's good: that's all your call. AI is just your new colleague. So what IS it? In one sentence: you're the director, AI is the programmer. You think and you call the shots; it writes the code. This course trains the director in you."*

**Watch for:** "you're the director, AI is the programmer" will come back all session — every time, point at the students, never at yourself.

**Say this (three house rules, 30 seconds):** *"While we're at it, three house rules. One: you don't need to understand the code AI writes — your job is to say it clearly, watch what happens, and tell it to change. Two: no hand-written code — not because code doesn't matter, but because this course trains something more valuable than code. Three: when you're stuck, say so — ask your AI first, then your neighbor, then raise your hand. Being stuck isn't failing; being stuck and being able to say exactly what's wrong — that's the real skill."*

**Watch for:** these three rules carry over to every later lesson verbatim. Learn them cold.

**14:11–14:16 ｜ The 8-step map (point only, don't explain)** [I Do]

**Say this:** (pointing at the 8-step map drawn on the whiteboard) *"A real project takes eight steps: frame the problem, find the user, prototype, code, make trade-offs, test & judge, document, share the value. Most people think AI only helps with step four — the code. Not this course: all eight steps, you learn to make AI your partner. Today we take steps three and four. After that, one step per session, until you've got all eight."*

**Watch for:** hard time-box: 5 minutes, **point at the map and read the names only** — don't expand any step. If it turns into a lecture, it drags; their confidence today comes from doing, not from listening.
- Local-example slot, see Section 7: when explaining Sense → Logic → Output you can use *[the automatic door — a sensing thing everyone in their town has seen]*.

**14:16–14:21 ｜ What this course trains** [I Do]

**Say this:** *"This course trains six skills: spot a problem, find the user, build it, make trade-offs, judge quality, tell the story. AI writes the code — these six, it can't do for you. Today we practice two: build it, and tell the story of how you built it."*

**Watch for:** keep it light, don't expand. All six will keep coming back, learned by doing.

**14:21–14:26 ｜ Preview + icebreaker** [I Do] → [We Do]

**Say this:** *"When this course is over, each of you walks away with a smart project of your own — one you defined, one you built — plus the full record of how it grew. Today is step one. First, let's meet each other: with your neighbor, 15 seconds each — 'the one thing I'd most like AI to do for me'. I'll go first — [I want AI to remind my mom to drink water → swap for your own real small thing, the smaller the better]."*

**Watch for:** the TA notes the good answers; you can quote them in later sessions ("last time X said they wanted AI to… — today we can actually do that").

**Pitfalls:**
- Dead silence, nobody speaks: you self-disclose one more, even smaller (*"I want AI to remind me to grab my keys when I leave"*), then call directly on the student you know best. Never let silence run past 10 seconds.

**14:26–14:30 ｜ Everyone logs in** [We Do]

**Say this:** *"Now — open your browser, go to codecraft.seeed.cc — the site I used in the demo. It's called Codecraft. It's where you talk to AI, and where AI writes the instructions for your board. Log in with the account on your seat card. Just log in — don't click around yet."*

**Watch for:** TA circulates handling login issues. **Before the next segment starts, login problems must be at zero** — wrong passwords get fixed against your paper seat map; accounts that truly won't open get flagged and fixed by the TA on a spare machine once the trio starts.

---

### Segment 2 ｜ Name lighting: my name on screen (14:30–15:00)

> Goal for this segment, and only this: **every single person's** name appears on their board. No concepts taught here — one job only: make each student believe *"I can make things."*

**14:30–14:33 ｜ The two spells (on screen)** [I Do] → [We Do]

**Say this:** *"Before we touch anything, two spells for talking to AI. (project spell one) Spell one: one thing at a time. Don't say 'set up the lights, the screen and the speaker all at once'. Say 'display my name in large text on the screen' — one thing, said clearly, and it gets it right. (project spell two) Spell two: if it's wrong, add one more line. The result isn't what you wanted? Don't delete the conversation, don't restart — just add one more line in the same conversation. AI remembers what you talked about. Both spells are in your Student Workbook too — check them whenever you forget."*

**Watch for:** read each spell once, then have the class read it back with you. This is the standard posture for all today's conversations.

**14:33–14:36 ｜ Meet your board + plug it in** [I Do]

**Say this:** (hold up a board, point as you go) *"Meet your partner. It has a formal name — a development board. Think of it as a tiny computer. It's dumber than your phone, but it has one thing a phone can't do: give it one job, and it'll do it all day, for a year, without complaining. It can't think for itself — the ideas come from AI, and the decisions come from you. This is the screen, the light, the little speaker — its face and voice. These little parts over here are sensors — parts that can feel things, its eyes and ears: this one feels light, this one feels sound, this one feels temperature. Today you're going to make it speak your name. Now — plug in the USB cable, one end in the computer, one end in the board."*

**Watch for:** 90 seconds max, **no theory**. Add one caution: *"The little modules on the board can be snapped off and used separately later — not today. Today nothing snaps."*

**14:36–14:43 ｜ Connect Codecraft (pitfall hotspot #1)** [I Do] → [We Do]

**Say this:** *"Follow me, step by step. Heads up — this step is called connecting. What's it for? Getting the computer and the board talking — the instructions AI wrote need to travel down this USB cable into the board. Step one: pick your board — click here, choose Grove Beginner Kit. Step two: click connect — the browser pops a small window asking permission; click Allow, then pick the row that says USB."*

**Watch for:**
- Project and lead the whole class in lockstep — **don't let fast students run ahead**. If a fast one connects early, have them wait; don't let the pack scatter.
- TA watches two things: the popup never appearing (usually a browser problem) and students clicking Deny by accident (just click connect again). This is the first pitfall hotspot — the rule for both is fix within 2 minutes, else swap to a spare machine.
- Serial list empty? Most common cause: the USB cable carries power but no data. Swap the cable — fixes it nine times out of ten.

**14:43–14:45 ｜ One rule: one thing at a time** [We Do]

**Say this:** *"One more pass at spell one: one thing at a time. Not 'set up the lights, screen and speaker'. Say 'display my name in large text on the screen'. One thing, said clearly, and it gets it right."*

**Watch for:** write this sentence in a corner of the whiteboard and leave it there all session. This is the standard posture for all today's conversations.

**14:45–14:53 ｜ Follow-along: light your name** [I Do] → [You Do]

**Say this (before the first flash — three new words, 20 seconds):** *"Three words are about to run across your screen. Meet them now. Generate — AI is writing the instructions. Compile — it's translating them into what the board understands. Flash — moving the translated instructions down the USB cable into the board. Once they're in, the board remembers. Unplug it — still remembers."*

**Say this:** *"Watch me once. (project, type slowly) 'Display in large text on the screen: Hello, I'm [your name].' Send. It writes it, compiles, flashes — (hold up your board) — lit. Your name — use your name in English letters. Chinese characters on this board are unreliable, so English lights up first, guaranteed; want to try Chinese? If it won't display, switch back to English and we'll teach it Chinese later. Your turn. Swap in your own name. When yours is lit, raise your hand — a TA will put a flag on your desk."*

**Watch for:**
- TA hands out "LIT" flags one by one as boards light. Flags make progress visible — and they keep slow students from feeling alone; they can watch the flags multiply.
- **10 minutes without lighting up → swap to a spare board, don't fix.** Swapping is the standing procedure, not a comment on the student.
- **You never type for a student.** You can dictate the sentence and let them type it — their hands, their success.
- Slow typer, or can't type: guide them to voice input, or write it on paper and have the neighbor type it (the words must be the student's own).

**Pitfalls:**
- A student insists on Chinese characters and gets mojibake/missing glyphs: (smile) *"It doesn't know that character yet — light it in English first, we'll teach it Chinese later."* Don't solve the font problem on the spot.
- Someone lights up and says "too easy, boring": immediately give them the fast challenge: *"Then try this — make the thing on screen move."*

**14:53–14:55 ｜ Group celebration: hold up your boards** [We Do]

**Say this:** *"Everyone — hold up your boards! (wait for the whole room) From this moment, you're people who can make hardware do what you say. Look at the camera —"*

**Watch for:**
- Compose the photo around raised boards and screens — the builds are the stars. Backs of heads and hand close-ups are fine.
- TA does one sweep first: anyone whose board is still dark gets helped to light it before joining the photo — **nobody photographs a dark board**.
- This photo is also log material and the end-of-course comparison shot. Take one landscape, one portrait.

**14:55–15:00 ｜ Free round: add an effect you want + show & tell in tables** [You Do]

**Say this:** *"It's yours now. Add an effect you want — blinking name, a beep when it appears, an emoji, make it scroll. Your pick. This is where spell two kicks in: effect not right? Don't delete, don't restart — add one line in the same conversation, like 'no, I want it to blink faster'. AI remembers what you said before. Keep going. (after ~3 min) Now look at your neighbor's — 30 seconds each: what effect did you add, and how did you tell AI?"*

**Watch for:**
- For slow students, three concrete options written on the whiteboard: *"make the name blink once per second" / "make a sound when the name shows" / "make the name scroll from right to left"*.
- Fast students do two effects, or take a fast challenge.
- TA quietly collects 2 screenshots of "broke it, then fixed it" conversations — for the show & tell projection.
- When projecting, **prefer the "broke it then fixed it" ones, not the flashiest** — the class needs to see that "fixing it back" is the normal, everyday move.
- **New pitfall: a student dumps the whole job on AI at once** (pastes a huge "do all of blinking, scrolling, sound and emoji"). Recovery script below.

**Pitfalls:**
- Student makes AI do everything at once: no scolding — walk over and say: *"Nice appetite. But directors shoot one scene at a time — pick one effect and make it solid, then shoot the next scene. One thing at a time — that's the rule."* Then walk them back to one thing. If they already got it all working, have them explain it to their neighbor in the 3 boxes (sets up the next segment), then give a fast challenge.
- A student deleted the conversation, restarted, and made it worse: no blame — demo live that "add one more line" is way faster than restarting.

---

### Segment 3 ｜ The sensor trio (15:00–16:55)

> Goal: students own the one hardware mental model of the whole course — **everything is Sense → Logic → Output** — and use it to build 3 things and say their own 3 boxes.

**Watch for:** in the first 2 minutes, the TA clears leftover login/device issues while you clear the whiteboard next to the 3-box diagram. Keep a mental list of fast students — they get the Build-3 challenges first.

**15:00–15:05 ｜ The 3-box diagram: the most important 5 minutes of the session** [I Do]

**Say this:** (pointing at the 3 boxes on the whiteboard) *"All of hardware, this whole semester, is one picture: sense, logic, output. Three examples. The automatic door: it sees someone — that's sense; it decides whether to open — that's logic; the door opens — that's output. The air conditioner: it measures the temperature, compares, cools. Third one — your mom: she sees you on your phone — sense; she decides whether to yell — logic; she calls you — output. (laugh) Now look at your board: eyes and ears on this side, face and voice on this side. The logic in the middle — that's your call."*

**Watch for:** give these 5 minutes their full due — but examples only, **no jargon**. Have the class read the six words back with you: "sense, logic, output."

**15:05–15:25 ｜ Build 1 (follow-along): the dark-detecting light** [I Do] → [You Do]

**Say this:** *"Build one, we do it together: a light that turns on when it's dark. Tell AI — 'When the light gets dim, turn on the LED; when it gets bright, turn it off.' Send, flash. Now — everyone, cover the light sensor on your board with your hand — (lights come on across the room, one after another) — look at that. A room full of night lights."*

**Watch for:**
- The cover-test is this segment's magic moment — make it happen together: *"Three, two, one — cover!"*
- Someone's light is sluggish (different classroom light): that's your teaching point. Walk over, loud enough for the room: *"It thinks your spot isn't dark enough. What do you do? Tell AI — 'make it more sensitive.'"* Let the whole room hear that line — that's spell two in action.

**Pitfalls:**
- Flash failure: run cable → board → machine, 2 minutes per step. The TA catches the student up privately — **never make the class wait for one person**.
- Cover test gets no reaction (sensor orientation, or the room is already dark): you cover your own demo board and show them the effect, then have students move to a spot with more light contrast (by the window / under a lamp) and try again.

**15:25–15:30 ｜ Name the pattern** [I Do]

**Say this:** (back at the whiteboard, fill in the 3 boxes) *"What did we just do? Sense — the light. Logic — dark means on. Output — the LED. Fill the boxes, that simple. Now you're going to fill the boxes yourselves — whatever you fill, you build."*

**15:30–16:00 ｜ Build 2 (semi-free): pick one sensor + one output** [You Do]

**Say this:** *"Look at the table card on your desk. Pick one sensor and one output — your combination. A clap light, a shake alarm, a heat alert… anything. One hard rule: **tell your neighbor your 3 boxes BEFORE you touch the keyboard.** Can't say it, can't code it — think it clear, say it clear, then build it."*

**Watch for:**
- The first question you ask while circulating is always: *"What are your three boxes?"* Can't answer? Use the analogy: *"In your build, which part is the automatic door's eye?"*
- **The moment the class's first error appears, stop the whole room for 1 minute**: project that student's screen, walk them through the correct error move — copy the full error + *"here's what I just changed"* — and throw it back at AI together. Then say to the class: *"See? An error isn't a broken thing. It's AI talking to you. It wrote the problem out — you just forward it back."*
- A sensor seems "dead" (noise, lighting differences): don't declare it broken: *"That's what a real-world sensor feels like. Want it more sensitive or less? Tell AI."*
- A student only stacks outputs with no sensor (a light show): *"Cool — now make it perform only when [some condition] happens."* Put the sense box back in.

**Pitfalls:**
- Student dumps everything on AI at once (one giant paste of three builds): same script as the free round — *"Directors shoot one scene at a time. Tell me the three boxes of this one build."*
- Slow student, 10 minutes stuck: move them to a follow-along spot next to you — target becomes "follow-along + one small change of their own." Still counts as done.

**16:00–16:40 ｜ Build 3 (fully free): make something that reacts** [You Do]

**Say this:** *"Last build. One-line brief: make something that reacts. What it reacts to, how it reacts — all yours. Wanted to upgrade your earlier build instead? Go for it."*

**Watch for:**
- Give fast students two challenge directions, pick one: ① **a tiny game** — whack-a-mole or a reaction-timer (buttons score, screen shows the score); ② **the board as a controller** — the board's buttons/knob drive a little game on the computer screen. Caution: **only release challenge directions you've rehearsed and run yourself** — a fast student crashing with no one to catch them is on you. Still fast? Make them the teacher: they explain their build to a neighbor using the 3 boxes; next lesson they officially TA.
- Students with no idea: three ready options — clap-light (one clap on, one clap off) / mini alarm (shakes → beeps; hold the button 2 seconds to disarm) / desk weather station (screen shows temperature, humidity, light; too dark → light on; too hot → beep).

**Pitfalls:**
- A student's build only "displays" instead of "reacts" (e.g., pure scrolling text): don't dismiss it — add one line: *"It can already talk. Now give it an eye — it only speaks when ___."*
- Students start copying each other: copying ideas is fine — **the 3 boxes must come out in their own words**; anyone copying the neighbor's build but unable to say the boxes goes back to "which part is the automatic door's eye?"
- Someone finishes early and starts wandering: give a fast challenge, or send them to help a slow student — helping means mouth only, hands off the other person's keyboard.

**16:40–16:55 ｜ Flash show & tell + the full AI log** [You Do] → [Share-out]

**Say this:** *"In your table: 30 seconds each — demo your build, say its three boxes. (after one circulation round) Now, today's log, four sentences to cover it all: today I made ___; I got stuck on ___; then ___; next time I want ___. Say it to your phone, then send it to AI with one more line: 'Tidy this into a log — only what I said, nothing I didn't say.' When it's done, read it. **AI will make things up with a straight face. Proofreading is your job.**"*

**Watch for:**
- First log ever: you model it first with your own four sentences — including where YOU got stuck. You show weakness first, and they'll tell the truth.
- Project 2 builds: the cleverest combination + one that was rescued after a crash.
- "What did you get stuck on" is a required field. Student says "I didn't get stuck" — reply: *"Went too smoothly? Then write down what you're worried about."*
- TA takes the build photos; students without phones (or no-phone classrooms) get photos taken by the TA, filed by table number.
- Someone accepts AI's log wholesale? Project the "AI got caught making stuff up" screenshot you prepared in Rehearsal 4 — and teach the proofreading responsibility on the spot. That's today's hidden bonus teaching point.

**Pitfalls:**
- Student grumbles about the log ("again?"): don't argue — point at their build: *"Everyone else graduates with one project. You graduate with a project AND its growth story — competitions, interviews, reports: the growth story is worth more than the build."* Still resistant? Floor requirement is "one photo"; the spoken part can be a voice note after class.

---

### Wrap ｜ Next-lesson preview (16:55–17:00)

**Say this:** *"Today's logs are all saved — that's the growth story of your builds. By the end of the course it'll be worth more than the builds themselves. Next time, we do something even more important: find the problem worth building all the way to the end. Start thinking on the way home — what's one small thing in your daily life that annoys you? Class dismissed!"*

**Watch for:** wrap fast — preview, then dismiss. Leaving them wanting more is the best way to end.

---

## 4. Live Demo Backup Plan at a Glance

| Demo | Used at | Rehearse | Backup asset | If it goes wrong live |
| --- | --- | --- | --- | --- |
| Sound-and-light SOS (3 sentences) | Kickoff (start) | Rehearsal 1 | `assets/` backup recording (record your own successful run on your phone and save it if none exists — mandatory before class) | Cut to the recording within 30 seconds, keep going — **not an incident** |
| Name lighting | 45 min in, follow-along | Rehearsal 2 | **No video version (by design: lighting must be a real board)**; spare machines + spare boards standing by | Swap to a spare machine and keep leading; total network failure → Section 5 |
| Dark-detecting light | 1 hr in, follow-along | Rehearsal 3 | Spare machine + keep a working project on your instructor machine for instant re-flash | Swap/refash; if still stuck, demo collectively with a board from a student who succeeded |
| Error handling | First error in the trio | Rehearsal 4 | The "make the board fly" error-conversation screenshot (prepared before class) | Project the backup screenshot; teach the point anyway |

---

## 5. Pitfall Speed Sheet

Remember the three moves first: **swap, cut to backup, ask AI.** Any device issue must reach a resolution within 10 minutes — and the resolution is always swap, never fix.

| Situation | What you do |
| --- | --- |
| Opening demo compile/flash fails | Cut to the backup video within 30 seconds: *"The board in this video is identical to yours — you'll do the real thing in a minute."* Never debug live past 30 seconds |
| Browser won't open Codecraft / too old | Swap to a spare machine, or share with a neighbor (owner operates first) |
| Serial port won't connect | Swap USB cable → swap board → swap machine, 2 minutes per step; still stuck after three? Pair up with a neighbor. **Don't try installing drivers — that's not your job** |
| Serial list is empty | Nine times out of ten: the cable charges but doesn't carry data. Swap the cable |
| Student types slowly / can't type | Voice input, or write it on paper and have the neighbor type (the words must be the student's own) |
| Name shows mojibake | *"It doesn't know that character yet — light it in English first, we'll teach it later."* |
| Student lights up, then "bored" | Fast challenge: make the thing on screen move |
| Whole classroom loses internet | Not back within 15 minutes: rotate students through the instructor machine + schedule a catch-up. **Lighting has no video version — watching a video is not lighting. Reschedule rather than fake it** |
| Fast student done in 20 min | Challenge A: tiny game (whack-a-mole / reaction-timer). Challenge B: board as controller for a screen game — only what you've rehearsed; still fast? Make them a mini-teacher, officially TA next lesson |
| Slow student stuck on Build 1 | 10-minute rule: move them to the instructor follow-along spot; target = "follow-along + one small change" |
| Sensor seems dead | Not broken: *"Want it more sensitive or less? Tell AI."* — that's the real-world sensor teaching point |
| Student builds a light show, no sensor | *"Cool — now make it perform only when [some condition] happens."* |
| Student dumps everything on AI at once | *"Directors shoot one scene at a time — tell me the three boxes of this one build."* If it's already built: have them teach it to a neighbor in 3 boxes, then give a fast challenge |
| Student can't say their 3 boxes | Go back to the examples: *"In your build, which part is the automatic door's eye?"* |
| Student deleted the chat, restarted, messier | No blame — demo live that "add one more line" is faster |
| Icebreaker dies | Self-disclose one more small thing, call directly on your best-known student; silence never runs past 10 seconds |
| "AI will replace people" heckle | One line: *"AI replaces people who don't use AI."* No debate |
| Log becomes empty fluff ("today was fun") | "Got stuck on" is required; no stuck? *"Went too smoothly — what are you worried about?"* |
| Student has no phone for the log | TA takes the photo, filed by table number; the spoken part stays |

### Bonus: student questions and how to catch them

| Student asks | You say |
| --- | --- |
| "Does AI know everything?" | "No. It guesses what you mean from what you say — the clearer you are, the better it guesses. So sometimes it answers confidently and wrongly. Deciding if it's right — that's your job." |
| "Then why learn? Just let AI do it." | "AI writes code, but it doesn't know your mom's pill schedule, or that the streetlight at your corner's been broken for six months. Knowing what to build, and who it's for — that's you." |
| "I can't read this code. Feels risky." | "You don't need to read it today. Right now your skill is say it clearly, watch what happens, tell it to change — be the director first. There's a lesson later that teaches you to read it. One step at a time." |
| "Is AI right? Could it lie to me?" | "Asking that already puts you ahead of most people. It gets things wrong — that's why every log and every effect needs your own eyes on it before you say yes. That's called proofreading, and it's your right." |
| "No computer at home. Can I practice?" | "You can think anywhere. Write the thing you want to build in 3 boxes in a notebook — what it senses, how it decides, how it reacts. Bring it next lesson. That's the best practice there is." |
| "Is this a coding class?" | "It's learning to turn ideas into real things with AI. The coding part, AI does. What you train is spotting problems, judging results, and expressing yourself — those outlast any syntax." |

---

## 6. Prompt Phrase Library (instructor reference)

All eight phrase sets from today, full text — read before class, project when you need them. **These are not printed or handed out** — "one thing at a time" and "add one more line" get projected and read together at 14:30; the rest you project as needed. The same phrases live in the Student Workbook on the matching pages — point students to the book when they forget. If the workbook wording differs slightly from here, either works; the meaning is the same.

### The four "make code" phrases

**Phrase 1 ｜ Say one thing clearly** (before every "make AI write code" request)
One line: let AI do ONE thing per request; say it clearly, then let it work.
> I'm using the Grove Beginner Kit. Please do one thing for me: ________ (just one). It counts as done when ________. Please don't add other features yet.

- ✅ Good: *"Display in large text on the screen: Hello, I'm Sam."*
- ❌ Bad: *"Set up the lights, the screen and the speaker, make it cool."* — three jobs plus "cool" — AI can only guess.

**Phrase 2 ｜ No, I'll say it again** (when the result isn't what you wanted)
One line: AI got it wrong — no need to start over, just add one line.
> The result isn't right: I see ________, I want ________. Please change it based on what you did, don't start over.

- ✅ Good: *"The text is too small and it's blinking; I want large text, steady. Change it based on what you did."*
- ❌ Bad: delete everything and resend: *"Forget it, redo: show text on the screen."* — all the context wasted, AI has to guess you from zero.
- Memory hook: don't delete, don't restart — add one more line. AI remembers what you talked about.

**Phrase 3 ｜ What does this code do** (when you want to know what AI actually wrote)
One line: have AI explain its own code in plain language.
> Explain this code in plain language: what does it do first, then what? Which number controls ________ (e.g., sensitivity)? No jargon.

- ✅ Good: *"Which number controls how long the light stays on? I want it to stay on for 5 seconds."* — AI points at the number, you change it yourself.
- ❌ Bad: can't read it, so ignore it. Runs today, but tomorrow when you need to change one number, you won't know where to look.
- No need for it today — it becomes the workhorse in the read-the-code lesson later.

**Phrase 4 ｜ What do I do about this error** (when compile/flash errors pop red text on screen)
One line: an error isn't a broken thing — it's AI talking to you. Forward it verbatim.
> I just did ________ (what I changed), then I got this error. Full error text below: [paste it all]. Tell me the most likely cause and the first thing to do.

- ✅ Good: *"I changed the delay number from 1000 to 100 and it errored. Full text below."* — AI locates it instantly.
- ❌ Bad: *"I got an error, what do I do?"* — no change, no error text — AI can only guess.
- Memory hook: an error isn't a broken thing, it's AI talking to you. Forward it verbatim.

### The four "document" phrases

**Phrase 5 ｜ One photo, 30 seconds of talking** (near the end of each session)
One line: before you leave, take a photo and say four sentences; AI turns it into a learning log.
> First take a photo of today's build (photograph the failures too). Then say four sentences: today I made ________ / I got stuck on ________ / then ________ / next time I want ________. Send it to AI: "Tidy this into a learning log — format: date / made / stuck on / next. Only what I said, nothing I didn't say." Read it before you confirm.

- ✅ Good: *"Today I got my name on the screen / stuck on the text being too small / then I changed the number to make it bigger / next time I want it to scroll."*
- ❌ Bad: *"Write a great-sounding log for today."* — AI's invented log won't even be recognizable to you next week.

**Phrase 6 ｜ Turn logs into a README** (finals week; keep safe today)
One line: a README is your project's self-introduction page — AI builds it from the logs you've collected.
> Here are all my learning logs. Based ONLY on these logs, write a project introduction: what the project is, how I made it, what problems I hit, how I solved them. Don't add anything I didn't write. [paste logs]

- ✅ Good: paste six sessions of logs before asking — every small thing AI writes matches something you really did.
- ❌ Bad: no logs, just *"write me a project introduction."* — with no logs underneath, it writes someone else's project.

**Phrase 7 ｜ One-minute video script** (before recording your demo video)
One line: AI lays out your project intro as a one-minute shoot script.
> Write a one-minute video script for my project: 5 seconds on the problem, 30 seconds demo, 15 seconds on what I learned. My project is: ________. The point I got stuck on was: ________.

- ✅ Good: *"My project is a box that reminds you to turn off the light, and I got stuck on the sensor being too sensitive."* — the script turns even your crash into a highlight.
- ❌ Bad: *"Write me a video script, make it flashy."* — flashy, sure, but it won't be your project.

**Phrase 8 ｜ Explain it to someone who's never seen it** (when introducing your build to non-technical people)
One line: translate your project intro into words a grandparent or classmate could follow.
> Rewrite this project introduction so someone who knows nothing about tech can follow it. No technical words allowed: ________.

- ✅ Good: "it senses light" becomes "it knows when it's dark, by itself" — any grandparent gets it instantly.
- ❌ Bad: reading the technical words verbatim to non-technical people. The smoother you talk, the less they dare ask.

---

## 7. Localization Slots

| Slot | Original | Swap in |
| --- | --- | --- |
| 14:03 self-intro | [your name] | whatever students call you ("Ms. / Coach / first name" — anything beats "instructor") |
| 14:21 icebreaker self-disclosure | [I want AI to remind my mom to drink water] | your own real small thing — the smaller and more mundane the better: "remind my dad to take his pills" / "watch the coop gate for me" beat grand examples every time |
| 15:00 3-box examples | [automatic door, air conditioner, mom] | the first two can become things everyone in your town has seen — the sensor light at the corner shop, the rice cooker at home; **keep the "mom" one — the room laughs every time** |
| 16:55 closing preview | [what small thing annoys you] | any question closer to your students' lives: "at home, at school, at work — what's something that needs running after, something that needs watching?" |

---

## 8. Teacher Reflection Page (10 minutes after class — every line becomes the next version's saved pitfall)

1. Which segment went best? Which one do you most want a do-over on?
2. Any 🗣️ line that felt stiff to say aloud — not like a human? Cross it out, write what you actually said.
3. Where did students get stuck the longest? Any pitfall missing from the speed sheet?
4. Timing: which segment ran over, which ran short?
5. Did you use the backup video / spare machines? Even if you didn't, say so.
6. After the next-lesson preview, what did students look like?

Write it up, photo it, send it to the teaching group, or tuck it back in the courseware. **Every line you fill in is a pitfall some other teacher doesn't have to step in.**

---

_Source: 中文版 v1.7 ｜ English v1 (2026-08-25) ｜ Design base: X0 v1 / A1 v1 / A2 v1 / X6 v1 / CFG-5 spec v1.0 ｜ Timetable: sample 14:00–17:00, shift to your actual start time_
