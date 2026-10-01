# R2 citation map

The bibliography retains 47 verified identities: 37 have an immediate, bounded use and 10 are held as metadata-only candidates. This is a research-use map, not a instruction to cite every entry. Existing14keys are preserved verbatim. Reading of the original set is documented in the [original exemplar notes](../../literature/exemplar-notes.md); new retrieval and selected-page reading are recorded in [source-ledger.json](source-ledger.json). No inferred citation minimum is treated as a journal requirement.

## Paragraph-level use

- Introduction paragraph1: king2015, hooper2018, myers2023 — process relevance and the need to interpret thermal conditions.
- Introduction paragraph2: rosenthal1946, vanelsen2007, rubenchik2018, promoppatum2017, kollmannsberger2019 — established affordable models, their useful successes and conditions.
- Introduction paragraph3: ross2022, whalen2021, heatsourcebayes2024, dynamic2024 — successful calibrated-source, uncertainty and transfer strategies. Do not imply that fixed calibration cannot ever transfer.
- Introduction paragraph4: myers2023, lane2020absorption, trapp2017, weeks2026 — geometry, effective absorption and observation mapping carry different information.
- Introduction paragraph5: yang2024, soares2026, hong2026, naderi2023 — current sensitivity/reliability/diagnosis work. The increment is narrower than “material sensitivity” or “conduction breakdown.”
- Introduction closing: this study design/results, supported by the existing evidence dossier; specialmetals625 supplies the actual property-table limits. Do not attach literature citations as if those papers produced our values.
- Methods: lane2020, nist2018, specialmetals625, vanelsen2007, kollmannsberger2019, fipy2009, scipy2020, oberkampf2002 — each with the specific role listed below.
- Discussion: compare current findings with the closestYang/Soares/Hong/Coleman/Whalen precedents; use khairallah2016, cunningham2019, bayat2019, martin2019 only for bounded alternate-physics context. mills2006/pottlacher2001 suggest property-evidence routes; weaver2024 supplies future benchmark design context. Peripheral powder sources matthews2016/gasliquid2025 need only be cited if that extension is actually discussed.

## Source-by-source use and boundary

### `lane2020` — usable_with_scope

**Use:** Methods observation operators; Results geometry comparison; Discussion material-time interpretation.

**Supported point:** AMMT length/cooling and cross-sectional measurement definitions, sampling and uncertainty.

**Read scope:** Prior direct full HTML §§2–5, documented with paragraph ranges and official source identity in ../../literature/exemplar-notes.md. No local original-text path is asserted here.

**Limit or counterevidence:** Radiance-length front/rear rules differ from two solidus crossings; cooling exemplars are not calibration data. Separate populations and uncertainty budgets.

### `kollmannsberger2019` — usable_with_scope

**Use:** Introduction existing geometry solutions; Methods benchmark lineage; Discussion shape discrepancy and competing closure/source choices.

**Supported point:** Nonlinear temperature/phase-change conduction can reproduce AMMT geometry with measured input and effective directional conductivity; scalar eta alone is insufficient for all geometry in its stated model.

**Read scope:** Prior direct author-preprint §§2–5, particularly §4.2–4.3 pp8–10 Tables7–10; documented original notes.

**Limit or counterevidence:** Its anisotropic closure and source differ from the current isotropic circular Gaussian. Authors explicitly do not establish internal temperature validity.

### `vanelsen2007` — usable_with_scope

**Use:** Introduction computational hierarchy; Methods moving-frame and enthalpy formulation; Discussion conditional latent contribution.

**Supported point:** Moving-source analytical and nonlinear enthalpy formulations; source representation and material-property effects need separate treatment.

**Read scope:** Prior direct author-preprint §§2–5, pp4–6 and16–24; equations32–35 in original notes.

**Limit or counterevidence:** Analytical solutions require constant properties/semi-infinite assumptions. Ti64 latent response is not an IN625 quantitative result.

### `vanini2024` — hold_metadata_only

**Use:** Hold pending direct substantive reading by journal/coordinator.

**Supported point:** Candidate: alternatives to heat-source calibration.

**Read scope:** Verified DOI and Crossref/OpenAlex identity only; public metadata no abstract.

**Limit or counterevidence:** Title/metadata only in this worker return. Do not use title as proof of calibration-free accuracy or generality.

