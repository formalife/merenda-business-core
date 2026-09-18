#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

EXPECTED_BRANCH = "architecture-review-routing-v2"
MODEL = "gpt-5.6-sol"
EFFORT = "high"
ARCH = "prototype_a"
SMOKE_CASES = ("R002", "R008", "R019", "R020", "R027", "R030")
CONTROL = {
    "LAYER1_CONTRACT.md",
    "FORMALIFE_REBUILD_PROTOCOL.md",
    "MERENDA_MODE.md",
    "merenda/DECISION_ROUTER.md",
    "merenda/00_fondamenti/sistema-operativo-merenda.md",
}
ROOT_CONTROL = ("LAYER1_CONTRACT.md", "FORMALIFE_REBUILD_PROTOCOL.md", "MERENDA_MODE.md")
ALLOWED_OPS = {
    "list",
    "headings",
    "read",
    "section",
    "semantic_index",
    "semantic_entry",
    "search_headings",
    "structure",
}

READER = r'''#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
RETR=ROOT/'.retrieval'
HEADING_RE=re.compile(r'^(#{1,6})\s+(.+?)\s*$')
STOP={'che','con','del','della','delle','degli','dei','per','una','uno','gli','le','la','il','lo','un','di','da','in','e','o','a','al','alla','alle','ai','agli','nel','nella','nelle','non','piu','più','come','prima','dopo','quando','se','si','su'}

def slug(s):
 s=s.strip().lower(); s=re.sub(r'[^\w\s\-]','',s,flags=re.UNICODE); s=re.sub(r'\s+','-',s); return re.sub(r'-+','-',s).strip('-')

def norm_tokens(s):
 xs=re.findall(r'\w+',s.lower(),flags=re.UNICODE)
 return {x for x in xs if len(x)>=3 and x not in STOP}

def safe_doctrine(rel):
 p=(ROOT/rel).resolve()
 if p!=ROOT and ROOT not in p.parents: raise SystemExit('path escapes workspace')
 if rel.startswith('.retrieval/') or '/.retrieval/' in rel: raise SystemExit('direct retrieval-store reads are forbidden')
 if not p.is_file() or p.suffix.lower()!='.md': raise SystemExit(f'not a doctrine markdown file: {rel}')
 return p

def text(rel): return safe_doctrine(rel).read_text(encoding='utf-8')

def heading_rows(raw):
 out=[]; fenced=False
 for i,line in enumerate(raw.splitlines()):
  if line.lstrip().startswith('```'):
   fenced=not fenced; continue
  if fenced: continue
  m=HEADING_RE.match(line)
  if m: out.append((i,len(m.group(1)),slug(m.group(2)),m.group(2)))
 return out

def section_text(raw,anchor):
 lines=raw.splitlines(); rows=heading_rows(raw); start=None; level=None
 for i,lvl,a,title in rows:
  if a==anchor: start=i; level=lvl; break
 if start is None: raise SystemExit(f'anchor not found: {anchor}')
 end=len(lines)
 for i,lvl,a,title in rows:
  if i>start and lvl<=level: end=i; break
 return '\n'.join(lines[start:end])+'\n'

def sem(): return json.loads((RETR/'semantic-index-v2.json').read_text(encoding='utf-8'))
def struct(): return json.loads((RETR/'structural-index.json').read_text(encoding='utf-8'))

def find_doc(data,path):
 for d in data['documents']:
  if d['path']==path: return d
 raise SystemExit(f'structural path not found: {path}')

def main():
 ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
 p=sub.add_parser('list'); p.add_argument('prefix',nargs='?',default='.')
 p=sub.add_parser('headings'); p.add_argument('path')
 p=sub.add_parser('read'); p.add_argument('path')
 p=sub.add_parser('section'); p.add_argument('path'); p.add_argument('anchor')
 sub.add_parser('semantic_index')
 p=sub.add_parser('semantic_entry'); p.add_argument('semantic_id')
 p=sub.add_parser('search_headings'); p.add_argument('query',nargs='+')
 p=sub.add_parser('structure'); p.add_argument('path'); p.add_argument('anchor')
 a=ap.parse_args()
 if a.cmd=='list':
  base=(ROOT/a.prefix).resolve()
  if base!=ROOT and ROOT not in base.parents: raise SystemExit('prefix escapes workspace')
  for p in sorted(x for x in base.rglob('*') if x.is_file() and x.name!='EVAL_READER.py'):
   rel=p.relative_to(ROOT).as_posix()
   if rel.startswith('.retrieval/') or '/__pycache__/' in f'/{rel}/': continue
   print(rel)
 elif a.cmd=='headings':
  for i,lvl,anchor,title in heading_rows(text(a.path)): print(f'{lvl}\t{anchor}\t{title}')
 elif a.cmd=='read': print(text(a.path),end='')
 elif a.cmd=='section': print(section_text(text(a.path),a.anchor),end='')
 elif a.cmd=='semantic_index': print(sem()['compact_index_text'],end='')
 elif a.cmd=='semantic_entry':
  entries=sem()['entries']
  if a.semantic_id not in entries: raise SystemExit(f'unknown semantic id: {a.semantic_id}')
  print(json.dumps(entries[a.semantic_id],ensure_ascii=False,indent=2))
 elif a.cmd=='search_headings':
  query=' '.join(a.query); q=norm_tokens(query); data=struct(); scored=[]
  for d in data['documents']:
   for s in d['sections']:
    h=norm_tokens(s['heading']); hp=norm_tokens(' '.join(s['heading_path'])); pt=norm_tokens(d['path'].replace('/',' ').replace('-',' '))
    score=5*len(q & h)+3*len(q & hp)+2*len(q & pt)
    if query.lower() in s['heading'].lower(): score+=10
    if score>0: scored.append((score,d['path'],s['anchor'],' / '.join(s['heading_path'])))
  scored.sort(key=lambda x:(-x[0],x[1],x[2]))
  print('score\tpath\tanchor\theading_path')
  for score,path,anchor,hpath in scored[:12]: print(f'{score}\t{path}\t{anchor}\t{hpath}')
 elif a.cmd=='structure':
  data=struct(); d=find_doc(data,a.path); matches=[s for s in d['sections'] if s['anchor']==a.anchor]
  if not matches: raise SystemExit(f'structural anchor not found: {a.path}#{a.anchor}')
  byid={s['structural_id']:s for s in d['sections']}; out=[]
  for s in matches:
   rec=dict(s); pid=s.get('parent_structural_id'); rec['parent']=byid.get(pid) if pid else None
   rec['children']=[byid[x] for x in s.get('children_structural_ids',[]) if x in byid]
   out.append(rec)
  print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
'''

