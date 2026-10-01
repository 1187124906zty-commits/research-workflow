"""Read-only inspection of retained AMMT data; no solver/PDE imports or runs.

Writes only this specialist's revision-r2/methods-results directory. The imported
passage_observer is a pure saved-field postprocessor, not a simulation driver.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import csv
import hashlib
import importlib.util
import json
import math
import numpy as np

OUT = Path(__file__).resolve().parent
PAPER = OUT.parents[1]
DATA = json.loads((PAPER / "evidence/verified-data.json").read_text(encoding="utf-8"))
BASE = Path(DATA["task"]["source_root"])

def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def crossings(x, t, level):
    indices = np.flatnonzero((t[:-1] >= level) != (t[1:] >= level))
    return [float(x[i] + (level-t[i])*(x[i+1]-x[i])/(t[i+1]-t[i])) for i in indices]

with (BASE / "material-properties.csv").open(encoding="utf-8-sig", newline="") as stream:
    table = list(csv.DictReader(stream))
expected = DATA["physical_model"]["material_table_rows"]
assert len(table) == len(expected)
for row, old in zip(table, expected):
    assert row["property"] == old["property"]
    assert float(row["temperature_C"]) == old["temperature_C"]
    assert float(row["value"]) == old["value"]
properties = {}
for kind in ("k", "cp"):
    rows = [r for r in table if r["property"] == kind]
    knots = [[float(r["temperature_C"]), float(r["value"])] for r in rows]
    slope = (knots[-1][1]-knots[-2][1])/(knots[-1][0]-knots[-2][0])
    properties[kind] = {"knots_T_C_value": knots, "last_slope": slope,
                        "endpoint_C": knots[-1][0], "held_value": knots[-1][1]}
assert properties["k"]["endpoint_C"] == 982
assert properties["cp"]["endpoint_C"] == 1093

spec = importlib.util.spec_from_file_location("saved_field_observer", BASE / "solver/passage_observer.py")
observer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(observer)
digests = {}
runs = []
for old in DATA["runs"]:
    run = Path(old["directory"])
    manifest, result = load(run / "manifest.json"), load(run / "result.json")
    bindings = []
    for ref in manifest["source_bindings"]:
        original = Path(ref["path"])
        frozen = {"fipy_application_frame.py": "frozen-solver-source.py",
                  "run_constitutive_factorial.py": "frozen-factorial-wrapper.py"}.get(original.name)
        path = run / frozen if frozen else original
        if path not in digests:
            digests[path] = hashlib.sha256(path.read_bytes()).hexdigest()
        matches = digests[path] == ref["sha256"]
        assert matches, str(path)
        bindings.append({"path": str(path), "matches_executed_binding": matches,
                         "identity": "executed_snapshot" if frozen else "current_dependency_matches_manifest"})
    with np.load(run / "fields.npz", allow_pickle=False) as f:
        temp, phi = f["T_C"], f["liquid_fraction"]
        assert np.all(np.isfinite(temp)) and float(temp.min()) >= 24.9
        assert float(phi.min()) >= 0 and float(phi.max()) <= 1
        x, center = f["x_m"], f["surface_y0_T_C"]
        ts, tl = crossings(x, center, 1290), crossings(x, center, 1350)
        assert len(ts) == len(tl) == 2
        length = (ts[1]-ts[0])*1e6
        assert math.isclose(length, result["L"]["length_m"]*1e6, abs_tol=1e-9)
        power = float(np.sum(f["top_q_W_m2"]*np.diff(f["x_faces_m"])[:, None]*np.diff(f["y_faces_m"])[None, :]))
        assert math.isclose(power, manifest["eta"]*manifest["power_W"]/2, abs_tol=1e-8)
        roi = result["passage_geometry"]["ROI_m"]
        geometry, _, _, _ = observer.passage_max_roi(temp, f["surface_T_C"], center,
                        f["y_m"], f["z_m"], roi["y"][1], roi["z"][0])
        assert geometry["qualified"]
        differences = {q: (geometry[q+"_m"]-result[q+"_fusion_m"])*1e6 for q in ("W", "D")}
        assert max(map(abs, differences.values())) < 1e-9
        runs.append({"run": old["run"], "source": str(run), "shape": list(temp.shape),
          "L_um": length, "W_um": geometry["W_m"]*1e6, "D_um": geometry["D_m"]*1e6,
          "Ts_crossings_um": [v*1e6 for v in ts], "Tl_crossings_um": [v*1e6 for v in tl],
          "rear_phase_span_um": (tl[0]-ts[0])*1e6,
          "rear_phase_passage_us": (tl[0]-ts[0])/manifest["speed_m_s"]*1e6,
          "half_power_W": power, "reproduced_passage_geometry_difference_um": differences,
          "finite_temperature": True, "phase_bounds": [float(phi.min()), float(phi.max())],
          "surface_peak_C": float(f["surface_T_C"].max()), "source_bindings": bindings})

corners = {r["branch"]: r for r in DATA["factorial"]["rows"]}
effects = {}
for key in ("L_um", "W_um", "D_um", "Ts_rear_um", "Ts_front_um", "Tl_rear_um", "rear_phase_span_um"):
    a,b,c,d = [corners[x][key] for x in ("LL", "HL", "LH", "HH")]
    effects[key] = {"k_at_cp_L": b-a, "k_at_cp_H": d-c,
       "cp_at_k_L": c-a, "cp_at_k_H": d-b,
       "interaction": d-b-c+a, "joint": d-a}
    assert math.isclose(effects[key]["k_at_cp_L"]+effects[key]["cp_at_k_L"]+effects[key]["interaction"], d-a, abs_tol=1e-9)
effects["rear_solidus_fraction_of_k_length_increase_percent"] = 100*abs(effects["Ts_rear_um"]["k_at_cp_L"])/effects["L_um"]["k_at_cp_L"]
metrics = {m["case"]: m for m in DATA["research_case_metrics"]}
b,c = metrics["B"], metrics["C"]
transforms = {"C_vs_B_span_percent": 100*(c["rear_Ts_Tl_span_um"]/b["rear_Ts_Tl_span_um"]-1),
 "C_vs_B_passage_percent": 100*(c["rear_phase_passage_us"]/b["rear_phase_passage_us"]-1),
 "C_vs_B_cooling_percent": 100*(c["model_centerline_Tl_to_Ts_mean_cooling_MK_s"]/b["model_centerline_Tl_to_Ts_mean_cooling_MK_s"]-1),
 "C_vs_B_model_aspect_ratio_percent":100*(c["model_width_depth_ratio"]/b["model_width_depth_ratio"]-1)}
matched = DATA["factorial"]["matched_temperature_properties"]
ll = next(r for r in matched["LL"] if r["T_C"] == 1320)
lh = next(r for r in matched["LH"] if r["T_C"] == 1320)
hl = next(r for r in matched["HL"] if r["T_C"] == 1320)
transforms.update({"at_1320_k_hold_change_percent":100*(hl["k_W_mK"]/ll["k_W_mK"]-1),
 "at_1320_sensible_cp_hold_change_percent":100*(lh["cp_J_kgK"]/ll["cp_J_kgK"]-1),
 "at_1320_effective_cp_hold_change_percent":100*(lh["cp_effective_J_kgK"]/ll["cp_effective_J_kgK"]-1),
 "at_1320_enthalpy_hold_change_percent":100*(lh["enthalpy_from_T0_J_m3"]/ll["enthalpy_from_T0_J_m3"]-1),
 "rear_hot_CV_diffusive_outward_HL_minus_LL_W":corners["HL"]["hot_rear_net_outward_diffusive_W"]-corners["LL"]["hot_rear_net_outward_diffusive_W"]})
for row in DATA["comparison_rows"]:
    assert math.isclose((row["simulated_um"]-row["experimental_um"])/row["expanded_uncertainty_um"], row["signed_difference_over_expanded_U"], abs_tol=1e-12)
record = {"task":"METHODS_RESULTS_R2_READ_ONLY_AUDIT", "PDE_runs":0,
  "imported":"pure passage_observer saved-field postprocessor only; no solver/driver",
  "input": str(PAPER / "evidence/verified-data.json"), "properties":properties,
  "runs":runs, "effects":effects, "derived":transforms,
  "claim_ceiling":"retained-output reproducibility, deterministic within-model comparison; no new physical validation"}
(OUT / "computed-audit.json").write_text(json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False)+"\n", encoding="utf-8")
print(json.dumps({"runs_rechecked":len(runs),"PDE_runs":0,"all_binding_matches":True,
 "all_primary_passage_geometry_reproduced":True,"endpoints_C":{k:v["endpoint_C"] for k,v in properties.items()},
 "derived":transforms}, ensure_ascii=False, indent=2))
