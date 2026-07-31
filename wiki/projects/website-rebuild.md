---
title: Ricostruzione sito web
type: project
status: completed
updated: 2026-07-29
summary: Realizzazione del nuovo sito web statico (Sito_Dave) ad alte prestazioni, con design system moderno, filtri dinamici e landing orientate alla conversione.
tags:
  - website
  - conversion
  - github
---

# Ricostruzione sito web

## Obiettivo

Creare un sito più semplice, moderno e orientato alla conversione verso workshop e corsi, sostituendo la precedente struttura con un'architettura statica veloce e di impatto visivo premium.

## Risultato ottenuto (`Sito_Dave`)

- **Landing Page Principale (`index.html`)**:
  - **Palette Colori Aziendali LAB(20,0,-20)**: Palette scura basata su tonalità slate midnight (`#17324D`), abbinata ad accenti cyan, sky blue e aurora purple derivati dai post social.
  - **Hero Section**: Badge animato ("HIKE • SHOOT • PRINT • REPEAT"), titolo con testo sfumato cyan/purple, statistiche chiave (15+ workshop, 100% assistenza, SIGMA Ambassador, Fine Art).
  - **Ticker Partner**: Nastro in evidenza per SIGMA Italia, Vanguard World, Kase Filters, RCE Foto, Star Adventurer.
  - **Griglia Workshop & Photo Tour**: Filtri dinamici per categoria (Astrofotografia, Montagna, Mare & Scogliere) via JavaScript (`main.js`).
  - **Sezione Formazione & Mentorship 1-to-1**: 3 corsi dedicati (Astrofotografia sul campo, Post-Produzione avanzata Lightroom/Photoshop, Dal RAW alla stampa Fine Art).
  - **Behind the Shot Showcase**: Analisi dello scatto "La Via Lattea sul Lago Serrù" al Nivolet con scheda EXIF interattiva.
  - **Sezione Biografia ("Chi Sono")**: Storia personale completa di Davide (Imperia, Boccadasse 2016, Padova 2017, collaborazioni brand e viaggi outdoor).
  - **Modal Form Prenotazioni**: Modale interattivo per la richiesta informazioni e iscrizioni con argomento precompilato.
- **Nuova Pagina Vetrina Gear & Attrezzatura (`gear.html`)**:
  - Pagina dedicata per la presentazione dell'attrezzatura utilizzata (8 articoli principali).
  - **Sezione Ambassador & Affiliati**: Schede micro-articolo con badge Ambassador (SIGMA, Vanguard) e badge Link Affiliato / Codice Sconto (Nomad Move Shoot Move).
  - **Product Showcase**: Immagini dedicate generate ad alta definizione per ogni prodotto (`assets/gear_*.png`), pillole di specifiche tecniche e box codice sconto interattivo con copia negli appunti (`MSM5DAVE`).
  - **Filtri Categoria Dinamici**: Filtri per Ottiche SIGMA, Treppiedi & Zaini Vanguard, Astro & Tracker.
- **Nuova Pagina Blog & Pubblicazioni (`blog.html`)**:
  - Sezione articolata e divisa nelle due macrocategorie richieste:
    - **✍️ Scrivo per Me**: Articoli del blog personale di Davide (es. guida alla pianificazione notturna al Nivolet, post-produzione e stampa Fine Art).
    - **📰 Scrivo per gli Altri**: Raccolta ed elenco di tutti gli articoli e test pubblicati su blog terzi (SIGMA Italia Blog, Vanguard World, RCE Foto Magazine, Kase Filters) con link diretti e badge editore.
  - **Preview in Home Page**: Sezione vetrina integrata su `index.html` prima della bio con i 3 articoli in evidenza.
- **Struttura Repository Organizzata per Macro-Aree**:
  - `workshops_2026/`: Landing page dedicate ai workshop nazionai (`friuli-2026.html`, `cascate-appennino-2026.html`, `canfaito-2026.html`, `foreste-casentinesi-2026.html`).
  - `viaggi_2027/`: Schede e landing viaggi esteri.
  - `gear/`: Pagina gear ed attrezzatura (`gear.html`).
  - `blog/`: Pagina articoli e diario fotografico (`blog.html`).
  - `data/`: Database JSON (`content.json`, `participants.json`, report ed export).
- **Sistema di Prenotazione Operativo Workshop & PayPal Business**:
  - **Counter Urgenza FOMO (-20%)**: Gestione posti totali (8 posti max) con algoritmo di visualizzazione sottrattiva del 20% per stimolare le iscrizioni urgenti.
  - **Punto di Cutoff (15 Giorni Prima)**: Chiusura automatica iscrizioni a 15 giorni dall'evento.
  - **Form Iscrizione Partecipanti**: Nome, Cognome, Email e Telefono obbligatorio con nota esplicativa per la creazione del gruppo WhatsApp.
  - **Doppia Formula di Pagamento**:
    - **Caparra Confirmatoria (€50)** (saldo in loco).
    - **Saldo Totale (€290)** (con opzione 3 rate senza interessi PayPal).
  - **Politiche di Annullamento & Full Refund**:
    - Saldo: 100% rimborso a 30gg; 50% rimborso a 15gg.
    - Caparra: 100% full refund della caparra a 15gg.
  - **Pulsanti di Contatto Affiancati**: "Prenota Ora", "Richiedi Info Email (`info@davideluongo.it`)" e "Chatta su WhatsApp (`+39 373 5096237`)".
  - **Modale Popup Richiesta Info (`#info-modal-overlay`)**:
    - Popup interattivo che si apre al clic su "Richiedi Info via Email".
    - Campi obbligatori: Nome, Cognome, Email e Messaggio.
    - Campo facoltativo: **Numero di Telefono** con nota: *"ℹ️ Il telefono è facoltativo: inseriscilo solo se preferisci un contatto rapido via WhatsApp."*
    - Invio diretto ed archiviazione su `info@davideluongo.it`.
  - **Pagina di Ringraziamento (`thank-you.html`)**: Conferma immediata iscrizione con riepilogo dati.
  - **Report Excel (.csv UTF-8 BOM) & Invio Automatico Email**:
    - Generazione file Excel partecipanti per il Cutoff.
    - Download diretto in qualsiasi momento dal pannello Admin (`/admin`).
    - Invio automatico ed on-demand via email a `info@davideluongo.com`.

## Prossime azioni mantenimento

- Aggiornamento periodico della disponibilità dei posti per i workshop (es. Nivolet 2026).
- Integrazione delle nuove date di workshop quando disponibili (es. Cinque Terre, Minorca 2027).

## Collegamenti

- [Content e personal brand](../areas/content-and-personal-brand.md)
- [Workshop e photo tour](../areas/workshops-and-photo-tours.md)
- [Davide Luongo](../profile/davide-luongo.md)

