from pathlib import Path
import re
import markdown


def inject_after(text: str, anchor: str, block: str, label: str) -> str:
    if anchor not in text:
        raise RuntimeError(f"Missing injection anchor: {label}")
    return text.replace(anchor, anchor + "\n\n" + block, 1)


ch1 = Path("manual-v2/golden/chapter-01/DRAFT.md").read_text(encoding="utf-8")
ch25 = Path("manual-v2/golden/chapter-25/DRAFT.md").read_text(encoding="utf-8")

ch1 = inject_after(
    ch1,
    "Se questa possibilità non viene compresa, i KPI diventano gabbie. Le persone imparano a migliorare il numero che viene premiato, non necessariamente il business.",
    "> **ERRORE FREQUENTE — Premiare il KPI più visibile**\n>\n> Le dashboard rendono alcuni numeri molto più facili da vedere di altri. Questo crea una tentazione: trasformare il dato disponibile nel risultato da ottimizzare. Il costo per lead può scendere mentre aumenta il costo commerciale necessario a chiudere i clienti; il tasso di chiusura può salire perché si concedono condizioni peggiori; il fatturato può crescere mentre scendono contribuzione e cassa. Il KPI locale resta utile, ma deve essere collegato almeno a una conseguenza a valle che impedisca di spostare il costo su un'altra parte dell'impresa.",
    "ch1-kpi-error",
)

ch1 = inject_after(
    ch1,
    "Confondere i due livelli produce uno dei comportamenti più costosi nelle imprese: spegnere il sintomo e credere di aver risolto il problema. Quando la pressione cala, tutto sembra tornato normale. Appena il volume riparte, la stessa fragilità ricompare.",
    "> **ERRORE FREQUENTE — Scambiare il contenimento per la soluzione**\n>\n> Ridurre una campagna, rallentare gli ordini o sospendere una promozione può essere la scelta giusta per proteggere clienti, cassa o capacità. Ma il fatto che il sintomo diminuisca non dimostra che la causa sia stata rimossa. Se il problema è una capacità insufficiente, un prezzo sbagliato o una selezione debole dei clienti, tornerà appena il volume riparte. Una misura di emergenza va quindi accompagnata da una seconda domanda: *che cosa deve cambiare perché non sia necessario contenere di nuovo lo stesso problema?*",
    "ch1-containment-error",
)

ch1 = inject_after(
    ch1,
    "Questa responsabilità è strategica perché tiene insieme le parti del sistema. Quando viene ceduta completamente all'esterno, l'impresa rischia di diventare dipendente da strumenti e fornitori senza essere più in grado di giudicare se stanno migliorando il business o semplicemente aumentando l'attività.",
    "> **VERIFICA NELLA TUA AZIENDA — Segui una decisione attraverso il sistema**\n>\n> Scegli una sola iniziativa commerciale che stai valutando o che hai lanciato di recente: una campagna, un aumento di prezzo, un nuovo canale, un'automazione, un nuovo venditore o un aumento di capacità.\n>\n> 1. **Risultato locale atteso.** Quale numero dovrebbe migliorare direttamente?\n> 2. **Conseguenza a valle.** Se quel numero migliora, quale reparto, costo o capacità viene coinvolto subito dopo?\n> 3. **Prerequisito a monte.** Che cosa deve essere già vero perché l'iniziativa produca valore invece di amplificare un difetto?\n> 4. **Metrica economica.** Quale numero ti dirà se il miglioramento locale ha prodotto un risultato utile per l'impresa?\n> 5. **Spiegazione alternativa.** Se il risultato non arriva, qual è almeno un'altra causa plausibile oltre alla tattica stessa?\n>\n> L'output utile è una mappa di ciò che dovrai osservare per evitare di giudicare la decisione da un solo KPI.",
    "ch1-self-check",
)

ch25 = inject_after(
    ch25,
    "Il punto pratico è questo: **più una decisione di spesa dipende da valore futuro non ancora osservato, più il margine di sicurezza deve aumentare**.",
    "> **ERRORE FREQUENTE — Usare il futuro per giustificare il presente**\n>\n> Il lifetime value può diventare molto convincente proprio quando è meno affidabile. Se il valore futuro dipende da retention, rinnovi, upsell o frequenze che non sono ancora state osservate, aumentare quelle ipotesi fa salire facilmente il CAC che l'impresa sembra potersi permettere. La disciplina corretta è separare sempre ciò che una coorte ha già prodotto da ciò che il modello prevede che produrrà. Le previsioni servono a decidere; non devono essere presentate come prova già acquisita.",
    "ch25-ltv-error",
)

