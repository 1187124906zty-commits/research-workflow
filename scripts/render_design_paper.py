"""Generate one self-contained LaTeX source from the maintained design paper.

Supports only the paragraph, heading, table, math and citation forms used by
this manuscript. It does not compile or claim to be a general Markdown parser.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def escape(text: str) -> str:
    mapping = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
               "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
               "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(mapping.get(char, char) for char in text)


def inline(text: str, cite: bool = True) -> str:
    pattern = re.compile(r"(https?://[^\s]+|`[^`]+`|\$[^$]+\$|\*\*[^*]+\*\*|\[[0-9]+(?:[–-][0-9]+|(?:\s*,\s*[0-9]+)*)?\])")
    pieces = []
    start = 0
    for match in pattern.finditer(text):
        pieces.append(escape(text[start:match.start()]))
        item = match.group()
        if item.startswith("http"):
            tail = "." if item.endswith(".") else ""
            url = item[:-1] if tail else item
            pieces.append(r"\url{" + url + "}" + tail)
        elif item.startswith("`"):
            pieces.append(r"\texttt{" + escape(item[1:-1]) + "}")
        elif item.startswith("$"):
            pieces.append(item)
        elif item.startswith("**"):
            pieces.append(r"\textbf{" + inline(item[2:-2], cite) + "}")
        elif cite:
            values = item[1:-1]
            if "–" in values or "-" in values:
                lo, hi = re.split("[–-]", values)
                ids = list(range(int(lo), int(hi) + 1))
            else:
                ids = [int(value.strip()) for value in values.split(",")]
            pieces.append(r"\cite{" + ",".join("r" + str(value) for value in ids) + "}")
        else:
            pieces.append(escape(item))
        start = match.end()
    pieces.append(escape(text[start:]))
    return "".join(pieces)


def render(markdown: str) -> str:
    lines = markdown.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("The manuscript must start with a title")
    title = lines[0][2:]
    output = [r"\documentclass[UTF8,fontset=fandol,a4paper,11pt]{ctexart}",
              r"\usepackage[margin=25mm]{geometry}",
              r"\usepackage{amsmath,booktabs,tabularx,array}",
              r"\usepackage[unicode,hidelinks]{hyperref}",
              r"\usepackage{url}",
              r"\urlstyle{same}", r"\setlength{\emergencystretch}{2em}",
              r"\setlength{\parskip}{0.3em}",
              r"\title{" + escape(title) + "}", r"\author{}", r"\date{}",
              r"\begin{document}", r"\maketitle"]
    index = 1
    bibliography = False
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            output.append("")
        elif line.startswith("## 参考文献"):
            bibliography = True
            output.append(r"\begin{thebibliography}{99}")
        elif bibliography:
            match = re.match(r"\[([0-9]+)\]\s+(.+)", line)
            if not match:
                raise ValueError("Unexpected bibliography line: " + line)
            output.append(r"\bibitem{r" + match[1] + "} " + inline(match[2], cite=False))
        elif line == "$$":
            equation = []
            index += 1
            while index < len(lines) and lines[index].strip() != "$$":
                equation.append(lines[index])
                index += 1
            if index >= len(lines):
                raise ValueError("Unterminated display equation")
            output.extend([r"\begin{equation}", *equation, r"\end{equation}"])
        elif line.startswith("|"):
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"[:\- ]+", cell) for cell in cells):
                    rows.append(cells)
                index += 1
            index -= 1
            columns = len(rows[0])
            if any(len(row) != columns for row in rows):
                raise ValueError("Inconsistent table width")
            output.extend([r"\begin{center}", r"\small",
                           r"\begin{tabularx}{\textwidth}{" + ">{\\raggedright\\arraybackslash}X" * columns + "}",
                           r"\toprule"])
            for number, row in enumerate(rows):
                output.append(" & ".join(inline(cell) for cell in row) + r" \\")
                if number == 0:
                    output.append(r"\midrule")
            output.extend([r"\bottomrule", r"\end{tabularx}", r"\end{center}"])
        elif line.startswith("### "):
            value = re.sub(r"^[0-9]+(?:\.[0-9]+)*\s+", "", line[4:])
            output.append(r"\subsection{" + escape(value) + "}")
        elif line.startswith("## "):
            value = line[3:]
            if value in ("摘要", "Abstract"):
                output.append(r"\section*{" + value + "}")
            else:
                value = re.sub(r"^[0-9]+\s+", "", value)
                output.append(r"\section{" + escape(value) + "}")
        elif line.startswith("**ResearchFlow:") and line.endswith("**"):
            output.append(r"\begin{center}\large " + inline(line[2:-2]) + r"\end{center}")
        else:
            output.append(inline(line))
        index += 1
    if bibliography:
        output.append(r"\end{thebibliography}")
    output.extend([r"\end{document}", ""])
    return "\n".join(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "paper/researchflow-design.zh.md")
    parser.add_argument("--output", type=Path, default=ROOT / "paper/researchflow-design.zh.tex")
    args = parser.parse_args()
    tex = render(args.source.read_text(encoding="utf-8-sig"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(tex, encoding="utf-8", newline="\n")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