### `ross2022` — usable_with_scope

**Use:** Introduction successful calibrated-source route; Discussion a source-based alternative to changing conductivity.

**Supported point:** An inverse heat-conduction procedure fits double-ellipsoid heat-source parameters from solidification-boundary temperatures; trends allow interpolation to intermediate power/speed.

**Read scope:** Full scholarly abstract reconstructed from OpenAlex inverted index on1October2026; no fulltext learning claim.

**Limit or counterevidence:** Published abstract only. Calibration incorporates effective absorption/vapour penetration, not identification of intrinsic eta or proof for the present source.

### `myers2023` — usable_with_scope

**Use:** Introduction central precedent; Discussion independent thermal data and limitations.

**Supported point:** Geometry-fitting parameter combinations can produce different thermal profiles; two-colour measurements offer an additional discriminating observable.

**Read scope:** Prior direct version-of-record Intro, Methods, Results, Discussion and Conclusion pp1–10; figure8 p9. Original notes retain links.

**Limit or counterevidence:** Already establishes this observation. Its FLOW-3D/source/surface and instrument assumptions differ; no universal mathematical forward nonuniqueness follows.

### `hooper2018` — usable_with_scope

**Use:** Introduction importance of thermal interpretation; Discussion independent measurements and spatial-versus-material time.

**Supported point:** Two-wavelength thermography measures spatial and temporal thermal histories relevant to gradients/cooling, with explicit instrument calibration.

**Read scope:** Prior direct version-of-record §§2.1–2.6 and3.4–3.6 pp2–4,10–12; figures13–14.

**Limit or counterevidence:** Close-band emissivity assumption, registration, plume/angle/reflection/noise remain. Ti64 and scan-turn transients differ from current quasi-steady bare IN625.

### `liu2024` — hold_metadata_only

**Use:** Hold pending substantive journal/coordinator reading.

**Supported point:** Candidate: scalable path-level thermal history and image validation.

**Read scope:** Verified DOI and Crossref/OpenAlex identity only; no public abstract returned.

**Limit or counterevidence:** Title/metadata only in this worker return; do not claim exact validation protocol from title.

### `fipy2009` — usable_with_scope

**Use:** Methods implementation.

**Supported point:** FiPy as the finite-volume Python PDE implementation.

**Read scope:** Existing verified software citation and implementation record; not counted as a scientific-method exemplar.

**Limit or counterevidence:** Software citation supports implementation lineage; it does not verify this discretization or validate physical temperatures.

### `scipy2020` — usable_with_scope

**Use:** Methods interpolation/root finding/implementation as applicable.

**Supported point:** SciPy numerical algorithms used by the implementation.

**Read scope:** Existing verified software citation and implementation record; not a fulltext research exemplar.

**Limit or counterevidence:** Software pedigree does not replace numerical or physical checks.

### `oberkampf2002` — usable_with_scope

**Use:** Methods verification and Discussion limits.

**Supported point:** Numerical verification and physical validation answer different questions.

**Read scope:** Existing verified methodological source from original dossier; scope restricted to standard verification/validation distinction.

**Limit or counterevidence:** General CFD methodology, not an LPBF accuracy tolerance or certification of this calculation.

### `specialmetals625` — usable_with_scope

**Use:** Methods property provenance and continuation figure; Discussion closure uncertainty.

**Supported point:** Supplier typical IN625 density/melting range and solid-state cp/k tables; cp endpoint1093°C and k endpoint982°C are below adopted solidus.

**Read scope:** Prior direct August2013 bulletin pp1–2 Tables2–3; source link in original bibliography and notes.

**Limit or counterevidence:** cp is calculated; k is measured for specified annealed material; typical values are not specifications or measured liquid functions for this coupon.

### `nist2018` — usable_with_scope

**Use:** Methods references/populations; Results shape comparison.

**Supported point:** Official AMB2018-02 width/depth class means and SDs.

**Read scope:** Prior direct official current page §2 Table2,1October2026; created2018/updated2025.

**Limit or counterevidence:** Class SD, individual measurement estimate and Lane expanded U(k=2) are different quantities/populations.

### `lane2020absorption` — usable_with_scope

**Use:** Introduction absorption-observation route; Discussion fitted eta and alternate causes.

