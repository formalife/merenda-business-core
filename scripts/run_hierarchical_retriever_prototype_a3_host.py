#!/usr/bin/env python3
from __future__ import annotations

import run_hierarchical_retriever_prototype_a_host as base

A3_DISCIPLINE = r'''

PROTOTYPE A3 — DISCIPLINA DI SELEZIONE E APPLICAZIONE
Queste regole precisano il retrieval senza cambiare doctrine o gold:

9. Parti da un massimo di QUATTRO semantic ID primari scelti dal compact index. Supera questo budget iniziale solo per: (a) upstream realmente necessario alla decisione, (b) `must_read_with` la cui condizione è chiaramente vera nel caso, oppure (c) blind spot emerso dalla structural search.
10. Preferisci semantic unit specifiche per il problema concreto a gate generici di mercato/posizionamento/economics. Non aggiungere un gate generico solo perché è teoricamente a monte: aggiungilo solo se cambia materialmente la decisione corrente o verifica una premessa che il founder sta dando per risolta.
11. Se un semantic entry dichiara in `not_sufficient_for` che non può sostituire un altro layer e il founder sta esplicitamente collassando i due layer, recupera anche la semantic unit specifica di quel layer prima di concludere.
12. Quando la condizione di un `must_read_with` è chiaramente soddisfatta dai fatti del caso, recupera quell'entry e la relativa sezione canonica. Non trattare `related` come obbligatorio.
13. Prima di produrre il JSON finale, esegui un APPLICATION AUDIT interno: per ogni semantic unit selezionata e canonically verified chiediti se il suo gate/distinzione modifica materialmente la diagnosi. Se sì, quella distinzione deve comparire nella risposta. Se no, non forzarla nel testo. L'obiettivo è evitare sia omissioni di concetti letti sia risposte-lista piene di concetti non necessari.
14. Dopo avere coperto il primo collo di bottiglia e le dipendenze materialmente necessarie, FERMATI: non espandere verso unità generiche solo per completezza.
'''

base.COMMON = base.COMMON + A3_DISCIPLINE

if __name__ == "__main__":
    raise SystemExit(base.main())
