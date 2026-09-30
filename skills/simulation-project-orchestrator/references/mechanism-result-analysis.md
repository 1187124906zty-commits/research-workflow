# Mechanism-oriented result analysis

Read this reference for a real-system simulation whose result must explain a physical response, support engineering inference, compare designs or operating conditions, or be validated against experiment. The role exists to make numerical simulation answer the physical question rather than terminate at a residual or agreement score.

## Evidence priority and scope

Anchor the case first to the best available real evidence: experimental geometry and conditions, material identity and properties, loads and boundary/interface conditions, measurement operators, replication, uncertainty, and frozen calibration/validation roles. A numerical paper's mesh, time step, solver brand, or discretization is secondary unless the stated Context of Use is code-for-code reproduction. Select or adapt the numerical method to the frozen physical problem and demonstrate its own convergence, stability, conservation, and solver accuracy.

Keep three changes distinct:

- a **numerical change** alters approximation or solution strategy while preserving the Physics Contract and measurement operator;
- a **model-form change** alters governing terms, constitutive closure, dimensionality, interfaces, or omitted physics and invalidates dependent physics and validation reviews;
- an **evidence-anchor change** alters a real condition, parameter, dataset role, uncertainty model, or observation operator and requires source/experiment reconciliation.

Do not refuse an otherwise answerable calculation merely because a sound numerical choice differs from the paper. Do not disguise a physical or evidence change as numerical flexibility.

## Independent role and timing

During exploration, state one physical question, provisional competing explanations if useful, and the minimum outputs that could inform the next decision. This may be a compact coordinator/domain responsibility; incomplete knowledge of mechanisms is a reason to investigate, not an automatic solver block. Before consequential formal mechanism execution/interpretation, assign an analyst who reads relevant primary papers and raw contracts and records a first pass independently of the solver/code producer.

The analyst may:

- state the physical question and competing causal explanations;
- extract analysis logic, nondimensional groups, diagnostic sections, trends, or mechanism arguments from located sources;
- derive clearly labeled new hypotheses from conservation laws, scale analysis, limiting cases, or adjacent literature;
- require fields, histories, integrals, probes, sensitivity runs, and comparison plots needed to distinguish those hypotheses;
- define what observation would falsify each explanation and what conclusion remains possible if a field is unavailable.

The analyst may not change experimental facts, data roles, governing equations, material values, boundary conditions, validation thresholds, or another role's supported stop-line. It cannot turn a plausible narrative into validation evidence.

The role is also an active scientific question owner, not only a report writer. After the baseline run's numerical and experiment-comparison status is explicit, it should use [scientific-dialogue.md](scientific-dialogue.md) to ask the experiment, domain, numerical and execution roles targeted questions. When current evidence cannot distinguish mechanisms, it may request controlled exploratory runs with a literature/theory basis, frozen controls, required returned fields, predicted alternatives and falsifiers. The executor returns artifacts and numerical-quality evidence; the analyst owns the later mechanism interpretation.

This responsibility is reciprocal and continues after the first run. The analyst must answer experiment/numerical roles when they ask which field or comparison is actually discriminating; it must evaluate every requested run response against the preregistered alternatives; and it must either close the thread, narrow the question, or record why no further run is justified. It cannot merely consume artifacts and write a persuasive final narrative.

As part of post-run research design, compare the current evidence with the analysis logic in the primary papers and identify missing but testable views: balance decompositions, scale transitions, interactions, conditional trends, spatial or temporal asymmetry, threshold behavior, or a model term whose signature differs from parameter error. A transferred or new analysis angle is welcome when labeled honestly and paired with a falsifier. Novelty is not a Gate; discriminating power and evidence traceability are.

## Run-stage output contract

For an exploratory run, a short versioned plan with question, scope, assumptions, discriminating comparison, required outputs, expected information gain and cost/return condition is sufficient. It does not imply a supported mechanism. Freeze only this run's outputs and controls; hypotheses can evolve after evidence is returned.

