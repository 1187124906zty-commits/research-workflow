# R5 交付与执行范围

日期：2026-10-02。当前交付是同一份 IN625 研究初稿、独立项目写作资源和真实审阅/修复记录；原安装技能及 SimAgent 数值案例保持原状。

## 实际使用与证据来源

- ResearchFlow 保存来源、结构、指南、实际修稿、审阅和交付任务；主协调者写共享状态，专家写各自候选与报告。
- 同任务 Codex 专家读取当前 MAF `guidance.load_role` 的实际导出，分别完成来源/Methods–Results、架构/Introduction 和指南/整稿审阅；两名作者交换五项承诺，协调者整合标题/摘要、Discussion/Conclusions 并处理实际审阅意见。
- R5 没有执行新的原生 MAF 模型/provider 写作批次。已发表的 R4 原生执行记录保持其历史身份。R5 的 MAF 实际图和 CLI 检查使用 demo 提供者；它验证框架/资源分发，不是一次真实论文模型写作或效果实验。
- 六个生产解及原始数值证据来自既有 SimAgent 工作。R5 新增生产 PDE 次数为 0，没有回溯改写原数值研究的执行来源。
- 来源阅读及指导来源分属 [领域来源报告](../sources/report.md)、[指导覆盖审计](../guidance/coverage-audit.md)和[精确指导来源](../guidance/source-ledger.md)。原期刊/机构全文与私有阅读抽取不在仓库发布。

## 实际验证

| 项目 | 结果与范围 |
| --- | --- |
| MAF 测试 | 95 项通过，覆盖显式 writing 范围、角色/参考直接分发、审阅反馈和现有工作流；未宣称通用写作质量得到统计验证。 |
| ResearchFlow 测试 | 38 项通过；过程与绑定检查不能代替科学判断。发布前审计 protocol_ok=true、阻断项为 0；历史已关闭任务的原输入/候选后续变化仍报告为非阻断警告，不被抹去。见 [governance-audit.json](governance-audit.json)。 |
| 项目 skill 检查 | 九项 MAF 项目技能及项目 governor 的 frontmatter 校验通过；原安装技能未修改。 |
| 打包实际运行 | 构建新 wheel，在源码目录外安装读取随包短方法并执行实际工作流 demo；本地 demo/status 也完成，两循环，protocol_ok=true。 |
| 原始编辑器编译 | 保存正稿后调用内置 compile_latex_document；实际返回 `Unable to find standard directories for platform`，未声称其成功。原编辑器保持打开。 |
| 同源 PDF 构建 | 使用本机已有 TeX Live 2026 的 XeLaTeX/BibTeX/XeLaTeX/XeLaTeX；20 页，无未定义引用、缺字或 overfull 诊断。未安装替代 TeX。 |
| 源码包独立重建 | 解压当前扁平 zip 后实际编译，20 页逐页文本与当前 PDF 相同；五幅使用的矢量图、BibTeX 与复现说明匹配。见 [package-rebuild-check.json](package-rebuild-check.json)。 |
| 稿件交付检查 | 核对引用身份、图件、PDF、编译日志、源码包及当前项目/指南链接。见 [delivery-check.json](delivery-check.json)。 |
| 物性图 | 只更新定义标签并保留曲线源数据；字号、对齐、碰撞及实际视觉检查通过。自动碰撞记录见 [property-figure-collisions.json](property-figure-collisions.json)，vector 为使用格式。 |
| 全文审阅 | 审阅者实际检查全部 20 页；正文对象/出处、目录和反向提纲按完整源码检查。修复及真实复核见 [review-response.md](../review/review-response.md)。 |

这些验证是各自范围内的实际检查。R5 的五项历史变更警告分别来自公开链接修复、交接说明更新和实际评阅后的候选修复；它们不绑定物理支持论断，最终交付重新绑定现行文件及修复记录。独立职责和上下文帮助发现问题，但审阅者同模型且有既往曝光；没有人类同行评审、跨平台编译或全 PDE 重放的结论。当前期刊专属 author guide 的访问缺口、作者与实际人类监督信息、真实热观察和贡献充分性仍分别保留。
