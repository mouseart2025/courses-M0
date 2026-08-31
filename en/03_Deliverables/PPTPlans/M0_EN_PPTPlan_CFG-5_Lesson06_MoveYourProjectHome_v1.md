# M0 English PPT Plan ｜ CFG-5 Semester Course · Lesson 6: Move Your Project Home (v1)

_The Big Move: from the Web into Your Own Computer ｜ Chaihuo Maker Academy · Smart Hardware Fundamentals (M0) ｜ 3 hours (sample 14:00–17:00, no scheduled break) ｜ Source: CN deck plan v2 as structural archive (v2.0–v3.2 revisions noted; the colleague-expanded 51-page deck is the CN final form — the EN deck is a brand rebuild from the V3 teaching structure, NOT a copy of the 51-page file) + EN Teacher's Guide L06 v1 (all 🗣️ lines match; the three-check self-test, the empty-house build-along, and the single-Grove-cable wording follow the V3 口径) ｜ This plan is the English blueprint — every on-screen line and every script line below is final English copy. The visual system follows the Chaihuo brand spec unchanged; only text is localized. Terms locked to the EN Glossary + EN Teacher's Guide L06 (from tenant to owner / moving isn't a step back — it's buying the house / the ownership ritual / the two-views moment / blocks view ⇄ code view / the engineer's loop / say it → AI builds → check → upload → verify / the three-box need: input · logic · output / the night-light / the dusk alarm station / the lookout / the alarm post / the signal wire + shared ground / the Grove cable / the install checkpoint (the 14:18 red line) / the install window / the three-check self-test / commander mode / the board picker / build the empty house / AI coding / flash (the upload button) / the serial monitor / the threshold / the whole-class calls / NLHD)._

> **Deck-level note (internal, never on screen)**: 20 pages in five beats — The Big Move (01–08) → Lift the Floor (09–11) → New Project · The Night-Light (12–14) → Joint Project · The Dusk Alarm Station (15–17) → Wrap-Up & Close (18–20). Timings align with the EN Teacher's Guide L06 timetable (the V3 structure): 14:00–14:45 / 14:45–15:20 / 15:20–16:00 / 16:00–16:45 / 16:45–17:00. **This is the biggest pivot of the whole course**: projects move out of the browser and into aily-blockly on the students' own computers; installing is homework settled before class — class only checks it off. **The non-negotiables: installation is settled before class — never gamble on the spot (the install checkpoint closes at 14:18, slide 03 — the deck's first red); the two-views 30 minutes are untouchable (slides 09–10, one of the reasons this lesson exists); "change only the letters inside the quotes" is the boundary of the first-ever hand-touch of code (slide 10 — the deck's second red); and the teacher circulates only — "ask, don't fix" (instructor-side, never on screen).** Red appears exactly twice — slide 03's checkpoint red line and slide 10's quotes-and-brackets boundary. Everything else that warns (paste errors back, the Grove cable, the no-new-windows rule) is bold black on a yellow light fill or plain black — not red. **V3 deltas absorbed into this EN deck, distinct from the CN v2 plan: the self-test is THREE checks (it's installed / it opens / I can reach the main screen — not four); there is a build-along page the CN v2 plan never had — slide 06, Build Your First Empty House (four steps, board picked today is the Wio Terminal); and the joint project's wiring is the ONE-GROVE-CABLE 口径 — signal and ground both live inside a single Grove cable, the instructor's check is "right port + clicked in firmly," NOT the CN plan's separate signal wire + ground wire.** The night-light uses the Grove Beginner Kit (onboard light sensor + LED, zero wiring — the V3 hardware correction, already fixed in CN v3.2). The whole-class calls run at 15:35 (night-light serial) / 16:15 (solo-run first) / 16:30 (Grove cable) — per the EN Teacher's Guide, not the CN plan's 15:45/16:15/16:30. Stand-still pages: 07 (tour), 10 (three steps), 13 (four steps — 30-min solo base), 15 (dusk alarm station — 45-min solo base, the longest stand-still of the lesson); slides 14 / 16 / 17 are temporary cut-ins (hand out prompts, whole-class calls) and always return to the current solo base. **Nothing Chinese ever goes on screen in the EN deck** — on-screen display text is English / numbers / graphics as a course-wide rule (board-picker screenshot is already English UI). Instructor-side content never appears on screen: the 14:18 discipline, the three things to circulate for, "ask, don't fix," the T-7 fallback decision, the Grove-cable check — all live in the Teacher's Guide and this plan's notes, never on a slide.

---

## Design Principles

- **A "turning-point" lesson needs two registers**: golden-line pages (02 tenant→owner, 11 three layers of value) use big-type quote energy and lots of white space, set apart from the operation pages; slide 09 "lift the floor" uses visual contrast (one block ⇄ a few lines of code, side by side) to stage the first-ever sight of code as a ceremony.
- **Installation never gets taught on screen**: slide 03 carries only the three-check self-test + the pair-up rule + the red line — no install screenshots, no steps. The install pipeline (T-7 recording, class-group assignment, the pre-class install window) lives entirely before class and in the instructor's side.
- **The two-views moment is the lesson's only whole-class led block**: slides 09–10 — everyone synchronized, the teacher leading from the front; after that, the rest of the lesson runs solo with the screen as a stand-still scaffold.
- **The screen is the students' working reference, not the instructor's teleprompter**: during solo blocks (slides 13, 15) the page stays fixed and carries the full step list + discipline line + fast-lane challenge; the instructor reads from the Teacher's Guide, circulates, and asks — never fixes.
- **Prompts are shown whole so students can copy**: 6.4 (slide 14) and 6.8's three parts (slide 16) are full monospace boxes — text-volume is licensed on those two pages; the embedded 6.2 (slide 07) and 6.3 (slide 10) boxes are short. The threshold blank `___` is yellow-highlighted everywhere it appears.
- **The one-Grove-cable 口径 is taught, not hidden**: slide 15's warning is the joint project's single hard rule — "signal and ground live inside this one cable; is it clicked in firmly?" — replacing the CN plan's separate "signal wire + shared ground" framing (both are true; the EN deck teaches the V3 update).
- **Output anchors everywhere**: slides 08 / 10 / 13 / 15 / 19 each carry a 📝 "write it in your workbook (or notebook)" action box; the ownership ritual (save → folder → see it) is the lesson's emotional anchor and is never skipped.
- **Zero print**: the self-test, the two buttons, the cheat sheet, the prompts, and the NLHD link are all on screen (the student workbook is shared read-only — nothing gets written in it today).
- **Stand-still pages**: 07 (tour + two buttons), 10 (three steps), 13 (four steps), 15 (division-of-labor). Slide 17 (whole-class calls) is a fast-flip cut-in with no separate timing.

### Colors / Type / Icons / Layout

Chaihuo brand spec (`chaihuo-ppt-brand.md`): white 70 / yellow F3D230 15 / black 10 / red D84144 5; no gradients, no shadows, no complex illustrations; 2 px black-stroke line icons; Source Han Sans; 16:9 (960×540 px); title zone 100 px top, content 110–490 px, footer 40 px. **Red appears exactly twice in this deck — slide 03's checkpoint red line (the 14:18 close) and slide 10's quotes-and-brackets boundary (change only the letters inside the quotes)** (two red elements, strictly capped). Graphic signal colors (slide 15's cable/arrow diagram) use graphic colours `#7FB069` / `#D84144`-family only inside diagrams, outside the red quota, consistent with the L4 traffic-light convention. Warning lines that are NOT red (slide 13's paste-errors-back discipline, slide 15's Grove-cable warning) are bold black on a yellow light fill with a 1 px black border — clearly a warning, but not in the red quota. Script/quote boxes: the one permitted fifth colour — light grey `#F5F5F5` fill + 1 px black border + monospace 14–16 pt.

### On-Screen Text Rules

- All on-screen text is final English copy (below, verbatim). Digits for all numbers.
- Student-typed prompt lines are shown in monospace boxes; the part students must swap in is marked with a yellow-highlighted blank `___` (the threshold).
- **On-screen display is English / numbers / graphics by design** — the board-picker screenshot is already English UI; all on-board display text stays English ("It's dark!" / "All clear"). If garbled glyphs still appear, tell AI *"change all on-screen text to English"* — don't debug the font library.
- During hands-on segments the page stays fixed (stand-still); instructors read from the Teacher's Guide, not from the slide.

---

## Slide Map

| # | On-screen title | Type | Beat | Time |
| --- | --- | --- | --- | --- |
| 01 | Move Your Project Home | Title page | Cover | Loops before class |
| **Act 1 · The Big Move (14:00–14:45, 7 content slides)** | | | | |
| 02 | From Tenant to Owner | Chapter cover (golden-line) | Frame | 8 min |
| 03 | Install Checkpoint — Three Checks | Operation step page — **red (1/2)** | Check | 10 min |
| 04 | Meet the New Tool: aily-blockly | Core concept (three facts) | Gear | 4 min |
| 05 | The Real Thing: Pick Your Board | Photo page (board picker) | Gear | 2 min |
| 06 | Build Your First Empty House — Four Steps | Build-along page (V3-only) | Hands-on | 3 min |
| 07 | Tour the New House — Three Rooms | Task page (stand-still) | Tour | 3 min |
| 08 | Unpack Your Most Precious Thing | Operation step page | Hands-on | 15 min |
| **Act 2 · Lift the Floor (14:45–15:20, 3 slides)** | | | | |
| 09 | Two Looks at the Same Project | Core concept (reveal page) | Concept | 10 min |
| 10 | Three Steps — Follow Me, Then Walk Alone | Operation step page (stand-still) — **red (2/2)** | Guided | 20 min |
| 11 | Three Layers of Value | Golden-line page | Bridge | 5 min |
| **Act 3 · New Project · The Night-Light (15:20–16:00, 3 slides)** | | | | |
| 12 | The Engineer's Loop | Method frame page | Frame | 10 min (open), then on-demand |
| 13 | Today's Four Steps — Run Solo | Operation step page (stand-still, solo base) | You Do | 30 min |
| 14 | Send This to AI (the night-light prompt) | Sentence page (cut-in, 6.4 verbatim) | You Do | cut-in 3 min, then back to 13 |
| **Act 4 · Joint Project · The Dusk Alarm Station (16:00–16:45, 3 slides)** | | | | |
| 15 | The Dusk Alarm Station — Division of Labor | Method frame page (stand-still, solo base) | You Do | 45 min |
| 16 | Three Parts, Same Window (6.8 verbatim) | Sentence page (cut-in) | You Do | cut-in 3 min, then back to 15 |
| 17 | Three Whole-Class Calls | Rhythm prompt page (fast flip) | Rhythm | cut-in 1 min ×3, then back |
| **Act 5 · Wrap-Up & Close (16:45–17:00, 3 slides)** | | | | |
| 18 | Three Sentences — and How Big Projects Run | Summary page | Wrap-up | 5 min |
| 19 | The New Home's Manual (NLHD) | Resource page | Wrap-up | 5 min |
| 20 | Today You Moved From Tenant to Owner | Call-to-action | Close | 5 min |

> 20 pages, ~180 minutes (includes stand-still time), matches the 3-hour session (±10%). Slides 14 / 16 / 17 are temporary cut-ins inside the solo blocks (hand out prompts, whole-class calls) — after each cut-in the deck returns to the current solo base (13 or 15). **The non-negotiables: installation settled before class — the checkpoint closes at 14:18 (slide 03); the two-views 30 minutes untouchable (slides 09–10); "change only the letters inside the quotes" (slide 10); teacher circulates only, "ask, don't fix" (instructor-side, never on screen).**

---

## Slide by Slide

### Slide 01 | Move Your Project Home — Title page

**Type**: Title · **Time**: loops before class

**On screen** (verbatim):

```text
Move Your Project Home

The Big Move: from the Web into Your Own Computer · Chaihuo Maker Academy · M0 Lesson 6

Lesson 6 · From Tenant to Owner
New tool: aily-blockly — the open-source hardware dev environment that lives on your computer
```

**Instructor notes**: cover page only; students see it as they sit down. No script. When the session starts, go straight to slide 02 — the opener's 30-second look-back is spoken, not projected. Right side: aily-blockly blocks-view screenshot (an open project) + a small XIAO board photo ("the new house"); yellow rule under the subtitle. Footer: `Chaihuo Maker Academy · M0 · Move Your Project Home | 06 / 20`.

**Assets**: IMG aily-blockly blocks-view screenshot + XIAO board photo (400×300).

---

### Slide 02 | From Tenant to Owner — Chapter cover (golden-line)

**Type**: Chapter cover (golden-line) · **Time**: 8 min (14:00–14:08)

**On screen** (verbatim):

```text
Today We Don't Create. Today We Move.

[OLD HOME / NEW HOME cards, white fill + black border, yellow arrow between]
OLD — lived on someone else's server; close the browser, it's gone
NEW — lives in MY computer — unplug the internet, it's there;
      shut down the website, it's there; ten years later, it's still there

(quote, yellow left border) Moving isn't a step back — it's buying the house.

[ROUTE MAP, five steps, yellow numbered dots]
checkpoint → tour the new home → unpack the old project → lift the floor
→ build something new with AI (last step, yellow light fill, highlighted)
```

**Instructor notes** (verbatim): *"30-second look-back: last session, you taught your hardware to see — you ran a ready model, then trained a model that's entirely yours. From Lesson 1 to now, your projects keep coming, and they keep getting better."* Then the close-the-tab demo: *"Today we don't create. Today we do one big thing: until now, your projects have lived on someone else's server — close the browser, and they're gone. Today, you move from tenant to owner."* *(demo: close the Codecraft tab)* *"See? Closed. Where's your project? — At someone else's house. *(open a local folder)* Now look here: after class today, your project will live in this folder. Unplug the internet — it's there. Shut down the website — it's there. Ten years after graduation — it's still there. **Moving isn't a step back — it's buying the house.**"* Then the five steps *(point at the screen)* and the Lesson 7 hook: *"Once the house is set up, what's next? — Next session, you give your project a brief: the topic grows out of your own experience, not copied from the internet. Brief done, the marathon starts. Today's five steps: checkpoint → tour the new home → unpack the old project → lift the floor → build something new with AI."* "Why move if the web version works fine?" → *"The web version isn't retiring — during the marathon you'll use both. But the feeling of owning it — you have to taste that once today."* Flat energy → this is a celebration, not moving day: over-act the opener.

---

### Slide 03 | Install Checkpoint — Three Checks — Operation step page — **RED (1/2)**

**Type**: Operation step · **Time**: 10 min (14:08–14:18 — the red-line transition)

**On screen** (verbatim):

```text
Install Checkpoint — Three Checks

[THREE-CHECK CARD, white fill + black border, yellow check squares]
□ It's installed
□ It opens
□ I can reach the main screen

[PAIR-UP RULE, yellow light fill] Not done? Share one computer with your neighbor —
you're the COMMANDER: you say what to do, they press the buttons.
Give your name to a TA — we'll get you set up within 10 minutes after class.

(red line) THE CHECKPOINT CLOSES AT 14:18 — NOT INSTALLED? PAIR UP ON THE SPOT. NO INSTALLING IN CLASS.
```

**Instructor notes** (verbatim): *"Finished your install homework? Open the tool, fill in the self-test on screen (it's in your workbook too): three checks — it's installed ／ it opens ／ I can reach the main screen."* *"Not done — raise your hand. No more installing now; you pair up on the spot: share one computer with your neighbor, you're the commander — you say what to do, they press the buttons. Give your name to a TA; we'll make sure you're set up within 10 minutes after class."* ⭐ **More than 1/3 not installed** → the homework pipeline broke: extend this block 5 minutes for a focused group install (all TAs on it); whoever still isn't done pairs up; note it on the reflection page. Installed but the board won't connect → TA B handles one-on-one (cable, port, permission); not fixed in 5 minutes → pair up. Whole-room permission block (a night policy change) → execute the 4.1 downgrade. **The red line is the deck's first red — the 14:18 close is today's iron law, never softened.** No install steps ever appear on this page.

---

### Slide 04 | Meet the New Tool: aily-blockly — Core concept (three facts)

**Type**: Core concept · **Time**: 4 min (14:18–14:22)

**On screen** (verbatim):

```text
Your New Tool Is Called aily-blockly

A hardware dev environment that lives on your computer — open source and free (GPL),
by the aily Project · the site is yiyu.pro

[THREE FACTS, three cards, white fill + black border, 2 px line icons]
UNIVERSAL — not some one-board companion app; 100+ development boards fit here,
and your future boards will too
AI-NATIVE — say what you need, get a wiring diagram, get code, get errors fixed —
AI is there the whole way
MADE FOR BEGINNERS — the official goal in one line: break the line between
professional and amateur — let anyone make hardware with plain language

(bottom, yellow light fill) The old home got you daring quickly; the new home gets you finishing properly.
```

**Instructor notes** (verbatim): *"Every house needs a name — this one is aily-blockly. Three facts, and that's it. One: it's open source and free — the site is yiyu.pro, anyone can install it. Two: it's universal — not some one-board companion app; it takes 100+ development boards, so when you change boards later, it's still your home. Three: it's AI-native — say what you need, get a wiring diagram, get code, get errors fixed — AI is there the whole way."* *"The third one matters most: the people who built it set out to break the line between professional and amateur — to let anyone make hardware with plain language. It was built for you. The old home got you daring quickly; the new home gets you finishing properly."* Software name + the site use monospace small type. Three facts skimmed fast — the page is a name-introduction, not a lecture.

---

### Slide 05 | The Real Thing: Pick Your Board — Photo page (board picker)

**Type**: Photo page · **Time**: 2 min (14:22–14:24)

**On screen** (verbatim):

```text
Look at the Real Thing — Pick Your Board

[BOARD-PICKER SCREENSHOT, full width, contain — aily-blockly's board-selection screen]

(bottom, yellow light fill) Grove Beginner Kit is in there — and so is Wio Terminal.
That's what "universal" means. Whatever board you use next, it's got a place here.
```

**Instructor notes** (verbatim): *"Words are cheap — look at the real thing (point at the screen). This is the first screen aily-blockly shows: pick your board. Look for it: Grove Beginner Kit is in there — and so is Wio Terminal. That's what 'universal' means. Whatever board you use next, it's got a place here."* Screenshot = evidence — "100+ boards" isn't claimed, it's shown. The screenshot is already English UI — no localization needed.

**Assets**: IMG board-picker screenshot (`screenshot-20260803-154849.png`, the user-provided real capture already embedded in the CN deck's media; reuse as-is — English UI).

---

### Slide 06 | Build Your First Empty House — Four Steps — Build-along page (V3-only)

**Type**: Build-along · **Time**: 3 min (14:24–14:27)

**On screen** (verbatim):

```text
Build Your First Empty House — Four Steps

[FOUR STEPS, yellow numbered dots, each with a mini screenshot]
① NEW PROJECT
② PICK THE BOARD — today: WIO TERMINAL
③ NAME IT: use English — and point the save path at your projects folder
④ CREATE

(sign it worked, yellow light fill) You're in the blocks screen — and the folder already has it.
```

**Instructor notes** (verbatim, build-along — "where I click, you click"): *"Intro done — time to build your first empty house. Four steps: new project → pick the board: today, Wio Terminal → name it: use English, and point the save path at your projects folder → create. The sign it worked: you're in the blocks screen, and the folder already has it."* Why the Wio today? — spoken, not on screen: *"The Wio is the board we'll team up with this afternoon — build its house first."* Students follow on their own machines; paired groups: the installed partner operates, the other points and commands (commander mode carries over). Can't find the project folder → whole-class sync: *"Where I click, you click — found it? Hands up."* This page is a V3 addition the CN v2 plan never had — the build-along is part of the 12-minute "meet the new home" block, not a separate lesson.

**Assets**: IMG empty-house four-step screenshots ×4 (new-project screen / board-picker with Wio selected / name + save path / created — captured on the teacher machine at rehearsal, English UI).

---

### Slide 07 | Tour the New House — Three Rooms — Task page (stand-still)

**Type**: Task (stand-still) · **Time**: 3 min (14:27–14:30)

**On screen** (verbatim):

```text
Tour the New House — Three Rooms

[THREE ROOM CARDS, white fill + black border, 2 px line icons: folder / blocks / code]
① YOUR PROJECTS' HOME — this folder IS your project: copy it out and it's portable,
send it and it's shared
② THE BLOCKS VIEW — drag and drop, the same graphical feel you already know
③ THE CODE VIEW — what AI has been writing for you; we lift that floor in a few minutes

[TWO BUTTONS THAT MATTER, grey monospace box, 1 px black border — 6.2 verbatim]
Whatever buttons there are, remember two today
① AI coding — tell it what you need in plain language; it writes code and fixes errors (today runs on it)
② Flash — click, and the program goes into the board (know what the "upload" button looks like)
Every other button — ask AI when you need it. It knows them better than you.
```

**Instructor notes** (verbatim): *"Tour the new house — three rooms. First room (open the file manager): this is where your projects live from now on. This folder is your project — copy it out and it's portable, send it and it's shared. Second room (back to the tool): this is the blocks view — drag and drop, same graphical feel you already know. Third room (click the code view): this is the code view — one of today's main courses; we lift that floor in a few minutes."* *"Whatever buttons there are, remember just two today. One: AI coding — tell it what you need in plain language, it writes your code and fixes your errors; today runs on it. Two: flash — click, and the program goes into the board; know what the 'upload' button looks like. Every other button — ask AI when you need it. It knows them better than you."* Students point to where "AI coding" and "flash (upload)" live in the interface (the "did it land" check). Stand-still during the tour. The two-buttons box is 6.2 verbatim — the shared text with the Teacher's Guide and the workbook; any later edit must sync all three.

---

### Slide 08 | Unpack Your Most Precious Thing — Operation step page

**Type**: Operation step · **Time**: 15 min (14:30–14:45)

**On screen** (verbatim):

```text
Unpack Your Most Precious Thing — Your Very First Project

[TASK CARD, white fill + black border]
Redo "show your name on screen" in the new tool.
Lesson 1: how long did it take you? I bet you finish in HALF the time today.
This isn't repetition — it's watching yourself grow in real time.

[TIMING LINE, yellow light fill] Lesson 1: ___ min  →  today: ___ min

[OWNERSHIP RITUAL, three steps, yellow numbered dots — the third is the peak]
① SAVE → ② OPEN THE FOLDER → ③ SEE IT WITH YOUR OWN EYES
From today, every project you make takes this step.

📝 Write your two times in the workbook — Lesson 1 vs today.
```

**Instructor notes** (verbatim): *"First thing after moving in: put out your most precious old thing — your very first project: showing your name on screen."* *"Don't roll your eyes. In Lesson 1, how long did it take you? (wait for answers) Timer starts now — I bet you finish in half the time. This isn't repetition; it's watching yourself grow in real time."* *"The one step that matters most when you're done: save, then open the folder and see it with your own eyes. That ritual has a name — the ownership ritual. From today, every project you make takes this step."* Redo = AI-coding entry + the flash five-step (rule: **pick the right port first, then click upload**). "This is boring" → the frame is built in; still resisting → let them redo *any* old project — but **the ownership ritual is never skipped**; fast students go straight into the night-light block (give them the 6.4 prompt early). Paired groups → **both students must do the save→folder→confirm run themselves** (acceptance: each partner operates independently).

---

### Slide 09 | Two Looks at the Same Project — Core concept (reveal page)

**Type**: Core concept (reveal) · **Time**: 10 min (14:45–14:55) — first half of the untouchable 30

**On screen** (verbatim):

```text
This Is What AI Has Been Writing for You All Along

[BLOCK ⇄ CODE side-by-side, yellow ⇄ arrow between, labelled:]
ONE BLOCK  ⇄  A FEW LINES OF CODE
"two looks at the same project"

Blocks are for hands ｜ Code is for machines

(bottom, yellow light fill) You don't need to read it all — today is about one feeling:
CODE IS NOT MYSTERIOUS. Find one match, and you graduate.
```

**Instructor notes** (verbatim): *"All eyes on the big screen. I'm lifting the floor. (switch to code view) This is what AI has been writing for you all along. From the first time you said 'show my name on screen,' it has been writing this every time. Today, we look at what it looks like."* Then one correspondence: *"Look at this pair — this one block is these few lines. Blocks and code are two looks at the same project — blocks are for hands, code is for machines. You don't need to read it all — today is about one feeling: code is not mysterious. Find one match, and you graduate."* This is the visual-contrast peak of the lesson — the code's first full-screen appearance. A student scared off by the code → *"You don't need to read it all — one match and you graduate"* (step one only; steps two and three optional). The page stays minimal — no task list, no code box; the contrast image carries it.

**Assets**: IMG block ⇄ code side-by-side screenshot (one enlarged block vs its matching code lines, 800×260 — captured on the teacher machine at rehearsal; the CN plan's IMG-07-01 equivalent).

---

### Slide 10 | Three Steps — Follow Me, Then Walk Alone — Operation step page (stand-still) — **RED (2/2)**

**Type**: Operation step (stand-still) · **Time**: 20 min (14:55–15:15) — second half of the untouchable 30

**On screen** (verbatim):

```text
Three Steps — Follow Me, Then Walk Alone

[STEP 1 · FIND THE MATCH, white card] Back to the blocks view, drag one block —
watch what changed over here in the code. One "this block = these lines" — you graduate.

[STEP 2 · ASK AI, white card] Select a chunk you don't understand, send it to your AI.
From today, AI has a new job: not just doing the work for you — teaching you to read it.

[grey monospace box — 6.3 verbatim]
(select a code chunk, send in the conversation you already have)
What's this code doing? Explain in plain language I can understand — two or three sentences max.

[STEP 3 · CHANGE ONE LINE, white card] Find the line that shows your name —
change only the letters inside the quotes to your nickname. Run it.

(red line) CHANGE ONLY THE LETTERS INSIDE THE QUOTES — DON'T TOUCH THE QUOTES OR BRACKETS ❌
(broke it? go back to the last version — that's why engineers save constantly)

(reminder) Ask in the conversation you already have — no new windows.
It knows your project, so its answers fit your code.

📝 Write in your workbook — the two-views cheat sheet: one block = which lines?
```

**Instructor notes** (verbatim): *"Three steps, follow me. Step one: find the match. Go back to the blocks view, drag one block — watch: what changed over here in the code? (wait for someone to point) Right — this one block is these few lines."* *"Step two: ask AI. Select a chunk of code you don't understand, send it to your AI (project the prompt): 'What's this code doing?' Have it explain in plain language. From today, AI has a new job: not just doing the work for you — teaching you to read it. Old rule: ask in the conversation you already have. No new windows."* *"Step three: change one line. Find the line that shows your name — change only the letters inside the quotes to your nickname. Run it. (wait) See that? You just touched code with your own hands — and you didn't break it. Changing a letter can't break it. That's your first time."* **The red line is the deck's second red — the boundary of the first-ever hand-touch of code.** They break a line (deleted a quote or bracket) → teach the save, on the spot: *"No panic — go back to the last version. See? This is why engineers save constantly."* Someone wants to change *logic* (numbers, conditions) → *"Today, letters only. The fire to change logic — hold it until the marathon starts, when you have your requirements sheet."* New window opened → point at the reminder line. Stand-still during the students' solo walk; the instructor circulates.

---

### Slide 11 | Three Layers of Value — Golden-line page

**Type**: Golden-line · **Time**: 5 min (15:15–15:20)

**On screen** (verbatim):

```text
Why Did You Just Do All This?

[THREE LINES, extra-large, yellow left borders]
It's yours.
You're not afraid of it.
The door opened.

(bottom, yellow light fill) Just now you READ what AI wrote.
Next, you'll DIRECT AI to write something brand new.
```

**Instructor notes** (verbatim): *"One point, then we move: why did you just do all this? Three reasons — it's yours (your project, your folder, your house); you're not afraid of it (from black box to clear box); the door opened (competitions, final projects, the real engineer's world — this is where you walk in)."* *"The door's open — now step through it. Just now you read what AI wrote. Next, you'll direct AI to write something brand new."* No code box, no task list — the page is deliberately set apart from the operation pages (same energy as slide 02).

---

### Slide 12 | The Engineer's Loop — Method frame page

**Type**: Method frame · **Time**: 10 min (15:20–15:30) to open, then on-demand return

**On screen** (verbatim):

```text
The Engineer's Loop — Every Lap of the Marathon Runs It

[LOOP, five station cards + yellow arrows + return arc — 6.1 verbatim]
say it → AI builds → check → upload → verify
   ↑_________ wrong? say the need more clearly, run another lap _________↓

[THREE BOXES] what it senses (input) ｜ what it does under what condition (logic) ｜ how it shows itself (output)

[PROJECT LINE, yellow light fill] Today's first new project: THE NIGHT-LIGHT —
Grove Beginner Kit, light sensor + LED built into the board, NOT A SINGLE WIRE to connect.
Short code, fast upload, verdict in two minutes.
Leave the number in brackets blank — you'll read the real value on the serial monitor and fill it in yourself.
```

**Instructor notes** (verbatim): *"Engineers working in a local tool run on this loop (point, read the five stations): say it → AI builds → check → upload → verify. Verification fails? Back to the first station — say the need more clearly, run another lap. This loop is the motion of every lap of the marathon — today we get fluent on a small project."* *"How do you say a need clearly? You already know — the three boxes: what it senses (input), what it does under what condition (logic), how it shows itself (output)."* *"The first new project: the night-light. Uses the Grove Beginner Kit in your hand — light sensor and LED are built into the board, not a single wire to connect, short code, fast upload, verdict in two minutes. Dark — light on. Bright — light off. Use the prompt on screen; leave the number in brackets blank — what the sensor actually reads, you'll see on the serial monitor in a moment, and fill in yourself."* Then cut to slide 14 to hand out the 6.4 prompt (3 min), then to slide 13 as the solo base. The loop diagram returns on demand when a student asks "what do I do next?" — the loop is the map.

---

### Slide 13 | Today's Four Steps — Run Solo — Operation step page (stand-still, solo base)

**Type**: Operation step (stand-still) · **Time**: 30 min (15:30–16:00)

**On screen** (verbatim):

```text
Today's Four Steps — Run Solo From Your Workbook

[FOUR-STEPS CARD, white fill + black border — 6.1 verbatim]
1. Send the 6.4 prompt with your need → read what AI explains first; point to the light sensor
   and LED on your board before you build
2. Build + upload (paste errors back verbatim, one step at a time)
3. Open the serial monitor: normal ___ / hand over it ___ → put the threshold back into your need,
   have AI use your number
4. Iterate one lap: change the threshold / add "when dark, the buzzer also beeps" (pick one)

(discipline line, bold black, yellow light fill) Paste errors back verbatim — one step at a time.
Don't guess and fiddle on your own.

(fast lane, yellow light fill) Done? Upgrade the need — "when it's dark, the buzzer also beeps once";
or play acceptance-tester: cover your neighbor's sensor — does their light obey?

📝 Workbook — the loop record: my need took ___ tries to say clearly;
light reading: normal ___ / hand over it ___ → my threshold is ___.
```

**Instructor notes** (verbatim, solo base — stand-still; the instructor circulates only): the single whole-class call at **15:35** — *"Time to open the serial monitor — take the number you measured with your hand over it and put it back into your need."* **Circulate, three things:** the conversation (is the need getting more specific, or are they re-pasting the same sentence?) ／ the serial (did the number come out?) ／ the LED (cover the sensor — does the light obey?). **Intervention red line: ask, don't fix** — *"What number is 'dark' in your need? How do you know?"* Errors go back to AI verbatim (old rule: one step at a time). No serial data → students run their own three-check out loud: did it upload? is the monitor open? is the sensor reading? ⭐ Whole class stuck on the serial → demo once on the teacher machine: open the monitor, cover the sensor, read the number — 30 seconds, then back to solo running. AI didn't get it on the first try → teaching point, not an incident: *"See — this is iteration. Engineers saying a need three times is normal."* **Output anchor**: at least one solo lap of the loop (say → build → upload → measure → fill the threshold → iterate) + the loop record in the workbook. The discipline line is **not red** — it's the old course-wide rule, bold black on yellow.

---

### Slide 14 | Send This to AI (the night-light prompt) — Sentence page (cut-in)

**Type**: Sentence page (cut-in) · **Time**: cut-in ~15:22, 3 min, then back to slide 13

**On screen** (verbatim):

```text
Send This to AI — in the Conversation You Already Have

[monospace box, white fill, black border — 6.4 verbatim, the `___` threshold yellow-highlighted]
I'm using aily-blockly, with a Grove Beginner Kit for Arduino
(Seeeduino Lotus, with an onboard light sensor and LED — no wiring needed).
Make me a new project: a night-light —
input: light sensor reading; logic: reading below ___ counts as "dark";
output: LED on when dark, off when bright.
First tell me where the light sensor and LED are on the board and which pins they use,
then give me the code, one step at a time.
Leave the threshold number blank — I'll read the real value on the serial monitor and fill it in myself.

(reminder, yellow left border) All three boxes are in there — input, logic, output.
Leave the threshold blank: the number in your need is measured by your own hand, not made up by AI.
```

**Instructor notes** (verbatim): *"The prompt is on screen — copy it into the conversation you already have. All three boxes are in there: input, logic, output. Leave the threshold blank — the number in your need is measured by your own hand, not made up by AI. Send it."* Cut out once to hand out the prompt, students copy it, return to slide 13 (the solo base). The `___` is yellow-highlighted. 6.4 verbatim — shared text with the Teacher's Guide and the workbook; any edit must sync all three.

---

### Slide 15 | The Dusk Alarm Station — Division of Labor — Method frame page (stand-still, solo base)

**Type**: Method frame (stand-still) · **Time**: 45 min (16:00–16:45) — the longest stand-still of the lesson

**On screen** (verbatim):

```text
The Dusk Alarm Station — Two Boards, Two Programs, One Wire Linking Them

[LEFT CARD: THE LOOKOUT — Grove Beginner Kit]   [RIGHT CARD: THE ALARM POST — Wio Terminal]
light sensor watches the sky → when dark:         watches the signal pin:
· lights its own LED                              · sees the hand → screen "It's dark!" + beep
· "raises its hand" on the signal pin (HIGH)      · no signal → screen "All clear"
        │                                             ▲
        └──────── ONE GROVE CABLE: signal + ground, agreed pin → agreed pin ────────┘

[JOINT THREE STEPS, white card — 6.9 verbatim]
1. Send part one: split the job, ask for the wiring explanation (no code yet)
2. Send parts two and three: generate and flash each program separately — run each board solo first
3. Link and verify: cover the light sensor, watch the alarm post — dead link? run the three checks
   (did each board run solo? / is the signal wire on the agreed pins? / is the ground shared?)

(warning, bold black on yellow light fill + 1 px black border) NINE DEAD LINKS OUT OF TEN ARE
A WRONG PORT OR A LOOSE CABLE — signal and ground live inside this ONE GROVE CABLE.
Is it CLICKED IN FIRMLY? (no shared ground, no link — don't add a second ground wire)

(fast lane, small) Upgrade the alarm — Wio shows the current light reading; or press the Wio button
to manually clear the alarm; or flip it: the Wio becomes the lookout (it has a light sensor too),
the Beginner Kit's buzzer becomes the alarm post.

📝 Workbook — the joint record: the lookout's hand pin is ___; the alarm post knows because ___.
Our link's first failure was because ___.
```

**Instructor notes** (verbatim, solo base — stand-still; the instructor circulates only): *"Just now, one board worked alone. Now, upgrade: two boards work together — and that's what the real world looks like: a doorbell — one button outside, one speaker inside, each doing its own job, one wire between them."* *"The joint project: the dusk alarm station. The Beginner Kit is the lookout: when it's dark, it lights its own LED and 'raises its hand' on a signal pin. The Wio Terminal is the alarm post: when it sees the hand go up, the screen says 'It's dark!' and the buzzer beeps once. Two boards, two programs, each minding its own job, linked by one wire."* *"The need also splits into two parts — first have AI sort out the division and the wiring (prompt part one), then ask for the two programs (part two, part three). Same conversation window — AI remembers the whole picture."* **The two whole-class calls** — 16:15: *"Both programs flashed? Run each board solo first — then link them"*; 16:30: *"Linking check, two things — is the Grove cable in the right port? Is it clicked in firmly?"* **Circulate, three things:** the division (can they say who senses and who performs?) ／ solo-run first (each end runs alone before linking — no skipped steps) ／ the Grove cable (nine dead links out of ten are a wrong port or a loose cable). **Intervention red line: ask, don't fix** — *"Which pin is the lookout's hand? How does the alarm post know?"* Wiring questions go to AI for a diagram (it was asked in the prompt) — the teacher doesn't check wires for them. Link dead → the three checks: did each board run solo? is the signal wire on the agreed pins at both ends? is it clicked in firmly? Still dead: unplug and re-seat, or swap in a fresh Grove cable; if it persists, demo one working pair on the teacher machine. One board "occupied" by the computer, the other won't flash → normal: flash the two boards alternately on one computer, or split across the pair's two machines. "Why not just use one board?" → *"One board could do it — but in real engineering, sensing and performing often don't live in the same box. Today, between two wires, you saw a system for the first time."* **The warning is NOT red** — the red quota is spent on slides 03 and 10; this is the joint project's hard rule, bold black on yellow. **Output anchor**: the joint three steps complete (split → flash both solo → link and verify) + the joint record in the workbook.

---

### Slide 16 | Three Parts, Same Window (6.8 verbatim) — Sentence page (cut-in)

**Type**: Sentence page (cut-in) · **Time**: cut-in ~16:05, 3 min, then back to slide 15

**On screen** (verbatim):

```text
Three Parts, Same Window — Send in Order

[PART ONE: SPLIT THE JOB FIRST — monospace, yellow tag ①]
I have two boards: a Grove Beginner Kit for Arduino (Seeeduino Lotus,
with onboard light sensor and LED) and a Wio Terminal (with screen and buzzer).
I want to build a "dusk alarm station": the Beginner Kit is the lookout — when it's dark
it lights its LED and "raises its hand" (outputs HIGH) on one digital pin; the Wio Terminal is the alarm post —
when it reads that signal, the screen shows "It's dark!" and the buzzer beeps once.
First help me sort this out: what does each end do? How do the signal wire and ground connect
(which two pins)? Draw me a wiring explanation I can understand. Don't write code yet.

[PART TWO: ASK FOR THE LOOKOUT PROGRAM — monospace, yellow tag ②]
Division's clear. Now give me the program for the Beginner Kit (the lookout):
read the light sensor; when it's dark, LED on + signal pin raises its hand; when bright, the reverse.
Use the threshold I measured: ___. One step at a time.

[PART THREE: ASK FOR THE ALARM POST PROGRAM — monospace, yellow tag ③]
Now the program for the Wio Terminal (the alarm post): watch the signal pin —
when it sees the hand go up, the screen shows "It's dark!" and the buzzer beeps once;
when it doesn't, the screen shows "All clear." One step at a time.
```

**Instructor notes** (verbatim): *"Three parts, send them in order, all in the conversation you already have. Notice part one says 'don't write code yet' — first have AI sort out the division and the wiring, and read it before you go on. Then ask for the two programs separately — generate and flash each one, run each board solo first, then link them."* The "don't write code yet" opener is itself the teaching point — the order is the lesson. Text volume is licensed on this page (three full prompt blocks must be copyable). `___` yellow-highlighted in part two. 6.8 verbatim — shared text; any edit must sync all three documents.

---

### Slide 17 | Three Whole-Class Calls — Rhythm prompt page (fast flip)

**Type**: Rhythm prompt (fast flip) · **Time**: cut-in 1 min each at 15:35 / 16:15 / 16:30, then back to the current solo base (13 or 15)

**On screen** (verbatim):

```text
Three Whole-Class Calls

[CALL 1 · 15:35, white card + yellow left border]
Time to open the serial monitor — write down your normal number and your hand-over number.
PUT YOUR NUMBER BACK INTO YOUR NEED.

[CALL 2 · 16:15, white card + yellow left border]
Both programs flashed? RUN EACH BOARD SOLO FIRST — THEN LINK THEM.

[CALL 3 · 16:30, white card + yellow left border]
Linking check, two things — is the Grove cable in the right port? IS IT CLICKED IN FIRMLY?
```

**Instructor notes**: the instructor flips to this page at each clock time, reads the call out loud, and immediately returns to the current solo base. The current call is highlighted with a yellow light fill behind its card. Timings follow the EN Teacher's Guide (15:35 for the serial call — not the CN plan's 15:45; 16:15 / 16:30 for the joint calls). Big-type single lines — a rhythm page, not a task page.

---

### Slide 18 | Three Sentences — and How Big Projects Run — Summary page

**Type**: Summary · **Time**: 5 min (16:45–16:50)

**On screen** (verbatim):

```text
Three Sentences — and How Big Projects Run

[THREE LINES, yellow left borders]
It's yours.
You're not afraid of it.
The door opened.

[LONG-PROJECT METHOD, three boxes + yellow arrows]
SET THE SPEC FIRST (the standard) → BUILD ONE FUNCTION AT A TIME (each board runs its own loop)
→ LINK THEM INTO A SYSTEM (one signal wire)

(bottom line) Today's alarm station did exactly this — and it's how your three marathon legs will run.
```

**Instructor notes** (verbatim): *"Three sentences to close: it's yours; you're not afraid of it; the door opened."* *"Two more from today: you can loop — say it, build, check, upload, verify, and if it's wrong, say it again; and you can link — today's alarm station is the proof: set the spec first (the standard), build one function at a time (each board runs its own loop), then link them into a system (one signal wire). That's how engineers take on big projects — and that's how your three marathon legs will run."* Echoes slide 11's three lines and slide 12's loop — the wrap-up lands the lesson's arc.

---

### Slide 19 | The New Home's Manual (NLHD) — Resource page

**Type**: Resource · **Time**: 5 min (16:50–16:55)

**On screen** (verbatim):

```text
The New Home's Manual

[RESOURCE CARD, white fill + black border, monospace — 6.7 verbatim]
The new home's manual: Natural-Language Hardware Development (NLHD, 15 chapters)
https://github.com/ailyProject/Natural-Language-Hardware-Development
— every chapter drills today's loop. You don't need to read it today — open it when you're stuck.

[LOG LINE, yellow light fill]
Log time — four lines as usual; the "done" line is required:
TODAY I BUILT ___ WITH AI GUIDING ME, AND I LINKED IT TO ANOTHER BOARD;
OUR LINK'S FIRST FAILURE WAS BECAUSE ___.
```

**Instructor notes** (verbatim): *"This is the new home's manual — Natural-Language Hardware Development, 15 chapters, from lighting your first project to full systems, and every chapter drills today's loop. It's going to the class group; put it in your workbook. You don't need to read it today — open it when you're stuck."* *"Log time. Four lines as usual — the 'done' line is required: today I built ___ with AI guiding me, and I linked it to another board; our link's first failure was because ___."* A student can't write the log → point at their cheat sheet: *"Five stations of the loop — where were you stuck, and how did you get past it? Write that. One sentence is enough."* "I want to play with it at home" → *"That's exactly what it was installed for — it's on your computer, play all you want. And the manual's in your hands."* The link goes to the class group + workbook.

---

### Slide 20 | Today You Moved From Tenant to Owner — Call-to-action

**Type**: Call-to-action · **Time**: 5 min (16:55–17:00)

**On screen** (verbatim):

```text
Today You Moved From Tenant to Owner

[FOUR WINS, yellow left border]
✅ Your project moved off someone else's server and into YOUR OWN COMPUTER — you're the owner
✅ You READ a piece of code for the first time — and changed one line by hand; nothing broke
✅ You DIRECTED AI to build a new project from zero — you ran the engineer's loop
✅ You made TWO BOARDS COOPERATE — one senses, one performs, one wire, one system

[NEXT TIME, white card + black border]
Lesson 7 — Give your project a brief.
Good topics grow from your own experience, not from the internet.
You'll write a requirements sheet: input, logic, output — only one core function survives.
Brief done, the marathon starts.

(small, footer) Project folders stay where they are. Boards in the box.
```

**Instructor notes** (verbatim): *"Look back at today — four things done. One: your project moved off someone else's server and into your own computer — you're the owner. Two: you read a piece of code for the first time, and changed one line by hand — nothing broke. Three: you directed AI to build a new project from zero — you ran the engineer's loop. Four: you made two boards cooperate — one senses, one performs, one wire, one system."* *"Next session preview: give your project a brief. Good topics grow from your own experience, not from the internet. You'll write a requirements sheet: input, logic, output — and only one core function survives. Brief done, the marathon starts — today you said 'I want to build'; soon you'll say 'I'm building.'"* *"Project folders stay where they are. Boards in the box."* No ability-card lighting ceremony today — the ceremony peaks were slide 02 (the close-the-tab demo) and slide 08 (the ownership ritual); this close lands the four wins and previews Lesson 7.

---

## Asset & Placeholder Checklist (from the CN plan + Teacher's Guide L06, localized notes)

| Slide | Asset | Size | Status |
| --- | --- | --- | --- |
| 01 | aily-blockly blocks-view screenshot (an open project) + XIAO board small photo | 400×300 | To capture at rehearsal (English UI) |
| 05 | Board-picker screenshot `screenshot-20260803-154849.png` (user-provided real capture; already in the CN deck's media — English UI) | 740×330 | Reuse as-is |
| 06 | Empty-house four-step screenshots ×4 (new project / board picker with Wio selected / name + save path / created) | 320×200 each | To capture at rehearsal (English UI) |
| 09 | Block ⇄ code side-by-side screenshot (one enlarged block vs its matching lines) | 800×260 | To capture at rehearsal |
| 15 | Grove cable close-up photo (signal + ground inside one cable, clicked into the port) — optional | 400×300 | To photograph at rehearsal (optional) |
| 19 | NLHD repository screenshot — optional | 400×300 | Optional |

**Downgrade**: slide 01 screenshot missing → plain-text cover (the cover is a waiting page); slide 06's four-step screenshots missing → the build-along becomes a live demo on the teacher machine (the page itself carries the four steps — screenshots are seasoning); slide 09's block ⇄ code screenshot missing → live "drag a block and point" on the teacher machine (slide 09 is a reveal page anyway — the screenshot is only the static base); board-picker screenshot missing → keep the page with just the two sentences and point at the live tool. **The prompts and step lists never depend on screenshots — the deck stands as pure text and live demos; nothing here blocks the lesson.**

---

## Backup & Downgrade

- **The install chain (the configuration's biggest flip risk) — three gates:** T-7 trial install fails and can't be solved → decide a week out: fall back to the "Codecraft deepening track" (this lesson becomes a Codecraft polish round + the two-views demonstrated on the teacher machine; Lesson 8's marathon proceeds on Codecraft) — this deck stays in the drawer, don't force it; more than 1/3 of the class didn't install → no in-class rework: extend the checkpoint 5 minutes for a focused group install (all TAs on it), the rest pair up, note it on the reflection page; USB serial disabled on the day → downgrade to "teacher-machine interactive projection + paper walk-through of the new-project loop" (needs still written, AI builds still watched, wiring diagrams still drawn — just nothing flashes; value kept ≈ 60%; flash deferred).
- Slide 02 close-the-tab demo fails live → just do the folder side: *"it lives here now"* — the tab-close can be narrated.
- Slide 03 checkpoint chaos → the 14:18 red line holds regardless; pairing happens on the spot; the 10-minute after-class catch-up is TA A's job.
- Slide 06 build-along lags → whole-class sync *"where I click, you click"*; some students far behind → they finish the empty house during slide 07's tour while the rest follow along.
- Slide 10 someone breaks a line live → teach the save on the spot (that's why engineers save constantly) — the incident IS the lesson.
- Slide 13 serial shows nothing → the three-check, students run it out loud: did it upload? is the monitor open? is the sensor reading? TAs don't operate for them; whole class stuck → teacher-machine demo once (30 seconds), then back to solo.
- Slide 15 link dead → the three checks: did each board run solo? is the signal wire on the agreed pins? is the ground shared (clicked in firmly)? Still dead: unplug and re-seat, or swap in a fresh Grove cable; if it persists, demo one working pair on the teacher machine.
- Time collapse → most compressible: unpack the old project (15→10 min, keeping only the save→confirm ritual) and the bridge (5→2 min); next: joint project (45→35 — release once both programs flash and the signal wire has linked once; the Wio's display flourishes are after-class play) and the night-light (40→32 — slow students release on "one example need runs through"). **Never cut: the two-views 30 minutes, the install-checkpoint red line, the 30-second look-back.**
- Students open new windows to ask about code / state needs → the old rule is on screen (slides 10 / 14 / 16): ask in the conversation you already have — it knows your project.
- The instructor itches to lead the solo blocks → **this lesson's slim-down red line (instructor-side, never on screen): circulate only, "ask, don't fix"** — "What number is 'dark' in your need? How do you know?"

---

## Localization Slots

| Slot | Default | Swap in |
| --- | --- | --- |
| New project (slide 12–14) | night-light (Beginner Kit onboard light sensor + LED, zero wiring) | any sensor your class's main kit has onboard: sound-triggered buzzer, button-controlled light — must satisfy "input is measurable, threshold can be filled by hand" |
| Joint project (slide 15–16) | dusk alarm station (Beginner Kit lookout + Wio alarm post, one Grove cable) | flipped roles: Wio as the lookout (it has an onboard light sensor), the Beginner Kit's buzzer as the alarm post; or a button alarm station (press one, the other rings) — must satisfy "one program per end, one signal wire" |
| The old project to unpack (slide 08) | showing your name on screen (Lesson 1 project) | whatever your class actually built in Lesson 1 (same sentiment works) |
| The change-one-line experiment (slide 10) | name → nickname | a local in-joke: class slogan, a local greeting — anything that's just the letters inside the quotes |
| Fast-lane challenges (slides 13 / 15) | dark-buzzer / Wio shows the reading | per class pace: "Wio button clears the alarm manually" or "screen shows the current light reading" |
| The hotel-vs-own-house line (slide 02) | hotel room vs. your own house | any local pair: rented storage vs. your own room, school locker vs. your desk — the point is "close the tab ≠ it stays" |

---

## 版本记录

| Version | Date | Change |
| --- | --- | --- |
| v1 | 2026-08-25 | First EN deck plan for Lesson 6. 20 pages in five beats. Source: CN deck plan v2 as structural archive (v2.0–v3.2 noted; the colleague-expanded 51-page deck is the CN final form) + EN Teacher's Guide L06 v1 (2026-08-25, based on CN 讲师版 v3). **V3 deltas absorbed: three-check self-test (not four); slide 06 Build Your First Empty House (build-along, Wio Terminal today — a page the CN v2 plan never had); the single-Grove-cable wiring 口径 ("right port + clicked in firmly," not the CN plan's separate signal wire + ground wire); whole-class calls at 15:35 / 16:15 / 16:30.** Red count: 2 (slides 03 and 10). Stand-still pages: 07 / 10 / 13 / 15; cut-ins: 14 / 16 / 17. Terms locked to EN Glossary + EN Teacher's Guide L06. Instructor-side content (14:18 discipline, circulate-three-things, "ask, don't fix," T-7 fallback) never appears on screen. |

---

_English PPT Plan · Lesson 6 · Move Your Project Home v1 ｜ 2026-08-26 ｜ Source: CN deck plan v2 as structural archive (v2.0–v3.2 noted; 51-page colleague-expanded deck = CN final form) + EN Teacher's Guide L06 v1 (2026-08-25, based on CN 讲师版 v3) ｜ Terms locked to EN Glossary + EN Teacher's Guide L06 ｜ Red count: 2 (slides 03 and 10) ｜ Note: this EN deck is a brand rebuild from the V3 teaching structure, not a copy of the 51-page CN file — the Session Map of Teacher's Guide L06 maps each beat to page ranges of the expanded deck for asset sourcing ｜ Next: build the EN .pptx from this plan (brand rebuild, Chaihuo spec; re-capture aily-blockly UI screenshots in English where possible)_
