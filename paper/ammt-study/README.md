# AMMT IN625：从既有多 Agent 模拟到期刊研究初稿

[阅读 R3 英文稿 PDF](manuscript.pdf) · [编辑 LaTeX](manuscript.tex) · [核对当前引用](literature/bibliography-r3.bib) · [近期研究线](revision-r2/literature/research-line.md) · [期刊学习](revision-r2/journal/journal-learning.md)

需要完整源文件时，可下载 [扁平 LaTeX 源码包](submission-source.zip)，其中包含 TeX、当前 BibTeX、highlights、五幅矢量图和复现说明。它是供修改与评阅的完整初稿包，投稿元数据仍待负责研究者补齐。

本案例围绕 **几何标定的实用价值与凝固热解释所需约束之间的科学矛盾**，整理为面向 *Additive Manufacturing* 读者的英文研究论文初稿。全文从已有模型与测量成就收束到一个有限研究点：固定已标定热源，分解高温物性变化、后部相界位移和材料时间。它具有摘要、关键词、充分的历史与近期研究背景、完整模型与观测定义、数值核查、结果、具体讨论、回扣科学矛盾的结论、数据声明、AI 使用声明和 26 项实际引用。

数值研究原由 [SimAgent](https://github.com/1187124906zty-commits/simulation-agent-research) 完成。本次 **ResearchFlow 任务治理 → 文献/期刊/证据专家 → PaperSpine 本地论证方法 → MAF 分章写作 → 章节交叉审阅 → 协调者整合 → 独立全文评阅** 在既有证据上执行。没有重新求解 PDE，也没有把 ResearchFlow/MAF 的参与追溯为原始模拟来源。PaperSpine 使用本地学术方法和实际文件适配器，未声称调用其在线产品或替用户点击配置。

R3 进一步执行 [科学编辑与逐句来源审查](revision-r3/README.md)，将方法和讨论各收拢为四个科学单元，移出库、agent 和求解器设置，补齐公式/参数/解释的直接来源与本地推导身份。当前引用数量反映本稿实际用途；历史 R2 的 39 项不作为本轮数量指标。复现信息见 [reproduction-notes.md](reproduction-notes.md)。

R2 原生 MAF 批次实际派发引言和讨论 writer；引言完成结构化返回，讨论产出章稿后在 1500 秒期限下中断。该批次的原生 reviewer/requester 未执行。协调者保留实际文件与超时记录，通过另行 Codex 专家交叉审阅和全文评阅推进稿件；[真实运行记录](revision-r2/native-drafts-record.md)与[MAF 诊断](https://github.com/1187124906zty-commits/research-assistant-maf/blob/codex/maf-reconstruction/examples/ammt-deep-revision/recovery/diagnosis.md)区分这些范围，未将部分运行报告为自动闭环。

![三工况的实际温度场与熔合区包络](figures/ammt-research-operating-cases.png)

## 稿件得到的结果

- B 工况拟合长度为 **359.16 μm**，但宽度为 **143.04 μm**、深度为 **31.12 μm**，参照均值为 **123.5/36 μm**。长度拟合没有解决宽浅偏差。
- 固定 B 的四角对照将联合长度响应分解为 **+43.21 − 6.17 − 2.76 = +34.28 μm**。主要变化是后部固相线与液相线共同平移。
- B/C 的后部相变空间跨度为 **80.26/80.79 μm**，但材料通过时间为 **100.33/67.33 μs**。空间相近不等于冷却历程相同。
- 保存场和原始执行绑定经过只读核对。基准 B 轴向精化使长度改变约 **0.361 μm**，支持讨论大热尾响应；它没有认证所有小交互的精度。

这些是当前传导/潜热模型内的结果。B 长度参与标定，A/C 为公开数据下的固定参数**非盲比较**。高温分支是线性延续与保持末值两种模型规则，没有识别真实液相物性或 Marangoni 流。长度与宽深来自不同观测及轨迹群；NIST 当前宽深均值和 Lane 扩展不确定度来源分别说明。稿件尚未经期刊同行评审。

## 工具如何用于本次写作

| 环节 | 实际使用 | 可核查产物 |
|---|---|---|
| 科研治理 | ResearchFlow 状态运行时，登记任务、结果、协调者解释与论断范围 | [治理配方与交接](governance/) |
| 原始证据审查 | 专门 evidence Agent 读源码、数据、保存场和实验定义 | [证据审查](evidence/evidence-dossier.md)、[核实数据](evidence/verified-data.json) |
| 期刊与文献 | 两项专家任务追踪近邻至 2026-10-01，核实身份、阅读范围、对比条件与反证 | [研究线](revision-r2/literature/research-line.md)、[期刊学习](revision-r2/journal/journal-learning.md) |
| 建模与定量结果 | 专家只读原执行绑定、六个保存场、物性和观测代码；协调者采用方法/结果候选 | [R2 定量审查](revision-r2/methods-results/audit.md) |
| 分章与接口 | 实际 `agent-framework-core==1.19.0` writer 批次；另一专家审阅引言–方法–结果–讨论接口 | [原生返回状态](revision-r2/native-drafts-record.md)、[交叉审阅](revision-r2/exchange/cross-section-review.md) |
| 成稿与评阅 | 协调者合成全文、学习期刊论证习惯；新上下文审查实际稿件与页面 | [当前全文评阅](revision-r3/review/independent-review.md)、[修复处置](revision-r3/review/review-response.md) |
| PDF 验证 | XeLaTeX/BibTeX 真实编译、页面渲染与图文检查 | [LaTeX](manuscript.tex)、[PDF](manuscript.pdf) |

软件协议审计检查交接和证据绑定，不判断科学真伪。原 R1 有已完成的有限 MAF evidence review；R2 native 写作批次中断，不能移用 R1 完成状态。R2 章节与实际全文另由专家读取，各检查范围分别说明。同模型不同上下文的审查不是统计独立的人类期刊同行评审。

## 期刊样式与当前限制

目标期刊是 *Additive Manufacturing*。采用官方 Elsevier `elsarticle` 的 `preprint,12pt` 与编号参考文献，按该期刊真实论文的读者逻辑组织 Introduction–Methods–Results–Discussion–Conclusions，并提供 [highlights](highlights.txt)。阅读版将单栏正文宽度设为 180 mm、高度设为 245 mm，以保持原矢量图标签可读；当前为 18 页。此尺寸是本稿阅读选择，未冒称 AM 专属投稿要求，印刷后的双栏版式由出版社处理。

已经读取合法公开取得的目标期刊原文，并记录具体学习位置。R2 目标学习包含五篇 final VoR 和一篇已实质阅读的 corrected proof；其版次与视觉范围分别记录，未冒称六篇 final。Paper Access 机构下载入口实际串行尝试四项关键全文，其中三篇 AM 和一篇热传导期刊未暴露 View PDF；未虚报取得全文。当前期刊专属 author guide 返回 403/验证码，摘要硬限、图形摘要、匿名规则等条款尚未核实；[当前学习索引](revision-r2/journal/source-index.json) 将可验证的官方要求、样本惯例和缺口分开。没有绕过访问控制，也不在仓库分发下载的期刊全文。

提交前仍需负责研究者补齐作者/单位/通讯作者、贡献、经费与利益冲突声明，完成全文人工核查，并依法获得当前期刊专属投稿条款。最主要的科学风险是**顶刊贡献充分性**：既有材料支持模型失配和有限物性敏感性研究，尚未证明新的计算方法、独立预测验证或广泛物理机制。更强论断所需判别证据见正文讨论及独立评阅。

## 文件与重建

- `data/`：已有结果的原精度 CSV、材料表及紧凑 JSON；不是新实验数据。
- `figures/`：原始绘图生产的 PDF/SVG/PNG，来自记录数据和场；不使用生成图像替代数据。
- `evidence/`：冻结审查与只读核对配方；原始字段定位可能含开发机路径，请使用 SimAgent 对应案例路径映射。
- `governance/`：真实工具使用记录与源码；运行时状态本身保持本地，公开清理后的交接/审计。
- `literature/`：引用与阅读/要求记录；第三方全文、出版社模板包和浏览器页不发布。
- `review/`：实际独立评阅意见与协调者修订处置。

在此目录使用 TeX Live（或提供 `elsarticle`、`siunitx` 等包的等价 LaTeX 环境）：

```powershell
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

LaTeX 源、当前 BibTeX 与五幅矢量图完整保留。桌面内置编译器本次仍报告 `Unable to find standard directories for platform`；交付 PDF 使用本机已有 TeX Live 2026 编译。源文件仍可在内置编辑器修改，未创建替代编辑文档。

完整源码包已解压至独立构建目录，在现有 TeX Live 2026 下完成 XeLaTeX/BibTeX 重建，18 页逐页提取文本与当前 PDF 一致，且所用五幅矢量图与当前稿件一致；[重建记录](revision-r3/delivery/package-rebuild-check.json) 限定了实际验证环境。这项检查不表示其他平台已验证，也不表示数值研究已重跑。

此包没有重复发布六个完整温度场、大型求解器环境或原始全部执行日志；不能仅凭紧凑表格重跑 PDE。完整求解再现需要原案例的脚本、执行清单和所指字段。代码适用项目许可证；本稿与用户授权的案例图表为研究初稿材料，不授予第三方论文/实验图像的转载许可。
