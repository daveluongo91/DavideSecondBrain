---
title: Report aggiornamento conservativo 2026-07-31
type: knowledge
status: completed
created: 2026-07-31
updated: 2026-07-31
summary: Verifica della pulizia dei contenuti e introduzione della provenienza LLM senza ristrutturazioni invasive.
tags:
  - report
  - maintenance
  - provenance
---

# Report aggiornamento conservativo — 2026-07-31

## Esito

- Contenuti relativi al lavoro da dipendente rimossi: **0**.
- Motivo: non sono stati trovati contenuti inequivocabilmente estranei all'attività fotografica. I riferimenti tecnici riguardano il sito, il workflow fotografico o l'infrastruttura del Second Brain e sono stati preservati.
- Documenti fotografici, workflow e documentazione del sito riscritti: **0**.
- File esistenti eliminati: **0**.
- File esistenti spostati: **0**.
- Nuovi file: **2** (registro di provenienza e questo report).

## Provenienza LLM

È stato adottato un registro centrale in [`../provenance/llm-provenance.md`](../provenance/llm-provenance.md), soluzione meno invasiva rispetto all'aggiunta massiva di metadati o alla creazione di cartelle per motore.

- ChatGPT: base iniziale del repository, secondo la conversazione di passaggio.
- Antigravity: contributi successivi ricavati dalla cronologia Git e dai riferimenti espliciti.
- Kimi: nessuna attribuzione sufficientemente verificabile nello stato corrente.
- Codex / ChatGPT: aggiornamento conservativo e report odierni.

## Verifiche

- Indice rigenerato con lo script del repository.
- Collegamenti interni e frontmatter controllati con il lint del repository.
- Differenze Git controllate prima del commit.
- Nessuna ristrutturazione di cartelle applicata.

## Anomalie e limiti

La cronologia Git registra l'autore umano dei commit, non il motore LLM. Le attribuzioni sono quindi conservative e riportano separatamente ciò che è verificabile da ciò che non lo è.

Il lint segnala tre collegamenti preesistenti verso risorse esterne a questa repository:

- `wiki/log.md` → `L:/Sito_Dave/gear/gear.html`
- `wiki/log.md` → `L:/Sito_Dave/blog/test-sigma-14mm-art.html`
- `wiki/projects/nivolet-2026.md` → `../../../Sito_Dave/nivolet-2026.html`

Non sono stati modificati perché la correzione richiede la verifica della repository del sito e non deve essere dedotta automaticamente. I nuovi collegamenti introdotti da questo aggiornamento risultano validi.
