# Paper-conditioned pre-solver preflight

Read this reference for paper reproduction, paper-derived physical inputs, or experimental-validation claims. A paper used only for motivation or an analysis analogy does not require full experiment reconstruction. Select obligations for the current stage and claim using [research-efficiency.md](research-efficiency.md); the objective is sufficient closure and evidence for the chosen run, not exhaustive reconstruction of every related paper.

## Admission invariant

Formal solver generation and execution are downstream of one immutable `preflight-manifest` with `solver_ready=true`. Do not infer readiness from an overall score, confidence average, majority vote, model rank, or the fact that software is installed.

`solver_ready` is true only when every applicable blocking obligation is `PASS`, or is `NOT_APPLICABLE` with a located mathematical reason. `WARN` may survive only for obligations declared non-blocking for the stated Context of Use. `FAIL` or `BLOCKED` on any critical obligation keeps the case out of formal execution.

Exploratory algebra, unit conversion, geometry previews, backend probes, or sensitivity bracketing may continue while blocked when they are explicitly labeled `EXPLORATORY_NOT_A_REPRODUCTION`. A useful-scale pilot may also proceed under its own scoped preflight when its equations and essential inputs are closed, with bounded assumptions and a question it can actually answer. Missing comparison data blocks the experimental-validation claim, not every calculation of a closed model. A missing essential physical closure still prevents that model's execution. Exploratory outputs cannot be promoted into the formal reproduction or validation candidate without a new preflight revision.

## Dependency order for formal reproduction/validation

This order describes evidence dependencies for the named formal claim, not a project-wide prohibition on exploration. A closed hypothetical model can first answer feasibility or tool questions using a short run-specific contract. Unknown real experimental inputs stay unknown and limit later validation claims.

```text
source acquisition and identity
-> paper decomposition and source tracing
-> experiment/referent reconstruction
-> domain Physics Contract and closure review
-> mechanism hypotheses and output/diagnostic contract
-> numerical-method obligations and backend capability match
-> cross-role condition/QoI reconciliation
-> immutable preflight decision
-> solver artifacts
-> execution and post-run V&V
```

If a numerical paper cites an earlier experiment, obtain and inspect the experimental source instead of copying its values through the numerical paper. Preserve both locators and any discrepancy. A value found only in the numerical paper is not silently promoted to an experimentally reported fact.

## Role split

Use separate scoped roles when sub-agents are authorized. Each role reads the frozen source set needed for its obligations; a downstream role must not rely only on another agent's prose summary.

### Source and experimental-evidence role

Owns:

- paper identity, version of record, supplements, repositories, licenses and retractions;
- the experiment referent, specimen/batch, actual geometry and tolerances;
- reported material properties and how they were measured, assumed or calibrated;
- loading, IC/BC/interface/contact/environmental conditions;
- instruments, calibration, sensor positions, sampling, filtering and measurement operators;
- raw observations, replicate structure, randomness, uncertainty and data roles;
- trace from a numerical paper to every original experimental source it uses.

It emits a source-located Validation Contract and an explicit list of `UNKNOWN` or conflicting items. It cannot select a convenient physical default or decide that numerical convergence compensates for missing experiment evidence.

### Domain physics role

Instantiate this role for the actual problem class, such as heat transfer, solid mechanics, fluid mechanics, electromagnetics, reacting flow, porous media, fracture, or a named multiphysics coupling. It must understand the paper's equations rather than receive only a parameter table.

Owns:

- domains, state variables, governing equations and constitutive closure;
- assumptions, validity range, signs, units, frames and limiting cases;
- initial, boundary, interface and contact conditions;
- conservation laws and coupling exchanges;
- a dependency map from every coefficient and condition to its evidence source;
- a structured request for the data required to close the model.

It cannot declare an experiment reconstructable, reinterpret calibration data as validation, or replace missing physics with a solver default.

### Numerical-method role

Owns:

- the documented framework formulation, spaces, stabilization and time/coupling schemes mapped to the Physics Contract; new strong-to-weak/discrete derivation when the task changes the numerical method or the mapping cannot otherwise be established;
- well-posedness and compatibility conditions;
- mesh/time/increment, nonlinear and linear-solver requirements;
- expected convergence, conservation and benchmark checks;
- mapping of experimental QoIs through the same sampling or spatial-averaging operator;
- backend capability matching, including reasons a verifier is not applicable.

It cannot start implementation until the domain contract is closed enough for the requested claim. It may propose alternatives, but each alternative records which physics or data assumption changes.

Mesh size, time step, increment size, nonlinear tolerances and linear-solver settings are not required to match the numerical paper unless the user explicitly requests a code-for-code or discretization reproduction. For an experiment-validation study, omission of those settings from the paper is not itself a preflight blocker. The numerical-method role must instead choose them for the adopted discretization and later demonstrate numerical adequacy with the applicable mesh/time convergence, stability, conservation and solver-error checks. This does not relax the requirement to close physical parameters, experimental conditions or the measurement operator before execution.

### Mechanism and results-analysis role

Use this responsibility when physical interpretation is needed. In exploration, the question and minimum discriminating output contract can be compact and handled by the coordinator/domain role; no complete frozen mechanism map or separate agent is required. For a consequential formal mechanism claim, an independent analyst reads the original evidence and current Physics Contract, then creates the revision-bound plan defined in [mechanism-result-analysis.md](mechanism-result-analysis.md).

Owns:

- the physical question and a claim ceiling distinct from the validation pass/fail statement;
- source-located analysis ideas and clearly labeled new deductions;
- falsifiable mechanism hypotheses, credible competing explanations and discriminating observations;
- the raw/derived field, history, integral, probe, sensitivity and figure contract required before solver generation;
- a post-run interpretation that separates observation, numerical inference, physical interpretation and unresolved alternatives.

