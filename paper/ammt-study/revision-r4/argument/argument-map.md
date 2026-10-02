# R4 Introduction argument

This candidate reconstructs the research line from the original evidence before introducing the local comparison. It is a simulation interpretation paper for *Additive Manufacturing*. Its central contribution is to distinguish the effects of constitutive choices on a length-calibrated thermal field through phase-boundary position, spatial span and material passage time. It does not claim a new model family or improved physical prediction.

## Paragraph logic

| Paragraph | Question answered and established knowledge | Evidence and role | Connection to the next paragraph |
|---|---|---|---|
| P1 | Why is a geometric fit scientifically useful but incomplete for solidification analysis? A fused boundary and a material cooling history contain different information. | Hooper 2018: resolved spatial profiles, stationary-point histories and cooling during solidification. The incompleteness of geometry as a thermal constraint is developed, rather than asserted as universal nonuniqueness. | The practical need for thermal information motivates computationally manageable moving-source descriptions. |
| P2 | What does the research line of moving-source conduction make possible? Distributed sources, nonlinear properties and latent storage extend classical heat-flow descriptions; rapid transient formulations address scan effects. | Van Elsen 2007 method development; Plotkowski 2017 rapid transient method and grain-trend assessment; Coleman 2024 original statement of unresolved fluid/surface effects. | The useful simplification makes source and effective transport part of how a boundary is reproduced. |
| P3 | What does geometric calibration establish about source/transport choices? Constrained incident beam geometry does not fix internal energy redistribution. Source and directional closure are substantive model components. | Kollmannsberger 2019 measured-beam AMMT comparison and calibrated directional closure; Coleman 2024 bare-track source calibration and subsequent layer case. | Their value and model dependence make temperature evidence a distinct assessment. |
| P4 | What directly demonstrates the limits of a geometric fit, and what does the observation actually constrain? Similar geometric agreement can coexist with different temperature profiles. Imaging length and metallographic cross-section dimensions observe different features/populations. | Myers 2023 original calibration/thermal comparison; Kollmannsberger 2019 internal-temperature validity limit; Lane 2020 measurement definitions. | Calibration cannot supply an independent constitutive description; material data coverage must be considered. |
| P5 | Why does high-temperature continuation have a scientific role before this study is designed? IN625 property tables terminate below melting. Conductivity and sensible storage have different roles in the energy balance. | Special Metals 2013 actual table endpoints/provenance; Mills 2006 liquid-estimation alternatives and measurement limitations. | A continuation of sensible properties must be kept distinct from the assumed phase-change law. |
| P6 | How do sensible storage, latent storage and the freezing interval differ? A phase-fraction closure distributes latent storage; the interval may differ between supplier range and a rapid-solidification approximation. | Van Elsen 2007 enthalpy accounting; Coleman 2024 linear fraction and Scheil-motivated eutectic endpoint; Special Metals supplier range. | Fixing that law permits a useful comparison of spatial phase-boundary structure. |
| P7 | What does a length change mean inside the temperature field? Paired rear boundaries can translate with little separation change, or their span can change. Overall length alone does not distinguish these responses. | Local definitions and coupled energy-balance reasoning, explicitly identified as synthesis/local derivation in the trace. No citation is attached to manufacture a literature discovery. | Even the spatial span needs motion information before it becomes a time interval. |
| P8 | How does spatial structure relate to material time? A steady translating field admits a length/speed mapping; pulsing and fluid motion alter physical histories. | Lane 2020 constant-speed mapping; Hooper 2018 pulsed stationary histories; Hou 2024 fluid-tracer thermal excursions, with their actual material/conditions retained in the trace. | The distinction justifies measuring individual constitutive responses and paired boundaries in a bounded steady conduction comparison. |
| P9 | What question can the present evidence answer? A source fitted to one length is retained while separate property continuations, shape discrepancies and derived time intervals are assessed. | Frozen R4 methods and refreshed retained numerical evidence. Local experiment enters here, after the scientific problem has been established. | Ends with the intellectual use of the comparison: interpreting constitutive sensitivity and choosing thermal observables. |

## Synthesis decisions

