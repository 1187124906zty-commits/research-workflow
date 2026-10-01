"""Plot the actual table interpolants and stated L/H continuations, not PDE data.

Python/Matplotlib is the established manuscript plotting workflow. All table
rows are retained in source-data.csv; the requested display range is 25–2200 C.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import csv
import importlib.util
import json
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

OUT = Path(__file__).resolve().parent
PAPER = OUT.parents[1]
INPUT = PAPER / "data/material-properties.csv"
HELPER = Path("C:/Users/Administrator/.codex/skills/nature-figure/scripts/audit_panel_alignment.py")
spec = importlib.util.spec_from_file_location("panel_alignment", HELPER)
alignment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(alignment)
require_matplotlib_panel_alignment = alignment.require_matplotlib_panel_alignment

with INPUT.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
verified = json.loads((PAPER / "evidence/verified-data.json").read_text(encoding="utf-8"))["physical_model"]["material_table_rows"]
assert len(rows) == len(verified) == 27
for row, ref in zip(rows, verified):
    assert row["property"] == ref["property"]
    assert float(row["temperature_C"]) == ref["temperature_C"]
    assert float(row["value"]) == ref["value"]
with (OUT / "property-table-source-data.csv").open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

mpl.rcParams.update({"font.family":"sans-serif", "font.sans-serif":["DejaVu Sans", "Arial"],
 "font.size":9, "axes.labelsize":10, "axes.titlesize":10,
 "xtick.labelsize":9, "ytick.labelsize":9,
 "axes.spines.top":False, "axes.spines.right":False, "axes.linewidth":0.7,
 "pdf.fonttype":42, "svg.fonttype":"none", "legend.frameon":False,
 "savefig.facecolor":"white"})
fig, axes = plt.subplots(1, 2, figsize=(7.086614173228346, 3.7401574803149606))
fig.subplots_adjust(left=0.085, right=0.984, bottom=0.30, top=0.87, wspace=0.32)
colors = {"common":"#42484F", "L":"#0072B2", "H":"#D55E00"}
curve_rows = []
panel_records = []
for idx, (kind, title, ylim, ylabel, endpoint_label) in enumerate([
 ("k", "Conductivity continuation", (8, 59), "Conductivity, k (W m⁻¹ K⁻¹)", "982 °C, k = 25.2"),
 ("cp", "Sensible-storage continuation", (395, 1000), "Specific heat, cₚ (J kg⁻¹ K⁻¹)", "1093 °C, cₚ = 670")]):
    axis = axes[idx]
    selected = [r for r in rows if r["property"] == kind]
    temp = np.array([float(r["temperature_C"]) for r in selected])
    value = np.array([float(r["value"]) for r in selected])
    assert np.all(np.diff(temp) > 0) and np.all(value > 0)
    endpoint = temp[-1]
    slope = (value[-1]-value[-2])/(temp[-1]-temp[-2])
    common_t = np.unique(np.r_[25.0, temp[(temp >= 25)&(temp <= endpoint)], endpoint])
    common_v = np.interp(common_t, temp, value)
    high_t = np.linspace(endpoint, 2200, 220)
    high_L = value[-1]+slope*(high_t-endpoint)
    high_H = np.full_like(high_t, value[-1])
    assert endpoint == (982 if kind == "k" else 1093)
    axis.axvspan(1290, 1350, facecolor="#DDE3E7", edgecolor="none", alpha=0.7, zorder=0)
    axis.axvline(endpoint, ymax=0.72, color="#9EA6AE", lw=0.7, ls=(0,(3,3)), zorder=1)
    axis.axvline(1290, ymax=0.72, color="#ADB5BD", lw=0.65, zorder=1)
    axis.axvline(1350, ymax=0.72, color="#ADB5BD", lw=0.65, zorder=1)
    axis.plot(common_t, common_v, color=colors["common"], lw=1.6, zorder=3)
    shown = temp >= 25
    axis.plot(temp[shown], value[shown], "o", color=colors["common"], ms=3, zorder=4)
    axis.plot(high_t, high_L, color=colors["L"], lw=1.7, zorder=3)
    axis.plot(high_t, high_H, color=colors["H"], lw=1.7, ls=(0,(4,2)), zorder=3)
    axis.set(xlim=(25,2200), ylim=ylim, xticks=[25,500,1000,1500,2000],
             xlabel="Temperature (°C)", ylabel=ylabel, title=title)
    axis.tick_params(length=3, width=0.65)
    axis.text(-0.16, 1.075, chr(97+idx), transform=axis.transAxes, fontsize=11, fontweight="bold")
    axis.text(0.025, 0.935, f"Full table: {temp[0]:.0f} to {endpoint:.0f} °C", transform=axis.transAxes,
              fontsize=8.5, va="top", color=colors["common"])
    # The phase thresholds are close on the common axis; one explicit label
    # identifies both boundaries rather than placing overlapping tick labels.
    axis.text(0.66, 0.30, "Tₛ = 1290 °C\nTₗ = 1350 °C", transform=axis.transAxes,
              fontsize=8.5, va="top", color="#59616A")
    axis.text(0.025, 0.805, "Endpoint: "+endpoint_label, transform=axis.transAxes,
              fontsize=8.1, va="top", color=colors["common"])
    for t,v in zip(common_t, common_v):
        curve_rows.append({"property":kind,"temperature_C":float(t),"value":float(v),"rule":"common_interpolation"})
    for t,a,b in zip(high_t,high_L,high_H):
        curve_rows.extend([{"property":kind,"temperature_C":float(t),"value":float(a),"rule":"L_final_secant"},
                           {"property":kind,"temperature_C":float(t),"value":float(b),"rule":"H_last_value"}])
    panel_records.append({"panel":chr(97+idx),"property":kind,"full_table_rows":len(temp),
      "markers_in_display":int(shown.sum()),"display_range_C":[25,2200],"endpoint_C":float(endpoint),
      "final_slope":float(slope),"uncertainty":"none: supplier table and deterministic continuation rules; no statistical ensemble"})
handles = [Line2D([],[],color=colors["common"],lw=1.6,marker="o",ms=3,label="Table interpolation"),
           Line2D([],[],color=colors["L"],lw=1.7,label="L: final-slope continuation"),
           Line2D([],[],color=colors["H"],lw=1.7,ls=(0,(4,2)),label="H: last-value holding")]
fig.legend(handles=handles,loc="lower center",bbox_to_anchor=(0.53,0.071),ncol=3,
           fontsize=8.5,handlelength=2.0,columnspacing=1.35)
fig.text(0.53,0.021,"Shaded interval: Tₛ ≤ T < Tₗ; latent addition to cₚ,eff = 4666.7 J kg⁻¹ K⁻¹",ha="center",fontsize=8.5)
fig.canvas.draw()
require_matplotlib_panel_alignment(fig,json_out=OUT / "ammt-property-continuations.alignment.json",
                                  axes=axes, require_panel_labels=True)
fig.savefig(OUT / "ammt-property-continuations.pdf")
fig.savefig(OUT / "ammt-property-continuations.svg")
fig.savefig(OUT / "ammt-property-continuations.png", dpi=600)
with (OUT / "property-continuation-curves.csv").open("w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=curve_rows[0].keys());writer.writeheader();writer.writerows(curve_rows)
(OUT / "property-figure-contract.json").write_text(json.dumps({
 "question":"Where does actual tabulated interpolation end, and how do the two implemented continuation rules differ in the phase-change and hotter ranges?",
 "claim":"All adopted mushy and liquid states exceed the actual k and cp endpoints; L and H are two explicit model choices for that missing range.",
 "archetype":"quantitative grid", "backend":"Python/Matplotlib established workflow",
 "size_mm":[180,95],"PDE_runs":0,"panels":panel_records,
 "source_rows_retained":27,"display_subset_note":"Rows below 25 C are retained in source data and used to interpolate 25 C; the display is the requested 25–2200 C window."},
 ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
plt.close(fig)
print("Created PDF/SVG/PNG, source tables, continuation curves, contract and alignment record.")