ch25 = inject_after(
    ch25,
    "Il rapporto LTV:CAC è quindi utile come sintesi, non come verdetto. Se non sappiamo come è stato stimato l'LTV, in quanto tempo arriva la contribuzione e quanta cassa serve per arrivarci, il rapporto rischia di essere preciso soltanto nell'aspetto.",
    "> **APPROFONDIMENTO — Perché lo stesso LTV:CAC può descrivere aziende molto diverse**\n>\n> Un rapporto LTV:CAC identico non implica lo stesso rischio finanziario. Un'impresa che recupera il CAC in tre mesi può reinvestire lo stesso capitale più volte nell'anno; un'altra che lo recupera in diciotto mesi deve finanziare molto più a lungo la crescita. Inoltre, la qualità del rapporto cambia con la stabilità dei dati: un LTV quasi interamente osservato è diverso da un LTV costruito su diversi anni di previsioni. Per questo il rapporto va letto insieme a payback, cassa e incertezza, non come una soglia automatica di salute.",
    "ch25-ltv-deep-dive",
)

ch25 = inject_after(
    ch25,
    "Se queste risposte non esistono, la crescita è in gran parte una scommessa sul volume.",
    "> **VERIFICA NELLA TUA AZIENDA — Costruisci la scheda economica di una coorte reale**\n>\n> Scegli un gruppo di clienti abbastanza omogeneo: per esempio quelli acquisiti nello stesso mese, dallo stesso canale o con la stessa offerta. Usa dati reali per ricostruire:\n>\n> 1. **CAC completo della coorte.** Quali costi hai incluso nel numeratore e quanti nuovi clienti stai usando come denominatore?\n> 2. **Contribuzione osservata.** Quanto è rimasto dopo i costi variabili attribuibili nei primi 3, 6 o 12 mesi disponibili?\n> 3. **Payback osservato.** In quale periodo la contribuzione cumulata ha recuperato il CAC, se lo ha già fatto?\n> 4. **Parte modellata.** Quale quota del valore futuro deriva da dati osservati e quale da ipotesi su retention, frequenza, prezzo o upsell?\n> 5. **Costo massimo sostenibile.** Quanto deve rimanere per struttura/profitto e quale margine di sicurezza richiedono cassa e rischio?\n> 6. **Economia marginale.** Il prossimo incremento di acquisizione dovrebbe produrre clienti allo stesso costo storico oppure a un costo diverso?\n>\n> Se non riesci a compilare uno dei punti, non riempire il vuoto con una stima silenziosa. Segnalo come dato mancante o ipotesi: è precisamente l'informazione che il prossimo ciclo di misurazione deve produrre.",
    "ch25-self-check",
)


docs = [
    ("part", Path("manual-v2/golden/part-01-intro.md").read_text(encoding="utf-8"), None),
    ("chapter", ch1, "manual-v2/golden/chapter-01/figures"),
    ("part", Path("manual-v2/golden/part-07-intro.md").read_text(encoding="utf-8"), None),
    ("chapter", ch25, "manual-v2/golden/chapter-25/figures"),
]

sections = []
total_words = 0
for kind, text, figure_root in docs:
    total_words += len(re.findall(r"\b[\wÀ-ÿ’'-]+\b", text))
    if figure_root:
        text = text.replace("(figures/", f"(../../{figure_root}/")
    body = markdown.markdown(text, extensions=["tables"])
    body = re.sub(r'<blockquote>\s*<p><strong>(ERRORE FREQUENTE[^<]*)</strong>', r'<blockquote class="callout error"><p><strong>\1</strong>', body)
    body = re.sub(r'<blockquote>\s*<p><strong>(VERIFICA NELLA TUA AZIENDA[^<]*)</strong>', r'<blockquote class="callout selfcheck"><p><strong>\1</strong>', body)
    body = re.sub(r'<blockquote>\s*<p><strong>(APPROFONDIMENTO[^<]*)</strong>', r'<blockquote class="callout deepdive"><p><strong>\1</strong>', body)
    body = re.sub(r'<blockquote>\s*<p><strong>(ESEMPIO[^<]*)</strong>', r'<blockquote class="callout example"><p><strong>\1</strong>', body)
    sections.append(f'<section class="{kind}">{body}</section>')

print(f"Total pedagogical preview words: {total_words}")

cover = """
<section class="cover">
  <div class="eyebrow">Manuale V2 · Prototipo apparato didattico</div>
  <h1>Seconda velocità di lettura</h1>
  <p>Stessa architettura e stessa prosa del terzo prototipo. Questa versione testa soltanto l'apparato didattico selettivo.</p>
  <div class="cover-list">
    <p><strong>Capitolo 1 — Il sistema di marketing</strong><br>Errore frequente · Esempio svolto · Verifica nella tua azienda</p>
    <p><strong>Capitolo 25 — Economia del cliente</strong><br>Errore frequente · Approfondimento · Esempi numerici · Verifica nella tua azienda</p>
  </div>
</section>
"""

