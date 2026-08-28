---
title: Ricostruzione sito web
type: project
status: active
updated: 2026-08-25
summary: SitoDave consolidato su FastAPI con quattro landing workshop autonome, backend condiviso e pagamenti sandbox protetti.
tags:
  - website
  - conversion
  - github
---

# Ricostruzione sito web

## Obiettivo

Creare un sito più semplice, moderno e orientato alla conversione verso workshop e corsi, sostituendo la precedente struttura con un'architettura statica veloce e di impatto visivo premium.

## Stato corrente (21 agosto 2026)

### Audit contenuti e interfaccia del 25 agosto

- Verificate le aggiunte recenti a homepage, gallerie, premi, caroselli e navigazione One-to-One.
- Confermata la distinzione tra flussi operativi e segnaposto intenzionali: Dardagna è pubblicata con flusso autonomo; Canfaito e Foreste restano locali con immagini da sostituire; i viaggi 2027 raccolgono interesse ma non sono acquistabili.
- Individuati link partner vuoti nel footer e certificati premio ancora sostituiti da immagini placeholder.
- I cinque articoli SIGMA locali richiedono revisione editoriale e verifica delle affermazioni tecniche prima di essere considerati pronti.
- Rapporto completo: [Analisi SitoDave del 25 agosto 2026](../reports/site-audit-2026-08-25.md).

### Evoluzione Backend & Admin completata

- **Export Partecipanti Estemporaneo**: Implementato endpoint dedicato `GET /api/admin/participants/export` per il download istantaneo in formato XLSX con filtri di data e stato, sanificazione formule e isolamento totale dal cutoff e dallo stato prenotazioni.
- **Template Esperienze & Viaggi Internazionali**: Schemi standardizzati `workshop-v1` e `international-trip-v1` con validazione pre-pubblicazione (controllo campi obbligatori, tour operator, date, prezzi, assenza placeholder `[TODO]`), render deterministico HTML.
- **CRM Contatti & Rubrica**: Modello relazionale (`Contact`, `ContactInteraction`, `Tag`), deduplicazione automatica (email/telefono) all'arrivo di lead da form e checkout PayPal, calcolo stati automatico (`new_lead` -> `customer` -> `loyal_customer`), gestione blacklist e follow-up, import ed export CSV con UTF-8 BOM e prevenzione injection.
- **Autenticazione 2FA WhatsApp OTP & Recovery Codes**: il canale OTP è stato portato su Meta WhatsApp Cloud API; richiede numero E.164, Phone Number ID, token e template approvato configurati fuori dal repository. In produzione l'accesso fallisce in modo sicuro se la consegna non è configurata.
- **Admin CMS ripristinato**: Esperienze e Viaggi carica e salva i campi completi esistenti tramite le API unificate; Pagine CMS permette di creare pagine e articoli in bozza; l'export partecipanti resta disponibile prima del cutoff.
- **Pipeline Video & Job in Background**: Caricamento asincrono con FFmpeg (1080p/720p H.264, web-ready, faststart, audio AAC, poster WebP/JPEG), gestione video verticali e monitoraggio tramite modello `Job`.
- **Backup Database SQLite Atomico**: Backup a caldo con hash SHA-256 e verifica automatica di integrità via `PRAGMA quick_check`.
- **Pannello Amministrativo Riprogettato**: Sezioni dedicate per Esperienze/Viaggi, Partecipanti con export XLSX immediato, Rubrica CRM con filtri e modale interazioni/blacklist/CSV, Media con video upload, Sicurezza e Backup.
- **Test Suite**: 29 test automatizzati pytest (`tests/test_evolution.py` + baseline completa) superati con successo (29/29 passed).

Il sito è stato sottoposto ad audit e consolidato in una baseline verificata. La base remota precedente all'aggiornamento dei workshop autunnali è il commit `dd6746e`; il nuovo lavoro viene preparato su un ramo dedicato prima dell'integrazione in `main`.

- Punto di ripristino: tag `backup/pre-consolidamento-2026-08-17` sul commit `259ae14`.
- Backend supportato: FastAPI (`python -m backend.run`); `server.py` resta soltanto riferimento della migrazione.
- Esposizione pubblica: allowlist esplicita; `.env`, `private/`, backend e dati personali non sono serviti.
- PayPal del backend FastAPI generale: ancora **sandbox**. La landing autonoma Dardagna usa invece gli endpoint PHP locali con credenziali Live private e webhook dedicato.
- Email: assenza di SMTP produce un errore esplicito, non un falso esito positivo.
- Qualità: 21 test backend superati il 19 agosto, compresi importi PayPal, posti, marker email, avvisi disponibilità e report cutoff.
- SEO tecnico: aggiunti `robots.txt`, sitemap, canonical e `noindex` per la pagina di ringraziamento.
- Landing autonome locali: `L:\Friuli_Prod`, `L:\Dardagna_Prod`, `L:\Canfaito_Conero_Prod` e `L:\Foreste_Casentinesi_Prod`.
- Landing Dardagna pubblicata il 19 agosto 2026 su `https://www.davideluongo.it/Dardagna_2026/`; configurazione privata e archivio prenotazioni rispondono 403.
- Canfaito & Conero e Foreste Casentinesi hanno anche copie versionate in `Sito_Dave/standalone_pages/`; le immagini sono segnaposto espliciti in attesa degli asset definitivi.
- Il backend condiviso gestisce per i due nuovi workshop 8 posti, caparra €50, saldo €350, PayPal Pay Later, politiche di rimborso, cutoff, avvisi a 2/1 posti e marker distinti nelle richieste informazioni.

### Gate prima del go-live