**Supported point:** Direct unreflected-power/absorption and morphology evidence distinguishes dynamic, integrated and ex-situ observables.

**Read scope:** Prior direct version-of-record Intro/Methods/Results/Discussion/Conclusion pp1–12; §§2.2,3.2.1,4 especially pp4–5,9–11.

**Limit or counterevidence:** Unreflected power includes plume and mass-energy pathways; reflection alone does not isolate substrate heating. Different spot/power/speed from current case.

### `rosenthal1946` — usable_with_scope

**Use:** Introduction analytical conduction lineage or Methods moving-source context.

**Supported point:** Moving-source heat-flow solutions and cooling-time/rate predictions are established foundations.

**Read scope:** Complete Crossref/OpenAlex scholarly abstract; no original fulltext inspected. Archive journal field retrospectively differs from original Transactions of ASME.

**Limit or counterevidence:** The historical abstract concerns welding/metal treatment and steel conditions, not near-source finite-Gaussian LPBF temperature accuracy.

Persistent source: https://doi.org/10.1115/1.4018624

### `goldak1984` — hold_metadata_only

**Use:** Hold; optional lineage only after reading.

**Supported point:** Candidate: double-ellipsoid welding source foundation.

**Read scope:** Crossref/OpenAlex identity only.

**Limit or counterevidence:** Metadata only; no source details imported. Current model is a surface Gaussian.

Persistent source: https://doi.org/10.1007/BF02667333

### `debroy2018` — hold_metadata_only

**Use:** Hold; broad review is optional, not indispensable.

**Supported point:** Candidate broad process-structure-property review.

**Read scope:** Crossref/OpenAlex identity only.

**Limit or counterevidence:** Metadata only; do not count as read background or substitute for directly read King/Sarkar.

Persistent source: https://doi.org/10.1016/j.pmatsci.2017.10.001

### `king2015` — usable_with_scope

**Use:** Introduction affordable models and thermal interpretation; Discussion omitted physics.

**Supported point:** LPBF spans coupled physical, material and computational scales; geometry and thermal histories have process-structure roles.

**Read scope:** Author manuscript PDF pp3–6 abstract/Introduction; rest of55pages not claimed read.

**Limit or counterevidence:** Review/context, not proof of the present closure or quantitative accuracy.

Local source: [pdfs/king2015.pdf](pdfs/king2015.pdf); [page-marked text](text/king2015.txt).

Persistent source: https://doi.org/10.1063/1.4937809

### `khairallah2016` — usable_with_scope

**Use:** Introduction high-fidelity route; Discussion source/flow/evaporation alternatives.

**Supported point:** High-fidelity powder-resolved models connect recoil/Marangoni/radiative/evaporative physics with melt flow and pores.

**Read scope:** Author-manuscript PDF p3 abstract and pp5–7 Introduction/physics, including no reflection tracking and35µm powder assumption; final metadata separately verified.

**Limit or counterevidence:** Read author manuscript uses earlier title/three-author cover; final DOI has four authors. Powder316L and direct rays differ from bare IN625. Does not diagnose this residual.

Local source: [pdfs/khairallah2016.pdf](pdfs/khairallah2016.pdf); [page-marked text](text/khairallah2016.txt).

Persistent source: https://doi.org/10.1016/j.actamat.2016.02.014

### `matthews2016` — usable_with_scope

**Use:** Discussion only if situating powder generalization boundary.

**Supported point:** Powder denudation depends on vapour flux, gas-driven entrainment and pressure; experiments constrain mechanisms.

**Read scope:** Complete Crossref/OpenAlex scholarly abstract; no fulltext.

**Limit or counterevidence:** Full abstract only; powder/gas mechanism absent from bare-plate study and cannot explain its residual without evidence.

Persistent source: https://doi.org/10.1016/j.actamat.2016.05.017

### `trapp2017` — usable_with_scope

**Use:** Introduction source-calibration burden; Discussion eta meaning.

**Supported point:** Calorimetric effective absorption depends on power, regime and powder/bare conditions.

**Read scope:** Complete Crossref/OpenAlex scholarly abstract; no fulltext.

**Limit or counterevidence:** Full abstract only; measurements on316L/Al/W cannot provide actual IN625 eta. Do not equate fitted model eta with material absorptivity.

Persistent source: https://doi.org/10.1016/j.apmt.2017.08.006

