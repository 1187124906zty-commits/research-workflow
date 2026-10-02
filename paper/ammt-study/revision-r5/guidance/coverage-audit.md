# R5 写作指导覆盖与落实审计

建议接收本轮调查为**有限的指导补充与接收方法**：现有写作技能已具备章节目的、文献综合、反向提纲和证据边界；需要补强的是句内／句间可执行诊断、对象进入与比较归属，以及让短方法确实进入显式 writing 任务并在实际稿件上核验。不能把冻结稿的每个读者问题归为“技能没有指导”，也不能以新增指南或 loader 测试通过替代修稿结果。

## 范围、曝光与原件

审计读取了两个仓库 AGENTS.md；MAF 当前 writer/reviewer role charters；scientific-writing、scientific-editor、paper-writing-review 与四个 section skills；section-specific-guidance、source-use、argument-and-readers、institution-guidance、review-and-handoffs；`src/research_assistant/guidance.py`，并补读 `engine.py` 的请求／review 路由和 `tests/test_writing_guidance.py`。未修改上述文件。

全文读取冻结的 `revision-r5/manuscript-input.tex`，并以行号定位应用例子。对稿件研究问题、方法设计和解释均有曝光；本轮没有先读取领域原始结果再盲审解释，也未重新审核领域文献、数值原件或渲染页。因此结论限于**指导覆盖、路由行为和实际文字的读者连续性**，不认证数值精度、原文引用事实、物理因果或投稿合规。同模型评阅不构成统计独立。

来源工作实际抓取读取了 Duke resource introduction、Lessons 1–2 和 Williams principles summary；Purdue Reverse Outlining；UNC Transitions、Scientific Writing；MIT CEE Journal Article、Broad Introduction。另回读 R4 已保存的 MIT Abstract、MIT Methods、UNC Paragraphs 全部实质指南，并检查 PLOS structuring paper 的 Rules 1、3、5–9 对应原文。所有读取范围、出处、短引和许可在 [source-ledger.md](source-ledger.md) 与 JSON 中。新抓取页面的完整本地记录在 `sources/`，供私有读原件，不随复用技能发布。

Gopen/Swan 出版社原页面本轮仍返回 503；CMU 候选镜像返回 404；Purdue 候选 cohesion 路径返回 404。未读取这些失败页面，不把 Duke 的制度性教学综合当成已读 Gopen/Swan 1990 原文。Duke 直接覆盖本轮需要的读者预期，不需为补齐名单继续扩大搜索。

## 既有内容、路由和落实必须分别判断

| 所需能力 | 调查起点已有内容 | 有意义的缺口与处置 |
|---|---|---|
| 原始来源、断言范围和谱系 | source-use 已要求具体断言对具体来源、方法原始出处、区分原文／综合／推断；Introduction guide 要比较条件和承认已有成功 | **部分操作细节缺失**：给新对象身份和角色、命名可展开比较、区别“来源方法”与“来源执行”可更明确。用短方法补充，科学 provenance 不归因给大学语法规则。 |
| 主语／动作与句内信息顺序 | Methods guide 和 UNC synthesis 已说清楚科学主语与动作、主动／被动按功能选择；现有 continuity guide 已要求稳定名词／指代 | **细粒度诊断缺失**：没给临时标出主语、主动作、old premise、new item 的执行步骤；没显式区分可理解主题推进与偶然 subject shifting。Duke Lessons 1–2 提供直接原件。 |
| 稳定前件与从句关系 | 已要求指代无歧义和转接有科学关系 | **已有原则未充分操作化**：用候选前件测试和 this + named noun 修复。冻结 L290、L292 是应用目标，不能只再重复“清楚”。 |
| Cohesion 与 coherence | UNC 段落／转接与 continuity guide 有控制判断、反向提纲与真实关系 | **已有内容＋新判别**：相邻句能回接与整段是否还支撑控制判断分别检查；不能由流畅句链直接接受游移段。Duke Lesson 2 给明确区分。 |
| 反向提纲 | section-specific continuity 已要求段落控制思想与前接／后交；argument guide 要整篇论证链 | **已经覆盖**，Purdue 给新的直接程序出处，不必声称新发明。保留主题＋全篇作用的两列；不采用固定 5–10 词硬门槛。 |
| 证据类型的 Introduction | 既有引言技能要求已知认识→具体问题→设计，按条件综合；核心技能区别 empirical/theory/review/design | **统筹细分曾不足**：数值、实验、理论、混合引言各需要何种背景与设计理由，可由 chapter-contracts 的项目分类明确。机构来源支持逻辑目的，不发布该分类表。 |
| Methods–Results 责任与标题／摘要／结尾闭合 | 既有四个章节技能、scientific-editor 和 argument guide 已覆盖职责、量和证据；title/abstract 和结尾 guide 有一致性检查 | **已有指导＋协调执行细节**：共同量／比较图谱和承诺回查有用；同责任人不是印刷章节合并规则，不应笼统宣称旧 skill 无此内容。 |
| 章节开头 | writer charter、scientific-editor、argument guide 明说按需要承接，不强制相同 roadmap | **已经覆盖**。冻结稿 Methods 2.1 L63 与 Results L176 已有局部目的；不能自动加一段只为格式齐全。缺口只在真实前提丢失处修复。 |
| 最终接收与再查 | review-and-handoffs 已有 location、basis、consequence、owner、smallest repair、recheck；要求协调者关闭实际修复 | **已有接收方法**。指南文本与执行测试不能证明其应用、独立阅读或期刊质量；需用命名薄弱处的实际修复确认。 |