1. Configurare segreti persistenti, dominio HTTPS, CORS, SMTP e credenziali PayPal live nell'hosting.
2. Registrare il webhook reale e completare un pagamento controllato end-to-end.
3. Verificare email, decremento posti, rimborso/annullamento e rollback.
4. Rimuovere `noindex` dalle landing soltanto quando contenuti, privacy/cookie e checkout live sono approvati.
5. Eseguire l'analisi conversioni su home, schede workshop e landing autonome dopo la stabilizzazione tecnica.

L'integrazione PayPal Sandbox del backend generale è completata e testata. Dardagna è il flusso autonomo già collegato a PayPal Live tramite PHP locale; non è stato eseguito un addebito reale durante la pubblicazione.

- Il lavoro PayPal sandbox è incluso nella baseline corrente di `SitoDave`; il riferimento operativo verificato il 19 agosto è `dd6746e`.
- **Sistema prenotazioni**: modal multi-step con PayPal JS SDK. L'utente sceglie tra caparra €50 o saldo completo €350 con opzione "Paga in 3 rate" gestita direttamente da PayPal.
- **Coupon sconto**: validazione server-side con due tipi — percentuale (`DAVEPRO10`: -10%) e prezzo fisso (`EARLYBIRD50`: €300). Preview live nel modal e nel pannello admin.
- **Endpoint backend attivi**: `/api/create-paypal-order`, `/api/capture-paypal-order`, `/api/validate-coupon`, `/api/bookings`, `/api/save-coupons`, `/api/mark-balance-paid`.
- **Admin panel**: tab Prenotazioni mostra stato pagamenti (pending/paid/failed), PayPal Order/Capture ID, pulsante "Segna Saldo Pagato"; editor coupon con campi separati percentuale/prezzo fisso, limite utilizzi e descrizione.
- **Prossimo step**: sostituire i segnaposto di Canfaito & Conero e Foreste Casentinesi, verificare i testi operativi e completare i rispettivi checkout sandbox prima del go-live.
- Credenziali, database, backup, ambienti virtuali e file `private/` restano esclusi dal repository pubblico.
- Il vecchio ramo `chore/conservative-llm-provenance` è stato integrato in `main` il 14 agosto 2026 e non è più un ramo operativo.

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
  - **Pulsanti di contatto**: prenotazione, richiesta informazioni via email e contatto WhatsApp. I recapiti non vengono duplicati nella wiki pubblicabile.
  - **Modale Popup Richiesta Info (`#info-modal-overlay`)**:
    - Popup interattivo che si apre al clic su "Richiedi Info via Email".
    - Campi obbligatori: Nome, Cognome, Email e Messaggio.
    - Campo facoltativo: **Numero di Telefono** con nota: *"ℹ️ Il telefono è facoltativo: inseriscilo solo se preferisci un contatto rapido via WhatsApp."*
    - Invio al recapito commerciale configurato, con trasporto server-side e nessuna credenziale esposta nel client.
  - **Pagina di Ringraziamento (`thank-you.html`)**: Conferma immediata iscrizione con riepilogo dati.
  - **Report Excel (.csv UTF-8 BOM) & Invio Automatico Email**:
    - Generazione file Excel partecipanti per il Cutoff.
    - Download diretto in qualsiasi momento dal pannello Admin (`/admin`).
    - Invio automatico e su richiesta al recapito commerciale configurato.

## Prossime azioni mantenimento

- Completare prima modifiche, contenuti e asset ancora in lavorazione. L'ottimizzazione massiva verrà eseguita soltanto quando Davide dichiarerà il sito finito, così da lavorare su una struttura stabile.
- Preparare a quel punto uno script di ottimizzazione unico e verificabile, con backup iniziale, controlli prima/dopo e possibilità di rollback.
- **Switch PayPal Live generale**: resta da fare per il backend FastAPI. Dardagna usa già PayPal Live nella propria cartella autonoma.
- Verificare periodicamente disponibilità posti, form informazioni, notifiche email e checkout PayPal.
- Testare il flusso E2E nel browser con account sandbox buyer reale prima del go-live.
- Consolidare la configurazione di produzione del backend senza versionare segreti.
- Integrare le nuove date di workshop e photo tour quando confermate.
- Il webhook PayPal Live di Dardagna è registrato su `/Dardagna_2026/api/paypal-webhook`; gli altri flussi vanno configurati separatamente prima del live.

## Prossimo risultato osservabile

Un test end-to-end controllato su hosting HTTPS che verifichi pagamento, webhook, email, decremento posti e annullamento senza esporre segreti.

## Dipendenze

- Repository locale e remoto `SitoDave`.
- Hosting HTTPS, dominio, SMTP e account PayPal Business.
- Landing autonome nelle quattro cartelle `*_Prod` su `L:`.

## Rischi

- Confondere i test sandbox con l'abilitazione dei pagamenti reali.
- Pubblicare segreti, dati di prenotazione o recapiti personali.
- Mostrare disponibilità, date o condizioni commerciali non aggiornate.

## Decisioni collegate

- FastAPI è il backend supportato; `server.py` resta un riferimento di migrazione.
- Le cartelle `*_Prod` restano pacchetti autonomi; Canfaito & Conero e Foreste Casentinesi hanno una copia versionata nel repository per tracciarne l'evoluzione senza includere database o segreti.
- Credenziali, database, backup e file privati non vengono versionati.

## Collegamenti

- [Content e personal brand](../areas/content-and-personal-brand.md)
- [Workshop e photo tour](../areas/workshops-and-photo-tours.md)
- [Davide Luongo](../profile/davide-luongo.md)
