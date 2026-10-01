# Additive Manufacturing：R2 期刊学习与篇章应用

日期：2026-10-01。用途：为 AMMT 三工况、六个生产稳态解的闭合诊断论文提供真实期刊样本、论证职责和阅读版式依据。本文是期刊学习交付，不是对 canonical 稿件的独立审稿，也不宣告其科学结论通过。

## 已完成范围与版本身份

主目录按协调者要求保留六个 distinct 目标期刊样本：Myers 2023、Hooper 2018、Lane 2020 absorption、Zafari 2025、Hou 2024、Bayat 2019。前五个本地 PDF 为最终出版版（VoR），已阅读完整引言与所需 Results/Discussion；Bayat 本地文件实际水印是 **UNCORRECTED PROOF**，首部和引言部分已读，相关 Results/Discussion 未由本代理完成。不能把它写成第六个已充分研读的 final VoR。

此前还实际读完 Tian 2024 的摘要、完整引言、相关 Results/Discussion 与结论；其 PDF 为出版商 **CORRECTED PROOF**。因此可提供六篇已实质学习的研究论文（五 final VoR + Tian corrected proof），同时维持协调者指定 Bayat 六篇目录。Tian 是补充学习样本，Bayat 的局部阅读缺口保持显式。两种集合不得混称六篇最终出版版。

原三篇位于旧 literature 目录，只读引用，没有改动。新增文件、文本和获取记录仅位于本 journal 目录。六个指定目标样本均不与研究线代理固定的六篇同方向样本重复；Lane absorption 与其 Lane geometry 是不同论文。Coleman 2024 由研究线代理负责解释，不在本目标学习数中。

已执行：身份/DOI 核对、正文阅读、前五篇视觉页面检查（新增 Zafari p1/p9/p13/p16，Hou p1/p9/p10/p23；原三篇检查记录见 index）。Tian 视觉 PNG 已生成，当前交付前未实际打开，因此仅用其正文结构和图注职责，不声称视觉版式检查完成。Bayat 首部是通过 pdftotext 判版，未做视觉页审。

## 对当前稿件最有用的篇章结论

1. **中心矛盾应驱动正文**：便宜热模型可在一个几何量上得到合理匹配，但读者需要知道该匹配能支持哪些凝固相关解释。Myers 已明确展示不同参数配对可保持横截面匹配而有不同温度场；本稿不能把这个已知问题包装成首次发现。本稿具体贡献是固定吸收率下，受控热物性高温延拓比较将响应分解到后部固相线/液相线，并量化通过时间后果。
2. **建议 Results 顺序成立**：几何匹配及宽/深残差 → 四角设计的后部边界分解 → 固相线到液相线的材料通过时间。每节首句应提出该节回答的问题，末句给出可被下一节使用的结论。把数值收敛作为该结论量级的支撑，避免流程工具检查成为论文主线。
3. **方法先讲研究设计与观测职责**：先列 B 长度用于拟合、B 宽深用于诊断、A/C 为固定参数回顾比较，再介绍方程/求解器。几何量来自不同观测算子和群体，不能用一个共同误差似然吞并。Methods 热物性图应标出 k、cp 的原数据端点、Ts/Tl、L/H 延拓以及潜热后的有效储热差异，让读者在看分解之前理解干预。
4. **Discussion 要比较具体条件和模型**：Hou 的流体质点 thermal excursion 受到流动与表面变形影响；本稿无液体流动的 x/v passage-time mapping 只有给定移动稳态场下的含义。Zafari 直接看到 flow，但 Al-Sn、粉末、未达稳态，不能用其机制数值解释 IN625 裸板 residual。比较完成后再给出本稿可以支持的用途与下一项最小验证。
5. **摘要保留少量真正决定结论的数值**：固定参数/受控设计、主要 k 与 cp 响应、后部占比、通过时间尺度可各承担一项职责。样本允许较长定量摘要，不支持为了虚构字数上限删除正文论证。当前 AM 摘要字数硬要求未核验。

## 逐篇学习与可定位证据

