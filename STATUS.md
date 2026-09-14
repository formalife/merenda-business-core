# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti 1–175 processati semanticamente; batch 151–175 completato; corpus ancora incompleto.

## Fase corrente

**Checkpoint 175 raggiunto.** Le fasi 8–13 sono complete per tutti i contenuti 151–175. È dovuta **CLAUDE CODE — FASE 14 soltanto**.

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 175
- STUDIATO / integrati nella KB: 169
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 293
- Corpus completo: NO
- Batch tecnico 151–175: 25/25 utilizzabili
- Elaborazione semantica 151–175: 25/25 completata
- Fallback ASR nel batch 151–175: 0
- Blocchi semantici aperti nel batch: 0

## Workflow attivo — v1.1

- CODEX / strumenti locali: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: FASE 14 ogni 25; FASE 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 150
- Refactor KB dovuto ora: **175**
- Ultimo audit tassonomia completato: 150
- Prossimo audit tassonomia: 200
- Checkpoint Claude richiesto ora: **YES**
- Documento handoff corrente: `reviews/CHECKPOINT_175.md`
- Checkpoint precedente: `reviews/CHECKPOINT_150.md`

## Batch 151–175 — sintesi semantica

Principali integrazioni:

- vendita consulenziale: guidare il cliente oltre decisioni precedenti fallite;
- offerta: rendere percepibile la qualità e costruire bundle sul risultato d'uso;
- business: collegare LTV/CAC alla durata minima profittevole;
- backend: upsell pertinente proposto in modo sistematico;
- HR: selezione verificata sul lavoro reale;
- fondamentali: strumenti vs competenza e customer experience come marketing operativo;
- canali: vincoli di acquisizione aumentano il peso di referral, retention e LTV.

Riclassificazioni semantiche sono state sincronizzate in `sources/catalog.json`, `sources/VIDEO_INDEX.md` e `sources/queue/QUEUE.md`.

Dettagli completi: `reviews/CHECKPOINT_175.md` e singole `sources/transcripts/*.review.md`.

## Agente richiesto

**CLAUDE CODE**

## Next Action

Eseguire **FASE 14 soltanto** al checkpoint 175:

- rilettura globale di `merenda/`;
- audit duplicazioni, frammentazione, gerarchia, routing e collegamenti;
- attenzione particolare ai sette documenti modificati nel batch 151–175;
- nessuna FASE 15;
- nessuna introduzione di Formalife;
- nessuna modifica ai file congelati senza autorizzazione;
- eseguire i validator locali e documentare l'esito in `reviews/CHECKPOINT_175.md`.

Dopo la FASE 14, se 176–200 non dispongono già degli asset tecnici necessari, impostare l'handoff a **CODEX** per l'acquisizione del batch 176–200.

## Validazione e blocchi

- Nessun blocco semantico residuo dal batch 151–175.
- Nessun fallback ASR richiesto nel batch.
- Nessun contenuto 176+ acquisito nel batch tecnico 151–175.
- Baseline validator tecnica nota prima dell'ingestione: 841 segnalazioni preesistenti (836 disallineamenti d'ordine/stato, 3 divergenze storiche dei congelati rispetto al tag v1.0, 2 etichette STATUS non riconosciute).
- La validazione locale completa deve essere rieseguita da Claude durante FASE 14.
