from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
DATE = '2026-10-02'

def passage(section, quote, paraphrase, application, boundary):
    return dict(section=section, short_quote=quote, paraphrase=paraphrase,
                agent_application=application, boundary=boundary)

def item(key, title, url, provenance, file, scope, passages, license, reuse, kind='institutional teaching guide'):
    text = (ROOT/'sources'/file).read_text(encoding='utf-8')
    normalized = ' '.join(text.split())
    for p in passages:
        if ' '.join(p['short_quote'].split()) not in normalized:
            raise ValueError(f'Unlocated quote: {key}: {p["short_quote"]}')
        q = p['short_quote']
        index = text.find(q)
        p['local_text_line'] = text[:index].count('\n')+1 if index>=0 else None
    return dict(id=key,title=title,original_url=url,provenance=provenance,
                source_kind=kind,retrieved_and_read_on=DATE,read_scope=scope,
                local_reading_record='sources/'+file,passages=passages,
                authority='writing pedagogy or scholarly advice; not this manuscript venue requirement',
                license_observed=license,reuse_scope=reuse)

mit_license='Footer explicitly states CC BY-NC 4.0 unless otherwise noted.'
mit_reuse='Attribute source and observe the noncommercial condition for copied/adapted licensed content; this package uses brief located quotation and independently worded synthesis, not a republished CommKit. Full local text is a private reading record.'
unc_license='Footer explicitly states CC BY-NC-ND 4.0 and permits noncommercial reproduction of the entire handout with attribution.'
unc_reuse='Do not distribute an edited/translated version of the handout as a licensed derivative. Here: attribution, minimal quotation and independently composed analysis of ideas; full extracted handout remains local. No permission for commercial republishing is claimed.'
unknown='No explicit open reuse license was observed in the substantive page/footer read.'
unknown_reuse='Link and attribute; use minimal quotation and independently worded commentary. Do not redistribute the full page or phrase bank as an open-licensed source. Local full text is a private reading record.'

