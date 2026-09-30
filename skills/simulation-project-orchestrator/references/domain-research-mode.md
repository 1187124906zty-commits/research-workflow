# Multi-agent domain research before implementation

## Aim

Produce a simulation that answers the user's physical question at a scale
comparable to relevant reality and literature. Mesh resolution is one part of
this decision. Model fidelity, geometry, dimensionality, constitutive laws,
loads, boundary conditions, source shape, phase/interface behavior, measurements,
typical result magnitudes and established remedies all belong to the research.
Do not interpret "use a simple compatible solver" as "use the smallest model".

## Scoped roles and direct exchanges

For substantive applications, dispatch these responsibilities to allowed models.
A model may own several roles on different artifacts, but cannot independently
review its own artifact. Roles do not require all concurrency slots at once.

1. **Literature and experimental evidence.** Read submitted papers first. Locate
   the system, experiment, numerical paper and reference data. Trace figures,
   tables and conditions to primary sources. Extract reported and missing
   parameters, geometry, assumptions, measurement definitions, repetition and
   uncertainty. Reply to the domain role's specific data requests.
2. **Domain modeling.** Read representative application studies and established
   solver examples. Explain dominant phenomena, typical scales, model families
   and useful regimes, common difficulties and practical treatments. Select a
   supported baseline and justified omissions. State which inputs are essential,
   which can be bounded and which need sensitivity; request them before coding.
3. **Implementation and runtime.** Inspect actual software/API versions. Map the
   model to mature framework features. Estimate actual cells, DOFs/particles,
   history length, memory and solve cost. Ask the domain role whether symmetry,
   dimensional reduction, local domain or reference-frame simplifications
   preserve the physical question. Do not choose numerics in isolation.
4. **Mechanism and results.** Read how the reference studies analyze physics,
   beyond their accuracy tables. Form the research question, alternative causes,
   expected magnitudes and trends, necessary fields and useful plots. Request
   outputs before execution. Initiate bounded exploratory runs after checking
   the numerical foundation, preserving data roles.
5. **Independent review.** Check the combined research contract against located
   sources and installed software. Challenge consequential simplifications and
   missing conditions. Reuse deterministic fixed checks; scientific anomalies
   receive scoped reasoning at an adequate strength.

Require relevant direct exchanges: domain→evidence for conditions, implementation
→domain for feasible scale/closure, mechanism→implementation for outputs, and
reviewer→producer for obligations. Record direct replies and requester
dispositions; coordinator summaries cannot replace expert answers.

## Bounded research contract

Save one evolving `domain-research-contract` with source locators and statuses:

- physical problem, intended use and experimental referent;
- actual geometry/operating scales, model family, dimensionality and processes;
- QoI-dependent minimum model: which representation answers each requested
  observable, and which mechanism claims require additional physics or dimensions;
- literature computation scale where reported, local/full domain, mesh/DOFs/
  particles and transient/steady representation;
- problem-specific details, their importance and established treatments;
- parameter completeness and explicitly bounded assumptions;
- mature solver features/version, application mesh/time/domain plan;
- experimental/literature magnitudes and trends for plausibility checks;
- measurement mapping, data roles, repetition, uncertainty and validation plan;
- mechanism questions, alternatives and raw-output obligations;
- unresolved issue, concrete remedy and responsible role.

Mark unreported numerical details `NOT_REPORTED`; never invent them. Comparable
scale does not require copying a paper's discretization or forcing its results.
Explain why a reduced domain/different method represents the same phenomenon
and check its relevant effect. Published values may be nonblind development
knowledge; do not relabel them blind validation later.

Start the application when consequential physics, inputs, measurements and
solver strategy are sufficiently understood for its use. Do not require an
exhaustive survey. A bounded assumption triggers a planned sensitivity, rather
than automatic refusal. Permit separate labeled exploratory calculations while
uncertain conditions are investigated.

## Research-to-implementation decision

Before dispatching script production, the domain and implementation roles agree
on a short scale-and-fidelity envelope inside that same contract:

- the actual geometry and operating scales, the phenomena and smallest physical
  structures needed to answer the question, and the expected QoI order of magnitude;
- the representative literature model families and computation scales actually
  reported, including what a supported lower-cost representation preserves;
- consequential details such as free surfaces, phase changes, contact, source
  profiles, constitutive limits or measurement response, with the source-backed
  common treatment and the consequence of omitting each relevant detail;
- the chosen mature backend, useful application scale, actual resource estimate,
  saved outputs and a finite numerical/sensitivity matrix;
- the incoming data requests already answered, the bounded assumptions to test,
  and only those missing facts that prevent the named scientific use.

The independent reviewer tests whether this envelope can answer the physical
question. More cells do not repair missing physics or an unmatched measurement.
Conversely, a smaller domain, symmetry or a different numerical method is
admissible when its retained phenomena and sensitivity are demonstrated. Do not
turn a source's unreported mesh/time details into mandatory missing experimental
inputs. Do not require every possible mechanism or an exhaustive literature
survey before a useful, explicitly scoped application starts.

Use the relevant competing process scales before accepting a model family or
symmetry. One regime label is insufficient: for example, a small Reynolds number
supports laminar flow but does not exclude buoyancy; tube orientation can change
the symmetry of a conjugate heat-transfer problem. The domain role names the
missing condition that decides the reduction, and the implementation role either
uses a compatible conditional model or investigates its effect. Cell counts,
memory and runtime inferred before execution remain estimates until measured.

Dispatch implementation with the contract, located sources, parameter status,
output obligations and the review disposition, not just a prose equation. When
results fall outside the documented scale/trend envelope, open a targeted
cross-role question and investigate whether numerics, conditions, the model or
the observation caused it; do not force agreement with published numbers.

## Repair loop

On a discrepancy, implementation/numerical roles first check their own mapping,
actual framework state, termination, suitable scale and output processing. Send
the unexplained residual pattern to evidence/domain roles with competing causes.
The responsible role locates relevant conditions, model limits or remedies,
answers with evidence, and the requester records its disposition. Implement the
best supported repair and rerun the meaningful application.

Do not make every discrepancy a resolution issue. Investigate material, source,
boundary, measurement mismatch and omitted physics using domain evidence. Do
not fit all possible causes at once. Preserve calibration and comparison roles;
use controlled changes to discriminate explanations. Present physical findings,
experimental comparison, numerical limits and remaining model discrepancy
together in the report.

A literature remedy belongs to its reported regime, source/closure and signed
residual pattern. Before importing it, the domain role compares those conditions
with the current model and asks the evidence role to confirm the relevant table
or figure. The implementation role states the expected signed effect, and the
requester records whether transfer is justified. Calibrated coefficients are not
universal material constants; a remedy that corrected the opposite discrepancy
must not be copied simply because it appeared in a similar application.
