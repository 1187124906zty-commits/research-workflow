# R5 Methods–Results application handoff

Date: 2026-10-02. Complete candidate: `methods-results.tex`, from `Materials and methods` through the end of `Results`. Scope is one substantive forward application of the actual MAF loader-selected method to six retained solutions. No canonical manuscript, shared state, source report or numerical evidence was changed; no PDE solve was run.

## Accepted argument and section purpose

This candidate makes the specific post-calibration object assessable: prescribed above-table conductivity/sensible-specific-heat functions change rear solidus/liquidus positions and their separation, and speed supplies the time interpretation of that separation. The geometric fit, fusion-shape comparison, paired rear-boundary response and material passage time have distinct roles. The result is a constitutive sensitivity/diagnostic account, not a new algorithm, measured liquid-property selection or physical thermal validation.

| Section | Scientific responsibility and outgoing relation |
|---|---|
| Methods opening | Defines the two comparisons and why rear position, separation and time are separate outputs. |
| 2.1 Benchmark observations and comparison design | Gives actual AMMT conditions, the source fraction's power-scaling role, the Gaussian diameter assumption, observation populations and retrospective data roles. |
| 2.2 Moving-frame enthalpy model and high-temperature properties | Defines the conservative balance, fixed phase law, tabulated inputs and exact final-secant/constant-endpoint functions, including consistent primitive/inverse changes. |
| 2.3 Geometry, rear phase boundaries and material passage | Defines the actual model length, maximum-temperature fusion envelope, paired rear crossings and speed transformation; distinguishes surface samples from the y=0 centerline. |
| 2.4 Length calibration and property comparisons at retained source power | Gives the B objective, eta, six-solution union and finite main/conditional/interaction effects. Defines diagnostics whose populations change with the field. |
| 2.5 Numerical solution and verification | Explains how consistent source/material recovery is implemented and what analytical, residual, mesh/domain and historical checks support. Preserves the fine-effect precision limit. |
| 3.1 Geometry discrepancy after length calibration | Answers which dimensions remain discrepant; uses explicit thermographic/metallographic means and separates contextual predecessor curves from internal interventions. |
| 3.2 Property effects on rear-boundary position and separation | Answers whether length differences mainly move the rear pair or change its spacing. Reports unequal local perturbation magnitudes, flux counterevidence, current-mesh cancellation and the sampled temperature maxima. |
| 3.3 Scan speed and derived material passage time | Uses the fixed-power B/C pair to explain why near-equal separation can mean substantially different passage time; A retains its changed-power role. |

## Actual guide use, rather than planned use

Read the complete loader export `instructions/methods-results.md`, which supplied `scientific-writing`, `scientific-editor`, `paper-methods-results` and the compact object/continuity method. Read the requested substantive references in `research-assistant-maf/skills/scientific-writing/references/`: `source-use.md`, `argument-and-readers.md`, `institution-guidance.md`, `object-and-continuity.md`, `chapter-contracts.md`, and the methods/continuity/results responsibilities in `section-specific-guidance.md`. These are editorial methods; they are not citations in the IN625 paper.

Applied them to actual prose in the following ways:

- **Object before name:** replaced an undefined reference with Lane 20 µs thermographic length or NIST 100 µs metallographic width/depth means. eta is introduced by the power etaP that it supplies; final-secant linear extrapolation and constant endpoint extrapolation are defined mathematically before the LL/HL/LH/HH cases are reused.
- **Parameter roles:** separated supplier density/melting range, predecessor latent heat, chosen T0, fixed linear fraction, fitted source factor, numerical mesh/recovery and measured target means. Density is traced to the bulletin, rather than grammatically to its melting range.
- **Relations before connectors:** geometry discrepancy motivates a post-calibration field diagnostic, rather than a claim to fix shape. The two rear crossings locate and delimit one interval; the time equation requires speed in addition to spacing. The joint finite change contains the two contributions and interaction.
- **Evidence responsibilities:** moved the four existing sampled temperature maxima into Results with a Methods definition; retained the rising outward conductive power as counterevidence to a simple lower-k/lower-heat-escape story. Fine interactions retain their current-mesh status.
- **Information placement:** separated numerical adequacy into 2.5, preserving all existing verification values and appendix links. Solver/software detail remains in the existing appendix/reproduction material, while source deposition and material recovery roles remain in main-text Methods.

The scientific source basis is the frozen `revision-r5/sources/report.md` and `source-ledger.json`; earlier actual originals were read in that audit. For the only added result-definition issue, directly read the retained `verification/fipy-application-B-cal-05-r13/frozen-solver-source.py`: `measures()` forms `surface` from material surface recovery, creates `surf_y0` by even extension, and reports `surface_peak_C=float(np.max(surface))`. The checked values are already in `evidence/verified-data.json` factorial rows. This confirms why the positive-y surface-sample maximum must not be renamed as a symmetry-centerline or actual melt-pool peak.

