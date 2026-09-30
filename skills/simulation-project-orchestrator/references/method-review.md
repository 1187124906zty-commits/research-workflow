# Numerical method review and derivation dossier

Use this when the user proposes a new discretization, coupling, surrogate, learned closure, or fusion of methods.

## Review sequence

1. State the mechanism: which physical or numerical bottleneck the combination addresses and why the change should help.
2. Separate what is literature-supported, naturally combined from established methods, newly assumed, and not yet verified.
3. Define domains, variables, operators, parameters, function spaces, IC/BC/interface conditions, and QoIs.
4. Derive the continuous coupled problem and identify conservation laws or thermodynamic restrictions.
5. Derive weak/residual forms, including all integration-by-parts boundary terms and sign conventions.
6. Specify spatial/time discretization, stabilization, nonlinear linearization, transfer/projection operators, and solver/preconditioner.
7. Check compatibility: well-posedness, inf-sup/coercivity where relevant, conservation, consistency, stability, positivity/monotonicity, frame invariance, dimensional consistency, and limiting behavior.
8. Identify the added error terms: discretization, splitting, mapping, surrogate/closure, quadrature, iteration, and data error.
9. Define measurable acceptance and falsification tests before running.

## Coupling-specific obligations

- Explicitly define exchanged variables, location, units, sign/orientation, interpolation, conservation property, and temporal synchronization.
- Distinguish monolithic, partitioned explicit, and partitioned implicit coupling.
- For partitioned coupling, state relaxation/acceleration, rollback/checkpoint behavior, convergence norm, tolerance, maximum iterations, and failure behavior.
- Verify nonmatching-mesh mapping separately from participant solvers; check that zero exchange cannot appear as successful convergence.

## ML-specific obligations

State exactly which numerical component ML replaces or augments; the data-generating process; labels/reference fidelity; physical constraints; extrapolation variables; uncertainty/calibration; fallback behavior; and comparison to the non-ML baseline. A black-box parameter-to-output network is not automatically a numerical-method contribution.

## Deliverable

Produce a Numerical Method Dossier containing definitions, equations, derivation, assumptions, discrete algorithm/pseudocode, stability/consistency discussion, error budget, implementation mapping, benchmarks, ablations, sensitivity tests, and falsification criteria. Clearly label unproved statements and empirical hypotheses.
