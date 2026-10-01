# Methods and Results evidence audit, revision R2

Date: 2026-10-01. Specialist: section_runtime_diagnosis. Contract: audit the existing methods, quantities and four figures against the original executed AMMT case; produce complete Methods/Results candidates and a property-continuation figure. The source case remains read-only. There are **zero new PDE runs**. The scientific ceiling is retained-output reproducibility and deterministic comparison inside the stated conduction model.

## Disposition

No consequential mismatch was found between the six retained production identities, the reported material tables, the primary geometry operator and the values used by the manuscript. The candidates therefore retain the numerical results and repair the account of what those results mean. They are ready for the coordinator's MAF drafting and targeted peer review. They are not promoted to the canonical manuscript by this specialist.

The strongest supported inference is that the two implemented high-temperature continuation choices produce opposing rear-tail responses under a fixed calibrated source. Both conditional conductivity contrasts lengthen the model pool, and both conditional storage contrasts shorten it. The small joint depth difference conceals cancellation. Neither this factorial nor one-target calibration identifies the physical high-temperature properties or the omitted melt-flow mechanism.

## Sources and executed implementation

All case paths in this section are relative to `C:/Users/Administrator/Documents/ChatGPT/电脑答疑/simulation-agent-mvp/research/reproduction-case/nist-amb2018-02`. The manuscript's frozen extraction is `evidence/verified-data.json` under the AMMT paper root. The new independent checks are recorded in `computed-audit.json` beside this audit.

| Evidence or implementation | Original locator | Audit interpretation |
|---|---|---|
| Actual table loading, enthalpy/inverse, conductivity primitive | `solver/native_fv_enthalpy.py:85` (CSV read at 89; phase knots at 110; primitive at 122; surface inverse at 147) | The executed input ends at 982 °C for k and 1093 °C for cp. The 871 °C point is a preceding k knot, not its endpoint. |
| Production mesh, boundary and Gaussian source | `verification/fipy-application-B-cal-05-r13/frozen-solver-source.py:327` (boundaries 356; top input 362) | The 199×56×81 half-domain and integrated surface Gaussian are the solved problem. |
| Fresh stencil terms and actual face map | Same executed snapshot at 373 and 523 | Secant coefficients use a derivative fallback for |ΔU|≤1e−8 K; recreating terms avoids cached initial convection weights. |
| Surface/symmetry recovery | Same executed snapshot at 187 | The top value is recovered through the conductivity primitive; even symmetry extension precedes extraction. |
| Mixed-branch consistency | `verification/fipy-application-B-khold-cplinear-r15/frozen-factorial-wrapper.py:28` | k, K and surface inverse follow the conductivity factor; cp, H and T(H) follow storage. Mixed corners are internally consistent. |
| Primary fusion observer | `solver/passage_observer.py:13` | Restore each ξ slice, interpolate it, then maximize over ξ. Stored `yz_Tmax_C` is an older nodal-max proxy and is not substituted for primary W/D. |
| Face Pe selection | `collaboration/analyze_fipy_r8_flux_native61.py:26` | Unweighted percentiles on internal axial faces adjacent to at least one mushy cell; face population changes with the solution. |
| Rear hot-cell budget | `collaboration/analyze_phase_budgets_native61.py:43` (selection45; boundary signs48) | Rear set is T≥1290 °C and x<0; signed outward diffusive powers sum over its boundary. This is a changing selected region. |
| Four retained figure renderers | `solver/redraw_research_figures.py:138`, `:178`, `:223`, `:289` | Comparison, geometry, trends and factorial retain the correct observation/data roles. |

`audit_extract.py` loads the original manifests, results and saved fields. It imports only the pure saved-field passage observer, with no solver or simulation driver import. Hash checks are used once per distinct dependency to test the immutable executed-source bindings, not as a substitute for numerical validation. Every executed snapshot/dependency binding inspected here matches its manifest.

## Actual material knots and continuation rules

The complete 27 rows are supplied in `appendix-methods.tex`, `property-table-source-data.csv` and `computed-audit.json`. k pairs (°C, W m−1 K−1) are: (−157,7.2), (−129,7.5), (−73,8.4), (−18,9.2), (21,9.8), (38,10.1), (93,10.8), (204,12.5), (316,14.1), (427,15.7), (538,17.5), (649,19.0), (760,20.8), (871,22.8), (982,25.2). cp pairs (°C, J kg−1 K−1) are: (−18,402), (21,410), (93,427), (204,456), (316,481), (427,511), (538,536), (649,565), (760,590), (871,620), (982,645), (1093,670).

