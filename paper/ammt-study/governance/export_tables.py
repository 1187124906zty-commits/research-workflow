"""Export exact retained result tables and deterministic checks; no PDE execution."""
from pathlib import Path
import csv
import json
import shutil
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
DATA.mkdir(exist_ok=True)
SOURCE = Path('C:/Users/Administrator/Documents/ChatGPT/电脑答疑/simulation-agent-mvp/research/reproduction-case/nist-amb2018-02')
for name in ('experimental-comparison.csv','constitutive-factorial-metrics.csv',
             'constitutive-factorial-effects.csv','constitutive-factorial-rear-profiles.csv'):
    shutil.copy2(SOURCE/'report'/name, DATA/name)
shutil.copy2(SOURCE/'material-properties.csv', DATA/'material-properties.csv')
d = json.loads((ROOT/'evidence/verified-data.json').read_text(encoding='utf-8'))
for key in ('research_case_metrics','B_C_descriptive_trends','calibration','numerical_evidence'):
    (DATA/f'{key}.json').write_text(json.dumps(d[key],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
factorial = d['factorial']
summary = {k:factorial[k] for k in ('coding','effect_formulas','effects','matched_temperature_properties','limits')}
(DATA/'factorial-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Exported existing tables and model definitions; no new solver results.')
