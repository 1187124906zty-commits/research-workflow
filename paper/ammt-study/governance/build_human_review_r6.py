"""Build a local human-reading bundle; never publish third-party originals."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse
import csv
import html
import json
import os
import re
import shutil
import zipfile
import pymupdf

PAPER = Path(__file__).resolve().parents[1]
OUT = PAPER / 'human-review-r6'
REV = PAPER / 'revision-r6'

def copy(path, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)

def visible(value):
    return str(value or '').replace('{', '').replace('}', '').replace(r'\&', '&')

def prune_supplement_copies(current_names, managed_names):
    """Remove only known supplement copies, never originals or unrelated files."""
    directory = (OUT / 'evidence/simulation-supplement').resolve()
    if not directory.is_relative_to(OUT.resolve()):
        raise ValueError('Supplement output escaped the local reading bundle')
    removed = []
    for name in sorted(set(managed_names) - set(current_names)):
        path = directory / name
        if path.is_file():
            if path.resolve().parent != directory:
                raise ValueError('Refusing to remove a supplement copy outside its output directory')
            path.unlink()
            removed.append(name)
    return removed

def localize_reading_links(source_path, target_path, targets):
    """Map included evidence links; retain other locators as nonclickable paths."""
    stats = {'mapped': 0, 'requires_original_project': 0}
    def replace(match):
        label, destination = match.groups()
        if destination.startswith(('http://', 'https://', 'mailto:', '#')):
            return match.group(0)
        locator, separator, fragment = destination.strip('<>').partition('#')
        original = (source_path.parent / locator).resolve()
        bundled = targets.get(original)
        if bundled and bundled.is_file():
            relative = os.path.relpath(bundled, target_path.parent).replace('\\', '/')
            stats['mapped'] += 1
            return f'[{label}]({relative}{separator}{fragment})'
        stats['requires_original_project'] += 1
        locator = original.relative_to(PAPER.resolve()).as_posix() if original.is_relative_to(PAPER.resolve()) else str(original)
        return f'{label}（原项目路径：`{locator}`；需原项目）'
    text = source_path.read_text(encoding='utf-8')
    target_path.write_text(re.sub(r'\[([^\]]+)\]\((<[^>]+>|[^)]+)\)', replace, text), encoding='utf-8')
    return stats

def abstract_from_json(path):
    item = json.loads(path.read_text(encoding='utf-8'))
    def find(value):
        if isinstance(value, dict):
            for key in ('abstract', 'abstract_inverted_index'):
                candidate = value.get(key)
                if isinstance(candidate, str):
                    return candidate
                if isinstance(candidate, dict):
                    positions = {p: word for word, ps in candidate.items() for p in ps}
                    return ' '.join(positions[n] for n in sorted(positions))
            for sub in value.values():
                result = find(sub)
                if result:
                    return result
        elif isinstance(value, list):
            for sub in value:
                result = find(sub)
                if result:
                    return result
        return ''
    return find(item)

def main():
    global OUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--revision', default='r6', help='Current local editorial revision; accepted numerical evidence remains R6')
    args = parser.parse_args()
    if not re.fullmatch(r'r[1-9][0-9]*', args.revision):
        parser.error('revision must be r followed by a positive integer')
    label = args.revision.upper()
    current = PAPER / ('revision-' + args.revision)
    if not current.is_dir():
        parser.error('Current revision directory is missing')
    OUT = PAPER / ('human-review-' + args.revision)
    source = (PAPER / 'manuscript.tex').read_text(encoding='utf-8')
    abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', source, re.S).group(1)
    abstract_words = len(abstract.split())
    figure_paths = list(dict.fromkeys(re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', source)))
    figure_count = len(re.findall(r'\\begin\{figure\*?\}', source))
    table_count = len(re.findall(r'\\begin\{table\*?\}', source))
    bbl = (PAPER / 'manuscript.bbl').read_text(encoding='utf-8')
    order = re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', bbl)
    cited = {k.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', source) for k in group.split(',')}
    if set(order) != cited or len(order) != len(cited):
        raise ValueError('Compiled bibliography and source citation set differ')
    ledger_path = current / 'sources/support-ledger.json'
    if not ledger_path.is_file():
        ledger_path = REV / 'sources/support-ledger.json'
    ledger = json.loads(ledger_path.read_text(encoding='utf-8'))
    lookup = {s['key']: s for s in ledger['sources']}
    if cited - lookup.keys():
        raise ValueError('Cited identity lacks located support')
    OUT.mkdir(exist_ok=True)
    for name in ('manuscript.pdf', 'manuscript.tex', 'submission-source.zip', 'reproduction-notes.md', 'highlights.txt'):
        copy(PAPER / name, OUT / 'manuscript' / name)
    word_available = (PAPER / 'manuscript.docx').is_file()
    if word_available:
        copy(PAPER / 'manuscript.docx', OUT / 'manuscript/manuscript.docx')
    bibliography = re.search(r'\\bibliography\{([^}]+)\}', source).group(1)
    copy(PAPER / (bibliography + '.bib'), OUT / 'manuscript' / (bibliography + '.bib'))
    for relative in figure_paths:
        copy(PAPER / relative, OUT / 'manuscript' / relative)
    for name in ('additive-manufacturing-guide-for-authors-2026-10-02.pdf', 'author-guide-ocr.txt'):
        copy(REV / 'journal' / name, OUT / 'journal' / name)
    copy(REV / 'guidance/author-guide-learning.md', OUT / 'journal/requirements-and-learning.md')
    requirements = current / 'journal/requirements.md'
    copy(requirements if requirements.is_file() else REV / 'journal/requirements.md', OUT / 'journal/current-manuscript-requirements.md')
    journal_sources = {
        (REV / 'guidance/author-guide-learning.md').resolve(): OUT / 'journal/requirements-and-learning.md',
        (requirements if requirements.is_file() else REV / 'journal/requirements.md').resolve(): OUT / 'journal/current-manuscript-requirements.md',
    }
    for name in ('additive-manufacturing-guide-for-authors-2026-10-02.pdf', 'author-guide-ocr.txt'):
        journal_sources[(REV / 'journal' / name).resolve()] = OUT / 'journal' / name
    prior_requirements = PAPER / 'revision-r7/journal/requirements.md'
    if args.revision == 'r8' and prior_requirements.is_file():
        target = OUT / 'journal/prior-r7-requirements.md'
        copy(prior_requirements, target)
        journal_sources[prior_requirements.resolve()] = target
    verification_files = []
    for name in ('package-rebuild-check.json', 'provenance.md'):
        path = current / 'delivery' / name
        if path.is_file():
            copy(path, OUT / 'verification' / name)
            verification_files.append(name)
    for relative in ('sources/citation-index.md', 'sources/report.md', 'sources/journal-learning.md',
                     'guidance/final-application-review.md', 'review/independent-review.md', 'review/review-response.md',
                     'guidance/callback-acceptance-review.md',
                     'application/supplement-integration-contract.md',
                     'application/methods-results-handoff.md', 'application/coordinator-disposition.md'):
        path = REV / relative
        if path.exists():
            copy(path, OUT / 'agent-learning' / path.name)
    copy(PAPER / 'evidence/verified-data.json', OUT / 'evidence/verified-data.json')
    for path in (PAPER / 'data').glob('*'):
        if path.is_file() and path.suffix in ('.csv', '.json'):
            copy(path, OUT / 'evidence/data' / path.name)
    state = json.loads((PAPER / '.researchflow/research-state.json').read_text(encoding='utf-8'))
    editorial_review_status = state['tasks'].get(label + '_REVIEW', {}).get('status', 'not_registered')
    editorial_recheck_status = state['tasks'].get(label + '_RECHECK', {}).get('status', 'not_applicable')
    current_reading_files = []
    current_sources = dict(journal_sources)
    if current != REV:
        for relative in ('editorial-contract.md', 'guidance/diagnosis.md',
                         'guidance/implementation-report.md', 'guidance/g1-response.md',
                         'guidance/routing-check.json',
                         'forward/prose.md', 'forward/transfer-review.md',
                         'forward/transfer-review.json',
                         'integration/editorial-disposition.md', 'integration/reverse-outline.md',
                         'integration/chapter-handoff.md', 'integration/source-diff.md',
                         'integration/terminology-and-scope.md',
                         'integration/render-inspection.md', 'integration/compile-result.json',
                         'integration/render-final-inspection.md',
                         'integration/pdf-binding-history.md',
                         'integration/reading-metrics.json', 'integration/promotion-summary.json',
                         'integration/maf-body-route.json', 'review/independent-review.md',
                         'guidance/transfer-map.md', 'guidance/result.json',
                         'guidance/patch proposal.txt', 'framing/original-boundary-excerpts.txt',
                         'integration/applied-writing-changes.md', 'integration/candidate-checks.json',
                         'integration/applied-guidance.md', 'integration/guidance-followup.md',
                         'integration/final-applied-guidance.md',
                         'integration/compression-promotion.json',
                         'integration/evidence-density-disposition.md',
                         'integration/guidance-tests.json',
                         'review/guide-review-prep.md', 'review/guide-followup.md',
                         'review/guide-followup.json',
                         'review/independent-review.json', 'review/final-recheck.md',
                         'review/final-recheck.json', 'review/g1-closure.md',
                         'review/g1-closure.json', 'review/final-repair-audit.json',
                         'review/source-read-scopes.json', 'review/review-response.md',
                         'review/read-scope.json',
                         'review/pdf-version-check.json',
                         'review/raw-evidence-check.json', 'review/primary-citation-spotcheck-scope.json',
                         'review/citation-placement-inspection.json', 'review/reviewer-guidance-trace.json',
                         'review/final-reviewer-guidance-trace.json',
                         'review/recheck-read-scope.json',
                         'review/final-recheck-actual-scope.md',
                         'review/recheck-reviewer-guidance-trace.json',
                         'delivery/argument-learning.md'):
            path = current / relative
            if path.is_file():
                target = OUT / 'current-revision' / relative
                copy(path, target)
                current_sources[path.resolve()] = target
                current_reading_files.append(relative)
        for relative in ('word/delivery/format-report.md', 'word/review/independent-review.md',
                         'word/review/independent-review.json', 'word/build/content-check.json',
                         'word/build/conversion-notes.md', 'word/delivery/guidance-tests.json'):
            path = current / relative
            if path.is_file():
                target = OUT / 'current-revision' / relative
                copy(path, target)
                current_sources[path.resolve()] = target
                current_reading_files.append(relative)
        maf = PAPER.parents[2] / 'research-assistant-maf'
        for name in ('section-specific-guidance.md', 'chapter-contracts.md',
                     'source-ledger.md', 'cohesion-source-ledger.md',
                     'object-and-continuity.md', 'review-and-handoffs.md',
                     'evidence-supplement.md', 'document-delivery.md'):
            path = maf / 'skills/scientific-writing/references' / name
            target = OUT / 'current-revision/reusable-writing' / name
            copy(path, target)
            current_sources[path.resolve()] = target
            current_reading_files.append('reusable-writing/' + name)
        # Reference-led revisions keep their actual dissection and reproducible
        # plot inputs alongside the paper. Large field archives remain at their
        # declared original case paths; a supplied published PDF stays local.
        for folder in ('reference-analysis', 'framing', 'body', 'methods', 'guidance', 'prose', 'visual'):
            folder_root = current / folder
            if args.revision in {'r9', 'r10', 'r11'} and folder in {'reference-analysis', 'visual'} and not folder_root.is_dir():
                folder_root = PAPER / 'revision-r8' / folder
            for path in sorted(folder_root.rglob('*')):
                if not path.is_file() or path.suffix not in ('.md', '.json', '.csv', '.py', '.tex', '.pdf', '.svg', '.png', '.npz'):
                    continue
                if any(part in {'renders', 'render', '__pycache__'} for part in path.relative_to(folder_root).parts):
                    continue
                relative = (Path(folder) / path.relative_to(folder_root)).as_posix()
                target = OUT / 'current-revision' / relative
                copy(path, target)
                current_sources[path.resolve()] = target
                current_reading_files.append(relative)
        reference_root = current / 'reference'
        if args.revision in {'r9', 'r10', 'r11'} and not reference_root.is_dir():
            reference_root = PAPER / 'revision-r8/reference'
        exemplar = reference_root / 'supplied-xiong2022.pdf'
        if exemplar.is_file():
            target = OUT / 'current-revision/reference/supplied-xiong2022.pdf'
            copy(exemplar, target)
            current_sources[exemplar.resolve()] = target
            current_sources[Path('C:/Users/Administrator/Downloads/main (1).pdf').resolve()] = target
            current_reading_files.append('reference/supplied-xiong2022.pdf')
        if exemplar.is_file():
            for path in sorted(reference_root.glob('*')):
                if path.name == exemplar.name or path.suffix not in ('.txt', '.json', '.png'):
                    continue
                target = OUT / 'current-revision/reference' / path.name
                copy(path, target)
                current_sources[path.resolve()] = target
            frozen = current / 'manuscript-input.tex'
            target = OUT / 'current-revision/manuscript-input.tex'
            copy(frozen, target)
            current_sources[frozen.resolve()] = target
            prior_number = int(args.revision[1:]) - 1
            before_folder = 'before-' + args.revision
            before_pdf = PAPER / f'human-review-r{prior_number}/manuscript/manuscript.pdf'
            if before_pdf.is_file():
                relative_before = f'{before_folder}/manuscript-r{prior_number}.pdf'
                target = OUT / 'current-revision' / relative_before
                copy(before_pdf, target)
                current_sources[before_pdf.resolve()] = target
                current_reading_files.append(relative_before)
            for relative in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', frozen.read_text(encoding='utf-8')):
                for suffix in ('.pdf', '.png'):
                    path = (PAPER / relative).with_suffix(suffix)
                    if path.is_file():
                        target = OUT / 'current-revision' / before_folder / 'figures' / path.name
                        copy(path, target)
                        current_sources[path.resolve()] = target
    supplement_task = state['tasks'].get('R6_SIMULATION_SUPPLEMENT', {})
    supplement_status = supplement_task.get('status', 'not_registered')
    application_status = state['tasks'].get('R6_SUPPLEMENT_APPLICATION', {}).get('status', 'not_registered')
    review_status = state['tasks'].get('R6_SUPPLEMENT_REVIEW', {}).get('status', 'not_registered')
    disposition_path = REV / 'simulation-supplement/acceptance-disposition.json'
    disposition = json.loads(disposition_path.read_text(encoding='utf-8')) if disposition_path.is_file() else {}
    supplement_accepted = supplement_status == 'accepted' and disposition.get('writing_callback_permitted') is True
    supplement_closed = supplement_accepted and application_status == 'accepted'
    supplement_notice = (
        '完整模拟补证已完成领域验收并由写作端接收、整合；支持、未解决与不支持的科学判断仍分别保留。'
        if supplement_closed else
        '模拟补证或写作接收尚未闭合，依赖新结果的最终数值判断保持待定。'
    )
    supplement_notice += f' 补证应用复核状态：{review_status}；人工评阅仍待用户实际反馈。'
    supplement_files = ['contract.md', 'acceptance-standard.md']
    if supplement_accepted:
        supplement_files += [
            'complete-report.md', 'writing-recommendations.md', 'acceptance-disposition.json',
            'final-researchflow-audit.json', 'execution-report.md', 'execution-report.json',
            'independent-review.md', 'independent-review.json',
            'observations-matched.csv', 'observations-matched.json', 'matched-analysis.json',
        ]
    (OUT / 'evidence/simulation-supplement').mkdir(parents=True, exist_ok=True)
    supplement_reading_files = []
    supplement_sources = {}
    for name in supplement_files:
        path = REV / 'simulation-supplement' / name
        if not path.is_file():
            raise FileNotFoundError('Missing contracted supplement reading artifact: ' + str(path))
        copy(path, OUT / 'evidence/simulation-supplement' / name)
        supplement_reading_files.append(name)
        supplement_sources[name] = path
    application_files = ['supplement-requester-disposition.md', 'supplement-application-disposition.md']
    if supplement_closed:
        for name in application_files:
            copy(REV / 'application' / name, OUT / 'evidence/simulation-supplement' / name)
            supplement_reading_files.append(name)
            supplement_sources[name] = REV / 'application' / name
    final_review_names = [
        'supplement-integrated-review.md', 'supplement-integrated-review.json',
        'supplement-final-review.md', 'supplement-final-review.json', 'supplement-review-response.md',
    ]
    for name in final_review_names:
        path = REV / 'review' / name
        if supplement_closed and path.is_file():
            copy(path, OUT / 'evidence/simulation-supplement' / name)
            supplement_reading_files.append(name)
            supplement_sources[name] = path
    session_path = REV / 'delivery/supplement-session.json'
    if session_path.is_file():
        copy(session_path, OUT / 'evidence/simulation-supplement/session.json')
        supplement_reading_files.append('session.json')
    historical_partial_names = [
        'initial-feedback.md', 'observations-initial.csv', 'observations-initial.json',
        'observations-HL.csv', 'observations-HL.json', 'observations-HL-LH.csv', 'observations-HL-LH.json',
        'threshold-conditioning-initial.json', 'requester-disposition.md',
    ]
    managed_names = supplement_files + application_files + final_review_names + historical_partial_names + [
        'session.json', 'complete-report.md', 'writing-recommendations.md', 'acceptance-disposition.json',
        'final-researchflow-audit.json', 'execution-report.md', 'execution-report.json',
        'independent-review.md', 'independent-review.json',
        'observations-matched.csv', 'observations-matched.json', 'matched-analysis.json',
    ]
    removed_supplement_copies = prune_supplement_copies(supplement_reading_files, managed_names)
    targets = {path.resolve(): OUT / 'evidence/simulation-supplement' / name
               for name, path in supplement_sources.items()}
    targets.update({(PAPER / name).resolve(): OUT / 'manuscript' / name
                    for name in ('manuscript.pdf', 'manuscript.tex', 'submission-source.zip', 'reproduction-notes.md', 'highlights.txt')})
    targets.update({(PAPER / name).resolve(): OUT / 'manuscript' / name for name in figure_paths})
    targets.update({(current / 'delivery' / name).resolve(): OUT / 'verification' / name for name in verification_files})
    targets.update(current_sources)
    for path, target in current_sources.items():
        if path.suffix == '.md':
            localize_reading_links(path, target, targets)
            if path == prior_requirements.resolve():
                historical_note = '# 历史R7指南核对记录\n\n以下原记录中的“当前”计数属于R7；R8实物与适配见[当前稿要求](current-manuscript-requirements.md)。官方指南原件仍为同一份2026-10-02快照。\n\n'
                target.write_text(historical_note + target.read_text(encoding='utf-8'), encoding='utf-8')
    for name in verification_files:
        path = current / 'delivery' / name
        if path.suffix == '.md':
            localize_reading_links(path, OUT / 'verification' / name, targets)
    supplement_link_counts = Counter()
    for name, path in supplement_sources.items():
        if path.suffix == '.md':
            supplement_link_counts.update(localize_reading_links(path, targets[path.resolve()], targets))
    supplement_note = '# 写作发起的主动补证\n\n' + supplement_notice + '\n\n'
    supplement_note += '原六组生产解保持不变；既有fine LL场复用而不重新标定eta；HL/LH/HH为三个新增同网格轴向精化分支。完整领域验收与写作端解释分别见acceptance-disposition和supplement-requester-disposition。原图和诊断保持基准网格身份，新增附录表报告精化值与配对漂移。\n\n'
    supplement_note += '最终状态以acceptance-disposition.json、complete-report.md及实际应用复核为准；writing-recommendations保留了形成时“待验收”的历史开场，不能据此否定其后实际处置。initial-feedback等部分返回仅保留在研究目录历史中，不纳入此最终阅读包。包内agent-learning的初次R6审查是补证前记录，不充当最终补证应用验收。\n\n'
    supplement_note += '\n'.join(f'- [{name}]({name})' for name in supplement_reading_files) + '\n'
    (OUT / 'evidence/simulation-supplement/README.zh.md').write_text(supplement_note, encoding='utf-8')
    entries, cards, paragraphs = [], [], []
    labels = {'full_text': '原文支持（选读相关位置）', 'abstract_only': '摘要支持', 'software_identity_only': '实际软件身份引用'}
    for number, key in enumerate(order, 1):
        item = lookup[key]
        identity = item['identity']
        raw = item.get('read_original_path')
        local = ''
        if raw:
            original = PAPER / raw
            if not original.is_file():
                raise FileNotFoundError(original)
            local = f'references/originals/{number:02d}-{key}{original.suffix}'
            copy(original, OUT / local)
        abstract = ''
        if raw and item['read_evidence_class'] == 'abstract_only':
            if original.suffix == '.json':
                abstract = abstract_from_json(original)
            elif original.suffix == '.pdf':
                with pymupdf.open(original) as pdf:
                    abstract = pdf[4].get_text() if key == 'feedforward2025' else ''
        row = {'number': number, 'key': key, 'title': visible(identity['title']),
               'authors': visible(identity.get('author')), 'year': identity.get('year', ''),
               'journal': visible(identity.get('journal', '')), 'doi_or_official_url': item['doi_or_official_url'],
               'reading_class': item['read_evidence_class'], 'version': item.get('source_version', ''),
               'locators': item.get('read_locators', ''), 'claim_supported': item.get('claim_supported', ''),
               'limits': item.get('limits', ''), 'local_original': local, 'abstract': abstract}
        entries.append(row)
        note = f"# [{number}] {row['title']}\n\n{row['authors']} · {row['journal']} · {row['year']}\n\n"
        note += f"- DOI/官方来源：{row['doi_or_official_url']}\n- 学习范围：{labels[row['reading_class']]}\n- 版本：{row['version']}\n- 原文定位：{row['locators']}\n- 支持：{row['claim_supported']}\n- 边界：{row['limits']}\n"
        if local:
            note += f"- 本地原件：[打开](../../{local})\n"
        if abstract:
            note += '\n## 保留摘要 / 摘要所在页\n\n' + abstract + '\n'
        note_path = OUT / f'references/notes/{number:02d}-{key}.md'
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_text(note, encoding='utf-8')
        paragraphs.append(note.replace(f'(../../{local})', f'({local})'))
        material_label = '保留摘要证据记录' if local.endswith('.json') else '本地原件'
        link = f'<a href="{html.escape(local, quote=True)}">{material_label}</a> · ' if local else ''
        fields = ''.join(f'<dt>{label}</dt><dd>{html.escape(str(row[field]))}</dd>' for label, field in
                         (('实际阅读', 'reading_class'), ('版本', 'version'), ('阅读定位', 'locators'), ('用于支持', 'claim_supported'), ('解释边界', 'limits')))
        cards.append(f'<article><h3>[{number}] {html.escape(row["title"])}</h3><p>{html.escape(row["authors"])} · {html.escape(row["journal"])} · {row["year"]}</p><p>{link}<a href="{html.escape(row["doi_or_official_url"], quote=True)}">DOI / 官方来源</a></p><dl>{fields}</dl></article>')
    counts = Counter(row['reading_class'] for row in entries)
    class_summary = '、'.join(f"{counts.get(key, 0)} 个{label}" for key, label in
                             (('full_text', '相关原文支持'), ('abstract_only', '摘要支持'),
                              ('software_identity_only', '软件身份')))
    (OUT / 'reference-index.md').write_text('# 与排印稿一致的参考文献阅读索引\n\n编号按当前 PDF 文末顺序。摘要支持不代表全文已读；预印本、接受稿与出版版保留各自身份。\n\n' + '\n\n'.join(paragraphs), encoding='utf-8')
    with (OUT / 'reference-index.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        columns = [x for x in entries[0] if x != 'abstract']
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(entries)
    with pymupdf.open(PAPER / 'manuscript.pdf') as pdf:
        manuscript_pages = len(pdf)
        text = '\n'.join(page.get_text() for page in pdf)
    with pymupdf.open(REV / 'journal/additive-manufacturing-guide-for-authors-2026-10-02.pdf') as guide:
        guide_pages = len(guide)
    original_documents = sum(row['local_original'].endswith(('.pdf', '.html')) for row in entries)
    abstract_document_count = sum(row['reading_class'] == 'abstract_only' and
                                  row['local_original'].endswith(('.pdf', '.html')) for row in entries)
    report = {'revision': label, 'human_review_status': 'awaiting_review', 'actual_citations': len(entries),
              'built_at_utc': datetime.now(timezone.utc).isoformat(),
              'reading_classes': dict(counts), 'local_reading_material_files': sum(bool(row['local_original']) for row in entries),
              'original_documents': original_documents,
              'abstract_only_original_documents': abstract_document_count,
              'abstract_metadata_records': sum(row['local_original'].endswith('.json') for row in entries),
              'guide_pages': guide_pages, 'manuscript_pages': manuscript_pages,
              'abstract_source_whitespace_words': abstract_words,
              'figures': figure_count, 'tables': table_count,
              'vector_figure_files': sum(Path(path).suffix.lower() in ('.pdf', '.svg') for path in figure_paths),
              'pdf_extracted_whitespace_word_estimate': len(text.split()),
              'word_count_scope': 'Entire rendered PDF including references and captions; local estimate, not Word/iThenticate result',
              'supplement_task_status': supplement_status,
              'supplement_application_status': application_status,
              'supplement_review_status': review_status,
              'domain_acceptance_status': disposition.get('status', 'not_recorded'),
              'supplement_requester_closed': supplement_closed,
              'supplement_reading_files': supplement_reading_files,
              'removed_obsolete_supplement_copies': removed_supplement_copies,
              'supplement_markdown_links': dict(supplement_link_counts),
              'verification_reading_files': verification_files,
              'editorial_review_status': editorial_review_status,
              'editable_word_available': word_available,
              'editable_word_review_status': state['tasks'].get(label + '_WORD_REVIEW', {}).get('status', 'not_registered'),
              'editorial_recheck_status': editorial_recheck_status,
              'current_revision_reading_files': current_reading_files,
              'supplement_notice': supplement_notice,
              'publication_status': label + ' held locally for user evaluation; third-party originals excluded from GitHub',
              'entries': entries}
    (OUT / 'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    note = '# ' + label + ' 人工评估资料包\n\n先打开 index.html。手稿、作者指南及文末实际引用的阅读材料按当前稿件一同提供。\n\n'
    if word_available:
        note += '另附[可编辑Word](manuscript/manuscript.docx)，转换范围与版式差异见[格式说明](current-revision/word/delivery/format-report.md)。\n\n'
    note += f"当前手稿 {manuscript_pages} 页，摘要源文本本地统计 {abstract_words} 词，{figure_count} 图、{table_count} 表，实际 {len(entries)} 个引用身份：{class_summary}。{original_documents} 个原始PDF/HTML阅读文件随包保留，其中 {abstract_document_count} 个本轮仅用于摘要支持；其他摘要元数据和软件记录保留真实阅读等级，不伪造缺失全文。\n\n"
    note += f'作者指南为用户提供的2026-10-02官方页面{guide_pages}页原件，OCR仅供搜索；重要数字以原页为准。摘要上限250词，完整研究论文5,000–13,000词（含图注和参考文献），最终要求Word或iThenticate计数。本地PDF提取估计见manifest，不能替代指定工具。指南中50条文献上限属于Perspective。\n\n'
    note += '建议先检查引言研究动机与文献谱系，再检查每个结果单元的比较目的、数据与解释是否相连，最后评估结论及模型边界。与某一来源核对时，使用相同编号的原件与定位说明。未读取的全文不得由阅读标记推断。\n\n'
    note += supplement_notice + ' [查看主动补证的实际交接](evidence/simulation-supplement/README.zh.md)。\n\n'
    if verification_files:
        note += '本地编译与重建说明：' + ' · '.join(f'[{name}](verification/{name})' for name in verification_files) + '。\n\n'
    if current_reading_files:
        note += '本轮写作与独立审查：' + ' · '.join(f'[{name}](current-revision/{name})' for name in current_reading_files) + '。\n\n'
    note += f'人工状态：待评阅。此包没有表示用户已批准、作者已完成最终人工审核或期刊已经评审。{label}新稿及其GitHub展示暂未推送。原件用于本地个人评估，公开仓库只保留手稿、工具、来源链接与学习总结；第三方原件不随项目许可证重新授权。\n'
    (OUT / 'README.zh.md').write_text(note, encoding='utf-8')
    page = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>R6 手稿与参考资料</title><style>body{max-width:1080px;margin:40px auto;padding:0 24px;color:#192638;background:#f3f6fa;font:16px/1.65 system-ui}h1{font-size:30px}a{color:#155bbb}nav,article,.notice{background:white;border:1px solid #dbe3ee;padding:18px 24px;border-radius:10px;margin:18px 0}nav a{display:inline-block;margin:5px 18px 5px 0}input{box-sizing:border-box;width:100%;font:inherit;padding:12px;border:1px solid #aab8ce;border-radius:8px}h3{margin:0 0 8px}dt{font-weight:600;margin-top:10px}dd{margin:0;overflow-wrap:anywhere}.meta{color:#506079}</style><h1>R6 手稿、作者指南与文献</h1><p class="meta">2026-10-02 · Additive Manufacturing · 待人工评估</p><nav><a href="manuscript/manuscript.pdf">阅读论文 PDF</a><a href="manuscript/manuscript.tex">LaTeX 源码</a><a href="manuscript/submission-source.zip">完整源码包</a>'''
    page += f'<a href="journal/additive-manufacturing-guide-for-authors-2026-10-02.pdf">{guide_pages}页作者指南原件</a>'
    if word_available:
        page += '<a href="manuscript/manuscript.docx">可编辑Word</a><a href="current-revision/word/delivery/format-report.md">Word转换与版式差异</a>'
    page += '''<a href="journal/author-guide-ocr.txt">指南OCR辅助搜索</a><a href="journal/requirements-and-learning.md">逐页要求与学习说明</a><a href="journal/current-manuscript-requirements.md">当前稿件适配</a><a href="reference-index.csv">文献索引CSV</a><a href="reference-index.md">文献用途与定位</a><a href="README.zh.md">评估说明</a></nav>'''
    if verification_files:
        page += '<nav>' + ''.join(f'<a href="verification/{name}">{name}</a>' for name in verification_files) + '</nav>'
    page += f'<div class="notice"><b>{len(entries)} 个实际引用身份</b>：{html.escape(class_summary)}。{original_documents} 个原始PDF/HTML阅读文件随包；其中 {abstract_document_count} 个本轮限于摘要支持。其余缺失全文保留真实状态与官方链接。<p>当前手稿{manuscript_pages}页，摘要本地统计{abstract_words}词，{figure_count}图、{table_count}表。全文本地PDF估计见manifest，Word/iThenticate正式口径待作者确认。R6暂留本地供你评估。</p></div>'
    page += '<div class="notice"><b>主动补证状态</b><p>' + html.escape(supplement_notice) + '</p><a href="evidence/simulation-supplement/README.zh.md">完整补证验收、请求者解释与当前应用复核</a></div>'
    page += '<input id="search" placeholder="搜索标题、作者、DOI、用途或限制"><section id="refs">'
    page += '\n'.join(cards) + '''</section><script>document.getElementById('search').addEventListener('input',function(){const q=this.value.toLowerCase();document.querySelectorAll('article').forEach(e=>e.hidden=!e.textContent.toLowerCase().includes(q));});</script></html>'''
    page = page.replace('R6 手稿', label + ' 手稿').replace('R6暂留本地', label + '暂留本地')
    page = page.replace('2026-10-02 · Additive Manufacturing · 待人工评估',
                        datetime.now().strftime('%Y-%m-%d') + ' · Additive Manufacturing · 待人工评估')
    if current_reading_files:
        priority_links = {
            'reference/supplied-xiong2022.pdf': '用户指定的参考原文',
            'reference-analysis/article-dissection.md': '逐节拆解参考论文',
            'reference-analysis/difference-map.md': '上一稿的具体差距',
            'delivery/argument-learning.md': '研究思路与因素分析的学习',
            'before-r8/manuscript-r7.pdf': '上一版PDF',
            'before-r9/manuscript-r8.pdf': '本轮修改前PDF',
            'before-r10/manuscript-r9.pdf': '本轮修改前PDF',
            'before-r11/manuscript-r10.pdf': '本轮修改前PDF',
            'integration/terminology-and-scope.md': '术语定义、引用简化与范围归属',
            'guidance/source-learning.md': '已发表论文的表达与论证对照',
            'guidance/contribution-assessment.md': '外推方案的贡献与通用性评估',
            'guidance/section-boundary-learning.md': '已发表论文的章节接口对照',
            'integration/chapter-handoff.md': '章节职责与双向交接',
            'integration/source-diff.md': '本轮实际源码修改',
            'guidance/diagnosis.md': '研究论证与表达诊断',
            'guidance/transfer-map.md': '范文与通用规范的对应',
            'integration/applied-writing-changes.md': '规范在修改稿中的实际应用',
            'integration/reverse-outline.md': '当前全文反向提纲',
            'visual/handoff.md': '新图的数据与解释',
            'review/review-response.md': '审查与修复处置',
            'review/independent-review.md': '独立整稿审查',
            'review/final-recheck.md': '最终受影响范围复查',
            'word/delivery/format-report.md': '可编辑Word的内容与版式核对',
        }
        selected_links = [(name, priority_links.get(name, name)) for name in current_reading_files
                          if name in priority_links]
        if not selected_links:
            selected_links = [(name, name) for name in current_reading_files]
        navigation = '<nav><b>' + label + '写作与独立复核</b> ' + ''.join(f'<a href="current-revision/{name}">{html.escape(title)}</a>' for name, title in selected_links) + '<a href="README.zh.md">全部材料与源数据索引</a></nav>'
        page = page.replace('<input id="search"', navigation + '<input id="search"')
    (OUT / 'index.html').write_text(page, encoding='utf-8')
    bad = []
    for target in re.findall(r'href="([^"#]+)"', page):
        if not target.startswith(('http://', 'https://')) and not (OUT / html.unescape(target)).is_file():
            bad.append(target)
    if bad:
        raise ValueError('Missing local reader targets: ' + str(bad))
    zip_path = PAPER / ('human-review-' + args.revision + '.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(OUT.rglob('*')):
            if path.is_file():
                archive.write(path, path.relative_to(OUT))
    summary = {k: v for k, v in report.items() if k != 'entries'}
    summary.update({'zip_bytes': zip_path.stat().st_size, 'reader_links_checked': True})
    (current / 'delivery').mkdir(exist_ok=True)
    (current / 'delivery/human-review-package.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