### `simonds2018` — usable_with_scope

**Use:** Discussion energy coupling and measurement distinction.

**Supported point:** Time-resolved optical coupling and calorimetry can differ because of mass loss; calibrated independent input/output data aid model assessment.

**Read scope:** Author manuscript PDF pp1–3 abstract/Introduction; direct instrumental claim bounded to that text.

**Limit or counterevidence:** 10ms stationary316L spot weld, not current moving-track conditions. Source is an author arXiv manuscript, not a studied publisher layout.

Local source: [pdfs/simonds2018.pdf](pdfs/simonds2018.pdf); [page-marked text](text/simonds2018.txt).

Persistent source: https://doi.org/10.1103/PhysRevApplied.10.044061

### `cunningham2019` — usable_with_scope

**Use:** Discussion potential omitted free-surface physics; broader Introduction route if needed.

**Supported point:** Synchrotron imaging directly observes vapour-depression/keyhole sequence and power-density-dependent transition.

**Read scope:** Complete scholarly OpenAlex abstract reconstructed and read; fulltext not inspected.

**Limit or counterevidence:** Scholarly abstract only. No regime label for current AMMT case is inferred. Crossref editor précis is not used as scientific abstract.

Persistent source: https://doi.org/10.1126/science.aav4687

### `martin2019` — usable_with_scope

**Use:** Discussion scope of quasi-steady and omitted transients, only if needed.

**Supported point:** X-ray experiments plus high-fidelity model connect laser turn-around transients to pore formation.

**Read scope:** Version-of-record PDF pp1–2 abstract/Introduction; remaining8pages not claimed read.

**Limit or counterevidence:** Ti64 transient turn-around, unlike this steady straight-track field; no causal transfer to current width/depth residual.

Local source: [pdfs/martin2019.pdf](pdfs/martin2019.pdf); [page-marked text](text/martin2019.txt).

Persistent source: https://doi.org/10.1038/s41467-019-10009-2

### `king2014` — hold_metadata_only

**Use:** Hold; not indispensable.

**Supported point:** Candidate historical keyhole observation.

**Read scope:** Crossref/OpenAlex identity only.

**Limit or counterevidence:** Metadata only. Use directly read Cunningham abstract/Khairallah text for bounded physics context instead.

Persistent source: https://doi.org/10.1016/j.jmatprotec.2014.06.005

### `rubenchik2018` — usable_with_scope

**Use:** Introduction fast-model successes; Discussion need for case-specific diagnostics.

**Supported point:** Eagar–Tsai conduction scaling in normalized energy and dwell/diffusion time can organize cross-material dimensions and reduce computation.

**Read scope:** Accepted-manuscript PDF pp4–7 abstract and Introduction/scaling scope; no whole-paper read claim.

**Limit or counterevidence:** Neglects flow, evaporation, surface tension and powder; empirical collapse is conditional and later Naderi finds important limits.

Local source: [pdfs/rubenchik2018.pdf](pdfs/rubenchik2018.pdf); [page-marked text](text/rubenchik2018.txt).

Persistent source: https://doi.org/10.1016/j.jmatprotec.2018.02.034

### `bertoli2017` — hold_metadata_only

**Use:** Hold; exclude from active prose.

**Supported point:** Candidate energy-density limitations.

**Read scope:** Crossref/OpenAlex identity only.

**Limit or counterevidence:** Metadata only; title is not evidence. Current paper need not make a broad VED claim.

Persistent source: https://doi.org/10.1016/j.matdes.2016.10.037

### `ye2019` — usable_with_scope

**Use:** Introduction measured/scaled coupling route; Discussion calibrated or correlated absorption.

**Supported point:** Absorption and melt-depth scaling couple laser conditions, material response and geometry across studied alloys.

**Read scope:** Complete Crossref abstract and author manuscript PDF p3–4 abstract/Introduction start; final metadata verified separately.

**Limit or counterevidence:** Author manuscript title/version differs from final journal title; empirical scaling is not independent eta truth for this coupon. Later limits in Naderi/Hong apply.

Local source: [pdfs/ye2019.pdf](pdfs/ye2019.pdf); [page-marked text](text/ye2019.txt).

Persistent source: https://doi.org/10.1002/adem.201900185

### `mills2006` — usable_with_scope

**Use:** Methods/Discussion property provenance and cheaper alternative to full new measurement.

