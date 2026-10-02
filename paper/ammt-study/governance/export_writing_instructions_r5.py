"""Export the actual MAF role loader output for same-task Codex application."""
import json
from pathlib import Path
from research_assistant import guidance

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'revision-r5/application/instructions'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    selection = {
        'introduction': ('writer', {'mode': 'revise', 'sections': ['introduction']}),
        'methods-results': ('writer', {'mode': 'revise', 'sections': ['methods_results']}),
        'whole-review': ('reviewer', {'mode': 'audit', 'sections': ['full_manuscript']}),
    }
    entries = []
    for name, (role, scope) in selection.items():
        text = guidance.load_role(role, scope)
        path = OUT / (name + '.md')
        path.write_text(text, encoding='utf-8')
        entries.append({'name': name, 'role': role, 'writing': scope,
            'skills': guidance.selected_skills(role, scope),
            'directly_delivered_references': guidance.selected_references(role, scope),
            'output': path.relative_to(ROOT).as_posix(), 'instruction_characters': len(text)})
    record = {'source': 'research_assistant.guidance.load_role', 'selections': entries,
        'execution_boundary': 'Actual loader output applied by same-task Codex specialists; R5 does not claim a new native MAF model execution.'}
    (OUT.parent / 'instruction-delivery.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(record, ensure_ascii=True))


if __name__ == '__main__':
    main()
