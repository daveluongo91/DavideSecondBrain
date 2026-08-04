# Log

Registro cronologico append-only delle modifiche principali.

## [2026-07-31] maintenance | Aggiornamento conservativo e provenienza LLM
- Verificata l'assenza di materiale inequivocabilmente relativo al lavoro aziendale da dipendente; nessun contenuto esistente è stato eliminato.
- Preservati integralmente documentazione fotografica, workflow e contenuti relativi al sito web.
- Aggiunto `wiki/provenance/llm-provenance.md` come registro centrale e non invasivo della provenienza ChatGPT, Antigravity, Kimi e Codex.
- Aggiunto `wiki/reports/conservative-update-2026-07-31.md` con riepilogo e verifiche.

## [2026-07-28] setup | Creazione repository
- Creata l'architettura `raw / wiki / schema`.
- Aggiunte pagine iniziali per profilo, aree, progetti, attrezzatura, conoscenza e workflow.
- Aggiunti script per indice, ricerca e lint.
- Integrata come fonte originale la specifica “LLM Wiki”.
- Esclusi dati sanitari, finanziari e aziendali riservati.

## [2026-07-28] content | Aggiornamento biografia e storia personale
- Aggiornata la sezione "La Mia Storia" sul nuovo sito web (`index.html`) con il testo biografico originale di Davide (Imperia, Boccadasse 2016 con Franz, trasferimento a Padova 2017, collaborazioni SIGMA/Kase/Vanguard, viaggi outdoor in Australia e Nuova Zelanda).
- Aggiornata la scheda profilo `wiki/profile/davide-luongo.md` nella wiki.

## [2026-07-29] ingest / update | Integrazione Sito Dave (Sito_Dave) nel Second Brain
- Aggiornato `wiki/projects/website-rebuild.md` a stato `completed` con l'architettura completa del nuovo sito statico (Hero, partner ticker, workshop grid, mentorship 1-to-1, Behind the Shot, bio e form modale).
- Aggiornato `wiki/projects/nivolet-2026.md` con i dettagli della landing page `nivolet-2026.html` (€290, Rifugio Savoia, ultimi 2 posti).
- Aggiornato `wiki/projects/minorca-2027.md` con lo stato anteprima 2027 e l'integrazione della lista d'attesa.
- Aggiornato `wiki/areas/workshops-and-photo-tours.md` incorporando la Formazione & Mentorship One-to-One e l'offerta workshop.
- Aggiornato `wiki/gear/lenses.md` con la scheda dell'ottica SIGMA 20mm F1.4 DG DN Art.
- Rigenerato l'indice (`wiki/index.md`) ed eseguito il lint senza errori.

## [2026-07-29] docs / backup | Registro Permessi, Skill e Ripristino Ambiente Antigravity
- Creato `wiki/workflows/antigravity-setup-and-permissions.md` contenente il registro completo dei permessi concessi (disco `D:\`, comandi PowerShell/Git/Python), percorsi eseguibili, comandi backend e script per il ripristino istantaneo su nuova macchina.
- Aggiornato `PRIVATE_SETUP.md` con il collegamento rapido alla documentazione di ripristino.

## [2026-07-29] feature | Architettura Backend & Admin CMS (`server.py`, `admin.html`)
- Sviluppato il server backend REST API (`server.py`) su porta 3000 con gestione persistence del database dati `data/content.json`.
- Implementato il motore di upload ed elaborazione immagini con preservazione del profilo colore **sRGB** e generazione automatica dei formati **WebP** e **JPEG** per il web.
- Creata la dashboard di amministrazione **Admin CMS** su `/admin` per l'editing in tempo reale dei testi del sito (Hero, Biografia, Workshop, Gear, Blog) e il caricamento con drag-and-drop delle foto.
- Sincronizzati e pushati i commit su GitHub (`SitoDave` e `DavideSecondBrain`).

## [2026-07-29] feature | Creazione sezione Blog & Pubblicazioni (blog.html)
- Creata la pagina `blog.html` con la suddivisione tra **✍️ Scrivo per Me** (blog personale di Davide) e **📰 Scrivo per gli Altri** (raccolta link ad articoli scritte su portali/brand terzi come SIGMA Italia, Vanguard World, RCE Foto, Kase Filters).
- Inserito il primo articolo test originale *"Pianificare la Via Lattea in Quota: Guida al Tracciamento Stellare al Nivolet"*.
- Integrata la sezione vetrina di anteprima del blog sulla Home Page (`index.html`) e aggiunti i filtri dinamici in `main.js`.
- Sincronizzati e pushati i commit su GitHub (`SitoDave` e `DavideSecondBrain`).

## [2026-07-29] feature | Ristrutturazione sezione Workshop (Nazionali & Viaggi cronologici)
- Semplificata la suddivisione dei workshop sul sito web (`index.html`) nei filtri: **Tutti gli Eventi**, **🇮🇹 Workshop Nazionali** e **✈️ Viaggi Fotografici**.
- Disposti 6 eventi in ordine cronologico rigoroso a partire dalla data odierna (Agosto 2026 -> Giugno 2027: Nivolet 2026, Cinque Terre 2026, Val d'Orcia 2026, Lisbona 2027, Minorca 2027, Madeira 2027).
- Aggiornata la scheda dell'area `wiki/areas/workshops-and-photo-tours.md`.
- Sincronizzati e pushati entrambi i repository GitHub (`SitoDave` e `DavideSecondBrain`).

## [2026-07-29] feature | Creazione pagina Gear.html & Palette aziendale LAB(20,0,-20)
- Applicata la nuova palette colori aziendale LAB(20, 0, -20) (`#17324D` midnight slate) su tutto il sito web e sul design system (`style.css`).
- Creata la nuova pagina `gear.html` con vetrina dei prodotti (SIGMA 14mm f/1.4 Art, SIGMA 24-70mm f/2.8 Art, SIGMA 100-400mm OS, Move Shoot Move Nomad Star Tracker, Vanguard Alta Pro 3VL 264CT, Vanguard LBP-50S, Vanguard VEO Active 53KG e 46KG).
- Integrati badge Ambassador, badge Link Affiliato, micro-articoli dedicati, specifiche tecniche e box interattivo per la copia del codice sconto (`MSM5DAVE`).
- Generate ed inserite immagini ad alta qualità per tutti i prodotti in `assets/gear_*.png`.

## [2026-08-04] feature | Conversione Sezione SIGMA Italia in Carosello 3D Interattivo
- Trasformata la sezione **SIGMA Italia** nella pagina [blog/blog.html](file:///L:/Sito_Dave/blog/blog.html) da griglia statica in un **Carosello 3D Interattivo** uniforme a *Vanguard World* ed *UniversoFoto*:
  - Aggiunto l'attributo `data-carousel` gestito da `blog.js`.
  - Integrata la barra di controllo superiore con contatore dinamico delle slide (`1 / 6`) e pulsanti freccia `←` e `→`.
  - Inserite le 6 slide 3D per: *14mm F1.4 Art*, *24-70mm F2.8 Art II*, *28-45mm F1.8 Art*, *28-105mm F2.8 Art*, *15mm F1.4 Fisheye Art* ed il profilo *Ambassador SIGMA Italia*.
- Sincronizzati e pushati i commit su GitHub (`SitoDave` e `DavideSecondBrain`).

























