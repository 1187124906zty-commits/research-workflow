from pathlib import Path
import concurrent.futures, json, requests, fitz

ROOT=Path(__file__).resolve().parent
for d in ['metadata','pdfs','text']:
    (ROOT/d).mkdir(exist_ok=True)
DOIS={
 'kollmannsberger2019':'10.1007/s40192-019-00132-9',
 'vanelsen2007':'10.1016/j.ijheatmasstransfer.2007.02.044',
 'coleman2024fixed':'10.1016/j.addma.2023.104011',
 'Plotkowski2017Rapid':'10.1016/j.addma.2017.10.017',
 'pottlacher2001':'10.1068/htwu340',
 'Hou2024Dissolution':'10.1016/j.addma.2024.104554',
}

def metadata(item):
    key,doi=item
    summary={'key':key,'doi':doi}
    for source,base in [('crossref','https://api.crossref.org/works/'),('openalex','https://api.openalex.org/works/https://doi.org/')]:
        try:
            r=requests.get(base+doi,timeout=30)
            data=r.json()
            (ROOT/'metadata'/f'{key}-{source}.json').write_text(json.dumps({'url':r.url,'status':r.status_code,'response':data},ensure_ascii=False,indent=2),encoding='utf-8')
            if source=='crossref':
                m=data['message']; summary.update(title=m['title'],journal=m.get('container-title'),date=m.get('published'),links=m.get('link'))
            else:
                summary.update(locations=[{'landing':l.get('landing_page_url'),'pdf':l.get('pdf_url')} for l in data.get('locations',[])],abstract=data.get('abstract_inverted_index'))
        except Exception as e: summary[source+'_error']=str(e)
    return summary

def download(key,url):
    try:
        r=requests.get(url,timeout=40)
        item={'key':key,'url':url,'final_url':r.url,'status':r.status_code,'type':r.headers.get('content-type'),'size':len(r.content),'pdf':r.content.startswith(b'%PDF')}
        if item['pdf']:
            path=ROOT/'pdfs'/f'{key}.pdf';path.write_bytes(r.content)
            doc=fitz.open(path)
            (ROOT/'text'/f'{key}.txt').write_text('\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
            item['pages']=len(doc)
        return item
    except Exception as e:return {'key':key,'url':url,'error':str(e)}

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        ms=list(pool.map(metadata,DOIS.items()))
    (ROOT/'metadata'/'verified-metadata-summary.json').write_text(json.dumps(ms,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps([{k:v for k,v in m.items() if k!='abstract'} for m in ms],ensure_ascii=False))
    urls=[('kollmannsberger2019','https://arxiv.org/pdf/1903.09076'),('specialmetals625','https://www.specialmetals.com/documents/technical-bulletins/inconel/inconel-alloy-625.pdf')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        ds=list(pool.map(lambda kv:download(*kv),urls))
    (ROOT/'metadata'/'retrieval-initial.json').write_text(json.dumps(ds,indent=2),encoding='utf-8')
    print(json.dumps(ds))