COMMON = '''Sei il modello sotto test in una routing evaluation isolata.

REGOLE CRITICHE:
- Hai UN SOLO caso e nessuna memoria di altri casi.
- Non usare web, MCP o conoscenza esterna come sostituto della repository.
- Gold/eval/review non sono presenti nel tuo ambiente. Non cercarli.
- Non modificare file.
- L'UNICO modo consentito per ispezionare la repository è:
  python3 EVAL_READER.py list [prefix]
  python3 EVAL_READER.py headings PATH
  python3 EVAL_READER.py read PATH
  python3 EVAL_READER.py section PATH ANCHOR
  python3 EVAL_READER.py semantic_index
  python3 EVAL_READER.py semantic_entry SEMANTIC_ID
  python3 EVAL_READER.py search_headings QUERY
  python3 EVAL_READER.py structure PATH ANCHOR
- Non eseguire nessun altro comando shell. Niente cat/sed/rg/grep/awk/head/tail/python -c, pipe o redirection.
- Diagnostica il problema: non accomodare automaticamente la premessa del founder e non saltare gate a monte.

CONTROL PLANE FISSO — devi leggere prima integralmente:
- LAYER1_CONTRACT.md
- FORMALIFE_REBUILD_PROTOCOL.md
- MERENDA_MODE.md
- merenda/DECISION_ROUTER.md
- merenda/00_fondamenti/sistema-operativo-merenda.md

ARCHITETTURA=prototype_a.
Dopo il control plane:
1. Usa `semantic_index` come mappa compatta. È metadata di navigazione, NON dottrina.
2. Scegli il minor numero plausibile di semantic ID e usa `semantic_entry ID` solo per quelli realmente candidati.
3. Un semantic entry non autorizza una conclusione: devi leggere il contenuto canonico indicato. Se ha `canonical.anchor`, preferisci `section PATH ANCHOR`.
4. Se l'entry non ha anchor, usa `headings PATH` e recupera la sezione minima sufficiente; usa `read PATH` completo solo quando la decisione dipende realmente da più sezioni o da caveat non localizzabili.
5. Controlla gli `upstream` quando la decisione dipende da essi; non caricare automaticamente tutti i `related` o `must_read_with` se la loro condizione non è vera.
6. Se l'indice semantico sembra insufficiente o sospetti un blind spot, usa `search_headings QUERY` come recall safety net. Poi apri la sezione canonica trovata. `structure PATH ANCHOR` serve solo per decidere se espandere a parent/child context.
7. Progressive disclosure: sezione minima → contesto parent/local solo se insufficiente → full node come fallback finale.
8. Provenance e supersession vanno preservate quando pertinenti.

Il runner ricostruirà retrieval e semantic IDs dai comandi reali. Nel JSON finale lascia vuote tutte le liste `retrieved_*` e `*_semantic_units`.
Rispondi ESATTAMENTE con un singolo oggetto JSON valido, senza markdown o testo extra:
{"case_id":"...","architecture":"prototype_a","retrieved_nodes":[],"retrieved_sections":[],"selected_semantic_units":[],"verified_semantic_units":[],"classification":[],"decision_level":"","answer":"","trace_notes":""}
decision_level: outcome, market_customer, positioning, offer, proof_authority, demand_channel, acquisition, sales, delivery_retention, economics_capacity, expansion.'''


