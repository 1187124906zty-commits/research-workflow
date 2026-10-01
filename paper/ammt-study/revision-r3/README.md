# R3：科学编辑、逐句来源核对与独立成稿审查

本轮针对正文实现细节过多、具体因素讨论借用宽泛背景引文、章节分散和承接不足开展修订。沿用原有六组生产解，没有新增 PDE 求解，也没有提升物理验证等级。正式稿始终维护在同一个 [LaTeX](../manuscript.tex)、[PDF](../manuscript.pdf) 与 [完整源码包](../submission-source.zip)。

## 实际分工与返回

| 责任 | 实际返回 | 如何用于整稿 |
|---|---|---|
| 科学编辑 / PaperSpine 方法 | [原件结构学习](editorial/venue-structure-audit.md)、[Methods 候选](editorial/methods.tex)、[Discussion 候选](editorial/discussion.tex) | 协调者将方法、讨论各整合为四个科学单元，重写摘要、引言、结果承接和结论；软件设置另入复现说明 |
| 逐句来源核对 | [引用审查](citations/citation-audit.md)、[支持账本](citations/support-ledger.json)、[定位建议](citations/recommended-replacements.tex) | 19 项关键表述、11 个实际来源、7 项本研究推导/结果，区分 full/partial 与具体材料、条件和读取边界 |
| 当前原证据复核 | [来源更新审查](evidence-refresh/audit.md)、[核对结果](evidence-refresh/verified-current.json) | 原始可变展示文件版本改变后，回读主要结果再记录当前支持，不重写历史绑定 |
| 独立整稿评阅 | [实际评阅](review/independent-review.md)、[协调者处置](review/review-response.md)、[修复复核](review/repair-verification.md) | 读取整合后源码、渲染页与必要原件；定位问题、修复，再核验受影响部分 |
| 构建与交付 | [交付检查](delivery/delivery-check.json)、[源码包重建](delivery/package-rebuild-check.json)、[实际来源](delivery/provenance.md) | 保持图表、引文、正式源码和 PDF 一致，检查公开介绍链接及实际重建范围 |

四篇直接结构样本是 Myers 2023、Hooper 2018、Coleman 2024 与 Plotkowski 2017。它们分别展示 measurement-first 方法组织、空间/时间解释分工、建模与标定承接，以及从几何检验转向凝固条件的论证关系。原文标题与阅读位置逐项记录；作者稿不冒称出版社排版样本，观察惯例不冒称 AM 正式投稿要求。R2 的近期研究追踪和原始数据审查继续作为历史输入保留。

## 可复用审查模式

通用规则见 [ResearchFlow 审查交接](../../../docs/manuscript-audit.md) 与 [MAF 论文审查模式](https://github.com/1187124906zty-commits/research-assistant-maf/blob/codex/maf-reconstruction/docs/manuscript-audit.zh.md)。协调者指定科学编辑；文献角色核对句子与原件，机制角色区分观察/解释，写作角色实施修订，独立评阅角色检查实际修复稿。

同一来源可以用于不同位置，但必须分别支持各处实际表述。数值设置需要选择与误差依据，物理参数需要来源及条件，拟合参数需要标定目标与数据角色；本研究推导不能借一篇相似文献伪造出处。正文、附录、[复现说明](../reproduction-notes.md) 与执行来源记录各承担不同的读者任务。

R3 是实际 Codex 多智能体修订及 MAF 角色提示改进。R2 原生 MAF writer 批次的超时记录保留；本轮未将后续 Codex 评阅倒填为那个未完成批次的节点成功。软件测试和确定性提供者演示只验证运行协议，不能证明科学或期刊质量。当前 AM 专属指南、人工作者核查和独立热史验证仍有明确缺口。