## Source/observation controls that survive in the prose

- AMMT expands to **Additive Manufacturing Metrology Testbed**, as in Lane §1 P2.
- L20 µs populations are 19/10/7 video frames; NIST100 µs microscopy classes contain 3/3/4 tracks. Length and cross sections are not three jointly observed dimensions of one pool.
- Lane combined-class width/depth U remains separately sourced from the actual NIST100 µs target means. Delta/U is descriptive measurement-scale normalization, not a formal uncertainty test or total prediction interval.
- B length alone is in the objective; the benchmark targets were consulted in development. B width/depth and A/C comparisons are retrospective/nonblind. The three other B property cases retain the LL-fitted eta rather than being separately fitted.
- Both tables end below the adopted solidus; interventions begin above their own endpoints and include a solid-temperature interval. k/K/surface inverse and cp/H/T(H) change consistently; latent heat and phase law are retained.
- The supplier-listed melting range is not renamed an equilibrium thermodynamic determination. Coleman supplies the linear-fraction precedent with an explicitly different freezing interval.
- Lane's below-solidus cooling exemplars support the constant-speed mapping, not independent validation of the present 1350–1290 °C time/rate.

## Weakest-relation checks on the actual candidate

| Consequential transition | Plain scientific relation and disposition |
|---|---|
| 2.1 source fraction → geometric calibration | eta scales etaP; B length is the objective. The parameter's physical-sounding name no longer substitutes for its function. |
| 2.2 material endpoint → property intervention | endpoints lie below Ts, so the solution needs an above-table function. The compact equation defines exactly what changes; primitives/recovery preserve consistency. |
| 2.3 length operator → eta interpretation | radiance-profile measurement and two temperature-threshold crossings differ. eta belongs to that adopted source/material/observer combination. |
| 2.3 two positions → separation → time | positions locate the rear interval; subtraction measures extent; division by speed gives stationary-material duration. No liquid-parcel trajectory is inferred. |
| 3.1 shape residual → 3.2 property comparison | length fitting leaves shape unresolved; retained-source property cases diagnose changes in the rear of the fitted field. They are not presented as a successful shape correction. |
| 3.2 length effects → paired rear crossings | front/rear contributions explain length, while paired rear positions distinguish common displacement from separation change. |
| 3.2 k reduction → rising regional power | lower k and greater integrated power coexist because gradients and the selected boundary change. The text preserves the observed increase rather than making a fixed-region causal claim. |
| 3.2 rear location/separation → 3.3 speed/time | the same object, rear separation, enters the next comparison; B/C use their own solved fields and different speeds. The calculation adds time meaning, not an independent validation endpoint. |

No same-object relation remains unresolved for the assigned sections. The residual physical questions remain explicit: which liquid properties are correct; whether rear thermal descriptors agree with measurements; and how omitted source depth/flow/surface/nonequilibrium phase effects contribute to the shape. Those require additional evidence, not more stylistic rewriting.

## Artifact preservation and checks

Compared the candidate against the frozen Methods–Results substring:

- All **8 original equation/align blocks** retained verbatim. Added only the compact property-extrapolation definition, not a new governing equation.
- All **3 table data blocks** from midrule through bottomrule retained verbatim; table/caption names now identify the measurements.
- All **5 figure paths** and original labels retained. No figure file was altered.
- Every original numeric token and citation key remains present; the only additional result values are the already frozen 2697/3507/2756/3721 °C maxima previously reported in Discussion.
- Begin/end environments balance; candidate reference targets resolve against the candidate plus the existing full manuscript. Added labels are `sec:benchmark-design`, `sec:geometry-passage` and `eq:property-extrapolation`.

This is a section fragment intended for integration with the existing preamble, appendix, bibliography and figure directory. TeX compilation and rendered page inspection are the integrator's remaining delivery checks; they were not simulated or claimed here. The candidate currently contains approximately 4,100 whitespace-delimited words including TeX markup, compared with approximately 3,300 in the frozen section; the added space carries formerly implicit object/definition/data-role information and the result now moved from Discussion.

## Adjacent-section handoff and remaining decisions

Directly exchanged the chapter interface with the architecture writer and read their complete `application/introduction.tex`. Its five promised comparisons match this Methods–Results candidate. Their AMMT expansion is authentic and no introduction change is required to accommodate the sampled maxima. The root Discussion/Conclusions candidate uses the same object sequence and terms; integration can shorten repeated peak-value and local-property reporting there now that Results contains those observations.

Keep the current appendix material/table and all existing reproduction details when replacing the canonical Methods–Results substring. The figures' embedded short labels may still use archived L/H labels or older generic measurement legends; the captions now give precise objects. Root should inspect those labels at the rendered-page review and change them only if their terminology creates a material misreading. No numerical or citation gap prevents integration of this complete candidate.
