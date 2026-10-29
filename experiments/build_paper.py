"""Assemble the audit and a portable LaTeX body; no scientific output changes."""
from pathlib import Path
import os
import re
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PAPER=ROOT/'paper'
names=['opening.md','source-and-model.md','scale-conversion.md','numerical-checks.md',
       'finite-guide-drive.md','equilibrium.md','discussion-and-closing.md']
parts=[]
for name in names:
    part=(PAPER/name).read_text(encoding='utf-8').strip()
    part=part.replace(r'\(', '$').replace(r'\)', '$')
    # Keep source typography portable across PDF and Markdown renderers.
    part=part.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
    parts.append(part)
text='\n\n'.join(parts)+'\n'
assert re.findall(r'^## (\d+)\.',text,re.M)==list(map(str,range(1,9)))
assert text.count('## Abstract\n')==1 and text.count('## References\n')==1
assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',text)
(PAPER/'manuscript.md').write_text(text,encoding='utf-8',newline='\n')
pandoc=os.environ.get('PANDOC') or shutil.which('pandoc')
if not pandoc:
    raise RuntimeError('Install Pandoc on PATH or set PANDOC to its executable.')
latex=PAPER/'latex'
latex.mkdir(exist_ok=True)
subprocess.run([pandoc,str(PAPER/'manuscript.md'),'-f',
    'markdown+tex_math_dollars+raw_tex+autolink_bare_uris-implicit_figures',
    '-t','latex','--no-highlight','-o',str(latex/'body.tex')],check=True)
body=(latex/'body.tex').read_text(encoding='utf-8').replace('../figures/','images/')
title=text.splitlines()[0].removeprefix('# ')
body=body.replace(r'\section{',r'\section['+title+r']{\raggedright ',1)
body=re.sub(r'\\texttt\{([^{}\n ]+)\}',lambda m:r'\nolinkurl{'+m[1].replace(r'\_','_')+'}',body)

def keep_table(match):
    value=match[0]
    # Pandoc supplies a width-bounded column specification for these small tables.
    value=value.replace(r'\begin{longtable}[]',r'\begin{tabular}')
    value=value.replace('\\endhead\n\\bottomrule\\noalign{}\n\\endlastfoot\n','')
    value=value.replace(r'\end{longtable}',r'\bottomrule\noalign{}'+'\n'+r'\end{tabular}')
    return '\n'+r'\begin{minipage}{\linewidth}\small'+'\n'+value+'\n'+r'\end{minipage}'+'\n'

body,count=re.subn(r'\\begin\{longtable\}.*?\\end\{longtable\}',keep_table,body,flags=re.S)
assert count==2,count
heading=r'\subsection{References}\label{references}'
assert body.count(heading)==1
body=body.replace(heading,r'\clearpage'+'\n'+heading)
(latex/'body.tex').write_text(body,encoding='utf-8',newline='\n')
(latex/'images').mkdir(exist_ok=True)
for image in (ROOT/'figures').glob('*.png'):
    shutil.copy2(image,latex/'images'/image.name)
print({'words_regex':len(re.findall(r'\b[\w-]+\b',text)),
       'body_words_before_references':len(re.findall(r'\b[\w-]+\b',text.split('## References')[0])),
       'characters':len(text),'tables':count})
