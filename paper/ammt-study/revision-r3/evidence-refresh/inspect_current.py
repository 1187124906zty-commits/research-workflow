from pathlib import Path
import json,csv,numpy as np

OUT=Path(__file__).resolve().parent
PAPER=OUT.parent.parent
BASE=Path('C:/Users/Administrator/Documents/ChatGPT/电脑答疑/simulation-agent-mvp/research/reproduction-case/nist-amb2018-02')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
v=read(PAPER/'evidence/verified-data.json');a=read(PAPER/'revision-r2/methods-results/computed-audit.json')
c=read(BASE/'report/current-results.json');f=read(BASE/'report/constitutive-factorial-results.json')
def compare_common(old,new,p=''):
    changed=[]
    if isinstance(old,dict) and isinstance(new,dict):
        for k in old.keys()&new.keys():changed+=compare_common(old[k],new[k],p+'/'+k)
    elif isinstance(old,list) and isinstance(new,list):
        if len(old)!=len(new):changed.append({'locator':p,'old_count':len(old),'current_count':len(new)})
        for i,(x,y) in enumerate(zip(old,new)):changed+=compare_common(x,y,p+'/'+str(i))
    elif old!=new:changed.append({'locator':p,'old':old,'current':new})
    return changed

comparisons=list(csv.DictReader((BASE/'report/experimental-comparison.csv').open(encoding='utf-8-sig')))
for row in comparisons:
    for k in row:
        if k not in ['case','observable','role']:row[k]=float(row[k])
oldrows={x['branch']:x for x in v['factorial']['rows']}
oldeffects={x['quantity']:{k:z for k,z in x.items() if k!='quantity'} for x in v['factorial']['effects']}
checks={
 'dashboard_comparison_common_values_vs_verified':compare_common(v['comparison_rows'],c['comparison_rows']),
 'primary_csv_common_values_vs_verified':compare_common(v['comparison_rows'],comparisons),
 'dashboard_research_case_metrics_vs_verified':compare_common(v['research_case_metrics'],c['research_case_metrics']),
 'factorial_metrics_vs_verified':{b:compare_common(oldrows[b],f['rows'][b]['metrics']) for b in oldrows},
 'factorial_effects_vs_verified':compare_common(oldeffects,f['effects']),
 'matched_temperature_properties_vs_verified':compare_common(v['factorial']['matched_temperature_properties'],f['matched_temperature_properties']),
 'existing_claim_status_vs_verified':compare_common(v['numerical_evidence']['current_claim_status_as_recorded'],c['claim_status']),
}
for rr in v['runs']:
    j=read(rr['result_source']); m=read(Path(rr['directory'])/'manifest.json')
    fields=['surface_peak_C','temperature_min_C','iterations','duration_s','nonlinear_equation_L1_relative','balance_relative','final_correction_T_C']
    checks['run_'+rr['run']]=compare_common({k:rr[k] for k in fields},{k:j[k] for k in fields})
    # Primary geometry already cross checked against CSV and factorial; read current result objects independently.
    checks['run_'+rr['run']]+=compare_common({'L':rr['L_um'],'W':rr['W_um'],'D':rr['D_um']},{'L':j['L']['length_m']*1e6,'W':j['passage_geometry']['W_m']*1e6,'D':j['passage_geometry']['D_m']*1e6})

animation=read(BASE/'report/showcase-animation.json')
h=list(csv.DictReader((BASE/'report/showcase-material-history.csv').open(encoding='utf-8')))
tt=np.array([float(x['t_from_laser_passage_ms']) for x in h]);xx=np.array([float(x['xi_m']) for x in h]);temp=np.array([float(x['surface_temperature_C']) for x in h]);frac=np.array([float(x['surface_liquid_fraction']) for x in h])
with np.load(BASE/animation['source_field']) as ar:
    xi=ar['x_m'];center=ar['surface_y0_T_C'];surf=ar['surface_T_C']
    history_err=float(np.max(np.abs(np.interp(xx,xi,center)-temp)))
    centerpeak=float(center.max());positivepeak=float(surf.max())
