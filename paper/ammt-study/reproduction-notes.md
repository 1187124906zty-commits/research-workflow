# Numerical reproduction notes

R11 explains the prescribed extrapolations through their actual function and consistently used coefficients, integrals, inverses and recovered observations. Conditions A/B/C, property schemes LL/HL/LH/HH and baseline/refined grids have separate definitions and concise subsequent names. The surface-sample maximum and two transport diagnostics retain their precise sampling identities. Study-level property-selection discussion is developed beside the corresponding temperature findings. The revision preserves the title, display equations, table data, appendix, used figures, numerical tokens and citation-key counts; it adds no simulation, physical validation or general extrapolation law. Source learning and actual changes are recorded in `revision-r11/`.

R10 coordinates the explanatory depth of the Introduction closing and Methods entry, using located section boundaries from three prior research articles. The entry assigns the actual thermographic and metallographic data their respective roles; full model, observation and comparison definitions remain in their Methods subsections. Conclusions retains the findings and scope earned by the accepted evidence. R10 changes no model, numerical run, observation operator, figure, result or evidence status.

R9 revises the research rationale, paragraph and sentence continuity, and factor interpretation following an actual reading of the user-supplied Xiong et al. (2022) article and institutional writing sources. It retains the accepted numerical evidence and R8 direct paired views, adding no PDE or experimental run. The comparison separates calibrated geometry, rear-boundary displacement, interval width and stationary-material time. Local property perturbations provide context for the tested interventions rather than a complete explanation of their full-field responses. The final evidence-sufficiency pass restores existing surface-sample maxima as visible paired numbers and condenses repeated inferences and untested applications; it does not set a paragraph quota. The supplied article provides an editorial and reasoning comparison; its experiments, flow and grain calculations are not current-study data. R8 visual reconstruction details below retain their original execution identity.

These implementation details retain the executed production case and distinguish R6 supplementary work. R3 through the initial R6 editorial revision reused the six production solutions. R6 then added three matched axial-refined HL/LH/HH PDE solutions, while reusing the existing refined LL field and retained B/C refinement. No new experiment or independent physical thermal-history validation was performed. The final-secant linear and constant endpoint extrapolation definitions remain unchanged. Original-field maps retain their baseline mesh; the appendix tables titled "B property combinations on the refined mesh" and "Matched finite property contrasts" report the refined fields and paired contrasts. The enthalpy face coefficient, exponential transport discretization, surface recovery and diagnostic definitions are in Appendix A of manuscript.tex. This file accompanies the flat source archive and canonical manuscript package.

## Executed environment and methods

The production record gives Python 3.13.5, NumPy 2.5.3, SciPy 1.18.1, FiPy 4.0.3 and PyAMG 5.3.0, with one BLAS thread. FiPy assembles diffusion and exponential coordinate-convection terms. SciPy Anderson acceleration solves the nonlinear fixed-point residual. The inner linear system uses GMRES with a PyAMG Ruge–Stuben classical-multigrid preconditioner. The corresponding scholarly software citations are the existing fipy2009 and scipy2020 bibliography entries.

| Control | Executed value |
|---|---|
| Anderson history depth | M = 8 |
| Anderson initial scale | alpha = 0.2 |
| Anderson regularization | w0 = 0.01 |
| Fixed-point residual tolerance | 2 × 10⁻⁴ K in scaled enthalpy U_H (manuscript notation) |
| Line search | Armijo |
| GMRES tolerance | 2 × 10⁻⁹ |
| GMRES restart and iteration cap | restart 80; cap 800 inner iterations |
| Multigrid strength threshold | 0.25 |
| Multigrid smoother | symmetric Gauss–Seidel |
| Multigrid cycle | V cycle |
| Maximum levels and coarse size | 20 levels; coarse size 100 |

These controls come from the production manifests. Alternative methods present in the solver source were not used for the six production solutions. The scientific appendix records the assembled-residual, global-balance and frozen-coefficient-correction acceptance criteria separately from the iterative solver tolerance.

## Coefficient-update behavior

The diffusion and exponential-convection objects are recreated after each coefficient update. Implementation checks found that reusing the objects could retain cached initial stencil weights. The production implementation recreates them to ensure the stencil follows the current coefficients. This is a software correction, not a finding about the physical thermal model.

## Retained numerical records

The original case retains solver snapshots, input manifests, temperature arrays, calibration history and primary-observer code. Source-power integration, threshold crossings, passage geometry and finite-contrast algebra were independently reproduced in the prior numerical audit. The constant-property verification recipes are `verify_constant_gaussian_frame_native61.py` and `qoi_constant_gaussian_reference_native61.py`; report identifier `native61-constant-gaussian-frame-r1`. Keep those recipes and their existing original-case links in the package documentation. They identify numerical records and do not constitute physical validation.

## R6 matched axial supplement

The new run records are `verification/R6-matched-branches/{HL,LH,HH}` in the originating `nist-amb2018-02` case. Their near-source spacings are 2/3/1 micrometres on the same graded domain; all six coordinate arrays match the retained fine LL grid. Power, speed, source fraction, phase thresholds, latent heat, boundary conditions and solver acceptance conditions are retained. HL uses fine LL temperature as its initial guess; LH/HH use the matching coarse temperature/surface fields, interpolated by the original implementation and mapped to their own enthalpy law. No enthalpy field was reused across specific-heat branches, and the source fraction was not refitted.

Three new solves completed in 3944.37 seconds of recorded solver/export time. Actual new residuals, global balance, final corrections, source integration, recovery and raw-field review are retained in `revision-r6/simulation-supplement/`. Complete delivery was accepted after independent raw-output checking and coordinator disposition. The writing coordinator independently checked derived rows and contrasts; a separate writing reviewer spot-checked the sensitive LH/LL pair from four original fields. Compact full-precision rows and finite contrasts are in `data/axial-property-comparison-r6.csv` and `data/axial-property-contrasts-r6.csv`; the source archive embeds the reported tables but does not include large field arrays or the full runtime.

The numerical conclusion is effect-specific: large rear displacements and B/C passage response persist on the tested axial meshes; some small separation magnitudes and continuum directions remain unresolved. Unchanged transverse/depth spacing supplies no full three-dimensional error bound. The original selected-region Peclet and diffusive-power diagnostics remain baseline-field observations. Reproduction of the PDE requires the original case scripts, per-run receipts and source snapshots in addition to this manuscript archive.

## Retained surface-sample diagnostic

On the original 4/3/1 micrometre near-source fields, the recovered positive-y surface-sample maxima for LL, HL, LH and HH are 2697.073, 3506.573, 2756.355 and 3720.947 degrees Celsius. These values are retained in `data/constitutive-factorial-metrics.csv`. They use recovered top-surface samples at axial and positive-y cell centers before the symmetry-plane extension, so their sampling differs from the y=0 centerline used for the phase-crossing comparisons. The fields omit evaporation, liquid momentum and free-surface deformation; a high calculated maximum is a response of that model, not a measured temperature or identification of a physical liquid-state property law.

## R8 direct visual reconstruction

The deterministic generation code and field-recovery checks are in `revision-r8/visual/`. It reads retained fields and constructs the original observation operators; it does not import the solver or solve a new heat balance. Maps and dimensional metrics retain their original mesh identities, and refined endpoint/time comparisons are explicitly distinct. The full flat LaTeX archive contains only figures actually referenced by the current manuscript. The local human-review package additionally contains the plot-generation code and compact visual inputs; replay of field reconstruction still requires the declared original arrays.
