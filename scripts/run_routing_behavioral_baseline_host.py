#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, shlex, shutil, subprocess, sys
from pathlib import Path

EXPECTED_BRANCH='architecture-review-routing-v2'
MODEL='gpt-5.6-sol'
EFFORT='high'
ARCHS=('current','current_plus_map')
CONTROL={
'LAYER1_CONTRACT.md','FORMALIFE_REBUILD_PROTOCOL.md','MERENDA_MODE.md',
'merenda/DECISION_ROUTER.md','merenda/00_fondamenti/sistema-operativo-merenda.md'}

READER=r'''#!/usr/bin/env python3
import argparse,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def safe(rel):
 p=(ROOT/rel).resolve()
 if p!=ROOT and ROOT not in p.parents: raise SystemExit('path escapes workspace')
 if not p.is_file(): raise SystemExit(f'not a file: {rel}')
 return p

def slug(s):
 s=s.strip().lower(); s=re.sub(r'[^\w\s\-]','',s,flags=re.UNICODE); s=re.sub(r'\s+','-',s); return re.sub(r'-+','-',s).strip('-')

def text(rel): return safe(rel).read_text(encoding='utf-8')

def main():
 ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
 p=sub.add_parser('list'); p.add_argument('prefix',nargs='?',default='.')
 p=sub.add_parser('headings'); p.add_argument('path')
 p=sub.add_parser('read'); p.add_argument('path')
 p=sub.add_parser('section'); p.add_argument('path'); p.add_argument('anchor')
 a=ap.parse_args()
 if a.cmd=='list':
  base=(ROOT/a.prefix).resolve()
  if base!=ROOT and ROOT not in base.parents: raise SystemExit('prefix escapes workspace')
  for p in sorted(x for x in base.rglob('*') if x.is_file() and x.name!='EVAL_READER.py'):
   rel=p.relative_to(ROOT).as_posix()
   if not rel.startswith('.git/') and '/__pycache__/' not in f'/{rel}/': print(rel)
 elif a.cmd=='headings':
  for line in text(a.path).splitlines():
   m=re.match(r'^(#{1,6})\s+(.+?)\s*$',line)
   if m: print(f'{len(m.group(1))}\t{slug(m.group(2))}\t{m.group(2)}')
 elif a.cmd=='read': print(text(a.path),end='')
 else:
  lines=text(a.path).splitlines(); start=None; level=None
  for i,line in enumerate(lines):
   m=re.match(r'^(#{1,6})\s+(.+?)\s*$',line)
   if m and slug(m.group(2))==a.anchor: start=i; level=len(m.group(1)); break
  if start is None: raise SystemExit(f'anchor not found: {a.anchor}')
  end=len(lines)
  for i in range(start+1,len(lines)):
   m=re.match(r'^(#{1,6})\s+(.+?)\s*$',lines[i])
   if m and len(m.group(1))<=level: end=i; break
  print('\n'.join(lines[start:end]))
if __name__=='__main__': main()
'''

COMMON='''Sei il modello sotto test in una routing evaluation isolata.

REGOLE CRITICHE:
- Hai UN SOLO caso e nessuna memoria di altri casi.
- Non usare web, MCP o conoscenza esterna come sostituto della repository.
- I gold/eval non sono presenti nel tuo ambiente. Non cercarli.
- Non modificare file.
- L'UNICO modo consentito per ispezionare la repository è:
  python3 EVAL_READER.py list [prefix]
  python3 EVAL_READER.py headings PATH
  python3 EVAL_READER.py read PATH
  python3 EVAL_READER.py section PATH ANCHOR
- Non eseguire nessun altro comando shell. Niente cat/sed/rg/grep/awk/head/tail/python -c, pipe o redirection.
- list non conta come retrieval; headings/read/section sì.
- Diagnostica il problema: non accomodare automaticamente la premessa del founder e non saltare gate a monte.

Devi leggere prima questi file del control plane:
- LAYER1_CONTRACT.md
- FORMALIFE_REBUILD_PROTOCOL.md
- MERENDA_MODE.md
- merenda/DECISION_ROUTER.md
- merenda/00_fondamenti/sistema-operativo-merenda.md
Poi recupera SOLO i nodi canonici specialistici realmente necessari.

Il runner ricostruirà retrieved_nodes/retrieved_sections dai comandi reali. Nel JSON finale lasciali come liste vuote.
Rispondi ESATTAMENTE con un singolo oggetto JSON valido, senza markdown o testo extra:
{"case_id":"...","architecture":"...","retrieved_nodes":[],"retrieved_sections":[],"classification":[],"decision_level":"","answer":"","trace_notes":""}
decision_level: outcome, market_customer, positioning, offer, proof_authority, demand_channel, acquisition, sales, delivery_retention, economics_capacity, expansion.'''