本轮期间协调者新增了 MAF `chapter-contracts.md` 和 `object-and-continuity.md`。我已读这两份实际文件：职责、证据类型、章节开头的项目归属清楚；对象／比较方法明确区分 Duke 读者依据与项目科学编辑方法，未把教学建议写成因果证据。建议在对象短指南中补上临时句标注、唯一前件和 cohesion/coherence 双检验三个执行点；不需要再复制一套重复章节指南。以上是**进行中的 R5 补充**，不能倒写成调查起点就有的内容。

## 实际路由：有链接不等于正文已装入

在审计时的 `guidance.py`：

- writer 无 metadata 时获得 scientific-writing 和 scientific-editor，但没有四个分节技能。
- 显式 `{mode, sections}` 被验证后选择对应分节；reviewer 有 selection 时加 scientific-writing 和 paper-writing-review，coordinator 有 selection 时也获得 scientific-editor。
- `skill_text()` 读取的是各 skill 的 SKILL.md。reference 正文当时以相对链接提示阅读，未由 loader 自动嵌入；这是一种渐进阅读设计，能够到达但不能证明被实际读取。
- `selected_skills('reviewer', None)` 本身不装 writing skills。不过 **engine.py 有 legacy writer review fallback**：review packet 标记 writing_review 后，Session.request 另附 scientific-writing 和 paper-writing-review。不能由前一事实推成“旧 writer 的 reviewer 完全无写作指导”。该 fallback 仍不选择所有章节，符合未指定 scope 的小输入目的。
- checkout 中没有 `src/research_assistant/resources`，当前 root 按 guidance.py 回到仓库 skills/roles；wheel 有 bundled resources 时优先它。分发包的副本是否及时更新，需项目构建验证，本轮不宣称已检查 wheel。

`test_writing_guidance.py` 检查 selection 验证、不同角色的 skill 分配、渐进链接存在、scope 到 worker/reviewer/disposition 的传播及反馈绑定。这些测试有实际流程价值，但 docstring 已说明并非 literary quality 的替代物。最小改进是在显式 writing scope 中直接给一份必要的短对象／句间方法；全稿／协调 scope 给章节依赖方法。保留无 scope 的窄输入，不把全部大学原文塞入 prompt。

自动加载后的验证应包含：请求中实际有对应短方法；真实写作样例能修复一个命名对象／比较归属问题；实际 reviewer 能找出至少一个残余语义缺陷；协调者根据修订稿作有限接收。只有字符串或 schema 测试不够支撑“写作质量改善”。本轮并未修改或运行 loader 的实现；实现和测试由协调者负责。

## 冻结稿中的落实证据与最小修复

| 定位 | 证据、受影响理解与严重程度 | 最小有用修复／核验 |
|---|---|---|
| L30 abstract / “reference means” | 抽象读者未见 Methods，不知道这是何种边界／观察。正文 L82 给独立影像与金相人群。**中等读者缺陷**，不是均值事实错误的认定。 | 用测量类型明确宽／深比较，如金相参考均值；摘要不用复制所有类群和 uncertainty provenance。核验不把长度代理、融合包络与金相混为同一量。 |
| L44 first AMMT | 全稿使用 AMMT 而未给长形式；新缩写身份未建立。**中等读者缺陷**。 | 文献责任人据 Lane/NIST 原件确认官方名称，然后首次展开并给 benchmark 角色；无需额外求解。 |
| L290 / “Their contrast” | 同段既有前驱拟合设计，又有当前 fixed-source continuations；代词可能指跨研究比较。**低至中等指代缺陷**。 | 重复准确对象，指向当前固定源延拓对照；核验来自 Methods L153 的同工况定义，而非由两篇文献建立受控对比。 |
| L292 / “common source and transport structure here” | 前句刚对照 measured source/directional closure 与 isotropic Gaussian；“common”不明确属于哪一比较。**中等比较归属缺陷**。 | 命名为“本研究四角对照内部”；保留材料函数、场响应和恢复操作都改变的实际含义。 |
| L54→L56；L82→L84 | 已有相变律→边界分解→运动；来源均值→开发/校准/uncertainty role 的连续推进。**有效应用正例**。 | 保留。不要把稳定回接改成统一 roadmap，或为了短而删掉来源人群差异。 |
| L176 Results opening；L227 figure-first opening | Results 开头已给比较序列；L227 的图表开头仍可追溯。加强控制问题可以帮助读者，但没有仅因图表开头就成立的科学缺陷。**可选编辑**。 | 只在读者确实失去比较目的时改首句；不以“每节必须开头一段”阻止接收。 |

这些是可定位的读者问题，不是所有存在的问题。没有检查 rendered pages、领域原件或 full numerical evidence，故不能清空其他 reviewer 的科学／布局 findings。新反证仍可使相关结论重开。

## 处置建议

接收 source-ledger 和 reusable-methods 为证据可追溯的写作方法输入；接收当前新增短指南的总体方法和归属，补上三项微观诊断后做实际前向样例。对冻结稿接收其已有高层连续性，但将上述对象身份和比较归属问题交 writer 作有限修复，并由 reviewer 对修订版本核验。所有问题只能由实际修复、理由化分歧或明确范围处置关闭；“已经有指南”、同模型共识和 confidence 均不能单独关闭。

本轮进行了一次 substantive investigation pass，没有反复修订稿件、没有编辑 canonical manuscript、没有新增科学主张。所有写入局限于 `revision-r5/guidance/`。原件失败已保留，不阻碍已读 Duke／UNC／Purdue 方法的有限使用。
