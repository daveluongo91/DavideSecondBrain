---
title: Provenienza LLM dei contenuti
type: knowledge
status: active
created: 2026-07-31
updated: 2026-07-31
summary: Registro conservativo dei motori LLM che hanno creato o aggiornato i contenuti del Second Brain.
tags:
  - llm
  - provenance
  - audit
---

# Provenienza LLM dei contenuti

Questo registro rende rintracciabile l'origine dei contenuti senza spostare o riscrivere i documenti esistenti. Le attribuzioni distinguono la creazione iniziale dai contributi successivi e si basano sulla conversazione di passaggio, sulla cronologia Git e sui riferimenti espliciti presenti nei file.

## Convenzione

- **Motore primario**: motore che ha prodotto la base iniziale del documento.
- **Contributore**: motore che ha successivamente ampliato o aggiornato il documento.
- **Non verificato**: attribuzione non sostenuta da evidenze sufficienti; non viene assegnata per supposizione.

## ChatGPT

La base iniziale del repository, corrispondente al commit radice `8256694`, è attribuita a ChatGPT in base alla conversazione di passaggio. Sono inclusi tutti i documenti presenti in quel commit, salvo successivi contributi indicati sotto.

## Antigravity

La cronologia successiva e la documentazione esplicita di ripristino identificano Antigravity come contributore dei seguenti documenti:

- `PRIVATE_SETUP.md`
- `wiki/areas/workshops-and-photo-tours.md`
- `wiki/dashboards/now.md`
- `wiki/gear/lenses.md`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/profile/davide-luongo.md`
- `wiki/projects/minorca-2027.md`
- `wiki/projects/nivolet-2026.md`
- `wiki/projects/website-rebuild.md`
- `wiki/workflows/antigravity-setup-and-permissions.md` — creato con Antigravity

Per i primi dieci documenti Antigravity è registrato come contributore, non come autore esclusivo: la base preesisteva.

## Kimi

Nello stato attuale del repository non è stato possibile associare con sufficiente certezza alcun file a Kimi. Nessun contenuto è stato spostato, duplicato o rietichettato arbitrariamente. Questa sezione va aggiornata quando sarà disponibile un riferimento verificabile (chat, commit, nota sorgente o indicazione del proprietario).

## Codex / ChatGPT

- `wiki/provenance/llm-provenance.md` — creato il 2026-07-31 durante l'aggiornamento conservativo.
- [`wiki/reports/conservative-update-2026-07-31.md`](../reports/conservative-update-2026-07-31.md) — creato il 2026-07-31 come report di verifica.

## Manutenzione

Per i nuovi documenti, aggiungere al frontmatter quando il motore è noto:

```yaml
llm:
  primary: ChatGPT
  contributors:
    - Antigravity
```

Non aggiungere un motore se l'attribuzione non è verificabile. Per i documenti esistenti questo registro resta la fonte centrale, così da evitare modifiche massive e la rottura di riferimenti.
