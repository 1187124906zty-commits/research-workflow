# Current original-source refresh audit

The current original reports preserve the physical and numerical facts supporting C_GEOMETRY, C_TIME and C_CLOSURE. The changed dashboard and README add presentation and reporting material, including a quasi-steady material-passage animation and its CSV history. That addition is real derived evidence and was checked; it does not add a new PDE solution or independent thermal validation. One newly exposed peak-temperature operator difference is retained below, rather than ignored as bookkeeping.

This audit writes only `revision-r3/evidence-refresh/`. `verified-current.json` contains exact comparisons and values; `inspect_current.py` is the read-only inspection recipe. No solver was imported, no PDE was run, no originals or historical hashes were changed, and no scientific PASS is self-issued. Coordinator interpretation and refreshed binding remain separate.

## Compared originals and historical referents

Source root:

`C:/Users/Administrator/Documents/ChatGPT/电脑答疑/simulation-agent-mvp/research/reproduction-case/nist-amb2018-02`

Current originals read: `report/current-results.json`, `README.md`, `report/experimental-comparison.csv`, `report/constitutive-factorial-effects.csv`, `report/constitutive-factorial-results.json`, each of the six production `result.json` objects and their manifests. The new `report/showcase-animation.json`, `report/showcase-material-history.csv`, `report/showcase-speed-source.csv` and relevant lines of `solver/render_case_showcase.py` were also read. The B retained `fields.npz` surface arrays were inspected without importing the solver.

Historical content compared: `evidence/verified-data.json` and `revision-r2/methods-results/computed-audit.json`. The former is richer than the dashboard: its comparison rows add source, signed-difference and source-U-scale flags. Those extra inspection fields are not expected to appear in the dashboard. All common scalar comparison fields were tested, rather than declaring whole JSON files identical.

Local Git cannot establish the chronology: this source case is untracked, and local `master` has no commits. `git diff` is therefore not evidence that the old dashboard was unchanged. The refresh establishes current-content agreement with frozen verified records, not an exact historical prose diff.

## Consequential values and comparisons

All nine current comparison rows have exactly the same floating-point values as the verified dossier and its primary CSV. A/B/C model L/W/D in µm remain:

| Condition | L | W | D | Reference L/W/D |
|---|---:|---:|---:|---|
| A | 309.8856792638423 | 153.36005335598344 | 40.46931231766381 | 300 / 147.9 / 42.5 |
| B | 359.1575457177625 | 143.0406226383922 | 31.12034988767346 | 359 / 123.5 / 36.0 |
| C | 320.6313629678825 | 129.04618690578758 | 22.044541383670747 | 370 / 106.0 / 29.6 |

The effective factor remains **0.2890548519203547**, fixed after B-length calibration. The C depth reference remains **29.6 µm**; it has not reverted to the old 29.5 literature transcription. B/C width is high and depth low. Their data remain condition-class comparisons with separate imaging and microscopy populations, and A/C remain retrospective nonblind comparisons.

All current `research_case_metrics` values exactly equal the dossier. Rear phase span / passage time / derived mean cooling magnitude remain:

| Condition | Span µm | Time µs | Mean cooling MK/s |
|---|---:|---:|---:|
| A | 48.29519038375836 | 120.7379759593959 | 0.4969438946051072 |
| B | 80.26402604458121 | 100.3300325557265 | 0.5980263184572783 |
| C | 80.79140265237265 | 67.32616887697722 | 0.8911839333920206 |

All four current factorial metric sets, finite effects and matched-temperature properties equal the historical verified dossier. Geometry/phase-span/time/peak values also equal the independent R2 computed audit. The length effects remain +43.213712463555225 µm for k at linear cp, −6.168857760595699 µm for cp at linear k, −2.761942119711591 µm interaction and +34.282912583247935 µm joint. The joint depth change remains −0.3232846168545471 µm, composed of opposing responses. Nothing in the added reports repairs the B shape discrepancy or establishes a physically identified continuation.

The selected rear outward diffusive power remains **14.723959252476138 W** in LL and **14.91330340892631 W** in HL. Its increase is +0.1893441564501721 W. The selected hot region and gradients vary with the solved state, so this contradicts only the naive claim that lower k necessarily lowers this integrated outward power. It cannot rule out all bulk-transport explanations.

For all six production results, current L/W/D, surface peak, minimum temperature, iteration/duration and equation/balance/correction fields match the dossier. A/B/C dashboard maxima remain equation L1 **1.2841515517804504e−7**, correction **2.6300048602934112e−5 °C**, and absolute relative power balance **6.034533007221461e−11**. These dashboard maxima describe the operating conditions; they should not be relabeled maxima over all factorial branches without consulting the six-run records. This refresh adds no branch-specific 3D convergence bound.

## Added postprocessing and genuine operator discrepancy

The new animation identifies `verification/fipy-application-B-cal-05-r13/fields.npz`, mode `POSTPROCESSING_QUASI_STEADY_MATERIAL_PASSAGE`, speed 0.8 m/s and mapping `xi=X-v*t`. It explicitly reports no new PDE and no physical-validation promotion. Its 73 display frames span −0.24 to +0.64 ms; the companion fixed-material history has 1001 samples. README now exposes this movie, a speed comparison and a four-corner closure view, and explains the preserved-field and public-asset distribution.

Independent read-only arithmetic found:

- Maximum coordinate mapping difference is 0 m.
- Maximum CSV temperature difference from interpolation of the retained `surface_y0_T_C` array is **4.547473508864641e−13 °C**.
- Phase fraction exactly equals `clip((T−1290)/60,0,1)` in the sampled history.
- The sampled rear liquidus and solidus crossing times are **0.2831218882133679 ms** and **0.3834519207690941 ms**. Their interval is **100.3300325557262 µs**, differing from the primary B interval by only −2.984279490192421e−13 µs.

The CSV material-point peak is **2697.937948411942 °C**, and the retained symmetry-centerline maximum is **2697.939199600421 °C**. The existing `surface_peak_C` is **2697.0732343382333 °C**, exactly the maximum of saved `surface_T_C` on positive-y nodes. Renderer lines125–132 constructs the surface with `surface_y0_T_C` as a new y=0 column followed by `surface_T_C`; line147 interpolates the material-point history. The centerline maximum exceeds the previously reported positive-y maximum by **0.8659652621877285 °C**. The history's dense sampling lowers its maximum by approximately0.00125 °C from the retained centerline node peak.

This is a definitional difference in peak operators on the same retained solution, not a changed thermal solve. It does not alter C_GEOMETRY, C_TIME or C_CLOSURE, nor the manuscript's approximate2697°C LL description. If exact maxima are presented in a future revised report, label positive-y sampled surface peak and symmetry-restored centerline peak distinctly or standardize their operator. Do not treat the added history as new transient validation.

## Remaining scope and requester disposition

The additions make the current fixed-material trajectory visible and reproducible. They neither infer fluid residence nor simulate ignition, shutdown, liquid flow, free-surface deformation or evaporation. Three operating conditions plus LL/HL/LH/HH still give **six unique production solutions**, because B is LL.

Current-content numerical agreement supports refreshing the affected report/README bindings after coordinator interpretation. The new presentation evidence and peak-operator difference should remain in that disposition. Matched liquid k/cp and nonequilibrium phase-path evidence, independent thermal validation and branch-specific submicrometre numerical precision remain absent. No claim promotion follows from the new visual artifacts.
