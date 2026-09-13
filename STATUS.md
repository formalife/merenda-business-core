# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primi 125 contenuti processati semanticamente; checkpoint 125 raggiunto e refactor FASE 14 completato.

## Fase corrente

**Checkpoint 125 completato — elaborazione semantica e FASE 14 (refactor KB) concluse. FASE 15 non eseguita (non dovuta a questo checkpoint).**

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 125
- STUDIATO / integrati nella KB: 121
- ESCLUSO dalla dottrina attiva: 4
- Da processare: 343
- Video completati: 121
- Video rimanenti: 343
- Corpus completo: NO
- Asset tecnici 101–125: ACQUISITI 25/25
- Elaborazione semantica 101–125: 25/25 completati

## Workflow attivo — v1.1

- CODEX / script locale: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: fase 14 ogni 25; fase 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 125
- Ultimo audit tassonomia completato: 100
- Checkpoint raggiunto: 125
- Checkpoint Claude richiesto ora: NO
- Refactor richiesto ora: NO — FASE 14 completata in questo checkpoint
- FASE 15 richiesta ora: NO — non dovuta a questo checkpoint (resta al contenuto 150) e non eseguita
- Prossimo refactor KB: 150
- Prossimo audit tassonomia: 150

Documento di checkpoint: `reviews/CHECKPOINT_125.md` (aggiornato con la sezione "Esito FASE 14").

## Agente richiesto

**CODEX**

## Next Action

FASE 14 completata su questo checkpoint. Il corpus non è completo (343 contenuti da processare): secondo `system/HANDOFFS.md` (Claude → ingestione), si verifica ora la disponibilità degli asset del prossimo contenuto.

Verificato localmente: `sources/transcripts/dwfknCGx8UI.*` non esiste. Gli asset del batch 126–150 non risultano acquisiti.

Next action per CODEX:

1. acquisire tecnicamente il batch 126–150 secondo il workflow canonico (fase 7 e supporto meccanico alle fasi 8/10), a partire da `dwfknCGx8UI`;
2. aggiornare `STATUS.md` indicando quanti video del batch sono acquisiti ma non ancora studiati e impostare `Agente richiesto: CHATGPT`.

Non acquisire il corpus oltre il batch indicato; non modificare stati `STUDIATO`/`ESCLUSO`; non alterare l'ordine della queue.

## Primo pendente

`dwfknCGx8UI` — *MARKETING | Diventare il punto di riferimento per il tuo Settore [Jay Abraham]* — `04_marketing` — posizione 126 della queue.

Verificata l'assenza di asset `sources/transcripts/dwfknCGx8UI.*` durante questo checkpoint. Batch 126–150 non avviato.

## Validazione e blocchi

FASE 14 (refactor KB) eseguita su questo checkpoint: audit completo di tutti i 40 file `.md` di `merenda/` (35 documenti di contenuto + 11 README + INDEX). Nessuna duplicazione sostanziale rilevata; le sovrapposizioni segnalate da `reviews/CHECKPOINT_125.md` sono risultate complementari e sono state lasciate invariate. Unica modifica: correzione del testo di un link in `merenda/03_offerta/README.md` per farlo coincidere col titolo reale del documento collegato. Controllo programmatico di link relativi e anchor su tutta `merenda/`: 0 errori. Nessun file orfano. Dettagli in `reviews/CHECKPOINT_125.md` (sezione "Esito FASE 14").

`scripts/validate_project.py` eseguito dopo il refactor: NON PASSA per le stesse anomalie preesistenti già documentate prima di questo checkpoint (confronto dei file congelati con il tag v1.0 — MASTER_PLAN.md, system/HANDOFFS.md e system/FROZEN_FILES.md differiscono già nella base — e disallineamenti d'ordine tra catalogo, VIDEO_INDEX e queue). Nessuna nuova anomalia introdotta dalla FASE 14. Script, ordinamenti e file congelati preesistenti lasciati invariati nel perimetro di questo task.

Nessuna nuova dottrina introdotta. FASE 15 non eseguita (non dovuta a questo checkpoint).