It cannot alter experimental facts, data roles, the Physics Contract, calibration targets or validation thresholds. Its first-pass plan and post-run judgment must be independent of the code/solver producer. A plausible explanation cannot clear a numerical or physical-validation failure.

### Implementation and execution roles

Formal reproduction/validation execution begins only after claim-specific admission. Exploratory generation/execution uses its own closed, labeled contract. The engineer maps the frozen run revision into solver inputs and reconstructs what the input actually encodes; the executor records the environment and native outputs. Neither role may silently fill a missing parameter, condition or data role. Authorized reversible hypotheses create a new labeled revision and rerun affected checks.

## Cross-role reconciliation before admission

Independent role reports are necessary but not sufficient. Before `solver_ready=true`, require direct, recorded reconciliation for every cross-role dependency that affects a blocking obligation:

- the domain role asks the experiment role for every coefficient, condition, interface or operating range that remains source-dependent;
- the numerical role asks the experiment role how each QoI is sampled, averaged, thresholded or otherwise observed, and asks the domain role which invariants and limits the discretization must preserve;
- the mechanism role asks the experiment role which trends/replicates can distinguish its hypotheses and asks the numerical/execution roles whether every discriminating raw field and cadence is actually available;
- the experiment role asks the mechanism/numerical roles which raw observations, uncertainty decomposition and coordinate conventions are needed, rather than exporting an undifferentiated data dump.

Use the scientific-dialogue lifecycle for consequential requests. Admission requires either a located answer, a bounded unresolved item whose affected formal claim remains blocked, or a documented `NOT_APPLICABLE` reason. A coordinator summary cannot stand in for a missing role response. The mechanism plan may be independently drafted before these exchanges, but its output mapping cannot pass until the responsible implementation/numerical role responds.

## Blocking obligation matrix

For the current formal claim, the preflight manifest records each applicable item below, its owner, evidence locators, status, reason, dependencies and missing-data request. Items irrelevant to the claim are NOT_APPLICABLE with a scope reason; unavailable validation data block validation, not a separately closed exploratory model.

| Area | Blocking obligations |
|---|---|
| Sources | identity/authenticity, full-text acquisition, experimental source tracing, supplements/data availability |
| Experiment | referent and specimen, geometry, materials, conditions, instrument and measurement operator, observations and data roles |
| Repetition and uncertainty | specimen/realization count, repeated measurements, randomness structure, experimental uncertainty appropriate to the claim |
| Physics | variables/equations, constitutive closure, IC/BC/interface/contact closure, units, conservation, assumptions and validity domain |
| Numerical method | documented formulation-to-physics mapping (new derivation when needed), spaces and compatibility, stabilization/time/coupling scheme, solver tolerances, convergence and conservation tests |
| Mechanism analysis | physical question, source-located analysis logic, falsifiable hypotheses and alternatives, required output/diagnostic contract, comparison design, output-to-solver mapping and claim consequences of missing fields |
| Validation alignment | QoI definition, sign/unit/frame, location/time/load state, condition match, measurement operator, disjoint calibration and validation data |
| Backend | required dimensions/elements/physics/BCs/couplings supported, versions recorded, output fields and verification hooks available |
| Acceptance | Context of Use, validation statistic, threshold and claim ceiling stated before inspecting the final comparison |

A paper need not report every quantity in the world. It must report or defensibly derive every quantity that can materially change the requested result or validation decision. Label derivations and additional assumptions; do not call them reported values.

For experiment-validation work, freeze the real geometry, material, operating and observation conditions first. The numerical method may then be selected or adapted to those anchors and need not duplicate the paper's mesh, time step or solver. Missing paper discretization detail does not block an independently verified method; changing a physical term, parameter, condition, observation operator or data role does.

Keep two comparisons distinct. Agreement with a paper's numerical output is a secondary implementation or trend check unless the Context of Use explicitly targets numerical reproduction. Agreement with held-out experimental observations, after calibration data have been separated, is the physical-validation comparison. A solver may use a different sound discretization from the paper and still support the latter claim when its own numerical-error evidence is adequate.

## Handoff contract

Every preflight opinion states:

- `claim` and exact scope;
- source and candidate revision inspected;
- `required_evidence` and evidence actually located;
- blocking and non-blocking missing obligations;
- assumptions proposed but not accepted;
- non-negotiable `stop_line` conditions;
- a discriminating observation or correction that would clear each stop-line;
- downstream tasks authorized if the opinion stands.

The integrator preserves separate first-pass opinions and conflicts. It produces a dependency-aware readiness decision; it does not persuade a specialist to weaken a requirement so that implementation can begin.

## Structured missing-data request

When blocked, ask only for evidence that changes readiness. For every request include:

1. the missing item and why the equation, BC, QoI or validation decision depends on it;
2. acceptable evidence forms, such as a paper locator, CAD dimension, instrument sheet, raw CSV, calibration record or user-confirmed operating condition;
3. whether a bounded exploratory assumption is possible;
4. which claims remain prohibited under that assumption.

Do not generate a full solver script merely to discover that a source, coefficient, BC or validation observation was missing.

## Invalidation

Any later change to a paper version, geometry, material, physics term, IC/BC/interface condition, data role, measurement operator, numerical method, backend or acceptance criterion sets `solver_ready=false` until affected obligations are rerun. Previously executed fields remain historical artifacts and cannot support the revised claim.

A later change to a mechanism hypothesis, discriminating comparison, required-output set, sampling rule or raw-to-derived diagnostic also invalidates `MECHANISM_ANALYSIS_READINESS` and the affected post-run interpretation. Adding a plot after execution cannot repair a raw field that was never exported.
