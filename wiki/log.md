# Log

Registro cronologico append-only delle modifiche principali.

## [2026-08-21] feature / content | Aggiornamento Homepage SitoDave (Story, Blog dinamico, Behind the Shot, Team)

- **SitoDave commit `d436571`**:
  - **Miniature Workshop Homepage (`#workshops-2026`)**: Tutte e 4 le card del carosello mostrano le foto hero reali delle rispettive location (Friuli `lago-friuli.jpg`, Dardagna `dardagna-hero-poster.jpg`, Canfaito `canfaito_workshop.png`, Foreste Casentinesi `foreste_casentinesi_workshop.png`).
  - **Sincronizzazione Pagine Workshop (`workshops_2026/`)**: Pagine workshop perfettamente allineate con le landing di produzione (`Friuli_Prod`, `Dardagna_Prod`, `Canfaito_Conero_Prod`, `Foreste_Casentinesi_Prod`), complete di CSS dedicato, script di checkout e asset.
  - **Cartelle Workshop Root**: Create e popolate le directory web dedicate `Friuli_2026/`, `Dardagna_2026/`, `Canfaito_Conero_2026/`, `Foreste_Casentinesi_2026/` con moduli PHP `/api` operativi e asset video/foto ad alta qualità.
- Allineato e sincronizzato repository `DavideSecondBrain`.


- **SitoDave commit `4aa6eb5`** (`feat(paypal): integra prenotazioni e pagamenti PayPal Sandbox`):
  - Implementato modal di prenotazione multi-step con PayPal JS SDK: l'utente sceglie tra caparra €50 (saldo in loco) o saldo completo €350 con eventuale "Paga in 3 rate" gestito da PayPal.
  - Backend: endpoint `/api/create-paypal-order`, `/api/capture-paypal-order`, `/api/validate-coupon`, `/api/bookings`, `/api/save-coupons`, `/api/mark-balance-paid` tutti testati e funzionanti in Sandbox.
  - Coupon: `DAVEPRO10` (−10%, validato €315 su €350) e `EARLYBIRD50` (prezzo fisso €300) con preview live nel modal.
  - Admin panel aggiornato: tab Prenotazioni con stato pagamenti, PayPal IDs, pulsante "Segna Saldo Pagato"; editor coupon con campi separati `percentage`/`fixedPrice`, limite utilizzi e descrizione.
  - `.gitignore` aggiornato: esclude `private/`, `backend/.venv/`, `data/bookings.json`, credenziali.
- **Unificazione Second Brain**: il branch `chore/conservative-llm-provenance` (41 commit) è stato mergiato in `main` con fast-forward. Entrambi i repository GitHub (`SitoDave` e `DavideSecondBrain`) sono stati pushati e allineati.
- Nessuna credenziale, password, ID sandbox o informazione privata è stata inclusa nel commit o nella wiki.

## [2026-08-10] maintenance | Allineamento Second Brain con SitoDave e produzione Friuli
- Verificato `SitoDave/main` al commit `825ac18` e confrontato lo stato della wiki con il repository e la pagina pubblica `Friuli_2026`.
- Aggiornato il progetto sito da `completed` ad `active` per riflettere backend FastAPI, CMS, coupon, report, email e flussi PayPal ancora in consolidamento.
- Corretti quota, caparra, location e programma del Workshop Friuli; rimossa l'indicazione obsoleta di una sessione notturna ufficiale.
- Registrata la correzione del modulo informazioni: errore SMTP backend risolto con fallback sul mailer locale e test end-to-end HTTP 200.
- Aggiornati dashboard, prossime azioni e stato operativo del Second Brain.
- Nessuna credenziale, password, database o informazione privata è stata trasferita nella wiki pubblicabile.


## [2026-08-05] ingest / strategy | Instagram, Metodo SIS e Bussola
- Integrata in forma conservativa la conversazione “Analisi profilo Instagram” e il playbook PDF “Sistema Dave — Strategia di Brand e Marketing”.
- Sintetizzati i punti verificabili ripresi da dispense SIS, esercizi e PDF finale “Bussola”; gli allegati originali non sono stati copiati perché non disponibili nel repository.
- Create `wiki/knowledge/brand-identity-metodo-sis.md` e `wiki/knowledge/instagram-conversion-strategy.md`.
- Aggiornate le pagine di profilo, content/personal brand, strategia social e domande aperte senza rimuovere contenuti esistenti.
- Conservato Reach / Trust / Conversion e reso più identitario con semplicità, serenità, autonomia, esperienza e sviluppo della visione personale.
- Registrate come ipotesi da validare metriche prive di definizione completa, target e claim non ancora approvati.

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

