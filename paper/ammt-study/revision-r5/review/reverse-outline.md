# Frozen R5 manuscript: reverse outline and argument closure

Reviewed input: `manuscript-reviewed.tex` and the corresponding 20-page `manuscript-reviewed.pdf`, frozen for R5 review. Line locators refer to this frozen TeX, not a later canonical revision. This outline records controlling points and reader dependencies; it is not a paragraph quota or a proposed replacement manuscript.

## Directory-level argument

| Frozen line | Section | Work performed for the reader |
|---|---|---|
| 27–29 | Title and abstract | Name geometry, solidification time and property extrapolation; summarize the retained-calibration design, rear-pair displacement and speed-dependent time. |
| 36 | 1. Introduction | Establish why geometric calibration leaves thermal interpretation conditional, identify the actual IN625 input gap, and motivate paired boundaries plus material passage time. |
| 55 | 2. Materials and methods | Define the two comparisons, source/material functions, measurement operators, numerical observers and evidence limits. |
| 59 | 2.1 Benchmark observations and comparison design | Allocate calibration and comparison targets to their actual populations and distinguish retained fraction from applied power. |
| 82 | 2.2 Moving-frame enthalpy model and high-temperature properties | Define the field, phase law, extrapolation interventions, coordinate transport and source/boundary conditions. |
| 131 | 2.3 Geometry, rear phase boundaries and material passage | Define each reported output, including the new surface-sample peak, and establish the space-to-time mapping. |
| 153 | 2.4 Length calibration and property comparisons at retained source power | Define the scalar fit, four B branches, deterministic effects and auxiliary diagnostics. |
| 170 | 2.5 Numerical solution and verification | State execution checks and what the separate numerical comparisons do and do not bound. |
| 181 | 3. Results | Move from post-fit shape discrepancy to property-induced boundary displacement and then to speed-dependent time. |
| 184 | 3.1 Geometry discrepancy after length calibration | Show that length calibration leaves transverse disagreement and an operating-condition response discrepancy. |
| 231 | 3.2 Property effects on rear-boundary position and separation | Quantify conditional effects, locate their rear/front contributions, and distinguish displacement from separation. |
| 279 | 3.3 Scan speed and derived material passage time | Convert B/C separations to time/rate in the respective fields and identify their dependence. |
| 293 | 4. Discussion | Explain the claim boundaries, compare the appropriate prior designs, and identify observations required for physical assessment. |
| 297 | 4.1 Constraints supplied by melt-pool geometry | Explain what a scalar length fit constrains and how the predecessor and Myers designs differ. |
| 304 | 4.2 Effects of property extrapolation on rear phase boundaries | Interpret unequal input perturbations and preserve the conductive-power counterevidence. |
| 311 | 4.3 Solidification interval in material coordinates | Connect position, span and time while separating stationary-material mapping from other measured or fluid paths. |
| 318 | 4.4 Material data and thermal measurements for model assessment | Treat liquid-property laws and alternative deposition/transport as open physical questions; assign observable-specific assessment roles. |
| 327 | 5. Conclusions | Answer the original objective with the shape limitation, rear-pair response and speed-dependent time, within the retained fraction/phase-law scope. |
| 334 | Data and code availability | Identify the manuscript package, original numerical case and source ownership. |
| 337 | AI declaration | Disclose Codex purposes and deterministic plotting; does not attest to human oversight. |
| 341 | Appendix A | Supply material knots, discretization, recovery, calibration, solution acceptance and verification details. |
| 342 | A.1 Material-property inputs | Preserve source knots and mathematical slopes/integration. |
| 376 | A.2 Spatial discretization and observation recovery | Distinguish solved mesh from interpolated observation sampling. |
| 389 | A.3 Scaled enthalpy diffusion and diagnostic definitions | Give the actual discrete coefficient, solver path and selected diagnostic populations. |
| 406 | A.4 Scalar calibration and solution acceptance | Record fit and acceptance thresholds separately from physical adequacy. |
| 413 | A.5 Separate constant-property verification problem | Specify the semi-infinite reference and its limited comparison with a finite-domain numerical problem. |
| 424 | A.6 Calibration record and retained sensitivities | Record local calibration scale, axial sensitivities and descriptive uncertainty normalization. |

