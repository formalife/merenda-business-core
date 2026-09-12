# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; primo batch semantico completato; checkpoint 25 (fase 14) completato.

## Fase corrente

**FASE 14 completata al checkpoint 25.** In attesa del prossimo batch di acquisizione (CODEX) per riprendere fasi 7–13 (CHATGPT).

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

- Ultimo refactor KB: 25 (completato)
- Refactor KB richiesto ora: no (prossimo a 50, insieme all'audit tassonomia)
- Ultimo audit tassonomia: nessuno
- Prossimo audit tassonomia: 50
- Checkpoint Claude richiesto: NO

## Agente richiesto

CODEX

## Refactor eseguito al checkpoint 25

`merenda/02_posizionamento/differenziazione-operativa.md` era cresciuto a 194 righe mescolando principi generali con sei esempi aziendali (Biraghi, Guapo, Burgez, Mike's Hot Honey, Il Toro, McDonald's).

Separato in:

- `merenda/02_posizionamento/differenziazione-operativa.md` — principi generali (83 righe);
- `merenda/02_posizionamento/esempi-di-differenziazione.md` — esempi aziendali (113 righe, nuovo file).

Nessun contenuto è stato riassunto, riscritto o eliminato: solo spostato. Aggiornati di conseguenza:

- `merenda/02_posizionamento/README.md` (routing al nuovo file);
- `merenda/05_acquisizione/README.md` (link con anchor al caso Guapo, spostato nel nuovo file).

Verificati tutti i link interni della KB (script di controllo file+anchor): nessun link rotto.

Le altre sezioni della KB (00–01, 03–10) sono state lette integralmente e risultano già ben organizzate: nomi, README, confini tra sezioni e collegamenti incrociati non richiedevano interventi al checkpoint 25.

## Next Action

Prossimo contenuto in queue: `zWVDQEuw_yI` — *MARKETING | Perchè per un Infomercial il settore non fa differenza?*. Il transcript non è ancora presente nel repository remoto.

Richiedere a **CODEX** l'acquisizione tecnica del prossimo batch (a partire da `zWVDQEuw_yI`), poi restituire il controllo a **CHATGPT** per le fasi 8–13.

Al prossimo checkpoint (50 contenuti processati): eseguire fase 14 (refactor) e fase 15 (audit globale della tassonomia).

## Blocchi / intervento umano

Nessun blocco semantico aperto nel batch 8–25. Restano soltanto le verifiche manuali non bloccanti già documentate nelle revisioni dei primi video.
