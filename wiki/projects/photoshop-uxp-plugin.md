---
title: Astro Sky Blender
type: project
status: active
updated: 2026-11-07
summary: Plugin Photoshop UXP per il compositing astronomico; preview 0.1.0 generata, collaudo Photoshop aperto.
tags:
  - photoshop
  - uxp
  - astrophotography
---

# Astro Sky Blender

## Obiettivo e stato

Sostituire il cielo di un foreground già postprodotto con quattro TIFF astronomici a 16 bit, allineati tramite le stelle del foreground. Il PSD conserva lo snapshot e i livelli originali; il gruppo cielo resta modificabile. Baseline funzionale v0.6.1, Implementation Plan v1.0.

Preview 0.1.0 prodotta con il packager Adobe. Nove test del motore passati; sulla fixture TIFF sono state ritrovate 34 stelle comuni e la traslazione nota. Archivio verificato. M0 resta aperta fino alla prova dentro Photoshop; Creative Cloud non ha ancora installato la preview in una prova verificata.

## Prossimo risultato osservabile

Caricare il CCX o eseguire lo script QA in Photoshop e salvare la diagnostica della fixture con versione host, Similarity, numero di stelle, RMS ed esito del rollback.

## Prossime azioni

Eseguire Analyze e il test di rollback su copia, quindi verificare maschera di gruppo, curve e profondità. Misurare i canali con H-alpha acceso/spento e l'effetto della maschera nera Starsoft. Ripetere dal pannello installato e passare a fotografie reali.

## Dipendenze e rischi

Photoshop e Creative Cloud Desktop per la prova di installazione. Select Sky e i descrittori delle curve devono essere confermati in host. Vanno misurati memoria e tempi sui panorami; geometrie non lineari restano fuori scope. L'asset grafico approvato è ancora da recuperare.

## Decisioni collegate

UXP Manifest 5, registrazione JS interna con Similarity e Affine, una matrice per quattro TIFF, rollback tramite cronologia. Dettagli nel [registro decisioni del progetto](https://github.com/daveluongo91/astro-sky-blender/blob/main/DECISIONS.md).

## Materiale e fonti

- [Repository privato](https://github.com/daveluongo91/astro-sky-blender), [codice della preview](https://github.com/daveluongo91/astro-sky-blender/commit/2aa47696cca191b31452cb571117e445f93610b9).
- [Specifica v0.6.1](https://github.com/daveluongo91/astro-sky-blender/blob/main/docs/SPEC-v0.6.1.md), [stato](https://github.com/daveluongo91/astro-sky-blender/blob/main/STATUS.md), [come riprendere](https://github.com/daveluongo91/astro-sky-blender/blob/main/docs/RESUME.md).
- [Software fotografico](../gear/software.md) e [Astrofotografia ambientata](../knowledge/astrophotography.md).

Data di revisione: alla prossima prova su Photoshop.

Tentativo del 7 novembre 2026. Photoshop 2025 aperto e finestra Apri raggiunta. La cattura della finestra è scaduta e il controllo remoto non ha potuto inserire il percorso. In attesa di caricare foreground.tif e lo script QA nell'app.

Tentativo del 7 novembre 2026. foreground.tif aperto in Photoshop in RGB/16 e dialogo Astro Sky Blender QA visibile. I pulsanti non sono esposti al controllo remoto. Analisi e rollback in attesa della prova.
