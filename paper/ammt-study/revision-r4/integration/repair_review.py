"""Apply located reviewer repairs; scientific execution remains unchanged."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT.parent
path = PAPER / 'manuscript.tex'
source = path.read_text(encoding='utf-8')
changes = [
    ('Conductivity and sensible heat-capacity continuations above their tabulated ranges are varied independently while the calibrated source and phase law remain fixed.',
     'Linear continuation and holding at the last tabulated value are compared independently for conductivity and sensible heat capacity, with the calibrated source and phase law retained.'),
    ('A separate transient-conduction study connected geometry verification, solidification-condition calculations and an experimental grain-structure comparison for AlSi10Mg laser and IN718 electron-beam cases~\\cite{Plotkowski2017Rapid}.',
     'A separate transient-conduction study assessed geometric and solidification-condition calculations for AlSi10Mg laser and IN718 electron-beam cases, and compared predicted grain morphology with experiments for the IN718 case~\\cite{Plotkowski2017Rapid}.'),
    ('The relation follows from passage through the same quasi-steady field and defines a derived centerline history.',
     'For each condition, the relation follows from passage through its calculated quasi-steady field and defines a derived centerline history.'),
    ('would establish their physical correspondence.', 'would test their physical correspondence.'),
    ('The solved problem is steady; retained warm fields provide nonlinear initial guesses rather than a transient thermal initial condition.',
     'The solved problem is steady; retained warm fields provide nonlinear initial guesses.'),
    ('This recovers conductive flux while conserving enthalpy; $U$ is a scaled enthalpy, not temperature.',
     'This coefficient recovers conductive flux in the conservative equation for scaled enthalpy $U$. Coordinate enthalpy transport uses an exponentially fitted finite-volume convection flux. Material coefficients and the diffusion--transport stencil are updated with each nonlinear iterate; Anderson acceleration solves the fixed-point residual and preconditioned GMRES solves the inner linear system. Software versions and iterative controls are given in the accompanying numerical reproduction notes.'),
]
records=[]
for old,new in changes:
    if source.count(old) != 1:
        raise ValueError((old,source.count(old)))
    source=source.replace(old,new)
    records.append({'before':old,'after':new})
path.write_text(source,encoding='utf-8')
(ROOT/'integration/review-repairs.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print('Applied',len(records),'located scientific/editorial repairs.')
