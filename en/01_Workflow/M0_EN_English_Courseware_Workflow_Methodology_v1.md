# M0 英文版课件工作流与方法论（English Courseware Workflow & Methodology）

_版本：v1 ｜ 2026-08-25 ｜ 目标学员：以英语为母语的国际学员 ｜ 适用范围：CFG-5 十次课学期班（后续扩展到 CFG-1/2 等配置）_

> **一句话定位**：英文版不是"翻译版"，是**本地化版本（localized edition）**——保留中文版的教学意图、环节、时长与信源（积木卡/讲师版），但按英语课堂的惯例重写每一句课堂语言，使**一位英语母语教师可以拿起文档直接照讲**，不需要"先理解中文再转译"。

---

## 一、为什么是"本地化"，不是"翻译"

### 1.1 三种模式的区别

| 模式 | 做法 | 结果 | 是否采用 |
| --- | --- | --- | --- |
| **直译（Translation）** | 逐句翻译 | 句子通顺但课堂语言不地道，教师照念会显得生硬；中式例子与语境残留 | ❌ |
| **本地化（Localization）** | 保留结构与信源，按英语课堂惯例重写课堂语言、例句与语境，术语锁定 | 母语教师可以"拿来就讲"，学生听到的是自然课堂英语 | ✅ 本工作流采用 |
| **重做（Recreation）** | 脱离中文版另起炉灶 | 工作量巨大，且与中文版口径分叉，双版本难以同步维护 | ❌ |

### 1.2 本地化的判断标准

一份英文版交付物合格与否，用一句话检验：

> **If an English-speaking teacher who knows nothing about China picks up this document and teaches from it for a full session, will the class feel natural?**

（一位对中国一无所知的英语母语教师，拿这份文档上一整节课，课堂会不会显得自然？）

如果答案是"会"，说明本地化成功。任何需要"了解中文原意才能讲对"的句子，都是失败的本地化，必须重写。

### 1.3 不可本地化的内容（必须保留原文）

| 内容 | 原因 |
| --- | --- |
| 品牌名：Seeed Studio、Chaihuo Makerspace、Codecraft、aily-blockly、SenseCraft AI、Grove Beginner Kit、Wio Terminal、XIAO ESP32S3 Sense、NLHD | 产品专名，无英文替代 |
| 方法名：BMAD、PM / UX / 架构 / 开发 / 测试 五角色 | 品牌方法论，直接保留（BMAD 是既有缩写） |
| 案例人物：Brandy（李世雯，Seeed Application Engineer） | 真实案例人物，姓名保留，头衔译英 |
| 课程代号：M0、CFG-5、积木编号（X0/A1…） | 内部一致性标识 |

---

## 二、目标画像与口径来源

### 2.1 目标画像（本工作流默认）

- **学员**：以英语为母语（或 CEFR B1 以上）的中学生/高校通识课学生，零编程基础
- **教师**：英语母语教师，可能无编程背景（即中文版"梁彩梅测试"的对象）
- **场景**：海外创客空间、国际学校、MakerFaire 工作坊、partner 机构英文班

### 2.2 官方口径来源（术语表必须对齐）

1. **柴火创客学院英文官网** `opc.chaihuo.org`（课程体系英文名、模块描述）
2. **课程介绍 v8**（`需求/柴火创客学院M0 · 零基础智能硬件入门 · 课程介绍.md`）——最新中文口径
3. **中文版讲师版 / 积木卡**（信源，本工作流的输入）
4. **全球社区升级方案**（`需求/全球社区升级方案｜内部复盘与建议.md`）——partner 场景口径

已有官方英文表述（术语表锚点）：

| 中文 | 官方英文 | 出处 |
| --- | --- | --- |
| M0 课程模块名 | **M0 Hardware Foundation · Smart Hardware Fundamentals** | opc.chaihuo.org |
| 课程定位 | **Build with AI — Create with AI tools, zero coding experience required. Let AI be your programmer while you be the maker.** | opc.chaihuo.org |
| AI 辅助编程 | **AI-assisted coding: use natural language to let AI write code** | opc.chaihuo.org |
| 用 AI 造物（方向名） | **Build with AI** | opc.chaihuo.org |

