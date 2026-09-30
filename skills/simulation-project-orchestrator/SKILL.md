---
name: simulation-project-orchestrator
description: Execute and assess physics or engineering simulations for a stated research question, with bounded numerical work and claim-specific evidence. Use for FEM, CFD, PDE, multiphysics, parameter studies, inverse problems, method development, and simulation audits.
---

# Simulation Project Orchestrator

Produce evidence that helps the research coordinator decide what to investigate, explain, or write next. A solver run is a means to that decision. Return scientifically useful negative findings as well as successful results; neither completion nor agreement alone validates a model.

## Start with one bounded question

Read the project's current research state and task contract. If absent, record a compact contract containing: research question, stage, proposed claim and Context of Use (COU), quantities of interest (QoIs), available evidence, expected effect or decision scale, relevant checks, time/compute budget, required outputs, and return condition. Inspect available files and software before asking for information.

Choose exploration, paper_formation, or submission. Read [references/research-efficiency.md](references/research-efficiency.md) for the stage policy, numerical-adequacy decision, and return protocol. Match fidelity to the current question; do not inherit a universal residual, mesh size, relative-error target, or another paper's exact numerics. State why further refinement could change the research judgment before doing it.

## Preserve scientific hard lines

- Close equations, units, physical parameters, and essential initial/boundary/interface conditions before running that model. A declared hypothetical model may use labeled assumptions; it cannot impersonate a real experiment.
- Distinguish USER_CONFIRMED, SOURCE_BACKED, SOFTWARE_DEFAULT, CALIBRATED, AGENT_PROPOSED, DERIVED, and UNKNOWN inputs. Never silently promote an assumption to a fact.
- Preserve source authenticity, equation-to-code fidelity, applicable physical bounds and balances, raw outputs, data roles, uncertainty, and contrary evidence. A plausible contour, low residual, another agent's agreement, or a zero exit code cannot substitute for these.
- Keep calibration and independent validation separate. Viewed or tuned holdout observations cannot later be called untouched validation data.
- A failed check stays failed for its affected claim. Budget exhaustion cannot grant PASS; scope reduction retires the broader claim and retains its failure history.

## Prepare only what this run needs

Record the simulation specification, Physics Contract, and evidence dependencies, using [references/project-objects.md](references/project-objects.md) when structure is needed. These can be sections of one small run plan; schemas and a directory per object are optional unless the selected adapter requires them.

Freeze a revision **for this reproducible run**, not the whole evolving research idea. User-authorized reversible exploratory modeling choices can be selected and documented without repeated approval. New information creates a new revision and makes only dependent results/claims stale. Ask for a human decision when an indispensable scientific choice is outside delegated scope, evidence is inaccessible, or consequences exceed the authorized use.

For application work, consult [references/application-strategy.md](references/application-strategy.md) and, when domain knowledge is missing, [references/domain-research-mode.md](references/domain-research-mode.md). Prefer a supported framework when it expresses the chosen physics. A custom method is appropriate for requested method research or a demonstrated framework limitation. Novelty assessment belongs to the coordinator unless requested here.

For a paper reproduction or experimental-validation claim, read [references/literature-validation.md](references/literature-validation.md) and [references/pre-solver-preflight.md](references/pre-solver-preflight.md). A paper used only for motivation does not trigger full experimental reconstruction. Missing comparison data blocks that comparison, while an independently closed exploratory model may still answer a narrower question.

For mechanisms, read [references/mechanism-result-analysis.md](references/mechanism-result-analysis.md). Before an exploratory run, define the physical question and the minimum outputs that could distinguish or inform it. A complete mechanism map is unnecessary at idea exploration. A formal mechanism claim later needs falsifiable alternatives, adequate diagnostics, independent review, and explicit counterevidence.

## Execute, assess, return

1. Map the intended physics to the actual framework/input. Derive a new discrete form when developing the method or when documentation cannot establish the mapping; otherwise use the documented formulation.
2. Check relevant units, signs, limits, physical closure, output configuration, and the cheap baseline/benchmark that could expose a consequential mistake. For method combinations use [references/method-review.md](references/method-review.md).
3. Run the frozen candidate. Bind evidence to its version, inputs, environment, and solver. Use content digests when concurrent edits, binary provenance, reproducible caching, or an adapter require them; do not hash ordinary text repeatedly instead of verifying behavior.
4. Evaluate only checks needed for the present claims, with reasons for nonapplicability. Use [references/gates.md](references/gates.md) to distinguish execution, numerical adequacy, experimental validation, and mechanism interpretation. Compare error and uncertainty with the effect/decision scale.
5. Return evidence paths, QoIs and uncertainty, supported/unsupported claims, remaining ambiguity, cost spent, and a recommendation for the next research decision. The requesting coordinator or analyst evaluates the scientific meaning; the executor cannot self-declare a mechanism supported.

## Bound repair and collaboration

Classify a failure before repair: input/specification, physics/formulation, implementation, environment, solver/numerical, validation, or provenance. Repair the responsible artifact and rerun only invalidated checks. Reuse reviews when their dependencies are unchanged.

After **two consecutive repair/refinement rounds that do not change the research judgment**, return to the main coordinator with the failed attempts, evidence, cost, and alternatives: a cheaper discriminating test, another explanation, a narrowed claim, or another task. Return earlier when the task budget is reached. The coordinator can authorize another bounded cycle with a stated information gain; this is not automatic acceptance or abandonment.

When authorized collaboration is available, read [references/multi-agent-governance.md](references/multi-agent-governance.md). Assign bounded producer, mechanism/data, and reviewer responsibilities as needed; roles may combine for low-risk exploration. Use independent first-pass review for consequential manuscript claims and disclose unavailable independence. Routine work does not require a new agent, model-adequacy benchmark, extensive routing record, or full governance bundle.

When an anomaly needs another role's knowledge, first check your relevant local obligations, then ask a located, bounded question. Use [references/scientific-dialogue.md](references/scientific-dialogue.md) for consequential requests and the locked append/audit helpers for shared ledgers. A request or supported dissent blocks its named claims and dependents. A ledger-level warning is not a reason to halt unrelated work. Neither majority vote nor model rank settles scientific truth.

## Adapter and delivery boundaries

For simulation-agent-mvp, read [references/local-mvp.md](references/local-mvp.md). Its legacy all-PASS governance rule remains an executable limitation: these instructions do not patch its code or bypass its promotion cap. Preserve its actual status and, if needed, choose a separate explicitly scoped workflow rather than fabricate an accepted prototype record.

For openPASO/MCP/subprocess execution, read [references/openpaso-backend.md](references/openpaso-backend.md) and [references/runtime-execution-contract.md](references/runtime-execution-contract.md). Probe the selected backend/runtime before expensive work; a handshake is only a capability fact.

Package the evidence appropriate to the stage using [references/result-package.md](references/result-package.md). Center a research report on the physical question, comparisons, mechanism, counterevidence, and bounded conclusions. Put repetitive numerical/governance detail in reproducibility files. Label results exploratory, executed, numerically adequate for a stated QoI/use, validated for a stated domain/use, or not accepted, with actual limitations.

During skill development/workflow debugging, record orchestration defects separately from scientific failures in workflow-defects.md: artifact, reproducing request, false/missed block or lost handoff, repair, and verification result.
