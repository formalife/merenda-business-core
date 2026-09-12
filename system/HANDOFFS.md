# HANDOFFS

## Regola generale

L'agente che termina una task aggiorna `STATUS.md` prima di fermarsi.

Il successivo agente deve poter capire cosa fare leggendo soltanto:

1. `00_START_HERE.md`;
2. `MASTER_PLAN.md`;
3. `system/RULES.md`;
4. `STATUS.md`.

## Codex → Claude

Passare a Claude quando:

- sono stati completati 25, 75, 125, 175... video: fase 14;
- sono stati completati 50, 100, 150, 200... video: fasi 14 + 15;
- il corpus è completo: fase 14/15 se dovute, poi fase 16.

## Claude → Codex

Dopo un checkpoint 14 o 15, se il corpus non è completo:

- aggiornare `STATUS.md`;
- impostare `Agente richiesto: CODEX`;
- indicare il prossimo video non completato nella queue.

## Corpus completo

Quando non esistono altri video da processare:

- `Corpus completo: YES`;
- `Agente richiesto: CLAUDE CODE`;
- `Prossima fase: 16`.
