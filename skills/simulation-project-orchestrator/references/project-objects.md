# Project objects and provenance

For exploration, the three objects below may be sections of one compact run plan with versioned evidence locators. Use full schemas when useful for programmatic checking or required by an adapter. Freeze the plan for one run, then version evolving assumptions and questions; only dependent artifacts become stale. Object completeness is judged against the current question and claim, not every field of every possible project.

## Simulation Specification

Use a stable project ID and monotonically increasing revision. A compact YAML representation is:

```yaml
project:
  id: sim-...
  revision: 1
  status: DRAFT | FROZEN | SUPERSEDED
context_of_use:
  decision:
  consequence_level: exploratory | engineering | safety_relevant
  operating_domain:
quantities_of_interest:
  - name:
    definition:
    location_or_region:
    unit:
    acceptance_rule:
geometry:
materials:
physics:
initial_conditions:
boundary_conditions:
interface_conditions:
validation_referent:
software_preferences:
compute_budget:
deliverables:
assumption_ledger: []
unresolved_decisions: []
```

Each consequential leaf stores `value`, `unit` where applicable, `status`, `source_id`, and `confidence_scope`. Preserve the raw user wording next to the canonical interpretation.

Machine-readable draft: [simulation-spec.schema.json](simulation-spec.schema.json).

## Physics Contract

```yaml
contract:
  id: physics-contract-...
  specification_revision:
  domains: []
  variables: []
  governing_terms: []
  constitutive_relations: []
  initial_conditions: []
  boundary_conditions: []
  interface_conditions: []
  coefficients: []
  time_scheme:
  assumptions: []
  units: []
  closure_requirements: []
  invariants_and_balances: []
  analytical_limits: []
  validity_domain: []
```

Represent a governing term structurally where possible: equation, domain, variable, operator, coefficient, sign, activation condition, and source. Solver adapters should map solver objects or input blocks back to these terms. Compare requested and reconstructed contracts by missing, extra, changed, or unresolved items; a text-similarity score is insufficient.

Machine-readable draft: [physics-contract.schema.json](physics-contract.schema.json).

## Artifact graph

Use typed nodes such as `specification`, `contract`, `derivation`, `geometry`, `mesh`, `solver_input`, `run`, `field`, `metric`, `figure`, `validation_observation`, and `claim`. Use edges such as `derivedFrom`, `implements`, `used`, `generatedBy`, `invalidates`, `comparesAgainst`, and `supports`.

An upstream revision change propagates `STALE` along dependency edges. A stale node cannot support an accepted conclusion.

## Evidence graph

Every important claim needs at least one evidence path. Record:

- source kind: user input, primary literature, official documentation, software metadata/default, calibration, raw solver output, derived computation, or experimental observation;
- exact local/remote identifier and version;
- acquisition or observation date;
- artifact/run revision;
- transformation steps and code version;
- uncertainty and applicability limits;
- reviewer/check that accepted the evidence.

Do not promote a successful repair into reusable knowledge without its triggering failure, applicable solver/version/physics, supporting run, and freshness dependency.
