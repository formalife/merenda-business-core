# Draft Audit — Parte I: Capire la macchina prima di toccarla

## Verdict

**PASS — nessun finding P0/P1**  
Data: 2026-09-20.

Draft verificato: `manual/draft/part-01-fondamenti.md`.

Spec: `manual/chapter-specs/part-01-fondamenti.md`.

---

# 1. Coverage

## PASS

I quattro capitoli coprono le funzioni previste:

1. marketing come progettazione del sistema di valore;
2. literacy economica minima;
3. diagnosi prima della tattica;
4. test/evidenza prima della standardizzazione e della scala.

Sono presenti framework, esempi, definizioni, errori e chiusure operative richieste dalle specs.

---

# 2. Beginner clarity

## PASS

Il primo draft conteneva gergo anticipato (`funnel`, `copy`, `churn`, `proof`, `onboarding`, `prospect` e simili). È stato corretto prima di questo audit sostituendo il gergo non necessario con linguaggio ordinario.

I termini introdotti intenzionalmente nella Parte I vengono definiti nel punto d'uso:

- marketing;
- sistema di valore;
- strategia / tattica;
- ricavi;
- margine / margine di contribuzione;
- cassa / cash flow;
- CAC;
- LTV;
- payback;
- cost-to-serve;
- break-even;
- capacità;
- diagnosi / ipotesi;
- collo di bottiglia;
- baseline;
- KPI;
- exploitation / exploration.

Il testo rinvia la profondità specialistica alle parti future senza richiedere al principiante di conoscerla già.

---

# 3. Economics depth

## PASS

Il Cap. 2 introduce il livello minimo necessario e non invade la funzione dei Capp. 30–32.

Rinvia implicitamente o esplicitamente:

- coorti;
- capitale circolante;
- cash conversion cycle;
- allowable CAC;
- capacity economics avanzata.

I numeri usati sono dichiarati didattici e non diventano benchmark.

---

# 4. Causal clarity

## PASS

La Parte I rende esplicite le distinzioni richieste:

- sistema vs output locale;
- promozione vs marketing;
- causa vs amplificatore vs sintomo;
- localizzazione vs diagnosi;
- test causale vs ricerca rapida di una combinazione migliore;
- risultato locale vs gate economico/operativo di scala.

---

# 5. Operational usability

## PASS

Il lettore riceve tre strumenti riutilizzabili:

1. quattro domande prima di una tattica;
2. protocollo diagnostico in nove passaggi;
3. template di test in sette campi.

Il Cap. 2 aggiunge le sei domande economiche minime.

---

# 6. Reader-facing agnosticism

## PASS

Il draft non espone:

- nomi delle fonti personali;
- Merenda/Frank;
- Layer 1;
- KB;
- ID semantici;
- classificazioni di provenance;
- file backend.

La voce è autoriale unitaria.

---

# 7. Redundancy / premature depth

## PASS

Mercato, positioning, offer, customer lifecycle e scale vengono citati solo per mostrare causalità o futuri prerequisiti; non vengono insegnati in profondità prima della loro casa primaria.

---

# 8. Findings P2 per l'editing globale

Non bloccanti:

1. uniformare nella release finale l'uso di inglese/italiano nei termini già spiegati (`cash flow`, `payback`, `cost-to-serve`, `exploitation/exploration`);
2. verificare nel pass terminologico globale che parole comuni del marketing come “conversione” siano definite abbastanza presto per il lettore target;
3. valutare in editing finale se alcuni esempi del Cap. 1 possono essere compressi senza ridurre la funzione pedagogica.

Questi finding non richiedono modifica della struttura né riapertura di gap.

---

# 9. Gate locale

- [x] 4/4 capitoli presenti;
- [x] coverage spec completa;
- [x] nessun prerequisito specialistico necessario per capire il testo;
- [x] economics al livello corretto;
- [x] strumenti operativi presenti;
- [x] nessuna provenance reader-facing;
- [x] nessun P0/P1.

**Parte I: READY — si può procedere alla Parte II.**