# PROJECT STATUS

## Stato generale

ACTIVE — fasi 1–6 complete; contenuti 1–163 processati semanticamente; checkpoint 150 (FASE 14 + FASE 15) completato da Claude Code; corpus ancora incompleto; batch tecnico 151–175 acquisito (25/25 transcript italiani utilizzabili), pronto per CHATGPT.

## Fase corrente

**Revisione semantica 151–175 in corso.** Completati 151–163/175. `5XW0s6NizEE` studiato come caso Urus già coperto, senza duplicazioni. Prossima azione: fasi 8–13 su `NCQ1lX3S5wk` (posizione canonica 164). Il checkpoint 150 resta concluso.

## Corpus

- Video individuati: 468
- Contenuti processati semanticamente: 163
- STUDIATO / integrati nella KB: 157
- ESCLUSO dalla dottrina attiva: 6
- Da processare: 305
- Corpus completo: NO
- Asset 126–150 utilizzabili: 25/25 — 22 acquisiti da YouTube + 3 fallback ASR locali
- Elaborazione semantica 126–150: 25/25 completati
- Nessun blocco residuo dal fallback ASR 143/148/149

## Workflow attivo — v1.1

- CODEX / script locale: acquisizione tecnica a batch e sincronizzazione meccanica.
- CHATGPT: revisione semantica e fasi 8–13.
- CLAUDE CODE: fase 14 ogni 25; fase 14 + 15 ogni 50.

## Checkpoint

- Ultimo refactor KB completato: 150
- Ultimo audit tassonomia completato: 150
- Prossimo refactor: 175
- Prossimo audit tassonomia: 200
- Checkpoint Claude richiesto ora: NO

Documento del checkpoint corrente: `reviews/CHECKPOINT_150.md`. Documento precedente: `reviews/CHECKPOINT_125.md`.

## Esito checkpoint 150 (sintesi)

FASE 14: KB riletta integralmente (35 file di contenuto + 11 README + INDEX). Tutte le integrazioni del batch 126–150 (marketing di settore, Sisma, owned demand, quantità/qualità lead, autorità/credibilità/fiducia, information marketing lungo il ciclo cliente, materiali per decisori diversi, direct response distributivo, sell-in/sell-through) risultano già correttamente fuse nei documenti corretti. Corretto un solo problema strutturale: sezione "Collegamenti" fuori posizione in `merenda/05_acquisizione/information-marketing.md`, spostata in fondo al file. Nessun'altra duplicazione, nessun file creato/fuso/eliminato. 0 link rotti, 0 file orfani su 47 file `.md`.

FASE 15: tassonomia a 11 categorie confermata adeguata, nessuna categoria unita/divisa/rinominata. Riclassificati 9 contenuti `DA STUDIARE` (su 318, letti tutti) il cui titolo indica con sufficiente sicurezza un caso/azienda specifico o un tema più preciso: 8 verso `10_casi_studio` (Skechers, Mike's Hot Honey, Ferrero, Lamborghini Urus, gommista, All'Antico Vinaio, Coca-Cola, azienda farmaceutica) e 1 verso `09_business` (errori di assunzione). Sincronizzati `sources/catalog.json`, `sources/VIDEO_INDEX.md`, `sources/queue/QUEUE.md`. A differenza del checkpoint 100, questi contenuti **non** sono stati spostati in fondo alla sezione né la coda è stata rinumerata, per non aggravare il disallineamento d'ordine preesistente fra i tre file (836 righe di scostamento, invariato prima/dopo il checkpoint). Dettagli completi in `reviews/CHECKPOINT_150.md`.

## Batch 126–150 (completato)

- 22 transcript acquisiti da YouTube, 3 con fallback ASR locale: `jcVKVKvy78k`, `joY6sigynis`, `ijVoIMF_gn8`
- Revisione semantica completata in ordine canonico fino a `VN1d2qBc0U0` — *Cos'è il MARKETING e perchè NON è La Mucca Viola* — posizione 150.

## Agente richiesto

**CHATGPT**

## Next Action

Continuare il batch **151–175** con `NCQ1lX3S5wk` — *Il Segreto del Gommista di Successo #Shorts* — posizione canonica 164 della queue. I video 151–163 sono completati semanticamente.

