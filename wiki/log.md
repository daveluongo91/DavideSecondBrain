# Log

Registro cronologico append-only delle modifiche principali.

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
