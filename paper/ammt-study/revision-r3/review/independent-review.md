# Independent R3 review of the IN625 AMMT manuscript

Reviewed 2026-10-01, approximately 15:16–15:27 UTC. Contract: assess whether the actual R3 paper resolves reader-facing overload, fragmented headings/transitions and source mismatch while preserving its scientific scope. No PDE solves, new literature additions, source edits, shared-state edits or publication actions were performed by this reviewer.

## Version and exposure

- Source: canonical `../../manuscript.tex`, 58,289 bytes, last-write time 2026-10-01 15:06:50 UTC; all 427 lines read. Locators below refer to this version.
- Render: `../../.latex-build-8wcy49_i/manuscript.pdf`, 400,422 bytes, last-write time 15:13:56 UTC, 18 pages. Both contact sheets covering all 18 pages were inspected, with full-page inspection of pages 3–6, 10, 12–14 for Methods, main factorial figure, Discussion and final matter. Other pages were assessed through the contact sheets and complete source. The canonical `manuscript.pdf` replacement was not assumed to have occurred.
- Question and Methods were inspected before the editorial producer audit. The first source read also exposed the Abstract and the opening C01–C03 support-ledger entries; consequently this was **not a blinded raw-evidence-first review**. Direct source passages and numerical tables were then inspected before reading the editorial audit's interpretation. The review shares the parent model family and is not statistical evidence of independent judgment.
- Raw numerical scope: the three case metrics, four retained branch rows, comparison CSV, retained six-run `result.json` residual/correction fields, and saved official NIST cross-section HTML table. Factorial and time-transform arithmetic was recomputed without importing a solver. Full retained field arrays were not reanalysed; this review does not repeat the separate evidence-dossier implementation audit.

## Disposition recommendation

**Accept the R3 structural and citation repair after one narrow scientific wording correction and removal of one author-action note from the article.** The actual pages and source support an affirmative answer to the contracted question. There is no basis from this pass to require another PDE solve, more references or a new section architecture. This recommendation is for the assigned revision, not journal acceptance, physical thermal validation or submission-readiness certification.

The scientific correction affects only an overbroad mechanism-elimination phrase. It does not invalidate the reported tail displacement, deterministic contrasts or time conversion. The final-matter repair is editorial and can preserve the honest disclosure without asserting that human review has already occurred. Both findings remain open until a changed source and corresponding proof are checked.

## Actionable findings

### R3-IR-01 — Narrow the mechanism excluded by the selected-region flux diagnostic

**Location/version:** source line 293, Discussion §4.2, rendered p12; supporting Methods line 159 and Appendix lines 381–388; Results line 250.

**Defect:** “The diagnostics support a changed balance between coordinate enthalpy transport and diffusion, **while ruling out a simple bulk-flux explanation**” can be read as excluding bulk heat-escape mechanisms generally. The same paragraph correctly says that gradients and the temperature-selected boundary both change, and ends by requiring a matched-region comparison to assign the response to suppressed bulk heat escape. The opening phrase therefore makes a broader exclusion than the diagnostic and the remainder of the paragraph permit.

**Evidence/source:** direct `data/constitutive-factorial-metrics.csv` rows LL/HL give rear hot-region outward diffusive powers 14.723959 and 14.913303 W, respectively. The selected region is defined separately by `T ≥ Ts` and `xi < 0`, so neither its boundary nor its face population is held fixed. The independently read Appendix describes that selection correctly. No external paper can turn this changing-region comparison into the missing matched-region causal test.

**Support:** **partial** for the sentence as written. Full support exists for the narrower counterexample: lower conductivity does not necessarily lower the integrated outward power of this separately selected hot region. Support is **absent** for a general elimination of bulk-flux mechanisms.

**Severity/affected claim:** minor scientific interpretation defect, confined to the mechanistic reach of §4.2. The raw numerical comparison and dominant rear translation remain intact.

**Smallest useful repair:** replace the opening sentence with, for example, “The diagnostics support a changed balance between coordinate enthalpy transport and diffusion, but do not support equating conductivity holding with reduced integrated outward heat flow from the selected rear region.” Retain the later matched-region limitation. No new test is necessary for the present scoped claim; a matched-region flux or field/recovery separation is needed only if the broader mechanism claim is retained.

### R3-IR-02 — Move the unfinished author action out of the AI declaration

**Location/version:** source line 322, rendered p14, Declaration of generative AI use.

