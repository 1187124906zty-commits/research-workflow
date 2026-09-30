# Cross-role scientific dialogue

Use this protocol for a consequential anomaly, ambiguity, missing obligation, simulation--experiment residual, or mechanism question requiring another role's evidence. Routine clarification may use the task handoff without a separate ledger event. The goal is an auditable feedback loop, not free-form debate or automatic parameter tuning.

## Message contract

Store messages append-only in `scientific-dialogue.jsonl`, following [scientific-dialogue-message.schema.json](scientific-dialogue-message.schema.json). When this Skill's scripts are available, append each prepared message with `scripts/append_scientific_dialogue.py`; do not create, replace, truncate, sort, or rewrite an existing ledger directly. The helper validates the schema, serializes concurrent writers with a lock, rejects duplicate IDs and checks predecessor links while holding the lock. If the helper is unavailable, use an equivalent atomic append and disclose degraded ledger assurance. Each request contains:

- immutable message/thread ID, predecessor, timestamp, sender/receiver roles and candidate/run binding;
- `trigger`: the exact field, residual, plot, table row, log entry, Gate or source conflict that raised the issue;
- `self_audit`: checks the sender completed inside its own responsibility and their evidence locators;
- `question`: one answerable scientific or implementation question;
- `competing_explanations`: alternatives that the requested evidence can distinguish;
- `requested_evidence_or_action`: source locator, raw-data audit, deterministic calculation, corrected candidate, or controlled run;
- affected claims/Gates, urgency, response condition and stop-line status;
- calibration/validation data-role consequence.

A response cites the request, provides located evidence or run artifacts, answers fully/partially/not resolved, states what changed, and may pose a bounded counter-question. Never replace the original request or earlier response.

## Executable thread lifecycle

Treat each `thread_id` as a scientific obligation, not a chat topic:

```text
QUESTION or RUN_REQUEST
-> RESPONSE or RUN_RESPONSE
-> requester evaluation
-> CLOSURE, COUNTER_QUESTION, or narrower RUN_REQUEST
```

The receiver named by the request is accountable for a response before the request's `response_condition` milestone. The response returns evidence and its own self-audit; it does not merely acknowledge the task. The original requester then owns the disposition. For a mechanism run, the executor cannot declare the mechanism supported, and the analyst cannot ignore failed numerical checks in the returned run.

Before promoting an affected claim, run `scripts/audit_scientific_dialogue.py`. It checks unique IDs, predecessor order, same-thread/project/candidate binding, reciprocal sender/receiver linkage, legal message transitions, unanswered requests, missing requester dispositions and unresolved stop-lines. Use `--fail-open-obligations` when the target milestone requires all audited threads resolved. Its aggregate status applies to the audited ledger; map open thread IDs to their affected claims, or audit a separate claim-scoped ledger. An unrelated thread does not globally block all research. This audit cannot judge evidence quality or clear any Gate.

If a requested role cannot answer, it still responds `UNRESOLVED` with the sources searched, missing evidence, the narrowest answerable sub-question and claim consequence. If the question was routed to the wrong role, that role answers with a bounded reroute request; the original message remains in the ledger.

If any writer overwrites or loses prior messages, stop claim promotion, preserve the surviving file, reconstruct missing events into a separate explicitly labeled record from source messages/artifacts, and record `DEGRADED_LEDGER_ASSURANCE`. Do not insert reconstructed events into the runtime-attested sequence as though they had always been present.

## Residual escalation loop

When an experimental residual is surprising:

1. **Numerical/implementation self-audit** — inspect relevant specification/candidate binding, equations/units, material/source/condition mapping, termination, balances, numerical adequacy and observation extraction. Reuse unchanged evidence; rerun only checks implicated by this anomaly. Do not refine indefinitely before asking a source question.
2. **Experimental evidence query** — ask a bounded question about unresolved experiment-side causes: condition identity, specimen/batch, raw records, replicate hierarchy, processing, instrumentation, coordinates, uncertainty or source conflicts. State remaining numerical uncertainty. Numerical and source checks can proceed in parallel when they are independent; physical attribution still waits for adequate credibility evidence.
3. **Experiment-role response** — locate the answer in primary sources/data, reproduce summaries when possible, report anomalies without deleting them, distinguish independent specimens from repeated readings, and state whether the Validation Contract changes. It may not select a processing rule because it improves agreement.
4. **Numerical requester disposition** — the numerical role that asked the experimental question must compare the answer with its own self-audit, record `ANSWERED`, `PARTIAL`, or `UNRESOLVED`, identify any invalidated numerical or observation-operator checks, and either close, counter-question, or narrow the request. A response alone does not authorize physical attribution. Preserve source conflicts and the residual's data-role consequence.
5. **Physics/model query** — once numerical and experiment credibility and the requester's disposition are explicit, ask the domain/mechanism roles which model terms, closures, scales or omitted couplings predict the residual pattern and which observation would discriminate them. Failed or blocked Gates remain visible and cap any interpretation.
6. **Discriminating action** — perform the cheapest sound check: analytical limit, measurement-operator replay, parameter sensitivity, frozen branch comparison, or controlled simulation. Re-run invalidated Gates.
7. **Disposition** — correct the candidate, narrow the claim, retain multiple explanations, or open a versioned model upgrade. Do not hide the original failure.

