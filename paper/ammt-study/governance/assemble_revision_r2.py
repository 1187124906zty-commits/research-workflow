"""Integrate explicitly adopted section versions into the existing open source.

Only the coordinator invokes this after reading actual MAF returns/exchange.
The existing manuscript.tex is the sole article/editor authority.
"""
from pathlib import Path
import argparse
import re
import shutil

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER / "revision-r2"

TITLE = "Geometric calibration and thermal interpretation in laser melting of IN625: a high-temperature closure diagnosis"
ABSTRACT = r"""Geometric calibration gives efficient laser-melting models practical value, yet the thermal meaning of boundary agreement remains incompletely constrained. Solidification interpretation requires distinguishing the location of a melting boundary from the temperature interval and material history behind it. This study examines that tension using a conservative moving-frame enthalpy model of bare-plate IN625 tracks and public AMMT measurements. One effective source factor is fitted to a single length and then fixed for geometric comparisons and a four-corner high-temperature property contrast. The fitted condition remains 19.54~\um{} wider and 4.88~\um{} shallower than the reference means. Conductivity holding lengthens the modeled pool by 43.21~\um, while sensible-heat-capacity holding shortens it by 6.17~\um; their interaction partially offsets the joint response. Most of the conductivity-induced length change is a common rear solidus/liquidus displacement, rather than a comparable enlargement of their separation. Similar rear phase spans at two scan speeds consequently coexist with material passage times of 100.33 and 67.33~\us. These comparisons expose the distinct information carried by fusion shape, constitutive response and spatial-to-material-time mapping after one geometric calibration. The resulting diagnosis specifies which thermal interpretations the calibrated model supports and which require an independent thermal observable; it does not identify liquid properties or validate the derived histories."""
CONCLUSIONS = r"""\section{Conclusions}
The practical value of geometric calibration depends on the thermal interpretation subsequently drawn from it. For the present IN625 moving-frame enthalpy model, matching one surface length does not establish agreement of the fusion shape or remove dependence on high-temperature closure. The length-fitted condition remains 19.54~\um{} too wide and 4.88~\um{} too shallow relative to the nominal reference means; the faster fixed-parameter condition retains the same wide/shallow pattern. The observed discrepancies greatly exceed the inspected baseline axial changes, while source representation and observation mapping remain viable competing explanations.

Separating conductivity and sensible-storage continuations exposes information hidden by their joint change. Conductivity holding increases length by 43.21~\um{} and storage holding decreases it by 6.17~\um; the $-2.76$~\um{} interaction gives a net increase of 34.28~\um. Their directions persist at both tested levels of the other factor. The rear solidus supplies 98.3\% of the conductivity-induced length increase, and both rear phase boundaries move much farther than their separation changes. The principal response is therefore a displaced thermal tail. Opposing depth effects partly cancel, yet none of these continuations resolves the remaining shape discrepancy.

The spatial interval and the material interval convey different information. Rear phase spans near 80~\um{} at 0.8 and 1.2~m/s correspond to passage times of 100.33 and 67.33~\us, and a 49.02\% difference in the derived interval-mean cooling rate. This result is the material-coordinate transformation of the modeled field. It supplies a useful thermal-history diagnostic but does not independently establish cooling-rate or microstructure accuracy.

Together, the findings support evaluating geometric calibration through separate shape, closure and material-time questions. A common rear-boundary displacement should not be read as a comparably enlarged solidification interval, and a small joint property response should not be read as insensitivity of each constituent. This distinction identifies the next evidence needed for thermal credibility: aligned source and observation definitions, credible high-temperature material data and an independent thermal observable under the stated process conditions.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--introduction", required=True, type=Path)
    parser.add_argument("--discussion", required=True, type=Path)
    args = parser.parse_args()
    old = (REV / "inputs/manuscript-r1.tex").read_text(encoding="utf-8")
    intro = args.introduction.read_text(encoding="utf-8")
    discussion = args.discussion.read_text(encoding="utf-8")
    if not intro.startswith(r"\section{Introduction}") or not discussion.startswith(r"\section{Discussion}"):
        raise ValueError("Adopted candidates must have the corresponding section heading")
    methods = (REV / "methods-results/section-methods.tex").read_text(encoding="utf-8")
    results = (REV / "methods-results/section-results.tex").read_text(encoding="utf-8")
    method_anchor = "For a locally quasi-steady translating field"
    property_figure = (REV / "methods-results/property-figure-caption.tex").read_text(encoding="utf-8")
    property_figure = property_figure[property_figure.index(r"\begin{figure}"):property_figure.index(r"\end{figure}") + len(r"\end{figure}")]
    methods = methods.replace(method_anchor, "Figure~\\ref{fig:properties} separates tabulated interpolation from the high-temperature assumptions: both endpoints lie below the adopted solidus.\n\n" + property_figure + "\n\n" + method_anchor)
    calibration_details = re.search(r"The retained endpoints give lengths.*?A and C retain", methods, re.S)
    if calibration_details:
        methods = methods[:calibration_details.start()] + "Calibration trials and the local sensitivity conversion are reported in the appendix. A and C retain" + methods[calibration_details.end():]
    # The reader encounters the controlled tail response before material-time mapping.
    chunks = re.split(r"(?=\\subsection\{)", results)
    if len(chunks) != 4:
        raise ValueError("Inspect Results organization before automatic integration")
    results = chunks[0] + chunks[1] + chunks[3] + chunks[2]
    # Public compact package and original retained case have distinct contents.
    methods = methods.replace("The reproducibility package retains executed solver snapshots", "The original numerical case retains executed solver snapshots")
    prefix = old[:old.index(r"\section{Introduction}")]
    prefix = re.sub(r"\\title\{[^\n]+\}", lambda _: r"\title{" + TITLE + "}", prefix)
    prefix = re.sub(r"\\begin\{abstract\}.*?\\end\{abstract\}", lambda _: "\\begin{abstract}\n" + ABSTRACT + "\n\\end{abstract}", prefix, flags=re.S)
    suffix = old[old.index(r"\section*{Data and code availability}"):]
    appendix_start = suffix.index(r"\appendix")
    suffix = suffix[:appendix_start] + r"""\appendix
