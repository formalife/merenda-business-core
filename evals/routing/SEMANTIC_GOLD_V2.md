# Routing Eval v2 — Semantic Gold Schema

Date: 2026-09-18
Status: DRAFT FOR REVIEW

## Purpose

File-level `required_nodes` materially overstates behavioral failure in the current suite. Eval v2 therefore introduces stable semantic-unit IDs as the primary retrieval target while retaining legacy file-level fields for historical comparison.

This does **not** make the Retrieval Map the gold standard. Semantic gold is manually reviewed evaluation metadata. Retrieval Map entries are candidate evidence and routing metadata only.

## Proposed record extension

Existing case fields remain unchanged. Eval v2 adds:

```json
{
  "required_semantic_units": [
    "MARKET.USER_VS_PAYER",
    "MARKET.APPROPRIATENESS"
  ],
  "optional_semantic_units": [
    "MARKET.IDENTIFIABILITY"
  ],
  "required_expansions": [
    {
      "semantic_id": "MARKET.USER_VS_PAYER",
      "minimum_context": "canonical_section",
      "expand_when": "buyer/user/payer roles remain ambiguous"
    }
  ]
}
```

## `required_semantic_units`

Stable concept IDs that must be available to make the decision correctly.

Rules:

- an ID represents a decision-relevant concept, not a file;
- multiple semantic IDs may point into the same Markdown document;
- one semantic ID may be satisfied by a canonical section without reading the whole file;
- the ID should survive file moves/refactors;
- include only concepts whose absence can materially degrade a required check or decision.

## `optional_semantic_units`

Concepts that can improve the answer but are not necessary to pass the case.

Optional units must not be counted as over-retrieval.

## `required_expansions`

Used only where the minimal semantic unit can be insufficient without local/parent context.

Candidate `minimum_context` values:

- `semantic_block`
- `canonical_section`
- `parent_section`
- `full_node`

Do not require expansion merely because a larger file exists.

## Primary deterministic metrics

### Semantic Unit Recall

`required semantic units retrieved / required semantic units gold`

### Semantic Context Precision

`retrieved required + optional semantic units / all retrieved semantic units`

### Expansion Accuracy

For units with explicit expansion requirements, whether the runtime expanded to at least the required context level without unnecessary full-node fallback.

### Full-node Fallback Rate

Share of cases where an entire canonical node is loaded after a smaller retrievable unit existed.

## Judgment metrics retained

- Required / upstream check recall
- Forbidden shortcut rate
- Doctrine fidelity
- Provenance accuracy
- Unsupported inference rate
- Premature tactic rate
- Founder accommodation failure

## Migration rule

`required_nodes` and `optional_nodes` remain in the current 30 cases until at least one semantic-level A/B is complete. They become compatibility/debug metadata, not the primary optimization target.

## Anti-overfitting rule

The semantic gold must **not** be generated automatically from `eval_cases` links in the Retrieval Map and then accepted without review.

A migration builder may create candidates, but each case must be manually reviewed against:

1. the actual `required_checks`;
2. canonical doctrine sections;
3. whether omission of the concept can change the decision;
4. whether the concept is required versus merely useful.

The same 30 cases must not be used indefinitely as the only architecture acceptance set. A blind holdout set is required before final adoption.

## Provenance

Semantic IDs reference canonical doctrine and routing metadata. They are not themselves doctrinal statements. Provenance remains attached to the semantic routing entry and the canonical source section.
