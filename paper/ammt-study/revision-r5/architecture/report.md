# R5 全文架构审计与写作者交接

日期：2026-10-02。输入为本地私有冻结稿 `revision-r5/manuscript-input.tex`、[已核对数值证据](../../evidence/verified-data.json)、[R3 引用支持账本](../../revision-r3/citations/support-ledger.json)、[R4 原始写作来源账本](../../revision-r4/guidance/source-ledger.json) 及其中本地私有阅读文本，以及 R2 期刊范例的原文结构。本报告只写入 `revision-r5/architecture/`，不修改正稿、共享研究状态或 PaperSpine 管理文件，不声称连接了实时产品服务。

## 1. 架构判断及当前交付边界

**保留数值研究的 Introduction → Materials and methods → Results → Discussion → Conclusions。方法与结果由同一名科学写作者负责衔接；引言、讨论、结论及摘要由另一名论证写作者统筹，协调者在整稿中决定标题。** 本稿提供六个已有解的数值重分析、回顾性几何比较和固定源的性质函数对照，没有新求解算法、新物理模型或精度改进证据，故不宜改成“新方法/模型开发”论文架构。

最有用的调整是：让方法目录体现“比较设计—控制模型—观测量—性质对照—数值核查”这条路线；让结果三块依次回答“长度拟合留下何种形状偏差”“性质假设移动了哪个后部边界特征”“相近空间区间对应何种材料时间”；让讨论负责这些结果的含义、来源比较及可区分的解释。本轮不需要新建一般机制章节或新机制图，也不需要把现有每段结尾都改成知识空白句。

这是一次有实质内容的架构审计和可执行交接。下文不把提议标题、章首句或写作指导当成已经应用于正稿。真正候选段落应在协调者传回共同论证和新指南后写入各自获授权的候选文件，再检查整稿。当前交付的验收对象为报告的研究路线、证据对应及可执行调整；不是完成稿质量或投稿准备度。

## 2. 读者、贡献与证据层次

### 2.1 读者的实际问题

目标期刊名称是 Additive Manufacturing。由已读范例主题推断，其相关读者包括 LPBF 热模型研究者、AMMT 基准使用者以及用热场作凝固/材料分析的研究者；这是读者定位判断，不是已核实的官方读者声明。

引言优先回应模型研究者：一个长度拟合后的低成本热场，哪些输出仍受表外性质描述影响？结果应让实验读者辨认长度成像、横截面形状及温度轨迹提供的不同信息。方法主要面向能判断控制方程、观察算子和数值解是否适用的专业读者。凝固研究者需要清楚知道本文时间量来自同一稳态场的坐标变换，并非液体质点驻留时间或独立冷却实验。

### 2.2 在源核对约束下选择的中心论证

> 在同一 IN625 导热—焓模型内保留条件 B 长度拟合得到的源因子，独立改变表外导热系数和显热比热的延续规则，可以把总体长度响应拆解为后部固/液相边界的共同位移与间距变化；再用扫描速度把该间距转换为材料通过时间。该分解说明性质延续改变了长度校准场的热学解释，且并未消除本文的宽/深形状偏差。

这一表述以 [verified-data.json](../../evidence/verified-data.json) 的 `calibration`、`factorial`、`research_case_metrics`、`numerical_evidence` 为当前研究支持，以 R3 账本 `C05/C14/C17/C18` 和 `D03–D06` 为引用及推导边界。协调者已传回最近原文核对：Kollmannsberger 前驱把高温外推本身视为需校准的物理模型，标量源拟合受三维尺寸约束；Myers 的几何拟合与表面温度比较说明温度信息有独立区分作用。上述来源使本文问题成立，同时削弱“首次发现几何不足以验证热场”这类新颖性表述。

本文更具体的研究增量是**共同源因子之后的表外 k/cp 响应及成对后部相界解释**。没有证据声称四个分支重新拟合后都能得到同样几何；本研究也未评估这些替代性质哪个是真实液态材料描述。数学非唯一性、整体物理有效性、流动机制及显微组织改善均不由现有六个解建立。

### 2.3 分清本研究比较和外部比较

| 证据类型 | 实际作用 | 允许的结论 | 在稿中的完整归属 |
|---|---|---|---|
| B 长度标量拟合 | 约束当前源、性质、边界观察组合 | 拟合该条件的长度代理，η≈0.28905 | 方法给目标/算法/数据角色，结果给实现值及剩余形状偏差 |
| B 宽深及 A/C | 已知公开目标后的回顾性比较 | 描述该模型与各条件均值的差异 | 方法给非盲角色，结果给差异，讨论解释其信息 |
| B 的 LL/HL/LH/HH | 固定 η、相律、网格、源和观察算子 | 两个规定延续规则的确定性有限对照 | 方法定义，结果报告方向、相界、作用量 |
| 后部相界与 passage time | 同一稳态温度场的派生描述 | 相界位置、间距和速度变换的区别 | 方法定义，结果分解，讨论解释轨迹含义 |
| 分析基准、残差、有限细化 | 数值实现及已观察的敏感性 | 支持主要数十微米响应的数值解释 | 方法摘要、附录细节；不晋升为绝对误差界 |
| Kollmannsberger / Myers 等 | 已发表设计下的研究背景与解释比较 | 几何约束和温度证据的互补性 | 引言建立问题，讨论比较本研究设计 |

有三个可比层次必须保留：

