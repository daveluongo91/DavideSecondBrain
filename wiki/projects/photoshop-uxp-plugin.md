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

7 novembre 2026. Analyze only riuscito in Photoshop 2025 sulla fixture RGB/16: 34 corrispondenze, Similarity, traslazione (−54, −34) px e RMS 0,00004879 px. Rilevati 86.836 pixel di cielo; campionamento H-alpha utilizzabile. Prossima prova: errore iniettato e rollback.

Il pulsante OK chiude il riepilogo di Analyze only. Verificata la finestra foreground.tif attiva senza dialoghi. Il rollback si avvia rilanciando lo script QA.

Rollback Photoshop 2025 verificato sugli ID dei livelli di primo livello. Errore iniettato dopo STARLESS e risultato Original top-level IDs intact: true. Prossimo passo: Build on a test copy e verifica dei livelli.

Photoshop 2025 ha completato il compositing della 0.1.0. Davide conferma il gruppo e richiede per H-alpha Screen, solo R in Advanced Blending, opacità e riempimento 100% e Blend Clipped Layers as Group attivo. La 0.1.1 imposta e verifica solo R via Photoshop. Da confermare in Layer Style sulla fixture.

Davide richiede Sky Replacement nativo come gruppo padre di ASTRO SKY BLENDER. Preview 0.2.0 implementa il flusso guidato: eseguire Edit > Sky Replacement con Output to New Layers, selezionare il livello cielo e usare Blend into Sky Replacement. Il plugin riusa la maschera nativa, integra il gruppo astro e nasconde il cielo di riferimento. Prova Photoshop ancora aperta.

Il file da fornire a Sky Replacement è starless.tif della stessa cartella dei quattro TIFF. La 0.2.1 lo indica nel pannello, nello script QA e nel collaudo. Importare e selezionare STARLESS nel dialogo nativo prima di Output to New Layers. Importazione manuale nella preview, integrazione Photoshop da collaudare.
