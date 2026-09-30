# openPASO backend contract

Read this reference when openPASO is selected as an execution or numerical-verification backend.

## Capability truth

Treat three inventories separately:

1. **control package**: whether the requested openPASO package and MCP entry point exist;
2. **tool handlers**: the names returned by an actual MCP initialize/list-tools exchange;
3. **solver backends**: the external solvers that `openpaso doctor` proves operational.

Do not report that a solver is installed merely because its adapter or MCP handler exists. Keep package metadata and MCP `serverInfo.version` as separate observed fields when their formatting differs.

On Windows, prefer a dedicated Python 3.10--3.13 runtime. Run `openpaso doctor`, then an MCP handshake and tool enumeration. A partial local installation remains `PARTIAL` even if a different previously installed runtime is operational. Do not remove required dependencies merely to make installation appear successful; openPASO uses ADIOS2 to inspect `.bp` output for non-finite values.

## Reviewed execution

Submit the critic review, obtain its token and call `run_simulation` in the same MCP session. Preserve the review text, token-bearing native receipt, solver log, job directory and output inventory. This binds the receipt to one review submission but does not prove the reviewer's identity, independence or scientific adequacy; those are orchestration-layer records.

Never promote `is_error=true`, a refused verification, missing output, nonzero solver exit, or malformed payload into execution success. Preserve initial refusals and repair history. A reachable solver that produces a scientifically failed result is evidence, not a reason to silently switch backends.

## Applicability of verification tools

Use each openPASO verifier only within its encoded mathematical scope. Record `NOT_APPLICABLE` when the tool cannot represent the equation, coordinate weighting, boundary condition, coupling or field location. Do not coerce an axisymmetric weighted weak form with Robin boundaries into a Cartesian constant-coefficient checker.

When a verifier needs a transformed field representation, preserve:

- the native field;
- the deterministic conversion code and versions;
- units, coordinates and point/cell association;
- the transform's interpolation or averaging error;
- the original refusal and the later applicable result.

An openPASO audit or residual check is one evidence item. Independently retain mesh/time convergence, analytic/MMS comparison, conservation/interface balances, solver residuals and application-specific validation.

## Claim ceiling

- MCP initialized and job completed: at most `EXECUTED`.
- Applicable numerical checks and independent recomputation passed: may support `NUMERICALLY_VERIFIED` for the frozen equation/discretization.
- Physical validation: additionally requires an aligned real referent, independently sourced conditions/data, measurement operator, uncertainty, replication appropriate to the claim, and a predeclared statistic/threshold.

No backend receipt, critic token or clean audit can bypass these ceilings.