- The candidate contains nine connected paragraphs, approximately 1150 words. Paragraphs P7 and P8 are separate because boundary translation/span and spatial/time conversion answer different reader questions.
- Ten primary-source citation keys are used, all already present in the bibliography. No manuscript paragraph is structured around an author list. The historical line follows changes in what moving-source calculations represent and assess, not a chronology of names.
- The former separate lists of calibration papers and recent reliability/sensitivity papers are replaced by two representative comparisons that establish the source/transport relationship and one direct geometry/temperature test. This is a bounded selection for the argument, not a claim that the omitted lines lack value.
- The supplier data problem is established before L/H is named. The paper does not claim that last-value holding is more physical, that linear continuation is invalid, or that the continuation contrast exhausts plausible liquid-property uncertainty.
- The phase-law paragraph makes a positive scientific distinction. It neither calls the adopted linear fraction an equilibrium measurement nor presents the Scheil endpoint as the correct endpoint for the present coupon.
- The experiment is framed as a controlled interpretation of a calibrated field. The Methods can describe public-target availability and the scalar objective once; the Introduction does not repeat retrospective/nonblind terminology or imply a prospective holdout.

## Abstract choices

`abstract.tex` starts from the thermal question and qualifies the central comparison as an enthalpy conduction model. It reports the opposed continuation responses, rear translation versus span, and spatial/time distinction qualitatively. The sole quantitative anchor is the approximately one-third shorter passage time at the higher of the two scan speeds. It does not imply that a thermal history was independently validated or that predictive accuracy improved.

## Consequential evidence gaps

1. **Thermal validation of the derived phase-interval history.** A same-condition surface temperature profile with a defensible phase/emittance interpretation would test the rear crossings directly. The published AMMT below-solidus cooling examples use another interval and are not recommended by their authors as reference/calibration data; they cannot validate the present 1350--1290 °C passage interval.
2. **Coupon-relevant high-temperature constitutive functions.** Measurements or independently justified liquid/near-melting conductivity, sensible enthalpy and phase fractions would constrain which continuation is physically appropriate. L/H is a controlled model contrast, not an uncertainty distribution or competing fitted property identification.
3. **Liquid parcel histories.** A matched thermo-fluid solution or appropriate observations would be needed before interpreting the stationary-material mapping as a liquid trajectory. Hou's different-alloy tracer result establishes the distinction, not the current residence time.

Another literature search could find more precise IN625 high-temperature measurements or same-condition thermometry that changes these constraints. It would not, by itself, convert the retained L/H solutions into independently validated histories. No expansion is needed to answer the current argument contract.

## Light audit

- All 10 citation keys resolve in `literature/bibliography-r2.bib`.
- No first-discovery, superiority or performance-improvement claim appears.
- Full-text evidence is used for all cited technical claims; inference and local derivation are marked in `synthesis-trace.json`.
- No PDE rerun or canonical manuscript edit was performed for this candidate.

## Incorporated writing guidance

The coordinator's independently curated package at `../guidance/` was read before final delivery, including `section-guides.md` and `synthesis.md`, followed by the original local MIT CEE title/main-message passage and the MIT/Broad Introduction and Abstract passages. The teaching sources are separate from the study bibliography and scientific evidence.

- [MIT/Broad Introduction](https://mitcommlab.mit.edu/broad/commkit/journal-article-introduction/), Specific Background/Knowledge Gap: the current question should follow logically from the supplied knowledge; background is selected to make the result comprehensible, not to exhibit literature breadth. The candidate therefore proceeds through the actual source/transport and measurement evidence before property continuation is introduced.
- [MIT CEE Journal Article](https://mitcommlab.mit.edu/cee/commkit/journal-article/), The title is attractive: "A great option for your title is a shortened version of your one-to-two sentence main message." This supports comparison with the central claim; the grammar/semantic parsing and the preference for a relational title are editorial judgments, not a university mandate.
- [MIT/Broad Abstract](https://mitcommlab.mit.edu/broad/commkit/journal-article-abstract/), writing from the completed results and Implications: results are consolidated by their role in the answer; the ending states the interpretation gained. No numerical quota or fixed sentence count is imposed.
- The curator's section guide applies the UNC paragraph/transition principles and Manchester's nonrigid introduction moves. Nine paragraphs are retained because each has a separate controlling idea; no gap is manufactured at every ending and no connection is supplied by a decorative transition alone.

Final coordinator exchange was incorporated: P1 states the tension declaratively; P4 confines the internal-temperature limitation to the cited authors' model; P9 describes the common fitted source without implying blind validation. `title-logic.md` recommends the coordinator's relational candidate while preserving the existing title as grammatical and optional.
