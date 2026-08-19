---
title: Ricostruzione sito web
type: project
status: active
updated: 2026-08-17
summary: SitoDave consolidato su FastAPI con baseline recuperabile, pagamenti sandbox protetti e landing Friuli produttiva separata.
tags:
  - website
  - conversion
  - github
---

# Ricostruzione sito web

## Obiettivo

Creare un sito più semplice, moderno e orientato alla conversione verso workshop e corsi, sostituendo la precedente struttura con un'architettura statica veloce e di impatto visivo premium.

## Stato corrente (17 agosto 2026)

Il sito è stato sottoposto ad audit e consolidato in una baseline verificata. Il ramo locale `main` di `SitoDave` include i commit di consolidamento e la separazione della landing Friuli; resta da sincronizzare con GitHub.

- Punto di ripristino: tag `backup/pre-consolidamento-2026-08-17` sul commit `259ae14`.
- Backend supportato: FastAPI (`python -m backend.run`); `server.py` resta soltanto riferimento della migrazione.
- Esposizione pubblica: allowlist esplicita; `.env`, `private/`, backend e dati personali non sono serviti.
- PayPal: ancora **sandbox**; validazione di workshop, formula, partecipanti, posti, importo e valuta; verifica firma webhook predisposta.
- Email: assenza di SMTP produce un errore esplicito, non un falso esito positivo.
- Qualità: cinque smoke test superati, JavaScript della home ripristinato e verificato.
- SEO tecnico: aggiunti `robots.txt`, sitemap, canonical e `noindex` per la pagina di ringraziamento.
- Landing produttiva Friuli: i 13 file autonomi sono stati spostati fuori da `Sito_Dave/prelancio` nella cartella sorella locale `L:\Friuli_Prod`.
- I viaggi e gli altri progetti futuri restano citazioni/placeholder intenzionali fino all'integrazione completa.

### Gate prima del go-live

1. Configurare segreti persistenti, dominio HTTPS, CORS, SMTP e credenziali PayPal live nell'hosting.
2. Registrare il webhook reale e completare un pagamento controllato end-to-end.
3. Verificare email, decremento posti, rimborso/annullamento e rollback.
4. Rimuovere `noindex` dalla landing Friuli soltanto quando contenuti, privacy/cookie e checkout live sono approvati.
5. Eseguire l'analisi conversioni su home, schede workshop e landing Friuli dopo la stabilizzazione tecnica.

L'integrazione PayPal Sandbox è completata e testata. Il sito ha un sistema di prenotazione funzionante con pagamenti reali (in attesa di switch a credenziali live).

- Il branch `main` di `SitoDave` è aggiornato al commit `4aa6eb5` (`feat(paypal): integra prenotazioni e pagamenti PayPal Sandbox`).
- **Sistema prenotazioni**: modal multi-step con PayPal JS SDK. L'utente sceglie tra caparra €50 o saldo completo €350 con opzione "Paga in 3 rate" gestita direttamente da PayPal.
- **Coupon sconto**: validazione server-side con due tipi — percentuale (`DAVEPRO10`: -10%) e prezzo fisso (`EARLYBIRD50`: €300). Preview live nel modal e nel pannello admin.
- **Endpoint backend attivi**: `/api/create-paypal-order`, `/api/capture-paypal-order`, `/api/validate-coupon`, `/api/bookings`, `/api/save-coupons`, `/api/mark-balance-paid`.
- **Admin panel**: tab Prenotazioni mostra stato pagamenti (pending/paid/failed), PayPal Order/Capture ID, pulsante "Segna Saldo Pagato"; editor coupon con campi separati percentuale/prezzo fisso, limite utilizzi e descrizione.
- **Prossimo step**: switch credenziali PayPal da Sandbox a Live (cambiare `PAYPAL_ENV=live` in `.env`).
- Credenziali, database, backup, ambienti virtuali e file `private/` restano esclusi dal repository pubblico.
- Il Second Brain è stato unificato: il branch `chore/conservative-llm-provenance` (41 commit) è stato mergiato in `main` con fast-forward il 14/08/2026.

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
    - **Saldo Totale Friuli (€350)** (con eventuale opzione PayPal in 3 rate, se disponibile per il cliente).
  - **Politiche di Annullamento & Full Refund**:
    - Saldo: 100% rimborso a 30gg; 50% rimborso a 15gg.
    - Caparra: 100% full refund della caparra a 15gg.
  - **Pulsanti di Contatto Affiancati**: "Prenota Ora", "Richiedi Info Email (`info@davideluongo.it`)" e "Chatta su WhatsApp (`+39 373 5096237`)".
  - **Modale Popup Richiesta Info (`#info-modal-overlay`)**:
    - Popup interattivo che si apre al clic su "Richiedi Info via Email".
    - Campi obbligatori: Nome, Cognome, Email e Messaggio.
    - Campo facoltativo: **Numero di Telefono** con nota: *"ℹ️ Il telefono è facoltativo: inseriscilo solo se preferisci un contatto rapido via WhatsApp."*
    - Invio diretto a `info@davideluongo.it`, con trasporto server-side e nessuna credenziale esposta nel client.
  - **Pagina di Ringraziamento (`thank-you.html`)**: Conferma immediata iscrizione con riepilogo dati.
  - **Report Excel (.csv UTF-8 BOM) & Invio Automatico Email**:
    - Generazione file Excel partecipanti per il Cutoff.
    - Download diretto in qualsiasi momento dal pannello Admin (`/admin`).
    - Invio automatico ed on-demand via email a `info@davideluongo.it`.

## Prossime azioni mantenimento

- **Switch PayPal Live**: sostituire `PAYPAL_ENV=sandbox` con `live` in `.env` e aggiornare Client ID/Secret con credenziali di produzione.
- Verificare periodicamente disponibilità posti, form informazioni, notifiche email e checkout PayPal.
- Testare il flusso E2E nel browser con account sandbox buyer reale prima del go-live.
- Consolidare la configurazione di produzione del backend senza versionare segreti.
- Integrare le nuove date di workshop e photo tour quando confermate.
- Configurare webhook PayPal per aggiornamenti automatici stato pagamento (URL pubblico necessario).

## Collegamenti

- [Content e personal brand](../areas/content-and-personal-brand.md)
- [Workshop e photo tour](../areas/workshops-and-photo-tours.md)
- [Davide Luongo](../profile/davide-luongo.md)
