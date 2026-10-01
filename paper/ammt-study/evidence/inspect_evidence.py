"""Read retained AMMT artifacts only; no solver imports or executions."""
from pathlib import Path
import csv
import hashlib
import json
import math
import numpy as np

BASE = Path(r"C:/Users/Administrator/Documents/ChatGPT/电脑答疑/simulation-agent-mvp/research/reproduction-case/nist-amb2018-02")
OUT = Path(__file__).resolve().parent

def readj(relative):
    return json.loads((BASE / relative).read_text(encoding="utf-8"))

def readc(relative):
    with (BASE / relative).open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        for key, value in row.items():
            try:
                row[key] = float(value)
            except (TypeError, ValueError):
                pass
    return rows

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def crossings(x, values, threshold):
    hit = values >= threshold
    ii = np.flatnonzero(hit[:-1] != hit[1:])
    return [float(x[i] + (threshold-values[i])*(x[i+1]-x[i])/(values[i+1]-values[i])) for i in ii]

app = readj("report/application-research-results.json")
current = readj("report/current-results.json")
factor = readj("report/constitutive-factorial-results.json")
comparisons = readc("report/experimental-comparison.csv")
factor_rows = readc("report/constitutive-factorial-metrics.csv")
effects = readc("report/constitutive-factorial-effects.csv")

run_names = ["fipy-application-A-frozen-r13", "fipy-application-B-cal-05-r13", "fipy-application-C-frozen-r13", "fipy-application-B-highT-frozen-r14", "fipy-application-B-khold-cplinear-r15", "fipy-application-B-klinear-cphold-r15"]
runs = []
for name in run_names:
    root = BASE / "verification" / name
    manifest = readj(f"verification/{name}/manifest.json")
    result = readj(f"verification/{name}/result.json")
    histories = readc(f"verification/{name}/history.csv")
    bindings = []
    for binding in manifest["source_bindings"]:
        original = Path(binding["path"])
        filename = original.name
        snapshot_name = {"fipy_application_frame.py": "frozen-solver-source.py", "run_constitutive_factorial.py": "frozen-factorial-wrapper.py"}.get(filename)
        inspected = root / snapshot_name if snapshot_name else original
        observed_digest = digest(inspected) if inspected.is_file() else None
        bindings.append({"recorded_path": str(original), "inspected_path": str(inspected), "recorded_sha256": binding["sha256"], "observed_sha256": observed_digest, "matches": observed_digest == binding["sha256"], "binding_kind": "executed_snapshot" if snapshot_name else "live_dependency_checked_against_executed_binding"})
    with np.load(root / "fields.npz", allow_pickle=False) as fields:
        x = fields["x_m"]
        center = fields["surface_y0_T_C"]
        ts = crossings(x, center, 1290.)
        tl = crossings(x, center, 1350.)
        t = fields["T_C"]
        surf = fields["surface_T_C"]
        phi = fields["liquid_fraction"]
        q = fields["top_q_W_m2"]
        dx = np.diff(fields["x_faces_m"])
        dy = np.diff(fields["y_faces_m"])
        power = float(np.sum(q * dx[:, None] * dy[None, :]))
        array_audit = {"source_path": str(root / "fields.npz"), "keys": list(fields.files), "shape": list(t.shape), "all_T_finite": bool(np.all(np.isfinite(t))), "T_min_C": float(t.min()), "T_cell_max_C": float(t.max()), "T_surface_max_C": float(surf.max()), "liquid_fraction_min": float(phi.min()), "liquid_fraction_max": float(phi.max()), "q_min_W_m2": float(q.min()), "integrated_half_source_W": power, "half_power_expected_W": manifest["eta"]*manifest["power_W"]/2., "half_power_difference_W": power-manifest["eta"]*manifest["power_W"]/2., "Ts_centerline_crossings_m": ts, "Tl_centerline_crossings_m": tl, "L_reconstructed_from_retained_centerline_um": (ts[1]-ts[0])*1e6 if len(ts)==2 else None, "L_vs_result_difference_um": ((ts[1]-ts[0])-result["L"]["length_m"])*1e6 if len(ts)==2 else None}
    row = {"run": name, "directory": str(root), "role": "production condition or deterministic constitutive corner; not an experimental replicate", "power_W": manifest["power_W"], "speed_m_s": manifest["speed_m_s"], "eta": manifest["eta"], "branch": manifest["branch"], "cells": manifest["cells"], "core_dx_dy_dz_m": manifest["core_dx_dy_dz_m"], "domain_m": manifest["domain_m"], "candidate": manifest["candidate"], "framework": manifest["framework"], "boundary_recipe": manifest["boundary_recipe"], "primary_observers": manifest["primary_observers"], "result_source": str(root / "result.json"), "L_um": result["L"]["length_m"]*1e6, "W_um": result["W_fusion_m"]*1e6, "D_um": result["D_fusion_m"]*1e6, "surface_peak_C": result["surface_peak_C"], "temperature_min_C": result["temperature_min_C"], "iterations": result["iterations"], "duration_s": result["duration_s"], "nonlinear_equation_L1_relative": result["nonlinear_equation_L1_relative"], "balance_relative": result["balance_relative"], "final_correction_T_C": result["final_correction_T_C"], "fusion_geometry": result["fusion_geometry"], "passage_geometry": result["passage_geometry"], "history_accepted_min_C": min(r["min_T_C"] for r in histories), "history_accepted_max_C": max(r["max_T_C"] for r in histories), "history_rows": len(histories), "raw_fields_audit": array_audit, "source_binding_audit": bindings, "mechanism_fields_present": (root / "mechanism-fields.npz").is_file(), "science_gate_as_stored": result["science_gate"]}
    assert array_audit["all_T_finite"]
    assert array_audit["liquid_fraction_min"] >= 0 and array_audit["liquid_fraction_max"] <= 1
    assert abs(array_audit["half_power_difference_W"]) < 1e-8
    assert abs(array_audit["L_vs_result_difference_um"]) < 1e-9
    assert all(v["matches"] for v in bindings), (name, bindings)
    runs.append(row)

