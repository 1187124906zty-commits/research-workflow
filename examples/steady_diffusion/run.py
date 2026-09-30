"""Real numerical-to-manuscript example; all numbers come from the solver.

The synthetic coefficient varies smoothly. No experiment or novelty is claimed.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from researchflow import runtime as rf


def solve(n: int, alpha: float, d0: float = 1e-9, length: float = 1.0) -> dict:
    """Conservative two-point flux discretization with a Thomas solve."""
    if n < 2 or d0 <= 0 or length <= 0:
        raise ValueError("Need n>=2, positive diffusivity and length")
    h = length / n
    diffusivity = [d0 * math.exp(alpha * (i + 0.5) / n) for i in range(n)]
    m = n - 1
    diagonal = [diffusivity[i] + diffusivity[i + 1] for i in range(m)]
    lower = [-diffusivity[i] for i in range(1, m)]
    upper = [-diffusivity[i + 1] for i in range(m - 1)]
    rhs = [diffusivity[0]] + [0.0] * (m - 1)
    for i in range(1, m):
        factor = lower[i - 1] / diagonal[i - 1]
        diagonal[i] -= factor * upper[i - 1]
        rhs[i] -= factor * rhs[i - 1]
    interior = [0.0] * m
    interior[-1] = rhs[-1] / diagonal[-1]
    for i in range(m - 2, -1, -1):
        interior[i] = (rhs[i] - upper[i] * interior[i + 1]) / diagonal[i]
    concentration = [1.0, *interior, 0.0]
    fluxes = [diffusivity[i] * (concentration[i] - concentration[i + 1]) / h for i in range(n)]
    exact_flux = d0 / length if alpha == 0 else d0 * alpha / (-math.expm1(-alpha) * length)
    flux = sum(fluxes) / n
    if alpha == 0:
        exact_c = [1.0 - i / n for i in range(n + 1)]
    else:
        exact_c = [(math.exp(-alpha * i / n) - math.exp(-alpha)) / (-math.expm1(-alpha))
                   for i in range(n + 1)]
    return {
        "n": n, "alpha": alpha, "x_m": [i * h for i in range(n + 1)],
        "concentration": concentration, "exact_concentration": exact_c,
        "flux_m_per_s": flux, "exact_flux_m_per_s": exact_flux,
        "relative_flux_error": abs(flux - exact_flux) / abs(exact_flux),
        "relative_flux_spread": (max(fluxes) - min(fluxes)) / abs(flux),
        "max_concentration_error": max(abs(a - b) for a, b in zip(concentration, exact_c)),
        "bounds_ok": all(-1e-12 <= value <= 1 + 1e-12 for value in concentration),
    }


def _write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _figure(path: Path, runs: list[dict]) -> None:
    # Editable SVG, with the exact source fields retained separately.
    pieces = ['<svg xmlns="http://www.w3.org/2000/svg" width="680" height="400" viewBox="0 0 680 400">',
              '<rect width="680" height="400" fill="white"/>',
              '<g font-family="Arial" font-size="15" fill="#222">',
              '<text x="60" y="28">Verified concentration profiles (synthetic model)</text>',
              '<path d="M60 60V330H610" stroke="#222" fill="none"/>',
              '<text x="320" y="375">x (m)</text>',
              '<text x="12" y="190" transform="rotate(-90 12 190)">Normalized concentration</text>']
    for value in (0, 0.5, 1):
        pieces.append(f'<text x="{60 + 550 * value}" y="350">{value:g}</text>')
        pieces.append(f'<text x="30" y="{330 - 270 * value}">{value:g}</text>')
    for run, color in zip(runs, ("#0072B2", "#D55E00")):
        points = " ".join(f"{60 + 550 * x:.2f},{330 - 270 * c:.2f}" for x, c in zip(run["x_m"], run["concentration"]))
        pieces.append(f'<polyline points="{points}" stroke="{color}" stroke-width="2.5" fill="none"/>')
        pieces.append(f'<text x="420" y="{70 if run["alpha"] == 0 else 93}" fill="{color}">alpha = {run["alpha"]:g}</text>')
    pieces.append('</g></svg>')
    path.write_text("\n".join(pieces), encoding="utf-8")


def run(project: Path) -> dict:
    project = project.resolve()
    project.mkdir(parents=True, exist_ok=True)
    question = "Within a 1D steady transport model, does decreasing diffusivity along x reduce flux relative to a uniform coefficient?"
    rf.initialize(project, question, {
        "purpose": "Demonstrate research governance and a real numerical evidence-to-note handoff; no claim of novelty or real-material validation.",
        "facts": ["Normalized boundary values are c(0)=1 and c(1 m)=0; D0=1e-9 m^2/s."],
        "hypotheses": ["A declining coefficient creates a larger total transport resistance."],
        "uncertainties": ["Transfer to any real material has not been tested."],
        "next_decision": "Can the comparison be stated without further grid refinement?",
        "claims": [{"id": "flux-ranking", "statement": "For this stated 1D model, alpha=-1 has lower flux than alpha=0."}],
    })
    spec = {
        "equation": "d/dx(D(x) dc/dx)=0", "coefficient": "D(x)=D0 exp(alpha x/L)",
        "length_m": 1, "D0_m2_per_s": 1e-9, "alpha": [0, -1], "grid_intervals": [8, 16, 32],
        "boundary_conditions": {"c_at_0": 1, "c_at_L": 0}, "concentration_unit": "dimensionless",
        "flux_unit": "m/s", "data_role": "analytical verification; no experiments",
        "acceptance_rationale": "Use analytic error and stable ranking; errors must be smaller than one twentieth of the comparison effect. This criterion is for this comparison only.",
    }
    _write(project / "model.json", spec)
    rf.task(project, {
        "id": "pilot", "role": "rf_evidence", "question": question,
        "purpose": "Bound numerical error relative to the ranking effect before interpreting the comparison.",
        "claim_ids": ["flux-ranking"], "inputs": [{"path": "model.json"}],
        "outputs": ["runs"], "writes": ["runs"], "stage": "paper_formation",
        "acceptance": spec["acceptance_rationale"],
        "budget": {"max_attempts": 2, "max_no_progress": 2},
    })
    all_runs = [solve(n, alpha) for alpha in (0, -1) for n in (8, 16, 32)]
    for result in all_runs:
        prefix = f"a{result['alpha']:g}-n{result['n']}"
        _write(project / "runs" / f"{prefix}.json", result)
        with (project / "runs" / f"{prefix}.csv").open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(["x_m", "normalized_concentration", "analytical_concentration"])
            writer.writerows(zip(result["x_m"], result["concentration"], result["exact_concentration"]))
    final = [result for result in all_runs if result["n"] == 32]
    effect = 1 - final[1]["flux_m_per_s"] / final[0]["flux_m_per_s"]
    errors = [value["relative_flux_error"] for value in all_runs]
    verified = all(value["bounds_ok"] and value["relative_flux_spread"] < 1e-9 for value in all_runs)
    verified = verified and max(errors) < effect / 20 and effect > 0
    if not verified:
        raise RuntimeError("The actual executed comparison did not meet this example's verification contract")
    summary = {
        "question": question, "effect_fraction": effect, "final_fluxes_m_per_s": [r["flux_m_per_s"] for r in final],
        "max_relative_flux_error": max(errors), "finest_relative_flux_error": final[1]["relative_flux_error"],
        "all_bounds_ok": all(value["bounds_ok"] for value in all_runs),
        "max_relative_flux_spread": max(value["relative_flux_spread"] for value in all_runs),
        "scientific_level": "numerically verified for this model/QoI", "physical_validation": "not performed",
        "next_action": "Write the bounded comparison; no further refinement needed for the ranking question.",
    }
    _write(project / "runs/summary.json", summary)
    rf.record(project, "pilot", {
        "attempt": 1, "changed_understanding": True,
        "reason": "The ranking is stable and analytic errors are much smaller than the modeled comparison effect.",
        "evidence": [{"path": "runs/summary.json", "level": "numerical_verification", "kind": "support",
                      "claim_ids": ["flux-ranking"], "summary": "Conservative executed model and analytic comparison support only the declared ranking."}],
        "blockers": [],
    })
    rf.decide(project, "pilot", {
        "action": "accept", "reason": "Accept the finite-model comparison; retain lack of physical validation.",
        "promotions": [{"claim_id": "flux-ranking", "level": "numerical_verification", "evidence_indices": [0],
                        "reason": "Actual bounded model outputs match the analytical referent and preserve the ranking."}],
    })
    rf.task(project, {
        "id": "note", "role": "rf_paperspine", "question": "Write a reproducible note with the actual comparison and its scope.",
        "purpose": "Show evidence-shaped writing without claiming experiments, novelty or a journal decision.",
        "claim_ids": ["flux-ranking"], "inputs": [{"path": "model.json"}, {"path": "runs/summary.json"}],
        "outputs": ["manuscript.md", "profile.svg"],
        "acceptance": "Methods, executed results, analytical comparison, interpretation and real limitations are explicit.",
        "budget": {"max_attempts": 1, "max_no_progress": 1},
        "depends_on": [{"task_id": "pilot", "claim_ids": ["flux-ranking"], "required_level": "numerical_verification"}],
    })
    _figure(project / "profile.svg", final)
    manuscript = f"""# A bounded flux comparison in a one-dimensional diffusion model

