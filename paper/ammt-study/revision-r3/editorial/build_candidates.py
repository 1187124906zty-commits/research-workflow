from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = (ROOT.parent / 'manuscript-input.tex').read_text(encoding='utf-8')
methods_source = source.split('\\section{Materials and methods}', 1)[1].split('\\section{Results}', 1)[0]
parts = methods_source.split('\\subsection{')[1:]
parts = {p.split('}', 1)[0]: p.split('}', 1)[1].strip() for p in parts}

design = parts['Study design, experimental referent and data roles']
design = design.replace(design.split('\n\n', 1)[0], r'''The study examines whether matching one melt-pool length also constrains fusion shape and the rear thermal interval in a conduction model. One source factor is fitted to condition B length. Width and depth are excluded from the fit, and conditions A and C retain the fitted factor. A four-corner comparison at B then changes the high-temperature conductivity and sensible-storage continuations independently. The rear solidus and liquidus positions resolve whether these changes displace the thermal tail or widen the phase interval; their separation and scan speed define a material passage time.''')
design = design.replace('The referent is constant-speed laser scanning', 'The experimental comparison uses constant-speed laser scanning')
design = design.replace('Current width and depth means are taken', 'Width and depth means are taken')
design = design.replace('The B length is the sole scalar calibration target. B width and depth are diagnostics after calibration, and A/C are retrospective, nonblind comparisons with $\\eta$ frozen. All public targets were available during development.', 'The comparisons are retrospective and nonblind: all public targets were available during development, although only B length enters the calibration objective.')

model = parts['Conservative enthalpy model in the laser frame']
model = model.replace('The laboratory-frame conduction balance is', 'The laboratory-frame conduction balance uses conservative enthalpy~\\cite{vanelsen2007}:')
model = model.replace('The equilibrium phase fraction is', 'The adopted linear liquid-fraction closure over the equilibrium melting interval is~\\cite{dynamic2024}')
model = model.replace('The Gaussian surface input at $z=0$ is', 'With the circular Gaussian $D_{4\\sigma}$ convention~\\cite{dynamic2024}, the surface input at $z=0$ is')
model = model.replace('Specific heat and conductivity are linearly interpolated between the actual input knots in Table~\\ref{tab:properties} in the reproducibility appendix.', 'Specific heat and conductivity are linearly interpolated between the input knots in Table~\\ref{tab:properties}.')
model = model.replace('These are the endpoints loaded by the executed material routine. ', '')
model = model.replace('Figure~\\ref{fig:properties} separates tabulated interpolation from the high-temperature assumptions: both endpoints lie below the adopted solidus.', 'Both property tables end below the adopted solidus, so the melting-range solution requires a high-temperature continuation (Fig.~\\ref{fig:properties}).')
contrast_source = parts['Calibration and high-temperature continuation contrast']
closure = contrast_source.split('\n\n')[1]
# The definition of the material branches belongs with the material model.
closure = closure.replace('At fixed B, two binary factors replace', 'Two binary factors replace')
closure = closure.replace('The LL solution is the B baseline; HH is a retained joint-closure comparison; HL and LH supply the two mixed corners. No corner is recalibrated. Across A/B/C and these four corners, sharing B=LL gives six unique production runs.', 'The baseline uses linear continuation for both properties (LL); HL and LH change one property, and HH changes both. The calibration and fixed-source contrasts are defined below.')
insert_at = 'For a locally quasi-steady translating field'
model = model.replace(insert_at, closure + '\n\n' + insert_at)
model = model.replace('Consequently, coordinate transport is not evidence of liquid flow.', '')
model = model.replace('use the knots loaded by the executed material routine', 'use the input knots listed in Table~\\ref{tab:properties}')
model = model.replace('Rectangle-wise error-function integration supplies each top-face power.', 'The Gaussian is integrated over each top face using error functions.')

observers = parts['Geometry and passage-history operators']
observers = observers.replace('The geometric figure labels $L_s$, $W_f$ and $D_f$ correspond to the text\'s $L$, $W$ and $D$, respectively: $L_s$ is the surface length proxy, while $W_f$ and $D_f$ are fusion-envelope extents.', 'Figures label the surface length proxy $L_s$ and fusion-envelope extents $W_f$ and $D_f$; these correspond to $L$, $W$ and $D$ in the text.')
observers = observers.replace('These are derived from one steady temperature solution. The passage time is a coordinate transformation, not a second independently predicted observable.', 'These quantities describe stationary material passing through the same quasi-steady field; they are derived quantities rather than independent thermal observations.')

