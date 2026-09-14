# Checkpoint 175 — handoff a Claude Code (FASE 14)

## Stato al raggiungimento della soglia

- Video individuati: **468**
- Contenuti processati semanticamente: **175**
- `STUDIATO`: **169**
- `ESCLUSO`: **6**
- `DA STUDIARE`: **293**
- Batch tecnico 151–175: **25/25** transcript utilizzabili
- Batch semantico 151–175: **25/25 completato**
- Corpus completo: **NO**
- Checkpoint dovuto: **175 — sola FASE 14**
- Prossimo audit tassonomia: **200**

Questo documento è l'handoff pre-checkpoint. Claude Code deve eseguire e documentare qui la FASE 14 finale del checkpoint 175. **Non eseguire FASE 15**.

## Integrazioni dottrinali del batch 151–175

I contenuti realmente incrementali sono stati fusi nei documenti esistenti secondo MERGE, NON APPEND:

- `merenda/06_vendita/prequalifica-follow-up-decisori.md`
  - guidare con fermezza il cliente dopo decisioni precedenti fallite;
  - separare convinzione interna del venditore e linguaggio esterno.
- `merenda/03_offerta/offerta-a-risposta-diretta.md`
  - tradurre qualità interna non percepibile in un'offerta valutabile;
  - costruire bundle attorno al risultato d'uso.
- `merenda/09_business/numeri-cassa-e-crescita.md`
  - collegare CAC/LTV alla durata minima profittevole della relazione.
- `merenda/03_offerta/front-end-e-back-end.md`
  - proporre sistematicamente upsell pertinenti senza interpretar-ne il rifiuto maggioritario come prova di inutilità.
- `merenda/09_business/marketing-del-personale.md`
  - distinguere errore di inserimento da errore di trattenimento;
  - verificare l'idoneità sul lavoro reale.
- `merenda/00_fondamenti/marketing-first.md`
  - strumenti come acceleratori, non sostituti del giudizio;
  - customer experience come marketing operativo.
- `merenda/04_marketing/gerarchia-domanda-e-canali.md`
  - quando vincoli esterni restringono l'acquisizione aumenta il peso economico di referral, conversione, retention e LTV.

Gli altri contenuti del batch hanno confermato principi già presenti o casi già coperti e sono stati documentati nelle rispettive `.review.md` senza duplicare la KB.

## Routing semantico finale 151–175

| Pos. | ID | Categoria finale | KB incrementale |
|---:|---|---|---|
| 151 | `8R8NR6nqhJY` | 06_vendita | sì |
| 152 | `-oYSpJrj024` | 03_offerta | sì |
| 153 | `v6WWqNpNSpE` | 02_posizionamento | no |
| 154 | `_6QCnb6Oj1Y` | 09_business | sì |
| 155 | `Z7FhdrG-fOw` | 03_offerta | sì |
| 156 | `5awWbxibHIE` | 09_business | sì |
| 157 | `G6j8xbargKY` | 08_brand | no |
| 158 | `LMzKVDWrGlk` | 10_casi_studio | no |
| 159 | `-6L9gCbicjk` | 07_copy_comunicazione | no |
| 160 | `I2RBYMESAsk` | 02_posizionamento | no |
| 161 | `mkhp-EGSORA` | 10_casi_studio | no |
| 162 | `NTy1ZHQ8NYs` | 10_casi_studio | no |
| 163 | `5XW0s6NizEE` | 10_casi_studio | no |
| 164 | `NCQ1lX3S5wk` | 10_casi_studio | no |
| 165 | `AjvfyImTiPI` | 10_casi_studio | no |
| 166 | `qIG_0TMol8s` | 00_fondamenti | sì |
| 167 | `fpao23ulhkQ` | 02_posizionamento | no |
| 168 | `9zvNhQOpRI4` | 00_fondamenti | no |
| 169 | `oQXsQzrIv2M` | 04_marketing | sì |
| 170 | `PKgWYVvme2s` | 00_fondamenti | sì |
| 171 | `degAX4kvT-0` | 03_offerta | sì |
| 172 | `YvfN2NUwXtY` | 10_casi_studio | no |
| 173 | `aw3Fu_LTH34` | 00_fondamenti | no |
| 174 | `znVPLom4j70` | 10_casi_studio | no |
| 175 | `y-8LBcQsS9M` | 10_casi_studio | no |

## Indicazioni per FASE 14

Claude Code deve:

1. rileggere integralmente `merenda/`;
2. verificare in particolare i sette documenti modificati nel batch;
3. eliminare eventuali duplicazioni, frammentazione o formulazioni ridondanti;
4. controllare gerarchia, routing, README, INDEX e collegamenti;
5. verificare che le fonti più recenti prevalgano dove realmente incompatibili;
6. mantenere esempi e casi subordinati ai principi generali;
7. non introdurre conoscenza esterna;
8. non introdurre Formalife;
9. non modificare file congelati senza autorizzazione;
10. **non eseguire FASE 15** al checkpoint 175;
11. eseguire i validator locali e documentare eventuali anomalie nuove rispetto alla baseline nota;
12. aggiornare questo documento con l'esito finale della FASE 14 e aggiornare `STATUS.md`.

Dopo FASE 14, se gli asset tecnici 176–200 non risultano già disponibili, l'handoff corretto è a **CODEX** per la nuova acquisizione tecnica.

## Baseline tecnica nota

Dal batch tecnico 151–175:

- 25/25 acquisiti;
- 0 fallback ASR;
- 0 errori;
- nessun contenuto 176+ acquisito;
- baseline validator riportata: 841 segnalazioni preesistenti, di cui 836 disallineamenti d'ordine/stato, 3 divergenze storiche dei congelati rispetto al tag v1.0 e 2 etichette STATUS non riconosciute.

Questa baseline va verificata localmente da Claude; non correggere automaticamente anomalie storiche fuori scope.

## Governance

- Nessun file congelato è stato intenzionalmente modificato nel batch semantico.
- Formalife non è stato introdotto nella KB.
- Nessuna fonte esterna al canale ufficiale è stata usata per arricchire la dottrina.
- Il batch 151–175 è stato elaborato in ordine canonico con una review per video.
