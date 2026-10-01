# Methods/Results argument and paragraph roles

Contracted question: how does one-target geometric agreement relate to uncalibrated fusion shape, sensitivity to missing high-temperature material data, and material passage time in this retained AMMT conduction model?

The section spine is **fit one length → inspect excluded geometry → independently change k/storage continuation at fixed source → locate the rear threshold response → distinguish spatial interval from scan-speed-transformed time**. Each transition asks a scientific question. Solver/provenance details support reproducibility and must not displace that question.

## Methods paragraph-level roles

| Candidate location/topic | Paragraph role and question answered | Evidence/reader obligation |
|---|---|---|
| Study-design opening |Explain the purpose of all five stages and why no single geometry fit answers the full question|Do not lead with agent workflow or software lineage|
| Bare-plate conditions and beam |Specify the experimental referent and controlled B/C speed change|Tableconditions; Gaussian reconstructs D4σ, not measured2D beam map|
| Referent populations |Explain why length and W/D are separate condition-level observations|Lane length; current NIST100 μs W/D; no joint3D track claim|
| Calibration/data roles |Identify B L objective, excluded W/D, A/C nonblind comparison, descriptive U scale|δ/U has no significance or combined-uncertainty interpretation|
| H and phase law |Define stored energy, latent interval and actual material assumptions|Full table appendix; endpoints982/1093; supplier calculated/measured distinction|
| Moving-frame conservation |Identify coordinate material passage and absent melt mechanics|Equationframe; avoid reading u as a liquid velocity|
| Gaussian/boundaries |Give inward source sign, integrated power and inflow/outflow closure|FullηP/halfηP2 power check; adiabatic omissions|
| Mesh and scaled enthalpy |Specify the solved discrete problem and why U is not T|Mesh199×56×81; face secant and derivative fallback; warm guesses are steady nonlinear initialization|
| Solver acceptance |Separate nonlinear gates and scientific adequacy|Fresh stencils; local/global residual distinction; detailed controls in appendix|
| Surface and fusion operators |Explain how L differs from W/D and why observation order matters|Surface primitive and symmetry; interpolate slice before passage max|
| Experimental operator difference |Define why fitted η is effective rather than measured absorption|Solidus proxy is not radiance replay|
| Rear history mapping |Define spatial span, passage time and interval rate|Equationpassage; all from same steady field|
| Calibration bracket |Disclose scalar fit and local sensitivity only|No posterior, global identifiability or propagated interval claim|
| L/H factorial |State ranges affected, consistent branch functions, four corners, no refit|Executed wrapper; one B shared so six production runs|
| Contrast algebra |Define baseline and conditional effects, interaction and joint|Deterministic finite contrasts; signs checked at both levels|
| Pe/selected-region budget |State what is selected and how it can change across branches|Local discretization diagnostic and changing rear hot set, not measured liquid transport|
| Numerical evidence |Explain which comparisons retained checks can support|Constant-property benchmark; axial/domain sensitivity; limited transient/loss checks|
| Reproducibility close |Identify concrete retained objects required to re-extract results|Executed snapshots, manifests, arrays, histories and primary observer|

## Results paragraph-level roles

| Candidate location/topic | Main statement | Evidence and inferential limit |
|---|---|---|
| Length-fit opening and geometry table |B length agrees by construction while B W/D retain discrepancy|B W+19.54,D−4.88 μm; δ/U descriptive|
| Comparisonfigure uptake |A is closer on reported scales; C is short/wide/shallow|Condition means and separate U; W/D ratios are class-mean ratios|
| B/C contraction paragraph |Fixed-power speed change reveals relative depth/width contraction mismatch|ModelW−9.78%,D−29.16%; referenceW−14.17%,D−17.78%; modelW/D+27.36%|
| Length-trend qualification |An11 μm nominal experimental rise does not establish a resolved opposite trend|Separate expanded uncertainties; C individual residual is still−49.37 μm|
| Geometryfield uptake |Surface length and passage fusion envelope answer different questions|Common physical axes; no microscopy or flow-map implication|
| Spatial/time subsection opening |Similar B/C spans coexist with substantially shorter C material interval|s0.66% higher,τ32.90% lower,rate49.02% higher; speed relation|
| History interpretation |Mapping does not independently validate cooling or microstructure|Centerline-equilibrium phase law; same steady solution|
| Trendsfigure uptake |Separate fusion-shape change from material passage-time change|Rate discussed but not plotted; no uncertainty propagation|
| Factorial opening and table |k/cp hold responses oppose and LL/HH hides this|Length+43.21−6.17−2.76=+34.28 μm; same directions at other level|
| Rear threshold paragraph |Length response is chiefly rear translation|98.3% rear solidus share; both thresholds move≈43 μm while span≈1 μm; small spans descriptive|
| Matched-property/Pe/counterevidence |Latent term moderates local storage contrast; local transport balance changes|At1320 values; Pe4.44→5.77; outward diffusion14.724→14.913 W prevents simple total-heat-loss explanation|
| Depth paragraph |Small joint depth change conceals cancellation and does not repair B shape|−1.03+0.49+0.21=−0.32 μm; all corners remain wide/shallow; no fine physical ranking|
| Factorialfigure uptake |Rear interval moves more than it widens|Span79.25–81.17 versusL352.99–402.37 μm; preserves current-mesh boundary|

## Interfaces for subsequent sections

Introduction must motivate incomplete material data and non-identifying scalar agreement from literature and the question, not infer novelty from agent/software execution. Discussion can interpret the opposing closure contrasts and rear translations, while preserving the counterevidence and changing selection. Abstract/Conclusion can state the robustwithin-model length contrast, excluded geometry residual and spatial/time distinction. They must not promote the1 μm span response, identify actual liquid transport, or claim independent cooling validation.

The property figure should be introduced when the material tables and actual endpoints are first stated. It establishes what is data-supported interpolation and what is assumed continuation. It is not an extra result from a PDE run. The appendix should contain the full27 knots and detailed nonlinear controls; duplicate slopes and Pe definitions already present in the old appendix should be consolidated during root-owned integration.