ARCH_PROMPT={
'current':'ARCHITETTURA=current. Usa solo il control plane corrente. La Retrieval Map non esiste nel tuo ambiente.',
'current_plus_map':'''ARCHITETTURA=current_plus_map. Puoi usare SOLO come metadata di navigazione:
- reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_SEED.json
- reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE3.json
- reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE4.json
- reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE5.json
La Map NON è dottrina: devi comunque aprire canonical path/anchor prima di usare un principio.'''}

READ_RE=re.compile(r"EVAL_READER\.py\s+(?P<op>headings|read|section)\s+(?P<path>[^\s\"']+|\"[^\"]+\"|'[^']+')(?:\s+(?P<anchor>[^\s\"']+|\"[^\"]+\"|'[^']+'))?")

def q(cmd): return ' '.join(shlex.quote(x) for x in cmd)
def run(cmd,cwd=None): print('+',q(cmd)); return subprocess.run(cmd,cwd=cwd,text=True,check=True)
def gout(repo,*a): return subprocess.check_output(['git',*a],cwd=repo,text=True).strip()
def unq(s): return s[1:-1] if s and len(s)>=2 and s[0]==s[-1] and s[0] in "'\"" else s

def prep(repo,base):
 branch=gout(repo,'branch','--show-current')
 if branch!=EXPECTED_BRANCH: raise SystemExit(f'ERRORE: branch {branch!r}; atteso {EXPECTED_BRANCH!r}')
 dirty=gout(repo,'status','--porcelain')
 if dirty: raise SystemExit('ERRORE: working tree non pulito:\n'+dirty)
 sha=gout(repo,'rev-parse','HEAD')
 for s in ('scripts/validate_project.py','scripts/validate_routing_evals.py','scripts/validate_retrieval_map.py'): run([sys.executable,s],repo)
 base.mkdir(parents=True,exist_ok=True); p=base/'routing-prompts.jsonl'
 run([sys.executable,'scripts/export_routing_eval_prompts.py','--out',str(p)],repo)
 rows=[json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
 forbidden={'required_nodes','required_checks','forbidden_shortcuts','optional_nodes'}
 for r in rows:
  if forbidden & r.keys(): raise SystemExit(f"ERRORE: prompt {r.get('case_id')} contaminato")
 return branch,sha,rows

def sterile(repo,dest,plus):
 if dest.exists(): shutil.rmtree(dest)
 shutil.copytree(repo,dest,ignore=shutil.ignore_patterns('.git','.codex','evals','reviews','__pycache__','*.pyc'))
 (dest/'EVAL_READER.py').write_text(READER,encoding='utf-8'); os.chmod(dest/'EVAL_READER.py',0o755)
 if plus:
  md=dest/'reviews'/'drafts'; md.mkdir(parents=True)
  maps=sorted(repo.glob('reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_*.json'))
  if len(maps)!=4: raise SystemExit(f'ERRORE: attesi 4 shard Map, trovati {len(maps)}')
  for x in maps: shutil.copy2(x,md/x.name)
 if (dest/'evals').exists(): raise SystemExit('ERRORE: gold presente nello workspace sterile')
 if not plus and (dest/'reviews').exists(): raise SystemExit('ERRORE: reviews presente in current')

def commands(events):
 out=[]
 for e in events:
  it=e.get('item')
  if e.get('type') in ('item.started','item.completed') and isinstance(it,dict) and it.get('type')=='command_execution':
   c=it.get('command')
   if isinstance(c,str) and c not in out: out.append(c)
 return out

def observed(cmds):
 nodes=[]; sections=[]
 for c in cmds:
  if 'EVAL_READER.py' not in c: raise RuntimeError(f'comando non consentito: {c}')
  if any(t in c for t in ('&&','||',';','$(','`',' > ',' >> ',' | ')): raise RuntimeError(f'chaining/redirection non consentito: {c}')
  m=READ_RE.search(c)
  if not m: continue
  path=unq(m.group('path')); anchor=unq(m.group('anchor')) if m.group('anchor') else None
  if path.startswith('merenda/') and path.endswith('.md') and path not in CONTROL:
   if path not in nodes: nodes.append(path)
   if m.group('op')=='section' and anchor:
    rec={'path':path,'anchor':anchor}
    if rec not in sections: sections.append(rec)
 return nodes,sections

def final_json(events):
 xs=[]
 for e in events:
  it=e.get('item')
  if e.get('type')=='item.completed' and isinstance(it,dict) and it.get('type')=='agent_message' and isinstance(it.get('text'),str): xs.append(it['text'])
 if not xs: raise RuntimeError('nessun agent_message finale')
 return json.loads(xs[-1].strip())

def one(root,case,arch,base):
 cid=case['case_id']; evp=base/'events'/arch/f'{cid}.jsonl'; stp=base/'stderr'/arch/f'{cid}.log'; trp=base/'traces'/arch/f'{cid}.json'
 if trp.exists() and evp.exists(): print(f'[RESUME] {arch}/{cid}'); return json.loads(trp.read_text(encoding='utf-8'))
 evp.parent.mkdir(parents=True,exist_ok=True); stp.parent.mkdir(parents=True,exist_ok=True); trp.parent.mkdir(parents=True,exist_ok=True)
 prompt=COMMON+'\n\n'+ARCH_PROMPT[arch]+'\n\nCASE ID:\n'+cid+'\n\nCASO DEL FOUNDER:\n'+case['prompt']
 cmd=['codex','-m',MODEL,'-c',f'model_reasoning_effort="{EFFORT}"','-c','web_search="disabled"','-c','agents.enabled=false','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','read-only','--cd',str(root),'--json',prompt]
 print(f'\n========== {arch} / {cid} ==========')
 p=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE); evp.write_text(p.stdout,encoding='utf-8'); stp.write_text(p.stderr,encoding='utf-8')
 if p.returncode: raise RuntimeError(f'{cid}/{arch}: codex exit {p.returncode}; vedi {stp}')
 events=[]
 for n,line in enumerate(p.stdout.splitlines(),1):
  if line.strip():
   try: events.append(json.loads(line))
   except json.JSONDecodeError as e: raise RuntimeError(f'{cid}/{arch}: stdout non JSONL riga {n}') from e
 nodes,sections=observed(commands(events)); t=final_json(events)
 if t.get('case_id')!=cid or t.get('architecture')!=arch: raise RuntimeError(f'{cid}/{arch}: identità trace errata')
 need={'case_id','architecture','retrieved_nodes','retrieved_sections','classification','decision_level','answer','trace_notes'}
 if need-t.keys(): raise RuntimeError(f'{cid}/{arch}: campi mancanti {sorted(need-t.keys())}')
 t['retrieved_nodes']=nodes; t['retrieved_sections']=sections; t['trace_notes']=(str(t.get('trace_notes') or '')+' | retrieval reconstructed from observed EVAL_READER commands').strip(' |')
 trp.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(f'[PASS] {arch}/{cid} nodes={len(nodes)} sections={len(sections)}')
 return t