### Myers et al. (2023), 10.1016/j.addma.2023.103663

*High-resolution melt pool thermal imaging for metals additive manufacturing using the two-color method with a color camera*，Additive Manufacturing。NIST 本地最终出版版，11 页，43 条编号参考文献。摘要约 302 英文词（旧样本 regex 观察，非投稿计数）。

实际读：摘要与完整 Introduction pp1–2，Results/Discussion pp7–9；视觉 p1、p8。定位：§4.1 p7；Fig.7 p8；Fig.8 p9。

引言从高速/高分辨率温度测量需求进入单色测温与发射率限制，再定位两色测量和相机方案。Results 用六种条件的横截面与中心线温度比较说明：多个 Fresnel/accommodation 参数配对在横截面误差 <20% 时仍产生不同温度场。这是本稿最直接的已知竞争事实。

Fig.7 配对粉末/无粉末与不同曝光，保持轴和颜色可比；Fig.8 将几何和温度歧义置于同一问题下。应用：本稿几何图与后部/热历程图应共享分支符号和单位，让读者追踪同一次干预。不可把该论文的参数配对等价为本稿四角重新拟合；本稿四角没有重新校准。

### Hooper (2018), 10.1016/j.addma.2018.05.032

*Melt pool temperature and cooling rates in laser powder bed fusion*，Additive Manufacturing。Imperial 本地最终出版版，12 页，17 条编号参考文献；摘要约 201 词。

实际读：摘要、完整 Introduction pp1–2，热历程及误差 pp10–12；视觉 p1、p11。定位：Fig.13 p10（空间温度剖面），Fig.14 p11（随时间温度/冷却）。

研究通过 Ti6Al4V、100 kHz、20 μm 温度测量，给出 5–20 K/μm 梯度和 1–40 K/μs 冷却等具体尺度。引言不是长篇工艺教程，而是把无法捕获高温快速场变化的测量矛盾与当前系统能力相连。空间 T(x) 与固定位置 T(t) 的图承担不同任务，不可互换。

应用：本稿 passage-time 图须明确坐标变换和材料运动假设；不将脉冲/瞬态实测历史当作当前准稳态 x/v 的独立验证。该论文参考量少源于聚焦的测量任务，不能据此推断本稿应删到 17 条。

### Lane et al. (2020), 10.1016/j.addma.2020.101504

*Transient Laser Energy Absorption, Co-axial Melt Pool Monitoring, and Relationship to Melt Pool Morphology*，Additive Manufacturing。NIST 最终出版版，13 页，52 条编号参考文献；摘要约 237 词。

实际读：摘要、完整 Introduction §§1.1–1.6 pp1–4，Results/Discussion pp9–11；视觉 p11、p13。定位：Fig.1 p3；Figs.10–11 p11。

引言按吸收、监测与形貌的物理联系组织，各背景子节对后文可测量量有明确职责。结果同时保留时间平均关系较强、动态相关较弱的发现。Discussion 比较 0.9 平均耦合与 0.7 量热吸收时，不把差异自动归因于 plume；需要同步测量区分未反射功率与进入基体的热量。

应用：本稿拟合吸收率应写作模型参数，不等同直接测得吸收。保留宽/深残差和不支持的归因，而不是把所有偏差归于遗漏流动。Fig.10/11 将相同工况横截面与宽/深证据并置，可借鉴为几何诊断多面板布局。

### Zafari et al. (2025), 10.1016/j.addma.2025.104754

*Operando synchrotron X-ray analysis of melt pool dynamics in an Al-Sn immiscible alloy*，Additive Manufacturing 103,104754。OSTI3001943 下载文件经 p1 DOI/出版标识及视觉判定为 final VoR，CC-BY，16 页，参考编号 [1]–[69]（p16 视觉确认、Crossref 69）。

实际读：摘要、完整 Introduction pp1–3、相关 Methods p3；Results/Discussion 的流场解释与力估算 pp11–14，结论 p14；视觉 p1、p9、p13、p16。核心定位：Fig.9 p9、Fig.12 p11、§4.3 pp12–14、Fig.13 p13。

