# Checkpoint 225 — pre-handoff FASE 14

Stato raggiunto dopo completamento tecnico e semantico del batch **201–225**.

Branch semantico: `semantic-201-225`  
Base tecnica del batch: `557132457a3616a7040101d09abb03624f26f212`  
Ultimo commit semantico prima del checkpoint: `3a1b8ad5239e10a798d25e0cf2107312c6776a3d`

## Stato corpus

- Video individuati: **468**
- Contenuti processati semanticamente: **225**
- `STUDIATO`: **219**
- `ESCLUSO`: **6**
- `DA STUDIARE`: **243**
- Corpus completo: **NO**
- Batch tecnico 201–225: **25/25 utilizzabili**
- Batch semantico 201–225: **25/25 completato**
- Review create nel batch: **25**
- Nuovi `ESCLUSO` nel batch: **0**
- Nessun contenuto 226+ processato semanticamente.

## Novelty yield 201–225

**6/25 = 24%** di contenuti incrementali.

Contenuti che hanno modificato la KB:

1. **201 — `vD7zMl6YXzs`** — granularità economica per sorgente di acquisizione e, quando confrontabile, per venditore.
2. **211 — `WtyLO1gMqVI`** — concentrare risorse limitate su una coorte finita di prospect ad alta priorità.
3. **212 — `TrY_mDjr7I4`** — scala coerente di offerte nella prima relazione: ingresso → add-on → riduzione del rischio → ponte → continuità.
4. **216 — `of0ppir9sq4`** — evitare calendari promozionali prevedibili che insegnano al mercato ad aspettare lo sconto.
5. **220 — `HwlqYf73Ctk`** — ridurre il rischio reputazionale di chi presenta un referral e selezionare/promuovere referrer appropriati.
6. **225 — `WCP26HC6wd0`** — formulazione più recente del front-end: ridurre la barriera con una porzione d'ingresso oppure con forte risk reversal sul prodotto pieno, senza rendere obbligatorio lo sconto del core offer.

Gli altri **19/25** sono stati letti e deduplicati senza gonfiare la KB.

## File KB modificati

1. `merenda/01_mercato/appropriatezza-clienti.md`
2. `merenda/03_offerta/front-end-e-back-end.md`
3. `merenda/03_offerta/prezzo-premium-e-percezione-del-valore.md`
4. `merenda/05_acquisizione/referral-e-soddisfazione.md`
5. `merenda/09_business/numeri-cassa-e-crescita.md`

Nessun nuovo file KB è stato creato nel batch.

## Routing finale 201–225

| Pos. | ID | Categoria finale | Novelty |
|---:|---|---|---|
| 201 | `vD7zMl6YXzs` | `09_business` | SÌ |
| 202 | `QJUjdX0zglA` | `05_acquisizione` | no |
| 203 | `uayjrQ6GWQc` | `05_acquisizione` | no |
| 204 | `nAqH9enAM1U` | `05_acquisizione` | no |
| 205 | `R22IWnVNYus` | `09_business` | no |
| 206 | `zfmFg5L7VDU` | `06_vendita` | no |
| 207 | `saBj3DmgsCg` | `05_acquisizione` | no |
| 208 | `-lqseFTfCzk` | `09_business` | no |
| 209 | `C4IfIcOkwdE` | `05_acquisizione` | no |
| 210 | `aEv9F66CZqA` | `09_business` | no |
| 211 | `WtyLO1gMqVI` | `01_mercato` | SÌ |
| 212 | `TrY_mDjr7I4` | `03_offerta` | SÌ |
| 213 | `_CPcSMMzIY0` | `06_vendita` | no |
| 214 | `I-YCFdXNSO0` | `02_posizionamento` | no |
| 215 | `bLmGe86nDAA` | `05_acquisizione` | no |
| 216 | `of0ppir9sq4` | `03_offerta` | SÌ |
| 217 | `bY6Lb0Dld88` | `05_acquisizione` | no |
| 218 | `JQXoKKwneBQ` | `05_acquisizione` | no |
| 219 | `ji8rHHO_KHY` | `05_acquisizione` | no |
| 220 | `HwlqYf73Ctk` | `05_acquisizione` | SÌ |
| 221 | `G0fxszrL9_M` | `06_vendita` | no |
| 222 | `0rM-F7msbkA` | `04_marketing` | no |
| 223 | `sUkGSSqTq3c` | `05_acquisizione` | no |
| 224 | `pJZSih3Lguw` | `03_offerta` | no |
| 225 | `WCP26HC6wd0` | `03_offerta` | SÌ |

Distribuzione finale del batch:

- `01_mercato`: 1
- `02_posizionamento`: 1
- `03_offerta`: 4
- `04_marketing`: 1
- `05_acquisizione`: 11
- `06_vendita`: 3
- `09_business`: 4

