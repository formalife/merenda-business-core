# Founder Review — Golden A + Golden B, secondo prototipo

Date: 2026-09-21

## Verdict

**ARCHITETTURA: PASS**  
**SCRITTURA: FAIL / ulteriore redesign necessario**

Il secondo prototipo conferma che la nuova struttura editoriale è nella direzione corretta. La gerarchia Parte → Capitolo → Sezione → Paragrafo, i titoli brevi e tematici, l'inquadramento generale prima del dettaglio, la teoria prima degli esempi e l'uso di esempi generici/A-B sono approvati come base del manuale.

Il founder non approva ancora la qualità della prosa come modello da scalare.

Golden A e Golden B restano quindi i prototipi correnti per struttura/contenuto, ma devono subire un nuovo pass di riscrittura prima che la produzione degli altri capitoli possa iniziare.

---

# Cosa ha funzionato

## F2-01 — Struttura generale

La struttura è ora considerata molto buona.

Confermati:

- inquadramento generale di capitolo;
- progressione generale → particolare;
- teoria prima dell'esempio;
- titoli brevi e tematici;
- macro-sezioni leggibili;
- gerarchia Part → Chapter → Section → Paragraph;
- esempi numerici quando realmente utili;
- grafici quantitativi;
- esempi generici/A-B al posto di marchi fittizi inventati.

Questi elementi non devono essere rimessi in discussione senza nuova evidenza.

---

# Problema residuo principale: qualità della spiegazione

Il testo è corretto ma ancora troppo poco sviluppato come vera spiegazione autoriale.

Il founder segnala:

- coesione insufficiente fra paragrafi e sezioni;
- fluidità limitata;
- linguaggio ancora poco naturale;
- tono sterile;
- spiegazioni troppo sintetiche rispetto alla complessità dei concetti;
- pochi approfondimenti nei punti in cui il lettore avrebbe bisogno di capire il perché;
- poca incisività e determinazione;
- applicazioni pratiche ancora insufficienti;
- sensazione che alcuni passaggi “espongano” il concetto senza davvero insegnarlo fino in fondo.

Il problema non è una richiesta di allungare indiscriminatamente il testo. È una richiesta di aumentare **densità esplicativa, continuità e utilità**.

---

# Diagnosi causale

## RC-01 — La prosa è ancora costruita per unità modulari

Le sezioni sono corrette ma spesso sembrano blocchi autonomi messi in sequenza.

Serve maggiore continuità interna:

- una sezione deve nascere logicamente dalla precedente;
- un paragrafo deve preparare il successivo;
- le transizioni devono derivare dal contenuto, non dal template editoriale.

## RC-02 — Troppa compressione concettuale

Il testo tende ancora a dire la cosa corretta in poche frasi invece di accompagnare il lettore fino alla comprensione completa.

Per i concetti fondamentali serve più spesso:

1. definizione intuitiva;
2. spiegazione causale;
3. implicazione pratica;
4. confine/errore tipico;
5. esempio breve;
6. conseguenza decisionale.

Non come template visibile, ma come profondità minima quando il concetto lo richiede.

## RC-03 — Voce eccessivamente neutra

Nel tentativo di eliminare il tono artificiale/consulenziale, la seconda iterazione ha corretto troppo verso una voce neutra e controllata.

Il risultato può sembrare sterile.

La voce desiderata deve essere:

- naturale;
- autorevole;
- sicura;
- capace di prendere posizione quando la dottrina è netta;
- capace di spiegare con maggiore energia perché una distinzione conta;
- priva di teatralità o slogan artificiali.

Quindi: meno “voce ingegnerizzata”, ma non voce piatta.

## RC-04 — Applicazione ancora troppo separata dalla teoria

La teoria viene ora prima degli esempi, correttamente. Tuttavia l'applicazione pratica non deve apparire solo nel box finale.

Durante la spiegazione occorre integrare:

- micro-esempi;
- implicazioni operative;
- errori frequenti;
- domande che un imprenditore dovrebbe porsi;
- piccoli confronti fra decisioni alternative.

I box restano per gli esempi sostanziali, ma la prosa deve già essere operativa.

## RC-05 — Alcuni concetti meritano più profondità

Non deve esistere una lunghezza standard per capitolo o sezione.

Un concetto fondamentale va approfondito finché il lettore può:

- capirlo;
- distinguerlo da concetti vicini;
- riconoscerlo in un caso reale;
- usarlo per prendere una decisione;
- sapere quali errori evitare.

Se servono due pagine in più, vanno scritte. Se non servono, no.

---

# Nuovi requisiti vincolanti

- **V2-D032 CURRENT:** la struttura 8 Parti / 34 Capitoli e la gerarchia editoriale corrente passano il founder gate come baseline architetturale.
- **V2-D033 CURRENT:** prima di scalare la produzione serve un prose-depth pass specifico su Golden A/B.
- **V2-D034 CURRENT:** la qualità della prosa si valuta su coesione, fluidità, naturalezza, profondità esplicativa, incisività e applicabilità pratica.
- **V2-D035 CURRENT:** nessun target fisso di lunghezza; la profondità termina quando il concetto è comprensibile e utilizzabile, non quando è stato nominato.
- **V2-D036 CURRENT:** teoria-first resta valida, ma micro-esempi e implicazioni pratiche possono essere integrati nella spiegazione; i box restano per worked examples/casi più sostanziali.
- **V2-D037 CURRENT:** la voce deve essere naturale e autorevole, non meccanica ma neppure neutra/sterile.
- **V2-D038 CURRENT:** Golden C resta bloccato fino al prose-depth pass e al terzo founder-read di A/B.

---

# Conseguenza operativa

Non rifare l'architettura.

Non iniziare Golden C.

Prossimo ciclo:

1. analizzare Golden A/B riga per riga per individuare compressione, discontinuità e sterilità;
2. costruire un `PROSE_DEPTH_SYSTEM.md` con criteri positivi e anti-pattern;
3. aggiornare la Style Bible senza toccare la gerarchia approvata;
4. fare un pass di espansione qualitativa su A/B;
5. aggiungere micro-applicazioni, approfondimenti e spiegazioni dove servono;
6. verificare che l'aumento di profondità non reintroduca AI-smell o ridondanza;
7. produrre terzo PDF A/B;
8. founder-read;
9. solo dopo eventuale PASS, riprendere Golden C.

---

# Founder gate state

**Structure gate: PASS.**  
**Writing-quality gate: OPEN.**  
**Production scaling: BLOCKED.**
