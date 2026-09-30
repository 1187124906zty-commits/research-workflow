# Result package

Match the package to the stage and requested deliverable. A pilot can return its short plan, inputs/code, run record, relevant raw/derived outputs and bounded decision. A manuscript evidence package needs the claim-critical sources, validation/uncertainty and review records. The full structure below is an available logical layout, not a mandate to create every directory or report for every calculation:

```text
project/
  specification/
    simulation-spec.yaml
    physics-contract.yaml
    decision-ledger.md
  formulation/
    numerical-method-dossier.pdf-or-md
    equations-machine-readable.json
    mechanism-analysis-plan.json
  model/
    geometry/
    mesh/
    solver-input/
  backend/
    capability-probe.json
    tool-catalog.json
    native-receipt.json
  runs/<run-id>/
    run-manifest.json
    stdout.log
    stderr.log
    raw-results/
    derived-results/
  verification/
  literature/
    source-manifest.json
    extracted-text/
    page-renders/
    supplementary/
  validation/
    validation-contract.json
    condition-alignment.json
    extracted-data.csv-or-parquet
    extraction-audit.json
    replication-audit.json
    uncertainty-model.json
    validation-statistics.json
  uncertainty/
  figures/
  analysis/
    required-output-coverage.json
    mechanism-interpretation.json
  collaboration/
    routing-records.json
    assignments.json
    interaction-contracts.json
    opinions.json
    dissent-ledger.json
    scientific-dialogue.jsonl
    scientific-dialogue-audit.json
  provenance/
    ro-crate-metadata.json
    claim-evidence-map.json
    environment-lock.*
  final-report.md-or-pdf
```

## Field formats

Choose for downstream use, not habit:

- VTK XML (`.vtu`, `.pvtu`, `.pvd`) for portable ParaView inspection;
- VTKHDF or XDMF/HDF5 for large or time-dependent fields;
- CGNS for CFD ecosystems;
- Exodus II for compatible structural/mechanics workflows;
- solver-native results when restart, contact/history variables, or audit fidelity require them;
- CSV/Parquet only for compact probes, integrals, histories, and metrics, not as a substitute for full fields.

Store original solver-native output when conversion loses metadata. Include units, coordinate frame, variable meaning, cell/point association, time/load step, and conversion code.

## Run manifest

Record specification/contract revision, artifact IDs, solver and adapter versions, OS/container, executable path, command, hardware relevant to reproducibility, random seeds, mesh statistics, parameter set, start/end time, exit status, output inventory, gate results, and parent/child run lineage.

For an MCP or external-process backend, also record the relevant control/server/runtime versions, executable, selected tool and raw error/refusal state. Use digests for binary provenance, immutable adapter candidates, concurrent-edit protection or reproducible caches as needed. Do not repeatedly hash ordinary text files, or use hashes as a substitute for syntax checks, solver diagnostics, numerical tests or physical validation.

For a mechanism-oriented run, audit the pre-solver output contract twice: first against the generated solver/output configuration, then against the exact completed run. Record every required field's variable meaning, unit, association, coordinate frame, time/load coverage, file path, deterministic transformation, finite/completeness check and missing consequence. A post-processing script cannot reconstruct a state variable or history that was never retained.

## Final report language

The executive conclusion names the highest achieved claim level, validation domain, COU, important uncertainty, failed/skipped gates, and conditions under which the result becomes stale. Include negative results and failed runs when they influenced selection or cost.

For physical interpretation, organize the main result as `question -> competing hypotheses -> numerical/experimental credibility -> discriminating fields and balances -> counterevidence -> bounded conclusion -> next falsifiable test`. Keep raw agreement statistics, mechanism evidence and validation status distinct.
