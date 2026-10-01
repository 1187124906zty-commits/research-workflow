# PaperSpine 接入：写作判断与真实产品状态分别验证

本项目把 [PaperSpine](https://github.com/WUBING2023/PaperSpine) 用作科研与写作角色依赖，保持其 managed 安装不变。独立的 stdlib 适配器负责文件交接、真实 public-host 调用及诊断，不复制上游产品，不把 Web 启动当作 agent 启动。

PaperSpine 应在选题阶段参与：学习候选期刊的读者、主题、贡献类型及论证顺序，把研究问题整理为可被证据检验的论断；结果返回后再改写框架、机制讨论和正文。期刊习惯帮助读者理解结果，不能决定结果是什么。

## 在研究循环中怎么用

1. 协调者先将研究理解、任务目的、claim 边界和已有证据写入本项目唯一的 `.researchflow/research-state.json`。文献和初步试验可以改变问题，不必先锁死完整论文结论。
2. 向 PaperSpine 角色发有范围的任务：例如“依据 C1/C2 和候选期刊读者，提出两种论证结构，标出需要哪个可辨别结果”，或“将已经接受的结果写成 Results/Discussion，保留反例与适用范围”。任务写清输入、交付、预算和返回条件。
3. 导出此任务的交接包。执行角色或 PaperSpine 可以读取实际资料，但不能把导出记录当作已阅读文件，也不能把任务 `accepted` 当成假设已获支持。
4. PaperSpine 将证据缺口返回协调者：哪个论断需要辨别、现有证据在哪里、一个最小可行任务是什么、如何使用输出、预算和返回条件。协调者决定继续计算、用更便宜的试验区分、收窄论断或先推进另一项工作。
5. 有实际结果后，PaperSpine 回读 claim 的支持、挑战和局限，写完整论证；另一独立 agent/context 审阅真实当前稿件、参考文献、图及渲染。审稿者检查科学问题，不能只看文件存在或后台状态。

以上步骤围绕真实问题循环；不是每个 claim 固定跑一遍所有软件、所有审查或所有期刊模板。

## 文件交接，不依赖 Web 可用性

从本仓库根目录运行，使用工作的 Python 3.11+（与本项目发行包要求一致）：

```powershell
python integrations/paperspine/adapter.py export `
  --project "D:/research/my-study" `
  --research-task "T-writing" `
  --output "D:/research/my-study/handoffs/T-writing"
```

`--research-task` 对应 research state 中已有的任务 ID。也可使用重复的 `--claim C1 --claim C2` 指定讨论范围；没有指定时导出全部 claim。该命令生成 `handoff.json` 和中文交接说明，不创建 PaperSpine backend task，不发送资料，不启动科研执行。

交接包包含：

- 原始状态文件路径、项目事务 revision、当前问题、目标期刊及研究理解。
- 被选中的 claim 原始记录及其 observation、numerical_verification、physical_validation 支持层级、挑战与局限；语义保持不变。
- 涉及这些 claim 的任务合同、状态、最近一次返回与决策。历史保留在原始 state 中，需要时针对性读取。
- 清楚的事实边界：agent 导出不等于用户 Web 确认；接受交接不等于支持假设；审稿需真实独立上下文。

该格式用于本项目科研状态的交接，不是 PaperSpine public API 请求体。不要直接把 `handoff.json` 填进上游 API，也不要建另一份可以悄悄改写论断的状态库。若工作中 state revision 改变，回读受影响 claim 和任务后重新导出。

## 实际 CLI 与 profile 检查

```powershell
python integrations/paperspine/adapter.py doctor `
  --skill-root "$env:USERPROFILE/.codex/skills/paper-spine" `
  --profile-root "$env:USERPROFILE/.paperspine5/profiles/default"
```

`doctor` 只读检查安装指针、绑定文件、真实 `paperspine_open_task` schema 及 Web status。它把 `host_schema_verified` 和 `web_start_verified` 分开，诊断命令完成不等于产品可执行论文。优先使用安装指针指向产品内的现有 bundled Python；可通过 `--python` 或 `PAPERSPINE5_PYTHON` 明确指定已有解释器。

本机默认 profile 的启动问题已定位：产品安装在 profile 的 `.paperspine5-lifecycle/installs/...` 内，而上游 `web_launch` 拒绝 profile 与产品 root 存在祖先关系，返回 `Keep the local profile separate from installed product files`。本适配器检测并报告这项冲突，没有改 managed 代码、移动数据库或选择另一个 profile 来冒充修复。当前该 profile 的 host schema 可读取，Web 启动问题仍需上游修正；文件级科研交接可以继续。

## 明确绑定的 public-host 调用

适配器允许以下真实工具：`paperspine_open_task`、`paperspine_get_task`、`paperspine_list_task_events`、`paperspine_bind_evidence`、`paperspine_publish_artifact`、`paperspine_commit_milestone`。它在当前实例缓存实际 schema，保持请求原样，调用失败或版本冲突立即返回错误，不自动重试、替换任务或补造科学事实。

```powershell
python integrations/paperspine/adapter.py schema `
  --skill-root "$env:USERPROFILE/.codex/skills/paper-spine" `
  --profile-root "<同一已有profile>" --tool paperspine_get_task

python integrations/paperspine/adapter.py call `
  --skill-root "$env:USERPROFILE/.codex/skills/paper-spine" `
  --profile-root "<同一已有profile>" --task-id "<明确任务ID>" `
  --tool paperspine_get_task --arguments "get-task.json"
```

`get-task.json` 可为 `{}`；上游通过显式 `--task-id` 绑定。修改类请求必须依据真实 schema 使用 `request` wrapper、实际 `task_version`、稳定的 `command_id` 及 payload。版本冲突后读取同一任务当前事实再判断，而不是对不同输入重放旧决策。创建产品任务只用于确实没有 backend task 的同一论文或明确的新测试，不能用于绕过启动或传输失败。

上游 public 1.1 evidence 绑定的 payload 包含 `claim_id`、`evidence_id`、`relation`，以及可选 `locator`。`supports`、`limits`、`challenges` 和 `visualizes` 的含义不同；模型不能为使页面进入下一阶段随便选择 `supports`。本机版本 `0.4.0-alpha.3` 的 task projection 回读时仅保留前三字段，未保留 `locator`。因此本项目 state 的实际路径、版本、证据层级、理由和反例仍是写作使用证据的依据。绑定关系成功是元数据持久化验证，不是来源已读、数值正确或结论成立的证明。

## 自动选择与真实身份边界

用户明确授权自动研究、选择方向和默认期刊时，可以在授权范围内做这些科研决定，并在研究 state 中保留理由和来源。上游 SKILL 的纯提示性人工选择要求不能制造重复审批；上游 backend 若仍要求真实 Web 确认，就报告这个实现限制或保持文件级交接，不伪造 `source=web_user`、`user_confirmed=true`、用户点击或保存记录。

适配器故意不开放保存配置、替用户解答 decision 或 `paperspine_submit_review`。后者需要实际独立 reviewer 的现有 runtime identity，作者不能打开 `--trusted-reviewer-id` 为自己签名。真实审稿者可依据上游当时 schema 直接使用它的公开独立审阅入口。配置、审阅、页面下载及投稿是否完成应各自依据真实操作判断。

开展实际论文生产前，负责该角色的 agent 按安装的 PaperSpine SKILL 执行一次更新 preflight，并按当前科研任务选读原始方法。安装更新后重新创建 `HostClient`、读取新 schema；本适配器不修改管理安装，不替它实现自动更新机制。

## 2026-10-01 的验证结果与适用范围

独立临时 profile 的实际探针执行了以下过程：隐藏 loopback Web `launch --no-open` → synthetic task `open` →同一 task `get` →将真实生成的 synthetic CSV 的引用绑定为 `limits` →再次 `get` 确认关系→停止该测试拥有的 Web 进程并清理临时目录。没有打开浏览器或接触真实用户任务。使用安装的 `0.4.0-alpha.3`，public request schema 为 `1.1`。

结果保存在 [`live-probe-20261001.json`](../integrations/paperspine/live-probe-20261001.json)。Web 启动、task open/get 和 evidence binding 回读均通过；`locator` 未回读。该探针只是传输与身份绑定测试，没有真实科研结论、Web 配置确认、论文生产、独立审稿或投稿验证。默认 profile 的启动冲突也未由隔离测试解决。

可明确运行一次新的隔离探针：

```powershell
python integrations/paperspine/live_probe.py `
  --skill-root "$env:USERPROFILE/.codex/skills/paper-spine" `
  --report "<本地探针结果.json>"
```

该命令会创建新的临时测试 profile；不把它当作原论文的恢复方式。10 个单元边界测试覆盖否定证据保持、层级保持、任务范围压缩、源状态不变、未知 schema、task mismatch、伪造用户/reviewer 身份、非零传输退出及成功封装中的 domain error。使用 Codex bundled Python 3.12 执行退出码为 0。本机系统 Python 3.14 在 unittest 显示 OK 后发生解释器退出 access violation，正式验证选用工作的 bundled runtime。

本项目适配器代码由本项目许可覆盖；上游 PaperSpine 是独立的 MIT 项目。仅引用其能力和公开依赖，不将上游后台状态当作科学质量或发表保证。