For formal mechanism claims, use the fuller plan below. Its schema is an adapter-compatible format, not an additional prerequisite for every pilot.

Create `mechanism-analysis-plan.json` conforming to [mechanism-analysis-plan.schema.json](mechanism-analysis-plan.schema.json), plus a readable Markdown rendering when useful. Bind it to the specification, Physics Contract, source set, candidate revision, and preflight report.

The plan must contain:

1. the concrete physical question and claim ceiling;
2. source-located literature analogies and their applicability limits;
3. at least one falsifiable mechanism hypothesis and, when causal attribution is intended, at least one credible competing explanation;
4. for each hypothesis, predicted signs, trends, spatial patterns, time/load ordering, or scaling behavior and observations that would contradict it;
5. required raw and derived outputs with variable meaning, unit, location/region, sampling cadence/load state, association, export method, and consequence if missing;
6. diagnostic calculations, including equations, balances, scale or nondimensional analysis, and transformations from raw fields;
7. a comparison design stating which condition or parameter changes, what stays frozen, and which experimental observations are aligned;
8. the independent first-pass review IDs and unresolved limitations.

Every claimed mechanism must have at least one diagnostic that can distinguish it from a competing explanation. A list of attractive plots is not a mechanism plan.

## Readiness and field-coverage audit

Evaluate `MECHANISM_ANALYSIS_READINESS` for a formal mechanism claim before its solver generation. It passes only when:

- the plan is revision-bound and independently reviewed;
- hypotheses are falsifiable within the simulated and observed domain;
- required outputs are mapped to actual solver fields, logs, integrals, or deterministic post-processing;
- units, coordinate frame, spatial/time sampling, and raw-to-derived transformations are specified;
- the experiment and simulation comparison conditions align;
- missing outputs have explicit claim consequences.

Missing a critical field, an unfalsifiable explanation, or a comparison that changes multiple uncontrolled causes is `BLOCKED` for the affected mechanism claim. Cheap exploratory runs may proceed when labeled, but they cannot be promoted into a formal mechanism conclusion. A pure analytical/MMS or software-verification case may be `NOT_APPLICABLE` with a scope reason.

Immediately before execution, compare the frozen plan to the generated solver output configuration. Immediately after execution, audit every required field for existence, finite values, units, coordinate/time coverage, and candidate/run binding. Preserve missing or malformed items; do not silently replace a requested raw field with a visually similar derived quantity.

## Post-run interpretation

Analyze in this order:

1. execution integrity and raw-field completeness;
2. solver residuals, numerical error, mesh/time/increment evidence, conservation, and interface balances;
3. calibration identifiability and propagated calibration uncertainty;
4. comparison to held-out experiment through the declared measurement operator;
5. condition trends, spatial/temporal field structure, balances, scales, and sensitivity drivers;
6. competing explanations, counterevidence, and the smallest discriminating next test;
7. a bounded conclusion and claim level.

Separate observation, numerical inference, and physical interpretation. Report whether the data support, contradict, or cannot distinguish each hypothesis. Agreement of a global QoI does not establish the local mechanism, and a mechanism explanation does not clear a failed validation statistic.

When residuals are systematic, partition plausible causes without pretending they are uniquely identified: numerical error; input/parameter uncertainty; measurement-operator mismatch; boundary/initial-condition error; constitutive or source-model error; omitted coupling or physics. Use sensitivity or discriminating runs to narrow alternatives. If evidence cannot distinguish them, say so.

Evaluate `MECHANISM_INTERPRETATION` only after binding the review to the exact post-run artifact set. It passes for a stated mechanism claim only when required outputs exist, applicable numerical and experimental Gates are visible, predictions and counterevidence were checked, and alternatives were considered. Failure or blockage here does not erase valid execution or numerical-verification facts; it only caps the mechanism claim.

