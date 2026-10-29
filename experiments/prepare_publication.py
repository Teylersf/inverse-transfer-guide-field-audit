"""Prepare a science-preserving venue adapter; no network or credentials."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'submissions'
OUT.mkdir(exist_ok=True)
raw=(ROOT/'paper/manuscript.md').read_bytes()
body=raw.decode('utf-8')
title=body.splitlines()[0].removeprefix('# ')
version=re.search(r'^Version ([0-9.]+);',body,re.M).group(1)
abstract=re.search(r'^## Abstract\n\n(.*?)(?=\n## 1\.)',body,re.M|re.S).group(1).strip()
snapshot=json.loads((OUT/'computational-snapshot.json').read_text(encoding='utf-8'))
assert snapshot.get('code_doi')=='10.5281/zenodo.23779360'
pin=snapshot['computational_commit']
repo='https://github.com/Teylersf/inverse-transfer-guide-field-audit'
adapted=re.sub(r'^## Abstract\n\n.*?(?=\n## 1\.)','',body,count=1,flags=re.M|re.S)
adapted=adapted.replace('../figures/','https://raw.githubusercontent.com/Teylersf/inverse-transfer-guide-field-audit/'+pin+'/figures/')
assert adapted.count('## Abstract')==0 and adapted.count('## References\n')==1
meta=dict(title=title,abstract=abstract,author='Taylor Kalin',orcid='0009-0003-9000-9315',
    version=version,scientific_code_commit=pin,code_doi=snapshot['code_doi'],repository=repo,
    agentpub_paper_type='short_communication',
    keywords=['magnetic reconnection','guide field','inverse energy transfer','CGL model','pressure anisotropy','reproducibility'])
(OUT/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
(OUT/'manuscript.md').write_text(adapted,encoding='utf-8',newline='\n')
sha=lambda x:hashlib.sha256(x).hexdigest()
receipt=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),canonical_markdown_sha256=sha(raw),
    submitted_body_sha256=sha(adapted.encode()),abstract_sha256=sha(abstract.encode()),
    transformations=['Remove duplicate body abstract; supply its identical text as metadata.','Expand two relative figure URLs to immutable public computational-snapshot URLs.'],
    all_scientific_body_and_references_preserved=True,canonical_abstract_retained=True,
    references=len(re.findall(r'^\[\d+\]',body,re.M)))
(OUT/'publishfun-format-adapter.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print({'version':version,'references':receipt['references'],'abstract_words':len(abstract.split()),'body_characters':len(adapted)})
