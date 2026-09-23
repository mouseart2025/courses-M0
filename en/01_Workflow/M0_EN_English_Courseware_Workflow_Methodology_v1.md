# M0 English Courseware Workflow & Methodology

_Version: v1 ｜ 2026-08-25 ｜ Target learners: international learners whose first language is English ｜ Scope: CFG-5 ten-session semester course (to be extended to CFG-1/2 and other configurations)_

> **Positioning in one sentence**: The English edition is not a "translation" — it is a **localized edition**. It preserves the teaching intent, stages, timing, and source material of the Chinese edition (block cards / teacher guides), but rewrites every piece of classroom language according to English classroom conventions, so that **an English-speaking teacher can pick up the document and teach from it directly** — with no need to "understand the Chinese first and then translate on the fly."

---

## 1. Why "localization", not "translation"

### 1.1 Three modes compared

| Mode | Approach | Result | Adopted? |
| --- | --- | --- | --- |
| **Translation** | Sentence-by-sentence rendering | Grammatical but not idiomatic classroom language; a teacher reading it aloud sounds stiff; Chinese-style examples and context remain | ❌ |
| **Localization** | Keep the structure and source; rewrite classroom language, examples, and context to English classroom conventions; lock terminology | A native teacher can "pick it up and teach"; students hear natural classroom English | ✅ This workflow |
| **Recreation** | Start over without reference to the Chinese edition | Huge effort; diverges from the Chinese edition's wording; the two versions become hard to keep in sync | ❌ |

### 1.2 The localization test

One sentence decides whether an English deliverable is good enough:

> **If an English-speaking teacher who knows nothing about China picks up this document and teaches from it for a full session, will the class feel natural?**

If the answer is yes, the localization succeeded. Any sentence that requires "understanding the Chinese original to teach it correctly" is a failed localization and must be rewritten.

### 1.3 What must NOT be localized (keep as-is)

| Content | Reason |
| --- | --- |
| Brand names: Seeed Studio, Chaihuo Makerspace, Codecraft, aily-blockly, SenseCraft AI, Grove Beginner Kit, Wio Terminal, XIAO ESP32S3 Sense, NLHD | Product proper nouns; no English alternative |
| Method names: BMAD, the five roles PM / UX / Architecture / Development / Testing | Branded methodology; keep as-is (BMAD is an established acronym) |
| Case personas: Brandy (Li Shiwen, Seeed Application Engineer) | Real case person; keep the name, translate the title |
| Course codes: M0, CFG-5, block IDs (X0/A1…) | Internal consistency identifiers |

---

## 2. Target profile and source of official wording

### 2.1 Target profile (default for this workflow)

