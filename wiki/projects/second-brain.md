---
title: Second Brain
type: project
status: active
created: 2026-07-28
updated: 2026-08-19
summary: Costruzione di una wiki persistente su GitHub mantenuta con agenti LLM.
tags:
  - second-brain
  - github
  - knowledge-management
sources:
  - ../../raw/sources/llm-wiki.md
---

# Second Brain

## Obiettivo

Trasformare conoscenza sparsa tra chat, documenti e appunti in una wiki Markdown persistente, versionata e interrogabile.

## Risultato atteso

Un repository GitHub che:

- separa fonti originali e conoscenza elaborata;
- mantiene pagine collegate;
- registra decisioni e aggiornamenti;
- può essere gestito da Codex, Claude Code o altri agenti;
- si apre direttamente in Obsidian;
- controlla automaticamente link e metadati.

## Stato

Repository pubblico operativo su GitHub e popolato con aree creative, professionali, progetti, workflow e registri di provenienza. `main` è il ramo unico di riferimento; eventuali rami temporanei servono soltanto a preparare modifiche e vanno integrati o eliminati dopo la verifica.

Al 10 agosto 2026 è stata eseguita una revisione di attualità rispetto a `SitoDave`: sono stati corretti stato del progetto web, dettagli del workshop Friuli, priorità correnti e registro delle modifiche.

## Prossime azioni

- Aprirlo come vault Obsidian.
- Ingerire progressivamente brief, script, landing page e documenti importanti.
- Definire quali fonti restano private in un vault separato.
- Eseguire una revisione settimanale di progetti, prezzi, date e prossime azioni.
- Fare un lint editoriale dopo ogni aggiornamento strutturale.

## Prossimo risultato osservabile

Una revisione settimanale chiusa con indice aggiornato, lint senza errori e `main` allineato a GitHub.

## Dipendenze

- Repository GitHub `DavideSecondBrain`.
- Script locali per indice, ricerca e lint.
- Fonti verificabili per gli aggiornamenti che riguardano progetti esterni.

## Rischi

- Stati e prossime azioni che restano invariati dopo la conclusione di un evento.
- Informazioni presenti nelle chat ma non trasferite nelle fonti o nella wiki.
- Dati personali o credenziali copiati per errore nel repository pubblicabile.

## Decisioni collegate

- `main` è il ramo unico di riferimento dopo la revisione.
- Le convenzioni operative e di scrittura sono mantenute in [`AGENTS.md`](../../AGENTS.md).

## Criteri di successo

- Una nuova informazione importante viene ritrovata in meno di due minuti.
- Le decisioni non vengono ridiscusse senza consultare il record precedente.
- Ogni progetto attivo ha prossima azione e stato aggiornato.
- I contenuti pubblicati producono apprendimenti archiviati.

## Fonte concettuale

[LLM Wiki](../../raw/sources/llm-wiki.md)

## Tracciabilità

- [Provenienza LLM dei contenuti](../provenance/llm-provenance.md)
- [Report aggiornamento conservativo 2026-07-31](../reports/conservative-update-2026-07-31.md)