sources=[
item('MIT_CEE_TITLE','Journal Article',
 'https://mitcommlab.mit.edu/cee/commkit/journal-article/',
 'MIT Civil and Environmental Engineering Communication Lab; page credits Communication Fellow Andrew Feldman for the most recent revision.',
 'mit-cee-title-fetch.txt','Complete substantive guide, especially Criteria for Success, Identify Your Purpose, Analyze Your Audience and Skills: The title is attractive / The abstract is key / Each paragraph starts with the message.',[
 passage('Skills > The title is attractive','A great option for your title is a shortened version of your one-to-two sentence main message.',
 'A title can condense the main message while using accessible topic keywords; readership determines background and detail.',
 'Compare title candidates with the evidence-supported central message and search terms.',
 'A useful option, not a mandate to use a declarative title or exactly one sentence. No title grammar/collocation list is supplied; that check remains an editorial inference.')],mit_license,mit_reuse),
item('MIT_ABSTRACT','Journal Article: Abstract',
 'https://mitcommlab.mit.edu/broad/commkit/journal-article-abstract/',
 'Broad Research Communication Lab on the MIT domain; page states adaptation from MIT Biological Engineering Communication Lab.',
 'mit-abstract-fetch.txt','Complete substantive guide: When to Write the Abstract, Purpose and Abstract Formula; linked annotated PDFs not read.',[
 passage('When to Write the Abstract','write your abstract last.',
 'Distill the actual completed sections and subtract/consolidate findings until the crucial results remain.',
 'Draft from the current Results/Discussion; rank possible quantitative anchors by what conclusion each establishes.',
 'Writing last is a tactic, not an exclusive sequence; a working abstract can guide earlier work.'),
 passage('Abstract Formula > Implications','Describe how your findings influence our understanding of the relevant field',
 'Context, question, approach, selected findings and implications jointly make the abstract informative.',
 'End on the concrete understanding or decision changed by the finding, including a useful negative finding.',
 'The six-component formula and suggested sentence ranges are this teaching model; do not impose six sentences or a fixed number of numerical results.')],mit_license,mit_reuse),
item('MIT_INTRODUCTION','Journal Article: Introduction',
 'https://mitcommlab.mit.edu/broad/commkit/journal-article-introduction/',
 'Broad Research Communication Lab on the MIT domain; adapted from MIT Biological Engineering Communication Lab.',
 'mit-introduction-fetch.txt','Complete substantive guide: When to Write the Introduction, Purpose and Introduction Formula; annotated example PDFs not read.',[
 passage('Introduction Formula > Specific Background','Your purpose is not to showcase the breadth of your knowledge',
 'Supply the knowledge needed to understand the system, question and significance, then articulate a question made logical by that background.',
 'Synthesize related evidence by what it establishes; remove background that does not help derive the current question.',
 'The four ordered components are a rhetorical model, not four paragraphs or a required broad-opening sentence.')],mit_license,mit_reuse),
item('MIT_METHODS','Journal Article: Methods',
 'https://mitcommlab.mit.edu/broad/commkit/journal-article-methods/',
 'Broad Research Communication Lab on the MIT domain; adapted from MIT Biological Engineering Communication Lab.',
 'mit-methods-fetch.txt','Complete substantive guide: Criteria, Identify Your Purpose, Analyze your audience, all Skills subsections; linked example PDF not read.',[
 passage('Skills > Provide minimal essential detail','specify any methodological details that might cause someone to reach a different conclusion.',
 'Methods serve validity assessment and replication; describe purpose/application, original standard-method sources and modifications, with a logical correspondence to Results.',
 'Preserve controls, operators, calibration data, parameter roles and changes affecting interpretation; allocate routine execution detail to an accessible reproduction record.',
 'Minimal means sufficient, not short by quota. Its avoid-we/passive preference is local advice, not universal journal policy; conflicts with UNC active-voice option are retained.')],mit_license,mit_reuse),
item('MANCHESTER_INTRODUCTION','Academic Phrasebank: Introducing work',
 'https://www.phrasebank.manchester.ac.uk/introducing-work/',
 'University of Manchester institutional Academic Phrasebank; its overview attributes CARS to John Swales (1990).',
 'manchester-introduction.txt','Full overview/CARS passage; full functional subsections Identifying a knowledge gap and Stating the purpose of the current research; relevant context/previous-research examples inspected, not every phrase category.',[
 passage('Overview before CARS','this is far from fixed or rigid, and not all the elements are present in all introductions.',
 'Introduction moves include context, a problem/niche and research purpose, but their presence/order varies. Phrase lists realize functions rather than supply evidence.',
 'Use rhetorical functions to diagnose missing reasoning, then write study-specific language from verified sources.',
 'Do not paste no/few-studies phrases without a literature search. CARS here is institutional explanation of Swales, not a fresh reading of his original monograph.')],unknown,unknown_reuse),
item('MANCHESTER_METHODS','Academic Phrasebank: Describing methods',
 'https://www.phrasebank.manchester.ac.uk/describing-methods/',
 'University of Manchester Academic Phrasebank institutional original page.',
 'manchester-methods.txt','Overview; complete categories current methodology, reasons adopted/rejected, established methods, selection/inclusion, infinitive purpose, statistical procedures and methodological problems/limitations.',[
 passage('Overview','clear and detailed enough for another experienced person to repeat the research and reproduce the results.',
 'Detail depends on method novelty, controversy and reader expertise; method descriptions include purpose, selection rules and reasons, not only actions.',
 'Describe why the design answers the scientific question and specify exclusions/selection factually where they alter inference.',
 'The simple-past observation applies to most example functional categories, not equations, definitions or all Methods sentences. Listed statistical phrases do not license unperformed tests.')],unknown,unknown_reuse),
item('MANCHESTER_TRANSITIONS','Academic Phrasebank: Signalling transition',
 'https://www.phrasebank.manchester.ac.uk/signalling-transition/',
 'University of Manchester Academic Phrasebank institutional original page.',
 'manchester-transitions.txt','Complete substantive overview and all transition/previewing categories; no linked PDF purchase.',[
 passage('Overview','It must be accurate, but it must be easy to follow.',
 'A preview or transition helps readers track movement between topics and sections; functions include contrast, return and summary.',
 'Select signposting only after identifying the actual relation between adjacent argument units.',
 'Thesis-style roadmaps and repeated section summaries are available options, not a requirement for every research-article paragraph.')],unknown,unknown_reuse),
item('UNC_PARAGRAPHS','Paragraphs',
 'https://writingcenter.unc.edu/tips-and-tools/paragraphs/',
 'University of North Carolina at Chapel Hill Writing Center, College of Arts and Sciences.',
 'unc-paragraphs.txt','Complete substantive handout: definition, thesis/control, organization options, five-step illustration, all troubleshooting sections and reuse footer.',[
 passage('What is a paragraph?','Length and appearance do not determine whether a section in a paper is a paragraph.',
 'Unity/coherence around a controlling idea, adequate evidence and explanation define a paragraph; completion can be a conclusion or transition.',
 'Reverse-outline each paragraph by its inference and supporting evidence, then remove or relocate unrelated claims.',
 'The five-step illustration is an example, not five sentences; the topic sentence can occur later; do not force every paragraph to end with a gap or summary.')],unc_license,unc_reuse),
item('UNC_TRANSITIONS','Transitions',
 'https://writingcenter.unc.edu/tips-and-tools/transitions/',
 'University of North Carolina at Chapel Hill Writing Center, College of Arts and Sciences.',
 'unc-transitions.txt','Complete substantive handout: logical function, diagnosis, organization/reverse outline, mechanics, transition types and relation table, footer.',[
 passage('How transitions work','Transitions cannot substitute for good organization',
 'Transitions expose relations already built into the argument. Diagnose organization before adding however/therefore or roadmaps.',
 'Write the relation in plain words; if no relation can be named, reorder or repair the reasoning first.',
 'Connectors can introduce unjustified causal/contrast claims. There is no requirement to insert a connector in every paragraph.')],unc_license,unc_reuse),
item('UNC_SCIENTIFIC_STYLE','Scientific Writing',
 'https://writingcenter.unc.edu/tips-and-tools/sciences/',
 'University of North Carolina at Chapel Hill Writing Center, College of Arts and Sciences.',
 'unc-sciences.txt','Complete substantive handout: precision, word choice, detail, quantification, clarity, sentence structure, verbosity, objectivity/voice and limitations; footer.',[
 passage('Word and phrasing choice','repetition is preferable to ambiguity.',
 'Choose terms for their precise scientific meaning, keep subjects and actions legible, include necessary details and avoid unsupported generalization.',
 'Check title noun relationships and collocations against their intended physical meaning; keep stable terms rather than decorative synonyms.',
 'Its sentence/preposition rules are heuristics, not automatic thresholds. Objective claims depend on evidence and scope, not passive voice.'),
 passage('Passive voice','Currently, the active voice is preferred in most scientific fields',
 'Active voice can be clear and acceptable; editorial preferences vary. Passive can be useful but may become awkward.',
 'Choose the grammatical subject to clarify the scientific action; never invent what an author did, and do not equate we with subjectivity.',
 'This statement is writing-center advice, not a verified present-day survey of every journal; check the actual target requirement.')],unc_license,unc_reuse),
item('PLOS_STRUCTURE','Ten simple rules for structuring papers',
 'https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619',
 'Brett Mensh and Konrad Kording, PLOS Computational Biology 13(9):e1005619 (2017); publisher original scholarly advice article; DOI10.1371/journal.pcbi.1005619.',
 'plos-structure.txt','Overview, Introduction, full Rules1–10 and Discussion; relevant Figure1/Table1 captions in text; image pixels not inspected; linked correction not substantively read.',[
 passage('Rule 1','make the claim and/or model as simple as the data and logic can support but no simpler.',
 'A central contribution focuses title and whole paper; complexity should follow evidence, and one contribution can be multifaceted.',
 'Write a contribution sentence and trace it to comparisons, figures and limits before revising prose.',
 'Central contribution need not be improved accuracy or a new algorithm. This advice is not the target journal author guide.'),
 passage('Rule 7','Every scientific argument has its own particular logical structure',
 'Results form a sequence of evidence-supported statements, not a chronology of work; negative/hypothesis-disproving findings can advance the argument.',
 'Select result units by what question they answer and connect them to the central contribution.',
 'CCC and gap-ending paragraphs are advocated defaults, not universal paragraph templates. No fixed title/abstract numbers or paragraph counts follow.')],
 'Article explicitly CC BY; unrestricted use/distribution/reproduction with author/source credit.',
 'Brief quotation and attributed paraphrase are used; an adapted scheme must be labeled our adaptation. Pedagogy references belong to guidance, not the study bibliography.', 'scholarly writing-advice article'),
item('USC_TITLE','Choosing a Title — Organizing Your Social Sciences Research Paper',
 'https://libguides.usc.edu/writingguide/title',
 'University of Southern California Libraries Research Guide. Institutional authored/curated teaching page, drawing on cited writing literature; not those cited originals themselves.',
 'usc-title-fetch.txt','Complete substantive Definition, Importance, Structure and Writing Style, Working/Final Title and Subtitle sections; page shows Last Updated Sep29,2026; linked references not read.',[
 passage('The Final Title','Indicate accurately the subject and scope of the study',
 'Titles should identify the research focus/scope and use current field nomenclature; subtitles can qualify context or method.',
 'Test each modifier and relational phrase for a supported meaning; distinguish topic, relationship and scope before removing words.',
 'The 5–12 substantive-word suggestion, capitalization and social-science examples are conventions of this guide, not universal requirements. Its flexible title-form advice does not excuse ambiguity or unsupported causality.')],
 'Page footer © University of Southern California; no explicit open license observed.',unknown_reuse)
]

