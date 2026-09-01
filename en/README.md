# M0 · English Edition

_Chaihuo Maker Academy · M0 Smart Hardware Fundamentals · English edition of the M0 course deliverables — localized for native English-speaking learners and teachers._

> **Localized, not translated.** The English edition reworks the teaching intent, stages, timing, and source material of the Chinese edition into classroom language that follows English teaching conventions. A native English-speaking teacher can pick up these documents and teach from them directly. See the methodology in `01_Workflow/`.

---

## Directory map

| Path | Contents | Status |
| --- | --- | --- |
| `01_Workflow/` | **English courseware workflow & methodology v1** — localization principles, English pedagogy adaptation (Bloom's / I-We-You-Do / CFU / wait time), classroom-language standards, cultural-localization rules, five quality gates, production pipeline, naming conventions, roadmap | ✅ |
| `02_Glossary/` | **Bilingual terminology glossary v1** — the arbitration baseline for all English deliverables (with the official anchor at opc.chaihuo.org); chapters 1–14 cover the L0–L3 foundation plus lessons 2–10, logged lesson by lesson (register-before-use enforced from Lesson 4) | ✅ |
| `03_Deliverables/TeacherGuides/` | **English teacher guides ×11 (v1, all lessons shipped)** — Lesson 0 *Before the First Light* + Lesson 1 *Sense and Respond* + Lesson 2 *Find a Problem Worth Solving* + Lesson 3 *Give Your Project a Screen* + Lesson 4 *Assemble Your Team* + Lesson 5 *Teach Your Hardware to See* + Lesson 6 *Move Your Project Home* + Lesson 7 *Brief Your Project* + Lesson 8 *Run the First Lap* + Lesson 9 *Call In Reinforcements* + Lesson 10 *My Project, My Story* | ✅ |
| `03_Deliverables/PPTPlans/` | **English PPT plans ×11 (v1 each)** — Lesson 0 (13 slides) + Lesson 1 (28) + Lesson 2 (22) + Lesson 3 (19) + Lesson 4 (20) + Lesson 5 (20) + Lesson 6 (20) + Lesson 7 (19) + Lesson 8 (42, incl. Brandy appendix) + Lesson 9 (20) + Lesson 10 (13) | ✅ |
| `03_Deliverables/PPTX/` | **English brand-redesigned PPTX ×11 (v1 each, all green)** — L0 (13) + L1 (28) + L2 (22) + L3 (19) + L4 (20) + L5 (20) + L6 (20) + L7 (19) + L8 (42, incl. 25-page Brandy appendix) + L9 (20) + L10 (13); 236 slides total, dual-engine verified | ✅ |
| `03_Deliverables/StudentWorkbooks/` | **English student workbooks ×10 (v1 each)** — Lessons 1–10; structure mirrors the Chinese workbooks 1:1 (sections / fill-in anchors); all verbatim prompts copied from the EN teacher guides' Section 6; Lesson 0 has no workbook | ✅ |
| `03_Deliverables/` | **English semester delivery checklist** CFG-5 v1 — Session 0–10 three-file index + prep requirements + course-wide conventions | ✅ |

## Relationship to the Chinese edition

- **Separate directories**: the Chinese edition lives in `交付物/`; the English edition lives in `en/`. They never overwrite or mix;
- **One-way source**: the English edition is localized from the finalized Chinese teacher guides; each English document header records `Source: CN vX` for traceability;
- **Independent versioning**: the English edition has its own version numbers (starting from v1);
- **Sync discipline**: when the Chinese edition's wording changes, the affected English passages are tagged `[Sync: CN vX → EN]` pending sync.

## Current status (snapshot 2026-08-26)

- **P0** methodology + glossary complete; **P1** Lesson 0 English teacher guide + English semester checklist complete (workflow demo batch); **P2** Lessons 1–3 English teacher guides complete; **P2+** full rollout complete (Lessons 4–10, v1 each, 2026-08-25).
- **P3 English PPT plans complete** — ×11 (Lessons 0–10, v1 each, 236 slides total, delivered in three rolling batches on 2026-08-26): P3a L00–L03 (13 / 28 / 22 / 19) ✅ ／ P3b L04–L06 (20 / 20 / 20) ✅ ／ P3c L07–L10 (19 / 42 / 20 / 13, L08 incl. 25-page Brandy appendix) ✅.
- Structural arbitration applied across all three batches: the EN plans take the EN teacher guides as their structural authority (they do not copy the Chinese plans); the Chinese plans are used only for source material and as a visual skeleton — L09 gained a review-record projection page per the EN zero-print convention (19→20 slides), and L10 added an engineer's checklist page per the EN teacher guide (based on CN guide v3) (12→13 slides).
- Glossary synced through Chapter 14 (Lessons 6–10, register-before-use per lesson, including locked translations for lesson titles, iron rules, sentence patterns, and key quotes).
- **P3 second half · English PPTX brand redesign complete (2026-08-26)**: all 11 decks delivered (v1 each, 236 slides) in `03_Deliverables/PPTX/`. Build pipeline: `PPTX/_build/` — `builder_lib.py` (Chaihuo brand primitive library) + per-lesson build scripts (`build_L00.py`–`build_L10.py`) + dual-engine verification (`verify_deck` text-level: CJK scan / page alignment / red-fill count D84144 / canvas overflow; `verify_layout` geometry-level: Pillow + Arial measurement estimating wrapped line count vs. text-box height), all decks PASS with 0 layout warnings. Zero Chinese / full-width characters / emoji on screen (regex scan `[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]`); ①/②/③/⭐/✅/⚠️/full-width `｜` all replaced with yellow blocks or ASCII (`｜` → `|`); red-discipline ≤4 per lesson (5% red-fill budget per slide count); teacher-side information (iron rules / patrol pacing / three gates / fallback plans / time elasticity band) lives only in speaker notes, never on screen.
- **P4 English student workbooks complete (2026-08-26)**: Lessons 1–10 delivered (v1 each, 10 documents) in `03_Deliverables/StudentWorkbooks/`. Derivation discipline: the Chinese workbooks are the structural source (sections, fill-in anchors, "write here" slots mirrored 1:1; L5 uses the v3 source — incl. the Section 9 Codecraft-output bonus appendix; the rest use v2); the EN teacher guides' Section 6 is the single arbitration source for verbatim prompts (five-round relay sentence patterns, release checklist, README/pitch templates, investor sparring, hardware prompt templates — all copied verbatim); Chinese wiki links removed, English wiki and GitHub links kept; second-person + short-sentence style. Lesson 0 has no workbook.
- **Next: P5 native-speaker review sampling + pilot feedback** — see the Chapter 10 roadmap in the methodology.
- Status sync: `03_Deliverables/M0_EN_CFG5_Semester_Delivery_Checklist_v1.md` quick-reference updated for Sessions 0–10 — all teacher guides v1 + PPT plans v1 + PPTX v1 (Slides column) ✅ + student workbooks v1 (Student Workbook column, L1–L10) ✅.

---

_English edition root README ｜ maintained as the English deliverables are updated. Part of the M0 open course, released under CC BY 4.0 — see `LICENSE.md` / `LICENSE-README.md` at the repository root._
