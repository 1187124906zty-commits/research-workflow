# Initial independent manuscript review

Date: 2026-10-01. Reviewer: the assigned `ammt_manuscript_review` agent. Scope: the new English manuscript, its four actual figures and the 20-page rendered preprint, with selective checks of the retained scientific evidence and closest literature. This is author-side review support, not a journal decision or submission certificate. Only this assigned review directory was written. No solver was imported or run, and no manuscript, original case, skill or shared research state was changed.

## Disposition recommendation

**Revise before presenting this as an Additive Manufacturing-facing research article.** The numerical values and principal claim boundaries are substantially sound. I found no critical data-integrity contradiction in the inspected material. Two figure captions describe content/layout absent from their actual figures. The contribution also needs a sharper literature-grounded statement and a stronger scholarly discussion of what the present controlled contrast adds. These are repairable with the existing evidence; a new solver campaign is not required to repair the current bounded manuscript.

The defensible core is a **fixed-model discrepancy and continuation-sensitivity study**: a B-length calibration leaves wide/shallow fusion-envelope residuals, and at fixed B and fixed effective source factor, separate conductivity/storage continuation contrasts reveal a substantial rear-boundary translation. The study does not establish predictive validation, actual liquid-property identification, or a unique missing-flow mechanism. It should not be promoted to any of those interpretations through editorial revision.

The main tens-of-micrometre length response does not need universal asymptotic convergence to remain useful. The retained baseline axial/domain sensitivities are relevant evidence against those inspected numerical changes explaining the large discrepancy. They do not establish the robustness of every small branch interaction or phase-span increment. The manuscript largely respects this distinction already.

## Review exposure and evidence coverage

I inspected the question, model/evidence structure and methods before reading the manuscript's Results/Discussion. However, the journal dossier and supplied evidence dossier contain producer interpretations, and I read some of those before independently opening the original result/code records. **This review therefore was not blinded to producer interpretation.** It is a separate-context review by another agent in the same model family; it is not statistically independent human replication.

Inputs actually inspected:

- `manuscript.tex`, the complete initial source plus a selective read of the evolving Discussion; line locators below refer to the source read on this date and are paired with quotes so they survive subsequent line movement.
- `evidence/evidence-dossier.md` and selected objects in `evidence/verified-data.json`: physical model/table knots, six production records, geometry comparisons, four-corner values/effects, case-history metrics and numerical sensitivity records.
- The six original `verification/*/result.json` files identified by the evidence JSON, the constant-property analytic-geometry record, and retained calibration/refinement summaries. These are original numerical outputs, not fresh PDE execution.
- Original implementation passages in `solver/native_fv_enthalpy.py`, `solver/fipy_application_frame.py`, `solver/run_constitutive_factorial.py`, `solver/redraw_research_figures.py`, and `collaboration/analyze_fipy_r8_flux_native61.py`. These were read as text only. In particular, the figure code reconstructs each slice before passage maximization; it does not silently use the older nodal-maximum array for the primary fusion envelope.
- `literature/journal-dossier.md`, `literature/bibliography.bib`, the built `.bbl`, the original Kollmannsberger author-source `modelVerification.tex`/`conclusions.tex`, and the relevant Myers published full-text passages. No comprehensive new field-wide novelty search was conducted; no claim of absence of prior work follows from this review.
- All four actual figure PNGs; all 20 preprint pages through `qa/contact-sheet-1.png` to `contact-sheet-3.png`; full-page views of pp. 9, 10, 11, 13, 15 and 20. Citations and numbered references now render. No visible clipping, blank page, missing figure or orphaned caption was found in those inspected views. Individual figure labels remain readable at their rendered size.

The review applied the PaperSpine evidence-grounded review/policy guidance and PDF inspection guidance. The substantive findings below are based on the actual files, not a tool PASS. Tool outputs provide read/inspection receipts; exact token telemetry for this whole review is unavailable, and no estimate is presented as measured usage.

## Located findings

### R1 — Two captions do not match their figures

**Severity:** MAJOR factual/editorial defect affecting figure/text identity. **Confidence:** high. **Status:** OPEN in the reviewed source/render. **Affected inference:** readers cannot reliably map the described observables to the displayed panels; the Fig. 3 caption falsely indicates visual evidence for a cooling-rate panel.

**Locations and evidence:**