---

## 三、英文课堂结构适配（教学法层）

中文版的教学设计（魔法时刻 → 概念注入 → 动手实操 → 分享收尾）与英语课堂的经典结构天然兼容。英文版在每个环节显式标注对应的英语教学法术语，让母语教师一眼认出"这段该怎么上"。

### 3.1 每节课开头：Learning Objectives（学习目标）

- 中文版没有显式的学习目标段，英文版每节课讲师版开头新增 **"By the end of this session, students will be able to…"** 段，动词用 **Bloom's taxonomy** 的行为动词（describe / explain / build / test / pitch…），不用"learn / know / understand"这类不可观测动词。
- 目标数量 2–4 条，直接对应本课验收标准。

### 3.2 环节结构：I Do → We Do → You Do

中文版的「演示 → 共做 → 独立做」映射到英语课堂标准三段式：

| 中文版环节 | 英文教学法 | 讲师版标注 |
| --- | --- | --- |
| 讲师演示 / 讲概念 | **I Do**（teacher modeling） | 讲师版每段标注 `[I Do]` |
| 带读句式 / 全班互动 | **We Do**（guided practice） | 标注 `[We Do]` |
| 学员动手 / 独立任务 | **You Do**（independent practice） | 标注 `[You Do]` |
| 分享 / 验收 | **Share-out & Check** | 标注 `[Share-out]` |

> 标注不改变内容，只帮助教师判断"这一段我的角色是什么"。

### 3.3 每段末尾：Check for Understanding（CFU）

中文版的"三问""随机问 3 名学员"就是 formative assessment，英文版用标准术语 **Check for Understanding (CFU)** 标注，并给出具体口令（见第四节句式库），例如：

- **Thumbs up / middle / down** — 快速全班投票
- **Turn to your neighbor and explain…** — 结对复述（think-pair-share）
- **One sentence: what are we doing in this course?** — 随机点名收口

### 3.4 关键停顿：Wait Time

中文版第 0 课页 12 的"留白 30 秒不说话"是经典的 **wait time**（Rowe, 1972）技巧。英文版保留并显式标注 `[Wait time: 30 s — do not fill the silence]`，这正是英语课堂的训练惯例，母语教师完全认同。

### 3.5 差异化教学：Differentiation

中文版的"时间松紧带"（可压/不可压环节）就是差异化教学的资源分配。英文版标注为：

- **Non-negotiable**（不可压缩：本课记忆点/核心产出环节）
- **Flexible**（可压缩：背景铺陈环节）

### 3.6 课堂管理：Classroom Management

中文版"铁律：严禁手写代码"在英语课堂语境中翻译为 **House rule**（课堂公约）更自然——英语教师习惯在开学/开课第一讲"establish house rules"。讲师版保留"当好消息讲"的语气（frame it positively）。

---

## 四、课堂语言规范（Classroom Language Standards）

### 4.1 六条硬规范

1. **用第二人称**：通篇称呼学员为 **you**，不用 "the students / learners / kids" 做主语。
2. **指令用祈使句、动作动词开头**：不说 "I would like you to…"，说 **"Open Codecraft and log in."**。
3. **短句优先**：一句话不超过 20 词；投屏句式逐字照念时必须口语化。
4. **教师话语与学生话语分离**：讲师版区分 **Say this**（讲师口播，逐字）与 **Students say/do**（学员反应）。
5. **避免中式英语（Chinglish）**：见 4.2 清单。
6. **术语只走术语表**：同一个概念全文档用同一个词，见第五章。

### 4.2 常见 Chinglish 规避清单（局部示例，完整版见术语表）

| 中文原意 | ❌ 直译 | ✅ 课堂英语 |
| --- | --- | --- |
| 会感知，会应答 | Sensing and responding | Sense and respond（祈使/名词短语并列，符合课名习惯） |
| 让 AI 写代码 | let AI write the code for you | **Let AI do the coding**（更口语） |
| 点亮板子 | light up the board | **get the board glowing / make the board light up** |
| 翻车点 | flipped car points | **common pitfalls / what can go wrong** |
| 巡场看什么 | what to patrol | **what to look for while students work** |
| 留白 | leave blank | **wait time / silence**（教学术语） |
| 双保险 | double insurance | **backup plan / plan B** |
| 收口 | close the mouth | **land the point / wrap up** |