*Synthetic verification and workflow demonstration. This note contains no real-material experiment, novelty claim or journal submission.*

## Question and methods

We ask whether a coefficient declining along the transport direction reduces steady flux relative to a uniform coefficient under identical boundary values. The normalized concentration obeys d/dx(D dc/dx)=0 on 0 <= x <= 1 m, with c(0)=1 and c(1 m)=0. We set D=D0 exp(alpha x/L), D0=10^-9 m²/s, and compare alpha=0 with alpha=-1. Flux has unit m/s because concentration is dimensionless.

A conservative two-point flux discretization uses midpoint coefficients and a Thomas tridiagonal solve. Runs with 8, 16 and 32 intervals are compared with the exact series-resistance result q = D0/L for alpha=0 and q=D0 alpha/[L(1-exp(-alpha))] otherwise. The verification criterion is claim-relative: analytical error must be smaller than one twentieth of the observed effect; bounded concentration and near-roundoff flux balance are also checked for this steady linear case. Actual field CSVs, model specification and run JSON are included.

## Results

At 32 intervals, the uniform and declining cases yield fluxes of {final[0]['flux_m_per_s']:.8e} and {final[1]['flux_m_per_s']:.8e} m/s. The modeled reduction is {100 * effect:.3f}%. The finest-grid relative analytical flux error for alpha=-1 is {100 * final[1]['relative_flux_error']:.6f}%; the largest across the planned grids is {100 * max(errors):.6f}%. Concentrations stay within [0,1]. The maximum relative flux spread is {summary['max_relative_flux_spread']:.3e}. Figure `profile.svg` is generated from the actual 32-interval fields.

