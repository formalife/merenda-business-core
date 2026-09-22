# Sandler Integration — Blinded Behavioral Judgment — 2026-09-22

## Stato

**FROZEN BLINDED — DO NOT UNBLIND BEFORE THIS ARTIFACT**

Suite: `R031–R041`  
Branch/head giudicata: `integrate-sandler-v1` @ `21081371299f4bcbcc47227be7e9ded9c6373abd`  
Input comportamentale: `sandler-blind-answer-bundle.jsonl` generato dal runner A/B.  
Mapping A/B: **non letto e non usato durante il judgment**.

Il judgment segue `reviews/BEHAVIORAL_JUDGMENT_PROTOCOL_V2.md` e
`reviews/SANDLER_INTEGRATION_MERGE_GATE_2026-09-22.md`.

## Risultato blinded

| Case | A | B | Nota |
|---|---|---|---|
| R031 | PASS | PASS | outbound subordinato a domanda/target/economics e rapporti osservati |
| R032 | PASS | PASS | processo della conversazione prima del closing |
| R033 | PASS | **MATERIAL FAIL** | B passa da Pain alla demo senza rendere obbligatori Budget + Decision |
| R034 | PASS | PASS | investimento e Decision prima della proposta |
| R035 | PASS | PASS | Decision process prima del preventivo |
| R036 | PASS | PASS | qualify-before-present e proposta selettiva |
| R037 | PASS | PASS | tattica condizionale; omissione del nome Strip-Lining non materiale |
| R038 | PASS | PASS | follow-up state-based e closure |
| R039 | PASS | PASS | B.A.T. prima del training |
| R040 | PASS | PASS | diagnosi multilivello prima dell'aumento activity |
| R041 | PASS | **MATERIAL FAIL** | B non rende esplicito il rientro nella full qualification prima della proposta expansion |

Totale blinded:

- A: **11/11 PASS**, material failures **0**
- B: **9/11 PASS**, material failures **2**
- provenance failures: **0**
- forbidden shortcuts attivati: **0**
- founder accommodation failures: **0**

## Failure R033-B

La risposta diagnostica correttamente il surface problem e approfondisce impatto,
priorità e volontà di intervenire. Il problema è la transizione successiva:
autorizza una `demo selettiva` senza rendere necessari anche i gate Budget e
Decision.

Questo è materiale perché il caso non testa soltanto la qualità della domanda sul
Pain: l'expected behavior richiede di passare agli altri gate prima della
presentazione. Saltare investimento/risorse e processo decisionale può anticipare
Fulfillment.

Classificazione congelata:

- `premature_tactic = true`
- `material_failure = true`
- `failure_category = CORRECT_RETRIEVAL_BAD_SYNTHESIS`

La categoria causale è supportata anche dal risultato deterministico comunicato
prima del judgment: entrambe le architetture hanno ottenuto `11/11` required
semantic recall. Quindi non è appropriato classificare questo comportamento come
routing miss prima dell'unblinding.

## Failure R041-B

La risposta distingue correttamente soddisfazione da valore realizzato e richiede
un nuovo bisogno reale. Tuttavia passa da `qualificazione del bisogno successivo`
a `proposta coerente` senza rendere esplicito il rientro della nuova opportunity
nella qualification commerciale completa, inclusi investimento/risorse e
decision process.

Questo è materiale perché l'integrazione ha fissato proprio il boundary:

**Customer Success / valore realizzato → nuova evidenza → nuova opportunity →
normale qualification → proposta.**

Saltare i gate economici e decisionali può trasformare account growth in upsell
prematuro.

Classificazione congelata:

- `premature_tactic = true`
- `material_failure = true`
- `failure_category = CORRECT_RETRIEVAL_BAD_SYNTHESIS`

## Osservazioni non bloccanti

### R036

Entrambe le risposte soddisfano materialmente il requisito di non continuare a
vendere oltre il necessario attraverso proposta selettiva, eliminazione del
materiale non pertinente e definizione preventiva dell'outcome. La parola
`readiness` non è necessaria per il PASS.

### R037

Entrambe distinguono materialmente Reversing e Negative Reverse, rifiutano
l'universalizzazione e subordinano la tattica a verità/fit/qualification.
`Strip-Lining` non viene nominato. Poiché il prompt riguarda l'uso universale del
Negative Reverse e l'omissione non cambia diagnosi o decisione, il punto è
considerato non materiale e non blocca il caso.

## Regola successiva

Ora il judgment è congelato. Il passo successivo è **unblinding** del mapping
A/B per i soli casi R031–R041.

Dopo l'unblinding:

1. associare A/B a FULL/KERNEL per ogni caso;
2. determinare chi ha prodotto R033-B e R041-B;
3. non modificare automaticamente il kernel;
4. applicare la matrice del merge gate:
   - se i failure appartengono al Kernel e il Full passa sugli stessi casi,
     verificare se la compressione è causalmente responsabile;
   - se un failure appartiene al Full, indagare synthesis/stocasticità/dilution;
   - se i failure sono distribuiti, trattarli separatamente;
5. eventuali modifiche a doctrine/map/kernel/runner richiedono un nuovo full A/B
   sulla head finale.

**PR #16 resta DRAFT — DO NOT MERGE.**
