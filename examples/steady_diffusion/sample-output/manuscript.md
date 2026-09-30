# A bounded flux comparison in a one-dimensional diffusion model

*Synthetic verification and workflow demonstration. This note contains no real-material experiment, novelty claim or journal submission.*

## Question and methods

We ask whether a coefficient declining along the transport direction reduces steady flux relative to a uniform coefficient under identical boundary values. The normalized concentration obeys d/dx(D dc/dx)=0 on 0 <= x <= 1 m, with c(0)=1 and c(1 m)=0. We set D=D0 exp(alpha x/L), D0=10^-9 m²/s, and compare alpha=0 with alpha=-1. Flux has unit m/s because concentration is dimensionless.

A conservative two-point flux discretization uses midpoint coefficients and a Thomas tridiagonal solve. Runs with 8, 16 and 32 intervals are compared with the exact series-resistance result q = D0/L for alpha=0 and q=D0 alpha/[L(1-exp(-alpha))] otherwise. The verification criterion is claim-relative: analytical error must be smaller than one twentieth of the observed effect; bounded concentration and near-roundoff flux balance are also checked for this steady linear case. Actual field CSVs, model specification and run JSON are included.

## Results

At 32 intervals, the uniform and declining cases yield fluxes of 1.00000000e-09 and 5.82000388e-10 m/s. The modeled reduction is 41.800%. The finest-grid relative analytical flux error for alpha=-1 is 0.004069%; the largest across the planned grids is 0.065117%. Concentrations stay within [0,1]. The maximum relative flux spread is 2.931e-14. Figure `profile.svg` is generated from the actual 32-interval fields.

## Interpretation and limits

The exact total resistance is the integral of 1/D(x). A declining coefficient increases this resistance, supporting the lower modeled flux. The ranking and error-to-effect separation answer the contracted comparison, so additional mesh refinement has no identified value for that question. This is an explanation within the stated equation and boundary conditions. It does not establish a physical mechanism in a tested material, calibrated parameter values, applicability to higher dimensions, or experimental validation. Selecting a real journal and establishing material relevance require separate evidence.

## Reproducibility and evidence

Run `python examples/steady_diffusion/run.py --project <new-output-directory>` from the ResearchFlow repository. The claim `flux-ranking` links to `runs/summary.json` and the frozen `model.json` through research state. This note is generated deterministically from executed outputs; a real writer/reviewer agent must interpret the evidence for a real paper. The example runner itself does not call an LLM, live PaperSpine or submit a manuscript.
