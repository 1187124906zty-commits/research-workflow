"""Generate section candidates from the read-only canonical manuscript.

Only this role's owned directory is written. Canonical labels and figure paths
are retained; the changes are proposals for coordinator/MAF peer disposition.
"""
from pathlib import Path
import difflib
import json

OUT = Path(__file__).resolve().parent
PAPER = OUT.parents[1]
source = (PAPER / "manuscript.tex").read_text(encoding="utf-8")
methods = source.split(r"\section{Materials and methods}", 1)[1].split(r"\section{Results}", 1)[0]
results = source.split(r"\section{Results}", 1)[1].split(r"\section{Discussion}", 1)[0]
methods = r"\section{Materials and methods}" + methods
results = r"\section{Results}" + results
old_methods, old_results = methods, results

def change(text, old, new):
    assert text.count(old) == 1, old[:100]
    return text.replace(old, new)

methods = change(methods,
 r"\subsection{Experimental referent and data roles}",
 r"\subsection{Study design, experimental referent and data roles}" + "\n" +
 "The study tests how one-target geometric agreement relates to fusion shape, constitutive sensitivity and derived material history. First, B length calibrates one effective source factor. Width and depth, which are excluded from that objective, then assess geometric discrepancy; A and C assess the fixed-parameter condition response. Next, a four-corner contrast at B separates conductivity and sensible-storage continuation while retaining power, speed, beam, density, phase thresholds, latent heat, mesh and observation operators. Decomposing the rear solidus and liquidus positions distinguishes translation of the thermal tail from widening of the phase interval. Finally, mapping the rear spatial interval through scan speed distinguishes geometric extent from material passage time.\n")
methods = change(methods,
 "Specific heat and conductivity are linearly interpolated between table knots.",
 "Specific heat and conductivity are linearly interpolated between the actual input knots in Table~\\ref{tab:properties}. The conductivity table contains 15 points and ends at 982~$^\\circ$C; the 12-point specific-heat table ends at 1093~$^\\circ$C. These are the endpoints loaded by the executed material routine.")
table = r"""
\begin{table}[htbp]
\centering
\caption{Property knots loaded by the executed material routine from the general IN625 bulletin~\cite{specialmetals625}. The two temperature columns describe different tables. Conductivity and sensible specific heat are interpolated independently.}
\label{tab:properties}
\begin{tabular}{rrrr}
\toprule
$T_k$ ($^\circ$C) & $k$ (W\,m$^{-1}$\,K$^{-1}$) & $T_c$ ($^\circ$C) & $c_p$ (J\,kg$^{-1}$\,K$^{-1}$)\\
\midrule
$-157$ & 7.2 & $-18$ & 402\\
$-129$ & 7.5 & 21 & 410\\
$-73$ & 8.4 & 93 & 427\\
$-18$ & 9.2 & 204 & 456\\
21 & 9.8 & 316 & 481\\
38 & 10.1 & 427 & 511\\
93 & 10.8 & 538 & 536\\
204 & 12.5 & 649 & 565\\
316 & 14.1 & 760 & 590\\
427 & 15.7 & 871 & 620\\
538 & 17.5 & 982 & 645\\
649 & 19.0 & 1093 & 670\\
760 & 20.8 & & \\
871 & 22.8 & & \\
982 & 25.2 & & \\
\bottomrule
\end{tabular}
\end{table}

"""
methods = change(methods,
 "Table~\\ref{tab:properties}.",
 "Table~\\ref{tab:properties} in the reproducibility appendix.")
methods = change(methods,
 "Rectangle-wise error-function integration supplies each top-face power.",
 r"With outward normal $\bm n$, the top condition is $-k\nabla T\cdot\bm n=-q$; the Gaussian supplies inward heat. Rectangle-wise error-function integration supplies each top-face power.")
methods = change(methods,
 "Outer widths increase by a factor of 1.22 up to 25~\\um.",
 "Outer widths increase by a factor of 1.22 up to 25~\\um. The half-domain mesh has $199\\times56\\times81$ cells. The solved problem is steady; retained warm fields provide nonlinear initial guesses rather than a transient thermal initial condition.")
methods = change(methods,
 "with harmonic face conductivity and the positive derivative limit for vanishing differences.",
 r"where $k_f$ is the harmonic face conductivity and $D_f$ has units of m$^2$\,s$^{-1}$. For $|\Delta U|\leq10^{-8}$~K, the implementation uses the positive derivative limit $\Delta T/\Delta U=C_0/[\rho(c_p+\mathcal L f')]$ at the first adjacent cell.")
methods = change(methods,
 "preconditioned by classical PyAMG.",
 "preconditioned by PyAMG Ruge--Stuben classical multigrid. Detailed acceleration and linear iteration controls are provided in the reproducibility appendix. Final acceptance uses the assembled nonlinear balance and the full-solve correction described below.")
methods = change(methods,
 "and the symmetry-plane value uses an even quadratic extension.",
 r"and the symmetry-plane value uses the even quadratic extension $T(0)=T(y_1)+[T(y_1)-T(y_2)]y_1^2/(y_2^2-y_1^2)$ from the first two positive-$y$ cell centers. The recovered surface temperatures and symmetry extension are applied before the threshold crossings are extracted.")
