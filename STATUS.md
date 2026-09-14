# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–250 processati semanticamente**. Checkpoint **250 completato**: FASE 14 + FASE 15 eseguite da Claude Code. Corpus ancora incompleto.

## Fase corrente

**FASE 7 — acquisizione tecnica 251–275 completata: 25/25 transcript utilizzabili, ancora da processare semanticamente.** Branch `acquisition-251-275`, base `e75aeca6b76f2e94678608dd90a2e550d7d486db`. Report tecnico completo: `sources/queue/acquisition-progress.md`.


Elaborazione semantica **226–250 completata da ChatGPT**. Checkpoint 250 (FASE 14 + FASE 15) **eseguito e chiuso da Claude Code**.

Esito sintetico:

- FASE 14: refactor mirato in `06_vendita` (il metodo diagnosi→prescrizione spostato da `prequalifica-follow-up-decisori.md` a `preventivo-consulenza-diagnosi.md`); tutti gli altri focus richiesti (`08_brand`, `07_copy_comunicazione`, `04_marketing`, `03_offerta`, RFM, prevalenza temporale 249) verificati corretti senza modifiche.
- FASE 15: nessuna modifica alla tassonomia a 11 categorie (nessun beneficio netto identificato); nessuna modifica al classificatore A/B/C; `reviews/RESIDUAL_CLASSIFICATION_201-468.md` rigenerato per riflettere l'avanzamento del residuo (243→218).
- Validator: baseline reale misurata **842 warning** (non 841 come nel pre-handoff; causa documentata: formattazione di una riga STATUS nel commit di handoff ChatGPT), identici prima/dopo il refactor. Nessuna nuova anomalia.

Report definitivo: `reviews/CHECKPOINT_250.md`.

## Corpus

- Video individuati: **468**
- Contenuti processati semanticamente: **250**
- STUDIATO / integrati o deduplicati: **244**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **218**
- Corpus completo: NO
- Batch tecnico 251–275: **25/25 utilizzabili**, acquisiti ma non studiati
- Sottotitoli batch 251–275: **25 automatici italiani originali / 0 manuali**
- Elaborazione semantica 226–250: **25/25**
- Review 226–250: **25**
- Transcript mancanti nel batch: 0
- Fallback ASR nel batch: 0
- Errori finali tecnici: 0
- Pending tecnici: 0

## Novelty 226–250

- Incrementali: **16/25 = 64%**
- Deduplicati/confermativi: **9/25**
- Nessun nuovo ESCLUSO
- A: **8/10 incrementali**
- B: **7/9 incrementali**
- C: **1/6 incrementale**
- Il C incrementale è 229, fonte recente del 16 dicembre 2025: C resta FAST REVIEW, mai SKIP.

Correzione qualità: il 239 era stato inizialmente interpretato come incrementale per RFM; il cross-check ha mostrato che RFM era già canonico in `appropriatezza-clienti.md`. Duplicazione rimossa e 239 correttamente marcato Novelty: no.

Dettagli completi in `reviews/CHECKPOINT_250.md`.

## Nuovi nodi KB del batch

- `merenda/04_marketing/eventi-proprietari-vip-experience.md`
- `merenda/06_vendita/follow-up-lead-non-convertiti.md`
- `merenda/06_vendita/preventivo-consulenza-diagnosi.md`
- `merenda/07_copy_comunicazione/checklist-risposta-diretta.md`
- `merenda/08_brand/brand-community-e-fan.md`
- `merenda/08_brand/testimonianze-e-prova-sociale.md`

## Workflow attivo — v1.1

- CODEX: acquisizione tecnica e supporto meccanico.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.
- Classificazione A/B/C: priorità/profondità, mai esenzione dalla revisione.
- Regola manuale di promozione per recenza attiva come documentazione dal checkpoint 225.
- Nessuna modifica ai file frozen.

## Checkpoint

- Ultimo refactor KB completato: **250 — FASE 14**
- Ultimo audit tassonomia completato: **250 — FASE 15**
- Prossimo refactor KB dovuto: **275 — FASE 14**
- Prossimo audit tassonomia dovuto: **300 — FASE 14 + FASE 15**
- Checkpoint Claude richiesto ora: **NO**
- Report checkpoint corrente: `reviews/CHECKPOINT_250.md` (definitivo)

## Agente richiesto

**CHATGPT**

## Next Action

Revisione semantica del batch **251–275**, fasi **8–13**, utilizzando gli asset tecnici disponibili. Elaborazione semantica ancora ferma a **250**; nessun contenuto di questo batch è stato marcato STUDIATO o ESCLUSO dalla fase tecnica.

Primo contenuto acquisito non completato: **251 — `ellOvKnIOqk` — “The #1 Sales Technique for a Record-Breaking Sales Team”**.

Prossimo checkpoint Claude: **275 — FASE 14** dopo il completamento semantico; prossimo audit tassonomia **300 — FASE 14 + FASE 15**. Nessuna acquisizione 276+; stop tecnico a 275, nessun merge su main.

## Validazione e limiti

- FASE 7 251–275: metadata/canale e JSON3↔Markdown verificati 25/25; 22 keyframe selettivi su 8 video ispezionati. Code fuori traccia: 252 2,640 s; 253 5,440 s; 259 13,320 s; 262 8,681 s; 263 9,401 s. Sforamenti positivi fino a 2,240 s. Nessuna correzione arbitraria; limiti visuali di 253/261 nel report tecnico.
- Validator tecnico pre/post: **842 warning identici**, nessuna nuova anomalia; `git diff --check` pulito. 25 commit individuali + 1 handoff globale. Frozen, KB, catalogo, queue e review invariati; nessuna `.review.md` creata.

Dettagli storici del checkpoint 250:

- Baseline validator **reale, misurata da Claude sulla HEAD del checkpoint 250**: **842 warning** (non 841: la fase tecnica 226–250 aveva certificato 841 identici prima/dopo l'acquisizione; il commit di handoff semantico ChatGPT ha poi aggiunto grassetto markdown a una riga di `STATUS.md`, portando a 3 le righe `Contatore STATUS errato` invece di 2 — stessa classe di drift di nomenclatura già nota, non una nuova anomalia semantica). Identici prima/dopo FASE 14+15 di questo checkpoint: nessuna nuova anomalia introdotta.
- Confronto tecnico→semantico verificato: **25 commit**, **25 review**, nessun frozen e nessun file 251+ modificato.
- Contatori catalogo verificati: **244 STUDIATO + 6 ESCLUSO + 218 DA STUDIARE = 468**.
- Limiti tecnici transcript: 227 copertura 95,51%; 228 copertura 92,79%; piccoli sforamenti timestamp fino a 2,360 s. Nessuna nuova regola semantica è stata basata sulle code non coperte.
- Dettaglio completo FASE 14/15: `reviews/CHECKPOINT_250.md`.