**Supported point:** Composition-based estimates of thermophysical properties help where experiments are unavailable, including liquid/phase concerns.

**Read scope:** Version-of-record J-STAGE PDF pp1–2 abstract/Introduction; remaining8pages not claimed read.

**Limit or counterevidence:** Authors explicitly do not present estimates as a replacement for measurement. Alloy-composition estimates are not current IN625 coupon properties.

Local source: [pdfs/mills2006.pdf](pdfs/mills2006.pdf); [page-marked text](text/mills2006.txt).

Persistent source: https://doi.org/10.2355/isijinternational.46.623

### `pottlacher2001` — usable_with_scope

**Use:** Discussion feasible high-temperature evidence routes, if needed.

**Supported point:** Fast resistive heating measures solid/liquid enthalpy/cp; conductivity can be estimated via resistivity/Wiedemann–Franz.

**Read scope:** Complete scholarly Crossref/OpenAlex abstract; no fulltext.

**Limit or counterevidence:** Actual first author is Hosaeus. IN718, not IN625; no numerical substitution for current liquid functions.

Persistent source: https://doi.org/10.1068/htwu340

### `promoppatum2017` — usable_with_scope

**Use:** Introduction successful affordable models; Discussion source/loss assumptions.

**Supported point:** FE and Rosenthal can both reasonably estimate IN718 geometry within studied conditions, while differing in absorption sensitivity and high-input shape.

**Read scope:** Complete Crossref/OpenAlex scholarly abstract; no fulltext (public PDF403).

**Limit or counterevidence:** Full abstract only; qualified success prevents a strawman claim that analytical/conduction models always fail. Microstructure result not replicated here.

Persistent source: https://doi.org/10.1016/J.ENG.2017.05.023

### `coen2022` — hold_metadata_only

**Use:** Hold pending targeted access; optional because other analytical-validation sources are usable.

**Supported point:** Candidate methodological validation of analytical pools.

**Read scope:** Crossref/OpenAlex identity only.

**Limit or counterevidence:** Metadata only; details can change gap appraisal, not current measured evidence.

Persistent source: https://doi.org/10.1016/j.jmatprotec.2022.117547

### `whalen2021` — usable_with_scope

**Use:** Introduction prior property/uncertainty treatment; Discussion distinction from deterministic continuation scenarios.

**Supported point:** An adapted Eagar–Tsai model includes temperature-dependent/powder properties, infers apparent absorption/porosity distributions and propagates depth uncertainty.

**Read scope:** Author-manuscript PDF pp1–4 abstract/Introduction,pp7–8 model properties/powder,pp19–20 external comparison/Conclusion.

**Limit or counterevidence:** 316L; input distributions fitted to geometry are effective parameters. External printability comparison is qualitative with different ratio thresholds; not internal thermal validation.

Local source: [pdfs/whalen2021.pdf](pdfs/whalen2021.pdf); [page-marked text](text/whalen2021.txt).

Persistent source: https://doi.org/10.1007/s40192-021-00238-z

### `naderi2023` — usable_with_scope

**Use:** Introduction known regime/transfer limits; Discussion no cross-condition ranking.

**Supported point:** Scaling-law fidelity depends on material and regime; revised separate regime fits improve studied depth errors.

**Read scope:** Version-of-record PDF pp1–2 Intro/abstract,p5 measurement conditions,pp13–14 Conclusions; print2023 vs online2022.

**Limit or counterevidence:** Not a universal condemnation of thermal conduction. Revised fits and multi-alloy depth data do not examine current local nonlinear cp/k continuations.

Local source: [pdfs/naderi2023.pdf](pdfs/naderi2023.pdf); [page-marked text](text/naderi2023.txt).

Persistent source: https://doi.org/10.1007/s40192-022-00289-w

### `bayat2019` — usable_with_scope

**Use:** Introduction physically richer route; Discussion alternate physics.

**Supported point:** High-fidelity ray-reflection/free-surface flow model plus XCT validates keyhole-porosity mechanisms in Ti64.

**Read scope:** Uncorrected-proof PDF pp1–2 abstract/Introduction; no complete numerical method read claim.

**Limit or counterevidence:** Uncorrected proof, powderTi64; scope differs. No current residual/keyhole label follows.

