# R5 source and object audit

Date: 2026-10-02. Contract: source-dependent decisions for the frozen `revision-r5/manuscript-input.tex`; six existing production solutions, one B-length calibration, no new algorithm or physical model. This report does not edit the manuscript or shared research state. It is an evidence memo, not a candidate manuscript section.

## Decision that can be carried into the shared argument

The strongest predecessor is the **specific AMMT model limitation identified by Kollmannsberger et al.**, not the general proposition that geometry and temperature can disagree. Their measured-beam isotropic calculation had insufficient freedom to fit three geometric dimensions with one remaining absorptivity parameter; their high-temperature conductivity was itself an extrapolated, calibrated model; even their improved anisotropic model was explicitly not intended to predict the temperature distribution inside the pool. Myers et al. subsequently demonstrated the geometric/thermal ambiguity experimentally in a different material and a CFD model. The present paper cannot claim to discover that ambiguity.

The defensible question is: **after fitting the effective source power to B's thermographic mean length, how do explicit definitions of conductivity and sensible heat capacity beyond their tabulated ranges change rear solidus/liquidus positions, their separation, and the material cooling-interval passage time?** Length alone combines boundary positions. Reporting the two rear positions and their separation assigns a more specific thermal meaning to the length response. The unchanged-source four cases answer a constitutive sensitivity question; they do not establish multiple equally length-fitted solutions.

中文论证核心：已有AMMT导热模型已经表明，实测光斑约束下单一吸收率不能同时拟合熔池三维形状，而高温导热率的外推又参与了校准。现有两色测温研究进一步证明几何吻合并不充分约束温度场。本研究的具体推进是：在B工况长度标定和相变规律固定后，明确表外导热率/显热比热的数学定义，辨别熔池后部固相线、液相线整体移位与两者间距变化，并量化该空间间距在给定扫描速度下对应的通过时间。它是对标定后热解释的具体诊断，不是新的热传导算法或物性测量。

No exhaustive novelty claim is supported by this bounded audit. The selected originals establish the scientific need and neighboring solutions, but do not prove that no publication has ever resolved paired rear isotherms.

## Originals and bibliographic identity

All page numbers below are **PDF page numbers** unless an HTML section/paragraph/table is identified. Author manuscripts/preprints are full-text sources for the quoted methods, not evidence of final publisher typography. Metadata was independently checked against Crossref and the source title/author block. Three Crossref records were retrieved on 2026-10-02; the two requests returning HTTP 429 were verified using the already archived successful Crossref records, rather than silently treating the failed requests as verification.

