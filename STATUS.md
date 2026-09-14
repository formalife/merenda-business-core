# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti **1–250 processati semanticamente**. Checkpoint **250 raggiunto**: FASE 14 + FASE 15 dovute a Claude Code. Corpus ancora incompleto.

## Fase corrente

Elaborazione semantica **226–250 completata da ChatGPT**. Il checkpoint 250 è in stato **PRE-HANDOFF CLAUDE** e non è ancora definitivo.

Claude deve eseguire:

- **FASE 14 — refactor KB**
- **FASE 15 — audit tassonomia**

Report pre-handoff: `reviews/CHECKPOINT_250.md`.

## Corpus

- Video individuati: **468**
- Contenuti processati semanticamente: **250**
- STUDIATO / integrati o deduplicati: **244**
- ESCLUSO dalla dottrina attiva: **6**
- Da processare: **218**
- Corpus completo: NO
- Batch tecnico 226–250: **25/25 utilizzabili**
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

- Ultimo refactor KB completato: **225**
- Ultimo audit tassonomia completato: **200**
- Refactor KB dovuto: **250 — FASE 14**
- Audit tassonomia dovuto: **250 — FASE 15**
- Checkpoint Claude richiesto ora: **SÌ**
- Report checkpoint corrente: `reviews/CHECKPOINT_250.md` (pre-handoff)

## Agente richiesto

**CLAUDE CODE**

## Next Action

Eseguire il checkpoint **250 — FASE 14 + FASE 15** sullo stato canonico che verrà portato su `main`.

Claude deve:

1. rileggere l'intera `merenda/`;
2. refactorare solo dove esiste un beneficio strutturale reale;
3. eseguire audit tassonomico completo;
4. verificare in particolare le nuove aree `06_vendita`, `07_copy_comunicazione`, `08_brand`;
5. verificare il nodo canonico RFM e le regole di prevalenza temporale;
6. valutare empiricamente il classifier A/B/C senza modificare frozen senza autorizzazione;
7. eseguire validator prima/dopo, `git diff --check`, link/orfani, contaminazione Formalife e frozen;
8. non processare/acquisire semanticamente alcun contenuto 251+;
9. aggiornare `reviews/CHECKPOINT_250.md` da pre-handoff a report definitivo e aggiornare `STATUS.md`.

Dopo il checkpoint, salvo diversa decisione motivata, il prossimo lavoro tecnico sarà **251–275**. Primo contenuto residuo: **251 — `ellOvKnIOqk` — “The #1 Sales Technique for a Record-Breaking Sales Team”**.

## Validazione e limiti

- Baseline validator certa alla fine della fase tecnica 226–250: **841 warning storici**, identici prima/dopo acquisizione.
- Il connettore GitHub usato da ChatGPT non può eseguire il validator sul working tree remoto: il validator post-semantico deve essere misurato da Claude, non viene inventato.
- Confronto tecnico→semantico verificato: **25 commit**, **25 review**, nessun frozen e nessun file 251+ modificato.
- Contatori catalogo verificati: **244 STUDIATO + 6 ESCLUSO + 218 DA STUDIARE = 468**.
- Limiti tecnici transcript: 227 copertura 95,51%; 228 copertura 92,79%; piccoli sforamenti timestamp fino a 2,360 s. Nessuna nuova regola semantica è stata basata sulle code non coperte.