- Asset acquisiti/tentati: **25/25**; `ACQUIRED`: **25**.
- Transcript italiani immediatamente utilizzabili: **25**; fallback ASR richiesti: **0**; errori: **0**; pending: **0**.
- Metadata del canale ufficiale verificati, JSON3 grezzi e Markdown normalizzati disponibili in `sources/transcripts/`.
- Nessun keyframe candidato emerso dalla ricerca meccanica di riferimenti visuali espliciti; valutazione visuale selettiva rimessa alla revisione ChatGPT.
- Revisione semantica in corso: **13/25** contenuti del batch completati. Ultimo: `5XW0s6NizEE` → `10_casi_studio`, `STUDIATO`; nessuna nuova dottrina. Contenuti semanticamente processati: **163**.
- `sources/queue/acquisition-progress.md` rappresenta il batch corrente; `sources/queue/next-batch.txt` contiene esattamente i suoi 25 URL. I campi data «da acquisire» di VIDEO_INDEX non sono un inventario degli asset: i metadata aggiornati sono nei rispettivi `.info.json`.
- Branch tecnico: `acquisition-151-175`, base `7f0c20c03f7d069d46447c81c76c7ad2a0f537d9`; un commit separato per video. Nessuna acquisizione del contenuto 176 o successivi.

Ordine e categoria del batch 151–175, confermati dopo l'audit tassonomico del checkpoint 150 (elenco completo con categorie aggiornate in `reviews/CHECKPOINT_150.md`):

1. `8R8NR6nqhJY` — "I Already Tried It and It Didn't Work" — The Excuse That Kills Your Revenue (04_marketing)
2. `-oYSpJrj024` (04_marketing)
3. `v6WWqNpNSpE` (04_marketing)
4. `_6QCnb6Oj1Y` (04_marketing)
5. `Z7FhdrG-fOw` (04_marketing)
6. `5awWbxibHIE` (09_business — riclassificato in questo checkpoint)
7. `G6j8xbargKY` (04_marketing)
8. `LMzKVDWrGlk` (10_casi_studio — riclassificato)
9. `-6L9gCbicjk` (04_marketing)
10. `I2RBYMESAsk` (04_marketing)
11. `mkhp-EGSORA` (10_casi_studio — riclassificato)
12. `NTy1ZHQ8NYs` (10_casi_studio — riclassificato)
13. `5XW0s6NizEE` (10_casi_studio — riclassificato)
14. `NCQ1lX3S5wk` (10_casi_studio — riclassificato)
15. `AjvfyImTiPI` (10_casi_studio — riclassificato)
16. `qIG_0TMol8s` (04_marketing)
17. `fpao23ulhkQ` (04_marketing)
18. `9zvNhQOpRI4` (04_marketing)
19. `oQXsQzrIv2M` (04_marketing)
20. `PKgWYVvme2s` (04_marketing)
21. `degAX4kvT-0` (04_marketing)
22. `YvfN2NUwXtY` (04_marketing)
23. `aw3Fu_LTH34` (04_marketing)
24. `znVPLom4j70` (04_marketing)
25. `y-8LBcQsS9M` (04_marketing)

Agente richiesto: CHATGPT. Eseguire le fasi 8–13 in ordine canonico. Dopo il completamento semantico di tutti i contenuti 151–175, prossimo checkpoint CLAUDE CODE: **175 — sola FASE 14**; prossimo audit tassonomia a 200.

## Validazione e blocchi

`scripts/validate_project.py`: output invariato rispetto alla base, con 841 segnalazioni preesistenti: 836 disallineamenti d’ordine/stato, 3 divergenze dei congelati rispetto al tag v1.0 e 2 etichette dei contatori STATUS non riconosciute. Nessuna riparazione automatica eseguita.

Controlli specifici del batch superati: 25 ID esatti, provenienza ufficiale, corrispondenza JSON3/Markdown, nessun asset 176+, KB e congelati invariati, catalogo/VIDEO_INDEX/queue invariati, stati semantici invariati (144 STUDIATO, 6 ESCLUSO, 318 DA STUDIARE). `git diff --check` superato. Nessun blocco tecnico o fallback richiesto.
