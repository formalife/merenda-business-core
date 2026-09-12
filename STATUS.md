# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primo batch semantico completato; checkpoint Claude richiesto.

## Fase corrente

**FASE 14 — Refactor KB al checkpoint 25.**

I primi 25 contenuti della queue sono stati processati.

## Corpus

- Video individuati: 468
- Contenuti processati: 25
- STUDIATO / integrati o classificati nella KB: 24
- ESCLUSO dalla dottrina attiva: 1
- Da processare: 443
- Corpus completo: NO

Il contenuto escluso è `Wk1Se1AeInw`, lezione di Jay Abraham ospitata sul canale senza intervento sostanziale di Frank.

## Workflow attivo — v1.1

- CODEX / locale: acquisizione tecnica a batch (metadata, transcript, normalizzazione, keyframe candidati).
- CHATGPT: revisione semantica e fasi 8–13 sui video acquisiti.
- CLAUDE CODE: fase 14 ogni 25 contenuti processati; fase 15 ogni 50; fasi 16–22 a corpus completo.

## Checkpoint

- Ultimo refactor KB: nessuno
- Refactor KB richiesto ora: 25
- Ultimo audit tassonomia: nessuno
- Prossimo audit tassonomia: 50
- Checkpoint Claude richiesto: YES

## Agente richiesto

CLAUDE CODE

## Next Action

Leggere:

1. `00_START_HERE.md`
2. `CLAUDE.md`
3. `STATUS.md`
4. `reviews/CHECKPOINT_025.md`

Poi eseguire **soltanto la fase 14**: refactor della Knowledge Base senza aggiungere nuova dottrina.

Al termine:

- aggiornare routing e link se necessario;
- mantenere invariati i significati;
- aggiornare questo `STATUS.md`;
- impostare `Agente richiesto: CODEX`, perché il prossimo transcript non è ancora acquisito su GitHub;
- fare commit.

## Prossimo contenuto dopo il checkpoint

`zWVDQEuw_yI` — *MARKETING | Perchè per un Infomercial il settore non fa differenza?*

Il transcript non è ancora presente nel repository remoto.

## Blocchi / intervento umano

Nessun blocco semantico aperto nel batch 8–25.

Restano soltanto le verifiche manuali non bloccanti già documentate nelle revisioni dei primi video.

## Verifica operativa

Catalogo GitHub verificato dopo il video 25:

- `STUDIATO`: 24
- `ESCLUSO`: 1
- `DA STUDIARE`: 443

La queue è pronta per il checkpoint strutturale Claude.
