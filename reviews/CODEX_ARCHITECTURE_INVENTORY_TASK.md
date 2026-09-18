# Codex Task — Architecture Inventory for Routing Review

Branch: `architecture-review-routing-v2`

## Mission

Produce a mechanical inventory of Merenda Business Core that helps evaluate routing and retrieval quality. Do **not** change doctrine and do **not** refactor `DECISION_ROUTER.md`.

Read first:

1. `00_START_HERE.md`
2. `STATUS.md`
3. `reviews/ARCHITECTURE_REVIEW_ROADMAP.md`
4. `evals/routing/README.md`
5. `AGENTS.md`

## First action

Run:

```bash
python3 scripts/validate_project.py
python3 scripts/validate_routing_evals.py
```

Record pass/fail and exact errors. Do not silently repair doctrine to make validators pass.

## Deliverable A — Markdown inventory

Create:

`reviews/ARCHITECTURE_INVENTORY.md`

Include:

### Repository topology

For every canonical file under `merenda/`:

- path;
- byte/line size;
- top-level and second-level headings;
- outbound internal links;
- inbound internal link count;
- section/README membership.

### Routing visibility

For every canonical file/meaningful section, record whether it is discoverable from:

- `merenda/INDEX.md`;
- section `README.md`;
- `merenda/DECISION_ROUTER.md`;
- `merenda/00_fondamenti/sistema-operativo-merenda.md`.

Do not infer semantic importance from link count alone.

### Candidate hidden concepts

Identify headings/sections that contain a distinct decision concept but are weakly visible from filenames/index/router.

Mechanical candidates include sections whose heading terminology does not appear in INDEX/README/Router or whose only discoverability is through a specialist file.

Examples to verify, not assume:

- user/payer separation;
- natural customer expiry;
- whale curve;
- state/relationship dimensions;
- sell-in / sell-through.

For each candidate include exact path + heading/anchor and why it may be hard to retrieve.

### Oversized / multi-concept files

Flag files that contain many distinct decision concepts or unusually many headings/links. Do not recommend splitting automatically; only expose retrieval risk.

### Governance conflicts

Mechanically compare active root/governance docs for explicit statements that appear incompatible, especially source/provenance scope. Quote only short snippets and point to exact files/headings.

## Deliverable B — machine-readable inventory

Create:

`work/architecture_inventory.json`

Use one record per meaningful section, not merely one record per file.

Suggested fields:

- `path`
- `heading`
- `anchor`
- `section`
- `line_start` if reliably derivable
- `line_end` if reliably derivable
- `outbound_links`
- `inbound_link_count`
- `visible_from_index`
- `visible_from_section_readme`
- `visible_from_router`
- `visible_from_system_map`
- `candidate_hidden_concept`
- `notes`

Do not invent provenance or canonical status beyond what files explicitly support.

## Deliverable C — eval coverage report

For each case in `evals/routing/cases.jsonl`:

- verify all `required_nodes` and `optional_nodes` exist;
- report whether each required node is explicitly named in the current Router;
- report whether the key concept named by the case appears in INDEX/section README/Router;
- do not score semantic answer quality yet.

Add this as a section of `reviews/ARCHITECTURE_INVENTORY.md`.

## Constraints

- Do not modify files under `merenda/`.
- Do not modify frozen files.
- Do not add or assimilate sources.
- Do not rewrite Router.
- Do not infer what Frank would say beyond explicit repo content.
- Do not build embeddings/vector DB/GraphRAG.
- Prefer simple Python standard-library scripts if helper tooling is needed.
- Generated mechanical artifacts may go under `work/`; durable conclusions go under `reviews/`.

## Completion criterion

The task is complete when a reviewer can answer:

1. Which high-leverage concepts are hard to discover with the current routing surface?
2. Which eval cases depend on those hidden concepts?
3. Which files are structurally overloaded for file-level routing?
4. Which governance statements conflict?
5. What evidence do we now have for designing a Doctrine/Retrieval Map v1?