bycase = {(r["case"],r["observable"]):r for r in comparisons}
for row in comparisons:
    row["signed_difference_um"] = row["simulated_um"]-row["experimental_um"]
    row["inside_source_expanded_U_scale"] = abs(row["signed_difference_over_expanded_U"]) <= 1
    row["source"] = str(BASE / "report/experimental-comparison.csv")
    assert math.isclose(row["signed_difference_over_expanded_U"], row["signed_difference_um"]/row["expanded_uncertainty_um"], rel_tol=1e-13)

derived_trends = {}
for qoi in ("L","W","D"):
    b,c = bycase[("B",qoi)],bycase[("C",qoi)]
    derived_trends[qoi] = {"model_C_minus_B_um": c["simulated_um"]-b["simulated_um"], "experiment_C_minus_B_um": c["experimental_um"]-b["experimental_um"], "model_C_vs_B_percent": 100*(c["simulated_um"]/b["simulated_um"]-1), "experiment_C_vs_B_percent": 100*(c["experimental_um"]/b["experimental_um"]-1), "combined_expanded_U_if_uncorrelated_um": math.hypot(b["expanded_uncertainty_um"],c["expanded_uncertainty_um"]), "uncertainty_note": "Descriptive class-mean contrast; cross-condition covariance not supplied. Quadrature scale assumes zero correlation and is not a new uncertainty validation model."}

efflookup = {r["quantity"]:r for r in effects}
corner = {r["branch"]:r for r in factor_rows}
for qoi in ("L_um","W_um","D_um"):
    direct = corner["HH"][qoi]-corner["LL"][qoi]
    composed = efflookup[qoi]["k_effect_at_cp_linear"]+efflookup[qoi]["cp_effect_at_k_linear"]+efflookup[qoi]["interaction_HH_HL_LH_LL"]
    assert math.isclose(direct, composed, rel_tol=1e-12, abs_tol=1e-12)