\section{Reproducible material and numerical controls}
""" + (REV / "methods-results/appendix-methods.tex").read_text(encoding="utf-8") + r"""

\subsection{Scalar calibration and retained sensitivities}
The calibration bracket $\eta\in[0.2,0.4]$ has retained endpoint lengths of 234.57 and 511.68~\um. Subsequent retained trial pairs $(\eta,L/\mathrm{\mu m})$ are $(0.2898051,359.96)$ and $(0.2853148,354.22)$, followed by the final $(0.2890548519,359.16)$. They establish a sampled local bracket, not global identifiability. The local secant sensitivity is approximately 1276.79~\um{} per unit $\eta$. Dividing B's 21.26~\um{} expanded uncertainty by this slope gives a scale $\Delta\eta=0.01665$; it is not a posterior interval and is not propagated into the geometry comparisons.
\begin{table}[htbp]
\centering
\caption{Retained calibrated axial sensitivities in \um, calculated as fine minus baseline. Only the near-source axial spacing changes from 4 to 2~\um; transverse and depth spacings remain 3 and 1~\um. These contrasts do not bound every discretization component.}
\begin{tabular}{lrrr}
\toprule
Condition & $\Delta L$ & $\Delta W$ & $\Delta D$\\
\midrule
B & +0.361 & $-0.009$ & +0.041\\
C & +0.199 & $-0.029$ & +0.045\\
\bottomrule
\end{tabular}
\end{table}

For uncertainty-scale reporting, $\delta/U=(Q_{\rm model}-\overline Q_{\rm source})/U_{\rm Lane}$. The separate $U$ values are not specimen standard deviations. Imaging and microscopy have different operators and aggregation, so the geometry triplet is not fitted to a joint likelihood. All finite contrasts use full-precision outputs before rounding for display.

\bibliographystyle{elsarticle-num}
\bibliography{literature/bibliography-r2}
\end{document}
"""
    source = prefix + intro + "\n" + methods + "\n" + results + "\n" + discussion + "\n" + CONCLUSIONS + "\n" + suffix
    (PAPER / "manuscript.tex").write_text(source, encoding="utf-8")
    for extension in ("pdf", "svg", "png"):
        shutil.copy2(REV / f"methods-results/ammt-property-continuations.{extension}", PAPER / f"figures/ammt-property-continuations.{extension}")
    print(f"Updated the existing manuscript.tex with explicitly supplied candidates ({len(source)} characters). Compile and review still required.")


if __name__ == "__main__":
    main()
