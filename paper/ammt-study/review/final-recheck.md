# Final limited recheck

Date: 2026-10-01. Reviewer: assigned `ammt_manuscript_review` agent. Contract: recheck initial R1–R5, current-mesh depth/phase-span scope, the Myers thermal-ambiguity and Lane absorption citations, and the corresponding rebuilt pages. Only this file is written. The manuscript and original case remain unchanged by this reviewer; no PDE or new scientific experiment was run. The initial findings remain in `review.md`.

## Disposition

The identified caption, positioning and reproducibility defects have been repaired in the actual source and affected rendered pages. The revised text supports delivery as a bounded English discrepancy-and-continuation-sensitivity manuscript. This finding-specific closure is **not a scientific PASS, a field-wide originality clearance, an AM editorial decision or a submission-readiness certificate**.

The explicit contribution statement now gives a reader the actual diagnostic addition: freeze the source fit, separate conductivity from sensible-storage continuation, and follow the paired rear solidus/liquidus positions to distinguish translation from widening. The remaining **Additive Manufacturing contribution risk is editorial significance and breadth**, not a newly found data contradiction. The study is still a one-alloy, three-condition, one-B-factorial diagnostic within a model and operator definition. This limited recheck adds no new scientific requirements or demand for more PDE runs.

## Actual inputs and pages checked

I read the revised `manuscript.tex`, selected original source records needed to verify the new method/citation details, the `.bbl`/BibTeX records, the actual PDF and its supplied page renders. The 22-page intermediate build was examined first. After the unit/render repair and its three local space corrections, the final PDF is a **21-page preprint**, with metadata creation time 16:59:34 on this date; its page images were rechecked at the changed locations. The source line locators below refer to that 21-page source and are paired with subject/quotes.

Read/inspection evidence included:

- Revised source at Introduction, Materials/Methods, calibration, figure captions, Results/Discussion and Appendix A.
- `qa/contact-sheet-1.png`–`contact-sheet-3.png`, and full affected-page images, including pp. 3, 4, 7, 10–13, 15, 18–21 across the successive renders.
- Original executed calibration driver `verification/fipy-application-calibration-r13/executed-calibrate_application.py`, lines 124–157: the [0.2,0.4] bracket, safeguarded secant clipping by 5% at either end, stopping at absolute residual below 0.5 µm, and local slope/sensitivity construction.
- The actual Special Metals bulletin p. 2, read through the existing read-only extraction helper: density 8.44 g/cc, melting interval 1290–1350 °C, Table 2 cp footnote “Calculated,” and Table 3 conductivity measurement footnote. Original Kollmannsberger `modelVerification.tex`, its constant-input table, confirms adopted latent heat 2.8e5 J/kg.
- Myers published full text, the geometry/thermal comparison around Fig. 8; Lane absorption full text, §2.2 P34–35 and its measurement caveats, alongside the bibliography entries.
- Final PDF text extraction was used to locate all time-unit output sites, followed by image inspection; it was not substituted for caption/layout inspection. No `undefined`, `Missing character` or `Overfull` match was found in the inspected build log. The actual page checks remain the basis for render findings.

This is a separate-context, same-model-family recheck and retains the exposure disclosure in the initial review. No statistical independence or human peer-review authority is implied.

## Finding-specific closure

| Initial finding | Verified repair and actual page evidence | Disposition |
|---|---|---|
| **R1 — stale captions** | Source `manuscript.tex:198`, Fig. 2, now names **(a)** surface solidus contours and **(b)** fusion envelopes; actual p. 11 matches the two side-by-side panels. Source `:210`, Fig. 3, names **(a)** nominal B→C percent changes, **(b)** class-mean aspect ratios, **(c)** model spans and **(d)** passage times; actual p. 12 matches. The caption explicitly says uncertainties are not propagated and cooling rates are not plotted. | **CLOSED**, source and actual caption/figure pairs verified. |
| **R2 — implicit scientific delta** | Source `:38`, Introduction, and actual p. 3 state the fixed-source, separate k/cp continuation and paired-boundary diagnostic relative to the cited source/anisotropy line. Myers' geometry/thermal ambiguity is made explicit at `:34`, actual p. 2. The manuscript does not assert a new heat equation, first-in-field status or physical-property identification. | **CLOSED for the specific positioning/reader gap.** AM significance and field-wide originality remain an unestablished editorial risk; this closure does not clear that risk. |
| **R3 — undefined local face Pe operator** | Appendix A, source `:301`, actual p. 19, gives `|Pe_f|=|u·n_f|d_f/D_f`, defines face distance/diffusivity, selects interior axial faces adjacent to at least one mushy cell, and says percentiles are unweighted. It explicitly states that populations change with solved temperature and that the statistic depends on the discretization/region. This matches the original extraction code inspected in the initial review. | **CLOSED** as an operator-definition defect. The median remains a discrete model diagnostic, not a measured liquid-flow or fixed-volume causal quantity. |
| **R4 — domain coordinate-unit notation** | Source `:96`, actual p. 5, now assigns mm to each of ξ, y and z intervals instead of appending mm³ to the tuple. The extents themselves are unchanged. | **CLOSED**, source and rendered dimensional notation verified. |
| **R5 — material/calibration source trail** | Source `:78`, actual p. 4, directly identifies calculated typical cp, measured supplier k, coupon distinction and constant-input lineage. Source `:133`, actual p. 7, reports the executed safeguarded secant, local bracket/trials, accepted 0.5 µm residual, final +0.158 µm residual, local slope and Δη sensitivity scale. It explicitly excludes a posterior/global-identifiability interpretation and propagation into geometry. Appendix source `:299`, actual p. 19, supplies both final secants, 0.0216216 W m⁻¹ K⁻² and 0.225225 J kg⁻¹ K⁻², matching the retained last two table knots. | **CLOSED** for the reported provenance/method gap. No independent high-temperature coupon measurements or combined predictive uncertainty were thereby created. |