def write_jsonl(p,rows): p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--workdir',type=Path,default=Path('/tmp/formalife-routing-baseline')); ap.add_argument('--case',action='append',dest='cases'); a=ap.parse_args()
 repo=Path.cwd().resolve(); branch,sha,prompts=prep(repo,a.workdir)
 if a.cases:
  want=set(a.cases); prompts=[p for p in prompts if p['case_id'] in want]
  miss=want-{p['case_id'] for p in prompts}
  if miss: raise SystemExit(f'ERRORE: case non trovati: {sorted(miss)}')
 roots={'current':a.workdir/'workspace-current','current_plus_map':a.workdir/'workspace-current-plus-map'}; sterile(repo,roots['current'],False); sterile(repo,roots['current_plus_map'],True)
 meta={'repository':'formalife/merenda-business-core','branch':branch,'commit_sha':sha,'model':MODEL,'reasoning_effort':EFFORT,'cases':[p['case_id'] for p in prompts],'isolation':'fresh codex exec process per case/configuration','gold_exposure':'physically absent','retrieval_instrumentation':'EVAL_READER command_execution'}
 (a.workdir/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
 traces={x:[] for x in ARCHS}
 try:
  for case in prompts:
   for arch in ARCHS: traces[arch].append(one(roots[arch],case,arch,a.workdir))
 except Exception as e:
  print(f'\nBASELINE STOPPED: {e}',file=sys.stderr); print('Nessuna metrica finale prodotta.',file=sys.stderr); return 2
 print('\n========== DETERMINISTIC SCORING ==========')
 summaries={}
 for arch in ARCHS:
  tp=a.workdir/f'{arch}-trace.jsonl'; sp=a.workdir/f'{arch}-score.json'; write_jsonl(tp,traces[arch]); run([sys.executable,'scripts/score_routing_run.py','--trace',str(tp),'--json-out',str(sp)],repo); summaries[arch]=json.loads(sp.read_text(encoding='utf-8'))['summary'][arch]
 (a.workdir/'deterministic-summary.json').write_text(json.dumps({'metadata':meta,'deterministic_summary':summaries},indent=2)+'\n',encoding='utf-8')
 print('\n==============================================\nBEHAVIORAL BASELINE — DETERMINISTIC PASS COMPLETE\n=============================================='); print('Commit testato:',sha)
 for arch in ARCHS:
  s=summaries[arch]; print(f"{arch}: cases={s['cases']} node_recall={s['mean_required_node_recall']:.4f} precision={s['mean_relevant_retrieval_precision']:.4f} over_retrieved={s['total_over_retrieved_nodes']}")
 print('Output locale:',a.workdir); print('Semantic judgment non eseguito: è il pass successivo sui trace congelati.'); return 0
if __name__=='__main__': raise SystemExit(main())
