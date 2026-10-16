---
title: Premontaggio locale CapCut e verifica del progetto
type: workflow
status: reference
updated: 2026-10-16
summary: Preparazione di una timeline locale da sorgenti cronologici, distinguendo provini, anteprima separata e apertura verificata in CapCut.
tags:
  - video
  - capcut
  - montaggio
---

## Richiesta e risultato del 16 ottobre 2026

Richiesto un premontaggio modificabile di 180 secondi, in ordine vestizione, cerimonia, ristorante, con i rispettivi tre WAV. I 242 sorgenti video sono accessibili e hanno durata complessiva di 2.992,32 secondi.

Preparati soltanto i file, su indicazione esplicita dell'utente che lascia CapCut aperto: cartella di progetto e ZIP, anteprima MP4, lista tagli CSV e rapporto delle verifiche. Il progetto aperto nell'app non è stato modificato e la nuova copia non è registrata nell'indice CapCut.

La timeline preparata contiene 60 segmenti video e tre tracce audio: vestizione 0–48 secondi, cerimonia 48–120, ristorante 120–180. Audio originale delle clip disattivato, musica con incroci alle giunzioni e dissolvenza finale. Colori originali. Il momento dell'acqua è mantenuto continuo.

## Evidenze e limiti

- Visionati provini centrali di tutte le 242 clip, tre posizioni di 109 clip e campioni al secondo della ripresa del rito dell'acqua. Non dichiarare una visione integrale del girato.
- Analizzati gli attacchi sonori dei WAV per avvicinare i tagli. Ascolto integrale non verificato; gli attacchi rilevati non sono automaticamente battiti musicali confermati.
- Verificati ordine cronologico, presenza media, intervalli sorgente, continuità e durata della timeline: 180 secondi a 50 fps, cioè 9.000 fotogrammi.
- Anteprima separata generata e decodificata: 180 secondi, 9.000 fotogrammi, nessun errore video. Controllati anche 180 provini della sequenza.
- La struttura nativa deriva da file locali salvati da CapCut. Il progetto nuovo non è ancora stato aperto nell'app. Un render esterno riuscito non prova la compatibilità del progetto CapCut.

## Accesso desktop

Computer Use rileva e attiva la finestra CapCut, ma la cattura restituisce timeout. L'accessibilità espone soltanto finestre generiche, senza comandi della timeline. Lo screenshot inviato dall'utente conferma l'editor aperto. Non usare tale screenshot come prova di un controllo desktop funzionante.

## Prossimo passo

Quando l'utente chiude CapCut e chiede di proseguire, registrare una copia separata fra i progetti locali con backup dell'indice, poi verificarne apertura, tracce, media collegati e riproduzione. Non presentare lo ZIP come formato importabile ufficialmente o apribile con doppio clic.

Collegamenti: [Software](../gear/software.md), [Post-produzione](photo-processing.md).

Fonte: richiesta e verifiche locali nella chat del 16 ottobre 2026; file di progetto e rapporto consegnati nella cartella outputs della chat.

## Registrazione del progetto, 16 ottobre 2026

Su successiva richiesta esplicita di apertura, CapCut è stato chiuso regolarmente con i comandi dell'app. Copiata la cartella separata Battesimo_3min e aggiunta una voce all'indice locale: 180.000.000 microsecondi, 17 progetti totali. Backup dell'indice conservato nel percorso work/capcut-backup/20261016-104608 della chat.

CapCut riaperto; la nuova finestra usa la versione 9.6.0.4097. Accessibilità conferma HomeWindow, mentre la cattura restituisce ancora FrameArrived timed out. La registrazione è confermata anche leggendo l'indice dopo l'avvio. Apertura della timeline e riproduzione ancora non confermate: l'utente deve selezionare Battesimo_3min dalla schermata progetti.

## Correzioni nella copia v2, 16 ottobre 2026

Su richiesta dell'utente creata e registrata una copia separata Battesimo_3min_v2. Timeline a 25 fps, durata 180 secondi. Conservati esattamente i tempi interni dei 60 tagli, le tracce audio, il livello colore aggiunto dall'utente e i segmenti non interessati. Verificato anche dopo l'installazione che tracce e materiali del progetto precedente siano invariati. I tagli originari a meta fra due fotogrammi a 25 fps restano ai tempi interni originali; la riproduzione li campiona sulla griglia di uscita.

Applicati 18 rallentamenti nativi al 50%, zoom nativo dal 100% al 105% su C31, nuove porzioni pulite su C76 e C207, esclusione abbassamento finale su C128 e mantenimento del bacio su C192. C76 e C207 hanno lunghezza sufficiente senza rallentamento.

Stabilizzazione richiesta su sette clip calcolata con libvidstab in due passaggi, su copie Full HD a 50 fps, con crop compensativo del 4%. Rampa continua 100%-50% di C103 e fade video di C237 calcolati in altre due copie: questi effetti sono incorporati nei media, non modificabili come curva o stabilizzazione native. I sorgenti originali rimangono disponibili. Fade audio finale di 2 secondi conservato.

Verificati riferimenti, intervalli sorgente, fotogrammi delle nove copie e nero pieno sull'ultimo campione visibile di C237. Progetto e ZIP, CSV correzioni, rapporto e istruzioni consegnati nella cartella outputs. Indice CapCut salvato prima della registrazione della v2; app riaperta. Apertura e render della v2 dentro CapCut restano da confermare per il limite del controllo desktop.
