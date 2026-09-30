# Research purpose, stages, and numerical effort

This policy governs ordinary simulation tasks. Detailed references describe applicable evidence obligations; they do not turn every possible obligation into a prerequisite for every run. A selected executable adapter may be stricter and must report its real result.

## Stage policy

| Stage | Decision being supported | Minimum useful evidence | Return boundary |
|---|---|---|---|
| exploration | Is the idea/tool/model worth pursuing; what should we test next? | Closed declared equations and inputs; units/signs/conditions; baseline/limit check; rough QoI and error/uncertainty scale; outputs relevant to one question | Inform feasibility, direction, or a new question. No claim of real-system validation or unique mechanism. |
| paper_formation | Which comparisons and explanations can support the evolving paper? | Claim-specific numerical adequacy, credible referents, explicit data roles, uncertainties and competing explanations; discriminating outputs | Return enough evidence to revise the argument and next experiment. Open noncritical limitations remain visible. |
| submission | Can each manuscript claim withstand independent scrutiny? | Current source/run bindings, reproducible relevant checks, validation alignment where claimed, calibrated uncertainty, independent review and counterevidence disposition | Deliver supported claims, retire unsupported ones, or issue a precise remaining evidence request. |

Stages can move backward after new evidence. They are work modes, not evidence of success. A paper may contain exploratory/model-internal findings if clearly described and accepted by its actual scope.

## Numerical adequacy is a research judgment

For each QoI record: definition and unit; decision it serves; expected or observed effect scale; numerical-error evidence; experimental/input/model uncertainty where available; proposed threshold and its rationale; what result would change the next decision. Estimate cost before refinement or a sweep. Do not select a threshold only because it is conventional, more digits appear possible, or another agent requested maximal precision.

Before final comparison, set the applicable threshold for a validation/pass statement. If the scientific question or scope changes, create a new version and report the reason. Do not tune a criterion after viewing the answer to rescue a failure. Exploratory adequacy can instead be an explicitly provisional, revisable judgment with no validation label.

Example: a design contrast is 12%, the finest two defensible mesh levels change the comparison by 0.8%, and input uncertainty is about 5%. If signs, balances and relevant field diagnostics are sound, refining to 0.01% offers little help for a claim about that contrast. The numbers are an illustration, not a reusable cutoff. A 0.5% contrast with 0.8% numerical variation remains unresolved, regardless of a visually smooth field or good global residual. Local mechanism/peak claims may need a different adequacy test from the average QoI.

Use analytical limits, an available benchmark, refinement, conservation, or a justified estimator appropriate to the question. Exploration need not run a full convergence matrix to decide whether a framework can express the physics. A formal precision claim does require evidence at its asserted scale. Violated units, equations, physical bounds, or data independence cannot be relaxed for efficiency.

## Work and return contract

A short task record contains question, stage, claim scope, QoI, versioned inputs, required outputs, adequacy rationale, budget, return condition, and forbidden changes. For example: investigate the signed width residual using one fixed-physics source-model contrast; return width, retained temperature field, balance and numerical variation; make only a model-internal sensitivity claim and preserve the validation data role.

No specialist may expand this into an unlimited solver optimization project. If the required evidence changes, return a proposed amended contract to the coordinator. A task that returns insufficient or contradictory evidence has still done useful work when it identifies the changed research judgment.

## Detect local optimization

After each repair/refinement, record the artifact changed, observation, and whether it changed feasibility, claim support, mechanism discrimination, parameter ranking, or the next research action. Improved residual digits alone are not research progress unless residual error is currently decisive.

After two consecutive rounds without such a change, send RETURN_FOR_REASSESSMENT with:

- failed or inconclusive attempts and their evidence;
- which claim remains blocked and which work may continue;
- cost spent and predicted cost/information gain of another round;
- the cheapest discriminating alternative, narrower claim, or next paper task.

The coordinator chooses continuation with a revised bounded rationale, a different investigation, claim revision, or writing supported results. New counterevidence reopens affected decisions even when an earlier threshold was satisfied. A negative result must not be hidden through backend switching or threshold relaxation.

## Record only useful provenance

Version IDs, file/run locators, data roles and change dependencies normally suffice for an exploratory text record. Use content digests for immutable adapter candidates, concurrent modification hazards, binaries, or caches where identity depends on content. Do not require a digest service, model fault suite, full opinion schema, or runtime-attested ledger before ordinary scientific exploration. Disclose weaker assurance honestly; enforce stronger requirements at the actual adapter and claim promotion they serve.