- `manuscript.tex:195`, Fig. 2 caption; preprint p. 10: “Upper panels show surface solidus contours … lower panels show … fusion envelopes.” The actual `ammt-research-operating-cases` figure has two side-by-side panels: **(a)** surface solidus isotherms and **(b)** fusion-zone envelopes. The original figure routine uses `plt.subplots(1, 2)`.
- `manuscript.tex:207`, Fig. 3 caption; preprint p. 11: “rear liquidus-to-solidus spatial span, derived material passage time, interval-mean cooling rate, and fusion-zone aspect ratio.” The actual `ammt-research-condition-trends` figure has **(a)** nominal B→C width/depth percent changes, **(b)** class-mean aspect ratios, **(c)** spatial phase spans, and **(d)** passage times. **There is no cooling-rate panel.** The plotted percent changes and aspect ratios are not solely derived quantities sharing one model solution; experimental class means are also plotted.

**Smallest useful repair:** rewrite these captions by panel letter. For Fig. 2, use “(a) …; (b) …”. For Fig. 3, name the four actual jobs above and state that percent changes/experimental aspect ratios use nominal source means with uncertainty/covariance not propagated. Retain the below-solidus distinction for cooling rates in the Methods/body where those rates are actually reported. No figure regeneration or new data is needed unless the producer chooses to add a cooling-rate panel.

### R2 — The scientific delta and AM-facing significance remain too implicit

**Severity:** MAJOR editorial/argument defect for the stated target; **not** a factual finding of no novelty. **Confidence:** high that the manuscript's positioning is incomplete; moderate concerning journal competitiveness. **Status:** OPEN. **Affected claims:** the significance and originality of the research contribution stated in Introduction and Conclusions.

**Locations and evidence:** `manuscript.tex:35`, Introduction: “Its contribution is an evidence-bound diagnosis of which aspects of this calibrated model remain stable, which respond strongly to closure, and which require different evidence before physical interpretation.” Discussion §4.1, `manuscript.tex:256`, explains the opposite bias directions relative to Kollmannsberger, but the remaining Discussion mainly explains limitations and future tests. The actual closest prior source already identifies high-temperature property extrapolation as a physical model needing calibration (`modelVerification.tex:162–167`), fits effective anisotropy above its conductivity endpoint (`:404–426`), and explicitly warns that its model is not valid for temperatures inside the melt pool (`conclusions.tex:9`). Myers 2023 independently shows multiple geometry-fitting parameter pairs with substantially different temperature profiles (published text lines 587–623 and Fig. 8).

The present four-corner contrast adds a useful **separate conductivity/storage response and rear-position decomposition** under a frozen model/source/operator. But the broad lesson that geometry calibration does not uniquely determine thermal physics is already supported by the cited literature. A reader needs the exact added information and the modeling decision it informs, not merely the fact that the investigation is carefully bounded.

**Smallest useful repair:** revise the final Introduction paragraph to state a specific question/delta: whether the two independently applied continuation rules alter the calibrated tail mainly by rear translation or phase-span change, and whether this alteration can repair the transverse geometry residual. In Discussion, distinguish this controlled within-model question from Kollmannsberger's calibrated directional-transport improvement and Myers's orthogonal thermal observation. Explain the practical implication: reporting only a joint property switch or only a fitted length can hide the source of closure sensitivity and the surviving shape failure. Do not call the approach “first” without additional external evidence. Do not treat agent coordination, solver implementation or the kinematic division by speed as methodological novelty.

This repair can improve a defensible bounded contribution without demanding an unrelated new flow solver or a different scientific objective. **Field-wide novelty/AM competitiveness remains unestablished by this review**, because the provided journal learning set is not a comprehensive property-sensitivity prior-art search.

### R3 — The local face Péclet statistic lacks a reproducible operator definition

**Severity:** MINOR scientific-reporting defect. **Confidence:** high. **Status:** OPEN. **Affected inference:** the reader's interpretation of the 4.44→5.77 median as support for reduced modeled diffusion relative to coordinate transport.

**Location:** `manuscript.tex:241`, Results §3.3: “A retained local face Péclet diagnostic for the mushy ξ faces increases in median from 4.44 in LL to 5.77 in HL.” The updated Discussion at `manuscript.tex:265` correctly notes that these medians select faces in different solved states, and does not infer a smaller integrated rear heat flux.

**Original evidence:** `collaboration/analyze_fipy_r8_flux_native61.py` defines `Pe=(u_f·n_f)*d_f/D_f`. Its median is of `abs(Pe)` over interior faces with nonzero axial transport and **at least one adjacent cell** in the mushy temperature range. This is an unweighted median over selected mesh faces. It is not a laser-radius Péclet number, a fixed physical-region average, or an area-weighted flux ratio.

