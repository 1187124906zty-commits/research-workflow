# Evidence gates and claim levels

## Applicability before gate contract

Select checks for the current stage, QoI, claim and consequence using [research-efficiency.md](research-efficiency.md). This is a catalog, not fourteen mandatory prerequisites for every pilot. Record why a check is deferred or inapplicable and the resulting claim ceiling. A missing formal-validation obligation does not block an unrelated closed-model feasibility calculation.

Numerical adequacy is tied to effect/decision scale and its uncertainty. A small algebraic residual is insufficient; a universal precision target is unjustified. Once relevant error evidence is adequate for the present question, return it to the coordinator rather than refining indefinitely.

## Gate contract

Every gate records `gate_id`, evaluated artifact revision, method, metric, threshold, observed value, evidence paths, outcome (`PASS`, `FAIL`, `WARN`, `NOT_APPLICABLE`, `BLOCKED`), and invalidation dependencies.

Machine-readable draft: [gate-result.schema.json](gate-result.schema.json).

## Required interpretation

| Gate | Minimum question | Typical deterministic evidence | What a pass does not prove |
|---|---|---|---|
| SPEC_COMPLETENESS | Are COU, QoI, physics-changing inputs, and acceptance rules known? | schema and dependency checks | correct model |
| DIMENSIONAL_CONSISTENCY | Are equations, parameters, and conversions dimensionally consistent? | unit algebra | correct physics |
| PHYSICS_CLOSURE | Are variables, relations, conditions, and parameters sufficient? | structural equation/unknown count and domain rules | well-posed discretization |
| MECHANISM_ANALYSIS_READINESS | For a formal mechanism claim, are the question, alternatives, diagnostics and outputs mapped to the run? Exploration uses a smaller question/output contract. | run-stage plan and field-coverage audit | that a mechanism will be supported or validation will pass |
| FORMULATION_SOUNDNESS | Do strong form, weak form, spaces, stabilization, time/coupling schemes agree? | symbolic checks, limiting cases, expert rules | implementation fidelity |
| CODE_EQUATION_FIDELITY | Does solver input encode the approved Physics Contract? | input-to-equation reconstruction and structural diff | discretization accuracy or reality |
| EXECUTION | Did the intended solver truly run and produce finite, complete outputs? | solver-native logs and output audit | correct physics or adequate resolution |
| NUMERICAL_ACCURACY | Is error below a case-calibrated threshold? | analytical/reference solution, MMS, estimators | validation against reality |
| PHYSICAL_BOUNDS_AND_INVARIANTS | Does every accepted state obey applicable positivity, maximum/minimum principles, admissible fractions/tensors, monotonicity, symmetry and limit invariants? | history-wide field bounds, invariant tests, matrix/flux monotonicity diagnostics | mesh/time convergence, global conservation or physical validation |
| MESH_TIME_CONVERGENCE | Does the QoI/field converge at an expected or defensible rate? | mesh/time refinement and GCI/order estimates | model-form validity |
| CONSERVATION_AND_INTERFACES | Are global/local balances and coupled transfers satisfied? | balance integrals and independent interface traces | empirical accuracy |
| PHYSICAL_VALIDATION | Does the model agree with a relevant referent within combined uncertainty? | experimental/observational comparison | uses outside the tested domain |
| UNCERTAINTY_AND_SENSITIVITY | Are material, input, numerical, and model uncertainties propagated and drivers known? | ensembles, PCE/MC, sensitivity indices, discrepancy model | universal credibility |
| MECHANISM_INTERPRETATION | Do the exact post-run fields, balances, trends and sensitivities support a bounded mechanism statement after counterevidence and alternatives are checked? | post-run-bound hypothesis table, diagnostic calculations and missing-field audit | experimental validation, causal uniqueness, or use outside the tested domain |
| COU_ACCEPTANCE | Is the accumulated evidence adequate for the stated decision and consequence? | risk-weighted acceptance record | another COU |
| OUTPUT_QUALITY | Is the final package internally consistent, complete, readable, and successfully compiled/rendered? | structure/source coverage audit, real LaTeX compile, PDF render inspection | scientific correctness of the underlying model |

Multi-agent claims need traceable tasks, evidence, responsibility, review and dissent. Strict adapters may additionally require bundle presence, runtime assurance, content binding, model-adequacy and full routing fields; consult [multi-agent-governance.md](multi-agent-governance.md). Ordinary exploration can use compact versioned records with honest assurance limits. Governance evidence does not establish physical or numerical correctness.

Use case-specific thresholds. A universal residual or relative-error cutoff is rarely defensible across PDE families, solvers, and QoIs.

Global balance and nonlinear convergence never override a violated physical bound. Check bounds over the accepted step/load states needed for the claimed domain and the actual state field, not only plotted samples. When a bound follows from the continuous problem, test whether the adopted discretization preserves it; clipping is not a pass and usually breaks the balance. Physically invalid low-cost levels cannot support calibration, convergence extrapolation, or physical interpretation. Their failure may still support diagnosis and a new corrected pilot. An inconclusive refinement test blocks its precision claim, not every distinct research question.

## Claim ladder

1. **Specified** — requirements and provenance recorded.
2. **Formulated** — mathematical and numerical formulation passed review.
3. **Implemented** — generated artifacts structurally match the formulation.
4. **Executed** — target solver completed with audited outputs.
5. **Numerically verified** — numerical errors and convergence are controlled for stated QoIs.
6. **Validated** — comparison to a real-world referent supports a stated domain and COU.
7. **Accepted for COU** — risk owner accepts residual uncertainty for the named decision.

Report the highest achieved level and all failed, skipped, or blocked gates. Never infer level 5 from level 4, or level 6 from level 5. `OUTPUT_QUALITY` controls whether a package is deliverable; it does not raise the scientific claim level.

`MECHANISM_ANALYSIS_READINESS` controls whether a mechanism-oriented formal run has an adequate output contract; `MECHANISM_INTERPRETATION` controls only the later mechanism claim. A useful diagnosis may remain reportable when physical validation fails, but the failure remains visible and the diagnosis is not relabeled as validation.

## Authority and cache invariants

- A scientific `PASS` or `WARN` needs at least one claim-specific `EvidenceRef` with source ID, locator, and supported claim.
- External authority cannot replace the raw artifact showing what this exact revision executed.
- An acquired source must exist at its recorded path; acquired PDFs must pass a PDF signature check before their text is treated as evidence.
- Cache an unchanged review only when the gate, inspected dependency versions and scope all match. Where the adapter or cache uses content digests, those digests must also match; ordinary text tasks need not create an Authority Registry or digest service.
- A report must contain every source cited by its final gate list. Do not render the report before adding `OUTPUT_QUALITY`; use a bounded final-render/check loop so the report and gate JSON agree.

## Fault injection for testing the Agent

For workflow development, choose representative fault classes for the capabilities being tested: missing BC/unit/material, wrong PDE term/sign, wrong boundary tag, stale input/result links, incompatible spaces, false convergence, violated bounds/balances, wrong observation operator, calibration/validation leakage or fabricated evidence. A full fault suite is not a prerequisite for each scientific task.
