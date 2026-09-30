# ResearchFlow runtime API

ResearchFlow keeps an evolving research question, task handoffs, and artifact-bound claims in ordinary JSON. It does not call an LLM, run a solver, select a journal, or decide whether a scientific inference is correct. The coordinator uses it at dispatch, evidence return, and disposition. A worker writes its own result files and returns a report; it does not mutate shared state.

Python 3.11 or newer is required. There are no runtime dependencies. From this repository, install with `python -m pip install -e .`, or set `PYTHONPATH` to the absolute `src` directory. Both `researchflow` and `python -m researchflow` then expose the same interface.

## Commands

```text
python -m researchflow init PROJECT --question TEXT [--config PLAN.json] [--coordinator NAME]
python -m researchflow plan PROJECT PLAN.json
python -m researchflow task PROJECT CONTRACT.json
python -m researchflow record PROJECT TASK_ID RESULT.json
python -m researchflow decide PROJECT TASK_ID DECISION.json
python -m researchflow context PROJECT [--task TASK_ID]
python -m researchflow snapshot PROJECT FILE [FILE ...]
python -m researchflow audit PROJECT
```

The optional global `--actor NAME` precedes the command. A mismatched coordinator name is rejected on `plan`, `task`, `record`, and `decide`. This is a collaboration protocol identity, not operating-system authentication. An agent with unrestricted filesystem access can bypass it; Codex instructions and declared write ownership remain necessary.

All commands return JSON. Exit codes are `0` for success, `1` for an invalid request, and `2` for an audit with blocking protocol risks. `protocol_ok: true` means no currently blocking protocol risk was found; it never means that the research is scientifically validated. Nonblocking historical limitations remain in `risks`.

## Minimal example

Create a working directory `demo` and save the following files. The input and result text are illustrative evidence for a protocol demonstration, not scientific findings.

`config.json`:

```json
{
  "purpose": "Build an evidence-bound explanation of a transport trend",
  "stage": "exploration",
  "constraints": ["No claim of physical validation without an independent comparison"],
  "hypotheses": ["A discretization artifact may explain the trend"],
  "uncertainties": ["Whether refinement changes the mechanism ranking"],
  "next_decision": "Compare the quantity of interest across two resolutions",
  "claims": [
    {"id": "C1", "statement": "The reported trend is numerically resolved within the stated comparison"}
  ]
}
```

`contract.json`:

```json
{
  "id": "T1",
  "role": "simulation",
  "question": "Does refinement change the mechanism ranking?",
  "purpose": "Choose whether refinement or a competing mechanism deserves the next experiment",
  "claim_ids": ["C1"],
  "inputs": [{"path": "input.txt"}],
  "outputs": ["results/T1/"],
  "acceptance": ["Return QoI, comparison conditions, uncertainty, and the changed research judgment"],
  "budget": {"max_attempts": 2, "max_no_progress": 1},
  "depends_on": [],
  "owner": "simulation_executor",
  "writes": ["results/T1/"]
}
```

`result.json`:

```json
{
  "attempt": 1,
  "changed_understanding": true,
  "reason": "The comparison changes which mechanism should be tested next",
  "evidence": [{
    "path": "results/T1/comparison.txt",
    "level": "numerical_verification",
    "kind": "support",
    "claim_ids": ["C1"],
    "summary": "An explicit numerical comparison with conditions and uncertainty"
  }],
  "blockers": []
}
```

`decision.json`:

```json
{
  "action": "accept",
  "reason": "The returned comparison answers the bounded question",
  "promotions": [{
    "claim_id": "C1",
    "level": "numerical_verification",
    "evidence_indices": [0],
    "reason": "These exact artifacts support the numerical statement at the stated conditions"
  }]
}
```

Execute these commands from the directory containing the JSON files:

```text
python -c "from pathlib import Path; p=Path('demo/results/T1'); p.mkdir(parents=True, exist_ok=True); Path('demo/input.txt').write_text('Example conditions, units SI', encoding='utf-8'); (p/'comparison.txt').write_text('Protocol demonstration only: actual scientific data belong here.', encoding='utf-8')"
python -m researchflow init demo --question "What explains the transport trend?" --config config.json
python -m researchflow task demo contract.json
python -m researchflow context demo --task T1
python -m researchflow record demo T1 result.json
python -m researchflow decide demo T1 decision.json
python -m researchflow audit demo
```

The demonstration reaches a `supported` numerical claim and a closed handoff because the caller explicitly requested a promotion. The runtime cannot verify the truth of the illustrative content. In a real research project, the coordinator and independent reviewer must inspect the actual evidence before requesting that promotion.

## Persistent files and transactions

`PROJECT/.researchflow/research-state.json` is the current authority. It contains `schema_version: 1`, a monotonically increasing transaction `revision`, timestamps, `project`, `research`, `claims`, and `tasks`. `events.jsonl` records dispatches, imports, plans, and decisions with the matching `seq`. The journal is an audit trail, not an alternative scientific memory.

An OS advisory lock permits one writer at a time: Windows uses `msvcrt.locking`; POSIX uses `fcntl.flock`. The lock is released when the process exits. State writes use a flushed temporary file and atomic replacement. A durable `transaction.json` covers state/journal updates; a subsequent coordinator command or audit replays an interrupted transaction and repairs an incomplete final journal line. Corrupt complete journal events are reported instead of silently discarded. This protects normal process interruption, not every possible network-filesystem or hardware failure. Use a local project directory.

## Plan and research memory

`init --config` accepts the same fields as `plan`; an update needs a nonempty `reason`. Omitted fields survive, and supplied memory lists replace their earlier contents. Allowed fields are:

| Field | Type | Meaning |
|---|---|---|
| `question`, `purpose` | nonempty string | Current research question and overall purpose |
| `target_journal` | nonempty string | Current journal/reader hypothesis, when selected |
| `stage` | nonempty string | Recommended: `exploration`, `paper_formation`, `submission`; not a claim quality shortcut |
| `constraints` | array | Project boundaries and fixed scientific obligations |
| `facts`, `hypotheses`, `uncertainties` | arrays | Compact research memory; entries may be strings or structured source-bearing notes |
| `next_decision` | string or object | The next question that changes what the project does |
| `claims` | array of `{id, statement}` | New claims, initially `hypothesis` |
| `reason` | nonempty string | Why the plan changed; optional on initial configuration |

Memory notes are narrative and do not create validated support. A changed scientific assertion needs a new claim ID. Do not overwrite an old statement to make conflicting evidence disappear; use `claim_updates` to retire the old assertion and `plan` to add the narrower one. Earlier plans remain represented by journal reasons and field changes; the current research memory is intentionally compact. The journal does not contain full historical plan snapshots.

Each claim has `id`, `statement`, `status`, `support`, `challenges`, and `limitations`. Status is `hypothesis`, `supported`, `invalidated`, `narrowed`, or `parked`. `support` maps each explicitly supported evidence level to specific artifact locators and source task/attempt. There is no automatic hierarchy from numerical verification to physical validation.

## Task contract

The minimal contract fields are:

| Field | Type / requirement |
|---|---|
| `id` | Unique 1–100 character ID using letters, digits, `.`, `_`, `-`; begins with a letter/digit |
| `role`, `question`, `purpose` | Nonempty strings |
| `claim_ids` | Array of known claim IDs, possibly empty for discovery work |
| `inputs` | Array of `{path, revision?}`; defaults to an empty array |
| `outputs` | Nonempty array of project paths identifying files or directories to return |
| `acceptance` | Nonempty claim-relative criteria; recommended array of strings |
| `budget` | `{max_attempts: positive integer, max_no_progress: positive integer}` |
| `depends_on` | Array of task IDs or dependency objects; defaults to empty |
| `owner` | Protocol worker identity; defaults to `role` |
| `writes` | Nonempty array of exclusively owned project paths; defaults to `outputs` |