Both tables use piecewise linear interpolation. Above the final knot, L continues the final secant, 0.0216216216 W m−1 K−2 for k and 0.2252252252 J kg−1 K−2 for cp; H holds 25.2 and 670 respectively. These changes begin below the solidus and affect every modeled mushy/liquid state. The supplier describes cp as calculated and k as measured typical data. They are not coupon-specific measurements, and neither extrapolation is a measured liquid-property law.

ρ=8440 kg m−3, latent heat=280000 J kg−1, T0=25 °C, Ts=1290 °C, Tl=1350 °C. The linear phase fraction contributes 4666.6667 J kg−1 K−1 to effective cp over the 60 K interval. The property figure plots sensible cp so that the much larger latent term is stated separately, not hidden in the panel scale.

## Equations, source, boundaries and solver

The laboratory conduction equation is ∂H/∂t=∇·(k∇T), H=ρ[∫cp dT+ℒf]. With ξ=x−vt and u=(−v,0,0), the steady equation is ∇·(uH−k∇T)=0. This coordinate transport is material passage, not liquid velocity. Momentum, melt convection, evaporation and free-surface deformation are absent. With the outward normal at the top, −k∇T·n=−q expresses inward Gaussian heating; the candidate makes the sign explicit.

The source q=2ηP/(πw²) exp[−2(ξ²+y²)/w²] uses w=85 μm and η=0.2890548519203547. Rectangle integration uses erf; the half-domain powers independently sum to 19.930332 W for A and 25.899315 W for B/C and every B corner. Positive-ξ inflow is cold H=0; negative-ξ outflow has zero diffusive gradient and coordinate enthalpy exit. The symmetry plane, outer transverse face and bottom are adiabatic. Radiation and ambient convection are omitted from the solved balance.

The domain is [−1,0.35]×[0,0.36]×[−0.30,0] mm; 902664 cells have a 4×3×1 μm core, grading 1.22 and maximum width25 μm. The solver uses scaled enthalpy U=H/C0 with C0=3.39288e6 J m−3 K−1. The actual face coefficient is (kf/C0)(ΔT/ΔU), with harmonic kf and the positive derivative limit at near-equal U. Its units are m² s−1. FiPy exponential coordinate convection, SciPy Anderson acceleration, GMRES and Ruge–Stuben AMG are described in Methods; implementation controls are in the appendix candidate. Warm fields are nonlinear guesses for a steady problem, not a transient initial condition.

Recorded final residuals satisfy the stated nonlinear gates: normalized absolute residual sums 6.90e−8–1.31e−7, signed global magnitudes below6.1e−11, and full-solve temperature corrections below2.7e−5 °C. These are convergence records, not a physical-model accuracy certificate.

## Calibration and experimental populations

B length359 μm is the only objective; fitted model length359.157546 μm has +0.158 μm residual. B W/D are excluded from the fit. A/C retain η and are retrospective, nonblind condition comparisons, because the public targets were available during development. The safeguarded bracket, retained trials and local sensitivity are disclosed without implying global identifiability or a Bayesian posterior.

Length means come from Lane's imaging analysis. Current decimal W/D means come from the NIST100 μs-track classes; Lane's width/depth uncertainty budgets combine 100 and20 μs tracks. Thus Lane U(k=2) is used as a separate descriptive measurement scale. δ/U is not statistical significance, combined numerical/experimental uncertainty, or a joint uncertainty analysis for the decimal means. Six production solutions are numerical cases, not experimental replicates. Published isotropic/effective-anisotropic calculations are contextual because their beam, phase, calibration and operators differ.

## Quantities checked from saved outputs

All six temperature fields are finite, phase fractions are bounded0–1, and the threshold intervals are qualified. Primary passage W/D values reproduce the original recorded values to below1e−9 μm using the same observer ROI. Source power, surface centerline Ts/Tl crossings, L, rear span and passage mapping were recomputed from retained arrays. This is an independent data extraction; it does not rerun the PDE.

| Case | L (μm) | W (μm) | D (μm) | Rear span (μm) | Passage (μs) |
|---|---:|---:|---:|---:|---:|
| A |309.885679|153.360053|40.469312|48.295190|120.737976|
| B=LL |359.157546|143.040623|31.120350|80.264026|100.330033|
| C |320.631363|129.046187|22.044541|80.791403|67.326169|
| HL |402.371258|143.150074|30.092012|79.250883|99.063604|
| LH |352.988688|143.716221|31.613427|80.570929|100.713661|
| HH |393.440458|143.786918|30.797065|81.169862|101.462328|

The displayed precision supports reproduction of arithmetic, not physical certainty to six decimals. The manuscript rounds appropriately and qualifies small effects.