crossings={}
for threshold in [1290,1350]:
    found=[]
    for i in range(len(tt)-1):
        if (temp[i]-threshold)*(temp[i+1]-threshold)<0:
            found.append(float(tt[i]+(threshold-temp[i])/(temp[i+1]-temp[i])*(tt[i+1]-tt[i])))
    crossings[str(threshold)]=found
rear_time=(crossings['1290'][-1]-crossings['1350'][-1])*1000
current={
 'scope':'Read-only current reports/README/retained result and surface arrays. No solver imported or PDE run. No historical hashes changed.',
 'source_root':str(BASE),'historical_inputs':[str(PAPER/'evidence/verified-data.json'),str(PAPER/'revision-r2/methods-results/computed-audit.json')],
 'comparison_checks':checks,'eta':f['eta'],'production_unique_runs':len(v['runs']),
 'model':v['physical_model']['moving_equation'],'source':v['physical_model']['laser'],
 'current_geometry':comparisons,'current_time_metrics':c['research_case_metrics'],
 'current_factorial':{b:{k:z for k,z in f['rows'][b]['metrics'].items() if k in ['L_um','W_um','D_um','surface_peak_C','Ts_rear_um','Tl_rear_um','rear_phase_span_um','rear_phase_passage_us','hot_rear_net_outward_diffusive_W','mushy_x_face_Pe_median']} for b in f['rows']},
 'current_effects':{k:f['effects'][k] for k in ['L_um','W_um','D_um','rear_phase_span_um']},
 'current_claim_status':c['claim_status'],'claim_status_added_keys':sorted(c['claim_status'].keys()-v['numerical_evidence']['current_claim_status_as_recorded'].keys()),
 'new_postprocessing':{'source':str(BASE/'report/showcase-animation.json'),'mode':animation['mode'],'new_PDE_solve':animation['new_PDE_solve'],'physical_validation_promoted':animation['physical_validation_promoted'],'mapping':animation['mapping'],'frame_count':animation['frame_count'],'time_range_ms':animation['time_range_ms'],'history_rows':len(h),'max_xi_mapping_error_m':float(np.max(np.abs(xx+0.8*tt*1e-3))),'max_history_vs_saved_centerline_error_C':history_err,'max_phase_formula_error':float(np.max(np.abs(frac-np.clip((temp-1290)/60,0,1)))),'fixed_material_history_peak_C':float(temp.max()),'saved_y0_centerline_peak_C':centerpeak,'retained_positive_y_surface_peak_C':positivepeak,'difference_centerline_vs_reported_peak_C':centerpeak-positivepeak,'sampled_rear_crossing_times_ms':crossings,'sampled_rear_interval_us':rear_time,'difference_vs_primary_rear_interval_us':rear_time-c['research_case_metrics'][1]['rear_phase_passage_us'],'interpretation':'Same retained solution, distinct symmetry-centerline versus positive-y surface peak operators; dense history interpolation adds negligible crossing interpolation difference. New dependent visual evidence, not new transient solve or thermal validation.'},
 'history_limit':'Local simulation-agent-mvp master has no commits and case is untracked. No git historical diff available. Comparison establishes current content agreement to frozen verified records, not exact chronology of every dashboard prose change.',
 'remaining_boundaries':['No matched independent thermal validation.','Selected-state hot region and gradients vary; flux increase refutes only naive lower-k/lower-integrated-flux shortcut, not all bulk-transport explanations.','No branch-specific 3D error bound or precision upgrade.','A/C retrospective nonblind and separate imaging/metallographic data classes remain.'],
 'disposition':'Returned for coordinator interpretation and binding. No self-issued PASS or scientific promotion.'}
(OUT/'verified-current.json').write_text(json.dumps(current,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'changed_comparisons':checks,'new_postprocessing':current['new_postprocessing']},ensure_ascii=True))
