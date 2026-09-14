# Classificazione strategica A/B/C — contenuti residui 201–468

Artefatto prodotto al checkpoint 200 (FASE 14 + FASE 15).

**Non modifica lo stato di alcun contenuto.** Tutti i 268 contenuti restano `DA STUDIARE` e dovranno comunque ricevere transcript, revisione, categoria finale e stato (`STUDIATO` o `ESCLUSO` motivato) quando processati da ChatGPT/Codex nei batch successivi. La classificazione stabilisce solo la **profondità iniziale suggerita** della revisione semantica, secondo le regole descritte in `scripts/classify_residual.py` e nel checkpoint.

## Regola di promozione per recenza (aggiornata al checkpoint 225)

Il video 225 (`WCP26HC6wd0`) era classe **C** perché short, ma ha introdotto una formulazione del 17 novembre 2025 prevalente sul front-end rispetto a fonti 2022. Questo conferma che **C significa FAST REVIEW, mai SKIP**.

`upload_date` in `sources/catalog.json` non è un segnale automatizzabile per promuovere C -> B prima della revisione: è assente per la maggioranza degli short residui (compreso lo stesso 225 prima di essere studiato). La promozione per recenza resta quindi una **verifica manuale durante la FAST REVIEW**, non una regola del classificatore:

- durante la lettura veloce di un contenuto C, controllare la data di pubblicazione reale sulla pagina YouTube (non solo il catalogo);
- se il contenuto tratta un nodo già presente in KB con una data successiva alla fonte canonica più recente già integrata, promuovere immediatamente a B (o A se introduce anche cifre/framework/procedure non ancora documentati);
- questa regola si aggiunge, senza sostituirle, alle promozioni già previste (cifra/soglia operativa nuova, framework con nome proprio nuovo, formulazione che sembra contraddire un principio consolidato).

## Riepilogo

- Totale residuo: 218
- A: 34 (16%)
- B: 131 (60%)
- C: 53 (24%)

## Per categoria

| Categoria | A | B | C | Totale |
|---|---:|---:|---:|---:|
| 06_vendita | 9 | 46 | 15 | 70 |
| 07_copy_comunicazione | 5 | 0 | 0 | 5 |
| 08_brand | 5 | 0 | 3 | 8 |
| 09_business | 12 | 53 | 22 | 87 |
| 10_casi_studio | 3 | 32 | 13 | 48 |

## Lista completa

