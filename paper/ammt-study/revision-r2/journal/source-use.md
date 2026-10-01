# R2 新源使用建议与边界

本文件给协调者具体引用职责；不直接修改 canonical TeX/Bib。引用是否进入正文由协调者按最终论断决定。这里见过 `argument-r001.md`，因此这些建议是证据绑定的写作支持，不是盲审。

## 推荐增加：Hou2024Dissolution

- 版本：已读 original final publisher PDF，DOI 10.1016/j.addma.2024.104554；见 `pdfs/dissolution2024.pdf`。
- 实际支持：§4.3 pp8–10/Figs.13–14 显示 fluid elements 在流动中经历位置相关 thermal excursions；§4.7 p13 采用经CFD缩放的 Eagar–Tsai 温度/时间解。原文 CFD 表面轨迹峰更窄、深处更热，且 convection/recoil depression 影响轨迹。它不是未修改导热模型即可复制流体热史的证据。
- 可放：Discussion 的材料通过时间与热历程解释段；Introduction 仅需要一处说明凝固相关应用需要热历程条件。
- 可用英文句意：`For structure-sensitive interpretation, the trajectory represented by a thermal history must be specified: Hou et al. constructed location-dependent excursions of fluid elements and scaled a conduction solution against CFD, whereas the present passage times follow material translation through a steady field without liquid flow.`
- 本稿推断另列：四角变化说明当前闭合场的通过时间敏感，不等于实际 fluid-parcel residence、组织变化或独立温度实验验证。
- 不能用来支持：本稿 IN625 宽浅残差的唯一机制；同工况性能排名；本稿导热模型具有 oxide/phase prediction 能力。

## 推荐但需协调者保留原文定位：Plotkowski2017Rapid

- DOI 10.1016/j.addma.2017.10.017；本地 `pdfs/vverification2017.pdf` 是 author manuscript，不是最终排版。
- 元数据身份：Plotkowski, Kirka, Babu；Additive Manufacturing18,256–268 (2017)。OSTI1408593 保存了完整摘要；本代理只检查title page并读到该保存摘要的内容，未完成正文方法/结果学习。协调者已独立读abstract，可据该范围使用狭窄背景断言。
- 摘要实际支持：实用 semi-analytical transient heat-conduction 方法用于 AlSi10Mg SLM 和 IN718 EBM simple geometries 的理论验证、与Rosenthal稳态比较，以及EBM IN718两种 point-melt scan strategies 的结构比较。其控制变量包括 scan strategy、diffusivity和preheat，不能当本稿AMMT裸板三工况的温度验证。
- 可放：Introduction 的“实用热模型已用于凝固相关解释，但应用条件与验证必须具体”背景句。
- 可用英文句意：`Pragmatic heat-conduction models have already been used to estimate transient solidification conditions and relate scan strategies to grain structure, including the semi-analytical study of Plotkowski et al.` 后接该文AlSi10Mg/IN718与本稿条件不同的一句即可，避免反复免责声明。
- 若要写公式、性能速度、具体G/R准确性或CET阈值，须补读原文对应页；不能从摘要制造这些细节。

## 可选而非必须：Zafari2025Operando

- 已读VoR，§4.3 pp12–14：直接flow observations与简化力尺度相互约束，某些流动形态不能单靠Marangoni解释。
- 唯一有用正文职责：Discussion 若比较本稿未含的liquid-flow physics，可举直接operando flow证据作为相邻研究，而保持Al-Sn、powder、transient的条件。
- 不用于解释IN625 residual，也不引用其约1m/s作为本稿真实velocity。其原文“two orders”与0.06–0.09m/s对约1m/s并不严格一致，引用数量级时遵守原数值而非夸张文字。
- 默认不插入正文：Hou与已有高保真研究已能承担同样范围职责时，Zafari只留作journal-learning。

## Bayat与Tian

Bayat2019 已由研究线代理处理；本代理只核首部UNCORRECTED PROOF与摘要/部分引言，不新增bib重复条目。Tian2024 CORRECTED PROOF的代理观测量/归一化比较可学写法，但研究主题是foaming Ti64，和当前closure问题关系弱，默认不引用。

## 引用数量

参考量按真实论断覆盖判断。17、43、52、69、72的样本跨度来自不同任务，37.33旧均值、50.6五final均值均不是稿件下限；Tian55编号项还含重复来源。至少38有功能来源是当前协调者覆盖计划，非AM官方要求。新增bib只包含具具体职责的Hou、窄背景Plotkowski与可选Zafari，不能仅为凑数全部调用。