引言进程：直接观测 melt flow 的必要性与挑战 → Al-Sn 的天然 X 射线对比 → immiscible alloy 混合/分离问题 → 现有单相材料/稀疏 tracer 的限制 → 用完整速度场与统计形貌来检验机制。实验 Al-50vol%Sn，400 W/300 mm/s 相对深且稳定，而 ≥500 mm/s 更浅/不稳定；不是本稿 IN625 工况。

Discussion 先从实测流向、waviness 和 jets 提出竞争解释，再估算 Marangoni、recoil、buoyancy 和 Weber 尺度。液体速度约 1 m/s 量级、重力沉降约 0.06–0.09 m/s；原文文字有“two orders”描述，但两者数值并不普遍相差两数量级，因此不应复制这一精度夸张。其球冠几何、混合规则热物性、均匀成分、简化梯度均被标注为数量级假设；观察期尚未达稳态（p14）。

Fig.9 用实测速度/图像承担证据，Fig.12 总结观察，Fig.13 仅为尺度模型几何定义，未把示意图当实测。应用：本稿新 property 图定义干预与阈值，后部图展示原始输出，Discussion 的示意/定性机制若使用须与已求解量区分。不可从 Zafari 推定本稿残差由某一种 flow force 导致。

### Hou et al. (2024), 10.1016/j.addma.2024.104554

*Dissolution zone model of the oxide structure in additively manufactured dispersion-strengthened alloys*，Additive Manufacturing 96,104554。OSTI2538374 文件 final VoR、CC-BY，23 页；参考 [1]–[72]，p23 视觉确认、Crossref 72。p1 记录 available online 16 November 2024；Crossref 的 published-print 月份与该页不一致，引用年份2024可靠，不用月份排序贡献。

实际读：摘要、完整 Introduction pp1–3，模型 §§4.1–4.3 pp7–10、§4.7 p13，case-study p15，完整结论 p18，相关 Appendix p19；视觉 p1、p9、p10、p23。定位：Fig.11/12 p8；Fig.13 p9；Fig.14 p10；§4.7 p13；§5.2 p15；Appendix C p21。

科学矛盾明确：短暂熔化应保留 dispersoids 的想法与实际 coarsening/slag 不一致。完整引言不是一句 generic gap，而是逐个比较机械 impingement、化学传输、初始大小、单一表面 T(t)、只算冷却、不考虑流动和多次熔化等条件。最后把需要满足的三项物理要求接到本研究设计。

Scaling analysis 限定 nanoscale 与 micron-scale 的机制；CFD 提供 fluid-element thermal excursions；reduced model 用 Eagar–Tsai 导热解，经温度和时间缩放匹配 CFD，而非声称导热本身复制流动。p9 在 Ni-20Cr、140 W、1.2 m/s、20 μm beam radius 条件下，CFD 池长/宽/深 244/54/40 μm，与 Eagar–Tsai 175/82/35 μm 比较。表面 tracer 快速离开高温区、深处受 convective redistribution 与 depression 影响。p13 讨论 peak 偏差为何对已完全溶解的氧化物不改变当前预测，并承认 keyholing-dependent absorption 未考虑造成高能量端偏差。此种“偏差→受影响主张→为何仍可用”的写法值得采用，但本稿必须以自身数据判断。

应用：此源可实际引用于 Discussion，说明从几何/导热场到材料结构解释需要明确热历程与流动条件。只能说本稿 x/v 是无液体流动的移动稳态材料通过时间；它不是 Hou 的流体质点轨迹，也不提供 oxide/microstructure 预测。Fig.13 定义 tracer 与运动，Fig.14 对应 thermal excursion 和温度敏感 solubility；这是图间接续职责的清晰样例。

### Bayat et al. (2019), 10.1016/j.addma.2019.100835

*Keyhole-induced porosities in Laser-based Powder Bed Fusion (L-PBF) of Ti6Al4V: High-fidelity modelling and experimental validation*。借用研究线目录 PDF，只读。首部实际为出版商 **UNCORRECTED PROOF**，卷期/页码为 xxx，不能视为最终版式或引用最终出版页码。