methods = change(methods,
 "The first letter labels conductivity.",
 r"The final table secants used for L are $(25.2-22.8)/(982-871)=0.0216216$~W\,m$^{-1}$\,K$^{-2}$ and $(670-645)/(1093-982)=0.225225$~J\,kg$^{-1}$\,K$^{-2}$. The changes apply above each table endpoint, including the solid range between the endpoint and $T_s$. Each conductivity branch changes $k$, its primitive $K$ and the surface inverse together; each storage branch changes $c_p$, $H$ and $T(H)$ together. The first letter labels conductivity.")
methods = change(methods,
 "These deterministic contrasts distinguish two continuation choices within the same model.",
 r"The conditional conductivity effect at held $c_p$ is $Q_{\HH}-Q_{\LH}=\Delta_k+I$; the conditional storage effect at held $k$ is $Q_{\HH}-Q_{\HL}=\Delta_c+I$. Reporting both conditions checks whether a direction changes with the other factor. These deterministic contrasts distinguish two continuation choices within the same model.")
diagnostic = r"""
The retained face transport diagnostic is
\begin{equation}
 |\mathrm{Pe}_f|=\frac{|\bm u\cdot\bm n_f|d_f}{D_f},
 \label{eq:pe}
\end{equation}
where $d_f$ is the adjacent cell-center separation. Unweighted medians are taken over internal axial faces adjacent to at least one cell with $T_s\leq T<T_l$. The diagnostic compares coordinate transport with diffusion in the discretized field; its selected face population can change between solved branches.

The discrete rear hot-region budget selects cells with $T\geq T_s$ and $\xi<0$. Net outward diffusive power is the sum of signed conductive face powers on the boundary of this selected cell set; internal face contributions cancel. The region is selected separately in each field, so its boundary and sampled faces change with the continuation. This accounting diagnostic is interpreted alongside the matched-coordinate centerline thresholds rather than as a fixed-region causal contrast.

"""
methods = change(methods, r"\subsection{Numerical checks and study provenance}", diagnostic + r"\subsection{Numerical evidence for the reported comparisons}")
provenance = "The original numerical case was produced with SimAgent-assisted execution."
assert provenance in methods
methods = methods[:methods.index(provenance)] + "The reproducibility package retains executed solver snapshots, input manifests, temperature arrays, calibration history and primary-observer code for the six solutions. Source-power integration, threshold crossings, primary passage geometry and finite-contrast algebra were independently reproduced from these artifacts.\n\n"

results = change(results,
 "Table~\\ref{tab:geometry} and Fig.~\\ref{fig:comparison} compare geometry after the B fit.",
 "The one-target calibration reproduces the B length proxy while leaving a systematic width/depth residual at B and C (Table~\\ref{tab:geometry} and Fig.~\\ref{fig:comparison}).")
results = change(results,
 "The discrepancy therefore concerns the relative contraction of transverse and depth extents as well as their absolute values.",
 "The modeled $W/D$ increases by 27.36\\% from B to C. The shape discrepancy therefore concerns the relative contraction of transverse and depth extents as well as their absolute values.")
results = change(results,
 "At C, material crosses a similar spatial interval 50\\% faster.",
 "The C span is 0.66\\% larger, while the passage time is 32.90\\% shorter because speed increases from 0.8 to 1.2~m/s.")
results = change(results,
 "A gives 120.74~\\us{} and 0.497~\\si{\\mega\\kelvin\\per\\second}.",
 "A gives 120.74~\\us{} and 0.497~\\si{\\mega\\kelvin\\per\\second}. Thus the B-to-C interval-mean cooling rate increases by 49.02\\% despite only a 0.53~\\um{} difference in the spatial phase span.")
results = change(results,
 "A comparison of LL and HH alone would miss this decomposition.",
 "A comparison of LL and HH alone would miss this decomposition. The signs persist at the other factor level: conductivity holding increases length by 40.45~\\um{} when $c_p$ is held, and storage holding decreases length by 8.93~\\um{} when $k$ is held. Conductivity therefore extends the tail and storage holding shortens it in both tested settings, with the interaction changing the magnitudes.")
results = change(results,
 "The rear phase span changes by only $-1.01$~\\um.",
 "The rear solidus displacement accounts for 98.3\\% of the conductivity-induced length increase; the front contributes the remaining 1.7\\%. The rear phase span changes by only $-1.01$~\\um.")
results = change(results,
 "Latent-inclusive effective specific heat changes from 5387.79 to 5336.67~\\si{\\joule\\per\\kilogram\\per\\kelvin}, about 0.95\\%.",
 "Sensible specific heat decreases from 721.13 to 670~\\si{\\joule\\per\\kilogram\\per\\kelvin}, or 7.09\\%. With the latent contribution included, effective specific heat decreases from 5387.79 to 5336.67~\\si{\\joule\\per\\kilogram\\per\\kelvin}, or 0.95\\%, and enthalpy from the cold reference decreases by 0.66\\%. This matched-temperature comparison describes the adopted mushy interval.")