**Defect:** “The responsible researchers must review the complete manuscript and finalize this disclosure before submission” addresses the authors' workflow inside the article. It is a residual delivery instruction after the rest of R3 has moved implementation/workflow material to appropriate supporting files.

**Evidence/source:** the literal sentence is present on the actual rendered page. The assigned `revision-r3/editorial/venue-structure-audit.md`, final disclosure note, explicitly distinguishes factual AI assistance from unfinished authorship/human-review verification. The present official AM author guide remains unavailable; this finding is about reader-facing allocation, not a claimed journal-mandated sentence.

**Support:** **full** for the stated current AI assistance and deterministic plotting in this review context; **unverified** for completed responsible-author review, which the article does not currently assert and the revision must not invent.

**Severity/affected claim:** minor editorial/finalization defect, affecting the declaration's function and the cleanliness of the delivered article; no numerical or physical claim is affected.

**Smallest useful repair:** retain the two factual disclosure sentences and move the final human-review instruction to the delivery/submission notes. Do not replace it with a false assertion that authors have reviewed the final manuscript. If a venue requires a completed author-responsibility assertion, the responsible authors must supply that fact before submission.

## What the R3 repair actually achieves

The Methods now follows the scientific dependency: benchmark/comparison design → material continuation and balance → observable definitions and time mapping → calibration/contrast/numerical evidence. The four subsection titles describe substantive tasks rather than isolated implementation fragments. The observation-recovery order remains in the main text because it changes the extracted envelope. Cell counts, scaled unknown, face coefficient, derivative limit, detailed source integration, diagnostic populations and acceptance residuals are recoverable in the Appendix. That allocation preserves scientific detail while removing its interruption of the main argument.

The Discussion likewise develops four connected questions: what the geometric fit leaves unresolved; what transport/storage changes do to the tail; why phase separation differs from material time; and which missing evidence would discriminate explanations. The bridges are specific to the results, including the end of §3.1 leading into the fixed-source comparison and §4.3 separating stationary passage from fluid trajectories. The complete page sequence reads continuously. It does not need a universal limit on subsection count or an imposed sample-paper template.

The principal numerical claims agree with retained rows. Recalculation gives conductivity/storage/interaction/joint length effects `43.213712 / −6.168858 / −2.761942 / 34.282913 µm`; depth effects `−1.028337 / +0.493077 / +0.211976 / −0.323285 µm`; rear-solidus extension fraction `0.98318997`; B–C passage-time change `−32.89530%`; and cooling-magnitude change `+49.02086%`. The local 1320 °C continuation values independently calculate to `kL=32.508108 W m−1 K−1` and `cpL=721.126126 J kg−1 K−1`. Six original result records support the reported residual range, signed global balance below `6.1e−11` and correction below `2.7e−5 °C`. These checks establish reporting consistency, not new numerical or physical validation.

Retrospective/nonblind calibration remains explicit (§2.1). The Gaussian is distinguished from the measured beam map, and eta remains an effective source/model/operator parameter (§2.3). Lane's P87/P40 establishes combined 100/20 µs microscopy versus 20 µs imaging; the saved official NIST Table 2 directly supplies the current 100 µs-class width/depth means used here (A 147.9/42.5, B 123.5/36, C 106/29.6 µm). The paper states that these are separate condition-level observation populations. Three operating conditions plus four corners sharing B=LL still give six unique production solutions, with no claim of experimental replication. Current-mesh fine effects and dependent passage/cooling quantities retain their limits.

## Direct original-source support inspected