## Paragraph-level controlling points

Equation-introducing prose and its immediately attached equation are treated as one unit. Continuations after equations retain their separate line locators where they add an interpretation or limitation. Captions and tables are covered in the object table below.

| Line | Controlling point | Link supplied or dependency |
|---|---|---|
| 29 | The specified property extrapolations alter the calibrated rear field; dominant boundary displacement and speed-dependent passage time are distinct outputs. | Compresses the design and findings without asserting measured thermal accuracy. |
| 39 | Melt extent and solidification thermal conditions supply different information. | Establishes the scientific reason for assessing more than geometry. |
| 41 | Moving-source conduction is practical, and the closest AMMT predecessor makes high-temperature conductivity extrapolation part of calibration. | Takes the reader from general models to a specific material/source dependency. |
| 43 | A geometric fit leaves thermal predictions unresolved; observation operators matter. | Uses the predecessor and Myers as specific support, then returns to AMMT observables. |
| 45 | The current IN625 tables stop below the adopted phase interval and contain typical measured/calculated alloy inputs. | Makes the constitutive gap concrete; avoids treating fitted source power as missing material data. |
| 47 | Sensible-property extrapolation and latent storage are separate choices; alternate phase endpoints exist. | Justifies holding the phase law fixed for this comparison. |
| 49 | Total length combines front/rear locations, whereas the rear pair separates displacement from interval extent. | Introduces the main diagnostic decomposition. |
| 51 | Time also needs speed and a defined material path. | Prepares the passage mapping and its limits. |
| 53 | The study will fit B length, compare geometry at retained fraction, contrast B material functions, and resolve the rear pair/time. | Explicit objective and design contract fulfilled by Results 3.1–3.3. |
| 57 | Two comparisons assess a length-calibrated field. | Correct roadmap, but “retains the B-fitted source power” across operating conditions needs R5-F01 repair. |
| 61 | Conditions and beam convention are specified; only the fitted fraction is retained across A/B/C. | Correct detailed condition statement exposes the L57 inconsistency. |
| 78 | Length and cross-section means come from distinct timing/sampling populations. | Prevents a jointly observed geometry interpretation. |
| 80 | Comparisons are retrospective; only B length is fitted; delta/U is descriptive. | Establishes the nonblind design and uncertainty limits before Results. |
| 83 | Conservative enthalpy separates sensible and latent energy. | Introduces the governing laboratory-frame balance and integral. |
| 89 | Density, adopted thresholds, latent heat and cold reference have named provenance; the phase fraction is linear. | Defines the common phase law rather than importing another paper's interval. |
| 97 | Tabulated inputs have distinct provenance; effective heat capacity includes the retained latent contribution. | Explains why sensible and effective heat-capacity perturbations differ. |
| 99 | Both tables require above-table definitions before the melting interval. | Leads directly to Figure 1 and the extrapolation equation. |
| 108 | L and H are final-secant and endpoint-constant definitions. | Explicit mathematical intervention. |
| 114 | Each intervention updates its primitive/inverse consistently and starts below the adopted solidus. | Defines LL/HL/LH/HH and limits them to numerical scenarios. |
| 116 | The moving-frame coordinate gives a steady conservative balance. | Defines coordinate enthalpy transport. |
| 121 | That transport follows stationary material and includes no liquid momentum. | Prevents flow/residence-time overinterpretation. |
| 123 | A circular Gaussian supplies surface heating. | Provides the source law rather than assuming a measured intensity map. |
| 129 | Its integral is eta P, and the fitted factor is model-conditional; boundary conditions are explicit. | Defines source/energy scope and omissions. |
| 133 | Length is two recovered symmetry-centerline solidus crossings. | Specifies operator, source enclosure and nontruncation. |
| 135 | Width/depth come from the source-connected passage-temperature envelope. | Introduces the fusion observer equation. |
| 140 | Reconstruction/interpolation precede passage maximization; the reported peak uses positive-y surface samples. | Defines observer ordering and separates peak sampling from centerline crossings. |
| 142 | Lane's radiance-feature length differs from the model's two-temperature-crossing length. | Links fitted eta to the actual observational mismatch. |
| 144 | Rear location, separation, passage time and mean cooling rate are explicitly defined. | Gives the central output relations and signs. |
| 151 | Separation/speed follows a fixed laboratory point; Lane's interval and role differ. | States the correct trajectory and rejects false cooling validation. |
| 154 | The B scalar fit and retained A/C parameters are stated. | Final sentence has the same source-fraction/power ambiguity as L57; repair jointly. |
| 156 | Four B cases share power, speed, beam, phase law, mesh and fitted fraction; six total solutions result. | Separates retained-parameter contrasts from refitting. |
| 158 | Finite effects are anchored to LL. | Introduces the effect and interaction algebra. |
| 166 | Conditional effects at the other factor level test directional consistency. | Defines deterministic interaction rather than statistical inference. |
| 168 | Peclet and rear-region power are solution-selected diagnostics. | Prepares the Results counterevidence without a common-boundary causal claim. |
| 171 | The finite-volume method integrates source power and changes material functions consistently. | Explains execution and local/global/correction checks. |
| 173 | A separate constant-property Gaussian comparison verifies selected implementation components. | Restricts the numerical accuracy claim to that problem. |
| 175 | Retained axial/domain sensitivities are small but do not bound every branch/discretization component. | Justifies large responses while preserving fine-scale limitations. |
| 177 | Earlier transient and fixed-field radiation estimates have separate, restricted roles. | Avoids promoting these checks to full physical validation. |
| 179 | All production solutions satisfy specified acceptance criteria. | Closes Methods execution account. |
| 182 | Results will proceed from shape discrepancy to boundary response to passage time. | Matches the Methods/Introduction comparisons. |
| 185 | B length fit leaves width excess and depth deficit. | Uses Table 2/Figure 2 as the first substantive result. |
| 216 | A/C residuals and aspect ratios extend the geometric assessment. | Includes condition-level means and avoids paired-frame interpretation. |
| 218 | At common B/C power, speed produces unequal width/depth contractions. | Restricts the speed comparison to the legitimate pair. |
| 220 | Measured B/C length difference is smaller than the descriptive combined uncertainty scale; numerical axial checks are small. | Limits the sign inference while retaining C's own residual. |
| 229 | Surface contours and transverse envelopes express different operators. | Handoff from unresolved fusion shape to property-induced rear-field changes. |
| 233 | Conductivity and cp interventions have opposing B length effects and a defined joint effect. | Gives branch values and decomposition. |
| 237 | Both directional length effects persist at the other factor level. | Completes the four-case comparison rather than relying on one contrast. |
| 260 | Rear-pair displacement accounts for most conductivity-induced length increase; span changes much less. | Supplies the decisive decomposition promised by the Introduction. |
| 262 | Transport/storage interventions have unequal relative magnitudes at a matched temperature. | Explains why their output effects are not per-unit sensitivities. |
| 264 | Lower conductivity accompanies higher selected-region outward power and changed face populations. | Preserves counterevidence to the simple heat-escape explanation. |
| 266 | Positive-y sample peaks are high and unvalidated under omitted liquid/surface physics. | Uses the new Methods definition faithfully. |
| 268 | Depth contributions oppose, shape discrepancy remains, and fine width interaction is unresolved. | Separates axial response from shape correction and numerical certainty. |
| 277 | The span range is small relative to the length range; fine ordering is a current-mesh result. | Closes the property section with the displacement/extent distinction. |
| 280 | B/C nearly equal spans imply different passage times/rates at different speeds; A changes power too. | Gives the condition-specific numerical time consequence. |
| 282 | Rate is another expression of the same span/speed, not independent evidence. | Prevents counting derived outputs as separate validation. |
| 291 | Fusion contraction and rear-interval passage answer different assessment questions. | Handoff from measured geometry to interpretation of thermal descriptors. |
| 295 | Position, separation and material time describe distinct parts of the response. | Discussion contract grounded in Results. |
| 298 | The scalar fit fixes the modeled input for B length but leaves transverse constraints and conditional absorption meaning. | Interprets Results 3.1 without claiming general source identification. |
| 300 | The predecessor has opposite residual direction and different inputs. | Prevents transferring its mechanism; preserves its relevant calibration lesson. |
| 302 | Myers's alternative fitted parameter sets and this study's retained-factor contrasts answer complementary questions. | Prevents equal-fit/nonuniqueness claims for current branches. |
| 305 | Dominant rear displacement differs from an enlarged phase span or improved shape. | Restates the property result as an interpretation. |
| 307 | Latent heat dilutes the effective cp perturbation; enthalpy is a separate integrated change. | Explains S2 repair and unequal interventions. |
| 309 | Changed region/gradients and surface recovery prevent a simple heat-escape causal attribution. | Proposes two distinct tests; does not claim them executed. |
| 312 | Displacement and separation acquire different time meanings; B/C fields and speeds both differ. | Connects Results 3.2 and 3.3. |
| 314 | Hooper's histories and Lane's below-solidus conversion require aligned operators/intervals for comparison. | Resolves the observation/path reader dependency. |
| 316 | Fluid parcel and transient multi-scan paths require other transport descriptions. | Keeps Hou/Plotkowski conditions and experimental allocation distinct. |
| 319 | Physically choosing extrapolation laws requires appropriate material data and explicit phase law. | Identifies the material question left open by numerical sensitivity. |
| 321 | Deposition and transport alternatives require aligned conditions; correlations do not guarantee agreement. | Uses Coleman/Hong/Soares within their own conditions. |
| 323 | High sample peaks and branch-specific refinement limits restrict physical and numerical interpretation. | Keeps limitations consequential to the reported claims. |
| 325 | Shape, rear profiles and aligned time histories have specific assessment roles. | Closes the argument with evidence appropriate to each output. |
| 328 | Input extrapolation matters and B length fit retains transverse disagreement. | Answers the first objective without adding a new result. |
| 330 | Opposing property effects and rear displacement dominate the joint length increase. | Answers the diagnostic decomposition objective. |
| 332 | Speed explains time/rate differences; retained fraction and phase law define the overall scope. | Closes the spatial/temporal objective. |
| 335 | Package/original-case availability and private-source ownership are stated. | Reproduction navigation; external publication status was not audited here. |
| 338 | Codex uses and deterministic figure generation are disclosed. | Human oversight remains the inherited submission-policy item R4-F05. |
| 374 | Final-secant slopes and analytic enthalpy treatment are specified. | Supports the intervention definition. |
| 377 | Domain and graded mesh are fixed; the solved problem is steady. | Distinguishes warm-start iterations from a transient production model. |
| 379 | Integrated Gaussian power is supplied through top control volumes. | Closes discrete source normalization. |
| 381/385 | Primitive-based surface recovery and even symmetry extension precede crossings. | Specifies observation reconstruction. |
| 387 | Observation pitch refines interpolation sampling, not the field. | Prevents a false resolution claim. |
| 390/395 | Scaled enthalpy, harmonic face coefficient and derivative limit recover conductive flux; production uses Anderson/GMRES. | Gives the actual method, units and selected solve path. |
| 397/402 | Face Peclet uses a specified temperature-selected axial-face population. | Explains why medians can change population between branches. |
| 404 | Rear-region budget cancels internal fluxes but changes region boundary between fields. | Closes the diagnostic's causal limitation. |
| 407 | Safeguarded B secant and retained A/C fraction are specified. | Correct detailed calibration scope. |
| 409 | Local absolute residual, global balance and further correction are separate criteria. | Prevents global cancellation from standing in for local convergence. |
| 411 | Accepted production residuals and corrections are recorded. | Numerical execution evidence only. |
| 414 | Constant-property verification has specified inputs/mesh and truncated boundaries. | Distinguishes its model from production physics. |
| 416 | The semi-infinite Gaussian reference is locally constructed from a Neumann heat kernel. | Cites the moving-source framework without attributing current derivation verbatim. |
| 422 | Quadrature transformation and geometry observer are problem-specific; errors do not bound production physical/numerical error. | Limits the verification result. |
| 425 | Fit trials and local eta scale do not establish global identifiability/posterior uncertainty. | Preserves calibration evidence scope. |
| 439 | Published uncertainty scales and full-precision contrasts are used descriptively. | Closes population/statistics and rounding interpretation. |