**Smallest useful repair:** add the formula, face distance/constitutive diffusivity definitions, adjacent-cell selection rule and unweighted median convention in Methods or the Appendix. Keep its role as a discrete diagnostic on the common mesh, conditional on temperature-selected state. The matched-temperature k/effective-storage comparison already supports the limited interpretation; the median should not become an independent causal test.

### R4 — Coordinate extents are assigned a volume unit

**Severity:** MINOR dimensional notation defect. **Confidence:** high. **Status:** OPEN. **Location:** `manuscript.tex:93`, Methods §2.3; preprint p. 5: “The domain is [-1,0.35] × [0,0.36] × [-0.30,0] mm³, ordered as (ξ,y,z).”

**Affected inference:** domain geometry/reproducibility. A Cartesian product of three coordinate intervals describes three lengths; the appended mm³ can be read as assigning a volume unit to each coordinate or to the interval tuple. The code/manifest clearly use millimetre coordinate extents, so this is notation, not an incorrectly sized numerical domain.

**Smallest useful repair:** state the three intervals with mm on each, or define `(ξ,y,z)` in mm before listing the product. If a volume is desired separately, this half-domain volume is 0.1458 mm³.

### R5 — Material and calibration inputs need a compact source/method trail

**Severity:** MINOR reproducibility/reader gap. **Confidence:** high. **Status:** OPEN. **Locations:** `manuscript.tex:67,75,130` and Appendix A. The paper lists the adopted density, latent heat and phase thresholds, and says scalar calibration “yields η=0.2890548519203547,” but gives no local calibration bracket/algorithm or stopping target. The general bulletin is cited in the Introduction for table endpoints rather than directly identifying the Methods' input table and adopted constants.

**Affected inference:** another investigator's ability to reproduce the same closure/calibration rather than obtain a merely similar fitted number. The evidence records show five successful local bracket points and a local slope about 1276.79 µm per unit η. They do not prove global uniqueness over [0,1]. This manuscript does not claim such uniqueness, and the omission does not invalidate the fit.

**Smallest useful repair:** add a direct material-table source citation and distinguish sourced typical data from adopted constants/phase-law assumptions. Supply the table knots or an exact stable supplemental-file locator. Add the actual scalar objective, bracket/update method and accepted residual criterion from executed calibration records. The full-precision fitted η may remain in machine-readable files; no universal digit rule is required. Optionally report the local sensitivity and the propagated B-U scale as **sensitivity only**, not a posterior. Do not invent a source for constants whose provenance remains an adopted reconstruction choice.

## Fine-contrast adequacy: retained concern, bounded repair

The exact finite-output algebra in Table 3 is correct. Its caption already says small transverse effects lack branch-specific refinement evidence, §2.6 calls submicrometre interactions descriptive, and §3.3 explicitly declines a robust width-interaction ranking. Those qualifications prevent this from being a new scientific blocker for the large tail finding.

There is nevertheless a local consistency improvement at `manuscript.tex:243,248,284`: “Depth illustrates cancellation,” “joint depth change conceals opposing … contributions,” and “Opposing depth responses partly cancel” should be qualified as **the retained/current-mesh contrast**. The +0.49 µm storage effect, +0.21 µm depth interaction, −0.32 µm joint depth change and 0.31 µm phase-span change lack corresponding branch-specific multidirectional accuracy evidence. Their displayed values are computational outputs, not demonstrated physical precision. This is a **MINOR claim-scope clarification**, not a requirement to discard the table or perform all-branch convergence.

If a later revision promotes the small interaction/phase-span ordering to a central robust inference, the smallest useful test is a matched pair/four-corner refinement targeted to that specific QoI, with a stable observer, rather than indiscriminate refinement of every production run. Baseline B/C axial sensitivity alone cannot clear that stronger inference.

## Scientific strengths that should survive revision