Local source: [pdfs/bayat2019.pdf](pdfs/bayat2019.pdf); [page-marked text](text/bayat2019.txt).

Persistent source: https://doi.org/10.1016/j.addma.2019.100835

### `weaver2024` — usable_with_scope

**Use:** Methods benchmark lineage or Discussion future multi-observable controlled measurements.

**Supported point:** AMBench2022 provides controlled IN718 track/pad geometry, uncertainties and heat-buildup effects.

**Read scope:** Complete Crossref/OpenAlex scholarly abstract; no fulltext (PMC request403).

**Limit or counterevidence:** Different year/material/dataset; cannot supply AMB2018IN625 statistics or repair Hong dataset identity.

Persistent source: https://doi.org/10.1007/s40192-024-00355-5

### `yang2024` — usable_with_scope

**Use:** Introduction direct material-sensitivity precedent; Discussion scope of our independent closure decomposition.

**Supported point:** Analytical LPBF models have already quantified k/cp and source/laser sensitivity of thermal/geometry outputs.

**Read scope:** Version-of-record18pp PDF: abstract/Intro1–2; methods3–6; sensitivity9,12–15; Conclusion16.

**Limit or counterevidence:** Constant-property Ti64; one-factor changes and radar weighting are not nonlinear high-temperature four-corner closure interactions. Some extreme peak values and a unit typo must not be imported as physical truth.

Local source: [pdfs/sigler2024.pdf](pdfs/sigler2024.pdf); [page-marked text](text/sigler2024.txt).

Persistent source: https://doi.org/10.3390/ma17112565

### `soares2026` — usable_with_scope

**Use:** Introduction recent reliability assessment; Discussion observation/shape discrepancies and correlation versus agreement.

**Supported point:** Thermal-camera and post-process comparisons expose different agreement for surface and depth; high correlation can coexist with biased scale.

**Read scope:** Version-of-record27pp PDF §§2.1 pp3–6;3.2 pp12–13;3.2.2p17;3.3pp17–18;Discussion18–21;Conclusion21–22.

**Limit or counterevidence:** Analytical Gaussian fixed0.8Tmelt properties, powder corrections and no explicit phase change. Camera calibration uses melting/metallography; not wholly independent temperature truth. Proposed depth correction is not prospective validation.

Local source: [pdfs/reliability2026.pdf](pdfs/reliability2026.pdf); [page-marked text](text/reliability2026.txt).

Persistent source: https://doi.org/10.3390/app16125850

### `hong2026` — usable_with_scope

**Use:** Introduction direct diagnostic overlap; Discussion controls needed before attributing conduction-model discrepancy.

**Supported point:** A recent fitting-free diagnostic asks whether an Eagar–Tsai conduction model requires physically infeasible absorption to explain measured depth; sensitivity/effective-diffusivity controls test robustness.

**Read scope:** Version-of-record21pp PDF Intro1–3;Methods2.1–2.4pp4–7;robustness3.4pp12–13;correction3.5p14;Discussion16–18;Conclusion18;refs20–21.

**Limit or counterevidence:** Effective/constant-property231bare tracks across datasets; IN625 empirical absorption and data-label concern require caution. Does not examine our nonlinear high-T functions or rear Ts/Tl split. Its mechanism inference cannot be transferred.

Local source: [pdfs/fittingfree2026.pdf](pdfs/fittingfree2026.pdf); [page-marked text](text/fittingfree2026.txt).

Persistent source: https://doi.org/10.3390/ma19153290

### `solidpath2024` — hold_metadata_only

**Use:** Hold; scientific question recorded in research-line.md.

**Supported point:** Critical candidate: alloy solidification path and melt-pool response.

**Read scope:** Crossref/OpenAlex identity only; parent handled one targeted publisher session.

**Limit or counterevidence:** Metadata only; do not claim lack of related latent/solidification analysis. This limits breadth/priority of novelty claim.

Persistent source: https://doi.org/10.1016/j.ijheatmasstransfer.2024.125632

### `jmapro2024` — hold_metadata_only

**Use:** Hold; gap-impact question in research-line.md.

**Supported point:** Close IN625 candidate: processing parameters and melt-pool characteristics.

**Read scope:** Crossref/OpenAlex identity only; parent public/session access queue.

**Limit or counterevidence:** Metadata only; not evidence of our exact continuation design or absence of overlap.

