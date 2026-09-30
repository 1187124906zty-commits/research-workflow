# Source and dependency provenance

- `skills/simulation-project-orchestrator` is the optimized version of the local skill supplied by the project owner. The original scope, schemas and dialogue helpers are retained; the efficiency audit describes policy changes. The external local `simulation-agent-mvp` program is not bundled or patched here.
- [PaperSpine](https://github.com/WUBING2023/PaperSpine) is an optional, separately installed upstream product under the MIT license. This repository references its skill/tools and contains original file-handoff/diagnostic integration code. It does not redistribute the managed PaperSpine product or claim upstream endorsement. Consult the upstream license for that product.
- Codex instruction/skill/agent integration follows the official documentation linked in `docs/design.md`. Codex is separately installed; this repository does not supply a Codex runtime or model.
- No published paper PDFs, private research results, credentials or browser session material are included in the distribution.
