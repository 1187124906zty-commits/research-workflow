# ResearchFlow 依赖与兼容说明

本文说明 v0.1.0 的安装条件、实际接口范围与已检查环境。项目采用能力与接口条件描述兼容性：能够安装 Python 包、能够发现 skill、能够派遣子智能体，以及能够连接外部产品是不同层次。

## 1. 依赖分层

| 层次 | 必需依赖 | 当前实现与限制 |
| --- | --- | --- |
| Python 状态运行时 | Python `>=3.11` | `pyproject.toml` 的 `dependencies=[]`；运行时、CLI、基础检查与确定性示例使用标准库 |
| Python 构建与安装 | `setuptools>=68`，安装时通常使用 `pip` | `setuptools.build_meta` 是构建后端；无运行时第三方依赖不意味着源码构建完全不需要下载构建工具 |
| Codex 集成 | 可发现 `AGENTS.md` 和本地 skill 的 Codex | 自动入口加载与 skill 选择属于宿主能力；指令层不构成不可绕过的程序边界 |
| 多智能体执行 | 宿主提供 subagent 派遣、回传与可用模型账户 | 本项目不包含模型、模型服务 SDK、独立 API 客户端或账户凭据 |
| 自定义角色 | 宿主支持独立 agent TOML 文件 | 不支持此发现方式时，可在受支持的 subagent 调用中明确传入同一职责与任务契约 |
| PaperSpine 文件导出 | 兼容的 ResearchFlow 状态文件与 Python 标准库 | 无需启动 PaperSpine Web 或调用后台；导出不能替代阅读原始证据 |
| PaperSpine 实时调用 | 单独安装的上游产品、有效 profile 与其 Python 环境 | 适配器调用上游公开 host；不安装、重新分发或修改上游管理产品 |
| 科研执行工具 | 由具体研究任务决定 | FEM、CFD、DEM、实验和统计软件的依赖、许可、硬件及数据均在项目中配置 |
| 源码获取与发布 | 获取源码时可使用 Git；发布时需要 GitHub CLI 与有效认证 | 发布脚本使用 PowerShell；普通运行不需要 `gh` 或 GitHub 写入权限 |

通过 `python -m pip install -e .` 安装的发行包名称是 `researchflow-governance`，导入模块及命令名称是 `researchflow`。包安装提供运行时；`scripts/install.py`、skills、角色模板和集成脚本来自完整仓库或发布源码包，不会仅凭包安装自动写入用户配置。

本包不要求单独的 API key。模型调用发生在 Codex 宿主；其账户资格、模型可用性、网络与权限仍需满足宿主要求。若具体研究另用第三方模型、数据库或软件服务，认证是该项目或服务的依赖。

## 2. Python 与操作系统范围

| 环境 | 已有检查 | 结论边界 |
| --- | --- | --- |
| Linux / Python 3.11 | GitHub Actions：可编辑安装、标准测试、确定性扩散示例 | 核心包与这些检查路径已运行；未验证任意 Linux 求解器或客户端 |
| Linux / Python 3.13 | 同上 | 同上 |
| Windows / Python 3.11 | GitHub Actions：可编辑安装、标准测试、确定性扩散示例 | 包及检查路径已运行；开发机另检查了安装器长路径处理 |
| Windows / Python 3.13 | 同上 | 同上 |
| Windows / Python 3.12.14 | Codex bundled Python：标准测试、独立检查、实际 CLI、安装及接口探针 | 开发机的完整验证解释器；不等于全部 Codex 用户环境 |
| macOS | 本项目尚未测试 | 标准库实现具有可移植基础，仍需安装、文件与宿主集成验证 |
| Python 3.14 | 开发机系统解释器曾发生 DLL/退出异常 | 不作为健康环境背书；包的 `>=3.11` 声明不能覆盖机器上的解释器缺陷 |
| Python 3.10 或更早 | 不在发行包要求范围内 | 整体工具应使用 Python 3.11 或更高，勿由单个脚本可启动推断整包支持 |

