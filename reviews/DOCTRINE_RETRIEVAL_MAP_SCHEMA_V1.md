# Doctrine / Retrieval Map v1 — Schema Draft

Data: 2026-09-18
Stato: DRAFT — ARCHITECTURE REVIEW

## Scopo

Definire il layer machine-readable minimo necessario per instradare un agente verso la conoscenza canonica corretta senza trasformare la mappa in una seconda copia della dottrina.

La mappa deve rispondere soprattutto a cinque domande:

1. **Quale principio/nodo governa questo tipo di decisione?**
2. **Quale prerequisito a monte devo controllare prima?**
3. **Quale evidenza deve essere disponibile prima di concludere?**
4. **Quale passaggio preciso della KB devo recuperare?**
5. **Quale provenance/evoluzione temporale devo preservare?**

La mappa NON deve rispondere completamente alla domanda di business. La risposta continua a provenire dal doctrine layer canonico + evidenza Formalife.

---

# 1. Unità della mappa

L'unità non è necessariamente un file.

Una entry rappresenta un **principio decisionale instradabile** o una **unità semantica ad alta leva**.

Più entry possono puntare allo stesso file con anchor diversi.

Esempio concettuale:

- `MARKET.IDENTIFIABILITY`
- `MARKET.USER_VS_PAYER`
- `MARKET.NATURAL_CUSTOMER_EXPIRY`
- `MARKET.AWARENESS_STATE`

possono vivere nello stesso nodo canonico ma servire decisioni diverse.

---

# 2. Schema minimo proposto

```json
{
  "id": "MARKET.USER_VS_PAYER",
  "label": "Distinguere utilizzatore da pagatore/decisore",
  "status": "current",
  "canonical": {
    "path": "merenda/01_mercato/clienti-identificabili-e-target.md",
    "anchor": "consumare-non-significa-comprare"
  },
  "kind": "diagnostic_dimension",
  "canonical_for": [
    "buyer_user_separation",
    "payer_decision_motivation"
  ],
  "use_when": [
    "chi usa e chi paga possono essere soggetti diversi",
    "vendita B2B o familiare con beneficiario diverso dal decisore economico"
  ],
  "not_sufficient_for": [
    "dimostrare attrattività del segmento",
    "scegliere il canale"
  ],
  "upstream": [],
  "must_read_with": [
    {
      "id": "MARKET.APPROPRIATENESS",
      "when": "la decisione riguarda quale segmento servire"
    }
  ],
  "evidence_required": [
    "chi paga",
    "chi decide",
    "chi usa",
    "motivazione economica del decisore"
  ],
  "provenance": {
    "class": "MERENDA_PRIMARY",
    "notes": null
  },
  "supersession": {
    "supersedes": [],
    "superseded_by": []
  },
  "related": [
    "MARKET.IDENTIFIABILITY"
  ],
  "eval_cases": ["R003"]
}
```

---

# 3. Campi obbligatori

## `id`

Identificatore stabile semantico, non legato al path.

Naming candidato:

`DOMAIN.CONCEPT`

Esempi:

- `MARKET.APPROPRIATENESS`
- `MARKET.USER_VS_PAYER`
- `POSITIONING.OPERATIONAL_DIFFERENCE`
- `DEMAND.OWNED_BEFORE_NEW`
- `ECONOMICS.CAC_PAYBACK_CASH`

L'ID deve sopravvivere a eventuali refactor dei file.

## `label`

Nome umano corto del principio/unità semantica.

## `status`

Valori candidati:

- `current`
- `historical`
- `superseded`
- `conditional`
- `draft`

La mappa v1 dovrebbe contenere normalmente solo entry `current` e i riferimenti necessari alla supersession.

## `canonical.path`

Path del nodo canonico.

## `canonical.anchor`

Anchor/heading preferito quando il principio non coincide con l'intero file.

Può essere `null` quando l'intero nodo è la vera unità canonica.

## `kind`

Vocabolario ristretto candidato:

- `gate`
- `diagnostic_dimension`
- `causal_dependency`
- `decision_rule`
- `process`
- `metric`
- `exception`
- `temporal_caveat`
- `provenance_caveat`

Non aggiungere tipi se non cambiano il routing.

## `canonical_for`

Lista di concetti/decisioni che questa entry governa direttamente.

Non deve diventare un elenco infinito di sinonimi naturali.

## `use_when`

Condizioni concettuali in cui la entry è candidata al retrieval.

Serve alla comprensione/routing; non è una keyword list esaustiva.

## `not_sufficient_for`

Impedisce una failure importante: usare un principio corretto per concludere qualcosa che non dimostra.

Esempio:

`search volume` può essere informativo sulla domanda, ma non è sufficiente per dimostrare willingness to pay o qualità economica del mercato.

## `upstream`

Entry che devono essere controllate prima quando la decisione corrente dipende da loro.

Questa è una delle differenze essenziali rispetto a similarity search.

## `must_read_with`

Dipendenze laterali/condizionali.

Formato:

```json
{
  "id": "...",
  "when": "condizione"
}
```

Evita di caricare companion nodes incondizionatamente.

## `evidence_required`

Fatti o categorie di evidenza che l'agente deve cercare nel Layer 2/founder prima di trasformare il principio in decisione specifica.

Questa lista non deve contenere domande di intervista complete; descrive solo ciò che deve essere noto.

## `provenance`

Minimo:

- `class`: `MERENDA_PRIMARY` / `ASSIMILATED` / `SYNTHESIS`
- `notes`: eventuale autore reale o caveat