- The model, moving-coordinate transport, source normalization, equilibrium phase law and observation operators are specified consistently with the inspected implementation. The correct production candidate is FiPy, not the legacy FEniCSx method.
- The B length fit and effective η are correctly disclosed. B width/depth remain diagnostics; A/C are explicitly retrospective and nonblind. The manuscript does not convert the tiny calibration residual into independent validation.
- The means/uncertainties are handled honestly. Current NIST 100 µs cross-section means and separate Lane combined-class U are distinguished; δ/U is descriptive; frame/track replication and the absence of raw reaggregation are stated. There is no unsupported significance or nine-QoI joint coverage claim.
- The B→C nominal length increase is not described as a statistically resolved opposite physical trend. A→B is not attributed to speed alone. Mean ratios are not passed off as simultaneous 3D specimen geometry.
- The retained four-corner values, their algebra and all main geometry residuals match the original result records. Fixed η isolates the implemented continuation response rather than comparing refitted branches.
- The updated §4.2 clearly separates the bulk constitutive change from conductivity-dependent surface recovery. It preserves state-dependent face-selection limitations and does not assign real rear heat flux or flow causality from a Péclet median.
- Hotter held-conductivity peaks are correctly excluded from physical-temperature claims. Omitting flow, evaporation, surface evolution and solved boundary-loss feedback remains visible. The paper proposes competing source/operator/transport tests without pretending those mechanisms have already been identified.

## Originality, target fit and scholarly presentation

**Topical fit:** Additive Manufacturing is a coherent target for an IN625 AMMT single-track thermal study. The data are bare-plate tracks, so the LPBF keyword/context should continue to be paired with that condition rather than implying powder-layer validation.

**Contribution judgment:** the separate continuation and rear-position analysis is an intelligible bounded computational result. It is incremental within a well-established modeling/measurement line, and its value is diagnostic rather than a new numerical method. I do not find evidence in the inspected originals that makes this exact fixed-factorial result a false contribution. I also cannot certify broad originality or journal acceptance from the narrow learning corpus. The most plausible editorial weakness is that the paper currently devotes more argument to evidential boundaries than to the scientific information added beyond existing calibration/property cautions. Repair R2 before calling the target argument complete.

**Discussion:** its mechanism language is appropriately conditional, especially after the added bulk/recovery and selected-face paragraph. It should make fuller use of the actual scientific literature already available. Myers provides direct empirical support for the need for thermal observables beyond geometry; Kollmannsberger provides a close contrast between directional correction of shape and the present scalar continuation response. Explaining those specific relations is more valuable than increasing the citation count. No reference-count minimum is imposed.

**Style advisories, separate from factual defects:**

- The title accurately signals the result but is long. Shortening it is optional; do not remove the fixed-model/IN625 scope merely to make it sound stronger.
- Repeated phrases such as “retained,” “evidence-bound,” and “not validation” are accurate but distract when repeated in Results, Discussion, Conclusions and disclosure. Concentrate the numerical/provenance boundaries where each inference needs them.
- `manuscript.tex:265`, “These distinctions emerged in the independent mechanism review,” is process commentary. State the scientific distinction directly in Discussion and leave review provenance in the Methods/disclosure.
- The paragraph beginning “The calculation set supports a first discrepancy-and-sensitivity manuscript” (§4.4) evaluates the manuscript rather than discussing the material/model. Replace it with the scientifically earned implication or delete that metatext. The agent-workflow paragraph is provenance; it should not bear the contribution argument.
- A short observation-operator schematic could help a reader distinguish thermographic length from a passage fusion envelope, but the existing equations/captions can also do that job. Its absence is not a scientific blocker or a figure-count failure.

## Journal/submission conditions, kept distinct from science

The preprint uses the official Elsevier `elsarticle` fallback and its numeric bibliography; it is a readable 20-page preprint, not a verified AM-specific final-layout requirement. The current AM author guide was inaccessible according to the dossier, so this review does not assert official abstract limits, mandatory highlights/graphical abstract, anonymity or file-resolution compliance.

Authorship/affiliations and human verification, funding, competing-interest and final AI-disclosure facts are explicitly unresolved in the draft. They must be supplied truthfully by the responsible researchers before submission. The current AI paragraph describes a first draft and future completion rather than a finalized author declaration. This is an intentional submission dependency, not a finding that the numerical study is scientifically invalid. The availability claims and remote package links also require the coordinator's actual release/read-back before publication; this review inspected local files and did not verify a remote release.

## Return condition and unresolved findings

This initial assigned review is complete. **R1 and R2 remain the priority open findings.** R3–R5 and the local fine-contrast qualification are bounded minor repairs. No consensus, confidence label, compile success or same-model agreement clears them. The coordinator should repair the actual source and verify the changed captions/argument in the rendered paper; this file records the reviewed state and is not silently overwritten with a PASS.

After this report was written, the coordinator reported source repairs to the two captions, the explicit contribution delta, material/calibration provenance, the final property secants and Péclet operator, and the small-depth/phase-span qualifications. That report is recorded as **producer-reported repair, final source/render recheck pending**, rather than evidence that this initial finding register has been cleared. A later requested recheck can record which exact affected locations and pages were verified without erasing this initial review.
