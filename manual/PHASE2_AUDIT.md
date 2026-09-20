# Phase 2 Audit — Semantic decomposition and cross-section consolidation

## Verdict

**PASS — FASE 2 COMPLETA**

Data: 2026-09-20.

Doctrine `main` verificato prima del gate:

`c86b5e3dd1cc04257a5f9f9250ffd244c98d4b1e`

Il branch editoriale risulta ahead rispetto a `main` e non behind al momento del controllo; quindi il crosswalk non sta ignorando modifiche canoniche intervenute dopo il branch point.

---

# 1. Coverage documentale

Corpus canonico censito: **60 file**.

Coverage finale Fase 2: **60/60 file**.

| Blocco | File | Unità first-pass |
|---|---:|---:|
| root routing (`INDEX` + `DECISION_ROUTER`) | 2 | 17 RTR |
| `00_fondamenti` | 3 | 60 FND |
| `01_mercato` | 5 | 53 MRC |
| `02_posizionamento` | 4 | 57 POS |
| `03_offerta` | 4 | 71 OFF |
| `04_marketing` | 7 | 68 MKT |
| `05_acquisizione` | 6 | 67 ACQ |
| `06_vendita` | 5 | 71 SAL |
| `07_copy_comunicazione` | 5 | 64 CPY |
| `08_brand` | 6 | 58 BRD |
| `09_business` | 10 | 107 BUS |
| `10_casi_studio` | 3 | 16 CAS |
| **Totale** | **60** | **709 unità** |

Il numero 709 è un artefatto di tracciabilità del first pass, non un obiettivo editoriale. La Fase 3 dovrà comprimere queste unità in concetti/capitoli senza perdere caveat o dipendenze.

---

# 2. Gate semantico

Requisito roadmap:

> ogni unità dottrinale rilevante ha almeno una destinazione editoriale candidata e ogni nodo canonico è marcato come coperto, escluso motivatamente o ancora aperto.

Esito:

- tutti i 60 file sono `COVERED`;
- nessun file canonico è sparito per omissione;
- README/router/index sono trattati come routing/reference quando non introducono materia autonoma;
- casi sono trattati come case material, non teoria autonoma;
- ogni unità first-pass ha un ruolo candidato nel crosswalk (`PRIMARY`, `SUPPORTING`, `EXAMPLE/CASE`, `REFERENCE` o gap/reference);
- nessun `OPEN` semantico richiede nuova acquisizione per chiudere il coverage.

**Gate: PASS.**

---

# 3. Semantic deduplication

Artefatto: `manual/PRIMARY_HOME_MAP.md`.

Decisioni chiave:

1. economics completi → `09_business`; versione minima introdotta presto;
2. market/customer → `01_mercato`;
3. VoC → sintesi editoriale trasversale;
4. positioning → `02_posizionamento`;
5. offer/pricing → `03_offerta`;
6. demand/awareness/channel → `04_marketing`;
7. funnel/database/state machine/pre-education → `05_acquisizione`;
8. sales end-to-end → `06_vendita`;
9. copy/argumentation → `07_copy_comunicazione`;
10. authority/proof/reputation/community → `08_brand`, con split didattico pre-sale/post-experience;
11. customer lifecycle/operations/scale → `09_business`, integrando unità di mercato/offerta/marketing/acquisition;
12. router per sintomo → toolkit diagnostico, non teoria duplicata.

Finding: le ridondanze principali sono di **routing e applicazione**, non conflitti sostanziali.

---

# 4. Dependency pass

Artefatto: `manual/DEPENDENCY_MAP.md`.

Il prerequisite graph contiene 35 blocchi D-01…D-35.

Findings vincolanti:

- economics minimi precedono già mercato e customer selection;
- VoC precede positioning e copy;
- positioning precede offer/copy/amplification;
- offer precede acquisition;
- authority/proof può essere necessario prima di acquisition/sales;
- awareness/intento precedono channel/copy/funnel directness;
- database/state precedono funnel adattivo e lifecycle;
- copy operativo arriva dopo strategia, proof e awareness;
- vendita inizia dall'handoff, non dalla call;
- delivery precede retention/referral/reputation;
- advanced economics + cash + capacity precedono scale;
- process/governance precedono automation e organizational scale;
- expansion riapre market/positioning per il nuovo contesto.

