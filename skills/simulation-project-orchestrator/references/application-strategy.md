# Choose the simulation strategy before designing the numerics

## Application simulation and algorithm development

An application task asks for an answer about a physical system. An algorithm
development task asks for a new or improved computational method. Use the user's
stated outcome to choose the mode; do not turn an application into algorithm
research because a low-level numerical check is available.

For an application, first read primary domain papers and established solver
examples. Locate their model assumptions, dominant scales, common difficulties,
mesh/time strategies, constitutive treatment, measurement definitions and
reported validity. Separate what the paper actually specifies from details it
omits. Then select the simplest adequate model and a mature available framework.
Use the framework's existing elements, nonlinear solvers, preconditioners,
meshing and output routines wherever their applicability is demonstrated.

The case-specific strategy records:

- the physical question, required outputs and experimental anchors;
- dominant length/time scales and the smallest structures that the QoIs must
  resolve, including boundary layers, interfaces and moving loads;
- source-located common failure modes and practical remedies;
- supported solver features and actual accessible runtime;
- a planned useful-resolution calculation and a finite mesh/time/domain matrix;
- resource estimate and an execution schedule covering baseline, calibration,
  validation comparison, sensitivity and mechanism analysis.

Resolution follows the physical structures and observation precision. Avoid
uniformly spending cells in the far field while leaving a melt depth, boundary
layer or interface only one or two cells thick. Local/adaptive/graded meshes,
symmetry, suitable reference frames and implicit integration may reduce cost,
but each must preserve the intended physical question and observation operator.
Document their assumptions and check their applicability.

## Use diagnostics to repair, then execute the application

A cheap test may identify a failure or reject a strategy. It cannot become the
main simulation merely because it finishes quickly. After locating a defect,
choose and implement the most likely effective repair, invalidate affected
evidence once, and run the application at justified resolution. Do not finish
with repeated diagnostic suggestions when the next repair is feasible and
authorized. Preserve failed runs and scoped opinions without letting that
history dominate the final physical analysis.

A failed numerical gate blocks only its named claims. It does not prohibit
permitted engineering, higher-resolution solves, a justified replacement
candidate, or a labeled exploratory experimental comparison. Formal calibration
and validation retain their data-role and adequacy requirements. Give the user
the completed process, raw results, comparisons and mechanism interpretation
that evidence supports; a model can have an informative experimental mismatch
after a complete, numerically adequate simulation.

For nonlinear or state-dependent framework terms, ensure that the reported
residual is assembled from the final material state, boundary state and scheme
weights. A framework can cache coefficients or interpolation weights; a small
residual of the cached equation is insufficient. If warm/cold initialization
changes the equation at an identical retained state, repair the wrapper's
refresh/reconstruction behavior and rerun the affected application. Check the
actual installed implementation once and reuse the revision-bound review;
do not invent a new numerical algorithm merely to avoid a framework cache.

Complete a finite, physically scaled calculation matrix. Use serial runs,
graded/local meshes and retained-field warm starts to manage resources. Judge
spacing against the melt depth, interface, boundary layer or other smallest
relevant structure, and the precision of the experimental observable. Geometry
resampling does not improve the field resolution. Include connected-component,
truncation and measurement-definition checks where the observable is a contour.
Maintain one current-results index and one evolving report. Preserve necessary
failure evidence and convergence levels; do not generate report copies or
unrelated historical solver versions for each routine edit.

## Review allocation

The domain role owns the strategy before code generation; the implementation
role estimates cost and identifies framework capabilities or limitations; the
experiment role answers required conditions and observation definitions; the
mechanism role requests fields needed for the physical question. These roles
exchange bounded evidence requests before committing to a long run.

For an established application method, review equation/parameter/BC mapping,
mesh/time choices, nonlinear termination, balances and output interpretation.
Do not demand a new general numerical-method theorem already supplied by the
framework's method documentation. Retain a practical counterexample or baseline
test when the actual mesh, coefficients or solver use could violate its scope.

For algorithm development, add the detailed derivation and method obligations
in [method-review.md](method-review.md). Standards and framework documentation
support their stated scope; they do not replace run-specific convergence or
experimental evidence.
