---
name: simulation-tool-execution
description: Run a specified simulation through an available MCP solver or compatible runtime when its physics, conditions and outputs are defined. Generate native inputs when needed; use for prepared execution, not literature acquisition or result validation.
---

# Simulation Tool Execution

把已闭合的工况与模型映射到真实工具并运行。接收 `simulation-task.md`、`evidence/model-plan.md` 或等价现有定义；上游不必提供现成命令，由执行者生成必要原生输入。只回答“是否按指定工况执行并留下可用输出”，不宣称实验验证或机制成立。

## 接口

开始前读取目标与工况、关注的观测量（quantity of interest, QoI）、指定软件或允许替代、输出字段及采样、预算、已准备命令，以及模型映射、参数/单位、初始/边界/接口条件和验证观测定义。缺件只阻断受影响运行或字段；具名返回上游责任方。不要自行补物理、改数据角色、调参拟合或把小试验替代目标规模。

输出包含：

- `runs/<run-id>/`：实际输入快照或修订标识、原生命令/请求、stdout/stderr、退出或拒绝状态、原始结果；
- `run-manifest`：工具/handler、solver、runtime 与版本，工作目录，参数和环境要点，起止时间，工况/种子/父子运行，输出清单；
- `results-index`：每个字段的含义、单位、坐标系、point/cell/积分等 association、时间/载荷覆盖、路径、转换和缺失后果；
- 返回状态 `EXECUTED | PARTIAL | FAILED`，并列出完成工况、失败尝试、未满足项和证据路径。

## 执行

1. 发现本机实际可调用的 MCP 工具；探测 handler、solver、runtime 和相关文档能力。不得从名称、适配器或旧记录推断可用。需选工具或 MCP 不可用时读 [references/tool-selection.md](references/tool-selection.md)。
2. 对照上游任务定义检查单位、初始/边界/接口映射、输出字段与时空覆盖；只修复执行映射或环境问题。新推导、新算法或改变物理必须退回具名上游。
3. 首次工具/接口不确定时用廉价探针确认能力；已有可信命令可直接执行。按指定规模和工况批量运行，固定物理条件；需要时先保存 checkpoint/原生输出。捕获拒绝、非零退出和失败日志，不做假调用。
4. 先落盘原始证据和 manifest，再转换。已有 raw 足够时仅重处理；只有关键字段未导出才重跑。检查可读性、有限值、单位/association/坐标/时间覆盖和工况对应。
5. 数值细化只在 QoI 或物理可信度确有需要且理由明确时做有限检查；不机械规定网格层数、误差阈值或通用收敛流程。

遇错读 [references/failure-recovery.md](references/failure-recovery.md)。两轮修复若症状和研究判断均未变化，停止重复尝试，保留失败链并返回仿真协调者。

## 状态含义

- `EXECUTED`：所有指定工况成功结束，所需原始输出和记录齐全；仅证明已执行。
- `PARTIAL`：至少一项有效运行或可复用 raw 已取得，但有工况、字段或记录缺失。
- `FAILED`：没有可支持任务目标的有效运行；仍须返回探针、日志、失败原因和最小解除条件。

零退出码、MCP 握手或有限值不能单独提升状态。失败也是证据，不得静默换后端或偷偷调参改成“成功”。