Large residuals are not the only trigger. Unexpectedly close agreement, a sign reversal, non-monotone response, abnormal replicate scatter, convergence dependent on one mesh, an implausible compensating parameter or a field inconsistent with the global QoI also require dialogue.

## Mechanism exploration loop

When interpreting a baseline run, its execution, numerical adequacy and experiment-comparison status must be explicit. Idea exploration and hypothetical controlled pilots may begin before full real-system validation under [research-efficiency.md](research-efficiency.md). A failed or blocked Gate stays visible and caps the affected interpretation; incomplete mechanism knowledge is not itself a prohibition on investigation.

The mechanism/results analyst reviews the exact post-run fields plus relevant literature and asks:

- What physical relation or trend is already supported?
- Which competing mechanisms can still produce the same observed QoI?
- Which spatial field, transient, balance, scale, controlled input or interaction would separate them?
- Is the required simulation inside the current Physics Contract, or is it a versioned new candidate?
- Will the proposed run use a holdout observation for model selection and therefore change its data role?

An exploratory-run request must define:

```text
mechanism question
literature/theory basis and locators
baseline candidate/run
varied factor(s) and justified range
frozen controls
required returned fields and diagnostics
predicted pattern under each explanation
falsifier / decision rule
numerical-adequacy checks
cost tier and stopping condition
data-role and claim impact
```

Prefer one-factor discriminating tests, dimensionless/scaling collapse, factorial or design-of-experiments studies, and sensitivity methods over ad hoc sweeps. Use a new candidate and re-run preflight if the request changes governing physics, material/BC closure, geometry, source shape, observation operator or validation role.

The executor returns raw artifacts and numerical-quality evidence, not a mechanism verdict. The analyst then evaluates predictions, counterevidence, effect magnitude and reproducibility across the declared conditions. A visually striking contour without a predeclared comparison or a statistically/numerically negligible effect does not establish a mechanism.

The mechanism analyst's requester disposition must enumerate **every preregistered competing explanation** as `SUPPORTED`, `TENTATIVE`, `FALSIFIED`, or `NOT_TESTABLE`, with an artifact locator, signed effect size, numerical and experimental/operator uncertainty comparison, and cross-condition repeatability or its explicit absence. A `RUN_RESPONSE` containing only QoI values, a contour, or an execution receipt remains open until that disposition is appended. If the returned run fails numerical adequacy, mark physical predictions `NOT_TESTABLE` rather than selecting the explanation with the best visual fit.

The analyst must also inspect what the baseline evidence and relevant literature do *not* analyze. It may propose a new field decomposition, balance, scale group, interaction, conditional comparison or operating-factor contrast when that view can distinguish live explanations. Record whether the proposal is directly source-backed, transferred from an analogous problem, or a new hypothesis. Research value comes from resolving a physical ambiguity or exposing a falsifiable limitation, not from adding plots or maximizing apparent agreement.

For every material unresolved mechanism question, the analyst must choose one of two explicit actions:

- issue a controlled evidence or run request with predictions and a stopping condition; or
- record `NO_ADDITIONAL_RUN_JUSTIFIED`, with evidence that the question is currently unidentifiable, outside the frozen Physics Contract, redundant with an existing test, dominated by failed numerical/experimental Gates, or not worth the declared cost.

After a run response, the analyst records `SUPPORTED`, `TENTATIVE`, `FALSIFIED`, or `NOT_TESTABLE` for each targeted explanation, together with effect size, uncertainty comparison, condition-to-condition repeatability and the next smallest test. A response that only says the run completed leaves the mechanism thread open.

## Termination

Close a dialogue thread only as one of:

- `ANSWERED_BY_SOURCE`;
- `ANSWERED_BY_REANALYSIS`;
- `ANSWERED_BY_DISCRIMINATING_RUN`;
- `CORRECTED_CANDIDATE`;
- `SCOPED_LIMITATION`;
- `UNRESOLVED_RETAINED`.
- `NO_ADDITIONAL_RUN_JUSTIFIED` (the evidence-bound closure retains the stated ambiguity; it does not upgrade the claim).

The close record lists evidence, invalidated/re-run Gates, affected artifacts and surviving uncertainty. Model rank, persuasion or agreement is never a closure reason.

Use [examples/scientific-closed-loop.jsonl](../examples/scientific-closed-loop.jsonl) as a schema-valid reusable exchange. Its invented values illustrate message structure only; they are not case evidence. Run `python scripts/audit_scientific_dialogue.py --ledger examples/scientific-closed-loop.jsonl --schema references/scientific-dialogue-message.schema.json --fail-open-obligations` when changing the example or lifecycle rules.