本代理实际读：p1 摘要与 Introduction 开头，p2 Introduction 部分；未读相关 Results/Discussion、未核参考终点、未视觉检查。摘要可支持它包含 Flow-3D finite-volume、高保真物理、multiple reflection/ray tracing 与 Fresnel 吸收，并用 X-CT/显微形貌比较 pores。具体 parameter comparisons 和性能强度不在本交付认证范围，由已读该文的研究线代理/协调者定向核对。

可学的首部进程：工艺和缺陷 → insufficient/excessive heat 的不同孔隙来源 → ex-situ 不能揭示形成过程、in-situ 成本与数据处理 → 数值模型对交互物理的需要。正文的 generic 工艺讲解偏长，当前稿不需要模仿。不可用摘要中的“very good agreement”代替定量比较。Bayat 是期刊样本集合中的真实来源，但其未读范围不得消失。

### 补充：Tian et al. (2024), 10.1016/j.addma.2024.104505

*Operando visualization of porous metal additive manufacturing with foaming agents through high-speed x-ray imaging*。OSTI2569860 本地 **CORRECTED PROOF**，14 页，Crossref AM94/104505，55 个编号参考项。正文参考列表重复若干同一来源（例如 [35]/[38]、[39]/[53]），因此 55 是编号项数，不等于独立参考文献数。不能把该样本直接作为“应该引用55篇”的依据。

实际读：摘要、完整 Introduction pp1–2，Methods pp2–4，相关 Results/Discussion pp4–5、pp7–12、完整结论 pp12–13、参考终点 p14。已渲染 p1/p11/p14 但未实际视觉打开。Discussion 以不同 pore 指标的问题组织；Fig.10 p11 先定义归一化 pore depth 的分母，再展示同工况的绝对/相对趋势。VDSZ 是代理观测量，作者明确该量与真 melt volume 的近似关系、2 μm/px 检出限以及不观测 powder/substrate 以上 pores 的范围。

应用：本稿 L、W、D 与时间指标的观测定义要同样先给；相比之下量值趋势不能绕过分母或阈值。作者保留孔隙绝对数与密度趋势相反，以及 foaming-agent 加多未必增加孔隙的反直觉事实；并把 laser-reflectivity/heating-mode 解释写为需未来验证的 hypothesis。不能将其 porous Ti64/foaming-agent 结论用于本稿 residual。

## 参考文献数量的适用边界

| 样本 | 实际编号项数 | 数量对应的科学职责 |
|---|---:|---|
| Hooper 2018 |17|聚焦的一项高速温度测量及热梯度/冷却应用|
| Myers 2023 |43|两色测温方法、校准与六条件模型比较|
| Lane absorption 2020 |52|吸收测量、同轴监测、形貌与动态关联|
| Zafari 2025 |69|新 alloy 对比实验、完整速度场、多个竞争力机制与物性来源|
| Hou 2024 |72|材料化学、结构表征、CFD、尺度分析、溶解/成核/长大、多道 case studies|
| Bayat 2019 proof |未核验|本代理未读参考列表，不填估计值|
| Tian 2024 proof（补充） |55编号项，含重复|foaming、成像/处理、代理指标、孔隙统计与多机制比较|

原三篇均值 37.33；前五个 final VoR 均值 50.6，跨度17–72。前者不能成为最低量，后者更不能成为此六解 closure case 的最低量。高参考数样本承担更多材料/实验/化学机制职责。当前稿引用应覆盖基准数据与观测算子、热物性/相变数据、方程和移动坐标、竞争模型/校准限制、材料通过时间解释、对比条件与应用范围。协调者规划的至少38条真实有功能来源可作为当前覆盖计划；它不是期刊硬门槛，实际支持程度由正文每条论断判断。避免只为达到数目引用不相关的目标期刊样本。

## 版式观察与可执行选择