- **Learners**: native English speakers (or CEFR B1+), middle-school / university elective students, zero programming background
- **Teachers**: English-speaking teachers, possibly with no programming background (i.e., the audience of the Chinese edition's "Liang Caimei test")
- **Contexts**: overseas makerspaces, international schools, MakerFaire workshops, partner institutions' English classes

### 2.2 Official wording sources (the glossary must align with these)

1. **Chaihuo Maker Academy's official English site** `opc.chaihuo.org` (English names of the course system, module descriptions)
2. **Course introduction v8** (`需求/柴火创客学园M0 · 零基础智能硬件入门 · 课程介绍.md`) — the latest Chinese wording baseline
3. **Chinese teacher guides / block cards** (the source; input to this workflow)
4. **Global community upgrade plan** (`需求/全球社区升级方案｜内部复盘与建议.md`) — the partner-context wording baseline

Official English expressions already available (glossary anchors):

| Chinese | Official English | Source |
| --- | --- | --- |
| M0 course module name | **M0 Hardware Foundation · Smart Hardware Fundamentals** | opc.chaihuo.org |
| Course positioning | **Build with AI — Create with AI tools, zero coding experience required. Let AI be your programmer while you be the maker.** | opc.chaihuo.org |
| AI-assisted coding | **AI-assisted coding: use natural language to let AI write code** | opc.chaihuo.org |
| Build with AI (direction name) | **Build with AI** | opc.chaihuo.org |

---

## 3. Adapting the classroom structure (pedagogy layer)

The Chinese edition's teaching design (magic moment → concept injection → hands-on work → sharing close-out) is naturally compatible with the classic structure of an English classroom. The English edition explicitly labels the corresponding English pedagogy terms at each stage, so a native teacher instantly recognizes "how this segment is taught."

### 3.1 Each lesson opens with: Learning Objectives

- The Chinese edition has no explicit learning-objectives section. The English edition adds **"By the end of this session, students will be able to…"** at the top of every teacher guide, using **Bloom's taxonomy** action verbs (describe / explain / build / test / pitch…), never unobservable verbs like "learn / know / understand".
- 2–4 objectives, mapped directly to the lesson's acceptance criteria.

### 3.2 Stage structure: I Do → We Do → You Do

The Chinese edition's "demo → co-build → independent work" maps onto the standard English classroom three-part structure:

| Chinese-edition stage | English pedagogy | Teacher-guide label |
| --- | --- | --- |
| Teacher demo / concept talk | **I Do** (teacher modeling) | each segment labeled `[I Do]` |
| Guided sentence practice / whole-class interaction | **We Do** (guided practice) | labeled `[We Do]` |
| Students hands-on / independent task | **You Do** (independent practice) | labeled `[You Do]` |
| Sharing / acceptance | **Share-out & Check** | labeled `[Share-out]` |

> The labels do not change content; they only tell the teacher "what my role is in this segment."

### 3.3 End of each segment: Check for Understanding (CFU)

The Chinese edition's "three questions" / "randomly ask 3 students" is formative assessment. The English edition uses the standard term **Check for Understanding (CFU)** and gives concrete prompts (see the sentence bank in Section 4), e.g.:

- **Thumbs up / middle / down** — quick whole-class vote
- **Turn to your neighbor and explain…** — pair re-explanation (think-pair-share)
- **One sentence: what are we doing in this course?** — random call to land the point

### 3.4 Key pause: Wait Time

The Chinese edition's Lesson 0, page 12 "stay silent for 30 seconds" is the classic **wait time** technique (Rowe, 1972). The English edition keeps it and labels it explicitly `[Wait time: 30 s — do not fill the silence]` — a standard English-classroom training habit that native teachers fully endorse.

### 3.5 Differentiation

The Chinese edition's "time elasticity" (compressible / non-compressible segments) is resource allocation for differentiation. The English edition labels it:

- **Non-negotiable** (non-compressible: the lesson's memory points / core-output segments)
- **Flexible** (compressible: background-setting segments)

### 3.6 Classroom Management

The Chinese edition's "iron rule: no hand-written code" translates more naturally as **House rule** in an English classroom — English teachers are used to "establishing house rules" in the first session. The teacher guide keeps the "announce it as good news" tone (frame it positively).

---

## 4. Classroom Language Standards

### 4.1 Six hard rules

1. **Use the second person**: address learners throughout as **you**; never make "the students / learners / kids" the subject.
2. **Imperatives that start with action verbs**: not "I would like you to…", but **"Open Codecraft and log in."**
3. **Short sentences first**: no more than 20 words per sentence; on-screen sentences must sound conversational when read aloud verbatim.
4. **Separate teacher talk from student talk**: the teacher guide distinguishes **Say this** (teacher reads aloud, verbatim) from **Students say/do** (student responses).
5. **Avoid Chinglish**: see the checklist in 4.2.
6. **Terminology goes through the glossary only**: use the same word for the same concept throughout every document; see Section 5.

### 4.2 Common Chinglish avoidance checklist (partial; the full version is in the glossary)

| Chinese meaning | ❌ literal | ✅ classroom English |
| --- | --- | --- |
| 会感知，会应答 | Sensing and responding | Sense and respond (imperative/noun-phrase parallelism; matches lesson-naming convention) |
| 让 AI 写代码 | let AI write the code for you | **Let AI do the coding** (more conversational) |
| 点亮板子 | light up the board | **get the board glowing / make the board light up** |
| 翻车点 | flipped car points | **common pitfalls / what can go wrong** |
| 巡场看什么 | what to patrol | **what to look for while students work** |
| 留白 | leave blank | **wait time / silence** (pedagogy term) |
| 双保险 | double insurance | **backup plan / plan B** |
| 收口 | close the mouth | **land the point / wrap up** |

### 4.3 Classroom sentence bank (shared by every lesson; teacher guides quote these directly)

| Function | Sentence (verbatim) |
| --- | --- |
| Opening | "Welcome to Chaihuo Maker Academy. Here's what we'll do today — and no, you don't need to know how to code. Not a single line." |
| Transition | "Okay, big picture done. Let's get our hands on it." / "Before we move on — quick check." |
| Giving instructions | "Turn to the person next to you and tell them one thing that annoys you in your daily life." |
| Guided practice (We Do) | "Read it with me: 'Say it clearly, watch what happens, tell it to change.'" |
| CFU | "Thumbs up if you've got it. Middle if you're not sure. Down if you're lost — no shame, that's what I'm here for." |
| Wait time | "Don't answer yet. Thirty seconds. Just think." |
| Close-out | "Before you leave, write down one sentence: the small thing in your life that annoys you. That's your ticket to Lesson 2." |

---

## 5. Glossary Discipline

1. **Mandatory reference**: before producing any English document, first read `02_Glossary/M0_EN_Glossary_CN_EN_v1.md`; every course term that appears must match the glossary.
2. **New-term process**: when you hit a concept not yet in the glossary → register it in the glossary first (Chinese + English + context + source), then use it in documents; never improvise a translation on the spot.
3. **One concept, one word**: e.g., "学员文档" is **Student Workbook** everywhere across the whole system; do not mix handout / worksheet / learner sheet.
4. **Official wording wins**: when an official English expression already exists (e.g., "Let AI be your programmer while you be the maker" on opc.chaihuo.org), adopt it rather than inventing a new one.

---

## 6. Cultural Localization Rules

| Category | Rule | Example |
| --- | --- | --- |
| Brand background | Keep the brand names; add one English-context sentence | "Chaihuo Makerspace — China's first makerspace, founded in 2011, supported by Seeed Studio." |
| Everyday examples | Choose cross-cultural, universal scenarios; rephrase China-specific scenarios into universal phrasing (the "grandma taking pills" example must keep its universal "caring for family" meaning) | Chinese "the classroom light no one turns off / grandma misremembering her pills / forgetting to water the plants" → English "the classroom light left on every night / a family member forgetting their pills / plants that never get watered" |
| Parent communication | "parent-present version" → **Parent note** (common in English schools); keep the wording intent but rewrite the tone | "What if my child isn't learning to code?" → "This course builds the thinking — the code comes later, and AI writes it. The four things we practice — spotting problems, judging results, understanding people, making decisions — are exactly what no AI can hand them." |
| Internal test names | 梁彩梅测试 → **The New-Teacher Test** (readable aloud by a teacher with no programming background); 小航测试 → **The Absolute-Beginner Test** (from the perspective of a complete beginner) | Used for naming the English-edition quality gates |
| Institutional context | China-specific contexts ("Chaihuo base truck parade / MakerFaire Shenzhen") are downplayed in the teacher-guide body, kept only on background slides | The teacher-guide body focuses on "small things around you", independent of Chinese context |
| Student output narrative | "show it to your parents" → "show your family and friends" | universalized |

---

## 7. Quality Gates

Every English deliverable must pass the following five gates in order before release (the upgraded version of the Chinese edition's "Liang Caimei test + Xiaohang test"):

| Gate | Name | What it checks | If it fails |
| --- | --- | --- | --- |
| **G1 Term consistency** | Glossary Check | Every term in the text compared against the glossary, one by one; no improvised translations | Send back to revise terminology |
| **G2 Source fidelity** | Source Fidelity | Compared segment by segment with the Chinese teacher guides / block cards: stages, timing, wording, and failure plans are **neither added nor removed** (change only expression, not content) | Send back to add/trim |
| **G3 Native readability** | The Aloud Test | A native English-speaking teacher reads the whole document **cold** (no prep) aloud without stumbling and without feeling "this reads like a translation" | Send back to rewrite awkward sentences |
| **G4 Pedagogy completeness** | Pedagogy Check | Every lesson has Bloom's learning objectives; every segment has I/We/You Do labels; every segment has a CFU; key pauses labeled as wait time | Send back to add labels |
| **G5 Timing/stage conservation** | Timing Fidelity | Stage durations match the Chinese edition exactly (the English edition does not change the course pacing) | Send back to check the overview table |

> The first four gates are self-checked by AI at production time plus user spot-checks; **G3 native readability is the only gate where we recommend bringing in an external human native speaker**, spot-audited once every 2–3 lessons per batch.

---

## 8. English-edition production pipeline

The English edition does **not** repeat the full Chinese pipeline that starts from the block cards. It starts from the **finalized Chinese teacher guides** and localizes from there (the Chinese teacher guides have already passed G1–G8 and the Liang Caimei / Xiaohang tests, so the content is trusted):

```
Chinese teacher guides (finalized; the source)
      ↓
① Read the glossary + official English wording (opc.chaihuo.org) → lock this lesson's terms
      ↓
② English localization rewrite (I/We/You Do labels + Bloom objectives + CFU + classroom sentences)
      ↓
③ Quality gates G1 → G2 → G4 (G3 spot-audited) → release once passed
      ↓
④ English student workbooks (derived from the English teacher guides; same term/sentence baseline)
      ↓
⑤ English PPT plans (page-level: titles, on-screen sentences, and speaker scripts all in English)
      ↓
⑥ English PPTX (Chaihuo brand spec; fonts need a check for the Chinese-asset replacement/retention strategy)
```

**Sync discipline**: any "term lock" in any stage of the English edition is arbitrated solely by the glossary; when the Chinese edition's wording changes → check the affected English passages and tag them in the English documents with `[Sync: CN vX → EN]` pending sync.

---

## 9. Naming and directory conventions

### 9.1 Directories (fully separate from the Chinese edition)

```
en/                            ← English-edition root (parallel to the Chinese `交付物/`; never overwrites it)
├── README.md                  English-edition overview
├── 01_Workflow/               Workflow & methodology
├── 02_Glossary/               Glossary
└── 03_Deliverables/           English deliverables
    ├── TeacherGuides/         English teacher guides
    ├── StudentWorkbooks/      English student workbooks
    └── Slides/                English slides
```

### 9.2 Naming

- Teacher guide: `M0_EN_TeacherGuide_CFG-5_LessonNN_<ShortName>_vX.md`
  - Example: `M0_EN_TeacherGuide_CFG-5_Lesson00_BeforeFirstLight_v1.md`
- Student workbook: `M0_EN_StudentWorkbook_CFG-5_LessonNN_<ShortName>_vX.md`
- Semester checklist: `M0_EN_CFG5_Semester_Delivery_Checklist_vX.md`
- Versioning is decoupled from the Chinese edition (the English edition numbers independently, starting from v1), but each document header records `Source: Chinese vX` for traceability.

### 9.3 English lesson names (Lesson 0 settled; the rest confirmed with the user lesson by lesson during production)

| Lesson | Chinese name | English name (v1 suggestion) |
| --- | --- | --- |
| Lesson 0 | 先导课 · 点亮之前 | **Lesson 0 · The Kickoff: Before the First Light** |
| Lesson 1 | 会感知，会应答 | Sense and Respond (to be confirmed per lesson) |

---

## 10. Roadmap

| Phase | Contents | Status |
| --- | --- | --- |
| P0 | Workflow methodology (this document) | ✅ v1 done |
| P0 | Glossary v1 (Chinese–English) | ✅ synced with this document |
| P1 | Lesson 0 English teacher guide + English semester checklist (demonstration; validates the workflow) | ✅ v1 done |
| P2 | Lessons 1–3 English teacher guides (first three lessons of the full rollout) | To start |
| P3 | English PPT plans + PPTX (brand redesign) | To start |
| P4 | English student workbooks (lesson by lesson) | To start |
| P5 | Full-course English edition + native-speaker review sampling + pilot feedback | To start |

---

_Changelog: v1 (2026-08-25) first draft: defined the localization methodology, pedagogy adaptation, glossary discipline, five quality gates, the English-edition pipeline, and directory conventions; demonstration lesson is Lesson 0._