results = change(results,
 "The diagnostic supports a model-internal transport explanation of the rear-tail shift.",
 "The diagnostic is consistent with a conductivity-dependent shift in the model's transport balance. The corresponding retained rear hot-region outward diffusive flux rises from 14.724 to 14.913~W. Since that region is selected by temperature and changes with the solved state, conductivity holding cannot be equated with a measured reduction in its integrated outward heat flow. The branch also changes surface recovery consistently with $k$.")
results = change(results,
 "These two continuation options therefore do not repair the baseline shape discrepancy.",
 "The conductivity depth effects remain negative at both storage levels ($-1.03$ and $-0.82$~\\um), whereas the storage depth effects remain positive at both conductivity levels (+0.49 and +0.71~\\um). These two continuation options therefore do not repair the baseline shape discrepancy.")
# Add uptake after retained figures, avoiding a dangling display at a section end.
results = change(results,
 r"\label{fig:fields}"+"\n"+r"\end{figure}",
 r"\label{fig:fields}"+"\n"+r"\end{figure}"+"\n\nThe common physical axes make the decrease in penetration relative to transverse width apparent. The surface contour and fusion envelope answer different geometric questions: the first determines the surface length proxy, while the second follows the maximum-temperature material passage through the field.")
results = change(results,
 r"\label{fig:trends}"+"\n"+r"\end{figure}",
 r"\label{fig:trends}"+"\n"+r"\end{figure}"+"\n\nThe operating-condition comparison therefore separates a change in the modeled fusion shape from a change in material passage time. The latter follows from the rear thresholds and speed; its experimental counterpart is not included in the geometric comparisons.")
results = change(results,
 r"\label{fig:factorial}"+"\n"+r"\end{figure}",
 r"\label{fig:factorial}"+"\n"+r"\end{figure}"+"\n\nAcross the four corners, the rear phase span lies between 79.25 and 81.17~\\um{} while total length ranges from 352.99 to 402.37~\\um. The contrast consequently changes the location of the rear phase interval much more than its spatial separation. This is the main comparison supplied by the retained centerline profiles; the small span ordering remains a current-mesh result.")

# Match the unchanged retained figures without inventing additional quantities.
methods = change(methods,
 "The 0.5~\\um\\ observation pitch samples interpolated geometry; it does not represent the resolution of the heat-field mesh.",
 "The 0.5~\\um\\ observation pitch samples interpolated geometry; it does not represent the resolution of the heat-field mesh. The geometric figure labels $L_s$, $W_f$ and $D_f$ correspond to the text's $L$, $W$ and $D$, respectively: $L_s$ is the surface length proxy, while $W_f$ and $D_f$ are fusion-envelope extents.")
def figure_notation(text):
    text = text.replace(r"s_m", r"\ell_m")
    text = text.replace(r"\Delta_k", r"\delta_k")
    text = text.replace(r"\Delta_c", r"\delta_{c_p}")
    text = text.replace(r"I&=", r"I_{k,c_p}&=")
    text = text.replace(r"+I", r"+I_{k,c_p}")
    return text.replace(r"$I$", r"$I_{k,c_p}$")
methods, results = figure_notation(methods), figure_notation(results)

for name, candidate, original in (("section-methods.tex", methods, old_methods), ("section-results.tex", results, old_results)):
    (OUT / name).write_text(candidate, encoding="utf-8")
    (OUT / (name + ".diff")).write_text("".join(difflib.unified_diff(original.splitlines(True), candidate.splitlines(True), fromfile="canonical/"+name, tofile="candidate/"+name)), encoding="utf-8")
appendix = r"\subsection{Executed material and nonlinear controls}" + "\n" + table + r"""
The Anderson controls are history depth $M=8$, initial scale $\alpha=0.2$, regularization $w_0=0.01$, fixed-point residual tolerance $2\times10^{-4}$~K in $U$, and an Armijo line search. The GMRES cap is 800 inner iterations with restart 80 and a $2\times10^{-9}$ tolerance. The preconditioner is Ruge--Stuben classical multigrid with strength threshold 0.25, symmetric Gauss--Seidel smoothing, V cycles, at most 20 levels and a coarse size of 100. The executed environment uses one BLAS thread. These controls are taken from the production manifests; alternative methods present in the solver source were not used for the six retained production solutions.
"""
(OUT / "appendix-methods.tex").write_text(appendix, encoding="utf-8")
print(json.dumps({"written":["section-methods.tex","section-results.tex"],"canonical_unchanged":True,
 "all_original_labels_retained":all(label in methods+results for label in [r"\label{tab:conditions}",r"\label{eq:enthalpy}",r"\label{eq:frame}",r"\label{eq:source}",r"\label{eq:face}",r"\label{eq:fusion}",r"\label{eq:passage}",r"\label{eq:contrast}",r"\label{tab:geometry}",r"\label{fig:comparison}",r"\label{fig:fields}",r"\label{fig:trends}",r"\label{tab:factorial}",r"\label{fig:factorial}"])}, indent=2))