## Interpretation and limits

The exact total resistance is the integral of 1/D(x). A declining coefficient increases this resistance, supporting the lower modeled flux. The ranking and error-to-effect separation answer the contracted comparison, so additional mesh refinement has no identified value for that question. This is an explanation within the stated equation and boundary conditions. It does not establish a physical mechanism in a tested material, calibrated parameter values, applicability to higher dimensions, or experimental validation. Selecting a real journal and establishing material relevance require separate evidence.

## Reproducibility and evidence

Run `python examples/steady_diffusion/run.py --project <new-output-directory>` from the ResearchFlow repository. The claim `flux-ranking` links to `runs/summary.json` and the frozen `model.json` through research state. This note is generated deterministically from executed outputs; a real writer/reviewer agent must interpret the evidence for a real paper. The example runner itself does not call an LLM, live PaperSpine or submit a manuscript.
"""
    (project / "manuscript.md").write_text(manuscript, encoding="utf-8")
    rf.record(project, "note", {
        "attempt": 1, "changed_understanding": True,
        "reason": "The executed comparison has been stated with reproducible methods and the unsupported empirical scope excluded.",
        "evidence": [{"path": "manuscript.md", "level": "observation", "kind": "observation", "claim_ids": ["flux-ranking"],
                      "summary": "Actual generated note, ready for independent review of the demonstration."}], "blockers": [],
    })
    rf.decide(project, "note", {"action": "accept", "reason": "Accept the demonstration note as an artifact; no new scientific promotion."})
    audit = rf.audit(project)
    _write(project / "audit.json", audit)
    if not audit["protocol_ok"]:
        raise RuntimeError("Example produced unresolved protocol risks; inspect audit.json")
    return {"project": str(project), "summary": summary, "protocol_ok": audit["protocol_ok"], "manuscript": str(project / "manuscript.md")}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.project), indent=2, ensure_ascii=False))