css = r"""
@page {
  size: A4;
  margin: 22mm 19mm 23mm 19mm;
  @bottom-center {
    content: counter(page);
    font-family: DejaVu Sans, sans-serif;
    font-size: 8.5pt;
    color: #666;
  }
}
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.8pt; line-height: 1.58; color: #1e1e1e; }
.cover { min-height: 245mm; display: flex; flex-direction: column; justify-content: center; page-break-after: always; }
.cover .eyebrow { font-family: DejaVu Sans, Arial, sans-serif; font-size: 9.5pt; text-transform: uppercase; letter-spacing: 0.07em; color: #666; margin-bottom: 9mm; }
.cover h1 { font-family: DejaVu Sans, Arial, sans-serif; font-size: 30pt; line-height: 1.1; margin: 0 0 8mm; }
.cover > p { font-size: 13pt; line-height: 1.5; max-width: 135mm; }
.cover-list { margin-top: 18mm; font-family: DejaVu Sans, Arial, sans-serif; font-size: 10pt; }
section.part { page-break-before: always; page-break-after: always; padding-top: 34mm; }
section.part h1 { font-family: DejaVu Sans, Arial, sans-serif; font-size: 28pt; line-height: 1.1; margin: 0 0 15mm; font-weight: 700; }
section.part p { font-size: 11.7pt; line-height: 1.68; margin-bottom: 5.5mm; }
section.chapter { page-break-before: always; }
section.chapter h1, section.chapter h2, section.chapter h3 { font-family: DejaVu Sans, Arial, sans-serif; color: #111; }
section.chapter h1 { font-size: 24pt; line-height: 1.12; margin: 0 0 17mm 0; font-weight: 700; page-break-after: avoid; }
section.chapter h2 { font-size: 15pt; line-height: 1.22; margin: 9mm 0 3.5mm; font-weight: 700; page-break-after: avoid; }
section.chapter h3 { font-size: 12.3pt; line-height: 1.25; margin: 7mm 0 2.5mm; font-weight: 700; page-break-after: avoid; }
p { margin: 0 0 4.2mm; orphans: 3; widows: 3; hyphens: auto; }
strong { font-weight: 700; }
blockquote { margin: 7mm 6mm; padding: 4mm 5mm; border-left: 3px solid #333; background: #f4f4f4; font-family: DejaVu Sans, Arial, sans-serif; font-size: 9.5pt; line-height: 1.48; break-inside: avoid; }
blockquote p { margin: 0 0 2.4mm; }
blockquote p:last-child { margin-bottom: 0; }
blockquote.callout { border-left: 0; border-top: 1px solid #999; border-bottom: 1px solid #bbb; padding: 4.5mm 5.5mm; }
blockquote.error { background: #f3f3f3; }
blockquote.selfcheck { background: #ededed; padding-top: 5mm; padding-bottom: 5mm; }
blockquote.deepdive { background: #f8f8f8; border-top-style: dashed; border-bottom-style: dashed; }
blockquote.example { border-left: 3px solid #333; border-top: 0; border-bottom: 0; background: #f4f4f4; }
blockquote.callout > p:first-child strong { font-size: 9pt; letter-spacing: 0.02em; }
table { width: 100%; border-collapse: collapse; margin: 7mm 0 8mm; font-family: DejaVu Sans, Arial, sans-serif; font-size: 8.7pt; line-height: 1.32; break-inside: avoid; }
th, td { border-bottom: 0.5px solid #aaa; padding: 2.4mm 2.2mm; vertical-align: top; }
th { background: #efefef; font-weight: 700; }
td:not(:first-child), th:not(:first-child) { text-align: right; }
img { display: block; max-width: 100%; max-height: 188mm; margin: 8mm auto 4mm; break-inside: avoid; }
p:has(> img) { margin-bottom: 8mm; }
ol, ul { margin: 4mm 0 5mm 7mm; padding-left: 5mm; }
li { margin-bottom: 1.5mm; }
blockquote.selfcheck ol { margin-top: 3mm; margin-bottom: 3mm; }
code { font-family: DejaVu Sans Mono, monospace; }
"""

out = Path("build/golden-pedagogy")
out.mkdir(parents=True, exist_ok=True)
html = f'<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{css}</style></head><body>{cover}{"".join(sections)}</body></html>'
(out / "preview.html").write_text(html, encoding="utf-8")