calibration = contrast_source.split('\n\n')[0]
calibration = calibration.replace('The baseline continues the final tabulated slope of each property above its endpoint. ', '')
calibration = calibration.replace('Calibration trials and the local sensitivity conversion are reported in the appendix.', 'The appendix gives calibration trials and the local sensitivity conversion.')
calibration += '\n\n' + r'''For the four B corners, power, speed, beam, density, phase thresholds, latent heat, mesh and observation operators remain fixed, and no corner is recalibrated. The first letter denotes conductivity and the second sensible specific heat. Sharing B=LL between the operating-condition and continuation comparisons gives six production solutions.'''
calibration += '\n\n' + contrast_source.split('For any output $Q$', 1)[1]
calibration = calibration.replace('\n\n\n', '\n\n')
calibration = calibration.replace('calibration\n', 'calibration\n')
calibration = calibration[:calibration.find('For any output')] if 'For any output' in calibration else calibration
# Restore the lead-in removed by the split.
calibration = calibration.replace('\n\n, define the baseline', '\n\nFor any output $Q$, define the baseline')

mesh = r'''The moving-frame balance is solved by a conservative finite-volume method on a graded orthogonal half-domain: $\xi\in[-1,0.35]$~mm, $y\in[0,0.36]$~mm and $z\in[-0.30,0]$~mm. The 902664-cell mesh has near-source widths of $4\times3\times1$~\um\ within $\xi\in[-0.48,0.16]$~mm, $y\in[0,0.12]$~mm and $z\in[-0.06,0]$~mm. Outer cell widths increase by a factor of 1.22 up to 25~\um. The solution is steady; warm fields supply nonlinear initial guesses. The scaled enthalpy discretization, face coefficients, solver controls and software versions are given in the appendix. Convergence is checked using both the sum of absolute cell residuals and the signed global energy balance, followed by a full frozen-coefficient correction.'''

adequacy = r'''A separate constant-property moving-Gaussian problem checks source integration, frame transport and geometric extraction against a semi-infinite analytical reference~\cite{oberkampf2002}. Its reference $L/W/D$ is $407.535/153.293/34.836$~\um; finite-volume differences are +0.139\%, +0.190\% and $-0.499$\%, respectively. This simpler comparison does not establish nonlinear phase-change accuracy.

At the calibrated $\eta$, reducing the near-source axial spacing from 4 to 2~\um\ changes B length, width and depth by +0.361, $-0.009$ and +0.041~\um, and C by +0.199, $-0.029$ and +0.045~\um. A/B domain enlargement changes these quantities by less than $3\times10^{-6}$~\um. These measured sensitivities support comparison with the larger geometric responses, but do not give a full three-dimensional error bound for each continuation branch. Submicrometre interactions are therefore reported descriptively. An earlier transient B comparison at a different calibration stage provides only approximate local steady consistency. Fixed-field blackbody estimates put B-corner top losses at 0.099--0.180\% of absorbed power; feedback from these losses is not solved.

The six production solutions have finite temperatures, bounded phase fractions, nontruncated extracted geometry and the prescribed integrated source power. Normalized absolute residuals are $6.90\times10^{-8}$--$1.31\times10^{-7}$, signed global balance magnitudes are below $6.1\times10^{-11}$, and full-solve temperature corrections are below $2.7\times10^{-5}$~$^\circ$C. The appendix records the acceptance thresholds and implementation controls.'''

methods = '\\section{Materials and methods}\n'
for heading, text in [
    ('Benchmark conditions and comparison design', design),
    ('Moving-frame enthalpy model and material continuations', model),
    ('Melt-pool geometry and material passage', observers),
    ('Calibration, constitutive contrasts and numerical adequacy', calibration + '\n\n' + mesh + '\n\n' + adequacy),
]:
    methods += '\n\\subsection{' + heading + '}\n' + text + '\n'
(ROOT / 'methods.tex').write_text(methods, encoding='utf-8')

