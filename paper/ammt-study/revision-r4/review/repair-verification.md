# R4 bounded repair verification

**Recommendation:** accept the bounded content repairs and promote the revised manuscript for author review. R4-F01–F04 are resolved by the inspected revision. The main diagnostic result remains evidence-supported within the manuscript's stated conduction-model and numerical limits. R4-F05 remains a separate pre-submission human-oversight attestation item. This recommendation does not certify journal acceptance, journal-specific submission compliance or completed human scientific review.

## Inputs and method

Checked the current canonical `paper/ammt-study/manuscript.tex`, its actual `manuscript.pdf`, `reproduction-notes.md`, and the source/PDF differences from the unchanged frozen R4 inputs. The current PDF has **19 pages**. Rendered and inspected all pages in `visual/repaired-manuscript-01.png` through `repaired-manuscript-19.png`, with individual enlarged checks of pp. 2 and 16 for the new paragraph and numerical-method prose. The original 18-page reviewed PDF and frozen reviewed TeX were not modified.

Read `revision-r4/argument/recent-assessment.tex` and `recent-source-trace.json`, then checked the actual integrated wording directly against the retained primary articles. The trace guides the locators; its assertions do not substitute for the originals. The separately assigned review remains same-model and nonblind, with the exposure disclosed in `independent-review.md`. Coordinator acceptance is not used as evidence that a repair is complete.

No PDE solve, new experiment, new literature retrieval or canonical edit was performed by this reviewer. All writes remain within the assigned review directory.

## Finding dispositions

| Finding | Actual revision and evidence | Disposition |
|---|---|---|
| R4-F01: abstract baseline | Canonical line 30, PDF p. 1, now says “Linear continuation and holding at the last tabulated value are compared independently for conductivity and sensible heat capacity,” with calibrated source and phase law retained. The qualitative held-property directions now have a defined comparator. Detailed final slopes and endpoints remain appropriately in Methods/Appendix. | **Resolved.** The minimal self-contained baseline is supplied; no extra abstract numbers are required. |
| R4-F02: coordinate transport scheme | Canonical line 385, PDF p. 16, names exponentially fitted finite-volume convection, current-iterate material coefficients and diffusion–transport stencil updates, Anderson acceleration and preconditioned GMRES. The accompanying reproduction notes disclose FiPy and solver controls. Executed source and all six selected production manifests support these operations; see exact locators below. | **Resolved as a method-disclosure defect.** No new accuracy claim or numerical run is introduced. |
| R4-F03: cited experimental allocation | Canonical line 306, PDF p. 13, now assigns geometric/solidification calculations to AlSi10Mg laser and IN718 electron-beam cases and experimental grain-morphology comparison to the IN718 case. This matches the original Plotkowski article. Hatch progression remains limited to overlapping multi-line melts. | **Resolved.** |
| R4-F04: conclusion scope | Canonical line 322, PDF pp. 14–15, states that each condition's history follows its calculated quasi-steady field and that aligned future evidence would “test” physical correspondence. The one-third passage-time reduction and derived rate relation remain correctly bounded. | **Resolved.** |
| R4-F05: AI oversight | Canonical line 328, PDF p. 15, still states tool and purposes without documenting extent of human oversight. No evidence of completed human-author oversight has been provided to this reviewer. | **Pending human attestation before submission.** Preserve the item; it is separate from the bounded scientific/content repair acceptance. |

The removal of “rather than a transient thermal initial condition” leaves the steady problem and warm nonlinear initial guesses correctly described. It changes no method or evidence claim and needs no further repair.

## Numerical recipe verification

The inspected original production snapshot is:

`C:\Users\Administrator\Documents\ChatGPT\电脑答疑\simulation-agent-mvp\research\reproduction-case\nist-amb2018-02\verification\fipy-application-A-frozen-r13\frozen-solver-source.py`

- Lines 373–377 rebuild the diffusion/exponential convection terms after `D` changes; line 811 records `FiPy ExponentialConvectionTerm` as the scheme.
- Line 379 uses the GMRES solve with the `ClassicalAMG` preconditioner. The class and restart implementation appear earlier in the same source, and the Anderson path is at lines 678–703.
- The six **original manifests**, not just the default parser option or reproduction-note interpretation, were inspected: `fipy-application-A-frozen-r13`, `fipy-application-B-cal-05-r13`, `fipy-application-C-frozen-r13`, `fipy-application-B-highT-frozen-r14`, `fipy-application-B-khold-cplinear-r15`, and `fipy-application-B-klinear-cphold-r15`. Each `manifest.json` records `solver_controls.nonlinear_method = anderson`, linear `GMRES`, the multigrid preconditioner and new terms on each assembly. Newton–Krylov options also present in the source are not mistaken for the selected production path.