| R3 use | Direct original locator and reading | Support and boundary |
|---|---|---|
| Conservative enthalpy and coordinate balance, Eqs1/3; latent-inclusive storage discussion | Van Elsen author PDF pp4–5 §2 and p21 Eqs32–35, local `citations/text/vanelsen2007.txt` | **Full** for the method family and energy accounting. The source uses a different latent distribution; the manuscript explicitly adopts its own linear phase closure and derives the frame equation. It does not attribute FiPy implementation to this paper. |
| Density, 1290–1350 °C endpoints, supplier table knots and calculated/measured provenance | Special Metals original bulletin p2 Tables2/3 and footnotes, local `citations/text/specialmetals625.txt` | **Full** for general-alloy input values and provenance. **Absent** for coupon-specific liquid properties; R3 correctly presents L/H as continuation scenarios. |
| Latent heat 280000 J/kg; closest directional-conductivity AMMT comparison | Kollmannsberger author PDF p6 Table5, pp9–10 §4.3, pp10–11 conclusion | **Full** for the reused model parameter and calibrated effective directional closure. Its conductivity dataset endpoint differs from the current supplier table. R3 does not claim an identical input dataset or controlled solver ranking. Its source-temperature-validity caution is directly present in the original. |
| Adopted linear fraction closure; Gaussian D4sigma convention; alternative dynamic source | Coleman author PDF p5 Eq1 paragraph, p6 Eqs2–3, pp17–18 calibration/case definition and phase assumptions | **Full** for closure precedent, beam convention and stated 195 W/800 mm/s source comparison. **Partial** if used to establish this coupon's freezing law: the original uses 1620–1410 K with a nonequilibrium eutectic endpoint. R3 identifies that difference and calls the law adopted. |
| Geometric fit versus surface-temperature ambiguity | Myers published PDF §4.1 pp7–9 and Fig8; direct text lines587–613 | **Full** for multiple 316L Fresnel/accommodation combinations fitting geometry while giving different temperature profiles. **Absent** for equally refitted current IN625 continuation branches; R3 explicitly excludes that extrapolation. |
| Spatial profile versus fixed-location time history | Hooper published PDF pp10–11, Fig14 and conclusions | **Full** for fixed-location histories, pulsed scanning and turn-event distinctions. No latent-heat cause from Ti64 is assigned to the current factorial result. |
| Fluid trajectories differ from stationary conduction passage | Hou published PDF pp9–10, §4.3 and Fig14/AppendixC comparison | **Full** for the reported narrower near-surface CFD excursions and hotter subsurface excursions in Ni–20Cr. **Absent** for validation of the present IN625 interval; R3 preserves that boundary. |
| Geometry verification, solidification diagnostics and grain-structure comparison; interface speed versus beam speed | Plotkowski author PDF §3.3 pp16–19 and §4 pp20–24 | **Full** for that methodological distinction and transient multi-line interface-speed departure, in AlSi10Mg laser/IN718 electron-beam cases. **Absent** for present IN625 grain/segregation validation, which R3 does not claim. |
| Experimental length operator, mapping by scan speed and exemplar cooling limitations | Lane full published-text paragraphs P21–34, P36–42, P49–60 | **Full** for rear second-derivative/front-threshold distinction, below-solidus interval and cooling-rate limitations. The current two-solidus observer is correctly distinguished. |
| Composition-based superalloy estimates including IN625 | Mills published PDF §9 pp6–7, Figs12–13 | **Full** for estimated thermophysical functions and limited/larger-error liquid-state information. **Absent** for selecting LL or HH for this coupon, which R3 does not claim. |

The source-support table records the current sentence-level uses, not just matching titles. Reuse of the same citation at two fitting locations is appropriate where the original actually supports both uses; it does not increase independent evidence count.

## Optional clarity and preserved limits

The Results p8 “statistically resolved” phrase could be changed to “resolved by this uncertainty-scale comparison” to align exactly with the declared descriptive use of U. I do **not** classify the current negative trend statement as a demonstrated factual defect: the zero-correlation scale is 38.8946 µm, and even the minimum covariance-compatible expanded scale from the displayed values is `|32.57−21.26|=11.31 µm`, above the displayed nominal 11 µm difference. The actual difference covariance and a formal trend test were not established. This optional wording must not be used to demand a new statistical study or to imply a resolved trend.

The positive expression labelled interval-mean cooling rate is a cooling magnitude. An optional word “magnitude” beside Eq6 would remove a possible signed-derivative ambiguity; the calculations and interpretation are consistent, so this is not a numerical defect.

The absence of an independent 1350–1290 °C trajectory, coupon-matched liquid properties, nonequilibrium freezing validation and branch-specific three-dimensional fine-effect refinement remains a material evidence boundary, explicitly preserved in the paper. It is not a new blocker for the scoped deterministic comparison. No field-level implementation reproduction, public-repository availability audit, human authorship verification or current official AM format-compliance check was performed here. The available AM examples establish editorial conventions only. Scientific evidence has not been upgraded by editorial improvement or by this review.

## Revision verification

One verification round is available within this contract. At initial return the two actionable findings above are **open**; the reviewer has not modified the source. A changed manuscript and matching proof must be read before clearing either finding. Optional preferences and unresolved physical-validation boundaries must remain separate from those two repairs.