Persistent source: https://doi.org/10.1016/j.jmapro.2024.05.025

### `heatsourcebayes2024` — usable_with_scope

**Use:** Introduction successful source-calibration/transfer route; Discussion source alternative and comparison design.

**Supported point:** Four source models were compared through fusion-zone errors and Bayesian optimization; a calibrated conical-source regression transfers across a studied process window.

**Read scope:** Version-of-record17pp PDF pp1–2 Intro/abstract,p4 calibration/Methods,pp15–16 Conclusions. Reported source ranking restricted to its experiment.

**Limit or counterevidence:** IN738LC; calibration still occurs during model construction. Cross-sectional agreement and reported LOOCV do not prove thermal histories or all-material validity. Conical source cannot be ranked against current Gaussian across unlike cases.

Local source: [pdfs/heatsourcebayes2024.pdf](pdfs/heatsourcebayes2024.pdf); [page-marked text](text/heatsourcebayes2024.txt).

Persistent source: https://doi.org/10.1007/s40192-023-00334-2

### `dynamic2024` — usable_with_scope

**Use:** Introduction successful calibrated-source route; Discussion source/closure alternatives and a future discriminating comparison.

**Supported point:** A dynamic two-parameter volumetric source adjusts depth/absorption and improves IN625 geometry across a calibrated spot-size range; local dynamic conditions motivate source transfer.

**Read scope:** Author manuscript45pp PDF pp1–6 Intro/model;pp17–20 calibration/problem/materials;pp39–40 Discussion/Conclusions. Final journal identity separately verified.

**Limit or counterevidence:** Bare-plate EOSmulti-spot195W/800mm/s then AMB2018-01 layer case, not our threeAMB2018-02 targets. Table2 uses different phase-dependent k/cp and eutectic1410K, not our solidus. Effective source success cannot validate internal temperatures.

Local source: [pdfs/dynamic2024.pdf](pdfs/dynamic2024.pdf); [page-marked text](text/dynamic2024.txt).

Persistent source: https://doi.org/10.1016/j.addma.2024.104531

### `gasliquid2025` — usable_with_scope

**Use:** Discussion boundary on extension to powder; optional citation only.

**Supported point:** Recent multiphase modelling connects spatter/entrainment and tail-flow perturbations with possible defects.

**Read scope:** Complete Crossref/OpenAlex scholarly abstract; public repository PDF403.

**Limit or counterevidence:** Full abstract only; powder mechanisms are not present in this bare-plate study and are not a cause assigned to its thermal tail.

Persistent source: https://doi.org/10.1016/j.actamat.2025.120816

### `feedforward2025` — hold_metadata_only

**Use:** Hold; no active prose.

**Supported point:** Candidate vector-level thermal model control.

**Read scope:** Crossref/OpenAlex identity only.

**Limit or counterevidence:** Metadata only; no algorithm/validation claims. Optional to present paper, not a dependency.

Persistent source: https://doi.org/10.1016/j.addma.2025.104981

### `weeks2026` — usable_with_scope

**Use:** Introduction observation-aware assessment; Discussion camera-to-field mapping.

**Supported point:** An observation model for internal thermal-emission reflections can reconcile some simulated/camera discrepancy.

**Read scope:** Complete scholarly OpenAlex abstract from prior search; version-of-record fulltext/format not read by this worker.

**Limit or counterevidence:** Full abstract only here;316L concave keyhole, not a universal correction or matched AMMT sensor. Changes observation mapping, not necessarily thermal physics.

Persistent source: https://doi.org/10.1016/j.addma.2026.105245

### `review2024` — usable_with_scope

**Use:** Introduction computational tradeoff or Discussion material-data requirements, with primary sources for detailed claims.

**Supported point:** Recent review describes FEM model hierarchies, material-temperature dependence and thermal/structural coupling.

**Read scope:** Journal-pre-proof84pp PDF p2 abstract,pp16–18 material properties/thermal equations; remaining66pages not claimed read.

**Limit or counterevidence:** Broad FEM/part-scale review and journal pre-proof; equation forms are illustrative and not imported without independent derivation.

Local source: [pdfs/review2024.pdf](pdfs/review2024.pdf); [page-marked text](text/review2024.txt).

Persistent source: https://doi.org/10.1016/j.addma.2024.104157
