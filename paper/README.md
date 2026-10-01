# ResearchFlow 方法与系统设计论文

正文：[researchflow-design.zh.md](researchflow-design.zh.md)。独立 LaTeX 源：[researchflow-design.zh.tex](researchflow-design.zh.tex)。

题目为 **ResearchFlow：基于技能与证据约束的多智能体科研协同框架**。中文正文附英文题目、摘要和关键词，采用动机、相关工作、组织对象、架构、治理协议、研究循环、实现、讨论和结论的结构。

本篇稿件讨论设计依据和可实施方法，不含实证结果、演示数据、效率提升幅度或发表成功率。既有软件检查继续保留在项目验证文档中；其结果没有被转写为论文的研究发现。作者署名、单位和目标期刊未被代填。

Markdown 是供 GitHub 阅读和修订的正文。LaTeX 是同一正文的独立排版源，内含参考文献，无外部 bibliography 或图形依赖。`scripts/render_design_paper.py` 从 Markdown 生成 LaTeX；排版需要支持 UTF-8、ctex/Fandol 字体的 XeLaTeX 或兼容 Tectonic 环境。这些是可选排版条件，不是 ResearchFlow 的运行依赖。

修改正文后，从仓库根目录重新生成同一份排版源：

```powershell
python scripts/render_design_paper.py
```

2026-10-01 的排版检查状态：已调用 Codex 内置编辑器打开源文件；内置编译器返回平台目录错误 `Unable to find standard directories for platform`，未能完成编译。此错误没有给出正文或 LaTeX 行级诊断，因此当前保留可编辑源文件，不将其标记为已通过 PDF 排版检查。

参考来源的检索与核对说明见 [source-notes.md](source-notes.md)，结构化记录见 [source-notes.json](source-notes.json)。项目依赖与兼容状态单独维护在 [compatibility.md](../docs/compatibility.md)，避免将某个版本的接口状态固化为方法本身。最新设计论文随当前仓库维护；v0.1.0 发布源码包对应首次工具发行，未被后续文档更新重新打包。