out=dict(task='R4_PRIMARY_WRITING_GUIDANCE',date=DATE,scope='Generalized writing pedagogy; distinct from R3 manuscript review and manuscript research bibliography.',
 core_source_count=len(sources),origin_groups=['MIT/Broad/CEE','University of Manchester','UNC Chapel Hill','PLOS scholarly article','USC Libraries'],
 sources=sources,
 access_gaps=[
 dict(target='Harvard Writing Center Transitions/Anatomy of a Body Paragraph',status='403 from direct requests; fetch service declined because robots retrieval403. Not read; not used or counted. UNC complete originals cover paragraph/cohesion needs.'),
 dict(target='Gopen & Swan (1990) The Science of Scientific Writing',status='American Scientist publisher URL503/proxy failure; guessed Duke/source-PDF URLs404. Author current site identifies the article but does not supply its full original text. No original Gopen/Swan reading claimed; its ideas are not attributed from an unread original.'),
 dict(target='MIT standalone Journal Article Title guessed paths',status='404 via fetch. Title guidance actually read in MIT CEE Journal Article, exact URL retained. Direct requests to MIT pages403; fetch tool succeeded for the listed substantive originals.')],
 local_methods_separate_from_primary_sources=[
 dict(path='C:/Users/Administrator/.codex/skills/research-workflow-governor/SKILL.md',use='Bound task, preserve evidence and return promptly; not institutional pedagogy.'),
 dict(path='C:/Users/Administrator/.codex/skills/research-workflow-governor/references/journal-and-claims.md',use='Separate journal rules/heuristics and claim scope; operational method.'),
 dict(path='C:/Users/Administrator/.codex/skills/research-paper-writing/SKILL.md',use='Reverse outline and claim/evidence check; global template instructions refined against source variability.'),
 dict(path='C:/Users/Administrator/.codex/skills/research-paper-writing/references/abstract.md',use='Section drafting questions; challenge/advantage templates are not imposed on negative findings.'),
 dict(path='C:/Users/Administrator/.codex/skills/paper-spine/references/editorial-completeness.md',use='Previously read R3; actual paragraphs and discussion do new work, no quotas.'),
 dict(path='C:/Users/Administrator/.codex/skills/paper-spine/references/assertive-scientific-writing.md',use='Previously read R3; evidence-calibrated assertion and consequential limits.')],
 reuse_policy='Full-source extracts are local reading records only. Public/shared agent guidance consists of independently written synthesis, minimal attributed quotations, locators and links. Do not copy the full guide collection into a reusable product. Source licenses remain source-specific; no blanket relicensing is claimed.',
 result_kind='editorial/pedagogical synthesis; no new study result, source citation count or physical validation claim')
(ROOT/'source-ledger.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Wrote {len(sources)} substantive sources from {len(out["origin_groups"])} origins; short quotes located in saved originals.')