The runtime adds `project_revision` at dispatch. Outputs must lie within declared writes. Workers cannot declare project-root ownership or writes inside `.researchflow`. Two active tasks cannot own overlapping paths. Closed tasks release ownership. Inputs may point to external source files; task output ownership is confined to the project. A relative path is resolved from `PROJECT`, not from the JSON report's directory.

A string dependency such as `"T1"` requires completed requester disposition only. It does not assert that a hypothesis is true. A substantive dependency explicitly identifies assumptions:

```json
{
  "task_id": "T1",
  "claim_ids": ["C1"],
  "required_level": "numerical_verification",
  "affects_claim_ids": ["C3"]
}
```

`claim_ids` names source claims. `required_level`, when supplied, requires current support at that exact level, fresh artifacts and fresh upstream inputs/dependencies. `affects_claim_ids` scopes which downstream claims rely on the assumption; it defaults to every claim in the downstream contract. Without `required_level`, named source claims still cannot be retired or invalidated. All dependency tasks must have requester disposition before dispatch.

## Evidence locators and result reports

Locators are `{path, revision}`. Omit `revision` to bind the file automatically when the coordinator dispatches/imports. `snapshot PROJECT FILE...` returns ready-to-use locators. A revision is `sha256:` followed by the digest of the actual file. It is used only to detect changed or missing evidence/input artifacts. A hash never establishes scientific correctness.

An input revision supplied at dispatch must match. A report with a supplied stale evidence revision can be imported as an honest record, but audit exposes the mismatch and promotion is refused. Prefer immutable result files for each attempt; changing one shared result file destroys the ability to reproduce earlier support.

Result fields are:

| Field | Type / requirement |
|---|---|
| `attempt` | Next consecutive integer, starting at 1 |
| `changed_understanding` | Boolean; did this attempt change a relevant research judgment? |
| `reason` | Nonempty explanation of the change or lack of progress |
| `evidence` | Array of evidence objects; may be empty for a documented failed attempt |
| `blockers` | Array of scoped blocker objects; may be empty |

An evidence object extends the locator with:

```json
{
  "path": "results/T1/attempt-1.csv",
  "revision": "sha256:...",
  "level": "numerical_verification",
  "kind": "negative",
  "claim_ids": ["C1"],
  "summary": "The predicted difference did not appear under the reported conditions"
}
```

Levels are `observation`, `numerical_verification`, and `physical_validation`. Kinds are `observation`, `support`, `negative`, and `counterevidence`. `claim_ids` must lie within the task contract. The explicit kind `support` is necessary for promotion; importing a result does not promote anything.

A blocker is `{claim_ids: ["C1"], reason: "...", kind?: "units"}`. It must name at least one affected claim; a concrete blocker reason is mandatory. A blocker on C1 prevents promotion of C1 while allowing C2 to proceed. Numerical residuals, QoI tolerances, experimental replication and other scientific criteria belong to the task-specific `acceptance`; the runtime hard-codes no accuracy threshold.

`counterevidence` invalidates the named assertion while retaining its earlier support and the conflicting artifact. New blockers invalidate affected previously supported claims. Invalidation propagates only through named substantive dependency claims and their `affects_claim_ids`. A supported downstream assertion derived by the affected task becomes `invalidated`; unrelated claims continue.

## Requester disposition

`decision` requires `action` and a nonempty `reason`. Actions are `accept`, `continue`, `narrow`, `reframe`, or `park`. Acceptance closes a handoff; it does not support a hypothesis. The last three actions are valid outcomes for unproductive directions or negative evidence.

After an attempt exhausts its allowance or reaches the consecutive no-progress limit, `continue` also requires:

```json
{
  "reassessment": {
    "reason": "Refinement no longer discriminates the competing explanations",
    "strategy_change": "Compare a corrected boundary formulation before spending on finer meshes",
    "additional_attempts": 1
  }
}
```

`additional_attempts` is a nonnegative integer and must be positive when the total attempt allowance is spent. The runtime checks that an explicit reassessment exists; the coordinator/reviewer assesses whether the stated change is meaningful. A worker's `changed_understanding: true` is also a report to be judged, not a trusted oracle.

Optional `promotions` is an array of:

```json
{
  "claim_id": "C1",
  "level": "numerical_verification",
  "evidence_indices": [0],
  "reason": "Why these specific returned artifacts support this exact claim"
}
```

Indices refer to the latest returned report. Promotion requires an `accept` or `narrow` disposition; every selected artifact must explicitly support this claim at the exact requested level, still exist, and still match its revision. Contract inputs and relevant upstream dependencies are checked again. Unresolved blockers or counterevidence prevent promotion. A numerical verification artifact cannot promote physical validation.

Optional `claim_updates` is an array of `{claim_id, status, reason}`. Allowed statuses here are `invalidated`, `narrowed`, and `parked`. They apply only to the task's scope. The previous evidence and challenges remain visible.

Optional `resolutions` is an array of:

```json
{
  "claim_id": "C1",
  "challenge_id": "T1:1:blocker:0",
  "evidence_indices": [0],
  "reason": "A later corrective comparison fixes the incompatible boundary units"
}
```

A resolution must cite fresh relevant evidence from a later attempt or a later returned task. The same result cannot clear its own blocker. The correction must include a different artifact/revision from the challenged evidence. Resolving a challenge does not itself restore support; a separate explicit promotion is needed. These are traceability checks. A reviewer must still judge whether the correction really resolves the scientific issue.

## Context and audit interpretation

`context` returns current project purpose/question/stage/revision, compact facts/hypotheses/uncertainties/next decision, claims, and a concise task status table. `context --task` scopes the claim set and includes that contract's inputs with freshness flags, outputs, ownership, acceptance, budgets, latest result and latest decision. It avoids dumping the full conversation or journal. The dispatcher should pass this context and the relevant skill, not the entire project history.

Audit risks include unfinished handoffs, stale/missing inputs or evidence, unsupported claimed support, changed substantive dependencies, unresolved challenges and journal gaps. Every risk includes `blocking`. A retained failure on a `narrowed`, `parked`, or `invalidated` assertion is nonblocking because that assertion is no longer used as established support. A challenge on an active hypothesis or supported assertion remains blocking. Historical stale artifacts of closed tasks are nonblocking unless used by a currently supported claim. Nonblocking does not mean corrected; authors must retain the limitation and avoid reusing the retired assertion.

The runtime cannot verify source authenticity, equations, units inside files, statistical adequacy, representativeness, novelty, journal suitability, or the causal meaning of a comparison. Agents and reviewers must perform those checks. The tool prevents several concrete protocol errors and preserves the reasons for scientific decisions; it does not guarantee a paper's acceptance or a model's obedience.

## Python API

The public functions mirror CLI commands: `initialize(project, question, config=None, coordinator="coordinator")`, `plan(project, update, actor=None)`, `task(project, contract, actor=None)`, `record(project, task_id, result, actor=None)`, `decide(project, task_id, decision, actor=None)`, `context(project, task_id=None)`, `snapshot(project, paths)`, and `audit(project)`. Protocol errors raise `GovernanceError`. All functions return dictionaries except `snapshot`, which returns a list of locators. Read/write failures may raise normal `OSError`.

Run `python -m unittest discover -s tests -p test_runtime.py -v` to verify the protocol behaviors. Tests exercise successful handoffs, negative evidence, budget/no-progress reassessment, stale evidence and inputs, claim-scoped dependencies, numerical/physical distinctions, unit blockers, later corrections, counterevidence propagation, retained historical failures, single-writer locking and interrupted transaction recovery.
