---
name: simulation-project-orchestrator
description: Route an upstream simulation request through source-based preparation, solver-tool execution and experimental or theoretical comparison. Use for an end-to-end simulation job or coordination of these stages; use the stage skill directly for a prepared execution or validation task.
---

# 仿真任务入口

接收上游研究目标或具体模拟命令，交付指定工况的实际计算、验证对比与可复用结果。研究动机、文献检索/下载、机制假设和额外探索由上游负责；本入口协调仿真工作，不重新开展研究项目。

## 接单与路由

先读上游材料和当前结果索引。把目标、工况、可观测量、已有文献/数据、软件约束、所需输出和预算写入或接续一份 `simulation-task.md`；简单任务几段即可。信息不足时先查已交付资料，向上游提出会改变本次计算的具体资源请求；实验数据缺失只影响相关验证，物理闭合缺失影响相应工况。

| 当前工作 | 交给谁 | 返回后做什么 |
|---|---|---|
| 从已交付文献/数据提取参数、验证数据并确定模型路径 | [simulation-evidence-preparation](../simulation-evidence-preparation/SKILL.md) | 接收可执行工况、模型/观测定义和缺件请求；必要文献请求交上游资源角色 |
| 已有条件/模型或具体命令，需要选工具并计算 | [simulation-tool-execution](../simulation-tool-execution/SKILL.md) | 检查实际运行与原始输出，再交验证角色；已完成任务不重新准备 |
| 已有结果，需要实验/理论对照或偏差诊断 | [simulation-result-validation](../simulation-result-validation/SKILL.md) | 接收结论适用范围、工况比较、未决项和具名修复请求 |

职责 Skill 不会自行启动。需要独立分工时，主代理用宿主的子代理工具派发，**每个子代理只给其职责 Skill 路径、相关原件、任务/输出路径和返回条件**，不让每人读取入口、全套参考或研究历史。小任务可以合并职责；重要结果的验证交独立执行者。模型使用上游允许池，不以模型名或多数意见决定事实。

MCP 和成熟求解工具承担计算；可用性由执行角色实测。工具不足时允许授权的 CLI、Python 或 WSL 途径，并如实记录；数值实现深挖只在会影响本次结果可信度时开展。工况/参数探索按上游命令执行，新的物理模型、校准或研究问题交回上游。

## 接收反馈并完成

异常由发现者先核对本职，再把定位、已查事项、待回答问题和受影响工况发给负责角色。请求方评价答复、实施可行修复、复测原异常；部分答复保留未决项。两次有界尝试未改变症状或判断时，协调者重新选择下一步并说明理由，不直接判通过或弃置。只重做失效部分。

任务交接、缺件与恢复读 [handoff.md](references/handoff.md)；只有重要争议需要持久对话账本时读 [dialogue.md](references/dialogue.md)。已有 ResearchFlow 时复用其任务状态；无该包用当前任务记录，不另建多套状态系统。

完成意味着：上游要求的可执行工况已处理，实际输出与比较可定位，未完成工况和验证范围已说明，重要反馈已有请求方处置。返回一份结果索引、验证报告及必要资源/修复请求。程序完成、理论核验、实验对比和限定用途的验证分别陈述；研究机制解释交由上游使用这些结果。
