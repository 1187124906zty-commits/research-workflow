# Evidence-preserving multi-agent governance

Use for substantive simulation collaboration when delegation is available and authorized. Govern the research question, evidence dependencies and return conditions. More agents or records do not establish better science.

## Minimum useful assignment

Each task states question and purpose, stage, claim/COU, incoming evidence and versions, responsibility and decision rights, outputs owed, adequacy rationale, budget, return condition, and what the role cannot alter. Read only the context needed for that task. A short run plan may carry these fields; a full collaboration bundle is not an ordinary-task prerequisite.

Use the current configured model unless the user or applicable project policy selects another. Record the actual model only when the dispatcher exposes it; say unknown otherwise. Do not fabricate model identity or demand a model fault-injection suite before using the available agent. Respect explicit model allow/deny lists. Deterministic tools perform fixed checks; an agent interprets scientific meaning and anomalies. Model benchmarking is appropriate when evaluating a routing policy itself, not as a new universal scientific gate.

## Responsibilities

Roles are responsibilities, not necessarily seven simultaneous agents:

- **Coordinator/planner** owns evolving question, paper argument, dependencies, budgets, priorities and dispatch. It can select the next investigation and revise scope but cannot rewrite evidence or factual failures.
- **Domain scientist** owns equations, closure, units, assumptions, validity domain and physical limits.
- **Engineer/executor** maps the model to software, executes versioned candidates, reports numerical adequacy and returns raw outputs and cost.
- **Experimentalist/literature role** owns source reconstruction, data roles, measurement operators, replication and experimental uncertainty.
- **Mechanism analyst** asks discriminating questions, specifies useful fields and contrasts, and evaluates the returned evidence against predictions and alternatives.
- **Independent reviewer** examines consequential claims for counterexamples, missed obligations and unsupported scope.

Combine compatible responsibilities for cheap exploration, with explicit self-review disclosure. Use an independent first pass for consequential paper claims. If collaboration or separation is unavailable, report DEGRADED_INDEPENDENCE and its affected claims; do not present a second self-prompt as an independent reviewer. Spawn only roles that improve a current decision, and respect the active slot limit.

## Handoff and dialogue

Return claim, scope, versioned evidence paths, observations, uncertainty, checks performed, unresolved obligations, cost spent, and recommended next decision. The requester owns disposition; an executor's completed task does not prove a mechanism or validate a hypothesis.

For consequential cross-role requests, use [scientific-dialogue.md](scientific-dialogue.md): REQUEST -> EVIDENCE RESPONSE -> REQUESTER DISPOSITION. State the triggering artifact/metric, relevant self-checks already done, competing explanations, bounded question, requested evidence, affected claims and response milestone. Do not perform every conceivable check before asking a useful source question; check those that could explain the actual anomaly.

A responder returns primary evidence or a bounded new calculation, a documented inability to answer, or a counter-question. Numerical roles retain responsibility for numerics and experiment roles retain responsibility for observations. An experimental value cannot change merely to improve agreement.

Use the locked append helper for a shared JSONL ledger. Never overwrite another agent's messages. Before promoting an affected claim, use scripts/audit_scientific_dialogue.py to expose open requests, missing requester dispositions or structural defects. Its aggregate claim_promotion_status applies to the audited ledger; map open threads to named claims rather than treating an unrelated open request as a project-wide halt. The script checks structure, not scientific truth.

The mechanism analyst states predicted contrasts, controls, required fields, falsifiers and cost before a requested run. After return, it evaluates every predeclared explanation against actual effects, numerical/measurement uncertainty and repeatability; then it closes, narrows, or asks one next question. NO_ADDITIONAL_RUN_JUSTIFIED may preserve an ambiguity with evidence and a reason. Not every unresolved detail warrants another simulation.

## Independence and evidence binding

Before reading the producer's persuasive explanation, a reviewer records its first pass from the actual question, input/run version and raw evidence. Preserve the first pass and later revisions, and disclose what context was visible. Declared independence is useful but does not imply runtime attestation or statistical independence.

Version IDs and located artifacts provide ordinary exploratory binding. Content digests are needed when an adapter demands immutable identity, concurrent edits could affect inspection, binaries need provenance, or caching relies on content. A pre-run binding cannot prove review of post-run outputs. Review output claims against the actual run and relevant metrics/checks, with content binding when required.

An upstream change makes only dependent opinions and results stale. Reuse an unchanged review when all its inspected dependencies and scope still match. Do not reread an unchanged literature set or repeat a solver check merely because another role is now writing.

## Claim-scoped failures and disagreement

A stop-line must name the claim, failed obligation, evidence, and a discriminating observation or correction that could resolve it. An unsupported demand for maximum precision or exact literature matching is not a veto. Pause the affected promotion and dependent high-cost work; independent work and bounded diagnostics may proceed.

Preserve the original failure and dissent. Resolve through new located evidence, corrected artifacts with affected checks rerun, a discriminating test, or strict reduction of scope. Scientific recovery of a disputed consequential claim needs independent review. The producer cannot self-clear an independent reviewer by changing a status string.

Scope reduction explicitly retires the broader claim and lists the surviving narrower claim and its evidence. It does not turn conservation failure, equation mismatch, leaked validation data, or fabricated evidence into a same-scope limitation. The coordinator can retire a claim; an independent reviewer checks disputed manuscript consequences rather than granting blanket permission.

Never decide truth by vote, model rank, role seniority, confidence average or consensus. An unresolved scientific failure blocks only its claims/dependencies. Noncritical WARN records remain visible; they do not universally prevent research progress or supported manuscript claims. A human risk owner can accept named residual uncertainty but cannot convert a factual failed check to PASS.

## Review and effort

Use cheap applicable checks before an expensive solve; review changed equations, conditions, data roles and software mapping when their dependencies change; review actual outputs and numerical adequacy before strong numerical claims; review data alignment, uncertainty and scope before physical validation; review mechanisms and counterevidence before asserting them.

After two consecutive repair/refinement rounds without changed research judgment, or earlier budget exhaustion, return to the coordinator under [research-efficiency.md](research-efficiency.md). The next cycle needs a new bounded information-gain rationale, not a longer debate or another decimal place.

## Strict adapter compatibility

Existing [collaboration-bundle.schema.json](collaboration-bundle.schema.json), [agent-assignment.schema.json](agent-assignment.schema.json), [agent-opinion.schema.json](agent-opinion.schema.json), and [dissent-record.schema.json](dissent-record.schema.json) remain available for integrations that require their detailed fields. Do not silently label a compact record as conforming to these strict schemas.

The legacy local MVP has its own GOV_* gates, actual-model and model-adequacy requirements, content-bound post-run review subject, runtime assurance and all-PASS promotion policy. Read [local-mvp.md](local-mvp.md). Its missing/WARN/FAIL/BLOCKED bundle keeps its governed cap at EXECUTED. This skill revision does not modify that executable behavior. General research-stage policy cannot bypass it, and strict adapter policy is not automatically imposed on every ordinary simulation task.

A separate workflow may assess independently acquired evidence under its declared research contract while preserving the MVP's original gate states and limitations. Governance PASS is process evidence, not physics evidence, and never raises a scientific claim by itself.