### 4.3 课堂句式库（每一课通用，讲师版直接引用）

| 功能 | 句式（逐字可用） |
| --- | --- |
| 开场 | "Welcome to Chaihuo Maker Academy. Here's what we'll do today — and no, you don't need to know how to code. Not a single line." |
| 过渡 | "Okay, big picture done. Let's get our hands on it." / "Before we move on — quick check." |
| 下指令 | "Turn to the person next to you and tell them one thing that annoys you in your daily life." |
| 带读（We Do） | "Read it with me: 'Say it clearly, watch what happens, tell it to change.'" |
| CFU | "Thumbs up if you've got it. Middle if you're not sure. Down if you're lost — no shame, that's what I'm here for." |
| Wait time | "Don't answer yet. Thirty seconds. Just think." |
| 收尾 | "Before you leave, write down one sentence: the small thing in your life that annoys you. That's your ticket to Lesson 2." |

---

## 五、术语表制度（Glossary Discipline）

1. **强制引用**：产出任何英文版文档前，先读 `02_Glossary/M0_EN_Glossary_CN_EN_v1.md`；文档中出现的每个课程术语必须与术语表一致。
2. **新增术语流程**：遇到术语表未收录的概念 → 先在术语表登记（中文 + 英文 + 场景 + 出处），再用于文档，不允许临场自译。
3. **同一概念一个词**：如 "学员文档" 全体系统一 **Student Workbook**，不得混用 handout / worksheet / learner sheet。
4. **官方优先**：官方英文（opc.chaihuo.org）已存在的表述（如 "Let AI be your programmer while you be the maker"）优先采用，不另造。

---

## 六、文化本地化规则（Cultural Localization）

| 类别 | 规则 | 示例 |
| --- | --- | --- |
| 品牌背景 | 保留品牌名，补充一句英文语境说明 | "Chaihuo Makerspace — China's first makerspace, founded in 2011, supported by Seeed Studio." |
| 生活例子 | 选用跨文化通用场景；中国特有场景（四点半课堂、奶奶吃药需保留"照顾家人"的普适性）改述为通用表述 | 中文"教室灯没人关/奶奶吃药记错时间/忘浇花" → 英文 "the classroom light left on every night / a family member forgetting their pills / plants that never get watered" |
| 家长沟通 | "家长在场版本" → **Parent note**（英语学校惯用），保留口径但重写语气 | "What if my child isn't learning to code?" → "This course builds the thinking — the code comes later, and AI writes it. The four things we practice — spotting problems, judging results, understanding people, making decisions — are exactly what no AI can hand them." |
| 内部测试名 | 梁彩梅测试 → **The New-Teacher Test**（无编程背景教师照念可讲）；小航测试 → **The Absolute-Beginner Test**（零基础学员视角） | 用于英文版质量关卡命名 |
| 机构语境 | "柴火基地车巡游/MakerFair 深圳" 等中国场景在讲师版正文弱化，只在背景页保留 | 讲师版正文聚焦"你身边的小事"，不依赖中国场景 |
| 学员产出叙事 | "给爸妈看" → "show your family and friends" | 通用化 |

---

## 七、质量关卡（Quality Gates）

英文版每一份交付物在发布前必须依次通过以下五关（对应中文版"梁彩梅测试+小航测试"的升级版）：

| 关卡 | 名称 | 检查内容 | 不通过的处理 |
| --- | --- | --- | --- |
| **G1 术语一致性** | Glossary Check | 全文术语与术语表逐条比对，无临场自译 | 打回修订术语 |
| **G2 信源一致性** | Source Fidelity | 与中文版讲师版/积木卡逐段对照：环节、时长、口径、翻车预案**不增不减**（只改表达，不改内容） | 打回补齐/删减 |
| **G3 母语可读性** | The Aloud Test | 一位英语母语教师**冷读**（拿到不预习）逐字念完全文不卡壳、不觉得"这是翻译腔" | 打回重写不顺的句子 |
| **G4 教学法完备** | Pedagogy Check | 每节课有 Bloom's 学习目标；每段有 I/We/You Do 标注；每段有 CFU；关键停顿标注 wait time | 打回补齐标注 |
| **G5 时间/环节守恒** | Timing Fidelity | 与中文版环节时长完全一致（英文版不改变课程节奏） | 打回核对总览表 |

