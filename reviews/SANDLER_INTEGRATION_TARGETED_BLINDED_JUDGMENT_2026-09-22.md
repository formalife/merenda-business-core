# Sandler Integration — Targeted Blinded Judgment — 2026-09-22

## Stato

**FROZEN BLINDED — mapping A/B non letto durante il judgment**

Scope del rerun: `R033`, `R041` soltanto.  
Motivo: correzione localizzata di semantic gold / routing dependencies dopo il primo A/B; doctrine, `REASONING_KERNEL.md` e retrieval architecture sostanziale invariati.

Gate semantico comunicato dal runner prima del judgment:

- Full verified semantic recall: `2/2`;
- Kernel verified semantic recall: `2/2`;
- Full mean verified precision: `0.7889`;
- Kernel mean verified precision: `0.8375`.

La precisione resta diagnostica, non criterio autonomo di PASS.

## Judgment blinded

| Case | A | B | Nota |
|---|---|---|---|
| R033 | **PASS** | **PASS** | entrambe distinguono surface problem da Pain qualificato, approfondiscono specificità/tentativi/conseguenze/impatto/priorità, verificano investimento/risorse e processo decisionale prima della demo, quindi limitano Fulfillment a una demo selettiva |
| R041 | **PASS** | **PASS** | entrambe rifiutano l'upsell automatico basato sulla sola soddisfazione, verificano valore realizzato e nuovo bisogno/use case e fanno rientrare la nuova opportunità nelle dimensioni Pain/investimento/Decision prima della proposta |

Totale blinded:

- A: **2/2 PASS**;
- B: **2/2 PASS**;
- material failures: **0**;
- provenance failures: **0**;
- forbidden shortcuts attivati: **0**;
- premature tactic failures: **0**;
- founder accommodation failures: **0**.

## R033-A

Soddisfa materialmente tutti i check. Non autorizza la demo sul solo Pain: dopo avere qualificato impatto e priorità richiede disponibilità a investire, risorse, stakeholder, criteri e processo decisionale; soltanto dopo consente una demo selettiva collegata al caso d'uso diagnosticato.

## R033-B

Soddisfa materialmente tutti i check. Oltre alla diagnosi del Pain esplicita willingness/ability, denaro, tempo e risorse, quindi processo decisionale, stakeholder, criteri e timing; solo successivamente consente la demo selettiva. Nessuna installazione artificiale di urgenza o valore.

## R041-A

Soddisfa materialmente tutti i check. Distingue soddisfazione da valore realizzato, richiede una review di valore e un nuovo problema/obiettivo pertinente, quindi tratta l'expansion come nuova decisione commerciale con Pain, Budget e Decision prima della prescrizione. L'automazione è subordinata a trigger, esclusioni, verifica umana ed evidenza economica.

## R041-B

Soddisfa materialmente tutti i check. Richiede risultato ottenuto e riconosciuto, nuovo problema/obiettivo, priorità, investimento sostenibile, stakeholder e processo decisionale prima di proporre l'upsell. Pur usando una formulazione più compatta di A, rende materialmente esplicite le dimensioni della normale qualification e mantiene l'automazione subordinata a verifica umana ed evidenza.

## Verdict blinded

**TARGETED BEHAVIORAL GATE: PASS — 4/4 blinded answers pass.**

Il mapping può ora essere rivelato. L'unblinding deve soltanto verificare che i quattro output appartengano alle due architetture attese e registrare il risultato finale Full/Kernel; non è più lecito modificare retroattivamente questo judgment in base all'identità A/B.
