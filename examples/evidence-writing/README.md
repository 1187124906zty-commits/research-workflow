# Evidence-to-writing forward cases

These eleven new synthetic cases test research interpretation and its paragraph-level handoff. They complement the earlier `examples/behavior` decision cases; their old observed reports remain historical observations. Nothing in this directory represents an experiment, published result, or evaluation of the user's manuscript.

Give an independent agent only the current governor skill, its needed references, and `scenarios.json`. Ask it to answer the original requests with paragraph purpose, located evidence use, permitted and unresolved inference, revised passage, adjacent-context check, and the next useful action. It may select library entry IDs when available, or explain direct wording. Do not give that agent expected decisions, test assertions, or another agent's answers. Review the reasoning and text against the raw records after its return. Keyword matches, text similarity and provenance anchors do not establish scientific adequacy.

The cases address existence versus learned performance, prediction versus mechanism, conditional ranking, inverse ambiguity, training-support boundaries, amortized cost, comparison identity and warranted strong findings. W9–W11 adapt the reasoning boundaries from the separately audited Ha, Peng and Pahlavani full texts: selected versus all generated candidates, acquisition rules versus training losses/data roles, and surrogate screening versus arbitrary-target design. The figures and numerical records here are synthetic fixtures, not paper quotations or new observations. The source-reading dossier remains separate from this behavior test. Results should remain unwritten until an agent actually performs the test. Report model/test context and read scope; one run of eleven synthetic cases cannot establish reliability across disciplines or full papers.

Run the portable CLI handoff demonstration in a fresh output directory:

```text
python examples/evidence-writing/run.py --output /absolute/path/to/fresh-demo
```

It runs actual `python -m researchflow` commands and preserves their exit codes/output, a synthetic evidence fixture, a paragraph evidence trace, and a revised paragraph. It demonstrates observation-level support scoped to the fixture, narrowing an unsupported mechanism inference, and accepting an editorial delivery without promoting its claim. It invokes no LLM, live PaperSpine, solver or publisher; its deterministic text is a protocol illustration, not an observed forward-test answer. `audit` should return `protocol_ok: true` while the mechanism remains narrowed and the editorial claim remains a hypothesis. Reusing an existing state directory is refused.

Regression tests execute this real CLI in temporary projects and check dependency freshness and promotion boundaries. Their success is a software result. Independent agent judgment is a separate behavior result documented only after execution.