| Key | Verified published identity | Actual original read here |
|---|---|---|
| `vanelsen2007` | M. Van Elsen, M. Baelmans, P. Mercelis, J.-P. Kruth. *Solutions for modelling moving heat sources in a semi-infinite medium and applications to laser material processing*. International Journal of Heat and Mass Transfer 50 (2007), 4872–4882. DOI [10.1016/j.ijheatmasstransfer.2007.02.044](https://doi.org/10.1016/j.ijheatmasstransfer.2007.02.044). | 26-page author preprint dated 20 February 2006; pp1,4–5,20–24. Publication year is 2007. |
| `kollmannsberger2019` | Stefan Kollmannsberger, Massimo Carraturo, Alessandro Reali, Ferdinando Auricchio. *Accurate Prediction of Melt Pool Shapes in Laser Powder Bed Fusion by the Non-Linear Temperature Equation Including Phase Changes*. Integrating Materials and Manufacturing Innovation 8 (2019), 167–177. DOI [10.1007/s40192-019-00132-9](https://doi.org/10.1007/s40192-019-00132-9). | arXiv:1903.09076v1, 13 pages; pp1,3–6,9–11. The preprint adds the subtitle “Model validity: isotropic versus anisotropic conductivity”; it is not part of Crossref's published title. |
| `lane2020` | Brandon Lane, Jarred Heigel, Richard Ricker, Ivan Zhirnov, Vladimir Khromschenko, Jordan Weaver, Thien Phan, Mark Stoudt, Sergey Mekhontsev, Lyle Levine. *Measurements of Melt Pool Geometry and Cooling Rates of Individual Laser Traces on IN625 Bare Plates*. Integrating Materials and Manufacturing Innovation 9 (2020), 16–30. DOI [10.1007/s40192-020-00169-1](https://doi.org/10.1007/s40192-020-00169-1). | Fresh [PMC8194244](https://pmc.ncbi.nlm.nih.gov/articles/PMC8194244/) complete author-manuscript HTML, §§2–5, Tables1–7. Header explicitly says “Author manuscript; available in PMC: 2021 Jun 11.” R3's label “Full published HTML” should be corrected. Paragraph IDs remain compatible with the existing extract. |
| `myers2023` | Alexander J. Myers, Guadalupe Quirarte, Francis Ogoke, Brandon M. Lane, Syed Zia Uddin, Amir Barati Farimani, Jack L. Beuth, Jonathan A. Malen. *High-resolution melt pool thermal imaging for metals additive manufacturing using the two-color method with a color camera*. Additive Manufacturing 73 (2023), 103663. DOI [10.1016/j.addma.2023.103663](https://doi.org/10.1016/j.addma.2023.103663). | 11-page version of record; pp1–2,7–9, including §4.1 and Fig.8. |
| `dynamic2024` | John Coleman, Gerald L. Knapp, Benjamin Stump, Matt Rolchigo, Kellis Kincaid, Alex Plotkowski. *A dynamic volumetric heat source model for laser additive manufacturing*. Additive Manufacturing 95 (2024), 104531. DOI [10.1016/j.addma.2024.104531](https://doi.org/10.1016/j.addma.2024.104531). | 45-page author manuscript; pp1–13,17–20,30–32,36–37. The author manuscript prints “Gerry L. Knapp”; Crossref's published author is “Gerald L. Knapp.” |
| `specialmetals625` | Special Metals Corporation. *INCONEL alloy 625*, August 2013 bulletin, copyright 2013. [Official bulletin](https://www.specialmetals.com/documents/technical-bulletins/inconel/inconel-alloy-625.pdf). No DOI. | Original 18-page supplier PDF; pp1–2,18. Page2 Tables2–3 and footnotes also visually inspected. |
| auxiliary `nist2018` | NIST, *CHAL-AMB2018-02-MP-xsection: Melt Pool Geometry—Width and Depth*, original challenge created 2018, page updated 2025. [Official page](https://www.nist.gov/ambench/chal-amb2018-02-mp-xsection). | Existing local original HTML/text, overview and Table2; needed to identify the actual current width/depth targets. It is separate from Lane's compiled Table4. |

## Historical research line and concrete source facts

### 1. Moving-source/enthalpy foundation: Van Elsen

- **Method:** pp4–5, §2, Eqs(1)–(4) formulate a moving-source coordinate description, conductive energy balance and constant-speed steady problem. The mathematical transport term can arise from choosing the source frame. It does not by itself demonstrate liquid circulation.
- **Enthalpy role:** p21, Eqs(31)–(35), says the source-based and enthalpy approaches conserve energy; the enthalpy implementation was more stable in their comparison. Locator phrase: “Both are conservative ways to introduce the latent heat.”
- **Phase assumption:** pp21–22, Eqs(36)–(38), distribute latent heat as a Gaussian in temperature and integrate it into enthalpy. This is not the present piecewise-linear liquid fraction. Cite the source for the conservative enthalpy foundation, and cite Coleman separately for a linear fraction precedent.
- **Relevant earlier result:** p22, Fig.7 discussion: their demonstration changes the rear temperature profile most strongly, while the peak is unchanged. But it uses a deliberately tenfold latent heat (2,920,000 J/kg), a Ti alloy example, low power/speed and constant properties. It supports the need to inspect the rear profile; it does not prove the current conductivity mechanism or magnitude.
- **Condition limit:** pp23–24 conclude a small latent-heat effect for their TiAl6V4 cases except low conductivity such as a loose powder bed. Do not transplant “latent heat is small” to IN625 or interpret the current sensible-property perturbation as a latent-heat test.

### 2. Closest AMMT predecessor: Kollmannsberger

- **Material/source coupling:** p4, §4, explicitly identifies limited high-temperature knowledge of absorptivity, emissivity, conductivity and heat capacity as the reason for calibration. p6, §4.2, says their conductivity is available only to **871 °C** and states: “this extrapolation itself represents a physical model which, in turn, needs to be calibrated.” This is the strongest direct motivation for making the present extrapolation functions explicit.
- **Source:** p4, §2.2, first uses a Goldak double-ellipse, then directly applies a measured laser profile. p9 notes that the measured profile removes the front/rear power and radius-ratio freedoms; with negligible emissivity sensitivity, only scalar absorptivity remains. Their AMMT scalar is **η=0.086**, under their own source/material/phase description.
- **Concrete inadequacy:** p9, Tables7–8 and paragraph ending “one parameter to calibrate but three values of interest to fit”: L/W/D are A=301/119/52, B=360/103/42, C=348/91/32 μm. Length is much closer than width/depth, which show approximately 10–20% errors. This is a specific constraint deficiency, not an abstract statement about calibration.
- **Competing remedy:** p9, §4.3, increases transport anisotropically above their final measured k temperature, using θx=1.0, θy=1.4, θz=0.9. They intend the tensor as a simplified representation of unmodeled convection. p10, Tables9–10: the fixed values improve A/C shapes; maximum geometric deviation is 6.49%.
- **Thermal claim ceiling:** p10, last sentence of §5: “it is not valid to predict the temperature distribution within the melt pool.” The current study should respond by explaining what its calculated rear descriptors mean under the stated model, not by claiming to repair this temperature validation problem.
- **Counterevidence that must remain:** their isotropic calculation is **narrower and deeper** than their benchmark means; the present model is **wider and shallower**. Neither the sign nor the mechanism of the present shape discrepancy can be claimed as a replication of their residual. Their input k endpoint 871 °C differs from the current bulletin's 982 °C. Their smooth phase law includes a calibrated parameter S (p3), whereas the present phase law is linear with fixed thresholds. η values and geometric discrepancies are not directly exchangeable across these models.

### 3. Observation definitions and populations: Lane

- **Beam identity:** §2.1 P6/Table1 gives measured AMMT D4σ=170 μm and FWHM=100 μm. The current circular Gaussian w=85 μm matches this second-moment diameter; it does not reproduce the measured 2D intensity map.
- **Length measurand:** §2.3 P15,P27–P31 identifies rear freezing using the second-derivative minimum of a radiance-temperature profile. The front is obtained by crossing the freezing temperature after emittance-based conversion. The current two-solidus-crossing temperature length is a model-defined counterpart, not the same observation operator.
- **Thermal assumptions:** P16–P18 use an assumed freezing temperature 1290 °C; P17 notes nonequilibrium undercooling. P34 says the temperature assumption changes cooling-rate estimates more than length. Do not describe this thermography as direct measurement of two physical phase boundaries.
- **Population:** §3 P38/Table3 defines N for thermography as video frames; microscopy N is measurements per track. Table4's length caption excludes AMMT-100 μs length and includes only AMMT-20 μs. Its microscopy caption says width/depth incorporate both 100 and 20 μs classes; P40 explains this compilation. The actual NIST challenge width/depth means used in this manuscript come from the 100 μs specimen (P36,P70).
- **Uncertainty:** §4/Table5 supplies the 20 μs length expanded uncertainties; Tables6–7 use the compiled microscopy analysis. P68 explicitly uses coverage factor k=2. The denominator is measurement uncertainty, not total model discrepancy uncertainty.
- **Negative validation result:** §3 P42 and §5 P69–P70 explicitly advise that cooling rates are exemplars and should not be used for model reference/calibration. The present 1350–1290 °C interval is also different from their 1290–1190 °C cooling interval (P32–P33). Lane supports the constant-speed spatial/time conversion, not independent validation of the present solidification time or cooling rate.
- **Operating regime:** §2.4 P36 classifies these AMMT sections as conduction-mode tracks; the smaller-spot CBM B/C sections show keyhole/transition shapes. Do not motivate a need for keyhole physics by relabeling the present AMMT benchmark.

### 4. Geometric ambiguity already demonstrated: Myers

- **Full-text fact:** p7, §4.1, fits Fresnel and accommodation coefficients simultaneously to **six no-powder 316L** power/speed cases using cross-sectional area and width-to-depth ratio. The former controls angle-dependent laser absorption, the latter vaporization/heat removal/recoil. Different coefficient pairs have <20% overall geometric error and substantially different temperature profiles.
- **Discriminating evidence:** p7 discussion and p9 Fig.8 show that lower Fresnel/higher accommodation coefficients better agree with the two-color surface-temperature measurements, especially behind the laser. This validates the usefulness of an additional thermal observable under those conditions.
- **Limits:** it is a CFD model with liquid flow/recoil and constant surface tension, therefore no Marangoni effect (p7). Plume obscuration/emission and camera sensitivity constrain the observations (pp8–9, §4.2). It does not show that the present property cases were independently refitted or establish mathematical forward nonuniqueness.
- **Journal structure learned from actual pp1–2:** the introduction proceeds from a specific measurement bottleneck, through limitations of alternative optical arrangements, to the implemented tool and its model-discrimination role. Apply that logic to the current constitutive problem; avoid generic LPBF background unrelated to the tested quantities.

### 5. Alternative closure advancement: Coleman

- **Specific predecessor limitation:** pp2–3 and §2.2.1 pp5–6 identify fixed heat-source depth/absorption calibrated to steady single tracks as unable to follow changed local thermal conditions and conduction–keyhole transitions.
- **Actual method:** pp6–8 Eqs(2)–(6) independently parameterize radial energy distribution and volumetric shape, retain measured D4σ, and normalize to ηP. §2.2.4 pp11–13 makes source depth depend on melt-pool depth and absorption depend on an idealized cavity aspect ratio. Its η is **effective absorption**, with η0=0.28 and ηeff=0.35 taken from cited experimental evidence; it is not the present B-fitted scalar.
- **Calibration/transfer:** p17 uses width/depth at 195 W, 800 mm/s and D4σ from 80 to 322 μm on the **EOS M270**, 20 comparisons; p18 applies the fitted model to AMB2018-01 representative IN625 layers. These are not the present three AMMT bare-plate conditions. p31 Fig.13 contrasts the dynamic model calibrated across the full dataset against static Goldak sources fitted at particular spot sizes.
- **Phase/property differences:** p5 uses a linear temperature–solid-fraction relation, but pp18,20 Table2 use liquidus 1620 K and eutectic 1410 K from Gulliver–Scheil calculations, motivated by limited solid diffusion at rapid cooling. Density, latent heat and property laws also differ from the current model. This source supports a linear continuum approximation, not the current thresholds or their equilibrium status.
- **Remaining discrepancy:** pp30–31 locate the largest cross-section mismatch near the top and discuss unresolved radial convection/Marangoni effects as a possible remedy. p36 says short-dwell even layers do not reach steady-state and require careful correspondence with metallographic observations. This is useful competing evidence: a more adaptive source is an existing route, and the current six steady solutions do not replace it or establish applicability to transient layers.
- **Journal structure learned from actual introduction/methods:** Coleman derives three explicit requirements from a documented failure of fixed source parameters (p6). The current manuscript needs one comparably concrete requirement: specify the table-exceeding constitutive choices and separate rear displacement from separation before interpreting a calibrated length thermally.

### 6. Actual supplier data: Special Metals

- **p1:** data are typical alloy properties, not specifications or benchmark-coupon measurements; the copyright/edition is August 2013.
- **p2 Table2:** density 8.44 g/cm³; “Melting Range” 1290–1350 °C; twelve specific-heat entries end at **1093 °C, 670 J/(kg K)**. Footnote a: **Calculated**.
- **p2 Table3:** fifteen nonblank conductivity entries end at **982 °C, 25.2 W/(m K)**. The 927 °C and 1093 °C rows have no conductivity value. Footnote b: measurements made at **Battelle Memorial Institute**; footnote c: material annealed **2100 °F/1 h**.
- The supplier does not identify its listed range as an equilibrium phase calculation and does not supply liquid conductivity/specific heat in this table. Use “supplier-listed melting range” and “adopted solidus/liquidus thresholds”; do not add an unverified “equilibrium” qualifier.

## Explicit mathematical definitions of the extrapolation cases

These are **study-defined extrapolation rules**, not established named physical IN625 models. Prefer “linear extrapolation using the slope of the final two tabulated values” and “constant extrapolation at the tabulated endpoint.” Short labels can be L and H if already bound in archived run names; their full definitions must precede those labels.

For a property p with final two tabulated pairs (Tn−1,pn−1),(Tn,pn), let m=(pn−pn−1)/(Tn−Tn−1). Both cases share piecewise-linear interpolation within the available table. For T>Tn:

\[
p_L(T)=p_n+m(T-T_n),\qquad p_H(T)=p_n.
\]

| Property | Final tabulated pair used for slope | Endpoint | Final-secant slope |
|---|---|---|---|
| k | (871 °C,22.8), (982 °C,25.2) | 982 °C | 2.4/111 = 0.0216216216 W m⁻¹ K⁻² |
| cp | (982 °C,645), (1093 °C,670) | 1093 °C | 25/111 = 0.225225225 J kg⁻¹ K⁻² |

Temperature differences in °C and K are identical here. Both tables end below Ts=1290 °C, so the interventions start **below the melting interval**, not only in liquid. For T>Tn, the difference of the corresponding primitive functions is ΔK=mk(T−982)²/2 and Δh_sensible=mcp(T−1093)²/2, respectively, with the same primitive value at the endpoint. The same latent contribution is retained in every corner. This is why k/K/surface recovery must be changed together, and cp/H/the inverse enthalpy relation together.

| T (°C) | kL / kH (W m⁻¹ K⁻¹) | cpL / cpH (J kg⁻¹ K⁻¹) |
|---:|---:|---:|
|1290|31.85946 / 25.2|714.36937 / 670|
|1320|32.50811 / 25.2|721.12613 / 670|
|1350|33.15676 / 25.2|727.88288 / 670|

At 1320 °C, the changes are −22.48088% in k and −7.08976% in sensible cp. The adopted latent contribution is 280000/60=4666.66667 J kg⁻¹ K⁻¹, so effective cp changes from 5387.79279 to 5336.66667, approximately −0.9489%. Integrating the actual twelve cp knots from T0=25 °C gives a 0.66198% total enthalpy change at 1320 °C, consistent with the frozen manuscript. The two interventions are not matched-percentage perturbations of transport and total storage. Their effect-size comparison must retain this asymmetry.

The values are numerical scenarios. Neither source supports treating the two extrapolation rules as upper/lower confidence bounds on the true liquid properties, or treating H as the experimentally established liquid plateau. A long high-temperature linear extension can depart substantially from real liquid behavior, but that fact requires external property evidence to quantify.

## Source-factor function and interpretation

The present q=2ηP exp[−2(ξ²+y²)/w²]/(πw²) integrates over the full plane to ηP and over the symmetric half-domain to ηP/2. For this Gaussian, σx=w/2 and D4σ=4σx=2w. Thus w=85 μm follows from 170 μm **under the assumed circular Gaussian**.

The fitted η≈0.28905 multiplies source power; it does not alter the distribution shape, penetration law or beam diameter. A useful descriptive name is **calibrated effective source-power fraction / 标定的有效热源功率系数**. “Effective absorption” is authentic language in Coleman; “absorptivity” is authentic in Kollmannsberger. For the present value, identify the fitted model function before using either physical-sounding term. It is conditional on the source map approximation, property extrapolations, phase law and length extraction. Its numerical proximity to Coleman's η0=0.28 does not validate it as measured Fresnel absorption.

## Comparator definitions and allowable claims

| Comparator | Exact object/population | Numbers and locator | Role and permitted interpretation |
|---|---|---|---|
| AMMT thermographic length mean | 20 μs imaging tracks only; profile-derived length; video-frame populations | Lane Table4: A/B/C 300/359/370 μm; N=19/10/7. Table5 U(k=2)=11.91/21.26/32.57 μm. | B=359 is the calibration target. A/C comparisons are retrospective because benchmark values were consulted during development. Neither is independent prospective validation. |
| NIST challenge mean width/depth | Transverse metallography of ten 100 μs-sample tracks; A and B each three tracks, C four | NIST Table2: W=147.9/123.5/106 μm; D=42.5/36.0/29.6 μm. Class standard deviations W=3.7/6.5/1.4; D=1.7/1.9/0.6 μm. Lane P36,P70 identify this specimen. | Separate dimensional shape assessment. These are not cross-sections of each thermographic frame used for length. The quoted class standard deviations are not automatically expanded uncertainty. |
| Lane compiled microscopy uncertainty | Author-reported analysis of combined 100 μs/20 μs microscopy classes | Lane Table4 caption/P40; Tables6–7: UW=6.42/6.30/4.48 μm; UD=4.49/3.97/3.26 μm. | δ/U using the NIST means is a descriptive deviation normalized by a separately sourced measurement scale. It is not a calibrated likelihood, formal joint statistical test or total prediction uncertainty. |
| Kollmannsberger isotropic result | Transient isotropic model with measured 2D source and η=0.086; its own property/phase model and 2019 targets | PDF p9 Table7; C target depth is 29.5 μm in their p5 Table4, whereas current NIST Table2 is 29.6. | Published-model context. Do not interpret its difference from the present curve as an isolated source, solver or property intervention. |
| Kollmannsberger anisotropic result | Same predecessor plus fitted θx/y/z and model-specific calibration | PDF pp9–10, Tables9–10 | Competing closure demonstrates shape improvement is possible within a thermal model. It does not validate the present isotropic thermal histories. |
| L/H four B cases | Same P,v,η,phase law,mesh and observation definitions; only the two prescribed extrapolation functions change | Current manuscript §2; LL is calibrated, HL/LH/HH are not refitted | Deterministic two-factor finite differences. The output differences are constitutive responses at retained source power, not equally calibrated alternatives or sampled uncertainty. |
| Rear phase boundaries and passage time | Rear surface symmetry-centerline crossings of the model's adopted 1290/1350 °C thresholds | Current model: ℓm=ξl−−ξs−, τm=ℓm/v; dT/dt=−v∂T/∂ξ | Derived descriptors of stationary material traversing a quasi-steady conduction field. They are not independently measured mushy-zone length or a liquid-parcel residence time. |

## Professional bilingual lexicon

“Authentic” below means conventional/source-used vocabulary. It does not certify the present model as physically validated. Prefer the concrete object in prose; keep concise labels in tables/legends.

| Recommended English | 推荐中文 | Status/use |
|---|---|---|
| thermophysical properties | 热物性 | Authentic general terminology. |
| temperature-dependent thermal conductivity | 温度相关导热率 | Authentic material input; use k with units. |
| sensible specific heat capacity | 显热比热容 | Specific cp term excluding latent addition; avoid “storage law” when the actual changed input is cp. |
| enthalpy-based heat conduction model | 基于焓的热传导模型 | Authentic method class; enthalpy formulation is not a new algorithm here. |
| liquid fraction; linear liquid-fraction approximation | 液相分数；线性液相分数近似 | Authentic continuum terms. “Equilibrium fraction” is not established by the present inputs. |
| supplier-listed melting range | 供应商列示的熔化温区 | Faithful to bulletin wording. |
| adopted solidus and liquidus thresholds | 采用的固相线、液相线温度阈值 | Explicit present-model role. |
| piecewise-linear interpolation | 分段线性插值 | Standard numerical operation within tabulated range. |
| linear extrapolation using the final tabulated slope | 按末段表格斜率线性外推 | Standard extrapolation; define the final two knots. More informative than “linear continuation.” |
| constant extrapolation at the tabulated endpoint | 在表格端值处作常数外推 | Standard operation; more informative than “last-value holding.” |
| effective source-power fraction | 有效热源功率系数 | Present operational name for η; its role is scaling q to integral ηP. |
| absorptivity / effective absorption | 吸收率／有效吸收 | Authentic source terminology; use only with that source's definition, or qualify present fitted value. |
| thermographic melt-pool length | 热成像熔池长度 | Source-defined measurand; specify 20 μs and its profile operator. |
| metallographic fusion-zone width and depth | 金相熔合区宽度与深度 | Concrete measured counterpart; identify 100 μs sample. |
| model solidus-crossing length | 模型固相线交点长度 | Present definition, not an identical thermographic operator. |
| maximum-temperature fusion envelope | 最高温度熔合包络 | Present model-defined threshold region; define maxξT≥Ts. |
| rear solidus–liquidus separation | 后部固相线—液相线间距 | Concrete present descriptor; safer than an unexplained “phase span.” |
| downstream displacement of the rear isotherms | 后部等温线沿后方移位 | Use direction relative to the source frame and stated sign convention. |
| passage time through the adopted freezing interval | 通过所采用凝固温区的时间 | Present derived descriptor for stationary material; state τ=ℓ/v. |
| interval-mean cooling-rate magnitude | 温区平均冷却速率的大小 | Derived from ΔT/τ; not an independently validated cooling rate. |
| deterministic two-factor property comparison | 两因素确定性物性比较 | Design description, not an external physical mechanism or uncertainty distribution. |
| retrospective fixed-parameter comparison | 固定参数的回顾性比较 | Accurate A/C/B-width/depth assessment status after benchmark consultation. |
| deviation normalized by the published measurement uncertainty | 以已发表测量不确定度归一化的偏差 | Explicit δ/U denominator; avoid “agreement score” or statistical significance. |

## Actionable evidence gaps and scope limits

1. **Property selection:** neither extrapolation is empirically selected by the supplier. A targeted search for IN625 solid/liquid high-temperature property measurements could replace the numerical scenarios with physically supported property laws and change quantitative effect sizes. It would not change the definition of the existing six runs. No extra broad search is necessary to answer this audit's source/object question.
2. **Thermal validation:** the current source calibration plus geometric comparison cannot validate rear phase boundaries or interval cooling rates. A co-registered rear thermal measurement spanning the adopted interval, with its phase/emittance assumptions made explicit, would assess those outputs. Lane's exemplar cooling values should not fill this gap.
3. **Identifiability after refitting:** a fresh B-length calibration for every property case would answer whether equally fitted lengths retain different rear spans/times. The current unchanged-η design answers the different question of fixed-source constitutive response. Do not imply those additional solves exist.
4. **Observation correspondence:** class-level length and microscopy comparisons do not provide a joint frame/section observation of the same melt pool. A matched specimen/track/position comparison, and uncertainty for the actual 100 μs target means, could change formal agreement claims; it is unnecessary for the present signed descriptive residuals.
5. **Mechanism attribution:** surface source shape, depth deposition, omitted flow, selected phase interval and high-temperature inputs are competing explanations for the shape residual. The six solutions isolate prescribed property changes but do not isolate these omitted phenomena. Wider/shallower geometry alone cannot identify Marangoni flow or any single missing mechanism.
6. **Spatial/time descriptor:** τ=ℓ/v is exact for the adopted steady translation mapping; it does not imply liquid parcels traverse that same path when melt flow exists. Predicting microstructure, defects or a real liquid residence time would require additional physical evidence beyond this audit and beyond the six conduction fields.

The contracted source-dependent decisions are now answered. Extending the search would be useful only if the coordinator changes the next claim to empirical high-temperature property selection, phase nonequilibrium, broader novelty coverage or independent thermal validation.
