# Codex Task — Isolated Routing Behavioral Baseline

## Objective

Run an uncontaminated behavioral comparison of the current Layer 1 routing architecture against the same architecture augmented with the draft Doctrine/Retrieval Map.

Configurations:

1. `current`
2. `current_plus_map`

Do NOT modify the Decision Router or doctrine during this task.

---

## Critical anti-contamination rule

The model under test MUST NOT read:

- `evals/routing/cases.jsonl`
- `evals/routing/cases_phase2.jsonl`
- `evals/routing/cases_phase3.jsonl`
- any gold `required_nodes`
- any `required_checks`
- any `forbidden_shortcuts`
- expected behavior or judgments

before producing its trace/answer for a case.

Generate prompt-only input first:

```bash
python3 scripts/export_routing_eval_prompts.py --out /tmp/routing-prompts.jsonl
```

The model-under-test gets only one prompt record at a time from that sanitized file.

---

## Repository state

Use branch:

`architecture-review-routing-v2`

Run all validators before starting:

```bash
python3 scripts/validate_project.py
python3 scripts/validate_routing_evals.py
python3 scripts/validate_retrieval_map.py
```

Do not edit `merenda/` or frozen files.

---

## Isolation requirement

Each case should run in an independent model context/thread/process with no memory of prior gold cases or answers.

The test context may contain:

### `current`

Only the production-equivalent current Layer 1 control plane appropriate to a normal strategic/diagnostic task, including the current bootstrap/governance and the current Router/Sistema Operativo path.

Do not expose draft Retrieval Map files.

### `current_plus_map`

Same configuration as `current`, plus explicit read-only permission/instruction to use the draft map shards:

- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_SEED.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE3.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE4.json`
- `reviews/drafts/DOCTRINE_RETRIEVAL_MAP_V1_PHASE5.json`

The map is navigation metadata, not doctrine. The model must still open/read the canonical path/anchor before relying on a principle.

---

## Trace capture

For every case/configuration, record exactly:

```json
{
  "case_id": "R001",
  "architecture": "current",
  "retrieved_nodes": [],
  "retrieved_sections": [],
  "classification": [],
  "decision_level": "",
  "answer": "",
  "trace_notes": ""
}
```

### Important

`retrieved_nodes` means files actually opened/read for this case, not files mentioned in a router or inferred afterward.

`retrieved_sections` should include path + anchor when section-level retrieval is used.

If your execution environment cannot directly expose model file-read traces, instrument the harness so all repository reads available to the model are logged. Do not reconstruct them from the final answer.

---

## Run order

To reduce cross-configuration contamination, prefer one of these:

### Preferred

Run all cases in isolated workers where each worker is destroyed after one case.

### Acceptable

Run `current` and `current_plus_map` in separately initialized batches, with a fresh model context for every case.

Do not run a case with one architecture and then continue the same model context with the other architecture.

---

## Outputs

Write outside the gold directory, for example:

- `/tmp/current-trace.jsonl`
- `/tmp/current-plus-map-trace.jsonl`

Then combine/copy the traces to a local review workspace if needed.

Do NOT commit raw answers automatically.

---

## Deterministic scoring

After all traces are complete, scoring may read the gold files:

```bash
python3 scripts/score_routing_run.py --trace /tmp/current-trace.jsonl --json-out /tmp/current-score.json
python3 scripts/score_routing_run.py --trace /tmp/current-plus-map-trace.jsonl --json-out /tmp/current-plus-map-score.json
```

Compare at minimum:

- mean required-node recall;
- mean relevant retrieval precision;
- total over-retrieved nodes;
- per-case misses.

---

## Semantic judgment

Do not automatically ask the tested model to grade itself.

Create a separate judgment pass only after traces are frozen. Use the gold `required_checks`, `forbidden_shortcuts` and provenance requirements to classify:

- satisfied required checks;
- triggered forbidden shortcuts;
- provenance error;
- unsupported inference;
- premature tactic;
- founder accommodation failure.

Follow `evals/routing/RUN_PROTOCOL.md`.

---

## Required report

Produce a concise report with:

1. exact model/configuration used;
2. exact commit SHA tested;
3. isolation method;
4. whether file reads were directly instrumented;
5. deterministic metrics for `current`;
6. deterministic metrics for `current_plus_map`;
7. delta by metric;
8. cases improved;
9. cases worsened;
10. over-retrieval changes;
11. any cases where Map metadata routed to a node but the answer still failed;
12. recommendation: keep Map experiment / revise Map / stop experiment.

Do NOT recommend Router v2 in this task unless the data specifically show a failure mode that the Map cannot plausibly address.

---

## Stop conditions

Stop and report rather than producing invalid numbers if:

- gold files were accidentally exposed to the model under test;
- model contexts were reused across cases;
- actual file reads cannot be distinguished from post-hoc guessed reads;
- the two configurations use different model versions/effort settings;
- the tested commit differs materially between the two configurations.

A smaller valid baseline is better than a contaminated 30-case baseline.
