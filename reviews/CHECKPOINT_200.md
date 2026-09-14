# Checkpoint 200 — pre-handoff FASE 14 + FASE 15

## Scopo

Questo documento consegna a Claude Code il corpus semanticamente processato fino al contenuto 200.

**Checkpoint richiesto: FASE 14 + FASE 15.**

Non processare contenuti 201+ durante il checkpoint. Non introdurre Formalife. Non modificare file frozen senza autorizzazione esplicita.

## Stato al raggiungimento della soglia

- Video individuati: **468**
- Contenuti processati semanticamente: **200**
- `STUDIATO`: **194**
- `ESCLUSO`: **6**
- `DA STUDIARE`: **268**
- Batch tecnico 176–200: **25/25 utilizzabile**
- Batch semantico 176–200: **25/25 completato**
- Review create nel batch: **25**
- Corpus completo: **NO**
- Ultimo refactor globale completato: **175**
- Ultimo audit tassonomia completato: **150**
- Checkpoint dovuto: **200 — FASE 14 + FASE 15**

## Rendimento marginale / novelty yield

Nel batch 176–200 sono stati considerati incrementali **8 contenuti su 25 = 32%**.

Contenuti incrementali:
- 185 — `H_dkTYpFb8I`
- 186 — `mDBoBf6qugE`
- 187 — `yu6t8pXgzMA`
- 188 — `PLIAmuNzx_s`
- 190 — `SK338MdNIy0`
- 197 — `0_dyJ0ZJMEE`
- 198 — `j171O4uv45I`
- 199 — `8xBneQflDhY`

Gli altri **17/25** hanno confermato o illustrato dottrina già consolidata e sono stati deduplicati senza gonfiare la KB.

Sottocampione utile:
- posizioni 176–184, tutte short: **0/9 incrementali**;
- posizioni 185–200: **8/16 incrementali = 50%**.

Questo non dimostra che tutti gli short futuri siano inutili. È però sufficiente per chiedere al checkpoint 200 una valutazione esplicita della priorità dei 268 contenuti residui.

### Ipotesi operativa da valutare, non ancora implementata

Mantenere la revisione semantica di **ogni** video, ma differenziare la profondità:
- priorità alta a long-form recenti, contenuti operativi/fondamentali e titoli che promettono procedure nuove;
- percorso rapido di deduplicazione per short, casi già coperti e fonti più vecchie chiaramente subordinate a una fonte recente;
- nessun video saltato: ognuno deve comunque ricevere review, categoria finale e stato.

Claude deve verificare questa ipotesi durante FASE 14/15 e documentare se è compatibile con governance e qualità della KB.

## Integrazioni KB del batch

File di contenuto KB toccati nel batch:

1. `merenda/03_offerta/front-end-e-back-end.md`
   - continuità resa più semplice tramite membership/autoordine quando esiste ricorrenza reale.

2. `merenda/03_offerta/offerta-a-risposta-diretta.md`
   - progressione problema → agitazione → alternative insufficienti → soluzione → prova;
   - stessa promessa rafforzata da angoli/prove diversi.

3. `merenda/05_acquisizione/database-email-e-sequenze.md` — **nuovo**
   - database proprietario come infrastruttura;
   - segmentazione progressiva;
   - sequenza minima in tre comunicazioni;
   - segmentazione per stato: attivi, persi, fan, lead non convertiti.

4. `merenda/05_acquisizione/funnel-e-conversione.md` — **nuovo**
   - landing con risposta specifica;
   - testimonianze/prove visibili presto;
   - riduzione del rischio, CTA, scarsità reale;
   - ottimizzazione continua;
   - funnel minimo come catena diagnostica per stadi.

5. `merenda/05_acquisizione/referral-e-soddisfazione.md`
   - referral trasformato da evento spontaneo a sistema;
   - momenti di richiesta, incentivi e introduzioni facilitate.

6. `merenda/09_business/numeri-cassa-e-crescita.md`
   - quattro leve: traffico, conversione, prezzo/valore medio, retention;
   - scaling finché regge l'economia marginale;
   - CAC completo/all-in;
   - separazione fra incasso, margine e CAC ancora da recuperare.

Routing aggiornato in `merenda/05_acquisizione/README.md` per includere i due nuovi nodi.

## Routing finale 176–200