implementation = parts['Finite-volume implementation and nonlinear solution']
implementation = implementation.split('\n\n', 1)[1]
implementation = implementation.replace('Detailed acceleration and linear iteration controls are provided in the reproducibility appendix. ', '')
implementation = implementation.replace('Final acceptance uses the assembled nonlinear balance and the full-solve correction described below. ', '')
appendix = r'''% Proposed additions for insertion in the existing reproducibility appendix.
% Keep the existing property table, constant-property integral and calibration table.
% Replace the current short solver-controls paragraph with the text below.
\subsection{Enthalpy discretization and nonlinear solution}
The half-domain mesh has $199\times56\times81$ cells. ''' + implementation + '\n\n'
old_control = source.split('The Anderson controls are', 1)[1].split('\\subsection{Separate constant-property', 1)[0]
appendix += 'The Anderson controls are' + old_control
appendix += r'''
\subsection{Implementation and retained numerical records}
Source-power integration, threshold crossings, primary passage geometry and finite-contrast algebra were independently reproduced from the retained temperature arrays and observer code. The original numerical case retains solver snapshots, input manifests and calibration history for the six solutions. The separate verification recipes are \path{verify_constant_gaussian_frame_native61.py} and \path{qoi_constant_gaussian_reference_native61.py}; the associated reports use the identifier \texttt{native61-constant-gaussian-frame-r1}. These locators identify the numerical records and do not constitute physical validation.
'''
(ROOT / 'appendix-additions.tex').write_text(appendix, encoding='utf-8')

# Final allocation follows the root's more compact main-text contract.
methods = (ROOT / 'methods.tex').read_text(encoding='utf-8')
methods = methods.replace('$\\eta=0.2890548519$', '$\\eta\\approx0.28905$')
methods = methods.replace('The Gaussian is integrated over each top face using error functions. Its full-plane integral is $\\eta P$ and the transverse half-domain receives $\\eta P/2$. The finite-volume implementation deposits the integrated boundary input into top control volumes.', 'Its full-plane integral is $\\eta P$; the appendix gives the discrete source integration.')

recovery = observers.split('Surface recovery satisfies', 1)[1].split('Fusion-zone width and depth', 1)[0]
methods = methods.replace('Surface recovery satisfies' + recovery, 'Surface and symmetry-plane recovery precede threshold extraction; the appendix gives their numerical definitions.\n\n')
methods = methods.replace('The 0.5~\\um\\ observation pitch samples interpolated geometry; it does not represent the resolution of the heat-field mesh.', 'The observation pitch samples interpolated geometry and does not define the heat-field resolution.')

calibration_old = methods.split('A safeguarded secant solves', 1)[1].split('\n\nFor the four B corners', 1)[0]
methods = methods.replace('A safeguarded secant solves' + calibration_old, r'''Fitting $L_B(\eta)=359$~\um{} gives $\eta\approx0.28905$, with a signed length residual of +0.158~\um. Conditions A and C retain this value, beam, phase law and property continuations. The appendix gives the scalar calibration algorithm, trial values and local sensitivity.''')

diagnostics = contrast_source.split('The retained face transport diagnostic is', 1)[1]
old_diagnostics = methods.split('The retained face transport diagnostic is', 1)[1].split('\n\nThe moving-frame balance', 1)[0]
methods = methods.replace('The retained face transport diagnostic is' + old_diagnostics, r'''An axial-face P\'eclet diagnostic compares coordinate enthalpy transport with diffusion in the phase interval. A discrete rear hot-region budget measures net outward diffusive power. Both use temperature-selected regions that can change between branches, so they complement matched-coordinate thresholds rather than supply a fixed-region causal contrast. Their definitions are given in the appendix.''')

methods = methods.replace(mesh, r'''The conservative finite-volume solution uses near-source cell widths of $4\times3\times1$~\um. The graded-domain geometry and enthalpy discretization are specified in the appendix. Convergence is checked using both the sum of absolute cell residuals and the signed global energy balance, followed by a full frozen-coefficient correction.''')
record = adequacy.split('The six production solutions have', 1)[1]
methods = methods.replace('The six production solutions have' + record, 'All six solutions satisfy the stated energy-balance and nonlinear-correction criteria and give bounded phase fractions and nontruncated extracted geometry. The appendix reports the acceptance thresholds and final residuals.')
(ROOT / 'methods.tex').write_text(methods, encoding='utf-8')

