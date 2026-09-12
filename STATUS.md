# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; ingestion loop in corso con workflow v1.1.

## Fase corrente

Prossimo video da elaborare semanticamente: `Wk1Se1AeInw`.

Completati i primi otto video della queue. Il video 8 (`27Bt3nswSyg`) è stato integrato nella KB con un nuovo documento sull'authority marketing e routing trasversale da brand, marketing, acquisizione e vendita.

## Corpus

- Video individuati: 468
- Video completati: 8
- Video rimanenti: 460
- Corpus completo: NO

296 video, 109 Shorts, 63 dirette; nessun duplicato tra le tre schede. Scansione del 2026-09-12.

Gli asset tecnici risultano acquisiti in anticipo per 25 video. L'acquisizione anticipata non conta come completamento: un video diventa `STUDIATO` dopo revisione semantica e merge nella KB.

## Workflow attivo — v1.1

- CODEX / locale: acquisizione tecnica a batch (metadata, transcript, normalizzazione, keyframe candidati).
- CHATGPT: revisione semantica e fasi 8–13 sui video già acquisiti.
- CLAUDE CODE: fase 14 ogni 25 completati; fase 15 ogni 50; fasi 16–22 a corpus completo.

## Checkpoint

- Ultimo refactor KB: nessuno
- Prossimo refactor KB: 25 video completati
- Ultimo audit tassonomia: nessuno
- Prossimo audit tassonomia: 50 video completati
- Checkpoint Claude richiesto: NO

## Agente richiesto

CHATGPT

## Next Action

Processare `Wk1Se1AeInw`, primo pendente della queue con asset già acquisiti.

Per ogni video:
1. leggere transcript normalizzato;
2. risolvere o segnalare soltanto incomprensioni sostanziali;
3. valutare i keyframe solo se aggiungono informazione non ricostruibile dall'audio;
4. confrontare con la KB pertinente;
5. MERGE, NON APPEND;
6. aggiornare catalogo, VIDEO_INDEX, queue e STATUS.

Continuare fino al video 25, salvo esaurimento degli asset tecnici. Al video 25 passare a Claude Code per fase 14.

## Blocchi / intervento umano

Nessun blocco per il video 8.

Restano non bloccanti le verifiche manuali già documentate nelle revisioni precedenti (mappa Disney del primo corso e altri dubbi locali non consolidati).

## Verifica operativa

Workflow aggiornato su GitHub: Codex non deve più consumare token per la distillazione semantica ordinaria. ChatGPT lavora sulla stessa KB remota; Claude resta responsabile dei checkpoint strutturali.
