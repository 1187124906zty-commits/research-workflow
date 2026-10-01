"""Render unchanged retained values with the review-corrected phase/time labels."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
metrics = json.loads((ROOT/'data/research_case_metrics.json').read_text(encoding='utf-8'))
contrast = json.loads((ROOT/'data/B_C_descriptive_trends.json').read_text(encoding='utf-8'))
colors = {'A':'#0072B2', 'B':'#D55E00', 'C':'#009E73'}
plt.rcParams.update({'font.family':'sans-serif', 'font.sans-serif':['Arial','DejaVu Sans'],
    'font.size':9.5, 'axes.labelsize':9.5, 'axes.titlesize':10,
    'xtick.labelsize':9, 'ytick.labelsize':9, 'axes.linewidth':0.75,
    'axes.spines.top':False, 'axes.spines.right':False,
    'svg.fonttype':'none', 'pdf.fonttype':42})
fig, axes = plt.subplots(2,2,figsize=(7.086614173,5.826771654))
fig.subplots_adjust(left=.105,right=.982,top=.925,bottom=.13,wspace=.44,hspace=.58)
axis = axes[0,0]
positions = np.arange(2)
for offset,color,label,field in ((-.17,'#222222','Experiment','experiment_C_vs_B_percent'),
                               (.17,'#0072B2','Present model','model_C_vs_B_percent')):
    values = [contrast[q][field] for q in ('W','D')]
    axis.bar(positions+offset,values,width=.30,color=color,label=label,zorder=3)
    for x,value in zip(positions+offset,values):
        axis.text(x,value-1.4,f'{value:.1f}',ha='center',va='top',fontsize=9)
axis.set(xticks=positions,xticklabels=[r'$\Delta W_f$',r'$\Delta D_f$'],ylim=(-38,1),
    ylabel='B→C relative change (%)',title='Fixed-power scanning-speed response')
axis.yaxis.set_major_locator(MultipleLocator(10))
axis = axes[0,1]
x=np.arange(3)
axis.plot(x,[r['experimental_mean_width_depth_ratio'] for r in metrics],'o',color='#222222',ms=5,label='Experiment')
axis.plot(x,[r['model_width_depth_ratio'] for r in metrics],'s',color='#0072B2',ms=5,label='Present model')
axis.set(xticks=x,xticklabels=list(colors),ylim=(3,6.5),xlabel='AMMT scan condition',
    ylabel=r'Fusion aspect ratio, $\chi=W_f/D_f$',title='Directional shape response')
axis.legend(loc='upper left',fontsize=8.5,frameon=False)
axis.grid(axis='y',color='#DEE2E6',lw=.45)
for column,key,ylabel,title,bound in (
    (0,'rear_Ts_Tl_span_um',r'Rear phase span, $\ell_m$ (µm)','Rear spatial phase interval',100),
    (1,'rear_phase_passage_us',r'Derived passage time, $\tau_m$ (µs)','Derived material passage time',150)):
    axis=axes[1,column]
    values=[r[key] for r in metrics]
    axis.bar(x,values,color=list(colors.values()),width=.48,zorder=3)
    for pos,value in zip(x,values):
        axis.text(pos,value+bound*.035,f'{value:.1f}',ha='center',va='bottom',fontsize=9)
    axis.set(xticks=x,xticklabels=list(colors),ylim=(0,bound),xlabel='AMMT scan condition',ylabel=ylabel,title=title)
for index,axis in enumerate(axes.ravel()):
    axis.set_axisbelow(True)
    axis.annotate(chr(97+index),xy=(0,1),xycoords='axes fraction',xytext=(0,14),
        textcoords='offset points',fontsize=12,fontweight='bold',annotation_clip=False)
fig.text(.52,.022,'B→C: P = 179.2 W; relative changes use reported means, with uncertainty not propagated.',ha='center',fontsize=8.5)
for ext in ('pdf','svg','png'):
    fig.savefig(ROOT/f'figures/ammt-research-condition-trends.{ext}',dpi=600,facecolor='white')
print('Rendered the same saved values; changed only phase/time labels. Original numerical case remains unchanged.')
