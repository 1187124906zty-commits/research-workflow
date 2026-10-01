# ResearchFlow 论文来源核对

核对日期：2026-10-01。范围是五篇指定论文的定点原文核对，服务于没有实证结果的方法/系统设计论文；不是系统综述，也不能用于证明“首次提出”。书目信息来自 arXiv 官方页、官方项目 README 及 ACM 向 Crossref 提交的元数据。原文方法核对使用指定版本的开放 HTML。

最需要守住的比较边界是：既有工作已经具有停止控制、角色专门化、结构化产物、记忆、结果反馈和局部重试限制。ResearchFlow 可以把研究问题、证据与论文论证共同治理，以及跨阶段的反证失效与协调者复核作为设计关注点；当前不能写成已验证的质量或效率收益。

## 推荐参考文献

[1] Yao S, Zhao J, Yu D, et al. ReAct: Synergizing Reasoning and Acting in Language Models. arXiv:2210.03629, 2022. https://doi.org/10.48550/arXiv.2210.03629.

[2] Wu Q, Bansal G, Zhang J, et al. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. arXiv:2308.08155, 2023. https://doi.org/10.48550/arXiv.2308.08155.

[3] Hong S, Zhuge M, Chen J, et al. MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. arXiv:2308.00352, 2023. https://doi.org/10.48550/arXiv.2308.00352.

[4] Lu C, Lu C, Lange R T, et al. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv:2408.06292, 2024. https://doi.org/10.48550/arXiv.2408.06292.

[5] Park J S, O'Brien J, Cai C J, et al. Generative Agents: Interactive Simulacra of Human Behavior. Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology, 2023: 1–22. https://doi.org/10.1145/3586183.3606763.

以上 [1]–[4] 的年份采用预印本初始年份，实际核对版本日期另列于下。若改用会议版本，必须同步作者名、作者顺序、年份、venue 与被核对版本。MetaGPT 尤其存在 arXiv 与官方 README 作者写法/顺序差异，不能拼接。

## [1] ReAct

