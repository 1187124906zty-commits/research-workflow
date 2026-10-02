# Numerical reproduction notes

These implementation details are retained from the executed case and the prior manuscript. R3 and R4 did not repeat the PDE solves or add physical evidence. The enthalpy face coefficient, exponential transport discretization, surface recovery and diagnostic definitions are in Appendix A of manuscript.tex. This file accompanies the flat source archive and the canonical manuscript package.

## Executed environment and methods

The production record gives Python 3.13.5, NumPy 2.5.3, SciPy 1.18.1, FiPy 4.0.3 and PyAMG 5.3.0, with one BLAS thread. FiPy assembles diffusion and exponential coordinate-convection terms. SciPy Anderson acceleration solves the nonlinear fixed-point residual. The inner linear system uses GMRES with a PyAMG Ruge–Stuben classical-multigrid preconditioner. The corresponding scholarly software citations are the existing fipy2009 and scipy2020 bibliography entries.

| Control | Executed value |
|---|---|
| Anderson history depth | M = 8 |
| Anderson initial scale | alpha = 0.2 |
| Anderson regularization | w0 = 0.01 |
| Fixed-point residual tolerance | 2 × 10⁻⁴ K in scaled enthalpy U |
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
