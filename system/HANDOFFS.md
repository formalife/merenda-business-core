# HANDOFFS

## Regola generale

Chi termina una task aggiorna `STATUS.md` prima di fermarsi.

Il successivo agente deve poter capire cosa fare leggendo:

1. `00_START_HERE.md`;
2. `MASTER_PLAN.md`;
3. `system/RULES.md`;
4. `STATUS.md`.

## Codex → ChatGPT

Codex lavora a batch sull'acquisizione tecnica.

Quando metadata, transcript normalizzati e keyframe candidati del batch sono disponibili:

- aggiornare `STATUS.md`;
- indicare quanti video sono acquisiti ma non ancora studiati;
- impostare `Agente richiesto: CHATGPT`;
- indicare il primo video acquisito non ancora studiato.

L'acquisizione tecnica non incrementa il contatore `Video completati`.

## ChatGPT → Codex

Passare a Codex solo quando il prossimo video della queue non dispone degli asset tecnici necessari oppure quando serve una nuova acquisizione locale non eseguibile dalla chat.

Codex acquisisce il batch richiesto e restituisce il controllo a ChatGPT.

## ChatGPT → Claude

Passare a Claude quando:

- sono stati completati 25, 75, 125, 175... video: fase 14;
- sono stati completati 50, 100, 150, 200... video: fasi 14 + 15;
- il corpus è completo: fase 14/15 se dovute, poi fase 16.

## Claude → ingestione

Dopo un checkpoint 14 o 15, se il corpus non è completo:

- impostare `Agente richiesto: CHATGPT` se il prossimo video ha già gli asset;
- altrimenti impostare `Agente richiesto: CODEX` per acquisire il prossimo batch;
- indicare sempre il primo video non completato nella queue.

## Corpus completo

Quando non esistono altri video da processare:

- `Corpus completo: YES`;
- `Agente richiesto: CLAUDE CODE`;
- `Prossima fase: 16`.