## Fine-contrast scope and citation use

**Depth and phase-span reporting:** source `:246`, actual p. 13, now calls cancellation the “current-mesh depth contrast.” Source `:270`, actual p. 16, explicitly calls the depth decomposition and near-1-µm phase-span changes “recorded arithmetic at this mesh,” without the branch-specific evidence needed for a fine physical ranking. Table 3 retains its small-transverse-effect qualification. The small width interaction also remains unranked. The original **reporting-scope concern is CLOSED**; actual branch-specific fine-contrast adequacy remains unresolved and is not silently promoted. The major 34–43 µm tail response continues to be interpreted at its previously bounded scope.

**Myers:** the new statement accurately uses an orthogonal thermal-observation result: multiple Fresnel/accommodation parameter combinations fit no-powder 316L geometry while producing different thermal profiles. The manuscript uses this as a limit on geometry-based thermal inference, not as a measurement of the present IN625 field. The claim is supported by the original Fig. 8 discussion inspected, not only by metadata or a paper title.

**Lane absorption:** source `:259`, actual p. 15, correctly distinguishes unreflected power from energy actually deposited into the substrate, with plume/evaporative measurement differences. Lane §2.2 P34 explicitly says the reflectometer quantity does not imply all energy is absorbed into the melt pool/substrate; P35 describes discrepancies with calorimetry. The next sentence—that the fitted conduction-model factor is further removed from intrinsic absorptivity—is a reasonable model/operator interpretation supported by the present length-proxy fit. No absorption number, keyhole transition or process condition from that different experiment is transplanted into this study.

The bulk-conductivity versus surface-recovery limitation remains explicit in §4.2. The text does not infer reduced integrated rear flux or identify Marangoni flow from a lower conductivity/Pe comparison.

## Actual render corrections found during recheck

The 22-page intermediate PDF rendered `\si{\micro\second}` as **“ţs”**, although the log had no missing-character report. This was observed in the actual p. 3 table and located at all affected time-unit sites by PDF text extraction. It was a real output glyph defect; the numerical values and intended source units were not wrong.

The producer replaced these output sites with the explicit math `\us` macro, `\mu\mathrm{s}`. In the 21-page rebuild I verified the proper **µs** glyph in the p. 3 table and throughout PDF text extraction, with no remaining “ţ”. Source units/data were unchanged. The replacement initially consumed a following TeX space at three prose locations (“µstracks,” “µsand,” “µsbecause”). These were corrected with `\us{}` at source lines 59, 203 and 289. I then read the final source, checked all PDF time-unit text sites, and viewed the final pp. 4, 10 and 18 directly: “20 µs tracks,” “120.74 µs and,” and “67.33 µs because” now render with the required separation. **The actual unit-glyph and local-spacing defects are CLOSED.** This closure is based on the final output, not the absence of compile warnings.

The intermediate p. 22 held only the final reference. The 21-page bibliography uses readable `\small` text and ends normally on p. 21 with several entries, including Lane absorption [13]. I viewed pp. 20 and 21 directly: reference text, links, protected IN625/FiPy/SciPy names and the repaired author-accent forms render legibly, without the former single-entry final page. This is a formatting closure, not scientific validation.

## Remaining boundaries and submission dependencies

- **AM contribution risk remains:** a specific, honest diagnostic addition is now expressed, but this recheck does not establish field-wide originality, broad applicability or whether AM editors will consider its significance sufficient. Do not manufacture superiority or predictive claims to make the framing stronger.
- **Fine-effect adequacy remains limited:** reporting is repaired; submicrometre branch rankings are still unsupported. No new solver requirement is imposed for this bounded draft.
- **Human author and declaration facts remain unresolved:** affiliations/authorship, complete human verification, final disclosure wording, funding and competing interests must be completed truthfully before submission.
- **Current AM guide remains unverified:** abstract/file/anonymity/highlights/graphical-abstract requirements are not certified by the Elsevier preprint template or this review.
- **The scientific scope is unchanged:** nonblind comparisons, distinct experimental operators/populations, separate Lane U, high-temperature extrapolation and omitted flow/evaporation limits remain. Manuscript repair does not create independent experimental evidence.

The return recommendation is to preserve the revised bounded manuscript and the remaining editorial/submission dependencies. Close only the defects actually checked above; do not replace this record with a global scientific or journal PASS.
