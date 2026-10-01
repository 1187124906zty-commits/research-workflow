"""Apply coordinator-adopted, source-bound R2 interface repairs in place."""
from pathlib import Path
import re

PAPER = Path(__file__).resolve().parents[1]
source = PAPER / 'manuscript.tex'
text = source.read_text(encoding='utf-8')

def replace_once(old, new):
    global text
    if new in text:
        return
    if text.count(old) != 1:
        raise ValueError('Inspect the current revision before applying this edit: ' + old[:90])
    text = text.replace(old, new, 1)

replace_once('computationally demanding~\\cite{king2015}.',
             'computationally demanding~\\cite{king2015}. Recent finite-element reviews likewise distinguish thermal, mechanical and microstructural modeling across scales, with different material-data and coupling requirements~\\cite{review2024}.')
replace_once('This hierarchy permits useful simplification,',
             r'Semi-analytical transient conduction has also been used to estimate solidification conditions and relate scan strategies to grain structure in studied AlSi10Mg laser and IN718 electron-beam cases~\cite{Plotkowski2017Rapid}. This hierarchy permits useful simplification,')
replace_once('For IN625, Lane et al. distinguished',
             r'Simonds et al. compared time-resolved optical coupling with calorimetry during 10~ms stationary 316L welds and found that mass loss affected their energy accounting~\cite{simonds2018}. Scanning calorimetry and scaling across Ti6Al4V, IN625 and 316L further related coupling and penetration to power, speed and beam size, with marked changes across the conduction--keyhole transition~\cite{ye2019}. Those studies provide measurement routes and condition-dependent relationships, rather than an independently known coupling factor for the present tracks. For IN625, Lane et al. distinguished')
replace_once(r'\subsection{What geometric calibration constrains}',
             r'\subsection{Geometric agreement as a conditional constraint}')
replace_once('The discrepancy therefore concerns energy distribution as well as its overall scale.',
             'The residual concerns the relative transverse and depth response and is compatible with differences in energy deposition, transport closure or observation mapping.')
replace_once(r"Conductivity holding reduces local diffusion relative to coordinate transport in the discretized mushy region, consistent with the retained axial face P\'eclet median increasing from 4.44 to 5.77.",
             r"The retained axial-face P\'eclet median increases from 4.44 to 5.77 under conductivity holding, consistent with a shift toward coordinate transport relative to diffusion in the selected discrete phase region.")
replace_once('The rear centerline phase spans are 48.30,',
             'On the present mesh, the rear centerline phase spans are 48.30,')
replace_once('The nearly equal B/C rear phase spans,',
             'The current-mesh B/C rear phase spans,')

additions = (PAPER / 'revision-r2/exchange/proposed-additions.tex').read_text(encoding='utf-8')
paragraphs = [p.strip() for p in re.split(r'\n\s*\n', additions)
              if 'The trajectory represented' in p or 'High-temperature property measurements provide' in p]
paragraphs = ['\n'.join(line for line in p.splitlines() if not line.startswith('%')) for p in paragraphs]
replace_once('The transformed interval is informative about this quasi-steady model but does not determine segregation, grain morphology or the alloy\'s actual nonequilibrium freezing path.',
             'The transformed interval is informative about this quasi-steady model but does not determine segregation, grain morphology or the alloy\'s actual nonequilibrium freezing path.\n\n' + paragraphs[0])
replace_once('Neither is measured liquid behavior, and the equilibrium phase law remains assumed.',
             'Neither is measured liquid behavior, and the equilibrium phase law remains assumed.\n\n' + paragraphs[1] + '\n\n')
replace_once('The useful next comparison is one that constrains source/measurement mapping and tests an excluded thermal or shape observable, rather than selecting a mechanism from the residual alone.',
             r'''The useful next comparison is one that constrains source/measurement mapping and tests an excluded thermal or shape observable, rather than selecting a mechanism from the residual alone.

Benchmark design can make these distinctions experimentally actionable. The AM Bench 2022 IN718 track and pad measurements combine controlled power, speed and spot-size changes with thermography, cross-sectional geometry and stated uncertainty budgets~\cite{weaver2024}. Their reported pad heat buildup also shows why a single-track comparison cannot establish multi-track transfer. For the present case, a prospective test would retain one defined source and observation mapping, reserve excluded tracks or thermal profiles before fitting, and evaluate geometry together with a temperature trajectory. Such a design would test the thermal meaning of calibration rather than add another dependent quantity extracted from the same computed field.''')
replace_once('The experimental comparisons are retrospective and nonblind,',
             r'''The quasi-steady straight-track setting also limits transfer to scan turnarounds and powder layers. Martin et al. linked scan-velocity transients to vapor-depression collapse and pore formation using X-ray imaging and multiphysics calculations~\cite{martin2019}; those events are absent from the steady solution here. Powder introduces additional interactions: Matthews et al. related denudation to vapor flux and gas-driven entrainment~\cite{matthews2016}, while recent gas--melt--particle modeling identifies entrained-particle momentum as a possible perturbation of the thermal tail~\cite{gasliquid2025}. These studies define mechanisms and operating conditions that must be added and assessed before extending the present bare-plate diagnosis to powder-bed defects.

The experimental comparisons are retrospective and nonblind,''')
source.write_text(text, encoding='utf-8')
keys = sorted(set(k.strip() for group in re.findall(r'\\cite(?:[a-zA-Z]*)?(?:\[[^\]]*\])*\{([^}]+)\}',text) for k in group.split(',')))
print(f'Updated the same open manuscript; {len(keys)} actively cited identities. Build and whole-paper review remain required.')