这部分仅来自 actual final PDFs；Bayat/Tian proofs 不替代最终 typography。已测新增 Zafari/Hou 页尺寸 595.276×793.701 pt，约210×280 mm。最终普通正文约8 pt，摘要/图注约7.2 pt，末页编号参考约6.4 pt；title 约13.4 pt。原三篇亦为同类紧凑双栏阅读布局。该密度是出版后观察，不是投稿规范。

| 已读页面 | 观察 | 对当前阅读版的选择 |
|---|---|---|
| Myers p8/Fig.7 |配对条件、相同色轴，多面板承担同一个比较|保持四角符号/颜色在 property、geometry、rear、time 图一致|
| Hooper p11/Fig.14 |时间历史有单独图与轴职责|time 图独立于 spatial/rear 图，图注先定义映射与阈值|
| Lane p11/Figs.10–11 |横截面与量化宽深配对|现有 geometry 图旁清楚呈现宽浅残差和观测身份|
| Zafari p13/Fig.13 |全宽两面板定义尺度模型，正文仍双栏|必要模型定义可全宽，但本稿无需添加未求解 flow 示意|
| Hou p9/Fig.13、p10/Fig.14 |运动轨迹定义图接到 thermal-excursion 图|property 作为 Methods 图，rear/time 作为 Results 图，减少读者追溯符号|
| Zafari p16、Hou p23 |双栏参考末页留有大量正常空白|不为满页效果删参考/压字体；允许自然末页节奏|

使用正式 elsarticle 产生阅读版，可保留较紧双栏和合适全宽图；不要复制 Elsevier logo、已发表 DOI/卷期、接收日期等身份。图字体按实际置入物理尺寸检查，正文8 pt观察不等于图标签可以缩到不可读。最终稿的并排页比较、实际图置入尺寸和全页审查由产稿代理完成，本交付没有检查未产出的R2 PDF。

## 官方要求、观察与未核事项分开

**已取得的官方出版商通用资料**：Elsevier LaTeX instructions（本地 `latex-official.txt/html`）推荐 elsarticle；最终 bibliography 要按期刊 guide；source submission 应提供 TeX/Bib/图与非标准依赖。页面提到多数期刊首次接受 PDF，这不能作为 AM 特定保证。旧 literature 有官方 elsarticle package，本次未改动。

Elsevier generative AI policies（本地 `ai-policy-official.txt/html`，Policy updated June2026）规定实质写作辅助需在 references 前声明工具、用途、人类复核/责任；研究方法中的 AI 分析/可复现绘图应在 Methods 披露；真实 primary-data 图不可生成或篡改。解释性 AI diagram 需真实且 caption/general disclosure；general-purpose genAI 不用于 graphical abstracts。它是出版商通用政策，未替代 AM guide。

**AM Guide for Authors 未实际取得**：当前URL为 https://www.sciencedirect.com/journal/additive-manufacturing/publish/guide-for-authors 。HTTP/fetch403与浏览器未成功，不填摘要250词、highlights/graphical abstract是否必须、匿名规则、具体图上传和数据清单等未核硬条件。提交前可定向补核；不因此阻塞当前有依据的正文修订。

**获取缺口**：Vanini2024 DOI104369、Liu2024 DOI104111、Weeks2026 DOI105245 已核元数据，但合法普通下载/机构浏览器路由未得到可读PDF。不得记为已读、不用于方法细节断言。其他 OSTI author manuscripts、pre-proof/更早 proof 的版次分类保存于 index，未替代 original final PDF。最新邻近路线的搜索结果不能等同全文支持。

## 交付建议与未解决项

可立即使用本 profile 继续R2 Methods/Results/Discussion 写作。Hou 可增加一条有明确职责的 Discussion 比较，Plotkowski2017 可作早期实用热模型→凝固解释的限定背景，详见 `source-use.md` 与 `new-sources.bib`。Zafari/Tian 主要承担期刊论证学习，不需为了样本计数强塞正文。

保留的缺口仅影响对应范围：AM当前硬投稿条件尚未核；Bayat后文/参考与视觉尚未由本代理完成；Tian proof 非最终版且视觉未打开；当前R2成稿尚未进行全文独立review。本交付不将这些缺口消解为共识或PASS。
