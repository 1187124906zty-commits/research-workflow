# Executed diffusion verification example

From the repository root:

```text
python examples/steady_diffusion/run.py --project local-runs/new-diffusion
```

Use a new output directory. The runner deliberately rejects an already initialized project rather than replacing earlier evidence. It executes a conservative 1D model with a smooth diffusion coefficient, checks actual fields against an analytical referent, registers tasks/evidence/dispositions, and writes `manuscript.md`, raw JSON/CSV, `profile.svg` and an audit.

`sample-output` contains the executed example's actual specification, six run files/fields, note and plotted profile. PNG was rasterized from that SVG for the repository preview; the editable figure is SVG. The note is a synthetic technical demonstration, with no experiment, novelty or journal acceptance claim. A real research project still needs agent judgment, journal research and appropriate independent evidence. The runner itself makes no LLM or live PaperSpine call.

![Executed profile](sample-output/profile.png)