1. **本文条件均值比较**：长度仅为 Lane 的 20 μs 类（帧数 19/10/7，不是独立试件数），W/D 为 NIST 100 μs 类。三维尺寸不是同一组轨道同时测得。Lane W/D 的 U 来自合并 100+20 μs 的分析，仅作测量不确定度尺度；不能作为当前 NIST 100 μs 类均值的正式置信区间或联合模型误差统计量。
2. **同一物理模型内的性质对照**：六解共享 B=LL。改变延续函数时 η 保持不变，固定相律并不等于测得材料的实际非平衡相律。细微横向效果的分支专属收敛尚未建立。
3. **不同文献模型之间的上下文比较**：前驱采用实测二维束斑及不同相函数，本文采用等效圆高斯；前驱的高温 k 数据端点为 871°C，本文当前表端点为 982°C；其各向同性偏窄偏深，本文偏宽偏浅。因此既不能直接排名精度，也不能赋予二者相同的残差机制。方法给本研究细节，讨论给这些比较限制；引言只保留足够防止错误类比的信息。

## 3. 原始指导的实际使用与期刊范例

### 3.1 本次真正读了哪些指导，改变了什么

本次完整读取了本地 PaperSpine 的 `SKILL.md`、`current-method-routing.md`、`motivation-thread-writing.md` 和 `editorial-completeness.md`；读取了生产协议关于审计按需适用的部分。完整读取 academic-paper-writing 的 `SKILL.md`、`whole-manuscript-architectures.md` 和 `manuscript-spine-and-audit.md`。这是只读架构工作，遵循任务约定未运行更新/启动产品流程。

R4 账本用于定位来源，未把账本摘录视作本次阅读的全部内容。实际重新读了以下私有原始文本的有关正文（不复制或再发布整组全文）：

