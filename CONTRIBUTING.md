# 参与贡献

欢迎改进科研协作、证据交接、工具适配、研究案例、测试与文档。小修复可直接提交 Pull Request；较大的状态协议、接口或研究流程变更，可先用 [Issue](https://github.com/1187124906zty-commits/research-workflow/issues/new) 描述问题、方案和验证依据。

## 提供可复现的反馈

| 类型 | 建议提供 |
|---|---|
| 安装、CLI 或集成错误 | 操作系统、Python 与宿主版本、执行命令、最小材料、关键日志 |
| 治理与证据规则问题 | 具体任务、输入/返回、预期处置与实际状态、受影响的论断 |
| 新工具或研究案例 | 原始出处、输入输出、版本、执行条件、验证方式和分发许可 |
| 文档与使用建议 | 使用场景、遇到的障碍、建议改法与相关页面 |

使用讨论也可在 [QQ 社区](docs/COMMUNITY.md) 进行；需要追踪的缺陷和改进同步到 Issue。公开材料使用 DOI、官方链接或获准分发的数据，保留必要的脱敏复现信息。

## 提交代码与文档

在自己的分支或 fork 中修改：

```powershell
git switch -c codex/your-change
python -m pip install -e .
```

阅读 [AGENTS.md](AGENTS.md) 与 [设计说明](docs/design.md)。保留其他协作者的改动；共享研究状态由协调者维护，独立任务使用各自输出路径。

Python 与协议修改执行标准测试及受影响的真实 CLI 或示例：

```powershell
python -m unittest discover -s tests -v
python scripts/independent_check.py
python examples/steady_diffusion/run.py --project ./local-runs/contribution-diffusion
```

示例使用新的输出目录。skill 实质修改需验证 frontmatter，并以独立的现实任务检查实际使用与返回。纯文档修改检查链接、命令和显示；图件修改查看最终导出。PR 描述具体问题、最终行为、实际验证和剩余边界。

## 科研案例与状态规则

- 参数、方程、实验条件与数据给出可检查来源，明确合成材料与实际研究。
- 原始输入与产物保留，区分观察、数值核验、物理验证、标定与比较。
- 接收有用交付和支持科研假设分别处理；负面结果与反证继续可见。
- 外部工具的运行回执与科研主张分别判断，数值充分性由用途和关注量决定。
- 稿件论断指向实际证据，保留模型假设、限制及未执行的验证。

本项目采用 [MIT 许可](LICENSE)，上游产品和外部资料遵循各自许可。说明新增材料的来源与可分发范围，见 [第三方说明](THIRD_PARTY.md)。PaperSpine 管理文件、用户凭据和既有全局配置由各自所有者维护。
