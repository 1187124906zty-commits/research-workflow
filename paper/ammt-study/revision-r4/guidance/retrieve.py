from pathlib import Path
from html.parser import HTMLParser
import concurrent.futures
import json
import requests

ROOT = Path(__file__).resolve().parent
(ROOT / 'sources').mkdir(exist_ok=True)

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.text = []
        self.links = []
        self.title = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style', 'nav', 'header', 'footer'}:
            self.skip += 1
        if tag == 'title':
            self.in_title = True
        if tag in {'p','h1','h2','h3','h4','li','div','section','br'}:
            self.text.append('\n')
        if tag == 'a':
            self.links.extend(v for k, v in attrs if k == 'href')

    def handle_endtag(self, tag):
        if tag in {'script', 'style', 'nav', 'header', 'footer'}:
            self.skip = max(0, self.skip - 1)
        if tag == 'title':
            self.in_title = False
        if tag in {'p','h1','h2','h3','h4','li','div','section'}:
            self.text.append('\n')

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if not self.skip:
            self.text.append(data)

URLS = {
    'mit-title': 'https://mitcommlab.mit.edu/broad/commkit/journal-article-title/',
    'mit-abstract': 'https://mitcommlab.mit.edu/broad/commkit/journal-article-abstract/',
    'mit-introduction': 'https://mitcommlab.mit.edu/broad/commkit/journal-article-introduction/',
    'mit-methods': 'https://mitcommlab.mit.edu/broad/commkit/journal-article-methods/',
    'manchester-introduction': 'https://www.phrasebank.manchester.ac.uk/introducing-work/',
    'manchester-methods': 'https://www.phrasebank.manchester.ac.uk/describing-methods/',
    'manchester-transitions': 'https://www.phrasebank.manchester.ac.uk/signalling-transition/',
    'harvard-paragraph': 'https://writingcenter.fas.harvard.edu/anatomy-body-paragraph',
    'harvard-transitions': 'https://writingcenter.fas.harvard.edu/transitions',
    'gopen-swan': 'https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing',
    'plos-structure': 'https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619',
}

def retrieve(item):
    key, url = item
    record = {'id': key, 'requested_url': url}
    try:
        response = requests.get(url, timeout=40)
        ctype = response.headers.get('Content-Type','')
        record.update(resolved_url=response.url, status=response.status_code, content_type=ctype)
        if 'html' in ctype:
            parser = TextParser()
            parser.feed(response.text)
            text = '\n'.join(line.strip() for line in ''.join(parser.text).splitlines() if line.strip())
            (ROOT/'sources'/f'{key}.txt').write_text(text,encoding='utf-8')
            record.update(title=''.join(parser.title),text_chars=len(text),links=parser.links)
        else:
            (ROOT/'sources'/f'{key}.bin').write_bytes(response.content)
    except Exception as exc:
        record['error'] = str(exc)
    return record

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        records = list(pool.map(retrieve, URLS.items()))
    (ROOT/'retrieval.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps([{k:v for k,v in item.items() if k!='links'} for item in records],ensure_ascii=True,indent=2))