Quando un singolo file mescola provenance diverse, la metadata deve vivere a livello di entry.

## `supersession`

- `supersedes`
- `superseded_by`

Serve solo in presenza di reale evoluzione/contraddizione pertinente al retrieval.

## `related`

Relazioni utili ma non obbligatorie.

Non devono essere automaticamente caricate.

## `eval_cases`

ID dei gold case che esercitano esplicitamente la entry.

Questo rende possibile misurare coverage e regressioni.

---

# 4. Campi esclusi intenzionalmente dalla v1

Per evitare overengineering, la prima versione NON include automaticamente:

- embedding;
- keyword exhaustive;
- abstract lungo della dottrina;
- copia delle prescrizioni del nodo;
- confidence numerica arbitraria;
- decine di categorie epistemiche;
- source list completa di ogni paragrafo;
- esempi/casi completi;
- prompt da mostrare al founder;
- output finale preconfezionato.

Questi elementi entrano solo se un eval dimostra che la loro assenza causa failure.

---

# 5. Retrieval algorithm candidato

## Step A — Case representation

Estrarre dal caso soltanto dimensioni decisionali:

- outcome economico richiesto;
- livello dove appare il sintomo;
- attore/i: buyer, user, payer, decisore, partner;
- stato relazione;
- domanda/intento/consapevolezza;
- vincoli;
- economics noti;
- tattica proposta dal founder;
- fatti vs ipotesi.

## Step B — Candidate entries

Selezionare le entry `use_when/canonical_for` pertinenti.

## Step C — Causal expansion

Aggiungere:

- `upstream` obbligatori;
- `must_read_with` solo quando la condizione è vera.

## Step D — Evidence sufficiency

Prima di leggere molti nodi, verificare quali `evidence_required` sono già disponibili e quali mancano.

## Step E — Canonical retrieval

Recuperare:

1. anchor specifico;
2. contesto locale sufficiente a comprenderlo;
3. file completo solo se serve a gestire caveat/dipendenze.

## Step F — Provenance/supersession check

Applicare prima della formulazione finale.

## Step G — Decision

Il Router/agent produce diagnosi, test e decisione usando il contenuto canonico recuperato, non la metadata come sostituto.

---

# 6. Sufficiency gate candidato

Una decisione sostanziale non è pronta se una delle seguenti condizioni è vera:

- esiste un upstream obbligatorio non controllato;
- manca evidenza richiesta capace di cambiare la conclusione;
- il nodo recuperato è solo `related`, non canonico per la decisione;
- una entry ha supersession pertinente non risolta;
- la provenance necessaria all'attribuzione non è stata preservata;
- la tattica richiesta è downstream di un gate non ancora passato.

---

# 7. Seed entries da costruire per prime

La v1 non deve mappare tutta la KB immediatamente.

Primo blocco candidato, guidato dagli eval R001–R025:

1. `MARKET.VALIDITY_GATE`
2. `MARKET.IDENTIFIABILITY`
3. `MARKET.APPROPRIATENESS`
4. `MARKET.USER_VS_PAYER`
5. `MARKET.NATURAL_CUSTOMER_EXPIRY`
6. `MARKET.SEARCH_VOLUME_VS_INTENT`
7. `POSITIONING.OPERATIONAL_DIFFERENCE`
8. `OFFER.DIRECT_RESPONSE`
9. `PRICING.PREMIUM_CONDITIONAL`
10. `DEMAND.OWNED_BEFORE_NEW`
11. `DEMAND.ACTIVE_BEFORE_LATENT`
12. `DEMAND.TIMING`
13. `FUNNEL.DEPTH_BY_DECISION_COMPLEXITY`
14. `DISTRIBUTION.SELL_IN_SELL_THROUGH`
15. `ACQUISITION.STATE_BASED_ROUTING`
16. `ACQUISITION.INFORMATION_BEFORE_HUMAN_TIME`
17. `SALES.DIAGNOSE_BEFORE_PRESCRIBE`
18. `CUSTOMER.SUCCESS_BEFORE_RETENTION_TACTIC`
19. `ECONOMICS.CUSTOMER_PROFITABILITY`
20. `ECONOMICS.CAC_PAYBACK_CASH`
21. `CAPACITY.BEFORE_SCALE`
22. `FOCUS.BEFORE_PROLIFERATION`
23. `TRANSFERABILITY.FOUNDER_DEPENDENCY`
24. `PROVENANCE.ASSIMILATED_ATTRIBUTION`
25. `ZERO_BASED.LEGACY_IS_NOT_CONSTRAINT`

Questo blocco è abbastanza piccolo da essere revisionabile e abbastanza ampio da coprire la baseline attuale.

---

# 8. Criterio di successo della v1

La mappa è utile se migliora gli eval senza richiedere di caricare più contesto totale.

Target qualitativo:

- maggiore routing recall;
- maggiore upstream recall;
- minori unsupported inference;
- minore premature tactic rate;
- provenance accuracy più alta;
- contesto medio uguale o inferiore.

Se la mappa richiede quasi tutta la KB per funzionare, l'architettura ha fallito.

---

# 9. Decisione non ancora presa

Non è ancora deciso dove vivrà la mappa canonica finale.

Candidate:

- `merenda/DOCTRINE_MAP.json`
- `system/DOCTRINE_MAP.json`
- altra directory di control plane dedicata

Durante la Architecture Review il draft resta sotto `reviews/` per evitare di promuovere prematuramente metadata sperimentali a parte canonica del doctrine layer.