cal = app["calibration"]
matrix = [{k:r[k] for k in ("case","cells","dx_dy_dz_um","eta","L_um","W_um","D_um","L1","final_correction_C","balance","duration_s")} | {"source":r["directory"]} for r in app["numerical_matrix"]]
neigh = readj("verification/fipy-application-neighborhood-r14/summary.json")
data = {"schema": "AMMT_EXISTING_EVIDENCE_DOSSIER_V1", "task": {"stage":"paper_formation", "scope":"read-only retained-source/array inspection; no solver imports, no PDE reruns", "source_root": str(BASE), "output_root":str(OUT), "production_unique_runs":len(runs), "disjoint_count_explanation":"A/B/C use 3; B four corners LL/HL/LH/HH use 4 including B reused as LL; union=6. Additional calibration and verification runs are historical evidence, not included in this six-run production count."}, "physical_model":{"candidate":"FIPY_APPLICATION_MOVING_FRAME_V5", "lab_equation":"partial_t H = div(k(T) grad T)", "moving_equation":"div(u H - k(T) grad T)=0; u=(-v,0,0), xi=x-vt", "enthalpy":"H=rho*(integral[T0,T] cp(theta)dtheta + latent*f(T))", "rho_kg_m3":8440.,"latent_J_kg":280000.,"Ts_C":1290.,"Tl_C":1350.,"T0_C":25.,"phase_fraction":"0 below Ts; (T-Ts)/(Tl-Ts) in [Ts,Tl); 1 at/above Tl", "C0_J_m3_K":3392880.,"U":"H/C0, unit K; this is a scale variable, not actual temperature", "laser":"q=2*eta*P/(pi*w^2)*exp(-2*(xi^2+y^2)/w^2)","w_m":85e-6,"D4sigma_m":170e-6,"source_location":"top z=0; flux integrated over each rectangle using erf, represented as equivalent source in top control volume", "material_table":str(BASE/'material-properties.csv'),"material_table_rows":readc('material-properties.csv'),"property_roles":"Tabulated alloy bulletin data; high-T interpolation/continuation, constant density/latent heat and linear equilibrium fraction are model closures, not measured high-T IN625 specimen properties.","omitted_physics":["liquid momentum and Marangoni flow","free-surface deformation","recoil/keyhole dynamics","evaporation","radiative/convective feedback in production solve"]}, "calibration":{"eta":cal["eta"],"root_residual_um":cal["root_residual_um"],"dL_deta_bracket_um":cal["dL_deta_bracket_um"],"eta_expanded_sensitivity_from_B_U":cal["eta_expanded_sensitivity_from_B_U"],"sensitivity_note":cal["sensitivity_note"],"objective_points":[{k:r[k] for k in ("eta","L_um","residual_um","data_role","directory")} for r in cal["objective_points"]],"data_roles":cal["data_roles"],"observations_read_by_calibration":cal["observations_read_by_calibration"],"provenance_audit_status":readj('verification/fipy-application-calibration-r13/provenance-audit.json')["status"],"source":str(BASE/'report/application-research-results.json'),"limitation":"Five retained successful points show a local bracket and monotone sampled response; no proof of global unique root over eta in [0,1]. Propagated B U is sensitivity, not a calibrated posterior or complete prediction uncertainty."},"runs":runs,"comparison_rows":comparisons,"comparison_statistic_boundary":"Signed difference divided by separately sourced experimental expanded U; not a z score, p-value, or combined experimental+numerical+calibration uncertainty En.","experimental_roles":{"length":"Lane AMMT-20 us thermography class means; A/B/C frame counts 19/10/7 (not independent specimens)","width_depth":"Current exact NIST Section 2 Table 2 targets from AMMT-100 us traces; A/B/C 3/3/4 independent tracks. Lane Table 4 class W/D combines AMMT-100 and AMMT-20 us measurements and reports integer means.","uncertainty":"Lane Tables 5-7 U=2*uc, components in quadrature without correlations; separate from NIST class SD and from standard uncertainty of mean.","joint_operator_limit":"Length and W/D are class comparisons, not same-track simultaneous 3D measurements."},"width_depth_primary_provenance":readj('validation/ammt-width-depth-provenance.json'),"research_case_metrics":current["research_case_metrics"],"B_C_descriptive_trends":derived_trends,"factorial":{"source":str(BASE/'report/constitutive-factorial-results.json'),"scope":factor["scope"],"eta":factor["eta"],"coding":"first letter k, second cp; L linear extrapolation, H hold last value at own endpoint", "rows":factor_rows,"effects":effects,"effect_formulas":{"k_conditional_at_cp_L":"Q_HL-Q_LL","cp_conditional_at_k_L":"Q_LH-Q_LL","interaction":"Q_HH-Q_HL-Q_LH+Q_LL","joint":"Q_HH-Q_LL","k_average_main":"((Q_HL-Q_LL)+(Q_HH-Q_LH))/2","cp_average_main":"((Q_LH-Q_LL)+(Q_HH-Q_HL))/2"},"matched_temperature_properties":factor["matched_temperature_properties"],"limits":factor["limits"],"mechanism_claim_as_recorded":factor["mechanism_claim"]},"numerical_evidence":{"uncalibrated_eta020_matrix":matrix,"frozen_eta_neighborhood":neigh["rows"],"current_claim_status_as_recorded":app["claim_status"],"constant_property_analytic_geometry":readj('verification/native61-constant-gaussian-frame-r1/qoi-analytic-report.json'),"steady_transient_retained_comparison":readj('verification/native61-steady-transient-retained-r1/report.json'),"factory_history_repair":readj('collaboration/native61-fipy-v3-factory-review-r2.json'),"formal_adequacy_boundary":"Observed sensitivity, not a certified absolute discretization bound. Calibrated B/C axial refinements and A/B domain extensions do not establish full 3D asymptotic convergence or branch-specific submicrometre accuracy."},"artifact_check_result":"All six source snapshot/dependency bindings matched; retained arrays finite and bounded liquid fraction; source power and centerline length independently reproduced from saved arrays; comparison ratios and factorial effect algebra checked. No new physical validation granted."}
(OUT/'verified-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
print(json.dumps({"unique_runs":len(runs),"all_source_bindings_match":all(v['matches'] for r in runs for v in r['source_binding_audit']),"run_extrema_and_gates":[{k:r[k] for k in ('run','temperature_min_C','surface_peak_C','iterations','nonlinear_equation_L1_relative','balance_relative','final_correction_T_C')} for r in runs],"comparison_inside_U_count_including_B_fit":sum(r['inside_source_expanded_U_scale'] for r in comparisons),"B_C_trends":derived_trends,"output":str(OUT/'verified-data.json')},ensure_ascii=False,indent=2))