**元数据与原文。** arXiv 初稿 2022；核对版本 v3（2023-03-10）。[官方摘要页](https://arxiv.org/abs/2210.03629)、[完整 HTML](https://arxiv.org/html/2210.03629v3)、[项目页](https://react-lm.github.io/)。摘要页 comments 称 v3 为 ICLR camera-ready，本次未成功读取 OpenReview 正式会议条目，推荐保留上面的预印本引用。

**核对位置。** §2；§3.2 “Combining Internal and External Knowledge”。§2 描述 thought–action–observation 的交织：外部观察用于下一步推理，思考用于分解目标、跟踪进度、处理异常、调整计划；知识推理任务密集交替，交互决策任务允许稀疏思考。§3.2 已通过步数限制和回退到 CoT-SC 控制失败轨迹。可用原文定位短语：*“thought-action-observation steps”*。

**可以支持。** 调研、行动、反馈与计划调整可以形成执行循环；外部获取的信息与模型判断应区别记录。

**与 ResearchFlow 的关系。** ResearchFlow 可以沿用类似的执行循环，但研究问题—证据—论文论证联动及反证复核是本稿提出的治理层设计。不能把 ReAct 称为毫无停止条件的无限循环。

**不能支持。** skills 渐进加载、跨 agent 一致性、科学证据正确性、长期科研方向控制，或 ResearchFlow 的性能提升。原论文问答、事实核验、游戏和网页任务的指标不能转写为本系统实证。

## [2] AutoGen

**元数据与原文。** arXiv 2023；核对 v2（2023-10-03）。[官方摘要页](https://arxiv.org/abs/2308.08155)、[完整 HTML](https://arxiv.org/html/2308.08155v2)、[官方 v0.2.35 README](https://raw.githubusercontent.com/microsoft/autogen/v0.2.35/README.md)。README 记载 ICLR 2024 LLM Agents Workshop 获奖；这不是 ICLR 主会证明。推荐引用 arXiv，不在本包断定其它会议发表状态。README 的 BibTeX 在标题尾部加入 “Framework”，本包标题遵循 arXiv 官方页。

**核对位置。** §2.1 Conversable Agents；§2.2 Conversation Programming。Agent 有角色与消息上下文，可组合 LLM、人工输入和工具。Conversation programming 同时编排计算与控制流；自然语言、Python 和二者转换都可控制工作流。自动回复在终止条件满足时结束，Python 可设置人工参与、工具逻辑与最大自动回复数。动态交互可通过自定义 reply、function calls 或 GroupChatManager 组织。原文控制边界短句：

> Python code can be used to specify the termination condition, human input mode, and tool execution logic

**可以支持。** 角色、能力、消息交互与停止规则可以成为程序对象；人工参与与自动运行能由同一基础设施组织。

**与 ResearchFlow 的关系。** AutoGen 的中心是可编程会话基础设施；ResearchFlow 的设计中心可表述为研究问题、证据与论文论证共同决定派发、提升和复核。仅凭所读原文不能断言 AutoGen 无法实现这样的治理层。

**不能支持。** “AutoGen 只聊天”“没有上下文/停止条件”等对照，以及任务契约必然提升效率、准确率或论文接收率。

## [3] MetaGPT

**元数据与原文。** arXiv 初稿 2023；核对 v7（2024-11-01）。[官方摘要页](https://arxiv.org/abs/2308.00352)、[完整 HTML](https://arxiv.org/html/2308.00352v7)、[官方 README](https://raw.githubusercontent.com/FoundationAgents/MetaGPT/main/README.md)。README Citation 列 ICLR 2024（The Twelfth International Conference on Learning Representations），并指向 [OpenReview 条目](https://openreview.net/forum?id=VtmBAGCN7o)，本次页面遇校验。README 写 Jonathan Chen，arXiv 写 Jiaqi Chen；Jinlin Wang/Ceyao Zhang 顺序亦不同。本包采取实际核对的 arXiv 作者表与预印本引用。

**核对位置。** §3.1–3.3。角色 profile 包含 goal/constraints，并初始化专属 context/skills；SOP 将 PRD、设计、分配、编码与测试用结构化产物连接。§3.2 给角色规定 schema/format，共享 message pool 和 publish-subscribe 按角色兴趣取相关信息，依赖满足后再行动。§3.3 用运行/测试反馈改代码，已有局部重试上限：

> This iterative testing process continues until the test is passed or a maximum of 3 retries is reached.

**可以支持。** 角色专门化、过程规范、结构化交接、依赖驱动协作、任务相关信息过滤和可执行反馈的设计背景。

**与 ResearchFlow 的关系。** 所核对 MetaGPT 以软件交付 SOP/产物为骨架。ResearchFlow 可以进一步把局部任务边界与研究理解的重审相连，并持续更新研究问题、证据与论文论证。这是研究判断层的设计定位，不能宣称角色契约、skills、结构化产物或有界重试是本稿首创。

**不能支持。** 软件工程 benchmark 证明科学真实性、研究贡献或 ResearchFlow 的效率；也不能把 MetaGPT 描述为无记忆、无执行反馈、纯聊天。

## [4] The AI Scientist

**元数据与原文。** arXiv 2024；核对 v3（2024-09-01）。[官方摘要页](https://arxiv.org/abs/2408.06292)、[完整 HTML](https://arxiv.org/html/2408.06292v3)、[官方 README](https://raw.githubusercontent.com/SakanaAI/AI-Scientist/main/README.md)。官方 README 建议引用 arXiv preprint；本包未核对正式会议或期刊版本。

**核对位置。** §3；§4；§8–9。§3 以实验/绘图/LaTeX 模板为起点，连接想法生成、实验迭代、论文写作与后续自动审阅。想法档案可接收既有想法和 review scores，文献检索筛相似想法。失败或超时最多四次修复重试；实验记日志、按结果重规划，实验迭代最多五次。写作使用 notes/figures，要求实际观察的结果和真实引用，并有编译反馈。

§8 明确承认错误实现、比较不公平、数值解释错误与幻觉结果；保存执行时的全部文件副本以支持复现。§9 把代码—实验绑定和独立复现列为未来可靠性方向。核心限定原句：

> one should manually check the implementation before trusting the reported results

**可以支持。** 科研想法、实验、图表、论文和审阅已能连接为自动流程；同时，自动执行/自动评分不能取代实现正确性、实验公平性和证据核验。

**与 ResearchFlow 的关系。** 应承认这篇已具备日志、限次迭代、实证写作约束与文件保存。ResearchFlow 的拟议区别是持续检查“结果回答何种问题、支撑何种论证、何种反证要求撤销并返回协调者”。这种机制目前只能作为设计贡献陈述。

**不能支持。** ResearchFlow 已提高研究质量、新颖性、效率或无需人工判断。原文的“低于15美元”不是跨领域通用全成本；自动 reviewer 超过 accept 阈值不等于真实会议/期刊录用。生成论文不可直接充当已确认科学发现。

## [5] Generative Agents

**元数据与原文。** arXiv v2（2023-08-06）；ACM 发表元数据确认 UIST '23、2023-10-29、1–22 页、DOI 10.1145/3586183.3606763。[官方摘要页](https://arxiv.org/abs/2304.03442)、[完整 HTML](https://arxiv.org/html/2304.03442v2)、[ACM 提交的 Crossref 元数据](https://api.crossref.org/works/10.1145/3586183.3606763)、[出版版 DOI](https://doi.org/10.1145/3586183.3606763)。Crossref 全名 Joseph O'Brien/Carrie Jun Cai 与 arXiv 首字母写法有差异；推荐简写引用相容。

**核对位置。** §4.1–4.3；§8.2。Memory stream 存观察与时间信息，按 recency/importance/relevance 检索上下文子集。Reflection 从检索记忆生成 insight，并保存指向引用 memory objects 的 pointers；计划也存入记忆，按粗到细分解，观察可触发后续重规划。§8.2 承认幻觉、memory hacking、稳健性与长期评估局限。可用短语：*“including pointers to the memory objects that were cited”*。

**可以支持。** 持久记忆、选择性检索、计划更新和推断到来源观察的引用关系都有相关先例。

**与 ResearchFlow 的关系。** 本文原方法的目标是社会行为可信度；把来源指针迁移为科学证据—论证绑定，以及用反证使绑定失效，是 ResearchFlow 的拟议设计。社会模拟结果不验证科学真实性或状态崩溃恢复语义。

**不能支持。** 经验记忆等于可信科学证据，选择性检索等于 skills 渐进加载，或者 25 agent 社会模拟说明 ResearchFlow 的多 agent 性能。

## 补充规范来源 [10]：PROV-DM

**元数据与原文。** Moreau L, Missier P, eds. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013。[官方规范](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)。正文设计审阅时核对 §2.1、§5.2.2 Revision、§5.3.4 Delegation，并区分 §5.1.8 Invalidation 的含义。

**可以支持。** 来源追溯可以使用 entity、activity、agent 与生成、使用、派生和责任关系组织；修订具有派生关系，委派不自动消除原责任主体的责任。

**使用边界。** 规范中的实体失效表示实体生命周期变化，不能直接等同于反证推翻科学论断。ResearchFlow 的论断支持、挑战与处置是本项目的科研应用协议。本文未实现或验证 PROV 格式兼容、序列化或互操作。

## 正文使用界限

| 拟写内容 | 适当依据或措辞 |
| --- | --- |
| 推理与工具行动交织 | [1] 的具体机制 |
| 多 agent 角色与交互可编排 | [2]；已有停止和人工控制 |
| SOP、结构化产物、依赖与角色相关信息流 | [3]；已有 skills/context 和限次调试 |
| 想法—实验—论文—审阅流水线及可靠性局限 | [4] |
| 持久记忆、选择性检索与来源指针 | [5] |
| 研究问题、证据与论文论证共同治理 | “本文提出/设计……”；属于本稿方案 |
| 契约、反证失效、协调者重审、状态恢复 | 描述实现属性与机制；效果待验证 |
| skills 的 metadata→正文→资源渐进加载 | 五篇论文没有直接依据；引用平台/skill 文档或本文实现 |
| 消除研究漂移、节省资源、提高论文质量 | 当前没有实证；不能陈述为已达成结果 |
| 首次/唯一/所有既有方法都缺少某机制 | 本次定点查阅不能支持 |

比较中的“尚未在所读机制中显式体现”须限定为本文核对范围；不要升级成“该框架无法实现”。代码/运行时能够核对过程和绑定，也不等于其已判断科学真伪。

## 检索限制与出处记录

五篇官方 arXiv 摘要页和所列 HTML 均已实际取得。长 HTML 工具输出尾部截断，但上列正文位置均包含于取得内容；没有以摘要替代三篇核心方法的正文核对。OpenReview 页面返回浏览器校验，公开 notes API 返回 403；未绕过验证。微软研究的旧 publication 路径返回一般首页，未作为元数据来源。开放 arXiv 正文已足够，因此没有启用认证出版商会话或调用任何模型 API。

对应机器可读对象见同目录 `source-notes.json`。全文事实、设计迁移与效果限制分别列出；这些来源不构成 ResearchFlow 的实验评估。
