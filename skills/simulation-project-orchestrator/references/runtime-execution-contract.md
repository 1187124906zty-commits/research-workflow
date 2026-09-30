# External solver runtime and evidence return

Use when the selected solver runs in a subprocess, another Python, another OS, or through MCP. Probe the actual selected executable/runtime and relevant solver capability before an expensive solve. Do not infer availability from a tool name, an unrelated interpreter import, or a previous machine's receipt.

## Execution contract

Record the input/run revision, executable or tool identifier, relevant solver/adapter/runtime versions, working directory, invocation, essential environment configuration and expected output paths. Preserve credentials outside artifacts and reports. State the time/compute budget and what output is needed to answer the assigned question.

Keep candidate inputs stable during inspection/execution. Use an immutable snapshot or content binding when concurrent edits or the backend contract require it; a descriptive version is sufficient only when this weaker assurance is explicit.

## Run and return

- Capture native logs, exit/error/refusal state, and the actual output inventory.
- Inspect needed outputs for completeness, finite values, units, state association and coordinate/time coverage.
- Persist raw evidence and the run receipt before optional profiling, extra figures or package conversions. An optional postprocessing failure must not erase a completed run's evidence.
- A handshake or zero exit code establishes only that recorded execution fact. Relevant numerical, physical, data-alignment and mechanism checks remain separate.
- If the tool refuses a check, preserve the refusal, state applicability and propose a supported alternative; never mark the unexecuted check complete.

A different runtime/backend is a new candidate with its own equation mapping and numerical evidence. Do not switch backends solely to hide a scientific failure. Repair environment errors within the task budget; after two rounds with no changed research judgment, return the evidence and a bounded alternative to the coordinator.