full_mesh = parts['Finite-volume implementation and nonlinear solution'].split('\n\n', 1)[0]
appendix = r'''% Proposed scientific appendix additions. Keep the existing property table,
% constant-property verification integral and calibration/sensitivity table.
\subsection{Spatial discretization and observation recovery}
''' + full_mesh + '\n\n' + r'''The Gaussian source is integrated rectangle-wise using error functions to supply each top-face power, which is deposited in the adjacent top control volume. Its full-plane integral is $\eta P$ and the transverse half-domain receives $\eta P/2$.

Surface recovery satisfies''' + recovery + r'''The observation pitch is 0.5~\um; it samples the interpolated geometry rather than changing the heat-field resolution.

\subsection{Scaled enthalpy diffusion and diagnostic definitions}
The scaled unknown is $U=H/C_0$, with $C_0=\rho(402~\si{\joule\per\kilogram\per\kelvin})=3.39288\times10^6$~\si{\joule\per\cubic\metre\per\kelvin}. On an internal face,
\begin{equation}
 D_f=\frac{k_f}{C_0}\frac{\Delta T}{\Delta U},
 \label{eq:face}
\end{equation}
where $k_f$ is the harmonic face conductivity and $D_f$ has units of m$^2$\,s$^{-1}$. For $|\Delta U|\leq10^{-8}$~K, the derivative limit is $\Delta T/\Delta U=C_0/[\rho(c_p+\mathcal L f')]$ at the first adjacent cell. This recovers conductive flux while conserving enthalpy; $U$ is a scaled enthalpy, not temperature.

The retained face transport diagnostic is''' + diagnostics + r'''

\subsection{Scalar calibration and solution acceptance}
A safeguarded secant solves''' + calibration_old + '\n\n' + r'''Nonlinear acceptance requires the sum of absolute assembled cell residuals, normalized by absorbed half-power, to be below $2\times10^{-5}$, the signed global balance magnitude below the same scale, and a further frozen-coefficient solve to change temperature by less than 0.002~$^\circ$C. Local residual and global balance are retained separately because opposing local errors can cancel in a global sum.

The six production solutions have''' + record + '\n'
appendix = appendix.replace('The appendix records the acceptance thresholds and implementation controls.', '')
appendix = appendix.replace('The appendix gives calibration trials and the local sensitivity conversion.', 'The existing calibration record gives trial values and the local sensitivity conversion.')
(ROOT / 'appendix-additions.tex').write_text(appendix, encoding='utf-8')

notes = '''# Numerical reproduction notes

These implementation details are retained from the frozen manuscript. This editorial task did not perform a new numerical reproduction or add physical evidence. The enthalpy face coefficient, surface recovery and diagnostic definitions are in appendix-additions.tex; they are not duplicated here.

## Executed environment and methods

The production record gives Python 3.13.5, NumPy 2.5.3, SciPy 1.18.1, FiPy 4.0.3 and PyAMG 5.3.0, with one BLAS thread. FiPy assembles diffusion and exponential coordinate-convection terms. SciPy Anderson acceleration solves the nonlinear fixed-point residual. The inner linear system uses GMRES with a PyAMG Ruge–Stuben classical-multigrid preconditioner. The corresponding scholarly software citations are the existing fipy2009 and scipy2020 bibliography entries.

| Control | Executed value |
|---|---|
| Anderson history depth | M = 8 |
| Anderson initial scale | alpha = 0.2 |
| Anderson regularization | w0 = 0.01 |
| Fixed-point residual tolerance | 2 × 10⁻⁴ K in scaled enthalpy U |
| Line search | Armijo |
| GMRES tolerance | 2 × 10⁻⁹ |
| GMRES restart and iteration cap | restart 80; cap 800 inner iterations |
| Multigrid strength threshold | 0.25 |
| Multigrid smoother | symmetric Gauss–Seidel |
| Multigrid cycle | V cycle |
| Maximum levels and coarse size | 20 levels; coarse size 100 |

These controls come from the production manifests. Alternative methods present in the solver source were not used for the six production solutions. The scientific appendix records the assembled-residual, global-balance and frozen-coefficient-correction acceptance criteria separately from the iterative solver tolerance.

## Coefficient-update behavior

The diffusion and exponential-convection objects are recreated after each coefficient update. Implementation checks found that reusing the objects could retain cached initial stencil weights. The production implementation recreates them to ensure the stencil follows the current coefficients. This is a software correction, not a finding about the physical thermal model.

## Retained numerical records

The original case retains solver snapshots, input manifests, temperature arrays, calibration history and primary-observer code. Source-power integration, threshold crossings, passage geometry and finite-contrast algebra were independently reproduced in the prior numerical audit. The constant-property verification recipes are `verify_constant_gaussian_frame_native61.py` and `qoi_constant_gaussian_reference_native61.py`; report identifier `native61-constant-gaussian-frame-r1`. Keep those recipes and their existing original-case links in the package documentation. They identify numerical records and do not constitute physical validation.
'''
(ROOT / 'reproduction-notes.md').write_text(notes, encoding='utf-8')