> 前四关由 AI 产出时自检 + 用户抽查；**G3 母语可读性是唯一建议引入外部真人（native speaker）把关的关卡**，可在每批 2–3 课后抽审一次。

---

## 八、英文版生产流水线

英文版**不重复**中文版从积木卡开始的完整流水线，而是从"已定版的中文讲师版"出发做本地化（中文讲师版已经过 G1–G8、梁彩梅/小航测试，内容可信）：

```
中文讲师版（已定版，信源）
      ↓
① 读术语表 + 官方英文口径（opc.chaihuo.org）→ 锁定本课术语
      ↓
② 英文本地化改写（I/We/You Do 标注 + Bloom 目标 + CFU + 课堂句式）
      ↓
③ 质量关卡 G1 → G2 → G4（G3 抽审）→ 通过后发布
      ↓
④ 英文学员文档（由英文讲师版派生，同一术语/句式口径）
      ↓
⑤ 英文 PPT 策划（页面级：标题、投屏句式、讲稿全英文）
      ↓
⑥ 英文 PPTX（柴火品牌规范，字体需检查中文素材替换/保留策略）
```

**同步纪律**：英文版任何一环的"术语锁定"以术语表为唯一仲裁；中文版口径更新 → 检查英文版受影响段落，在英文版文档内标注 `[Sync: CN vX → EN]` 待同步标记。

---

## 九、命名与目录规范

### 9.1 目录（与中文版完全分开）

```
交付物_EN/                  ← 英文版根目录（与中文版「交付物/」并列，互不覆盖）
├── README.md               英文版总览
├── 01_Workflow/             工作流与方法论
├── 02_Glossary/             术语表
└── 03_Deliverables/         英文交付物
    ├── TeacherGuides/       英文讲师版
    ├── StudentWorkbooks/    英文学员文档（后续）
    └── Slides/              英文演示文稿（后续）
```

### 9.2 命名

- 讲师版：`M0_EN_TeacherGuide_CFG-5_LessonNN_<ShortName>_vX.md`
  - 例：`M0_EN_TeacherGuide_CFG-5_Lesson00_BeforeFirstLight_v1.md`
- 学员文档：`M0_EN_StudentWorkbook_CFG-5_LessonNN_<ShortName>_vX.md`
- 学期清单：`M0_EN_CFG5_Semester_Delivery_Checklist_vX.md`
- 版本号与中文版解耦（英文版独立编号，从 v1 起），但文档头标注 `Source: 中文版 vX` 追溯信源。

### 9.3 课名英文译名（第 0 课已定，其余课次在逐课产出时与用户确认）

| 课次 | 中文课名 | 英文课名（v1 建议） |
| --- | --- | --- |
| 第 0 课 | 先导课 · 点亮之前 | **Lesson 0 · The Kickoff: Before the First Light** |
| 第 1 课 | 会感知，会应答 | Sense and Respond（待逐课确认） |

---

## 十、路线图

| 阶段 | 内容 | 状态 |
| --- | --- | --- |
| P0 | 工作流方法论（本文档） | ✅ v1 完成 |
| P0 | 术语表 v1（中英对照） | ✅ 与本文档同步 |
| P1 | 第 0 课英文讲师版 + 英文学期清单（示范，验证工作流） | ✅ v1 完成 |
| P2 | 第 1–3 课英文讲师版（正课批量铺开的首三课） | 待启动 |
| P3 | 英文版 PPT 策划 + PPTX（品牌重制） | 待启动 |
| P4 | 英文学员文档（逐课） | 待启动 |
| P5 | 全课英文版 + 母语审校抽审 + 试讲回填 | 待启动 |

---

_版本记录：v1（2026-08-25）初版：确定本地化方法论、教学法适配、术语表制度、五道质量关卡、英文版流水线与目录规范；示范课次第 0 课。_