Tutti i 25 erano preliminarmente instradati in `05_acquisizione`. La dispersione finale conferma che il routing preliminare di coda non deve sostituire la classificazione semantica.

## A/B/C — verifica empirica sul primo batch classificato

Classificazione pre-batch prodotta al checkpoint 200:

- **A:** 2 contenuti (206, 208) → **0/2 incrementali**
- **B:** 19 contenuti → **5/19 incrementali**
- **C:** 4 contenuti (218, 219, 224, 225) → **1/4 incrementale**

Il dato più importante è **225**: era classe C perché short, ma ha introdotto una formulazione del **17 novembre 2025** più recente e prevalente sul front-end.

Conclusione operativa:

- la classe C ha funzionato correttamente solo perché è rimasta **FAST REVIEW, non SKIP**;
- la regola di promozione C → B/A quando emerge novità resta obbligatoria;
- la recenza dovrebbe essere rivalutata come possibile segnale che può impedire a uno short di essere classificato automaticamente C;
- il singolo batch non basta per riscrivere la governance, ma è evidenza concreta da esaminare in FASE 14 e nei checkpoint successivi.

## Limite tecnico video 218

Per `JQXoKKwneBQ` il JSON3 termina **125,61 s oltre** la durata metadata.

La review semantica:

- ha usato il testo come fonte utilizzabile;
- non ha inventato offset o correzioni;
- non ha usato timestamp/keyframe della porzione problematica come evidenza precisa.

Il limite resta documentato in `sources/queue/acquisition-progress.md` e nella review del video.

## Verifiche remote eseguite

Confronto `557132457a3616a7040101d09abb03624f26f212...semantic-201-225`:

- branch semantico avanti di **25 commit**, indietro di **0**;
- esattamente **25 nuovi file `.review.md`**;
- modifiche semantiche limitate a catalogo/indice/queue + i 5 file KB sopra;
- **nessun file frozen modificato**;
- nessun asset/review 226+ introdotto semanticamente.

Confronto `main...semantic-201-225` prima del checkpoint:

- `main`: `6304bdc7d3ae4d3fb6d2a22e94f87082eb727bc3`
- branch semantico avanti di **51 commit**, indietro di **0**
- composizione attesa: **26 commit tecnici + 25 commit semantici**.

## Validator

Ultima validazione locale certa, eseguita nel batch tecnico prima della semantica:

```
python3 scripts/validate_project.py → 841 warning, identici alla baseline
git diff --check → OK
```

Le 841 segnalazioni sono la baseline storica già documentata nel checkpoint 200 e nel report tecnico.

Il connettore GitHub usato per la revisione semantica non può eseguire il validator sul working tree locale. **Claude Code deve quindi rieseguire localmente il validator prima di qualunque refactor FASE 14 e dopo le proprie modifiche**, confrontando l'output con la baseline 841 e separando warning storici da eventuali nuove anomalie.

## FASE 14 dovuta a 225

Il prossimo agente deve essere **CLAUDE CODE**.

Obiettivi:

1. rileggere l'intera KB `merenda/` dopo le integrazioni 201–225;
2. applicare MERGE, NOT APPEND;
3. cercare duplicazioni, sovrapposizioni, file divenuti troppo estesi, confini da chiarire, link/orfani e gerarchia principio → procedura → esempio;
4. controllare in particolare:
   - crescita di `front-end-e-back-end.md` dopo le due integrazioni 212 e 225;
   - coerenza fra front-end, offerta a risposta diretta, pricing e funnel;
   - crescita di `numeri-cassa-e-crescita.md` dopo il 201;
   - relazione fra `appropriatezza-clienti.md` e concentrazione su coorti prioritarie;
   - relazione fra referral, garanzia/risk reversal e qualità dei clienti;
   - prevalenza delle fonti più recenti, soprattutto la fonte 225 del 2025 rispetto alle formulazioni 2022;
5. esaminare il falso negativo A/B/C del 225 e decidere se aggiornare `scripts/classify_residual.py` e/o l'artefatto di classificazione residua. Nessuna modifica ai file frozen senza autorizzazione;
6. non eseguire FASE 15: il prossimo audit tassonomia è dovuto a 250;
7. non processare semanticamente contenuti 226+ durante il checkpoint.

## Handoff

- **Corpus completo:** NO
- **Agente richiesto:** CLAUDE CODE
- **Checkpoint:** 225 — **FASE 14**
- **Audit tassonomia:** non dovuto fino a 250
- **Contenuti semantici completati:** 225
- **Primo contenuto non processato:** posizione 226 della queue
- **Nessun 226+ da processare prima della chiusura della FASE 14.**