| ID | Categoria | Formato | Classe | Titolo | Motivazione |
|---|---|---|:---:|---|---|
| ellOvKnIOqk | 06_vendita | videos | B | The #1 Sales Technique for a Record-Breaking Sales Team | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| rI00A_jHqz8 | 10_casi_studio | videos | B | Il Potere Del Marketing: +50% di Vendite Per Un'Azienda Farmaceutica di Successo | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| -_oOcTQgkcY | 06_vendita | videos | B | The Best SALES TECHNIQUES on the Internet | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| P_LavmWySLs | 06_vendita | videos | B | How to Sell Anything With Frank Merenda's "Secret Word" | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| an5eXiIyyiA | 06_vendita | videos | B | How to Create High-Converting Ads [That Sell] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| wDPyGhkY_CA | 06_vendita | videos | B | The 3 UPSELLING Options to Explode Your Revenue Without Finding New Clients | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| oefQwsBIUc0 | 06_vendita | videos | A | RETE VENDITA: Come Raddoppiare le Vendite in 5 Step [Mai svelati] | area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing) |
| jzQcezkw8_o | 06_vendita | videos | B | How to Manage a Top-Rated Sales Network | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 5-UeSJzSvos | 06_vendita | videos | B | Da Estetista a Imprenditrice: Le Tecniche di Vendita che portano al Successo | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| XDnktZGk-ZM | 06_vendita | videos | B | How to Sell More? Learn from the Money-Grabbing Method of American Churches | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| A4I-A5hldQw | 06_vendita | videos | B | VENDERE di più grazie alle PR - [ Live Fabio e Riccardo Biancolini] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| RExoYxfxFWQ | 06_vendita | videos | A | TECNICHE DI VENDITA \| Script e Processi per diventare un VENDITORE PROFESSIONISTA | area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing) |
| HJBySYV6HjA | 06_vendita | videos | B | Close the SALES NEGOTIATIONS thanks to the Authority | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 9FpKpV15B_4 | 06_vendita | videos | B | COME VENDERE DI PIÙ - Cattura l’attenzione dei tuoi clienti | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| imdxn91jLik | 06_vendita | videos | B | How to create a high-performance sales network | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| NB9g-DhSj-4 | 06_vendita | videos | B | Come vendere di più creando affinità e fiducia con i clienti | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| Vqn55dABlHQ | 06_vendita | videos | B | How to SELL more to your active customers | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| IGR6IPPvY3Q | 06_vendita | videos | B | How to Sell More to the Right Target \| The 7 Types of Customers [Part 2] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 9YoGG3UT1Yc | 06_vendita | videos | B | How to Sell More to the Right Target \| The 7 Types of Customers [Part 1] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 21iVqc13KoE | 06_vendita | videos | A | Come vendere di più utilizzando gli script di vendita | area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing) |
| D96IKTeUfK4 | 06_vendita | videos | B | How to sell more thanks to mental dialogue | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| NyH30NE16_0 | 06_vendita | videos | B | How to Sell More with the 5 Levels of Clarity | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 0QpK3scgm4c | 06_vendita | videos | B | Come Vendere di più e con maggior frequenza [Parte 3] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| G4j1zImJq8I | 06_vendita | videos | B | Come Vendere di più e con maggior frequenza [Parte 2] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| jIVCaEJe9RU | 06_vendita | videos | B | Come Vendere di più e con maggior frequenza [Parte 1] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| Hs8y1wNyamo | 06_vendita | videos | B | THE ideal SALES PROCESS for generating TARGETED clients | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| UAGHHUm8Ncg | 06_vendita | videos | B | Marketing Strategies \| The 6 Levers to sell more [Part 2] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| HrExv7tbcuE | 06_vendita | videos | B | Marketing Strategies \| The 6 Levers to Sell More [Part 1] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| IN1Rm9HNhSE | 06_vendita | videos | B | Strategie di MARKETING per fare SOLD OUT e VENDERE Live | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| nJmttjxEbG8 | 06_vendita | videos | B | SALES without authority is a discount sale | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 6t5_mdsdv9o | 06_vendita | videos | B | SALES is affinity and mental dialogue with customers | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| VsakZMnjMyo | 06_vendita | videos | A | MARKETING \| Come creare AUTORITA' per vendere di più | area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing) |
| 7tWAsKiB0-Q | 06_vendita | videos | B | MARKETING \| The Sales Letter in an Envelope Structure | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 0Aj28sGSKkw | 06_vendita | videos | B | #4 Marketing Strategies to Sell to High-Spendants | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| qX8bJHUIDjI | 06_vendita | videos | A | Marketing Strategies \| Dan Kennedy's 3 Steps to Increase Sales | titolo con struttura numerata/framework/checklist: alta probabilità di procedura riutilizzabile |
| dFuZc7rFwgE | 06_vendita | videos | A | Le TECNICHE DI VENDITA per diventare un Venditore di Successo | area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing) |
| -v8fL_RzWKw | 06_vendita | videos | B | HOW TO SELL TO THE RICH \| Dan Kennedy reveals how to attract wealthy clients | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| fpX3evEGoHY | 06_vendita | videos | B | [Tecniche di Vendita] Come vendere fornendo la prova | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| dHKIWZFBHoA | 06_vendita | videos | B | [Tecniche di Vendita] Il potere di una parola nella trattativa di vendita | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| kGEOki4orFg | 06_vendita | videos | B | [Tecniche di Vendita] Perchè utilizzare il sistema Plug and Play | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| l4AcZXmUQUs | 06_vendita | videos | B | [Sales Techniques] The Simple Trick of Scammers | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| jVM-EVC0Tj4 | 06_vendita | videos | B | Sales Techniques - Fear of the Future | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| LAhN97eLwf8 | 06_vendita | videos | B | [Tecniche di Vendita] Parlare di denaro in Italia è un problema | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| ZsjuqCIaxP4 | 06_vendita | videos | B | Tecniche di Vendita: come vendere ai ricchi | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| TRXt5UDCQqM | 06_vendita | videos | B | SALES TECHNIQUES - The deadly mistake in selling | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| YD5Slijhu40 | 06_vendita | videos | B | Professional Sales - Competitive Orientation | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 5aI9CBLFH1k | 06_vendita | videos | B | [Professional Sales] The lever of public recognition | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| KhWKRvXYNFk | 06_vendita | videos | A | [Tecniche per la Vendita Professionale] Simbolismo e Autorità | area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing) |
| kI5CD1rmIRg | 06_vendita | videos | B | Vendita Professionale - Come identificare la voce narrante per scrivere un libro in Azienda? | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| FupPXETlhew | 06_vendita | videos | B | [Sales Techniques] The Basics of Selling - Part 3 | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| X7xZyHvQG7M | 06_vendita | videos | B | [Sales Techniques] The Basics of Selling - Part 2 | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| bCfQSlTSHtY | 06_vendita | videos | B | [Sales Techniques] The Whole Truth About Professional Sales (Part Three) | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| Gj9zFPY0NQg | 06_vendita | videos | B | [Tecniche di vendita] Tutta la verità sulla vendita professionale (Seconda Parte) | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| Qfr0lQEiaxU | 06_vendita | videos | B | [Tecniche di vendita] Tutta la verità sulla vendita professionale (Prima parte) | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| Vi2HZ7k5zWU | 06_vendita | streams | C | Tecniche di Vendita in Negozio: Come Raddoppiare le Vendite | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| HA8FTIpB9mo | 06_vendita | streams | C | SELL ME THIS PEN \| The Most Effective Sales Techniques | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| V74HGPNrO84 | 06_vendita | streams | C | Cosa Vendere ai Ricchi: L'Ottava Regola | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| rXoHmUGsYww | 06_vendita | streams | C | DAN KENNEDY e TELEVENDITE - Marketing a Risposta Diretta [Corso] | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| 7OHWKhhvdfk | 06_vendita | streams | C | WHAT TO SELL TO THE RICH - 7 Ways to Attract a Target Who Wants to Spend! | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| bkkDzsBa3YE | 06_vendita | shorts | C | Stop Selling Products: Start Solving Problems (And Sell More) | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| 68vQ8oZsEtg | 06_vendita | shorts | C | You're Losing Sales Every Day for a Reason They Never Explained to You | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| 4i7ISpIeXNw | 06_vendita | shorts | A | After-Sales Support: How Follow-Up Determines Your Brand's Fate | area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing) |
| MJWfijvL8H8 | 06_vendita | shorts | C | How to Talk to Customers to Really SELL (Without Looking Stupid) | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| rt-f18mskYI | 06_vendita | shorts | C | The Real Secret to Selling to Wealthy Customers and Conquering the Market [Frank Merenda] | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| o4Y0uyxzQAM | 06_vendita | shorts | C | Rule #1 for Sales Network Management | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| jEND8wY7cjs | 06_vendita | shorts | C | Selling Homes: Stop Waiting for Clients and Do THIS [Frank Merenda] | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| H3d6sJ6_ois | 06_vendita | shorts | C | Commission-Based or Fixed-Wage Salespeople? Frank Merenda Answers | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| R4koY-hl7TM | 06_vendita | shorts | C | Tecniche di Vendita \| Crea il Test Drive per i Clienti #shorts | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| S1UqJocqQUc | 06_vendita | shorts | C | Strategie di Direct Marketing per Vendere nel B2B | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| DrjevuNThsI | 06_vendita | shorts | C | Come VENDERE di più e alle TUE CONDIZIONI #shorts | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| eSyOgMr_UWs | 06_vendita | shorts | A | La Vendita Professionale secondo Venditore Vincente #shorts | area vendita segnalata come poco satura (preventivi/testimonial/follow-up/script/qualificazione/closing) |
| 6sNjbCGzd2A | 07_copy_comunicazione | videos | A | How to Create an Effective Call to Action | blocco 07_copy_comunicazione piccolo e ad alta densità attesa (indicazione di governance) |
| KipX0tAAWr4 | 07_copy_comunicazione | videos | A | Why COPYWRITING starts with your positioning [Full Course] | blocco 07_copy_comunicazione piccolo e ad alta densità attesa (indicazione di governance) |
| DTIhYJnLyGs | 07_copy_comunicazione | videos | A | Ice for the Eskimos - Direct Response Copywriting [Part 2] | blocco 07_copy_comunicazione piccolo e ad alta densità attesa (indicazione di governance) |
| iuly2QEl9no | 07_copy_comunicazione | videos | A | Ice for the Eskimos - Direct Response Copywriting [Part 1] | blocco 07_copy_comunicazione piccolo e ad alta densità attesa (indicazione di governance) |
| nKOvJg4lq6k | 07_copy_comunicazione | streams | A | COPYWRITING: Cos'é Oggi il Copy a Risposta Diretta | blocco 07_copy_comunicazione piccolo e ad alta densità attesa (indicazione di governance) |
| DcnlHK3p9u8 | 08_brand | videos | A | Come Tenere I Clienti Incollati Al Tuo Brand (E Proteggerti dai Competitor) | blocco 08_brand piccolo e ad alta densità attesa (indicazione di governance) |
| DgbZMAqw4NY | 08_brand | videos | A | REPUTAZIONE DEL BRAND \| Come EVITARE ERRORI e gestire la crisi | blocco 08_brand piccolo e ad alta densità attesa (indicazione di governance) |
| eBvEH3TPqSA | 08_brand | videos | A | Direct Response Marketing \| What's the Difference Between a Brand and a Category? | blocco 08_brand piccolo e ad alta densità attesa (indicazione di governance) |
| 9lPjA4n3UB4 | 08_brand | videos | A | How to Find Clients Without a Strong Brand | blocco 08_brand piccolo e ad alta densità attesa (indicazione di governance) |
| N547HVgrQmk | 08_brand | videos | A | Proteggere il BRAND da Joint Venture nocive | blocco 08_brand piccolo e ad alta densità attesa (indicazione di governance) |
| 16l3EQerKgQ | 08_brand | shorts | C | How to Know if You Have a Strong Brand (or Are Just Another Commodity) | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| VywpU3-Ll_M | 08_brand | shorts | C | The 2 Conditions That Separate Real Brands from Small Companies \| Frank Merenda | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| 6A1VXELopys | 08_brand | shorts | C | Aumentare il fatturato grazie alla forza del Brand #shorts | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| asMedYJtd4I | 09_business | videos | B | CONCORRENZA SLEALE dei dipendenti? | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| UZPsGxcC-_0 | 09_business | streams | C | MENTALITÀ VINCENTE \| Dan Kennedy svela i segreti per ottenere Successo | contenuto motivazionale/mindset/polemico/fiscale generico |
| _7CcZG5-Vdc | 09_business | streams | C | The Rich Mentality: Briatore vs. Sorbillo [Free Training Course] | contenuto motivazionale/mindset/polemico/fiscale generico |
| Jubodsxv8aQ | 09_business | streams | C | ONLINE SCAMS - Where the heck do you invest your money? | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| eGC1td6H3yE | 09_business | videos | B | The #1 Marketing Investment to Get Excited Customers Who Only Talk About You | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| ek1eEIYtgqk | 09_business | videos | A | MARKETING Investment with a 423% ROI [and 100% Conversion] | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| GUolZGprkP8 | 09_business | videos | B | BUDGET per MARKETING \| Come capire quanto investire per il Paccone? | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 7khsng5QpSs | 09_business | videos | B | How to Double Your Company's Results in Just 6 Months | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| wqo0CMzCsYY | 09_business | videos | B | The ONE RULE to apply to become a MILLIONAIRE ENTREPRENEUR | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| O5YdmHmfnAw | 09_business | videos | B | La TUA VITA è un INFERNO e non riesci a GUADAGNARE come vorresti? | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| bfH2NqlcGzw | 09_business | videos | B | LE TRUFFE per FARE SOLDI con gli E-Commerce Automatizzati | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| D7_NRV619Pw | 09_business | videos | C | TASSE MALEDETTE! Come difendersi dalle aggressioni del Fisco? | contenuto motivazionale/mindset/polemico/fiscale generico |
| _GL-3a90TJQ | 09_business | videos | B | Il MIGLIOR INVESTIMENTO per diventare ricchi | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| jZ8iQZq-kP0 | 09_business | videos | B | HOW TO MARKET your company [Part 2] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 8E8Cj1F0V9M | 09_business | videos | B | Amazon is no longer an e-commerce site: it's now 100% Merenda Method | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| VW36EYJReRU | 09_business | videos | B | HOW TO BECOME A successful ENTREPRENEUR at 18? | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 2DEKsiMb11Y | 09_business | streams | C | How to Become an Entrepreneur \| and Succeed Even Without Experience | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| Nk5BZqfkO-A | 09_business | videos | B | Il Sistema Di Offerte Spilla Soldi Mai Rivelato Dalle Big Company | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 7EY0X8kMJ0o | 09_business | videos | B | 🔴 Direct Response Marketing: The Technique That Made Great Entrepreneurs Rich | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| i2_3ygDL148 | 09_business | videos | B | SALES TECHNIQUES \| What does it mean to be a Salesperson in a company? | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| KvISQI3qS5w | 09_business | videos | B | CREATING AN E-COMMERCE \| The best way NOT to sell | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| IKT-pq1mJc0 | 09_business | videos | B | How to Start a Business from Scratch: 8 Strategies Your Competitors DON'T Know | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| Ldy_Av2G1SA | 09_business | videos | B | 🔴 Business Growth: How to Take Your SMB from Zero to Success (Complete 2025 Strategy) | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| GdSf3-b_aIQ | 09_business | videos | A | 🔴 Why Delegating Strategic Marketing Is Your Most Costly MISTAKE | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| oqoMqLQl9G4 | 09_business | videos | B | How to Make Your Seasonal Business a Steady Source of Income | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| n25U2m__pnQ | 09_business | videos | A | Vuoi Guadagnare Di Più? 3 Regole (Testate) Per Riempire Il Tuo Conto Corrente Aziendale | titolo con struttura numerata/framework/checklist: alta probabilità di procedura riutilizzabile |
| JyGh1R6O3hg | 09_business | videos | B | I 3 Investimenti Top Dei Ricchi Per Far Crescere Il Tuo Business | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| JFb67cV2HfE | 09_business | videos | B | Perché La Tua Azienda Non Cresce? Scopri L’errore Che Ti Costa Milioni! | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 5FEOsDJ5HAU | 09_business | videos | B | How to Tackle a Business Crisis and Turn It Into an Opportunity in 5 Simple Steps | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| GFrT89AGv50 | 09_business | videos | B | A Practical Guide to Exiting: How to Prepare Your Business and Turn It Into a Gold Mine | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| yZsBzaiH_Ic | 09_business | videos | A | Franchising: Opportunità o Trappola? Come Espandere La Tua Azienda Senza Farti Male | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| 9UxJuYEpf30 | 09_business | videos | B | Making Money with Your Business? Discover 2 Skills That Make a Difference | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| -6TU0HZ8cQo | 09_business | videos | B | Come Rendere La Tua Azienda Ricca e Inattaccabile Dai Concorrenti | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 2tWslHOkxIc | 09_business | videos | A | Seleziona i Collaboratori Perfetti: 2 Tecniche Provate per Imprenditori di Successo | titolo con struttura numerata/framework/checklist: alta probabilità di procedura riutilizzabile |
| -HLNTlFhGW8 | 09_business | videos | A | Come Espandere il Tuo Business con 2 Regole Semplici ma Potenti | titolo con struttura numerata/framework/checklist: alta probabilità di procedura riutilizzabile |
| RNsDovlfwK8 | 09_business | videos | B | L'unico Sistema Valido E Testato Per Guidare Un'Azienda Che Guadagna Davvero | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| DA_NpLZLn9U | 09_business | videos | B | 3 Cose Da Cambiare Subito Per Creare Un’Azienda Che Genera Ricchezza | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| wg3tWYf6iho | 09_business | videos | B | #11 Controversial Truths to Scale Your Business Fast | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| v2LEVo40O_w | 09_business | videos | A | Come Generare Flusso di Cassa In Anticipo Nella Tua Azienda | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| dt5NN20BeOY | 09_business | videos | B | 7 Numbers You Must Know to Make Your Business Take Off | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| AZYdLrjgvK0 | 09_business | videos | B | Where NOT to Invest Your Money If You Want to Start a Business [That Won't Fail Immediately] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 8u-1Ffgv4Gc | 09_business | videos | B | La Mappa Del Marketing Per Generare Ricchezza e Solidità in Azienda | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| jI___z2yDMM | 09_business | videos | B | How to Market Your Business Even If You Have Little Money | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 2QG4EBTT0Jk | 09_business | videos | B | Trasforma La Tua AZIENDA in Una Macchina STAMPA SOLDI [Con 3 Numeri] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| lV-ZZx5T5L4 | 09_business | videos | B | 3 Mistakes to Avoid to Build a Successful Business | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| RM9YvT6K9IQ | 09_business | videos | B | How to Choose the Right EMPLOYEES to Grow Your Business | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| e0dqAD4ySaA | 09_business | videos | B | How to build a successful business with MARKETING | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| jm6CRgEbWpE | 09_business | videos | B | Quali abilità servono per diventare un imprenditore di successo? | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| UNsFL0TyO5Q | 09_business | videos | B | Come investire i soldi della liquidità aziendale | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| ERpAPQPX9J0 | 09_business | videos | B | 5 Marketing Strategies to Get Your Business Off the Ground | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| feaFaTbIP6s | 09_business | videos | B | I VERI nemici dell’imprenditore [Che non vedi] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| jJszWli8eu8 | 09_business | videos | B | Entrepreneurship: 5 reasons not to start a business @FranchinoErCriminale | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| UD34Yfw_efE | 09_business | videos | B | COME FARE MARKETING per la propria azienda [Parte 3] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| wGgXryNPbxg | 09_business | videos | B | COME FARE MARKETING per la propria azienda [Parte 1] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| d7H5vX6zPQM | 09_business | videos | B | HOW TO DO BUSINESS IN ITALY [and not in the USA] | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| RlgpRIc7ljc | 09_business | videos | B | Aumentare il fatturato della tua Azienda \| Il vero segreto | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| Fo8PB_7fE60 | 09_business | videos | B | HOW TO DO BUSINESS \| The organizational chart of a modern company | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 3vfZIcsrilc | 09_business | videos | B | MARKETING \| 3 Azioni fondamentali per la tua Azienda | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| pjrMVek56EU | 09_business | videos | B | WHERE TO INVEST TODAY to make your business successful | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| zDEL2i541CA | 09_business | videos | B | INFLAZIONE \| Dove deve INVESTIRE un imprenditore per proteggere l'azienda | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| phMz5WxmXRo | 09_business | videos | B | MARKETING \| Come gestire il Marketing nell'azienda di Famiglia | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| uw7ESoevavQ | 09_business | videos | B | MARKETING\| Come creare un'Azienda Marketing First | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 49CpCqYaXFA | 09_business | videos | B | FONDI DI INVESTIMENTO \| Perchè NON devono entrare in azienda | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| KPzMmscoyro | 09_business | videos | B | MARKETING \| La Bacchetta Magica per Creare Un’Azienda di Successo | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| 8uQMbmRHUmk | 09_business | videos | B | COLLABORATORE DANNOSO \| Eliminare le mele marce in Azienda | video lungo in area operativa senza segnali forti né di alta né di bassa densità |
| Cc5IllVUUy4 | 09_business | videos | A | AGENZIA DI MARKETING \| Perchè NON puoi delegare il Marketing | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| IabwR13dZK0 | 09_business | streams | C | HOW TO DO BUSINESS IN ITALY - [Italian-Style Business] | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| mygv4grg_XA | 09_business | streams | C | MINDSET \| I Segreti della Mente degli Imprenditori di Successo | contenuto motivazionale/mindset/polemico/fiscale generico |
| LEXROXRm4gY | 09_business | streams | C | MEMBERSHIP \| Come Diventare Imprenditore anche Senza Soldi | live/stream generico: alta probabilità di Q&A o commento estemporaneo a bassa densità dottrinale nuova |
| vr4OJQVgB1k | 09_business | streams | C | COME NON PAGARE LE TASSE - La vera guida per piccoli imprenditori | contenuto motivazionale/mindset/polemico/fiscale generico |
| KxYueziNHXM | 09_business | shorts | A | You Spent €100,000 on CRM and It's Not Working? Here's Why (Frank Merenda Explains) | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| DN2dO1UBRZc | 09_business | shorts | C | Come scegliere i COLLABORATORI GIUSTI #shorts | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| GElTJ7sJHhQ | 09_business | shorts | C | Collaborator selection? #shorts | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| F6004PvguF8 | 09_business | shorts | C | 90% of Entrepreneurs Don't Understand This Concept | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| upu5iqJUCgk | 09_business | shorts | A | CRM and Customer Segmentation: The System That Separates Rich from Poor Entrepreneurs | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| WD-UPHoqogc | 09_business | shorts | C | Message to the DUBAI SCAM GURUS: Stop SCREWING OVER Entrepreneurs | contenuto motivazionale/mindset/polemico/fiscale generico |
| _o1n-VE2zfk | 09_business | shorts | C | A Fatal Mistake Entrepreneurs Make: The True Cost of a New Salesperson (It's Not the Salary) | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| vbO0I1bgCWk | 09_business | shorts | C | If You're Afraid of Losing a Customer, You Don't Have a Business — You Have a Prison | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| 8KxvTL5qFKU | 09_business | shorts | C | Why Your Business Is Failing (NO, It's Not Taxes' Fault) | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| 8TqBkL3xrzc | 09_business | shorts | A | 💣 The World's Fastest Delegation Course: Just 1 Rule | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| -GI3yZY-Yio | 09_business | shorts | C | 💲From Employee to Entrepreneur: The Mental Leap That Changes Everything | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| WsumrqBrMLU | 09_business | shorts | C | Why Italian Universities Don't Create Entrepreneurs But They Create Employees | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| oItk4I50omg | 09_business | shorts | C | Trade Associations: The Fatal Mistake That Kills Your Business [Frank Merenda] | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| Javgw1LWl24 | 09_business | shorts | A | Cosa significa LIFETIME VALUE e perchè è un concetto chiave per l'Azienda #shorts | area business segnalata come poco satura (numeri/cassa/CAC/LTV/organigramma/delega/CRM/exit/franchising) |
| iwhtNji1vVA | 09_business | shorts | C | Crea un’Azienda di Successo \| Da dove partire? #Shorts | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| n9L4NSinAXM | 09_business | shorts | C | Da ditta individuale a SRL #shorts #piva #azienda #impresa | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| zLAK2Qm5gLM | 09_business | shorts | C | Gli investimenti fondamentali per un imprenditore #shorts | formato short: alta probabilità di derivare da un video già in coda/già studiato (0/9 incrementali nel campione 176-184) |
| UL7p310omY8 | 10_casi_studio | videos | B | Marketing per CENTRI ESTETICI \| Come Raddoppiare il Fatturato in 1 Mese | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| sJ-PgDVRmwY | 10_casi_studio | shorts | B | Luciano Pavarotti's Restaurant in Modena: When Authority Surpasses Marketing | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| y17XqNh4nww | 10_casi_studio | shorts | B | The Mortadella Shop Marketing Lesson in Bologna | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| i_nXlRCdgPA | 10_casi_studio | shorts | B | Medical Clinic's Turnover Doubled Thanks to Merenda Method Marketing | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| Qk41565Wvqk | 10_casi_studio | shorts | B | Strategic Marketing for Restaurants - Guapo Argentine Restaurant #shorts | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| MHbLVF1ij3M | 10_casi_studio | videos | B | Record-Breaking Real Estate Agency in Parma: From Frozen Food Seller to Top Performer in 9 Months | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| hoVoLLL3eZk | 10_casi_studio | videos | B | From 0 to 464 Orders Thanks to the Sales Techniques of Tana Delle Tigri | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| AQcmrNLZc2s | 10_casi_studio | shorts | C | The Secret Behind TESLA: Why Does It Sell 10 Times More Than Automotive Giants? | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| yEZJEAiQALo | 10_casi_studio | shorts | B | Why You Shouldn't Create a Generic Brand? The Mortadella Shop Case in Bologna | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| nWGgyKZY0bc | 10_casi_studio | shorts | B | Positioning Errors: Mortadella Shop's Lesson for Every Entrepreneur | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| hBXLN6pzLSU | 10_casi_studio | shorts | B | The One-Flavor Ice Cream Shop: The Business Lesson You Don't Expect | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| abr257wwW3U | 10_casi_studio | streams | C | CHIARA FERRAGNI e il caso del PANDORO BALOCCO | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| cPDsbG0fZ_I | 10_casi_studio | streams | B | L'Impero del Miele: Come diventare ricchi con un solo prodotto | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| QlCVKca7Ygk | 10_casi_studio | streams | C | Come si diventa RICCHI con le sneakers? | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| h5e1TxDcVV0 | 10_casi_studio | streams | C | Coca Cola: Il Suo Errore Più Grande | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| dC6avQzKliQ | 10_casi_studio | streams | C | Il segreto di TESLA: perché vende 10 volte di più dei colossi dell'Automotive? | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| d1xejlyQVWM | 10_casi_studio | streams | C | La Battaglia del Thé | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| 60Nu2UhFAJ8 | 10_casi_studio | videos | B | MORTADELLA SHOP - The Marketing Lesson from the Kings of Bologna Station | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| GFPwnUHLQm8 | 10_casi_studio | videos | B | ALL'ANTICO VINAIO: 5 Key Marketing Strategies for Global Success | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| eGt2WUGelbU | 10_casi_studio | videos | A | INCASSI STELLARI di una Clinica Medica grazie al MARKETING di Metodo Merenda | titolo con struttura numerata/framework/checklist: alta probabilità di procedura riutilizzabile |
| UkzQe2Rpl8Y | 10_casi_studio | videos | B | The Secret to a Successful Tire Shop: How Marketing Changed the Game | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| KvkF605zLxo | 10_casi_studio | streams | B | BURGEZ MARKETING: Com'è dal vivo? | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| 9NraLPMJkpQ | 10_casi_studio | streams | B | Burgez Marketing: La creatività che funziona? | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| l6vW1WRrlqQ | 10_casi_studio | streams | A | Il Metodo CHIARA FERRAGNI: Le Strategie di Marketing della nota Influencer | titolo con struttura numerata/framework/checklist: alta probabilità di procedura riutilizzabile |
| RquiibFn3lo | 10_casi_studio | streams | C | La Pasta Integrale Barilla e il Marketing che NON Funziona | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| 4w9tk1wrjWQ | 10_casi_studio | streams | C | Il Marketing dei Detersivi: L'errore di Perlana | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| IzAwfz5hpI8 | 10_casi_studio | streams | C | Barilla e il suo Marketing: Troppe Estensioni di Linea? | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| gX9mQAcVsNg | 10_casi_studio | streams | C | DYSON: il Marketing Vincente che l'ha portato al SUCCESSO | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| trYcsCYjI_s | 10_casi_studio | streams | B | DUCATI \| Vince nel Marketing come Vince nelle Gare? | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| UNT0aSS6wWM | 10_casi_studio | streams | C | Le strategie di marketing che possono battere Nutella | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| G3OVBYUpOuo | 10_casi_studio | streams | C | Qual è il VERO SEGRETO del Marketing della Nutella? | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| Af9nYsZjjTM | 10_casi_studio | streams | B | Le vendite record 2023 di LAMBORGHINI bastano per battere FERRARI? | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| GWpaBmY-h8c | 10_casi_studio | streams | C | AMAZON SELLER CENTRAL \| Vendere su Amazon conviene alle Aziende Italiane? | caso su grande brand esterno notissimo: alta probabilità di illustrare dottrina già consolidata |
| jVnCaENbxus | 10_casi_studio | videos | B | How to Market with a Wonder Package: The Secret to Successful Businesses | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| nn33VweEdB0 | 10_casi_studio | videos | B | Come Trasformare Una Clinica Estetica In Un Business Milionario Grazie Al Marketing | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| LtFeqet7OFc | 10_casi_studio | videos | B | GELATERIA WALLY MILAN \| The Brutal Truth About the Ice Cream You Eat Every Day | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| dftLQTuK0cY | 10_casi_studio | videos | B | CAMMI GOMME PIACENZA: The Tire Dealer That Doesn't Look Like a Tire Dealer | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| wDRHWHNHP5c | 10_casi_studio | videos | B | EUROPA 92 a Modena: Il Ristorante Di Pavarotti Dove I Food Blogger Non Entrano | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| rEtbwMHdJcM | 10_casi_studio | videos | B | Le Iene and the Roberto Re Case: How to Protect Yourself and Your Company? | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| H23lJVsXUjo | 10_casi_studio | videos | A | FRANCHISING \| Svelati TUTTI i retroscena di Posta Power dal CDA Metodo Merenda | titolo con struttura numerata/framework/checklist: alta probabilità di procedura riutilizzabile |
| QoWTlWZnyIQ | 10_casi_studio | videos | B | How Brand Positioning Makes You UNIQUE in the Market (and Rich) \| VLOG | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| A9aD8P9W6BM | 10_casi_studio | videos | B | I SEGRETI DEL BRAND POSITIONING \| Creare Campagne Online di Successo [Case History] | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| -1l4to7UBDw | 10_casi_studio | videos | B | Dan Kennedy's Marketing Strategies for Raising Prices [Case History] | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| jjriqAHkJYc | 10_casi_studio | streams | B | TAFFO PUBBLICITÁ \| Una Case History da Studiare | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| YPbOmNqxdmA | 10_casi_studio | videos | B | Televendite \| Come utilizzare al meglio un Infomercial [Case History] | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| S6XcqyhsjGw | 10_casi_studio | videos | B | DON PEPPINU: Gelato Verace \| How to Create a Category and Dominate the Market [VLOG] | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
| k-6P-_ZcFwY | 10_casi_studio | videos | B | Come il MARKETING può far crescere la tua azienda [Case History Dustin Burleson] | caso applicativo su azienda specifica: probabile ma non certo consolidamento di dottrina esistente |
