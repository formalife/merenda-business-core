# Acquisition Progress

Ultimo aggiornamento: 2026-09-14T07:17:40.033904+00:00

Batch: posizioni canoniche 151–175 di `QUEUE.md` — 25 video

- Tentati: 25/25
- Acquisiti normalmente (`ACQUIRED`): 25
- Transcript italiani mancanti / fallback ASR richiesti: 0
- Errori (`ERROR`): 0
- Pending: 0
- Elaborazione semantica del batch: 0/25; totale corpus invariato a 150

| # | Video ID | Titolo | Stato | Nota |
|---:|---|---|---|---|
| 1 | 8R8NR6nqhJY | "I Already Tried It and It Didn't Work" — The Excuse That Kills Your Revenue | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 2 | -oYSpJrj024 | The Customer Doesn't Understand Your Quality. And They Never Will: Here's What to Do | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 3 | v6WWqNpNSpE | The Unfair Advantage You Can Create From Scratch Today | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 4 | _6QCnb6Oj1Y | Customer Lifetime Value: Why Not Knowing This Value Will Set You Back | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 5 | Z7FhdrG-fOw | How to Increase Revenue with Just One Question | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 6 | 5awWbxibHIE | Hiring Mistakes? Frank Merenda Tells You the Brutal TRUTH 💣 | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 7 | G6j8xbargKY | Coaches and Trainers for Companies - Be Careful Who You Follow | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 8 | LMzKVDWrGlk | The Placement Rule That Brought Skechers to Success #shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 9 | -6L9gCbicjk | Come Capire il Dialogo Mentale di un Cliente? Ecco la soluzione! #shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 10 | I2RBYMESAsk | HOW TO FIND CUSTOMERS by giving them a dream shopping experience #shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 11 | mkhp-EGSORA | L'Impero del Miele di Mike's Hot Honey [Direttamente dalla Florida] #shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 12 | NTy1ZHQ8NYs | Il più grande FLOP di FERRERO #Shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 13 | 5XW0s6NizEE | Il SUCCESSO della URUS [O forse no?] #Shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 14 | NCQ1lX3S5wk | Il Segreto del Gommista di Successo #Shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 15 | AjvfyImTiPI | All’Antico Vinaio: il “segreto” del suo successo #shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 16 | qIG_0TMol8s | Chat GPT: Intelligenza Artificiale come opportunità o minaccia? #shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 17 | fpao23ulhkQ | Why You Shouldn't Spend on Marketing (Unless You Do This First) | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 18 | 9zvNhQOpRI4 | Is Marketing Important? This Is the Definitive Answer | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 19 | oQXsQzrIv2M | Marketing for Medical Clinics: How to Survive Italian Regulations and Win in the Market | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 20 | PKgWYVvme2s | Customer Experience: The Marketing Secret No One Tells You | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 21 | degAX4kvT-0 | Digital Marketing for Typical Products: The Formula for Winning Bundles | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 22 | YvfN2NUwXtY | Marketing per il tuo CENTRO ESTETICO #shorts | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 23 | aw3Fu_LTH34 | What does Marketing #shorts mean? | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 24 | znVPLom4j70 | Marketing for Dentists \| Here's What Happens When a Dentist Does Marketing #shots | ACQUIRED | Metadata + transcript Markdown disponibili. |
| 25 | y-8LBcQsS9M | RESTAURANT MARKETING \| Launching a Successful Restaurant | ACQUIRED | Metadata + transcript Markdown disponibili. |

## Verifiche tecniche

- Base verificata: `7f0c20c03f7d069d46447c81c76c7ad2a0f537d9`; branch `acquisition-151-175`.
- Batch coerente con STATUS, checkpoint 150 e posizioni 151–175 della queue; `next-batch.txt` rigenerato.
- 25/25 metadata con ID corretto e canale ufficiale `UCaAzr7bvYcZRfGR8EyBynOA`; JSON3 italiani e Markdown normalizzati tramite `scripts/transcript.py`, verificati segmento per segmento.
- Nessun candidato emerso dalla ricerca meccanica di riferimenti espliciti a slide, grafici, tabelle o schermate nei transcript. Nessun keyframe estratto; necessità visuali da valutare nella revisione ChatGPT.
- Esattamente un commit di acquisizione per ciascuno dei 25 ID; nessun asset relativo alle posizioni 176+.
- KB, file congelati, catalogo, VIDEO_INDEX e queue invariati rispetto alla base. Nessun `.review.md` creato e nessuno stato semantico modificato.
- Validator del repository: le stesse 841 segnalazioni della base (836 disallineamenti ordine/stato, 3 divergenze storiche dei congelati rispetto al tag v1.0, 2 etichette contatori STATUS); nessuna nuova anomalia.
- Rimossi soltanto spazi finali di formattazione dai JSON3 scaricati; equivalenza dei dati JSON verificata (testo, segmenti e timestamp invariati).
- `git diff --check` anche rispetto alla base: superato.
