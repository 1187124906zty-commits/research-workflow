"""Check the Git index, public links and source archive for this case release.

Run after selectively staging the intended release. This check uses tracked
blobs rather than local file existence; private reading copies are not needed.
It checks publication packaging, not research claims or journal acceptance.
"""
from pathlib import Path
import argparse
import io
import json
import posixpath
import re
import subprocess
import zipfile
import xml.etree.ElementTree as ET

REPO = Path(__file__).resolve().parents[3]
CASE = "paper/ammt-study"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", default="revision-r11")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    tracked = set(git("ls-files", "-z").decode("utf-8").split("\0")) - {""}
    documents = ["README.md", f"{CASE}/README.md"] + [
        f"{CASE}/{args.revision}/{name}" for name in (
            "README.md", "journal/requirements.md",
            "integration/terminology-and-scope.md", "integration/source-diff.md",
            "review/review-response.md", "word/delivery/format-report.md")]
    issues = []
    links = 0

    def blob(path):
        return git("show", ":" + path)

    for path in documents:
        if path not in tracked:
            issues.append(f"Public document not staged: {path}")
            continue
        content = blob(path).decode("utf-8")
        for target in re.findall(r"\]\((<[^>]+>|[^)]+)\)", content):
            target = target.strip("<>").split("#")[0]
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            links += 1
            if re.match(r"^(?:[A-Za-z]:|/|\\)", target):
                issues.append(f"Local absolute link in {path}: {target}")
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), target))
            if resolved not in tracked and not any(
                item.startswith(resolved.rstrip("/") + "/") for item in tracked
            ):
                issues.append(f"Unpublished target in {path}: {target}")

    excluded = [path for path in tracked if path.startswith(CASE + "/") and (
        re.search(r"/human-review-r\d+(?:/|\.zip$)", path)
        or path.endswith(".npz")
        or re.search(r"/(?:pdfs|texts?|ocr|raw|renders?)/", path)
        or re.search(r"/revision-r11/word/(?:build|review)/", path)
        or re.search(r"(?:author-guide|guide-for-authors|supplied-xiong).*\.pdf$", path)
    )]
    issues.extend(f"Private or intermediate file tracked: {path}" for path in excluded)

    source = blob(f"{CASE}/manuscript.tex").decode("utf-8")
    bibliography = re.search(r"\\bibliography\{([^}]+)\}", source).group(1)
    figures = list(dict.fromkeys(re.findall(
        r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", source)))
    expected = {"manuscript.tex", "bibliography.bib", "highlights.txt",
                "reproduction-notes.md", "README.txt"} | {
                    posixpath.basename(path) for path in figures}
    with zipfile.ZipFile(io.BytesIO(blob(f"{CASE}/submission-source.zip"))) as archive:
        names = archive.namelist()
        if len(names) != len(expected) or set(names) != expected:
            issues.append("Archive contents differ from the manuscript source/asset set")
        flattened = source.replace("{figures/", "{").replace(
            "{" + bibliography + "}", "{bibliography}")
        mappings = {"manuscript.tex": flattened.encode("utf-8"),
                    "bibliography.bib": blob(f"{CASE}/{bibliography}.bib"),
                    "highlights.txt": blob(f"{CASE}/highlights.txt"),
                    "reproduction-notes.md": blob(f"{CASE}/reproduction-notes.md")}
        mappings.update({posixpath.basename(path): blob(f"{CASE}/{path}") for path in figures})
        for name, data in mappings.items():
            archived = archive.read(name) if name in names else None
            if archived is not None and name.endswith((".tex", ".bib", ".txt", ".md")):
                archived = archived.replace(b"\r\n", b"\n")
                data = data.replace(b"\r\n", b"\n")
            if archived != data:
                issues.append(f"Archive asset differs from staged canonical source: {name}")

    with zipfile.ZipFile(io.BytesIO(blob(f"{CASE}/manuscript.docx"))) as word:
        xml = ET.fromstring(word.read("word/document.xml"))
        tables = len(xml.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl"))
        maths = len(xml.findall(".//{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath"))
    report = {
        "scope": "Selected public documents and case assets in the Git index; no private originals required",
        "checked_documents": documents,
        "checked_repository_relative_links": links,
        "source_archive_files": names,
        "source_archive_matches_staged_canonical": not any("Archive" in item for item in issues),
        "text_comparison": "CRLF/LF normalized; all other text bytes and vector-figure bytes compared",
        "word_native_tables": tables,
        "word_native_math_objects": maths,
        "unresolved_publication_defects": issues,
        "limits": "Link targets are checked against tracked paths, not remote HTTP availability. Packaging does not verify physical claims or human approval."
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return bool(issues)


if __name__ == "__main__":
    raise SystemExit(main())