For each material ambiguity, require a dialogue disposition: a controlled next request, a bounded closure, or `NO_ADDITIONAL_RUN_JUSTIFIED` with located evidence and the surviving uncertainty. Require a mechanism analyst's response after every executor `RUN_RESPONSE`; otherwise the thread remains incomplete even if all files exist.

## Report structure

Organize the result around the physical question:

```text
physical question
-> hypotheses and competing explanations
-> numerical credibility and experiment alignment
-> decisive fields, balances, trends, and sensitivities
-> counterevidence and unresolved ambiguity
-> bounded mechanism conclusion
-> smallest falsifiable model or experiment upgrade
```

Include quantitative comparison and uncertainty, but do not reduce the Results section to an error table. Preserve scientifically useful negative results and explain how they constrain the next model without relabeling them as validation success.

### Research deliverable and verification appendix

For an application research report, make the main argument answer the user's
physical question. Establish the usable model scope once, show the relevant
experimental or classical benchmark comparison, then develop operating-case
behavior, field patterns, parameter or closure effects, mechanism interpretation
and physical implications. Use the benchmark that matches the selected
equation/source/observable; a code test cannot establish experimental validity.

Keep nonlinear tolerances, mesh/time/domain matrices, runtime comparisons,
framework-defect history, agent routing and detailed review records in the
methods appendix or reproducibility package unless a numerical finding itself
answers the physical question. Passing checks are a basis for analysis, not the
report's central research result. State a necessary validation limitation where
it changes the claim; do not repeat it after every figure or paragraph.

If a numerically reliable model disagrees with experiment, show the signed
spatial/condition pattern and compare it with the primary paper's actual
baseline and improved treatments. Assign a supported physical repair or
discriminating study to its owner. Do not substitute repeated unchanged checks,
more cells, or a final admission of failure for the next useful investigation.
Conversely, report the remaining mismatch accurately until a corrected model
has been compared with its designated observations.

Prefer controlled mechanism studies over indiscriminate parameter fitting.
When a sensitivity changes two closures together, separate the factors if
their effects matter to the physical question: retain the existing corners,
add only the missing cases at adequate application resolution, and quantify
main effects and interaction from actual solves. Keep real conditions, data
roles and observation definitions fixed. These are model-internal counterfactuals;
they do not identify true properties or establish experimental causality.
Ask the execution role for comparable fields and, where appropriate, balances
over the same spatial region so that changing a diagnostic region does not
masquerade as changing a transport mechanism.

### Scientific presentation contract

Before drawing an application-result figure, the domain/mechanism role must
state one physical question, the decisive comparison, the controlled variables
and the interpretation the figure can support. Map each panel to a distinct
evidence role. A field image, a list of run names or an error table does not
automatically explain a physical response.

Use the discipline's established terms and a consistent symbol/unit dictionary.
Distinguish measured observables from model proxies, instantaneous fields from
material-history envelopes, spatial intervals from elapsed times, conditional
effects from averaged main effects, and model response from experimental
causality. Legends identify scientific methods or physical conditions; internal
revision names and casual labels belong in provenance records.

Select comparisons that make the question answerable: overlaid contours on
shared physical scales for geometry, measured means with their stated intervals
for validation, fixed-condition finite contrasts for operating responses, and
signed component/interaction decompositions for mechanism studies. Preserve
equal physical aspect ratios in geometry panels. State reference denominators
and data roles when normalizing; do not invent covariance or propagate
uncertainty without a justified model. Small or unresolved effects retain their
scale and uncertainty limits instead of being enlarged into a claimed law.

Assign an independent figure/results reviewer to check source values,
terminology, measurement operators, calibration cues, statistical meaning,
visual hierarchy, legends, axes and captions. Inspect actual rendered panels
and the assembled figure at its intended physical size, including fonts,
overlap, clipping, contrast and consistency with the manuscript. Rendering
success or layout checks alone cannot satisfy this review. Correct identified
problems and refresh the same current figures, captions and result index; keep
the underlying scientific source data intact. Provide reproducible plotting
code, source data and editable vector exports with the research package.
