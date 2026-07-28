# Davide Second Brain

Un repository Markdown progettato per funzionare come **second brain personale e professionale**, mantenuto insieme a un agente LLM e consultabile con GitHub, Obsidian o qualsiasi editor di testo.

Il sistema segue tre livelli:

1. `raw/` — fonti originali e immutabili.
2. `wiki/` — conoscenza elaborata, collegata e aggiornata.
3. `AGENTS.md` — regole operative per l'agente che mantiene la wiki.

## Avvio rapido

```bash
git init
git add .
git commit -m "Initial second brain"
```

Poi crea un repository GitHub vuoto e collega il remote:

```bash
git branch -M main
git remote add origin URL_DEL_TUO_REPOSITORY
git push -u origin main
```

## Uso quotidiano

- Metti nuove fonti in `raw/inbox/`.
- Chiedi all'agente: **“Ingerisci le nuove fonti seguendo AGENTS.md”**.
- Parti da [`wiki/home.md`](wiki/home.md) per navigare.
- Usa [`wiki/dashboards/now.md`](wiki/dashboards/now.md) per le priorità correnti.
- Esegui `python scripts/lint_wiki.py` per controllare collegamenti e metadati.
- Esegui `python scripts/rebuild_index.py` per rigenerare l'indice.

## Privacy

Questa versione include solo informazioni creative e professionali adatte a un repository eventualmente pubblico. Dati sanitari, finanziari, credenziali, indirizzi, numeri di telefono e informazioni aziendali riservate **non devono essere inseriti nel repository pubblico**.

Per note sensibili usa una cartella locale esterna al repository oppure un vault separato e privato. Vedi [`PRIVATE_SETUP.md`](PRIVATE_SETUP.md).

## Struttura

```text
.
├── AGENTS.md
├── README.md
├── PRIVATE_SETUP.md
├── raw/
│   ├── inbox/
│   ├── sources/
│   └── assets/
├── wiki/
│   ├── dashboards/
│   ├── profile/
│   ├── areas/
│   ├── projects/
│   ├── gear/
│   ├── knowledge/
│   ├── workflows/
│   ├── people/
│   ├── organizations/
│   ├── decisions/
│   ├── questions/
│   └── templates/
└── scripts/
```

## Filosofia

La chat è temporanea. La wiki è persistente. Ogni fonte, decisione, analisi o risposta utile deve lasciare una traccia strutturata e riutilizzabile.