已发布 CI 记录与本地测试细节分别见[仓库 Actions](https://github.com/1187124906zty-commits/research-workflow/actions)和[验证记录](validation.md)。需要第三方求解器的真实项目不属于此标准库示例测试范围。

## 3. Codex 规则、skill 与角色发现

### 3.1 规则入口

Codex 官方说明在一次运行开始时读取指令链：全局 `AGENTS.override.md` 优先于 `AGENTS.md`，项目内从根目录到当前目录加载相应文件。默认合并长度上限为 32 KiB。ResearchFlow 安装器只维护 `researchflow:begin/end` 标记之间的短规则入口，并保留其他内容；遇到不完整或重复标记时拒绝修改。

当目标目录存在非空 `AGENTS.override.md` 时，安装器将治理区块写入该文件，以使入口位于实际优先文件中。完成安装后应新建 Codex 运行确认发现情况。指令发现并不保证模型在任意任务里必然选择某个 skill，关键科研任务可显式调用 `$research-workflow-governor`。

### 3.2 skill 布局

| 安装方式 | skill 位置 | 角色位置 | 规则位置 |
| --- | --- | --- | --- |
| 默认用户安装 | `<CODEX_HOME>/skills`，通常为 `~/.codex/skills` | `<CODEX_HOME>/agents` | `<CODEX_HOME>/AGENTS.md` 或生效的 override |
| `--skill-layout agents` 用户安装 | `<CODEX_HOME>` 的父目录下 `.agents/skills`，默认对应 `~/.agents/skills` | `<CODEX_HOME>/agents` | 同上 |
| `--project <existing-directory>` | `<project>/.agents/skills` | `<project>/.codex/agents` | `<project>/AGENTS.md` 或生效的 override |

当前官方文档描述 `.agents/skills` 作为本地用户和仓库 skill 的发现位置。默认 `.codex/skills` 是本项目开发时实际桌面环境使用的兼容布局；不能将其作为所有 Codex 版本的统一目录要求。若配置自定义 `CODEX_HOME`，`--skill-layout agents` 根据它的父目录计算位置，需核对该宿主实际采用的用户 skill 路径。

同名 skill 在不同可发现路径中不会自动合并。请选择适合当前宿主的一套安装范围与布局，避免同时在用户和项目位置保留两份同名版本。更新已有本项目文件需显式使用 `--update`；本地定制应先整理为可维护差异。

### 3.3 subagent 与角色 TOML

完整研究模式需要可调用的 subagent 能力。宿主是否提供该能力、可同时运行的数量及账户资格以实际客户端为准。项目不固定所有角色同时启动，也不配置特定模型。

五份 `rf_*.toml` 使用 `name`、`description`、`developer_instructions` 三个字段，用户范围位于 `~/.codex/agents`，项目范围位于 `.codex/agents`，与当前官方独立角色格式对应。文件未写入模型、权限或 sandbox 覆盖，采用父任务设置。

开发时核对的 Codex CLI 版本为 **0.159.0**。角色 TOML 解析与官方格式核对已经完成；实际工作曾通过 collaboration 派遣职责契约。该事实不表示全部桌面、CLI 或 IDE 版本都已实测自动发现这些角色。对于角色发现差异，应使用显式委派并记录宿主限制；没有 subagent 能力时仍可使用 CLI 状态工具，但不能把串行单智能体执行称为已完成多智能体验证。

本项目不是插件目录分发包，也不据本地 skill 安装推断 ChatGPT 网页或其他第三方 agent 平台兼容。迁移需要实现相应宿主的发现、派遣、文件与状态接口。

## 4. PaperSpine 兼容边界

[PaperSpine](https://github.com/WUBING2023/PaperSpine) 是可选、单独安装和更新的 MIT 上游产品。本仓库包含原创交接与诊断代码，不 vendor 上游产品，不更改其 managed 文件。

| 接入能力 | v0.1.0 范围 | 所需条件与边界 |
| --- | --- | --- |
| 科研到写作文件交接 | 导出相关 claim、任务、版本、证据层级与研究理解 | 以 ResearchFlow state 为来源；不创建 backend task，不表示用户点击或证据已读 |
| 只读诊断 | 安装指针、profile、真实 host schema 与 Web 状态 | 优先使用上游现有 bundled Python；可通过 `--python` 或 `PAPERSPINE5_PYTHON` 指定解释器 |
| public-host 传输 | 白名单中的任务创建/读取、事件读取、证据绑定、artifact 发布与 milestone 提交 | 回读实际 schema，保持明确 task/profile 绑定；未授权伪造配置确认或 reviewer 身份 |
| 已核验上游版本 | **0.4.0-alpha.3**，public request schema **1.1** | 隔离 profile 实测启动、open/get、证据绑定和回读；不承诺其他版本稳定兼容 |
| 默认开发机 profile | 存在 profile 与产品安装 root 的祖先路径冲突 | 上游返回 `Keep the local profile separate from installed product files`；隔离探针不代表原 profile 修复 |
| evidence locator | 所测版本的 task projection 未回读传入 locator | ResearchFlow 原状态保留证据路径、版本与作用范围；不能只依据上游页面引用证据 |

PaperSpine 更新后应重新建立 host client 并读取当前 schema。命令传输成功与科学支持成立分别判断；未进行真实写作、独立审稿或投稿的接口探针不能证明这些流程完成。完整细节见[接入说明](paperspine-integration.md)。

## 5. 模拟、实验与其他外部工具

仓库提供优化后的 `simulation-project-orchestrator` skill、专业参考、schema 与科学对话脚本。它组织任务、输入、结果与验证，不包含商业求解器、所有 Python 科学计算库或统一软件连接器。

真实项目需要逐一核对：

- 软件/API 版本、输入格式、材料与边界条件、输出中可供验证的关注量。
- 求解器安装、许可、资源限制及自动化入口；实验的设备、数据质量和采集条件。
- 能否将运行绑定到已登记任务，以及如何回传日志、结果、失败与证据版本。
- 与研究论断相适应的基准、对照、数值核验和物理验证。

FEM、CFD、DEM、PINN 等属于 skill 的方法范围，不是已逐软件测试的兼容列表。本仓库没有拦截任意求解器调用；更强的执行约束需要具体工具适配器在调用前后使用契约与审计入口。

外部 `simulation-agent-mvp` 未包含或修改。如果该原型要求所有治理条目 PASS，仍须遵守其真实程序行为；本框架的逐论断治理规则不会自动改变外部实现。

## 6. 数据、权限与发布工具

共享状态由协调者串行记录，工作智能体写独立输出。运行时的 actor 是协议身份，不是操作系统权限隔离；科研意义与未经报告的错误仍由负责角色判断。证据内容版本用于识别交接中变化的文件，不证明物理正确性。

`scripts/install.py` 不编辑 `config.toml`、模型设置或权限，不移动 PaperSpine 数据库，不读取或复制凭据。运行权限与外部提交授权遵循宿主和用户要求。

`scripts/publish.ps1` 需要 PowerShell、Git、GitHub CLI 与有效认证，面向维护者。它检查已审阅的干净工作区，再推送或创建仓库。科研项目数据、模型认证、浏览器会话与本地运行目录不应纳入工具发布。发布工具的依赖不属于研究运行时必需条件。

## 7. 官方接口依据

以下文档于 2026-10-01 核对；宿主更新后应重新核对其当前说明：

- [Codex：AGENTS.md 指令发现](https://developers.openai.com/codex/guides/agents-md)
- [Codex：skills 与本地发现位置](https://developers.openai.com/codex/skills)
- [Codex：subagents 与独立角色配置](https://developers.openai.com/codex/multi-agent)
- [PaperSpine 上游项目](https://github.com/WUBING2023/PaperSpine)

兼容性结论应同时写明软件版本、宿主能力、实际执行路径与尚未核验的边界，避免从一个入口可读或文件可解析推断完整科研流程已经支持。