The B production source is at the sibling path `verification\fipy-application-B-cal-05-r13\frozen-solver-source.py`; its equation locator is also lines 373–377. These are original-case locators, with package-relative methods and controls supplied in `reproduction-notes.md`. The repair describes the executed scheme; it does not turn the constant-property analytical verification into a full nonlinear branch error certificate.

## New recent-literature paragraph

The integrated paragraph is canonical line 48, rendered p. 2, placed between the existing observation/calibration discussion and material-data coverage. It has a controlling argument—parameter response, observed agreement and model-specific attainability answer different assessment questions—and its last sentence hands that argument to the constitutive assumptions in the following paragraph. It is a synthesis paragraph, with sources earning distinct roles rather than a sequence of unrelated summaries.

| Source and original inspected | Supported use in the paragraph | Boundary checked |
|---|---|---|
| Yang et al., *Materials* 17 (2024) 2565, DOI `10.3390/ma17112565`; retained `revision-r2/literature/pdfs/sigler2024.pdf`, pp. 1, 3, 9 and 12–14 | Analytical model-internal changes in pool dimensions and temperature histories with laser parameters and constant thermophysical inputs. | Ti6Al4V, isotropic constant-property analytical conduction; no import of extreme peaks, sensitivity ranking, physical material causality or a nonlinear-continuation precedent. |
| Soares et al., *Applied Sciences* 16 (2026) 5850, DOI `10.3390/app16125850`; retained `reliability2026.pdf`, especially pp. 4–5, 17–18 and 21 | Combined thermography/metallography of the stated 316L, IN625 and CoCr tracks gives useful surface trends, while strong depth correlations coexist with systematic deviations outside stable conduction melting. | Its powder-track, constant-property model has no explicit phase change; camera calibration uses metallographic information. The paragraph neither claims wholly independent temperature truth nor imports its bias magnitude or keyhole diagnosis to the current bare-plate case. Original p. 21 explicitly gives strong depth linearity and a slope near 0.3 in the keyhole regime, supporting the correlation/agreement distinction. |
| Hong et al., *Materials* 19 (2026) 3290, DOI `10.3390/ma19153290`; retained `fittingfree2026.pdf`, pp. 1, 4, 6–7 and 12–13 | Invert the specified conduction map for required absorptivity, compare with the physical ceiling, and test alternative effective-transport assumptions. | Inverse attainability is diagnostic under its specified assumptions. Directional effective-diffusivity controls appear in the original. The paragraph does not claim all conduction closures are impossible, diagnose the current residual as keyholing or apply a physical-absorptivity ceiling to the present fitted effective source factor. |

The addition does not claim a globally absent prior sensitivity literature, global superiority or first-in-field novelty. “Together” supports a useful classification of these three studies, not a comprehensive history. Their bibliography entries in the actual rendered PDF contain the matching titles, journals, years and DOIs. **No consequential new source or reader defect was found in this paragraph.**

## Render and retained boundaries

The actual repaired PDF displays the accepted changes and all five figures. No clipping, overlap or unresolved citation/reference was observed. The build log contains no undefined reference/citation or error; one underfull box at lines 82–87 did not produce a visible defect and is not a content blocker. The page count increases from 18 to 19 with the added paragraph and references. Figure proximity remains the optional navigation preference recorded in the original review; readable late floats do not invalidate evidence.

The unchanged evidence limitations remain active: fixed-source deterministic contrasts, distinct observation populations, derived time/rate quantities, descriptive fine interactions, missing branch-specific three-dimensional refinement, no solved loss feedback, extreme held-property peaks, and absent melt flow/evaporation. The repair does not clear those boundaries by confidence or consensus. Authorship and human oversight remain pending author matters; the current reading PDF is not certified against an unverified journal Guide for Authors.

**Bounded review contract complete:** frozen findings are preserved in `independent-review.md` and `findings.json`; accepted repairs are verified here, with the remaining official disclosure item explicitly retained.