## [2026-08-04] fix | Rifinitura Copywriting Box "Cosa Imparerai" (Friuli)
- **Workshop Friuli (`SitoDave/workshops_2026/friuli-2026.html`)**: Corretta la dicitura nel box di evidenziazione finale in *"imparare un metodo che potrai applicare in qualsiasi tua uscita fotografica futura"* (rimossa la ridondanza "metodico").
- Sincronizzati e pushati i commit su GitHub (`SitoDave` e `DavideSecondBrain`).
























## [2026-08-04] feature | Aggiornamento Immagini Scontornate Vanguard VEO BIB T18 e VEO BIB T25
- **Aggiornamento Asset**: Sostituite le immagini in `assets/gear_vanguard_veo_bib_t18.png` e `assets/gear_vanguard_veo_bib_t25.png` con le foto ad alta risoluzione fornite dall'utente, processate con sfondo trasparente ed allineamento perfetto.
























## [2026-08-17] decision | Consolidamento SitoDave e separazione Friuli Prod
- Auditata e consolidata la baseline tecnica del sito su FastAPI.
- Creato il tag di ripristino `backup/pre-consolidamento-2026-08-17`.
- Ripristinato il JavaScript della home e aggiunti smoke test, protezioni dati, SEO tecnico e controlli PayPal sandbox.
- Separati i 13 file della landing Friuli dalla cartella `Sito_Dave/prelancio` alla cartella sorella locale `L:\Friuli_Prod`.
- Gli altri progetti citati sul sito restano placeholder intenzionali fino alla loro integrazione.
- Aggiornate: `wiki/projects/website-rebuild.md`, `wiki/dashboards/now.md`.

## [2026-08-19] decision | Linee guida per una scrittura naturale
- Aggiornato `AGENTS.md` con regole permanenti contro i pattern tipici della scrittura AI.
- Privilegiate specificità, parole semplici, voce personale, ritmo naturale e formattazione determinata dal contenuto.

## [2026-08-19] maintenance | Audit di coerenza e consolidamento su main
- Allineati stato e dashboard del Second Brain al ramo principale unico.
- Archiviato lo stato operativo del Nivolet senza dedurne lo svolgimento; aggiunta la retrospettiva tra le questioni aperte.
- Uniformate le date di lavoro di Minorca e segnalata la durata ancora incoerente come dato da confermare.
- Aggiornato il riferimento verificato di `SitoDave`, chiarito lo stato della landing Friuli e rimossi recapiti duplicati dalla wiki pubblicabile.
- Riclassificata la guida Antigravity come riferimento storico, distinguendo i vecchi percorsi dai repository correnti su `L:`.
- Completate le sezioni operative mancanti nei progetti attivi e chiarita la separazione tra PayPal sandbox e pagamenti reali.

## [2026-08-19] feature | Landing Canfaito & Conero e Foreste Casentinesi
- Create le cartelle autonome `L:\Canfaito_Conero_Prod` e `L:\Foreste_Casentinesi_Prod`, con copie versionate in `Sito_Dave/standalone_pages/`.
- Collegati i due workshop al backend condiviso: 8 posti, caparra e saldo, PayPal Pay Later, cutoff, avvisi disponibilità e marker email distinti.
- Lasciati segnaposto nominati per tutte le fotografie ancora da fornire; le pagine non sono indicate come pubblicate.
- Aggiunta la scheda `wiki/projects/autumn-workshops-2026.md` e aggiornate area workshop, dashboard e progetto sito.

## [2026-08-19] release | Pubblicazione Workshop Dardagna 2026
- Pubblicata la landing su `https://www.davideluongo.it/Dardagna_2026/` dalla cartella `L:\Dardagna_Prod`.
- Aggiunti endpoint PHP locali per 8 posti, caparra €50, saldo €350, PayPal Live, email con marker `[DARDAGNA 2026]` e avvisi alle soglie 2/1.
- Registrato un webhook PayPal Live dedicato alla pagina Dardagna.
- Verificati pagina, video, tre fotografie, disponibilità, SDK PayPal, protezione 403 dei file privati e validazioni API; inviata una mail test reale.
- Non è stato eseguito alcun addebito reale durante la pubblicazione.