| Verified comparison | Result | Claim boundary |
|---|---:|---|
| Conductivity L contrast, cpL / cpH |+43.213712 / +40.451770 μm|Same sign at both factor levels within the stated model|
| Storage L contrast, kL / kH |−6.168858 / −8.930800 μm|Same sign at both factor levels within the stated model|
| L interaction / joint |−2.761942 / +34.282913 μm|Finite deterministic contrast, not a statistical estimate|
| Rear solidus share of baseline k length response |98.318997%|Tail translation dominates the chosen length proxy|
| Rear span joint change |+0.905836 μm|Current-mesh descriptive result; no branch-specific precision proof|
| Conductivity D contrast, cpL / cpH |−1.028337 / −0.816362 μm|Arithmetic direction persists, without fine physical ranking|
| Storage D contrast, kL / kH |+0.493077 / +0.705053 μm|Current-mesh cancellation account|
| Width interaction |−0.038755 μm|Do not interpret as a resolved effect|
| C versus B rear span / passage / cooling rate |+0.657052% / −32.895298% / +49.020855%|Coordinate mapping of one steady field and speed; no independent cooling validation|
| C versus B model W/D |+27.358867%|Aspect ratios of model geometry and separate class means have different observation status|
| At1320 °C held k / sensible cp / effective cp / H |−22.480878% / −7.089762% / −0.948925% / −0.661984%|Matched-temperature illustration at one mushy temperature, not a universal ratio|
| Rear selected-region diffusive power, HL−LL |+0.189344 W|14.723959→14.913303 W contradicts equating held k with reduced total outward diffusion|

The Pe medians4.44→5.77 are consistent with changed coordinate transport/diffusion balance; this remains a local discretization and selected-population diagnostic. A conductivity change also changes temperature gradients, region boundaries and surface recovery. The present evidence does not isolate which of those explains the rear shift physically.

## Figure-by-figure audit

| Figure and candidate label | Source/operation | What the reader can infer | Qualification retained or added |
|---|---|---|---|
| `ammt-application-experiment.pdf`, fig:comparison |Condition model geometry, NIST class means, Lane uncertainty scales, published model points; renderer at138|Length fit leaves W/D discrepancy, especially B/C|B L is fitted; U populations differ; published points are not a controlled solver ranking|
| `ammt-research-operating-cases.pdf`, fig:fields |Surface centerline/symmetry recovery and primary per-slice passage fusion envelope; renderer at178|Relative transverse/depth contraction across conditions|Equal physical axes; model output, not microscopy or flow map; two geometric operators differ|
| `ammt-research-condition-trends.pdf`, fig:trends |B/C changes, class-mean ratios, centerline rear spans, spans/speed; renderer at223|Spatial phase interval and material time can change differently|A/B also changes power; no propagated uncertainty; histories are not independent validation observables; cooling rate is discussed, not plotted|
| `ammt-research-constitutive-factorial.pdf`, fig:factorial |Saved four-corner centerline profiles, matched thresholds and arithmetic effects; renderer at289|Rear translation and opposing k/cp effects|No recalibration; source clipping preserves original segments; submicrometre orderings remain descriptive|
| New `ammt-property-continuations.pdf`, fig:properties suggested |Actual27 knots, common interpolation, L final secant and H final value; `plot_properties.py`|Where data end and missing-range assumptions begin|Display25–2200 °C retains all original rows in source data, including sub25 °C interpolation input; latent term is stated separately; no PDE or copied published plot|

## Numerical adequacy and unsupported extensions

Retained B/C4→2 μm axial refinements change L by0.361/0.199 μm and W/D by at most0.045 μm. A/B domain enlargements change reported geometry by less than3e−6 μm. A simpler constant-property analytical comparison has sub0.5% geometry differences. These support the large residual and34–43 μm length comparisons but do not provide a branch-specific three-dimensional error bound. Older transient evidence is at another calibration stage. Fixed-field blackbody loss screening0.099–0.180% does not solve loss feedback.

Do not promote these outputs to validated liquid temperatures, resolved one-micrometre phase-span changes, unique omitted-flow attribution, statistically established experimental length-trend reversal, or a new transport solver. The ~1 μm values and width interaction remain numerically descriptive. No new PDE is necessary for the current bounded claim set; stronger physical or small-effect claims would need distinct evidence.

## Delivery and integration

Full replacements: `section-methods.tex` and `section-results.tex`, with `.diff` files. Appendix addition: `appendix-methods.tex`. New property figure and source data: PDF/SVG/PNG, script, two CSVs and figure contract. Editorial/argument memory: `memory.md`, `argument.md`, `interfaces.md`. The property insertion snippet is `property-figure-caption.tex`; the coordinator copies the figure into canonical `figures/` and resolves placement. No original evidence, SimAgent source, skill, or canonical manuscript is changed here. This round's independent preview TeX/PDF/auxiliary files were removed as instructed; do not recreate them. Final canonical compilation belongs to the coordinator.