Finding: nessun hard prerequisite fondamentale è privo di materiale canonico sufficiente.

---

# 5. Provenance/temporal pass

Artefatto: `manual/PROVENANCE_MAP.md`.

Coperti:

- source family e assimilated-source boundaries;
- temporal precedence sui principali assoluti storici;
- cluster MAF/Bonechi;
- cluster jAI/Jay Abraham-Michael Simmons-Max Bernstein;
- sintesi editoriali non attribuibili a una singola fonte.

Decisione:

**G-003 — RESOLVED EDITORIALLY.**

---

# 6. Case inventory pass

Artefatto: `manual/CASE_INVENTORY.md`.

Casi reali forti identificati:

- Il Muratore Bergamasco;
- Studio Di Caprio;
- Maccheroni;
- MotoArgento;
- Il Toro come caso/microcaso trasversale;
- esempi di positioning/focus aggiuntivi.

Gap residui di casistica:

- VoC completo;
- pricing/economics;
- vendita end-to-end;
- customer lifecycle;
- brand accumulation;
- transferability/founder independence.

Piano editoriale: casi sintetici originali e dichiaratamente didattici, non nuova acquisizione dottrinale.

Decisione:

**G-002 resta CASE GAP editoriale, ma non blocca il curriculum.**

---

# 7. Gap decisions dopo il cross-section pass

## G-001 — Vendita end-to-end

**RESOLVED EDITORIALLY.**

La sequenza completa è ricostruibile dal corpus corrente. Non è necessario modificare il doctrine layer.

## G-002 — Case library

**OPEN — closure plan defined.**

La casistica reale è utile ma incompleta. Sarà chiusa con casi sintetici in Fase 4/5.

## G-003 — Provenance map

**RESOLVED EDITORIALLY.**

Esiste `PROVENANCE_MAP.md`.

## G-004 — Costruzione del brand

**RESOLVED EDITORIALLY.**

La sintesi causale regge senza nuova dottrina:

**posizione → authority/credibility/proof → esperienza → reputazione → memoria → advocacy/community.**

## G-005 — Voice of Customer / market research

**IN SYNTHESIS — no doctrinal escalation indicated by Phase 2.**

Gli input e le procedure componenti esistono; manca il documento editoriale unificato. Da chiudere in Fase 4.

## G-006 — Economics early curriculum

**CONFIRMED — da chiudere in Fase 3.**

Il prerequisite graph richiede economics minimi all'inizio.

## G-007 — Glossario beginner-first

**OPEN.**

Va governato dal curriculum e finalizzato in release.

## G-008 — Customer lifecycle

**RESOLVED EDITORIALLY.**

La sequenza completa è ricostruibile integrando mercato, offer, marketing, acquisition e customer success.

---

# 8. Doctrinal review decision

La Fase 2 non ha prodotto un finding che richieda modificare `merenda/` prima di progettare il curriculum.

In particolare:

- vendita: knowledge sufficient, synthesis missing;
- brand: knowledge sufficient, synthesis missing;
- lifecycle: knowledge sufficient, synthesis missing;
- VoC: knowledge molto distribuita ma sufficiente a tentare una sintesi editoriale prima di qualsiasi nuova acquisizione.

Quindi:

**nessuna escalation al doctrine layer in questo gate.**

Se la Fase 4 non riuscirà a costruire una procedura VoC autosufficiente senza inventare passaggi, allora G-005 verrà rivalutato come possibile doctrinal gap.

---

# 9. Phase 2 gate checklist

- [x] 60/60 file coperti;
- [x] unità semantiche first-pass tracciate;
- [x] primary-home pass;
- [x] dependency pass;
- [x] provenance/temporal pass;
- [x] case inventory pass;
- [x] gap pass;
- [x] nessun file canonico non considerato;
- [x] nessuna nuova acquisizione necessaria per avviare il curriculum;
- [x] doctrine layer non modificato.

**FASE 2: DONE.**

Next: **Fase 3 — Curriculum e architettura didattica.**