def q(cmd: list[str]) -> str:
    return " ".join(shlex.quote(x) for x in cmd)


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print("+", q(cmd))
    subprocess.run(cmd, cwd=cwd, text=True, check=True)


def gout(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def prep(repo: Path, base: Path) -> tuple[str, str, list[dict], Path, Path]:
    branch = gout(repo, "branch", "--show-current")
    if branch != EXPECTED_BRANCH:
        raise SystemExit(f"ERRORE: branch {branch!r}; atteso {EXPECTED_BRANCH!r}")
    dirty = gout(repo, "status", "--porcelain")
    if dirty:
        raise SystemExit("ERRORE: working tree non pulito:\n" + dirty)
    sha = gout(repo, "rev-parse", "HEAD")
    for script in (
        "scripts/validate_project.py",
        "scripts/validate_routing_evals.py",
        "scripts/validate_retrieval_map.py",
        "scripts/validate_semantic_gold_v2.py",
    ):
        run([sys.executable, script], repo)

    base.mkdir(parents=True, exist_ok=True)
    prompt_path = base / "routing-prompts.jsonl"
    run([sys.executable, "scripts/export_routing_eval_prompts.py", "--out", str(prompt_path)], repo)
    prompts = [json.loads(x) for x in prompt_path.read_text(encoding="utf-8").splitlines() if x.strip()]
    forbidden = {
        "required_nodes",
        "required_checks",
        "forbidden_shortcuts",
        "optional_nodes",
        "required_semantic_units",
        "optional_semantic_units",
    }
    for row in prompts:
        if forbidden & row.keys():
            raise SystemExit(f"ERRORE: prompt {row.get('case_id')} contaminato")

    generated = base / "generated"
    generated.mkdir(parents=True, exist_ok=True)
    sem_json = generated / "semantic-index-v2.json"
    sem_txt = generated / "semantic-index-v2.txt"
    struct_json = generated / "structural-index.json"
    struct_md = generated / "structural-index.md"
    run(
        [
            sys.executable,
            "scripts/build_compact_semantic_index.py",
            "--json-out",
            str(sem_json),
            "--txt-out",
            str(sem_txt),
        ],
        repo,
    )
    run(
        [
            sys.executable,
            "scripts/build_structural_index.py",
            "--json-out",
            str(struct_json),
            "--md-out",
            str(struct_md),
        ],
        repo,
    )
    sem_data = json.loads(sem_json.read_text(encoding="utf-8"))
    if sem_data.get("gold_linkage_exposed") is not False:
        raise SystemExit("ERRORE: semantic runtime store espone gold linkage")
    return branch, sha, prompts, sem_json, struct_json


def sterile(repo: Path, dest: Path, sem_json: Path, struct_json: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    for rel in ROOT_CONTROL:
        shutil.copy2(repo / rel, dest / rel)
    shutil.copytree(repo / "merenda", dest / "merenda")
    retr = dest / ".retrieval"
    retr.mkdir()
    shutil.copy2(sem_json, retr / "semantic-index-v2.json")
    shutil.copy2(struct_json, retr / "structural-index.json")
    (dest / "EVAL_READER.py").write_text(READER, encoding="utf-8")
    os.chmod(dest / "EVAL_READER.py", 0o755)
    forbidden = (dest / "evals", dest / "reviews", dest / "STATUS.md")
    if any(path.exists() for path in forbidden):
        raise SystemExit("ERRORE: gold/review/status presente nello workspace sterile")


def completed_command_items(events: list[dict]) -> list[dict]:
    out: list[dict] = []
    seen: set[str] = set()
    for event in events:
        item = event.get("item")
        if event.get("type") != "item.completed" or not isinstance(item, dict):
            continue
        if item.get("type") != "command_execution" or not isinstance(item.get("command"), str):
            continue
        command = item["command"]
        exit_code = item.get("exit_code")
        if isinstance(exit_code, int) and exit_code != 0:
            continue
        if command not in seen:
            seen.add(command)
            out.append(item)
    return out


def reader_argv(command: str) -> list[str]:
    if "EVAL_READER.py" not in command:
        raise RuntimeError(f"comando non consentito: {command}")
    if any(token in command for token in ("&&", "||", ";", "$(`", "`", " > ", " >> ", " | ")):
        raise RuntimeError(f"chaining/redirection non consentito: {command}")
    pos = command.index("EVAL_READER.py") + len("EVAL_READER.py")
    tail = command[pos:].strip()
    if tail.endswith("'") or tail.endswith('"'):
        tail = tail[:-1].rstrip()
    try:
        argv = shlex.split(tail)
    except ValueError as exc:
        raise RuntimeError(f"cannot parse reader command: {command}") from exc
    if not argv or argv[0] not in ALLOWED_OPS:
        raise RuntimeError(f"reader op non consentita: {command}")
    op = argv[0]
    valid = (
        (op == "list" and len(argv) in (1, 2))
        or (op in ("headings", "read", "semantic_entry") and len(argv) == 2)
        or (op in ("section", "structure") and len(argv) == 3)
        or (op == "semantic_index" and len(argv) == 1)
        or (op == "search_headings" and len(argv) >= 2)
    )
    if not valid:
        raise RuntimeError(f"reader argv non valido: {argv}")
    return argv


def reader_payload(root: Path, argv: list[str]) -> str:
    cmd = [sys.executable, str(root / "EVAL_READER.py"), *argv]
    return subprocess.check_output(cmd, cwd=root, text=True)


def load_runtime_entries(root: Path) -> dict[str, dict]:
    data = json.loads((root / ".retrieval" / "semantic-index-v2.json").read_text(encoding="utf-8"))
    return data["entries"]


def classify_context(op: str, argv: list[str]) -> str:
    if op in ("semantic_index", "semantic_entry"):
        return "routing_metadata"
    if op in ("search_headings", "structure", "headings", "list"):
        return "structural_metadata"
    path = argv[1] if len(argv) > 1 else ""
    if path in CONTROL:
        return "control_plane"
    if path.startswith("merenda/"):
        return "specialist_doctrine"
    return "other"


def observed(root: Path, command_items: list[dict]) -> dict:
    entries = load_runtime_entries(root)
    nodes: list[str] = []
    sections: list[dict] = []
    selected: list[str] = []
    full_reads: set[str] = set()
    section_pairs: set[tuple[str, str]] = set()
    ops: list[dict] = []
    category_chars: dict[str, int] = defaultdict(int)
    category_words: dict[str, int] = defaultdict(int)

    for item in command_items:
        command = item["command"]
        argv = reader_argv(command)
        op = argv[0]
        payload = reader_payload(root, argv)
        chars = len(payload)
        words = len(payload.split())
        category = classify_context(op, argv)
        category_chars[category] += chars
        category_words[category] += words
        ops.append({"op": op, "argv": argv[1:], "category": category, "chars": chars, "words": words})

        if op == "semantic_entry":
            sid = argv[1]
            if sid not in selected:
                selected.append(sid)
        elif op == "read":
            path = argv[1]
            full_reads.add(path)
            if path.startswith("merenda/") and path not in CONTROL and path not in nodes:
                nodes.append(path)
        elif op == "section":
            path, anchor = argv[1], argv[2]
            section_pairs.add((path, anchor))
            if path.startswith("merenda/") and path not in CONTROL and path not in nodes:
                nodes.append(path)
            rec = {"path": path, "anchor": anchor}
            if path.startswith("merenda/") and path not in CONTROL and rec not in sections:
                sections.append(rec)

    verified: set[str] = set()
    for sid, entry in entries.items():
        canonical = entry.get("canonical") or {}
        path = canonical.get("path")
        anchor = canonical.get("anchor")
        if not isinstance(path, str):
            continue
        if path in full_reads:
            verified.add(sid)
        elif isinstance(anchor, str) and (path, anchor) in section_pairs:
            verified.add(sid)
        elif anchor is None and sid in selected and any(p == path for p, _ in section_pairs):
            verified.add(sid)

    stats = {
        "semantic_index_reads": sum(x["op"] == "semantic_index" for x in ops),
        "semantic_entry_reads": sum(x["op"] == "semantic_entry" for x in ops),
        "structural_searches": sum(x["op"] == "search_headings" for x in ops),
        "structure_reads": sum(x["op"] == "structure" for x in ops),
        "headings_reads": sum(x["op"] == "headings" for x in ops),
        "section_reads": sum(x["op"] == "section" and x["category"] == "specialist_doctrine" for x in ops),
        "full_node_reads": sum(
            x["op"] == "read" and x["category"] in ("specialist_doctrine", "other") for x in ops
        ),
        "control_reads": sum(x["op"] == "read" and x["category"] == "control_plane" for x in ops),
        "operation_chars": sum(x["chars"] for x in ops),
        "operation_words": sum(x["words"] for x in ops),
        "category_chars": dict(category_chars),
        "category_words": dict(category_words),
    }
    return {
        "retrieved_nodes": nodes,
        "retrieved_sections": sections,
        "selected_semantic_units": selected,
        "verified_semantic_units": sorted(verified),
        "retrieval_stats": stats,
        "retrieval_operations": ops,
    }


def final_json(events: list[dict]) -> dict:
    messages: list[str] = []
    for event in events:
        item = event.get("item")
        if event.get("type") == "item.completed" and isinstance(item, dict):
            if item.get("type") == "agent_message" and isinstance(item.get("text"), str):
                messages.append(item["text"])
    if not messages:
        raise RuntimeError("nessun agent_message finale")
    return json.loads(messages[-1].strip())


def one(root: Path, case: dict, base: Path) -> dict:
    cid = case["case_id"]
    evp = base / "events" / ARCH / f"{cid}.jsonl"
    stp = base / "stderr" / ARCH / f"{cid}.log"
    trp = base / "traces" / ARCH / f"{cid}.json"
    if trp.exists() and evp.exists():
        print(f"[RESUME] {ARCH}/{cid}")
        return json.loads(trp.read_text(encoding="utf-8"))
    evp.parent.mkdir(parents=True, exist_ok=True)
    stp.parent.mkdir(parents=True, exist_ok=True)
    trp.parent.mkdir(parents=True, exist_ok=True)
    prompt = COMMON + "\n\nCASE ID:\n" + cid + "\n\nCASO DEL FOUNDER:\n" + case["prompt"]
    cmd = [
        "codex",
        "-m",
        MODEL,
        "-c",
        f'model_reasoning_effort="{EFFORT}"',
        "-c",
        'web_search="disabled"',
        "-c",
        "agents.enabled=false",
        "exec",
        "--ignore-user-config",
        "--ephemeral",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--cd",
        str(root),
        "--json",
        prompt,
    ]
    print(f"\n========== {ARCH} / {cid} ==========")
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    evp.write_text(proc.stdout, encoding="utf-8")
    stp.write_text(proc.stderr, encoding="utf-8")
    if proc.returncode:
        raise RuntimeError(f"{cid}/{ARCH}: codex exit {proc.returncode}; vedi {stp}")
    events: list[dict] = []
    for lineno, line in enumerate(proc.stdout.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{cid}/{ARCH}: stdout non JSONL riga {lineno}") from exc
    observed_data = observed(root, completed_command_items(events))
    trace = final_json(events)
    if trace.get("case_id") != cid or trace.get("architecture") != ARCH:
        raise RuntimeError(f"{cid}/{ARCH}: identità trace errata")
    needed = {
        "case_id",
        "architecture",
        "retrieved_nodes",
        "retrieved_sections",
        "selected_semantic_units",
        "verified_semantic_units",
        "classification",
        "decision_level",
        "answer",
        "trace_notes",
    }
    missing = needed - trace.keys()
    if missing:
        raise RuntimeError(f"{cid}/{ARCH}: campi mancanti {sorted(missing)}")
    trace.update(observed_data)
    trace["trace_notes"] = (
        str(trace.get("trace_notes") or "")
        + " | retrieval reconstructed from completed EVAL_READER commands"
    ).strip(" |")
    trp.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"[PASS] {ARCH}/{cid} semantic_selected={len(trace['selected_semantic_units'])} "
        f"semantic_verified={len(trace['verified_semantic_units'])} sections={len(trace['retrieved_sections'])} "
        f"full_nodes={trace['retrieval_stats']['full_node_reads']} chars={trace['retrieval_stats']['operation_chars']}"
    )
    return trace


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def context_summary(traces: list[dict]) -> dict:
    if not traces:
        return {}
    categories = ("control_plane", "routing_metadata", "structural_metadata", "specialist_doctrine", "other")
    return {
        "cases": len(traces),
        "mean_operation_chars": mean(t["retrieval_stats"]["operation_chars"] for t in traces),
        "mean_operation_words": mean(t["retrieval_stats"]["operation_words"] for t in traces),
        "mean_full_node_reads": mean(t["retrieval_stats"]["full_node_reads"] for t in traces),
        "mean_section_reads": mean(t["retrieval_stats"]["section_reads"] for t in traces),
        "mean_semantic_entry_reads": mean(t["retrieval_stats"]["semantic_entry_reads"] for t in traces),
        "mean_structural_searches": mean(t["retrieval_stats"]["structural_searches"] for t in traces),
        "mean_category_chars": {
            c: mean(t["retrieval_stats"]["category_chars"].get(c, 0) for t in traces) for c in categories
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", type=Path, default=Path("/tmp/formalife-hierarchical-prototype-a"))
    ap.add_argument("--case", action="append", dest="cases")
    ap.add_argument("--smoke", action="store_true", help="Run the six high-information smoke cases only.")
    args = ap.parse_args()
    if args.smoke and args.cases:
        raise SystemExit("ERRORE: usa --smoke oppure --case, non entrambi")

    repo = Path.cwd().resolve()
    branch, sha, prompts, sem_json, struct_json = prep(repo, args.workdir)
    if args.smoke:
        wanted = set(SMOKE_CASES)
        prompts = [p for p in prompts if p["case_id"] in wanted]
    elif args.cases:
        wanted = set(args.cases)
        prompts = [p for p in prompts if p["case_id"] in wanted]
        missing = wanted - {p["case_id"] for p in prompts}
        if missing:
            raise SystemExit(f"ERRORE: case non trovati: {sorted(missing)}")

    root = args.workdir / "workspace-prototype-a"
    sterile(repo, root, sem_json, struct_json)
    metadata = {
        "repository": "formalife/merenda-business-core",
        "branch": branch,
        "commit_sha": sha,
        "model": MODEL,
        "reasoning_effort": EFFORT,
        "architecture": ARCH,
        "cases": [p["case_id"] for p in prompts],
        "smoke": bool(args.smoke),
        "isolation": "fresh codex exec process per case; sterile doctrine + runtime indexes only",
        "gold_exposure": "physically absent; semantic runtime entries explicitly strip eval_cases",
        "bootstrap": "full fixed five-file control plane",
    }
    (args.workdir / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    traces: list[dict] = []
    try:
        for case in prompts:
            traces.append(one(root, case, args.workdir))
    except Exception as exc:
        print(f"\nPROTOTYPE A STOPPED: {exc}", file=sys.stderr)
        print("Nessuna metrica finale prodotta.", file=sys.stderr)
        return 2

    trace_path = args.workdir / "prototype-a-trace.jsonl"
    score_path = args.workdir / "prototype-a-semantic-score.json"
    context_path = args.workdir / "prototype-a-context-summary.json"
    write_jsonl(trace_path, traces)
    run(
        [
            sys.executable,
            "scripts/score_semantic_routing_run.py",
            "--trace",
            str(trace_path),
            "--json-out",
            str(score_path),
        ],
        repo,
    )
    ctx = context_summary(traces)
    context_path.write_text(json.dumps({ARCH: ctx}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    score = json.loads(score_path.read_text(encoding="utf-8"))["summary"][ARCH]

    print("\n==============================================")
    print("HIERARCHICAL RETRIEVER PROTOTYPE A — PASS")
    print("==============================================")
    print("Commit testato:", sha)
    print("Cases:", len(traces))
    print(
        "Semantic verified recall="
        f"{score['mean_verified_semantic_recall']:.4f} "
        "precision="
        f"{score['mean_verified_semantic_precision']:.4f} "
        "full_recall_cases="
        f"{score['cases_full_verified_recall']}/{score['cases']} "
        "over_verified="
        f"{score['total_over_verified']}"
    )
    print(
        "Context mean chars="
        f"{ctx['mean_operation_chars']:.0f} "
        "routing_metadata="
        f"{ctx['mean_category_chars']['routing_metadata']:.0f} "
        "structural_metadata="
        f"{ctx['mean_category_chars']['structural_metadata']:.0f} "
        "specialist_doctrine="
        f"{ctx['mean_category_chars']['specialist_doctrine']:.0f} "
        "control_plane="
        f"{ctx['mean_category_chars']['control_plane']:.0f}"
    )
    print("Output locale:", args.workdir)
    print("Semantic answer judgment non eseguito: eseguire solo dopo aver congelato i trace.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