## Objects that carry the argument

| Object | Definition / source | Main use and result |
|---|---|---|
| Table 1, L65 | P, v, eta P/v and w/v under actual A/B/C conditions | Exposes why A is not a fixed-power speed experiment. |
| Figure 1, L104 | Actual knots, endpoint definitions, phase band, sensible-versus-latent distinction | Visual definition of the material interventions; full source ranges are stated despite the display crop. |
| Table 2 / Figure 2, L188/L212 | Current model dimensions; separate length and cross-section populations; contextual published models | Establish post-fit shape disagreement without a single-factor ranking or formal joint test. |
| Figure 3, L225 | Recovered surface contours and passage fusion envelopes | Distinguish spatial boundary operators; show B/C penetration contraction. |
| Table 3 / Figure 4, L241/L273 | Common-source B branches and LL-anchored finite effects; original rear profiles | Support opposing effects, rear displacement and depth cancellation. |
| Figure 5, L287 | B/C percent changes, class-mean aspect ratios, phase spans and derived times | Link geometry, spatial interval and speed; uncertainty is not propagated. |
| Appendix property table, L345 | Two independently tabulated temperature columns | Preserve the actual material input rather than a fitted curve proxy. |
| Appendix sensitivity table, L428 | Calibrated B/C axial refinement only | Bound the inspected component, not all branch errors. |
| Eqs. 1–5 | Enthalpy, phase law, extrapolations, moving frame and Gaussian | Define the solved model. |
| Eqs. 6–9 | Passage envelope, rear span/time/rate and finite effects | Define the reported scientific distinctions. |
| Eq. 10 | Joint length decomposition | Displays the finite-response arithmetic. |
| Eqs. A.1–A.4 | Recovery, face diffusion/Peclet and reference kernel | Supply method/verification details without changing claim scope. |

## Closure assessment

The chain closes: the Introduction's conditional thermal-information question produces explicit Methods operators and interventions; Results quantify their specified responses; Discussion separates numerical response from physical selection and aligns the needed measurements; Conclusions and abstract report the same bounded outcome. The main reader defect is the source-power/fraction recurrence at L57 and the final sentence of L154, recorded as R5-F01 in the independent review. No rearrangement of sections or paragraph count is needed to fix it.

The contribution is the particular rear-boundary interpretation of retained conduction solutions. It does not require claiming a new solver, first proof of geometry/temperature ambiguity, liquid-property identification, equal refits, or validated grain prediction. Those stronger claims remain outside this outline and are not demands for accepting the assigned bounded revision.

The coordinator subsequently repaired R5-F01 and the source specialist's L300/L309 points in the canonical manuscript. This outline continues to describe the frozen review input; the single concrete repair recheck and final disposition are recorded at the end of `independent-review.md`.