| 原始来源及位置 | 本次应用 | 条件/不能机械套用之处 |
|---|---|---|
| [MIT/Broad Introduction](https://mitcommlab.mit.edu/broad/commkit/journal-article-introduction/)，`mit-introduction-fetch.txt` 全部实质正文 | 优先从结果和讨论反推引言需要的背景，使具体材料问题从 closest prior work 合乎逻辑地导出 | 四组件不是四段；不能拿一般模板生成未检索的新颖性 |
| [MIT/Broad Methods](https://mitcommlab.mit.edu/broad/commkit/journal-article-methods/)，`mit-methods-fetch.txt` 全部实质正文 | 方法说明设计用途，且与结果有可查对应；将会改变结论的观察/控制细节保留 | 原文明确方法/结果小标题可一对多、多对一；不要求同样目录或同一位作者 |
| [MIT CEE Journal Article](https://mitcommlab.mit.edu/cee/commkit/journal-article/)，`mit-cee-title-fetch.txt` 的 Purpose/Audience/Skills | 从全文主信息生成最终标题，区分专业方法读者与跨领域结果读者 | 同权重、主题句优先等是教学建议；不是章长或标题词数要求 |
| [MIT/Broad Abstract](https://mitcommlab.mit.edu/broad/commkit/journal-article-abstract/)，`mit-abstract-fetch.txt` 的 Writing/Purpose/Formula | 摘要提炼完成后的整篇论证，选择能证明区别的数值锚点 | 不强制六句、固定结果数或必须所有结果带数字 |
| [Manchester Introducing work](https://www.phrasebank.manchester.ac.uk/introducing-work/)，本地 overview/CARS 段 | 把 context/niche/purpose 当功能，允许按证据类型重排 | 原文说顺序和元素非固定；短语库不提供缺口事实 |
| [UNC Transitions](https://writingcenter.unc.edu/tips-and-tools/transitions/) 全部正文 | 先定位 §2.4 与 §3.2 混合任务，再写过渡；连接词不能修复组织 | 不给每段增设 however/therefore，也不把道路图当每章必需 |
| [UNC Paragraphs](https://writingcenter.unc.edu/tips-and-tools/paragraphs/) 全部正文 | 以控制思想和证据构造逆向提纲；一句桥梁有时已足够 | 五步示例不是五句；段长、末句知识缺口不是段落有效性的定义 |
| [Mensh & Kording, PLOS 2017](https://doi.org/10.1371/journal.pcbi.1005619)，本地 Rules 1–3、5–10 及 Discussion | 让结果依研究论证排列，摘要含完整信息，讨论收回引言问题 | “每段到 gap”是该指导的较强模式；本稿用不确定性推进，不把其段式普遍化 |
| [USC Title](https://libguides.usc.edu/writingguide/title)，Definition/Importance/Structure/Working–Final Title | 对每个标题名词关系检验对象、变量、方法范围 | 社科标题词数、句式/大小写建议不用于本稿硬性验收 |

本表引用的是写作方法原件，不是本文科研文献；不应把这些指导加入 IN625 论文参考文献。实际阅读限于上述正文；未把原网页的链接例文、Swales 原书或未取得的 Harvard/Gopen 原件称为已读。

### 3.2 从原文读取的期刊结构，及其适用差异

以下结构来自实际读取各发表论文的本地原文提取，不只是 R2 `journal-learning.md` 的总结。定位见 [R2 来源索引](../../revision-r2/journal/source-index.json) 及下列 extract。此次目标是结构，不声称重新完成每篇科学全文审查或像素/版式审查。

| 原文 | 实际结构 | 对本稿的启发与限定 |
|---|---|---|
| Myers 2023，`literature/myers2023-published.txt` L153–154、466、524、568、651、723 | Introduction；Methods（two-color/camera/validation/setup）；无小节 Results；Discussion（含 Comparison to simulation、Uncertainty and limitations）；Conclusion | 模型温度比较可在讨论形成独立解释任务；本稿结果有三个问题，保留子节更清楚。它没有 Results 章首总览段，不能据此要求所有章节先总览 |
| Hooper 2018，`literature/hooper2018-published.txt` L154、450、606、738、796、815 | Methods 七小节；Results and discussion（扫描区域、gradients/cooling profiles、system limitations/errors）；Conclusions | 合并结果/讨论是可行选项；本稿跨三证据族有解释综合，拆开更有用。实验系统 validation 小节不能照搬为当前导热场的物理验证 |
| Lane absorption 2020，`literature/lane2020-absorption-nist.txt` L35、298、359、508、631、712、769、817 | 引言 1.1–1.6；Methods；Results 按 dynamic / time-integrated / ex-situ；Discussion；Conclusions | 目录可以按不同证据时间尺度/观测层次呈现研究路线；没有必要按仪器或图号排结果。本文不足以采用吸收与形貌相关的机制结论 |
| Zafari 2025，`revision-r2/journal/texts/operando2025-layout.txt` L157、263–279、547、661、828 | Methods；Results（melt pool dimensions→keyhole→melt flow）；Discussion（pattern/mixing/forces）；Conclusions | Results 章首确有科学路线：先几何/不稳定性，再解释主要流动观察。证明条件性章首可有用途，不意味着本稿可添加未研究的 forces 章节 |
| Hou 2024，`revision-r2/journal/texts/dissolution2024-layout.txt` L160、467、986、1234 | Materials and methods；experimental observations；Modeling dispersoid structural evolution；Implications for L-PBF of ODS alloys；Conclusions | 观察→模型→应用的架构由该文实验与新模型贡献决定；本稿没有其物理模型/应用证据，不能照搬第4、5章职责 |

**官方要求与推断分离**：R2 未取得当前 Additive Manufacturing Guide for Authors。Elsevier 通用 LaTeX/AI 政策另有来源，但不能替代该刊对节名、节序、标题/摘要长度、页边距、图尺寸的具体要求。因此本报告关于 IMRaD、独立 Discussion、章首段及小节标题均为依据同刊范例和读者任务作出的编辑建议，非“期刊规定”。

## 4. 当前完整目录

冻结稿共五个正文一级章节、两个无编号声明、一个附录章节；无独立 Literature Review、无独立机制章节。

```text
Title: Thermophysical-property effects on melt-pool geometry and cooling histories in IN625 laser processing
Abstract
Keywords
1 Introduction
2 Materials and methods
  2.1 Benchmark conditions and comparison design
  2.2 Moving-frame enthalpy model and material continuations
  2.3 Melt-pool geometry and material passage
  2.4 Calibration, constitutive contrasts and numerical adequacy
3 Results
  3.1 Melt-pool geometry across scanning conditions
  3.2 High-temperature property effects on the thermal tail
  3.3 Scan-speed dependence of the rear thermal interval
4 Discussion
  4.1 Geometry calibration and model discrepancy
  4.2 Conductivity and storage in the thermal tail
  4.3 Spatial phase span and material cooling time
  4.4 Thermal interpretation and discriminating evidence
5 Conclusions
Data and code availability
Declaration of generative AI use in manuscript preparation
Appendix A Material data and numerical verification
  A.1 Material-property inputs
  A.2 Spatial discretization and observation recovery
  A.3 Scaled enthalpy diffusion and diagnostic definitions
  A.4 Scalar calibration and solution acceptance
  A.5 Separate constant-property verification problem
  A.6 Calibration record and retained sensitivities
References (elsarticle-num; bibliography-r3)
```

## 5. 当前完整逆向提纲

本节覆盖冻结稿所有叙述块及主要显示项。跨方程前后、组成同一科学定义的文本合列为一个论证单元；表格数据行不虚算叙述段落。行号仅指该冻结版本，后续候选以内容定位为准。

### 5.1 题名、摘要与引言

| ID / 行号 | 当前承担的论证任务 | 后续处置 |
|---|---|---|
| T / 27 | 标示性质、几何与冷却史在 IN625 激光加工中的关系 | 最后由整稿重定范围：延续函数、计算模型、派生材料时间 |
| AB / 30 | 从几何拟合提出热史依赖，概述四角对照、残差、尾部位移和速度变换 | 论证顺序可保留；从整稿选择定量锚点，不引入物理验证 |
| KW / 33 | LPBF、IN625、geometry、enthalpy、properties、discrepancy 检索词 | 检查 bare-plate / numerical modeling 范围与主题一致 |
| I1 / 40 | 几何和热史用途不同，热成像提供进一步信息 | 保留对象入口，缩短重复的校准边界陈述 |
| I2 / 42 | 低成本移动源导热的历史和用途，流动/表面过程未描述 | 合并为使 closest model 可理解的简短方法背景 |
| I3 / 44 | 同基准标量/方向导热校准及 dynamic source 显示源/closure 耦合 | closest AMMT 为主要支点；dynamic source 细节移讨论 |
| I4 / 46 | Myers 几何相似而温度不同；前驱内温无效；观察定义不同 | 将几何/温度信息逻辑并入前驱段；精细观察定义归方法 |
| I5 / 48 | 敏感性、符合性、可达性的近期研究分类 | 避免单列全部 taxonomy；仅留下会改变本问题的相关进展 |
| I6 / 50 | k/cp 职责、表端点低于相区、来源性质及液体数据缺口 | 提前成为材料特定问题核心；保留实际端点与实测/计算区别 |
| I7 / 52 | 显热延续与潜热/相律不同、不同凝固端点有后果 | 留下保持同相律的必要理由，替代相律技术细节移讨论 |
| I8 / 54 | 总长度不能区分成对相界共同位移和间距 | 保留解释研究诊断的直接必要性 |
| I9 / 56 | 空间间距除速度得到材料时间；不同真实轨迹有界 | 保留转换意义；pulse/fluid 两例的细节归讨论 |
| I10 / 58 | 三工况、B长拟合、独立延续、相界和时间构成本文设计 | 用精确的三个研究回答关闭引言；不称新算法/精度提升 |

### 5.2 方法

| ID / 行号 | 当前任务/显示项 | 后续归属 |
|---|---|---|
| M0 / 60–62 | 一级方法标题后直接进首小节 | 把 M1 移到此处作已有科学路线的章首 |
| M1 / 63 | 两类比较连接长度、形状、后部区间和时间 | 方法章首；不必在2.1再重复 |
| M2 / 65 | 三条件、B/C固定功率、圆高斯重建束宽 | §2.1 条件与设计 |
| T1 / 69–80 | P、v、吸收线能量、w/v 查表 | 保留条件表；这些是输入尺度 |
| M3 / 82 | 长度和W/D不同文献/观察群来源 | §2.1 数据角色 |
| M4 / 84 | 公开目标已知、仅 B长度入目标、U来源与δ/U | §2.1 比较设计；保持回顾性与尺度语义 |
| M5 / 87–92 | lab能量平衡与保守焓定义 | §2.2 物理模型 |
| M6 / 93–99 | ρ、Ts/Tl、latent、T0来源及线性相分数 | §2.2 共用材料/相律 |
| M7 / 101 | 插值表、来源身份与潜热有效cp | §2.2；数值比例解释归讨论 |
| M8 / 103 | 表终点低于Ts使延续不可避免 | §2.2 引出property图 |
| F1 / 105–110 | k/cp实际输入、L/H、相区、潜热的显示 | 保留方法图，帮助读者看到被改变的函数 |
| M9 / 112 | 两因素延续、温度范围、primitive/inverse一起改变 | §2.2 函数定义；四角比较角色由§2.4给出 |
| M10 / 114–119 | xi=x-vt导出frame平衡；坐标输运非流速 | §2.2；保持推导和模型范围 |
| M11 / 121–127 | 高斯q、能量规范、源/侧/入出边界及损失省略 | §2.2；离散source integration留附录 |
| M12 / 130 | L观察算子及连通/截断条件 | §2.3 几何观察 |
| M13 / 132–137 | Tmax fusion-envelope定义和重建先于最大化 | §2.3；顺序会改变数值几何，必须保留 |
| M14 / 139 | Lane辐亮度边界与模型solidus阈值不同 | §2.3；不把η当测得吸收率 |
| M15 / 141–148 | 成对后相界、ell、tau、平均cooling及链式法则 | §2.3 相界与材料通过；来源区间与本文区间不同 |
| M16 / 151 | 拟合实际η及残差、A/C固定 | §2.4 目标/共用规则；实现值也在结果3.1报告 |
| M17 / 153 | 四角共用控制，B=LL造成六解并集 | §2.4；模型设计示意不等于物理机制 |
| M18 / 155–163 | baseline有限效应/interaction/joint及两个条件效应 | §2.4 定义确定性对照；无统计试验语言 |
| M19 / 165 | selected Pe faces及rear hot-region budget | §2.4 辅助诊断；指出人口/边界各场不同 |
| M20 / 167 | 近源网格和三种解核查尺度 | 新§2.5 数值解及核查摘要 |
| M21 / 169 | 另一个constant-property benchmark及实际误差 | 新§2.5设计摘要；具体值移/引用已有附录A.5 |
| M22 / 171 | 校准后axial/domain敏感性、旧transient、blackbody估计 | 新§2.5简述有效尺度；不同作用的历史/损失信息不要拥挤在一段 |
| M23 / 173 | 六解残差/相分数/几何通过阈值 | 新§2.5简短实测摘要，保留附录结果位置 |

### 5.3 结果

| ID / 行号 | 当前任务/显示项 | 后续归属 |
|---|---|---|
| R0 / 176 | 几何比较→性质分解→速度/时间的研究路线 | 保留已有 Results 章首，少作程序性叙述 |
| R1 / 179 | B长拟合及B宽深残差 | §3.1主证据入口 |
| T2 / 181–201 | A/B/C L/W/D、reference、U、δ/U精确查表 | 保留查值功能；U不能成正式validation interval |
| F2 / 203–208 | 当前/文献模型与reference几何关系 | 保留上下文比较，本文结论以自身与reference为准 |
| R2 / 210 | A及C偏差、aspect ratio及mean ratios来源 | §3.1；不得称A物理validated |
| R3 / 212 | B/C固定P的W/D变化，shape response | §3.1；trends图a/b应在此明确panel引用 |
| R4 / 214 | nominal experimental L趋势弱于U尺度，axial变化小于残差 | §3.1；描述量，不做显著性检验 |
| F3 / 216–221 | Surface Ts contours和passage fusion envelopes | 保留源内两种几何观察的形状证据 |
| R5 / 223 | 两种观察响应不同，转向固定条件property comparison | 保留桥；补明该对照测敏感性而非拟合shape remedy |
| R6 / 227–231 | 四角长度、joint algebra及direction persistence | §3.2用“固定B/source”问题句先于figure句 |
| T3 / 233–251 | 四角L/W/D和effects精确数值 | 保留lookup及depth cancellation，轻度图表重复可接受 |
| R7 / 254 | rear Ts/Tl/front位移，98.3%，span小变 | §3.2核心科学证据 |
| R8 / 256 | 同温性质扰动、latent accounting、Pe、region flux、recovery | 分出观测值与解释；必要diagnostic结果留3.2，accounting含义归4.2 |
| R9 / 258 | 深度相消、direction persistence、shape residual、precision | §3.2；精细对照称current-mesh而非实证改善 |
| F4 / 260–265 | Centerline profiles、phase pair/span、finite geometry effects | 核心性质对照图；不用新泛机制图替代 |
| R10 / 267 | 大length范围与小span范围总结 | 与R7整合，避免图后重新再说同结论 |
| R11 / 270 | A/B/C spans、times、cooling及B/C百分比 | §3.3；B/C主比较，A作为背景 |
| R12 / 272 | cooling增加由同一ell/v关系代数导出 | 保留一句避免把三个派生量当独立证据，合入R11 |
| F5 / 274–279 | a/b shape对比 + c/d model span/time | §3.1用a/b，§3.3用c/d；避免整幅图被误当单一结果问题 |
| R13 / 281 | fixed-power shape contraction与interval passage是不同响应 | 保留收束，避免无端将passage算作额外experiment constraint |

### 5.4 讨论、结论和声明

| ID / 行号 | 当前任务 | 后续归属 |
|---|---|---|
| D0 / 284–287 | Discussion一级标题后直接首小节 | 增/移入综合主回答；非重复目录预告 |
| D1 / 288 | fit是source/material/observation组合，形状残差含义 | 章首或4.1起点，但不把宽浅残差因果归于一个过程 |
| D2 / 290 | Myers geometry/temperature区分，refit与本文固定η区别 | 4.1；说明不同设计能共同支持何层次结论 |
| D3 / 292 | closest directional calibration与本文isotropic contrast区别 | 4.1；加偏差方向/beam/phase不同，别借前驱机制 |
| D4 / 295 | 再报length/98.3%/span与shape residual | 压缩成“尾部移动与shape correction不同”的解释入口 |
| D5 / 297 | latent-inclusive有效储热解释unequal perturbation、prephaseH | 4.2新解释；减少Results已报数值 |
| D6 / 299 | Pe/flux与moving selection/operator共同影响，matched-region可区分 | 4.2；具体未知限定为尚未分离的贡献 |
| D7 / 302 | 再报B/Cspan/time/cooling、共同移位与时间区别 | 压缩为相界位置/间距/时间三个信息层次 |
| D8 / 304 | Hooper/Lane观察角色及温区/position/exposure对齐 | 4.3物理测量对应，避免把别材料温史当validation |
| D9 / 306 | flow-advected路径和transient hatch条件不同 | 4.3必要轨迹范围；有用但不延伸成未研究microstructure章节 |
| D10 / 309 | dynamic volumetric source为竞争解释及需要matched protocol | 4.4；强调尚未直接比较，而非已经确认原因 |
| D11 / 311 | 材料数据不足、极端模型温度及省略过程 | 4.4；peaks第一次出现属新结果，需交方法/结果owner处理 |
| D12 / 313 | numerical vs physical evidence，fine-scale需求，measurement roles | 4.4；数字/细节回指方法与附录，保留解释性边界 |
| D13 / 315 | 三类观察怎样检验各部分，下一 assessment | 4.4结尾；不是完成了这些检验 |
| C1 / 318 | fit后shape残差→形状提供额外信息 | 结论保留具体研究发现，删泛模型用途重复 |
| C2 / 320 | opposing continuations、rear translation、shape residual | 结论核心，与引言问题对应 |
| C3 / 322 | B/C time/cooling派生关系及互补观察的完整意义 | 修正“adds a further constraint”：派生time是descriptor，测得轨迹才是independent constraint |
| DA / 325 | 数据与代码包、原case/source范围 | 保留事实性声明；外部link有效性本次未验 |
| AI / 328 | Codex协助与deterministic figures | 保留真实声明；官方适用格式由交付/政策核查处理 |

### 5.5 附录

| ID / 行号 | 当前任务/显示项 | 后续归属 |
|---|---|---|
| AP1 / 336–360 | 全部k/cp原表及独立温度列 | A.1查值和完整输入 |
| AP2 / 364 | continuation slopes与analytic H/inverse | A.1；正文函数描述引用 |
| AP3 / 367 | graded mesh/domain/initial guess | A.2数值重现 |
| AP4 / 369 | rectangle Gaussian top powers/half power | A.2 source离散 |
| AP5 / 371–375 | K surface recovery及even symmetry reconstruction | A.2观察算子，不能省掉branch对应primitive |
| AP6 / 377 | observation pitch非heat-field spacing | A.2定义，防假超分辨解读 |
| AP7 / 380–385 | scaled U、face D、derivative limit和solver/stencil updating | A.3解法；正文新2.5指向 |
| AP8 / 387–392 | face Pe定义与temperature-selected population | A.3诊断 |
| AP9 / 394 | hot-region boundary flux与moving selection | A.3诊断，讨论不可误作fixed-region causality |
| AP10 / 397 | safeguarded secant、bracket、acceptance和实现η | A.4数值校准重现 |
| AP11 / 399 | absolute residual/global balance/correction thresholds | A.4数值核查 |
| AP12 / 401 | 六生产解实际残差范围和state checks | A.4数值结果支持 |
| AP13 / 404 | constant property benchmark setup和finite-domain | A.5不同问题的verification设计 |
| AP14 / 406–412 | heat-kernel integral、quadrature/extraction与error scope | A.5 verification；不可替换一般production observer |
| AP15 / 415 | 五试点/local slope/Δη尺度、非global identifiability | A.6数值校准记录 |
| AP16 / 418–426 | B/C axial fine-minus-baseline | A.6已观察的refinement sensitivity |
| AP17 / 429 | δ/U定义、不同operator无joint likelihood、full precision | A.6；正文方法应已有主要规则，不留作首次解释 |
| REF / 431–432 | numeric bibliography | 书目来源/citation位置核查由source owner完成 |

## 6. 具体语义断点与最小修复

| 优先级 / 位置 | 实际断点 | 科学/读者后果 | 最小修复及验收 |
|---|---|---|---|
| 高 / I3→I5→I6 | closest calibration问题之后绕入sensitivity/agreement/attainability taxonomy，材料特定缺口到第6段才出现 | 读者容易以为论文贡献是通用评估框架，而非k/cp延续对照 | 把材料缺口紧接closest success/limit；近期来源合入其能支持的具体关系。读者在引言中部可说出“为什么改k/cp” |
| 高 / I8、R5、§3.2 | shape residual接property contrast，但后者没有重拟合source或修正shape | 易把敏感性设计误读成纠正宽浅形状的改善尝试 | 在设计过渡明确：共同源下区分不同后相界响应；最终结果说shape残差保留。无需添加防御性免责声明 |
| 高 / §2.4 | calibration、four-corner definition、diagnostic、verification与结果值放同一小节 | 方法目录隐藏研究路线，数值支撑和物理对照边界混合 | 原§2.4留calibration/contrast；抽出新§2.5 Numerical solution and verification。正文保留判断结果所必需的少量核查证据，详值引用既有附录 |
| 高 / R8→D5/D6 | §3.2同温性质值和flux解释拥在一段，讨论几乎重报 | 主相界结果被长解释冲淡；selected Pe/flux被误当因果识别 | Results报告诊断值/选择定义，Discussion发展潜热accounting与变化人口意义；不新增未经检验“k下降必导致散热下降”机制 |
| 高 / D11 | 2697/3507/2756/3721°C peaks首次进入Discussion | 讨论引入新结果，读者不能回查其观察/数值定义 | 方法/结果owner决定：若会实质改变高温continuation可信度，方法定义positive-y sample并在3.2报告一次；否则不报四峰数字，在讨论以已显示场范围和模型省略项限定用途。不能凭可删细节而消失这项物理问题 |
| 高 / C3“adds a further constraint” | 当前passage time是ell与v的派生量，被说成进一步约束 | 暗示独立验证信息 | 改为adds a temporal descriptor；只把独立测量temperature trajectory称约束 |
| 中 / M0/D0 | 方法的设计总览放2.1内，讨论无首段总回答 | 一级标题下层级的科学职责不清 | 把M1升作§2章首；§4章首先从两个对照得出的共同回答开始，随后第一小节不复述 |
| 中 / F5 a/b与c/d | shape panels早在3.1解释，整图只放3.3，3.3写“fixed-power comparison”又含shape | 阅读/图文对应跨问句重复 | 最小方案保留图文件，3.1明确cite(a,b)、3.3明确cite(c,d)，章首解释figure复用；如排版仍阻碍阅读才拆existing panels，非先新画图 |
| 中 / §3.2/§4.2、§3.3/§4.3 | 相同34.28、98.3%、80.26/80.79、100.33/67.33重新一套报告 | Discussion增加长度却未提供相称新推理 | 讨论留下形成解释的最少锚点，重点是transport/storage量的不同作用与轨迹含义 |
| 中 / I3、D3、F2 | 用closest source而未突出不同residual direction | 可能借前驱“effective anisotropy”解释当前宽浅误差 | 引言只说scalar geometry limits；讨论具体列明反向shape残差和不同输入，F2不作为matched method ranking |
| 中 / Abstract/title | “thermophysical-property effects…cooling histories…laser processing”比实际设计宽 | 读者期待真实property识别、一般热史或实验外推 | 标题从整稿指定continuations/model scope；摘要保持computed passage语义 |
| 低 / repeated cautions | U/mesh/temperature范围在多处全量重复 | 推动论证受阻 | 方法完整定义，结果在影响细微结论时局部限定，讨论发展整体物理范围；不按“越少caveat越好”删必要事实 |

## 7. 建议的最小可行目录与章节首段

### 7.1 建议目录

无需更动五个一级标题；给方法增加一个小节，细调三个结果小节和第四讨论小节的职责显示。标题可继续英文名词式，不强制全部声明式。

```text
1 Introduction
2 Materials and methods
  2.1 Benchmark observations and comparison design
  2.2 Moving-frame enthalpy model and property continuations
  2.3 Geometry, rear phase boundaries and material passage
  2.4 Length calibration and fixed-source property contrasts
  2.5 Numerical solution and verification
3 Results
  3.1 Geometry discrepancy after length calibration
  3.2 Property effects on rear-boundary position and separation
  3.3 Scan speed and derived material passage time
4 Discussion
  4.1 What geometric calibration constrains
  4.2 Transport, storage and translation of the thermal tail
  4.3 Spatial phase spans and thermal trajectories
  4.4 Model interpretation and discriminating observations
5 Conclusions
```

`fixed-source` 在2.4仅指 η 和束形保持，不能暗示所有函数场相同；实际changed k/cp仍由2.2及four-corner定义说明。若该词使读者误会，也可用 `Property contrasts with the calibrated source factor retained`。一级Methods现名足够，本稿不需“new modeling framework”。

### 7.2 条件性章首的选择规则

章首段只在一级章节后有多个小节、而读者需要知道其设计/证据依赖关系时使用。Methods确有两个互补comparison；Results确有三步证据路线；Discussion确有需要综合的不同量。Introduction没有子节，首段直接研究对象；Conclusions没有子节，首句直接结论；附录的表后与小节间解释已足够，不额外添一段“本附录分六部分”。

对本稿的具体要求：

- **Methods章首**：移用现M1，说明A/B/C几何comparison与B four-cornercontrast共享B=LL，并引出相界/材料time。它不需枚举后文小节号，不需泛述“为了清楚理解”。
- **Results章首**：现R0已能做这件事。保留其从未拟合geometry到pair shifts再到time的路线；必要时将“remaining measurements”改成“post-calibration condition comparisons”以保留retrospective角色。
- **Discussion章首**：把现D1的中心含义与R7/R11的关系综合，回答引言所问；只需说明相同校准场内shape、tail position及material time的信息不同。不给一次全部数值或每节summary。

章首不应代替每小节科学开头。§3.2现首句“四角结果见表/图”只定位文件，应改为明确其测试目的：共同B源因子下，独立k/cp变化会怎样改变后相界。§3.3从B/C同功率的近似spans直接进入速度到time关系，避免以A/B/C数字清单开头。

## 8. 引言的证据类型优先级及与结尾的闭合

### 8.1 此类数值重分析引言先写什么

引言排序应服从数值证据，而非“工程背景—综述—宏大机制—泛创新”的通用模板：

1. **对象与用途**：bare-plate IN625 的低成本导热场被用于几何及凝固相关热描述；几何和thermal history的问题不同。使用LPBF背景，但不把bare plate等同powder-bed evidence。
2. **closest calibration已经成功什么、仍限制什么**：前驱实测beam/η使length更好，directional closure进一步改善shape，仍不保证池内温度。Myers作为不同设计下温度信息的实例。区别源/观察足以防误类比即可，不在此详列工艺参数。
3. **该已知问题中实际材料缺口**：当前supplier k/cp表止于982/1093°C，低于本文采用相区。高温函数需要延续，较近前驱已明确外推是模型而不是数据。这里是本文最具体的必要性。
4. **为什么需要保持相律及共同源**：显热延续与latent law不同；固定它们中的共用因素才能把规定k/cp变化解释为响应。材料非平衡相律另有未知，留讨论，不为未做ablation增设一段gap。
5. **为什么检查成对相界而非只看总L**：总L不能区别rear interval平移与厚度变化，paired Ts/Tl是当前解支持的诊断。
6. **为什么还要转换到材料time**：近似相同spans可因v不同而产生不同passage interval；这是derived field descriptor，对真实thermal trajectory的物理对应待独立观测。
7. **本文设计及回答承诺**：B lengthfit→保留η作retrospective geometry comparison；固定B做four corners→rear pair/shapecontrast；B/C速度→材料通过时间。结尾可预告main finding方向，但不把全Results数字复制进引言。

这些是七个逻辑工作，可形成约7–8个充实段落，也可合并为更少段落；没有硬段数。当前I2/I3/I4可合并重组，I5的全taxonomy不再独占一段，I6提前。最新来源若只作为话题覆盖而无支撑当前问题的作用，应退出引言主线，必要内容留discussion，不为保引文而写段落。

### 8.2 引言—结果—讨论—结论—摘要的对应

| 引言提出的读者问题 | 方法如何使问题可问 | 结果回答 | 讨论增加什么 | 结论/摘要留下什么 |
|---|---|---|---|---|
| B长拟合后场还留下什么geometry信息？ | B_L拟合，B_WD/A/C角色、各自operator及U尺度 | §3.1宽浅残差和固定P shape response | calibrated parameter的组合意义；不同source/closure/observer及前驱反向residual | 一处fit不约束全部shape；本文specific discrepancy |
| 表外k/cp改变总L的哪一部分？ | fixed η、phase law、four corners、Ts/Tl/front | §3.2 opposing length responses，rear translation为主 | unequal local perturbation sizes；flux/Pe与selection/recovery未分离 | property continuation改变tail位置，非shape improvement |
| spatial span与material time何关系？ | quasi-steady chain rule、同interval、v | §3.3 B/C相近span，time约少1/3 | stationary track与fluid/transient trajectory不同；observational alignment | transformedtime有额外语义，无额外独立证据 |

**Introduction 与 Discussion 可以同一人写，但目的相反**：前者只建立结果为何值得问，后者从具体回答走回已有知识及能区分的解释。Conclusions取最少耐久结论；不新增来源或“下一步所有可能”。Abstract从完成稿提炼，不应从引言单独写出。题名需覆盖三块证据的共同信息，不能只从I6或某张图生造。

## 9. 图与证据计划：保留已有工作，改善科学归属

图计划依据冻结稿caption及verified-data，不是新绘图/像素验收。现有五图已覆盖全部主要结果；本研究没有需要强制添加的一般流动机制图。

| 图/表 | 读者问题与证据工作 | 正文使用的必要调整 |
|---|---|---|
| property continuations F1 + property input appendix | 两因素实际改了哪些函数、在哪里进入相区？ | 方法先说明为何表外需描述；区分sensible cp与latent increment |
| geometry comparison F2 + exact T2 | lengthfit后shape和A/C差异是什么？ | 本文observations比较先讲；published model点仅上下文。T2精确值、F2模式各有用途 |
| operating contours/envelopes F3 | Ls与fusion-envelope不是同一种几何观察 | 3.1解释两个观察层，而非重复每条曲线 |
| constitutive factorial F4 + T3 | length变化是rear translation还是phase-span变化？ | 3.2主图；profiles/pair/span证据大于只展示effects柱状图；T3提供finite-effect查值 |
| condition trends F5 | shape response及spatial-time分别怎样随B/C改变？ | 明确a/b在3.1，c/d在3.3；coolingrate是同一span和v的再表达，不需另立第三validation图 |
| numerical appendix T6/integral | 实现核查和主效应尺度的支持是什么？ | main仅给其结论所需尺度，原始重复参数和history放附录 |

若需要面向读者的研究设计示意，最多是“六解集合及共享B=LL”的计算设计图，标记校准/回顾性比较/有限性质对照；它不会增加物理证据。没有必要把计算流程命名为机制。已有F4的成对相界空间显示更接近本文真实解释任务。

## 10. 写作责任、依赖与验收

### 10.1 方法和结果应不应该同一个人负责？

本研究**应由同一名科学写作者最终负责 Methods+Results**。这不是文献规定，也不是要求同一个人做每一个字；它是本项目的有效责任划分。原因是观察算子改变结果含义，L/H改变primitive和surfaceinverse，temperature-selected population改变diagnostic解释，数值adequacy直接限制fine effects措辞。分开两个无共同科学责任的writer容易得到“方法讲一个算子、结果讲另一种观测”或“tiny interaction当精确机制”等错误。

可允许不同contributors在同一Methods+Results责任下产生分块候选，但一位owner核对：每个结果变量的数学/观察定义、输入角色、对照规则、解来源、报告精度和对应图。不要要求 Methods/Results 小标题逐字对应；这里2.2模型支持3.1–3.3，2.3operator支持三块，2.4支持3.2，2.5支持全部，天然一对多。

建议另一论证writer负责Introduction+Discussion+Conclusion+Abstract。这四项应共享上述闭合表。最终整稿readerflow、title和source对比由协调者持有；source审计者对科研 citation 支持负责，不由architecture报告替代。

### 10.2 对两个writer的输入/输出约束

| 责任 | 等待的实质依赖 | 要产出的实际内容 | 接受标准 |
|---|---|---|---|
| Methods+Results owner | 协调者共同论证、新section guides、source audit在comparison/diagnostics上的结论 | §2/§3及必要附录候选，按最小TOC重排；解决peaks归属 | 各主要结果能定位到定义和source；six unique runs；B仅Lfit；A/Cretrospective；finite contrasts无统计显著性；主要L响应vsfine effects准确分级 |
| Argument owner | 同一共同论证、新guides、Methods+Results候选内容、closestsource修订 | 引言、讨论、结论、摘要候选及标题逻辑 | 引言承诺被3块结果回答；discussion发展新推理；没有新experiment/numbers；closing不把derivedtime称independentconstraint；源间不同regime保留 |
| Coordinator | 两组候选、source评价及actualfigures/render | 整合正稿、选择finaltitle、最终过渡、检查整稿 | TOC可复述研究路线；title/abstract/intro/results/discussion同一paperidentity；先比内容后改措辞 |

不允许writer把本报告中的source片段自动复制进稿；仍需读被分配的具体原文和共同sourceaudit。本报告是架构理解，并非有资格替sourceowner授予全部citation支持。

### 10.3 保留的标题方向，最终从整稿选

当前题名的变量与对象有基础，但 `thermophysical-property effects` 容易掩盖“表外延续规则”，`cooling histories` 易超出当前rear interval，`laser processing` 范围较宽。两个不同的可用方向如下，均为提议：

- 以整稿解释任务为主：**Interpreting melt-pool geometry and material passage time in an IN625 conduction model**。包含geometry和material time的共同信息，强调计算解释；abstract/keywords承担high-temperaturecontinuations检索词。
- 以主要固定性质对照为主：**High-temperature property continuations and rear thermal intervals in an IN625 conduction model**。更准确显示被比较的变量和模型；整稿需仍把geometry残差解释为校准后的context。

如果共同论证最终保留“保留B长度校准源因子”作为读者最关键的条件，可采用副标题或摘要首部说明。不要为了把所有变量都塞进题名，写成更长的计算任务清单。不能采用“improved/validated/novel thermal model”标题。本文尚不确定能否充分承载 `cooling histories` 的宽含义，优先使用 `material passage time` 或 `rear thermal intervals`。

## 11. 缺失证据应是有边界的科学问题

以下缺失不阻止完成当前数值研究稿；只阻止相应更强的物理/因果说法。

| 有边界的问题 | 对本文的影响 | 较便宜的替代/下一检验 |
|---|---|---|
| 与当前组成/状态匹配的液态k/cp是否支持L或H？ | 不能把四角情景排序为真实material accuracy，不能给liquid-property识别结论 | 先比较现有IN625 composition-based estimates及其范围；可新增有据函数scenario作后续研究，但仍不等于measurement |
| rear displacement中field与surface-recovery改变分别贡献多少？ | 可以报告成对位移，不能确认唯一transport mechanism | 对保存fields做matched observer/region decomposition作为独立授权分析；无需先求新PDE或加fluid模型 |
| submicrometre span/width interactions在每分支是否稳定？ | 可以描述nominalcurrent-mesh，不能精确排序或据此大机制 | 先补关键两分支局部/多方向敏感性；若收益小，保留大位移结论并降级tiny interactions |
| 相同温区/轨迹定义下独立thermal measurement是否匹配？ | τ/cooling是derived diagnostics，非validated histories | 先对齐Lane已有below-solidusoperator/温区以比较定义，或复用已有可用trajectory；需要1350–1290°C证据时明确哪项独立observations仍缺 |
| 源分布、effective transport或observation mapping谁解释当前宽浅误差？ | shape残差成立，唯一物理原因不成立 | 先replay已有imaging/operator；之后在matchingprotocol下选最小sourcealternative。不能从前驱反向residual借cause |

这些是后续科学工作的问题，不是本次writer必须先解决的要求。报告没有授权新PDE求解；上述便宜替代也不声称已经执行。

## 12. 本轮停止点

已完成一个实质架构审计：读取冻结稿全部正文/附录，读取证据角色、数值输出和claim边界，读取R3支持账本，重读相关写作原始指导及原文范例结构，并形成当前全目录、逆向提纲、最小修复、图证据归属和writer验收。本轮未改canonicaldraft、未新增科学结果、未做source全文审计的替代、未做PDF/figure像素验收。

下一次工作仅在收到协调者的新共同论证/指南后，执行被分配的实际候选段落。可选措辞调整到此停止；没有继续反复润色这份规划报告的价值。
