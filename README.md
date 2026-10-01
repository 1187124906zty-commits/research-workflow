# ResearchFlow：面向 Codex 的多智能体科研治理框架

ResearchFlow 是一个以 skill 为知识与流程载体、以轻量运行时为状态基础的多智能体科研协调框架。项目面向从研究问题形成、文献与工具能力调查，到证据获取、机制解释、论文写作和独立评阅的完整研究过程。

框架关注研究目标与局部执行之间的失衡：执行智能体可能持续优化数值精度、检索覆盖或文字表达，而未说明这些投入是否改变研究判断。ResearchFlow 将研究问题、论文论断、证据层级、任务预算和返回条件显式关联，使专业执行服务于可演化的整体研究路线。

项目采用 MIT 许可，当前版本为 **v0.1.0 预发布版**。

- [源码仓库](https://github.com/1187124906zty-commits/research-workflow)
- [版本发布与源码包](https://github.com/1187124906zty-commits/research-workflow/releases/tag/v0.1.0)
- 设计论文：[中文正文](paper/researchflow-design.zh.md) · [LaTeX 源文件](paper/researchflow-design.zh.tex)

设计论文阐述问题、动机、治理原则与系统架构，不包含实证结果。最新论文随当前仓库维护；v0.1.0 源码包对应首次工具发行，未被后续文档更新重新打包。软件检查、示例与既有行为观察另见[验证记录](docs/validation.md)。

## 定位与设计原则

ResearchFlow 提供科研协作的组织方法与可检查状态，不提供通用数值求解器，也不把程序运行成功等同于科学结论成立。研究协调者负责问题、论断范围、任务优先级和下一行动；专业角色负责各自的调查、证据生产、解释或评阅。

框架遵循以下原则：

1. **研究路线允许演化。** 阅读、工具试用与反证可以改变问题、模型和论文框架；一次运行的输入应固定，整个研究方向可有依据地调整。
2. **要求由用途与论断确定。** 数值精度、检索深度和重复试验依据关注量、效应尺度、不确定性与用途设置，保持方程、单位、证据真实性及校准与验证的区别。
3. **任务有明确的回传点。** 委派说明研究意义、输入、交付、预算、验收依据和返回条件；请求者解释结果意味着什么，再决定下一行动。
4. **负面结果保留科研价值。** 接收任务交付与支持研究假设分别判断。反证影响相关论断及其依赖，失败记录不因收窄论断而消失。
5. **上下文按任务组织。** 持久状态保存当前理解和证据定位；工作智能体读取相关任务与必要原始材料，避免重复载入全部历史。

两轮没有改变研究理解时，默认返回协调者重审。这个条件触发研究判断：继续投入、采用更有区分力的检验、调整论断或推进另一项工作。它不构成科学充分性的统一标准。

## 系统组成

| 组件 | 位置 | 职责 |
| --- | --- | --- |
| 规则入口 | `templates/AGENTS.research.md` | 在适用科研任务中调用治理 skill，约定协作与状态记录方式 |
| 顶层治理 skill | `skills/research-workflow-governor` | 演化研究问题、安排阶段与任务、解释证据、衔接论文论证 |
| 模拟 skill | `skills/simulation-project-orchestrator` | 组织有限模拟任务、真实执行与逐论断验证；专业求解器另行配置 |
| 专业角色 | `templates/agents/rf_*.toml` | 文献、论证与写作、证据生产、机制分析、独立评阅五类职责 |
| 状态运行时 | `src/researchflow` | 保存研究理解、任务契约、证据版本、依赖与处置，提供审计命令 |
| PaperSpine 适配器 | `integrations/paperspine` | 导出写作交接包，诊断并调用单独安装的上游公开接口 |
| 安装与开发工具 | `scripts` | 安装自有 skill、角色和规则入口，执行检查与维护者发布流程 |

五类角色是职责模板，实际按任务需要启用。独立证据任务可以并行；依赖前序结果的任务顺序开展。协调者单独写共享研究状态，工作智能体写各自声明的输出。

`AGENTS.md`、skill 与角色指令引导模型遵循治理约定。运行时检查其入口内的状态、证据绑定、预算和依赖，不能拦截任意外部工具调用，也不能自动判定机理、因果或期刊接受可能性。具体求解器和数据工具需要在项目中接入已登记任务，并在关键使用点审计。

## 研究流程

```mermaid
flowchart LR
    Q[研究想法与用户问题] --> L[文献研究线与工具能力调查]
    L --> P[候选期刊读者与暂定论证]
    P --> T[有限证据任务]
    T --> E[文献 · 实验 · 模拟证据]
    E --> J[解释与研究判断更新]
    J --> W[证据约束的论文成稿]
    W --> R[独立评阅与针对性修改]
    J --> P
    J --> T
    R --> T
    R --> W
```

PaperSpine 角色在早期参与期刊读者、贡献类型和论证方案，结果返回后参与正文与讨论。期刊惯例影响表达和所需比较，科学主张仍以实际证据为依据。模拟或实验角色先评估工具能力与可行性，再开展能够回答当前问题的有限工作。

工作流程区分探索、形成论文与最终评阅阶段。阶段决定当前任务需要的证据深度，并保留尚未完成的验证事项。具体设计见[设计说明](docs/design.md)、[治理 skill](skills/research-workflow-governor/SKILL.md)和[模拟规则调整依据](docs/simulation-audit.md)。

## 依赖与兼容

| 使用范围 | 必需条件 | 可选或外部条件 |
| --- | --- | --- |
| 状态运行时与 CLI | Python **3.11 或更高**；无第三方运行时 Python 依赖 | `pip` 用于安装；构建后端为 `setuptools>=68` |
| 完整 Codex 工作流 | 支持 `AGENTS.md`、本地 skills 和 subagents 的 Codex 客户端与可用模型账户 | 自定义角色 TOML 的发现取决于客户端版本；职责可显式委派 |
| PaperSpine 写作接入 | 基于文件的导出使用 Python 标准库 | 实时调用需要单独安装 PaperSpine、其运行环境和有效 profile |
| 数值或实验研究 | 本仓库包含模拟编排 skill | 求解器、软件许可、项目依赖、数据来源及实验设备由研究项目提供 |
| 开发与 GitHub 发布 | 检查使用 Python 标准库；源码安装需要构建工具 | Git 用于克隆；GitHub CLI 与认证仅供维护者发布 |

核心代码已在 Windows 和 Linux 的 Python 3.11、3.13 CI 矩阵中检查，本地使用 Python 3.12 验证。macOS 未经本项目测试。`requires-python >=3.11` 是包声明范围，不表示所有更新解释器、客户端或求解器均已验证。

本包不要求配置独立 API key，也不调用模型服务；Codex 或其他外部服务的账户、访问权限与认证由相应宿主管理。已核验的 PaperSpine 接口范围为 **0.4.0-alpha.3 / public request schema 1.1**，不构成对全部上游版本的兼容承诺。

布局、版本、profile 限制和外部软件接入条件详见[依赖与兼容说明](docs/compatibility.md)。

## 安装

克隆仓库或解压发布源码包，进入项目目录：

```powershell
git clone https://github.com/1187124906zty-commits/research-workflow.git
cd research-workflow
python -m pip install -e .
```

运行时安装与 Codex 集成安装分别进行。以下方式任选其一：

```powershell
# 用户范围：本项目开发时的桌面兼容布局 ~/.codex/skills
python scripts/install.py

# 用户范围：当前官方文档的 ~/.agents/skills 布局
python scripts/install.py --skill-layout agents

# 项目范围：先建立目标科研项目，再安装到其中
python scripts/install.py --project D:/my-research
```

已有本项目同名 skill 或角色时，安装器会停止并提示冲突。确认更新这些内容后，在所选命令末尾添加 `--update`。这个选项会覆盖本仓库提供的 skill 与角色文件；请先保留需要继续维护的本地定制。

项目安装使用 `.agents/skills` 与 `.codex/agents`；用户安装的兼容布局可以选择。不要在同一宿主可发现的多个位置重复安装同名 skill。安装器保留既有用户规则，只维护 ResearchFlow 标记区块；存在非空 `AGENTS.override.md` 时，将入口写入该优先文件。

安装不修改 `config.toml`、模型设置、权限或 PaperSpine 管理文件。完成后启动新的 Codex 运行，以重新发现规则与角色。源码包包含集成脚本、skills 和模板；仅安装 Python 包不会自动安装这些资源。

## 使用

在已有科研项目中向 Codex 提交研究问题，例如：

> 使用 $research-workflow-governor，以多 agent 模式推进这个研究项目。先调查现有材料、问题和工具能力，建立候选期刊论证与有限证据任务；依据结果调整问题和框架，完成论文草稿及独立评估。

协调者通过运行时保存 `.researchflow/research-state.json`，并按契约委派工作：

```powershell
python -m researchflow init ./study --question "哪个机制影响这个可测量的结果？"
python -m researchflow plan ./study ./plan.json
python -m researchflow task ./study ./contract.json
python -m researchflow context ./study --task pilot
python -m researchflow record ./study pilot ./result.json
python -m researchflow decide ./study pilot ./decision.json
python -m researchflow audit ./study
```

命令中的 JSON 是需要依据实际任务填写的计划、契约、返回和处置文件，字段与可运行示例见 [CLI 与状态协议](docs/API.md)。接收交付与提升论断分别登记；观察、数值核验和物理验证保留不同证据层级。

PaperSpine 的文件交接可独立于其 Web 服务运行。实时接入需要回读当前 schema，并检查目标 profile；已有启动冲突和证据 locator 的回读限制见 [PaperSpine 接入说明](docs/paperspine-integration.md)。本框架保留研究状态中的原始证据定位，不以服务页面状态替代科学审阅。

## 开发与验证

```powershell
python -m unittest discover -s tests -v
python scripts/independent_check.py
python examples/steady_diffusion/run.py --project ./local-runs/diffusion
```

标准检查覆盖状态恢复、契约、证据版本、反证、交接与安装；确定性扩散示例演示从数值求解到证据登记和技术稿的路径。它不调用模型或实时 PaperSpine，其合成输出仅说明示例工作流。

[验证记录](docs/validation.md)区分软件检查、有限模型行为观察和产品接口探针。它们的范围有限，不能推出长期科研可靠率、论文可接收性或所有客户端的兼容性。CI 配置见 [GitHub Actions](https://github.com/1187124906zty-commits/research-workflow/actions)。

## 文档、许可与维护

- [设计论文](paper/researchflow-design.zh.md)：研究动机、多智能体治理与系统方法。
- [依赖与兼容](docs/compatibility.md)：最低条件、已检查环境和未验证边界。
- [CLI 与状态协议](docs/API.md)：任务、证据、处置和审计字段。
- [PaperSpine 接入](docs/paperspine-integration.md)：交接格式、公开调用和身份边界。
- [第三方来源说明](THIRD_PARTY.md)：上游依赖及分发范围。
- [MIT 许可](LICENSE)：本项目代码与维护内容的许可。

PaperSpine 是独立维护的可选上游项目，本仓库不重新分发其管理产品。外部 `simulation-agent-mvp` 的程序没有包含或修改，仍遵守其原有运行限制。维护者可使用 `scripts/publish.ps1` 发布已审阅提交；普通使用者无需 GitHub CLI 或仓库写入权限。
