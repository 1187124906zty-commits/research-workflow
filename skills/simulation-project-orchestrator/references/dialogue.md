# 重要反馈的可选账本

只有需要跨角色持久记录的重要争议才使用本协议。普通请求/回复/请求方处置可写在任务交付中，不要求每个计算都建账本。主代理或负责记录者执行脚本，子角色无需加载 schema/脚本全文。

账本是追加的 `scientific-dialogue.jsonl`。单条消息按 [schema](scientific-dialogue-message.schema.json) 准备，再调用：

```text
python scripts/append_scientific_dialogue.py --ledger LEDGER --schema references/scientific-dialogue-message.schema.json --message MESSAGE.json
python scripts/audit_scientific_dialogue.py --ledger LEDGER --schema references/scientific-dialogue-message.schema.json --fail-open-obligations
```

以上路径相对本 Skill 目录，调用时先定位真实目录/解释器。追加助手持锁并共用审计验证；消息不得通过重写账本追加。

每个请求含异常定位、本职核查、具体问题、替代原因、所需动作、责任接收方、工况/候选与受影响结论。请求 → 每名责任接收方的有证据答复 → 请求方对每条答复的一次处置。同线程保留原 claim/Gate 集合。`PARTIAL`/`UNRESOLVED` 需要继续请求或显式限制，不允许成功关闭。缩窄问题先限制原结论，再开关联的新线程。

新反证可由原请求方在关闭后追加 `COUNTER_QUESTION`，其前驱和 `reopens_closure_id` 均指向原关闭；新答复/处置前原关闭不能清除阻断。模型/候选改变则建立新线程关联原决定。

审计输出缺失回应、缺失处置与未决 stop-line，只影响有关结论。`DIALOGUE_COMPLETE` 包括限制性处置，不证明数据真伪、数值适当或实验有效性。记录外部脚本版本，CLI 不自行保证版本身份。

新规则可能拒绝旧账本的缺字段、义务变化、重复关闭或矛盾状态，追加也可能因此失败。保留历史文件，在明确关联原义务的后续记录中继续；不改旧记录制造通过。账本不重复计数尝试，计数仍归当前任务/ResearchFlow。
