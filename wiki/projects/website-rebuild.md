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
- **Architettura Backend & Admin CMS (`server.py`, `admin.html`, `admin.js`, `data/content.json`)**:
  - **Server REST API (`http://localhost:3000`)**: Gestione persistence contenuti in formato JSON e gestione delle rotte amministrative per la modifica dinamica dei testi per pagina.
  - **Motore Elaborazione Foto sRGB & Auto-scaling (>5MB o >2048px)**: Ridimensionamento automatico ad alta fedeltà (Lanczos) per file superiori a 5MB o con lato lungo >2048px, preservazione del profilo colore **sRGB** senza alterazioni e generazione parallela delle varianti **WebP** e **JPEG**.
  - **Gestione Asset & Testi Suddivisi per Pagina**: Tagging degli asset caricati per specifica pagina (Home, Workshop, Viaggi 2027, Gear, Blog) e filtri di ricerca in Admin.
  - **Generatore Dinamico Entità & Landing Page**: Modali in Admin per creare direttamente nuovi Workshop, Viaggi 2027, Articoli Blog e prodotti Gear. Quando viene creato un nuovo Workshop o Viaggio, il backend genera automaticamente la relativa pagina HTML landing su misura (`slug.html`).

## Prossime azioni mantenimento

- Aggiornamento periodico della disponibilità dei posti per i workshop (es. Nivolet 2026).
- Integrazione delle nuove date di workshop quando disponibili (es. Cinque Terre, Minorca 2027).

## Collegamenti

- [Content e personal brand](../areas/content-and-personal-brand.md)
- [Workshop e photo tour](../areas/workshops-and-photo-tours.md)
- [Davide Luongo](../profile/davide-luongo.md)

