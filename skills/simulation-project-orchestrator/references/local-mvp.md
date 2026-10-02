# Local Simulation Agent MVP

Read this reference only when `simulation-agent-mvp` is present or the user asks to exercise the local prototype.

**Compatibility boundary:** this reference describes a separately installed executable prototype, not code shipped in this skill. Its all-PASS governance promotion rule and EXECUTED cap below remain unchanged by the research-stage/efficiency instructions. Do not claim these prompt changes relax its implementation or relabel its WARN/FAIL/BLOCKED bundle as accepted. Use its real returned states; any separately assessed research claim must name its own evidence contract and preserve the prototype's original limitation.

## Scope

The prototype provides native and external-backend execution, together with separately registered application cases:

1. a native one-dimensional steady heat-conduction MMS problem with a smooth exact field, SymPy-derived source, uniform-grid centered second differences, and an O(n) Thomas tridiagonal solver; and
2. a process-isolated openPASO MCP adapter that probes the real tool catalog and executes reviewed solver cases in a separate Python runtime; and
3. registered application cases with their own physical models, source/experimental contracts, calibration data, comparisons, sensitivity analyses and interpretation outputs. Discover the available cases from the prototype's current case index and read only the selected case's contract.

The MMS and Poisson cases verify code/numerics and demonstrate the control layer. A literature-conditioned reconstruction or application has its own physical and comparison assumptions; its actual numerical and physical status comes from the current case index and bound run artifacts. It does not inherit acceptance from the MMS or from a completed subprocess.

Never generalize an MMS result to real material parameters, geometry, boundary conditions or model form. Imported data may be screened, but the MMS backend keeps physical validation blocked because it lacks a real-system model and combined uncertainty model. Calibration, experiment comparison and mechanism conclusions retain their separate data roles and limits in each selected application. Reject safety-relevant use at input validation.

## Commands

From the project directory on Windows:

```powershell
.\bootstrap.ps1
.\.venv\Scripts\python.exe -m simagent doctor
.\.venv\Scripts\python.exe -m simagent diagnose .\examples\heat_mms.json --data-root .\.simagent-data
.\run.ps1
```

The bootstrap must select a healthy Python 3.11-3.13, verify core modules, and fail immediately when a native command fails. Python 3.14 is excluded from this prototype. `openpaso` and `gmsh` are optional for the native heat backend. Their absence must block only requests that actually select those capabilities. For an openPASO request, probe the configured runtime instead of importing openPASO into the control-plane interpreter:

```powershell
.\.venv\Scripts\python.exe -m simagent backend-probe --runtime-root <openpaso-runtime>
.\.venv\Scripts\python.exe -m simagent backend-tools --runtime-root <openpaso-runtime>
```

Do not equate MCP tool registration with solver installation. Record the control-package version, MCP server-reported version, actual tool names and doctor/discover result separately. Earlier audits with only scikit-fem do not determine current availability: the latest local discovery also found FEniCSx, NGSolve and Kratos. Probe the requested capability and runtime; do not claim every openPASO adapter is installed.

Run the syntax/lint/tests and actual calls affected by a change. Broaden only for a new failure or a material concern. These are available commands, not a requirement to rerun every check after each report edit:

```powershell
.\.venv\Scripts\python.exe -m compileall src tests
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m pytest
```

## Authority Registry

The machine-readable registry is `src/simagent/data/authority_sources.json`. Validate `acquired=true` paths before a run. Do not use `C_PREPRINT` as the sole support for a high-consequence acceptance claim. `D_PROJECT_DERIVATION` supports implementation and observed-run claims only, never independent physical validity.

For MMS, prefer the acquired Salari and Knupp Sandia report and cite verified local locators. The current local copy is `simulation-agent-literature/pdfs/37_salari-knupp-mms.pdf`; its core construction is in PDF p. 22 (Section 3) and its summarized verification procedure begins on PDF p. 32 (Section 5). The report explicitly distinguishes code verification from solving the right physical equations.

## Expected scientific result

For the default example, require monotone error reduction and approximately second-order observed convergence. Do not hard-code a success result: read `run-summary.json` and raw field CSVs from the new or cached run. With no real validation data, the raw scientific candidate may reach `NUMERICALLY_VERIFIED`, but without a content-bound, runtime-attested collaboration bundle the final governed level is capped at `EXECUTED`; `PHYSICAL_VALIDATION` remains `BLOCKED` and `COU_ACCEPTANCE` remains blocked. A bundle with any governance WARN, FAIL, or BLOCKED also cannot promote. Governance is two-stage: first produce `review-subject.json`; then review its exact digest and post-run gates. Binding only the pre-run solve candidate cannot support review of numerical outcomes.

Use a stricter-than-observed threshold as a negative test to confirm that the convergence gate can fail. Repeat the identical run and confirm reuse of the same `run_id`, snapshot revision, and content-addressed blobs.

For the two-dimensional Poisson MMS, require the independently recomputed P1 finite-element rates (approximately second order in L2 and first order in the H1 seminorm), a small algebraic free-DOF residual, and retained VTU fields. openPASO's Cartesian PDE-consistency tool may require fields resampled to its supported regular-cell midpoint representation; preserve every initial refusal and the transformation used to make the check applicable.

For the axisymmetric fin case, require mesh convergence, free residual and global heat balance from the axisymmetric weak form. Do not force the Cartesian constant-coefficient PDE checker onto the weighted axisymmetric Robin problem. Its correct status is `NOT_APPLICABLE` with a reason. A single published tip temperature with unknown convection-coefficient provenance, measurement operator, uncertainty and replication keeps `PHYSICAL_VALIDATION=BLOCKED`, even when numerical convergence is excellent.

## Validation-data minimum contract

A validation CSV requires `x_m`, `temperature_k`, and positive finite `standard_uncertainty_k` on every row, plus source citation, source kind, operating condition, `validation_dataset_role=validation`, and an independence declaration. Calibration data cannot be reused as validation evidence. Passing a residual-over-observation-uncertainty screen does not by itself establish physical validation.

## Final package audit

The run package must include specification, pre-run candidate manifest, post-run review subject, formula audit, raw fields, scientific and governance gates, environment, claim-evidence map, artifact manifest, run summary, LaTeX, and PDF when requested. If a bundle was supplied, preserve its exact frozen JSON bytes as `collaboration-bundle.json`. The final gate list and report references must agree. Treat LaTeX compilation warnings about overflow or annotations outside the page as `OUTPUT_QUALITY=FAIL`; render the final PDF to images and visually inspect it before presenting it as a finished artifact.
