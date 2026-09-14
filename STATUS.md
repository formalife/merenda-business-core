# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti 1–150 processati semanticamente; checkpoint 125 e FASE 14 completati; batch 126–150 completato; checkpoint 150 pronto per FASE 14 + FASE 15.

## Fase corrente

**Checkpoint 150 — elaborazione semantica 126–150 completata 25/25. In attesa di CLAUDE CODE per FASE 14 + FASE 15.**

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 150
- STUDIATO / integrati nella KB: 144
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 318
- Corpus completo: NO
- Asset tecnici 101–125: ACQUISITI 25/25
- Elaborazione semantica 101–125: 25/25 completati
- Asset 126–150 utilizzabili: 25/25 — 22 acquisiti da YouTube + 3 fallback ASR locali
- Elaborazione semantica 126–150: 25/25 completati

## Workflow attivo — v1.1

- CODEX / script locale: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: fase 14 ogni 25; fase 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 125
- Ultimo audit tassonomia completato: 100
- Prossimo checkpoint: 150 (FASE 14 + FASE 15)
- Checkpoint Claude richiesto ora: YES
- Dopo il checkpoint 150: prossimo refactor 175; prossimo audit tassonomia 200.

Documento checkpoint corrente: `reviews/CHECKPOINT_150.md`.

Documento precedente: `reviews/CHECKPOINT_125.md`.

## Batch 126–150

Acquisizione tecnica completata 25/25.

- 22 transcript acquisiti da YouTube
- 3 transcript recuperati con fallback ASR locale: `jcVKVKvy78k`, `joY6sigynis`, `ijVoIMF_gn8`
- 0 contenuti semanticamente pendenti nel batch
- nessun blocco tecnico residuo per 126–150

La revisione semantica è stata completata in ordine canonico fino a:

- `VN1d2qBc0U0` — *Cos'è il MARKETING e perchè NON è La Mucca Viola [Corso Completo di Marketing]* — posizione 150.

## Agente richiesto

**CLAUDE CODE**

## Next Action

Eseguire **FASE 14 + FASE 15 al checkpoint 150**.

FASE 14:
- audit/refactor globale della KB per duplicazioni, frammentazione, gerarchia, dimensione dei file, routing e collegamenti;
- preservare il significato e la precedenza delle fonti più recenti;
- non introdurre conoscenza esterna;
- non introdurre Formalife.

FASE 15:
- audit globale della tassonomia;
- verificare categorie, routing e ordine futuro della queue;
- aggiornare coerentemente queue canonica, catalogo e VIDEO_INDEX se necessario;
- determinare il corretto prossimo batch tecnico soltanto dopo l'audit.

**BLOCCO OPERATIVO:** non acquisire i contenuti 151–175 prima della conclusione della FASE 15, perché l'audit tassonomico può modificarne ordine e routing.

## Primo pendente pre-audit

Nella queue corrente il primo `DA STUDIARE` successivo al batch è `8R8NR6nqhJY` — *"I Already Tried It and It Didn't Work" — The Excuse That Kills Your Revenue*.

Questo riferimento è soltanto il primo pendente **prima** della FASE 15. Non avviarne l'acquisizione finché Claude non ha completato l'audit tassonomico del checkpoint 150.

## Validazione e blocchi

Le anomalie note di `scripts/validate_project.py` restano quelle preesistenti già documentate: confronto file congelati vs tag v1.0 e disallineamenti d'ordine tra catalogo, VIDEO_INDEX e queue.

Il blocco sui transcript 143/148/149 è risolto. Nessun nuovo blocco introdotto dal batch 126–150.
