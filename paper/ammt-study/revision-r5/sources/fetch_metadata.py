from pathlib import Path
import json
import requests
from concurrent.futures import ThreadPoolExecutor

DEST = Path(__file__).resolve().parent
DOIS = {
    'kollmannsberger2019': '10.1007/s40192-019-00132-9',
    'vanelsen2007': '10.1016/j.ijheatmasstransfer.2007.02.044',
    'lane2020': '10.1007/s40192-020-00169-1',
    'myers2023': '10.1016/j.addma.2023.103663',
    'dynamic2024': '10.1016/j.addma.2024.104531',
}

def fetch(item):
    key, doi = item
    try:
        r = requests.get('https://api.crossref.org/works/' + doi, timeout=25)
        r.raise_for_status()
        data = r.json()['message']
        (DEST / f'{key}-crossref.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        return {'key': key, 'doi': data['DOI'], 'title': data['title'], 'authors': data.get('author'), 'journal': data.get('container-title'), 'volume': data.get('volume'), 'pages': data.get('page'), 'article_number': data.get('article-number'), 'date': data.get('published')}
    except Exception as exc:
        return {'key': key, 'error': str(exc)}

with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fetch, DOIS.items()))
(DEST / 'verified-metadata.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
for record in results:
    print(json.dumps(record, ensure_ascii=False))

for label, url in [
    ('lane2020-original.html', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8194244/'),
    ('lane2020-original.xml', 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8194244/fullTextXML'),
]:
    try:
        r = requests.get(url, timeout=25)
        valid = r.status_code == 200 and ('Measurements of Melt Pool Geometry' in r.text or 'Measurements of melt pool geometry' in r.text)
        if valid:
            (DEST / label).write_text(r.text, encoding='utf-8')
        print(json.dumps({'url': url, 'status': r.status_code, 'valid_full_text': valid, 'bytes': len(r.content)}))
    except Exception as exc:
        print(json.dumps({'url': url, 'error': str(exc)}))