| Pos. | ID | Categoria finale | Incrementale |
|---:|---|---|:---:|
| 176 | aQ5V7845jX4 | 10_casi_studio | No |
| 177 | 4FNdTMDCC6g | 10_casi_studio | No |
| 178 | fm3RYkxRXCk | 10_casi_studio | No |
| 179 | 6tgz9aFzyNE | 02_posizionamento | No |
| 180 | G7Jiu-Ig9vI | 04_marketing | No |
| 181 | Revqwijd6P0 | 09_business | No |
| 182 | R9fhEHLn8ww | 05_acquisizione | No |
| 183 | Gy82YE1iul4 | 05_acquisizione | No |
| 184 | Qt4lGjC-NdY | 04_marketing | No |
| 185 | H_dkTYpFb8I | 05_acquisizione | **Sì** |
| 186 | mDBoBf6qugE | 03_offerta | **Sì** |
| 187 | yu6t8pXgzMA | 05_acquisizione | **Sì** |
| 188 | PLIAmuNzx_s | 09_business | **Sì** |
| 189 | GEWf_KjMfhI | 10_casi_studio | No |
| 190 | SK338MdNIy0 | 05_acquisizione | **Sì** |
| 191 | TF9UGPSLxSw | 05_acquisizione | No |
| 192 | wF8Dqa_VtW8 | 01_mercato | No |
| 193 | MORFqQB8xGg | 05_acquisizione | No |
| 194 | k2H4428Uj00 | 04_marketing | No |
| 195 | MOrs4uWtXO0 | 02_posizionamento | No |
| 196 | JXQkNx5YyX8 | 05_acquisizione | No |
| 197 | 0_dyJ0ZJMEE | 05_acquisizione | **Sì** |
| 198 | j171O4uv45I | 09_business | **Sì** |
| 199 | 8xBneQflDhY | 09_business | **Sì** |
| 200 | bW_LBSe6s5U | 05_acquisizione | No |

## Indicazioni per FASE 14

Rileggere l'intera KB e controllare in particolare:

- i due nuovi documenti di `05_acquisizione`;
- possibile sovrapposizione fra `funnel-e-conversione.md`, `information-marketing.md`, `offerta-a-risposta-diretta.md` e `front-end-e-back-end.md`;
- possibile sovrapposizione fra `database-email-e-sequenze.md`, `riattivazione-clienti.md` e `referral-e-soddisfazione.md`;
- crescita di `numeri-cassa-e-crescita.md`: valutare se resta coeso o se richiede split reale;
- gerarchia principio → procedura → caso;
- link interni, README, INDEX e file orfani;
- prevalenza delle fonti più recenti quando esiste incompatibilità reale;
- assenza di Formalife nella KB.

Applicare **MERGE, NOT APPEND**. Non eseguire interventi cosmetici solo per ridurre il numero di righe.

## Indicazioni per FASE 15

- rileggere la tassonomia a 11 categorie;
- verificare se le nuove integrazioni 176–200 richiedono davvero nuove categorie, merge o split;
- ricontrollare i contenuti non ancora studiati 201–468 solo nei limiti previsti dalla FASE 15 e senza ingestione semantica;
- correggere categorie future soltanto quando il titolo/metadata fornisce evidenza ad alta confidenza;
- non aggravare i disallineamenti storici di ordine già noti;
- documentare esplicitamente la decisione sulla priorità differenziata suggerita dal novelty yield.

## Validazione

Verifiche già eseguite nel pre-handoff:

- 25/25 righe 176–200 in QUEUE risultano `STUDIATO`;
- catalogo: **194 STUDIATO / 6 ESCLUSO / 268 DA STUDIARE**;
- 25 review create;
- 25 commit semantici individuali;
- nessun file frozen modificato nel diff semantico;
- nessun contenuto 201+ processato.

Ultimo validator locale noto prima del batch semantico: **841 segnalazioni**, baseline già documentata al checkpoint 175 e nel handoff tecnico. Non assumere che il totale debba restare 841 dopo l'avanzamento degli stati.

Claude deve eseguire localmente:

```
python3 scripts/validate_project.py
git diff --check
git status --short
```

e documentare:
- totale e tipologia delle segnalazioni;
- quali sono baseline/storiche;
- eventuali nuove anomalie;
- working tree finale;
- frozen files;
- routing/link/orfani.

## Handoff dopo il checkpoint

Se il corpus resta incompleto:

- se gli asset tecnici 201–225 esistono già, impostare `Agente richiesto: CHATGPT`;
- altrimenti impostare `Agente richiesto: CODEX` e richiedere acquisizione tecnica 201–225;
- indicare sempre il primo contenuto non completato.

Il checkpoint deve aggiornare questo documento con il report finale FASE 14 + FASE 15 e aggiornare `STATUS.md`.
