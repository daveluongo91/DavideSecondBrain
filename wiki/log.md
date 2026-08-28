# Log

Registro cronologico append-only delle modifiche principali.

## [2026-08-27] feature / onetoone | Aggiornamento terzo slider Before/After (Islanda A7R00076)

- **SitoDave (`L:\Sito_Dave`)**:
  - Convertito il file RAW originale Sony ARW (`A7R00076.ARW`) in `assets/confronto_03_raw.jpg`.
  - Ottimizzato lo scatto elaborato definitivo (`A7R00076-Enhanced-NR.jpg`) in `assets/confronto_03_elaborata.jpg`.
  - Aggiornato il terzo slider interattivo della pagina `one-to-one/one-to-one.html` completando la sequenza dei 3 confronti Before/After.


## [2026-08-27] feature / onetoone | Aggiornamento secondo slider Before/After (Islanda A7R00018)

- **SitoDave (`L:\Sito_Dave`)**:
  - Convertito il file RAW originale Sony ARW (`A7R00018.ARW`) in `assets/confronto_02_raw.jpg`.
  - Ottimizzato lo scatto elaborato definitivo (`A7R00018-Edit.jpg`) in `assets/confronto_02_elaborata.jpg`.
  - Aggiornato il secondo slider interattivo della pagina `one-to-one/one-to-one.html` con il paesaggio islandese.


## [2026-08-27] feature / onetoone | Aggiornamento primo slider Before/After (Tenerife Sky 35mm)

- **SitoDave (`L:\Sito_Dave`)**:
  - Convertito il file RAW originale Sony ARW (`DSC00203.ARW`) in `assets/confronto_01_raw.jpg`.
  - Ottimizzato il file TIF elaborato definitivo (`35mm.tif`) in `assets/confronto_01_elaborata.jpg`.
  - Aggiornato il primo slider interattivo della pagina `one-to-one/one-to-one.html` per mostrare la lavorazione del cielo stellato e della Via Lattea a 35mm di Tenerife.


## [2026-08-27] ui / onetoone | Disposizione frase vantaggi su riga singola

- **SitoDave (`L:\Sito_Dave`)**:
  - Impostato `max-width: none` per il sottotitolo *"In gruppo è sicuramente bellissimo, ma nel One-to-One sono tutto per te."* in `one-to-one/one-to-one.html` garantendo la disposizione su una sola riga continua.


## [2026-08-27] ui / onetoone | Rimozione titoli e didascalie dalle card di confronto Before/After

- **SitoDave (`L:\Sito_Dave`)**:
  - Rimossi i blocchi di testo (titoli `<h4>` e descrizioni `<p>`) da ciascuna delle 3 card di confronto interattivo RAW/Elaborata in `one-to-one/one-to-one.html`, lasciando spazio pulito e full-bleed agli slider interattivi.


## [2026-08-27] ui / gallerie | Integrazione bandiere grafiche SVG per Islanda, Tenerife e Madeira

- **SitoDave (`L:\Sito_Dave`)**:
  - Creati asset vettoriali SVG ad alta definizione in `assets/flags/`:
    - `islanda.svg` (Bandiera Islanda)
    - `spagna.svg` (Bandiera Spagna per Tenerife)
    - `portogallo.svg` (Bandiera Portogallo per Madeira)
  - Sostituite le emoji unicode con vere bandiere grafiche SVG nei badge delle card in homepage, nelle intestazioni delle modali e nella barra informativa del lightbox per garantire la visualizzazione a colori su tutti i browser e sistemi operativi (incluso Windows).


## [2026-08-27] ui / lightbox | Ottimizzazione visibilità pulsante di chiusura (X)

- **SitoDave (`L:\Sito_Dave`)**:
  - Ridiscusso e potenziato il pulsante di chiusura del Lightbox a schermo intero (`.lightbox-close-btn`):
    - Pulsante circolare in vetro scuro opaco con bordo bianco nitido (`rgba(15, 23, 42, 0.88)` e `border: 1px solid rgba(255, 255, 255, 0.35)`).
    - Icona "✕" bianca spessa in rilievo con effetto glow.
    - Hover reattivo con sfondo rosso (`#ef4444`), rotazione a 90° ed espansione per un feedback immediato e inequivocabile.


## [2026-08-27] ui / gallerie | Aggiornamento copertina galleria Islanda con scatto Brúarfoss

- **SitoDave (`L:\Sito_Dave`)**:
  - Sostituita l'immagine di copertina della galleria **Islanda** (`assets/galleries/cover_islanda.jpg`) con lo scatto iconico verticale delle acque turchesi glaciali di *Brúarfoss* tra rocce laviche e neve.


## [2026-08-27] ui / gallerie | Aggiornamento copertina galleria Madeira con scatto foresta di Fanal

- **SitoDave (`L:\Sito_Dave`)**:
  - Sostituita l'immagine di copertina della galleria **Madeira** (`assets/galleries/cover_madeira.jpg`) con lo scatto iconico verticale dell'albero millenario e tronco muschioso avvolto dalla nebbia nella foresta di *Fanal*.


## [2026-08-27] ui / gallerie | Aggiornamento copertina galleria Tenerife con scatto Roques de García

- **SitoDave (`L:\Sito_Dave`)**:
  - Sostituita l'immagine di copertina della galleria **Tenerife** (`assets/galleries/cover_tenerife.jpg`) con lo scatto iconico verticale del torrione vulcanico di *Roques de García* / Teide National Park con il sentiero dorato.


## [2026-08-27] feature / gallerie | Integrazione portfolio fotografico completo (Islanda, Tenerife, Madeira)

- **SitoDave (`L:\Sito_Dave`)**:
  - Integrate tutte le fotografie selezionate per le 3 gallerie:
    - **Islanda** (24 foto da `L:\1_Social\SITO DATA\Islanda\selected`): salvate in `assets/galleries/islanda/` con nuova copertina `cover_islanda.jpg`.
    - **Tenerife** (28 foto da `L:\1_Social\SITO DATA\Tenerife\selected`): salvate in `assets/galleries/tenerife/` con nuova copertina `cover_tenerife.jpg`.
    - **Madeira** (14 foto da `L:\1_Social\SITO DATA\Madeira\selected`): salvate in `assets/galleries/madeira/` con nuova copertina `cover_madeira.jpg`.
  - Applicato rigoroso ordinamento di prestigio con fregi **1x**:
    1. `1X Awarded` (badge oro/ambra)
    2. `1X Published` (badge azzurro/ciano)
    3. `1X Accepted` (badge viola/magenta)
    4. Seguite da tutte le altre fotografie d'impatto e Top 10.
  - **Eliminati tutti i counter numerici** da card, badge, modali e lightbox.
  - Sviluppato **Lightbox Immersivo a Schermo Intero**:
    - Apertura in sovraimpressione al click sul thumbnail.
    - Pulsante "×" in alto a destra per tornare alla vista precedente.
    - Frecce di navigazione laterali fluttuanti (Sinistra / Destra) + supporto tastiera (Freccia Sinistra, Freccia Destra, Escape).


## [2026-08-27] ui / gallerie | Rimozione galleria Montagna e ottimizzazione griglia

- **SitoDave (`L:\Sito_Dave`)**:
  - Rimossa la galleria **Montagna** da:
    - `index.html` (sezione Gallerie Fotografiche `#gallerie`).
    - `data/galleries.json` e `DEFAULT_GALLERIES_DATA` in `main.js`.
  - Ottimizzata la griglia `.galleries-grid` in `style.css` con layout a 3 colonne per le gallerie principali (**Islanda**, **Tenerife**, **Madeira**).


## [2026-08-27] planning / Instagram | Caroselli engagement e community

- Creato il progetto Canva 4:5 `DAHTe3PPkgA`, titolo `Caroselli Engagement — Davide Luongo`, composto da 39 slide modificabili.
- Ripreso il sistema visivo del carosello “Se domani spegnessero i social” usando le tre slide fornite da Davide come riferimento diretto.
- Inseriti dieci mini-caroselli basati su domande aperte e il format “Confessioni di un fotografo” con tre esempi.
- Le aree fotografiche restano vuote come placeholder. Nessun contenuto è stato pubblicato su Instagram.
- Correzione dello stato: il primo import non rispettava abbastanza il riferimento. Il progetto nativo successivo è `DAHTe5hl-LU`; soltanto cover e sviluppo del primo carosello risultano convertiti, modificabili e salvati. La raccolta completa non è pronta.

## [2026-08-26] ui / team | Collegamento profilo Instagram di Elia Marcon

- **SitoDave (`L:\Sito_Dave`)**:
  - Collegato il profilo Instagram di **Elia Marcon** (`https://www.instagram.com/elia.marcon/`) nella sezione Team in `index.html`:
    - Reso cliccabile l'avatar fotografico con anello luminoso e tooltip `Segui Elia su Instagram ↗`.
    - Aggiunto il pulsante dedicato `Segui @elia.marcon ↗`.


## [2026-08-26] ui / team | Collegamento profilo Instagram di Manuel Linari

- **SitoDave (`L:\Sito_Dave`)**:
  - Collegato il profilo Instagram di **Manuel Linari** (`https://www.instagram.com/manuel_linari/`) nella sezione Team in `index.html`:
    - Reso cliccabile l'avatar fotografico con anello luminoso e tooltip `Segui Manuel su Instagram ↗`.
    - Aggiunto il pulsante dedicato `Segui @manuel_linari ↗`.


## [2026-08-26] branding / ui | Generazione e integrazione favicon ufficiale del logo

- **SitoDave (`L:\Sito_Dave`)**:
  - Generato il pacchetto completo delle favicon ad alta nitidezza ritagliate dal pittogramma ufficiale (`assets/pittogramma.png`):
    - `favicon.ico` (multi-risoluzione 16x16, 32x32, 48x48, 64x64) nella root e in `assets/`.
    - `assets/favicon-32x32.png` e `assets/favicon-16x16.png` per i moderni browser desktop.
    - `assets/apple-touch-icon.png` (180x180) per smartphone iOS/Android e scorciatoie home screen.
  - Inseriti i relativi meta tag `<link rel="icon">` e `<link rel="apple-touch-icon">` in tutte le 35 pagine HTML del sito (Home, Blog, Workshop, Gear, Hospitality, One-to-One, Landing Pages e Admin).


## [2026-08-26] ui / team | Integrazione avatar Eleonora Fioravante da Instagram

- **SitoDave (`L:\Sito_Dave`)**:
  - Scaricato, ottimizzato e integrato l'avatar circolare ufficiale di **Eleonora Fioravante** (@travel.fiore) (`assets/team_eleonora_fioravante.jpg`) nella sezione Team di `index.html`.
  - Ora tutti i 6 componenti del team (Loris, Manuel, Elia, Luca, Eleonora, Mauro) dispongono di avatar fotografici professionali circolari con anello luminoso sfumato.


## [2026-08-26] ui / team | Correzione definitiva abbinamento avatar fotografici del team

- **SitoDave (`L:\Sito_Dave`)**:
  - Riassegnate correttamente tutte le foto del team in `index.html`:
    1. **Mauro Boccali** (`assets/team_mauro_boccali.jpg`): ritratto sul campo con fotocamera, treppiede e zaino nel prato verde.
    2. **Manuel Linari** (`assets/team_manuel_linari.jpg`): scatto outdoor seduto sul tronco nella foresta.
    3. **Elia Marcon** (`assets/team_elia_marcon.jpg`): ritratto su poltrona in pelle con fotocamera e teleobiettivo bianco.
    4. **Luca Sensoli** (`assets/team_luca_sensoli.jpg`): ritratto in quota sulle Dolomiti con le vette alpine.
    5. **Loris Ferrini** (`assets/team_loris_ferrini.jpg`): scatto astronomico con telescopio ed equipaggiamento notturno.


## [2026-08-26] ui / team | Aggiornamento avatar di Luca Sensoli con ritratto montano

- **SitoDave (`L:\Sito_Dave`)**:
  - Sostituita la foto avatar di **Luca Sensoli** (`assets/team_luca_sensoli.jpg`) con il nuovo ritratto in quota tra le vette alpine/dolomitiche, centrato e ritagliato a cerchio.


## [2026-08-26] ui / team | Integrazione avatar fotografici circolari per il team

- **SitoDave (`L:\Sito_Dave`)**:
  - Ottimizzati, ritagliati e integrati i 4 avatar fotografici circolari nella sezione *Vi Presento il Team* (`#team`) in `index.html`:
    1. **Loris Ferrini** (`assets/team_loris_ferrini.jpg`): scatto notturno con telescopio ed equipaggiamento astronomico sotto le stelle.
    2. **Manuel Linari** (`assets/team_manuel_linari.jpg`): ritratto sul campo con reflex Canon e treppiede.
    3. **Elia Marcon** (`assets/team_elia_marcon.jpg`): ritratto outdoor nella foresta su tronco muschioso.
    4. **Luca Sensoli** (`assets/team_luca_sensoli.jpg`): ritratto su poltrona in pelle con fotocamera e teleobiettivo.
  - Aggiunta in `style.css` la classe `.team-avatar-photo` con resa perfettamente circolare, preservando gli anelli luminosi sfumati (`team-avatar-ring`) e i collegamenti esterni.


## [2026-08-26] feature / hospitality | Player video Instagram Reel incorporati nelle card Case Study

- **SitoDave (`L:\Sito_Dave`)**:
  - Sostituite le immagini statiche nelle card delle collaborazioni in `travel-hospitality.html` con i player video embedded ufficiali di Instagram per **Hotel Keflavík** (`DTTC2x6iCTv`) e **Hotel Monopol** (`DNyEEpsWmie`).
  - I video sono ora riproducibili direttamente all'interno della pagina in formato verticale 9:16 con controlli nativi.


## [2026-08-26] feature / hospitality | Creazione landing page dedicata Travel & Hospitality

- **SitoDave (`L:\Sito_Dave`)**:
  - Creata la nuova landing page B2B `travel-hospitality.html` dedicata a hotel, resort e brand di viaggio:
    - Hero section immersiva con visual aurora e van, metriche chiave e posizionamento come *Travel & Hospitality Videomaker*.
    - Griglia dei 4 servizi chiave per le strutture: *Reel 4K (9:16)*, *Libreria Fotografica d'Ambiente & Lifestyle*, *Integrazione della Destinazione*, *Licenza Commerciale & Collaborazione Social*.
    - Showcase interattivo dei Case Studies con link diretti ai Reel Instagram di **Hotel Keflavík (Islanda)** e **Hotel Monopol (Tenerife)**.
    - Spiegazione del metodo di lavoro in 4 step (*Briefing*, *Shooting*, *Post-produzione*, *Consegna & Boost*).
    - Modale e form di contatto dedicato alle strutture ricettive.
  - Aggiornata la card **Travel & Hospitality** nell'homepage (`index.html`) per rendere l'immagine, il titolo e il pulsante cliccabili direttamente verso `travel-hospitality.html`.


## [2026-08-26] ui / homepage | Aggiornamento immagine di copertina Travel & Hospitality

- **SitoDave (`L:\Sito_Dave`)**:
  - Sostituita l'immagine di copertina della card **Travel & Hospitality** con il nuovo scatto d'impatto con aurora boreale e van/camper (`assets/travel_hospitality_aurora.jpg`), ottimizzato per il web.


## [2026-08-26] ui / homepage | Aggiornamento Travel & Hospitality con anteprime Reel Instagram

- **SitoDave (`L:\Sito_Dave`)**:
  - Aggiornata la card **Travel & Hospitality** nella sezione *Progetti Paralleli* (`#other-projects`) in `index.html`:
    - Riformulato il testo editoriale e il posizionamento come *Travel & Hospitality Videomaker* (creazione di reel cinematici e storytelling emozionale del soggiorno integrato al territorio).
    - Integrato un blocco di anteprima interattivo con collegamenti diretti ai due reel ufficiali Instagram verificati:
      1. **Hotel Keflavík (Islanda)** (`https://www.instagram.com/reel/DTTC2x6iCTv/`)
      2. **Hotel Monopol (Tenerife)** (`https://www.instagram.com/reel/DNyEEpsWmie/`)
    - Aggiornato il pulsante di contatto in `Proponi una Collaborazione →` collegato alla modale con oggetto preimpostato `Collaborazione Travel & Hospitality`.


## [2026-08-26] ui / homepage | Impostata la card Wedding nei Progetti Paralleli in stato Coming Soon

- **SitoDave (`L:\Sito_Dave`)**:
  - Aggiornata la card **Wedding** nella sezione *Progetti Paralleli* (`#other-projects`) in `index.html`:
    - Applicato il placeholder visivo `neon-pink-card-placeholder` con testo animato flicker `COMING SOON` (coerente con la sezione *Viaggi 2027*).
    - Aggiornato il badge di stato da `Disponibile` a `Coming Soon` (`badge-status upcoming`).
    - Aggiornata la CTA in `Richiedi Info Wedding →` collegata alla finestra modale per le richieste di informazioni.


## [2026-08-25] export / PDF | Raccolta professionale articoli SIGMA

- Esportati dal nuovo sito locale, senza modificare le pagine sorgente, i quattro articoli dedicati a **SIGMA 14mm F1.4**, **24-70mm F2.8 DG DN II Art**, **28-105mm F2.8 DG DN Art** e **28-45mm F1.8 DG DN Art**.
- Creati quattro PDF singoli e una raccolta unica di 27 pagine in `output/pdf/` nel progetto Codex `Sito`.
- Conservati testi, titoli, immagini, tabelle e gerarchia editoriale; applicata una resa A4 con margini da stampa e controllata visivamente su apertura, pagine interne e chiusura.
- Nota editoriale: nei tre articoli riscritti restano didascalie con diciture placeholder già presenti nelle pagine locali. Non sono state corrette durante l'esportazione per rispettare la richiesta di non modificare i contenuti del sito.

## [2026-08-25] editorial / blog | Riscrittura completa dei tre articoli Sigma (24-70mm II, 28-105mm, 28-45mm)

- **SitoDave (`L:\Sito_Dave`)**:
  - Riscritto completamente il contenuto editoriale dei tre articoli dedicati alle ottiche Sigma, adottando la struttura, la profondità, il ritmo narrativo e la gerarchia visiva dell'articolo di riferimento **Sigma 14mm F1.4 DG DN Art**:
    1. **Sigma 24-70mm F2.8 DG DN II Art** (`blog/test-sigma-24-70mm-art.html`):
       - Sviluppata la contraddizione fondante: *"Vedo il mondo a 14mm, ma il 24-70 è il primo che metto nello zaino"*.
       - Analizzata la personalità ottica a 24mm (distorsione utile ed effetto immersivo), la tenuta sui 60MP+, il margine di crop a 70mm, l'autofocus HLA e la netta riduzione di peso/volume.
    2. **Sigma 28-105mm F2.8 DG DN Art** (`blog/test-sigma-28-105mm-art.html`):
       - Strutturato l'articolo su due piani distinti: *Santo Graal nel Wedding* (105mm a F2.8 costante senza cambi ottica) vs *Limiti nel Landscape* (i 4mm mancanti tra 24 e 28mm e la gestione del kit da trekking).
       - Approfondito il concetto fondamentale di *"valutare l'obiettivo dentro il kit reale e non isolato"*.
    3. **Sigma 28-45mm F1.8 DG DN Art** (`blog/test-sigma-28-45mm-art.html`):
       - Sviluppato il concetto di *"tre ottiche fisse F1.8 in un unico zoom"*.
       - Spiegata la meccanica dello *zoom interno* con baricentro invariato (ideale su astroinseguitore e gimbal).
       - Raccontata l'esperienza nel wedding (movimento consapevole) e la straordinaria resa del coma a F1.8 lungo tutto il range in astrofotografia (*"entrato a gamba tesa nell'astro kit per restarci"*).
  - Inseriti placeholder espliciti e descrittivi per tutte le immagini intermedie, crop e confronti, con relative tabelle tecniche e griglie PRO/CONTRO.


## [2026-08-25] feature / one-eyeland | Integrazione dei 2 premi ufficiali One Eyeland (Italy Rank #1 e Silver Award)

- **SitoDave (`L:\Sito_Dave`)**:
  - Analizzate le immagini ufficiali One Eyeland (`World's Top 10 Fine Art Photo Contest 2025`):
    1. **Italy Rank #1 (1° Classificato Italia)** • Fotografia *Roque Cinchado under the Galactic Core (Tenerife)* con badge dorato Top 10 e logo One Eyeland.
    2. **Silver Award (Medaglia d'Argento)** • Fotografia *Roque Cinchado under the Galactic Core (Tenerife)* con badge d'argento Top 10 e logo One Eyeland.
  - Ottimizzati e salvati gli asset in `assets/awards/one_eyeland_rank1_italy_2025.jpg` e `assets/awards/one_eyeland_silver_2025.jpg`.
  - Integrato il link diretto ufficiale di verifica: `https://oneeyeland.com/world-top10-fine-art-photographers-2025`.
  - Aggiornato `data/awards.json`, sincronizzato `main.js` ed impostato il badge contatore homepage su **One Eyeland (2)**.


## [2026-08-25] feature / bpa | Integrazione completa dei 5 premi Best Photography Awards

- **SitoDave (`L:\Sito_Dave`)**:
  - Eseguita scansione accurata dell'archivio postale Thunderbird (`daveluongo.ph@gmail.com`) e verificati i 5 riconoscimenti ufficiali assegnati da Best Photography Awards:
    1. **Silver Medal (2° Posto)** • Categoria Nature (Entry #3909, Edizione 2025-26)
    2. **Bronze Medal (3° Posto)** • Categoria Night Photography (Entry #3908, Edizione 2025-26)
    3. **Blue Medal (Honorable Mention)** • Categoria Nature (Entry #3908, Edizione 2025-26)
    4. **Blue Medal (Honorable Mention)** • Categoria Nature (Entry #4075, Edizione 2025-26)
    5. **Blue Medal (Honorable Mention)** • Categoria Nature (Entry #2477, Edizione 2024-25, *Pan di marmotta*)
  - Integrati i link di verifica ufficiali diretti per ciascuno dei 5 premi, le medaglie associate e le fotografie premiate in alta definizione.
  - Aggiornato il contatore nella barra homepage a **BPA (5)**.


## [2026-08-25] decision / sito | Ottimizzazione rimandata alla chiusura delle modifiche

- Davide continua in autonomia le modifiche al nuovo sito.
- Nessun intervento di ottimizzazione va applicato finché struttura, contenuti e asset non saranno dichiarati conclusi.
- A sito finito verrà preparato uno script unico di ottimizzazione con backup, verifiche prima/dopo e possibilità di rollback.

## [2026-08-25] fix / awards | Incorporamento dati completi premi e gallerie in main.js per protocollo locale

- **SitoDave (`L:\Sito_Dave`)**:
  - Incorporati direttamente in `main.js` (`DEFAULT_AWARDS_DATA` e `DEFAULT_GALLERIES_DATA`) tutti i certificati, le medaglie, le 6 opere 1x e le 4 gallerie fotografiche.
  - Risolto il problema di visualizzazione quando il sito viene aperto in locale su protocollo `file://` (dove le policy di sicurezza dei browser bloccano le `fetch` locali dei file JSON).
  - Aggiornati i badge numerici dei concorsi in `index.html`: **BPA (3)**, **One Eyeland (1)**, **1x.com (7)**.


## [2026-08-25] feature / awards | Integrazione Certificati, Medaglie e Banner Ufficiali dei Concorsi

- **SitoDave (`L:\Sito_Dave`)**:
  - Estratti e integrati in `assets/awards/` tutti i materiali e i certificati ufficiali:
    - **Best Photography Awards**: medaglie ufficiali (Silver Medal, Bronze Medal, Blue Medal) e fotografie premiate (Astrofotografia Nivolet e Paesaggio).
    - **1x.com**: certificato ufficiale Awarded Photographer (`awarded_photographer_certificate-796527.jpg`) e 6 banner ufficiali delle opere premiate e pubblicate dai curatori.
    - **One Eyeland**: vittoria Fine Art 2025 Country Winner Italia (Rank 1 con 10 punti).
  - Aggiornato `data/awards.json` con metadati reali, percorsi delle immagini e link diretti ai portali di verifica.
  - Aggiornato `main.js` per mostrare le medaglie nelle card e i certificati/banner in alta definizione nel popup di verifica con pulsante di verifica diretta.


## [2026-08-25] audit / sito | Verifica nuovo sito e articoli SIGMA

- Confrontato `L:\Sito_Dave` sul ramo `main`, commit `0759587`, con lo stato registrato nel Second Brain.
- Integrato l'audit di concept dopo la precisazione di Davide: efficacia del posizionamento, chiarezza della promessa, gerarchia tra offerta principale e progetti paralleli, ruolo di gallerie, premi, team e articoli SIGMA.
- Esito concettuale: identità fotografica e prove sono forti, ma la homepage non rende ancora centrale il Metodo SIS; troppi contenuti ricevono lo stesso peso e la biografia arriva troppo tardi.
- Distinti i flussi operativi dai segnaposto intenzionali: Dardagna pubblicata con flusso autonomo; Canfaito e Foreste locali con fotografie da sostituire; viaggi 2027, workshop 2027 e fotochiacchierate ancora informativi.
- Verificate le nuove sezioni Premi e Gallerie; i banner dei certificati premio risultano ancora placeholder.
- Rilevati link partner vuoti nei footer e più copie delle landing da mantenere sincronizzate.
- Auditati i cinque articoli SIGMA locali: struttura completa, ma tono troppo promozionale, introduzioni duplicate e affermazioni tecniche assolute da verificare.
- Creata la nota [`wiki/reports/site-audit-2026-08-25.md`](reports/site-audit-2026-08-25.md) con problemi, priorità e piano di revisione.
- Nessuna modifica applicata al repository del sito.

## [2026-08-25] archive / awards | Materiali One Eyeland aggiunti manualmente

- Confermata la presenza in `L:\1_Social\One Eyeland` di `watermark-socialcrop.jpg` e `watermark-socialcrop (1).jpg`, aggiunti manualmente da Davide.
- I file sono stati lasciati invariati; i nomi non permettono da soli di associare con certezza ciascuna immagine al relativo premio.

## [2026-08-25] fix / awards | Recuperata menzione d'onore BPA 2024

- Identificata nella galleria ufficiale Best Photography Awards 2024 la menzione d'onore di Davide Luongo in Amateur Nature per `Pan di marmotta` (`entry=2477`, `form_id=2240`).
- Scaricata l'immagine ufficiale in `L:\1_Social\Best Photography Awards\2024 - Honorable Mention - Pan di marmotta - Davide Luongo.jpg` e aggiornato il manifesto con URL di verifica e SHA-256.
- La mail del 27 agosto 2024 è una conferma d'iscrizione, non la comunicazione del premio; il risultato è stato quindi verificato sulla galleria BPA.

## [2026-08-25] fix / footer | Aggiornamento canali Social (Instagram @davepics_91, rimozione Facebook, aggiunta YouTube @davepics_91)

- **SitoDave (`L:\Sito_Dave`)**:
  - Aggiornato il link Instagram nel footer di `index.html` e `one-to-one/one-to-one.html` verso `https://www.instagram.com/davepics_91/` (`@davepics_91`).
  - Rimosso il link obsoleto a Facebook.
  - Aggiunto il link ufficiale a YouTube verso `https://www.youtube.com/@davepics_91` (`@davepics_91`).


## [2026-08-25] archive / awards | Raccolta materiali premi fotografici dalle email

- Cercate nella casella Gmail disponibile le comunicazioni relative a Best Photography Awards, One Eyeland e 1x, distinguendo i risultati personali dalle newsletter e dalle call for entry.
- Salvati in `L:\1_Social\Best Photography Awards` i materiali BPA 2024-25 e 2025-26: medaglie blu, bronzo e argento e tre fotografie associate.
- Salvati in `L:\1_Social\1x` sei file social delle fotografie premiate e il certificato ufficiale `awarded_photographer_certificate-796527.jpg`.
- Verificata nell'email One Eyeland la vittoria Fine Art 2025 come Country Winner per l'Italia, rank 1 con 10 punti. Certificati e badge non sono stati scaricati perché la pagina dedicata richiede un login One Eyeland separato.
- Creato `L:\1_Social\awards_download_manifest_2026-08-25.csv` con stato, destinazione e SHA-256; un duplicato BPA è stato rilevato e non copiato.

## [2026-08-25] feature / galleries | Nuova area Gallerie Fotografiche (Islanda, Tenerife, Madeira, Montagna)

- **SitoDave (`L:\Sito_Dave`)**:
  - Creata la nuova sezione **Gallerie Fotografiche** (`#gallerie`) in `index.html` con 4 card verticali d'impatto ad alto contrasto e tipografia dedicata: **Islanda**, **Tenerife**, **Madeira** e **Montagna**.
  - Aggiunto il link `Gallerie` nella navbar per una navigazione rapida.
  - Creata la base dati in `data/galleries.json` con 10 immagini/placeholder strutturate per ciascuna delle 4 gallerie (titolo, didascalia, thumb, e numerazione `1 / 10`).
  - Implementato in `main.js` il sistema di modali/lightbox:
    - Popup della galleria con griglia responsive a 10 foto.
    - Lightbox ingrandito per la visualizzazione a pieno schermo con navigazione foto precedente/successiva (`←` / `→`), supporto a tastiera (tasto ESC, frecce) e swipe.
  - Aggiunti stili dedicati in `style.css` e verificata la test suite (29/29 superati).


## [2026-08-25] clean / homepage | Rimozione card di anteprima articoli dal blog

- **SitoDave (`L:\Sito_Dave`)**:
  - Rimosse le 3 card di anteprima articoli da `index.html`.
  - Trasformata la sezione *Blog & Pubblicazioni* in un banner pulito ed elegante con titolo, descrizione e pulsante di collegamento rapido **"Vedi Tutti gli Articoli →"** che porta direttamente all'archivio completo `blog/blog.html`.
  - Pulito `main.js` rimuovendo il codice ridondante di iniezione delle card in homepage.


## [2026-08-25] fix / blog | Eliminazione scritta "Vai al Blog completo" e fallback schede reali

- **SitoDave (`L:\Sito_Dave`)**:
  - Rimossa la stringa di fallback "Vai al Blog completo" in `main.js`.
  - Integrato un fallback resiliente con gli articoli in evidenza reali (`DEFAULT_HOMEPAGE_ARTICLES`), garantendo che la griglia del blog mostri sempre le card complete e formattate (anche in caso di consultazione locale su protocollo `file://` o fetch offline).


## [2026-08-25] feature / awards | Sezione Premi & Riconoscimenti con Contatori Dinamici e Modal di Verifica

- **SitoDave (`L:\Sito_Dave`)**:
  - Creata la nuova area **Premi & Riconoscimenti** subito sotto il carosello delle recensioni in `index.html`.
  - Aggiunti i badge interattivi per i concorsi richiesti: **Best Photography Awards** (BPA), **One Eyeland** e **1x.com**, con pillola contatore incrementale alimentata dinamicamente dal numero di premi vinti.
  - Creata la base dati strutturata in `data/awards.json` contenente per ciascun concorso l'elenco premi, l'anno, il titolo della menzione/vittoria e l'opera fotografica associata.
  - Implementato in `main.js` il sistema di modali/popup:
    - Popup di concorso con l'elenco dei riconoscimenti e pulsante *"Verifica Riconoscimento ↗"*.
    - Popup di verifica/anteprima certificato (attualmente con placeholder dedicato e pronto per accogliere i banner ufficiali definitivi).
  - Aggiunti stili dedicati in `style.css` e verificata la test suite (29/29 superati).


## [2026-08-25] style / team | Layout Team (4 membri prima riga + 2 membri centrati seconda riga)

- **SitoDave (`L:\Sito_Dave`)**:
  - Aggiornato il layout CSS di `.team-grid` e `.team-card` in `style.css`: configurato un layout a 4 colonne per la prima riga (`flex: 0 0 calc(25% - 1.5rem)`) con `justify-content: center`, in modo che i 2 membri sottostanti risultino posizionati al centro della sezione, sotto le card centrali.
  - Mantenuta piena responsività: 2 colonne per riga su tablet e 1 colonna su smartphone.


## [2026-08-25] fix / ui | Ripristino Caroselli 3D Rotanti per Workshop e Viaggi

- **SitoDave (`L:\Sito_Dave`)**:
  - Ripristinato e integrato nel motore globale `main.js` il sistema di caroselli 3D rotanti con gestione classi (`is-active`, `is-previous`, `is-next`, `is-hidden`) per tutte le sezioni `[data-carousel]`.
  - Aggiunti controlli di navigazione completi (frecce circolari interattive `data-carousel-prev` / `data-carousel-next` e contatore di stato `.carousel-status-pill`) nelle testate di Workshop 2026 e Viaggi 2027 in `index.html`.
  - Aggiunto supporto completo a rotazione con clic su card laterale, hover/pointerenter, frecce da tastiera e swipe touch su mobile.
  - Aggiornati stili in `style.css` e test suite (29/29 superati).


## [2026-08-25] fix / navigation | Collegamento pulsante hero One-to-One

- **SitoDave (`L:\Sito_Dave`)**:
  - Aggiornato il pulsante secondario della Hero in `index.html` ("Corsi One-to-One", posizionato accanto a "Scegli la tua prossima avventura"): sostituito il vecchio anchor `#corsi` con il link diretto alla pagina dedicata `one-to-one/one-to-one.html`.
  - Verificata la navigazione coerente tra navbar, hero e footer. Test suite (29 test) superata al 100%.


## [2026-08-24] adaptation / Instagram | Asterra Z+ in 60 secondi

- Condensato lo script YouTube Asterra Z+ in una versione parlata per Reel da circa 60 secondi.
- Conservato il punto centrale degli 850 grammi come riduzione del peso fisico e del carico mentale; chiusura lasciata sul futuro test sul campo.
- Esportate una versione italiana e una traduzione inglese naturale in due PDF locali su pagina singola. I file non sono stati copiati nel repository.

## [2026-08-24] production / YouTube | Script Asterra Z+

- Recuperato e impaginato lo script completo del primo contatto con Asterra Z+, mantenendo le indicazioni di ripresa.
- Prodotti due PDF locali: versione italiana e traduzione inglese naturale per il parlato.
- Registrato come passaggio successivo il test sul campo a 100, 200 e 400 mm. I PDF non sono stati copiati nel repository.

## [2026-08-24] archive / formazione | Serie UGC Starter Kit

- Individuate nella casella professionale Aruba le sette email inviate da Noemi Colaianni tra l'8 e il 20 giugno 2026 e verificate come lette.
- La serie tratta avvio nel lavoro UGC, differenza tra creator e influencer, criteri usati dai brand, errori iniziali, tariffe dichiarate, scelta della formazione e invito finale al percorso commerciale.
- Nessun allegato tradizionale. Scaricata fuori dal repository la guida PDF collegata; gli altri link portano a Instagram, YouTube, WhatsApp o pagine di testimonianze.
- Nessun contenuto integrale delle email, dato privato o file scaricato è stato aggiunto alla wiki.

## [2026-08-24] refinement / Instagram | Tono della bio

- Rivista la bio proposta per eliminare la possibile distanza creata da “ti aiuto” e dalla promessa assoluta “con me diventerà semplice”.
- Preferita la formulazione “La fotografia di paesaggio sembra complessa. Insieme la rendiamo più semplice”, coerente con il ruolo di guida e con il tono paritario definito nel Metodo SIS.
- Nessuna modifica applicata al profilo Instagram.

## [2026-08-24] planning / Instagram | Nuova bio orientata alla conversione

- Verificata direttamente la bio pubblica di `@davepics_91`: ruolo, ambassador e premi occupano lo spazio senza spiegare destinatario, risultato e offerta.
- Preparata una nuova bio in italiano centrata su metodo, sviluppo di una fotografia personale, workshop, percorsi individuali e CTA verso il Friuli.
- La proposta è registrata per revisione; nessuna modifica applicata al profilo Instagram.

## [2026-08-24] ingest / brand | Verifica completa fonti Metodo SIS su Drive

- Letta in sola lettura la cartella Drive condivisa da Davide: tre dispense SIS, sedici esercizi compilati e il documento finale “Davide Luongo - La Bussola”.
- Verificata direttamente la provenienza dei contenuti già sintetizzati il 5 agosto, senza copiare gli allegati originali nel repository.
- Integrati nella pagina identitaria la storia formativa con Franz, Gaspare Silverii ed Erik, l'esempio cliente di Flavio, il cliente ideale, i confini dell'offerta e l'architettura editoriale proposta dalla Bussola.
- Nessun file o dato della cartella Drive è stato modificato.

## [2026-08-21] diagnosis / backend | WordPress Aruba e FastAPI locale non collegati

- Verificato in sola lettura il nuovo `https://www.davideluongo.it/`: il dominio serve WordPress e `/wp-admin/` reindirizza correttamente alla schermata di login, senza pagina bianca, loop o errore PHP visibile.
- `https://www.davideluongo.it/api/health` restituisce la pagina 404 di WordPress: il backend FastAPI di `L:\Sito_Dave` non è pubblicato né instradato sul dominio Aruba.
- Verificato `L:\Sito_Dave` in locale senza modifiche: avvio con `python -m backend.run`, `/api/health` HTTP 200, `/admin/` HTTP 200 e suite completa con 29 test superati.
- Diagnosi: il codice FastAPI locale funziona; il problema è il disallineamento architetturale/deployment tra il nuovo WordPress su Aruba e il backend presente nel repository. Nessuna modifica applicata al sito o a WordPress.

## [2026-08-21] feature / backend / admin | Evoluzione Backend FastAPI, CRM Contatti, Template Esperienze e 2FA Admin

- **SitoDave (`L:\Sito_Dave`)**:
  - **Export Partecipanti Estemporaneo**: Implementato endpoint isolato `GET /api/admin/participants/export` per il download istantaneo in XLSX (fogli Partecipanti, Riepilogo, Costi) con filtri per stato, data e formula, sanificazione formule `=/+/-/@` e nessuna alterazione di stato o cutoff.
  - **Template Esperienze & Viaggi Internazionali**: Modelli unificati con template versionati `workshop-v1` e `international-trip-v1`, controlli pre-pubblicazione (Tour Operator, documenti, date, prezzi, assenza placeholder `[TODO]`), wizard e render deterministico HTML.
  - **CRM Contatti & Rubrica**: Modello dati relazionale completo (`Contact`, `ContactInteraction`, `Tag`), acquisizione automatica da form contatti, avvisi e ordini PayPal con deduplicazione (email/telefono) e calcolo stati (`new_lead` -> `customer` -> `loyal_customer`), gestione blacklist con motivo, import/export CSV con UTF-8 BOM, delimitatore configurabile e strategie di risoluzione conflitti.
  - **Autenticazione 2FA Email OTP & Recovery Codes**: Login a due fasi obbligatorio con codice a 6 cifre inviato via email (validità 10 min, cooldown 60s, max 5 tentativi), challenge token HMAC effimero e 8 codici di recupero monouso per emergenza, gestione revoca sessioni multiple.
  - **Pipeline Video & Background Jobs**: Endpoint `POST /upload-video` con transcodifica FFmpeg asincrona (1080p, 720p H.264 web-ready, faststart, audio AAC, poster WebP/JPEG), gestione formato verticale e tracciamento progresso in database `Job`.
  - **Backup SQLite Atomico**: Servizio di copia atomica a caldo con verifica di integrità `PRAGMA quick_check`, hash SHA-256 e download protetto da admin panel.
  - **Frontend Admin Panel**: Ridisegnate `admin/index.html` (login 2FA), `admin/dashboard.html`, `admin/admin.js` e `admin/admin.css` con tab e modali dedicate per Esperienze/Viaggi, CRM contatti, Media & Video, Sicurezza e Backup.
  - **Qualità & Test**: Suite estesa con 29 test automatizzati pytest (`tests/test_evolution.py` + baseline completa) superati con successo (29 passed).
- **Davide Second Brain**: Aggiornata documentazione di progetto e registro log; lint wiki verificato senza errori.


## [2026-08-21] feature / content | Riprogettazione Pagina One-to-One e Motore Pricing

- **SitoDave (`L:\Sito_Dave`)**:
  - Riprogettata la pagina `one-to-one/one-to-one.html` secondo le direttive visive e commerciali:
    - Footer unificato e coerente al 100% con `index.html` (P.IVA IT03043130737, link e colonne identiche).
    - Inseriti 3 confronti RAW / Elaborato orizzontali subito sotto la Hero (Via Lattea Nivolet, Cascate del Dardagna, Laghi di Fusine) con slider fluido mouse, touch e tastiera.
    - Sezione Vantaggi riscritta in prima persona: "In gruppo è sicuramente bellissimo, ma nel One-to-One sono tutto per te", card personalizzazione ("Costruire il tuo stile, non copiare il mio") e card registrazioni/Drive condiviso con file .xmp, .psd e appunti Gemini.
    - Due percorsi principali (Percorso da remoto e Percorso dal vivo) con pulsante "Richiedi un preventivo" e modale accessibile collegata a `api/send-info-email.php`.
    - Terza card "Acquista le tue ore": selettore 1..5 ore con calcolo dinamico del prezzo (80 €/h, sconti progressivi 0%, 10%, 20%, 30%, 40%), prezzi barrati, badge percentuale e checkout PayPal Sandbox integrato con validazione server-side.
    - Come funziona il percorso in 4 step e 9 FAQ con accordion accessibile.
  - Aggiornati i backend `backend/app/routes/paypal.py` e `api/create-paypal-order.php` con calcolo sicuro dei prezzi e test di regressione pytest passati (23/23).
- **Davide Second Brain**: Aggiornato registro modifiche e allineata la documentazione operativa.


## [2026-08-21] audit / planning | Evoluzione backend SitoDave

- Auditata la baseline FastAPI, SQLite e admin senza modificare il sito.
- Confermate funzioni già presenti: CMS a blocchi, revisioni, workshop, partecipanti, PayPal Sandbox, report XLSX, sicurezza sessioni e pipeline immagini fino a 2048 px.
- Definiti i prossimi ambiti: export partecipanti indipendente dal cutoff, template uniformi per workshop e viaggi, CRM con CSV e blacklist, video 1080p/720p e OTP email di dieci minuti.
- Durante l'audit sono comparsi sei asset RAW/elaborato non versionati nel repository del sito; sono stati lasciati intatti come modifiche esterne.
- Nessuna modifica applicata a `Sito_Dave`; il risultato operativo di questa fase è un prompt per Antigravity.

## [2026-08-21] planning | Nuova impostazione commerciale One-to-One

- Registrata la proposta di revisione della pagina: footer coerente con il sito, tre confronti RAW/elaborato, due percorsi principali (remoto e dal vivo) e una terza scheda per comprare ore.
- Definiti materiali delle lezioni online (registrazione, appunti Gemini, XMP e PSD), contatto telefonico entro il giorno successivo e posizionamento centrato sullo sviluppo dello stile personale dello studente.
- Il prezzo base richiesto è 80 euro l'ora. La regola dello sconto progressivo necessita di una formula e di un limite espliciti prima di implementare il pagamento PayPal.
- Nessuna modifica eseguita sul sito in questa fase: il risultato richiesto è un prompt operativo per Antigravity.

## [2026-08-21] audit | Analisi pagina One-to-One

- Analizzata in sola lettura `L:\Sito_Dave\one-to-one\one-to-one.html` insieme a `style.css` e `main.js`.
- La pagina ha una struttura completa (hero, vantaggi, tre percorsi, metodo, FAQ e CTA), ma non chiarisce prezzi, condizioni, credenziali del docente, prove sociali e differenze operative tra le formule.
- Rilevati problemi tecnici da correggere in un intervento successivo: conferma di invio mostrata anche in caso di errore API; FAQ inizialmente aperte e primo clic inefficace; selettore inglese quasi privo di traduzioni per questa pagina; modale senza gestione completa di tastiera, focus e attributi ARIA; menu principale nascosto sotto 768 px senza alternativa.
- Nessuna modifica eseguita sul sito. Il browser integrato non consente di aprire URL `file:///`, quindi il responsive è stato valutato dal codice e richiede ancora una verifica visiva renderizzata.

## [2026-08-21] feature / content | Aggiornamento Homepage SitoDave (Story, Blog dinamico, Behind the Shot, Team)

- **SitoDave commit `e7cb68b`**:
  - **Pagina One to One (`one-to-one/one-to-one.html`)**: Istituita la pagina dedicata ai percorsi formativi individuali e mentorship di Davide Luongo, con 3 moduli formativi (Astrofotografia sul Campo, Post-Produzione Digitale avanzata e Portfolio Review/Fine Art), sezione Metodo in 4 step, FAQ e modulo di richiesta info taggato per `info@davideluongo.it`.
  - **Navigazione & Footer**: Collegata la voce "One to One" nei menu di navigazione e nei footer di tutto il sito (`index.html`, `blog/blog.html`, `gear/gear.html`).
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

## [2026-08-24] maintenance | Stato collaborazioni e controllo Thunderbird
- Incrociato il CSV disponibile con i messaggi indicizzati nella Posta in arrivo di Thunderbird.
- Registrati gli stati di ALPAKA, PGYTECH, SmallRig, SIRUI, iOptron e Vanguard; mantenute come dichiarazioni dell'utente le collaborazioni attive non ricostruibili dal solo indice.
- Annotata la differenza tra le 12 righe dell'allegato recuperato e le 21 dichiarate nella conversazione precedente.
- Preparati un master di 27 brand e un CSV residuo con le 10 proposte complete ancora da inviare.

## [2026-08-24] maintenance | Storico completo collaborazioni e affiliazioni
- Aggiunti a Thunderbird `fangoman91@gmail.com` e `daveluongo.ph@gmail.com`, mantenendo invariato l'account Aruba.
- Esteso il controllo a 3.444 messaggi ricevuti indicizzati nei tre account; Posta inviata e Tutti i messaggi non sono ancora indicizzati integralmente.
- Ricostruite 45 relazioni tra collaborazioni, affiliazioni, offerte, invii e rifiuti.
- Corretti gli stati: ORICO ripartita; SIRUI e PGYTECH da riattivare; Kase e Vallerret storiche.
- Separati link pubblici, codici personali o monouso e campagne scadute; registrati sette ordini e €94,05 di cashback sul coupon RCE al 17 agosto 2026.

## [2026-08-24] maintenance | Verifica affiliazione Move Shoot Move
- Registrato come link corrente `https://www.moveshootmove.com/it/collections/move-shoot-move-rotator?aff=13`; mantenuto `?aff=448` come riferimento storico.
- Confermati dalle email il 10% di commissione e il 5% di sconto per chi acquista dal link.
- Nessun riepilogo di ordini, vendite o commissioni compare nelle email indicizzate; il totale deve essere letto dal pannello Affiliatly.
- Annotata la soglia comunicata dal brand il 2 luglio 2026: almeno 10 ordini in un anno per la valutazione ambassador.
- Chiarito che `aff=17` non compare nelle fonti: 17 è il numero di righe affiliate del master. Il link `aff=13` deriva dalla dichiarazione diretta di Davide, mentre `aff=448` è quello confermato via email dal brand.

## [2026-08-24] maintenance | Verifica affiliazione BrightinStar
- Confermata l'approvazione dell'account GoAffPro del 14 marzo 2024 e l'esistenza attuale del programma sul sito ufficiale.
- Registrata una vendita verificata: ordine `US2883`, valore `60,17 USD`, commissione `6,02 USD`; nessuna prova del pagamento nelle email.
- Aggiornata la struttura corrente: 5% generale, 10% sul 28mm F2.8 e indicazione pubblica “fino al 10%”.

## [2026-08-24] maintenance | Rendimenti affiliate e provvigioni Vanguard
- Ricostruiti i rendiconti Vanguard: due ordini nel 2023, €26,55 di commissioni; un ordine nel 2024, €12,98; nessun ordine con codice nel 2025.
- Separata la commissione monetaria dal credito prodotto raddoppiato: €39,53 maturati e €79,06 di credito utilizzato per VEO SELECT 39RBM.
- Inseriti nel master i link personali trovati nel foglio Google per Maven (`aff=171`), H&Y (`aff=18`) e BrightinStar, oltre al codice Vanguard `DAVIPRO2026`.
- Aggiunta la scheda Rendimenti affiliate con 11 ordini verificati: Vanguard 3, BrightinStar 1 e RCE 7. Totali documentati: €133,58 e 6,02 USD, senza sommare due volte il credito prodotto Vanguard.
- Verificati i programmi pubblici Kolari Vision e Cinomadist; le iscrizioni non sono state inviate perché richiedono conferma finale e dati di account/pagamento.

## [2026-08-24] maintenance | Copia master collaborazioni in archivio social
- Copiati `Master_Storico_Collaborazioni_Completo.xlsx` e `thunderbird_brand_collaborations_da_contattare.csv` in `L:\1_Social`.
- Verificata l'identità delle copie tramite hash SHA-256.

## [2026-08-24] maintenance | Copia outreach Islanda in archivio social
- Copiati in `L:\1_Social` i workbook e i CSV dell'outreach Islanda 2026: strutture ricettive, autonoleggi e rilancio puffin per agosto 2027.
- Conservati gli originali nella cartella di lavoro Codex e verificata l'identità delle cinque copie tramite hash SHA-256.

## [2026-08-26] maintenance | Aggiornamento tracking outreach Islanda
- Controllata in sola lettura la Webmail Aruba: nessuna email inviata o modificata.
- Registrata l'accettazione di Afternoon Cottages, con finestra indicata da Davide tra il 4 e il 7 dicembre.
- Registrata la richiesta di media kit ed esempi da Hotel Örk e il rifiuto definitivo di Blue Hotel & Cabins.
- Chiuso Hotel Skógafoss dopo 7 giorni lavorativi senza risposta; riepilogo corrente: 1 `OK`, 15 `APERTO`, 4 `CHIUSO`, 5 `NON INVIATA`.
- Aggiornato e sincronizzato `L:\1_Social\Outreach_Islanda_2026.xlsx`; creata la scheda `wiki/projects/outreach-islanda-2026.md`.

## [2026-08-24] maintenance | Consegna CSV collaborazioni e verifica form WANDRD
- Consegnata una copia verificata del CSV residuo con 10 brand ancora da contattare; hash SHA-256 `462E4CD875AD2FE4E829DDB522F869F94F34F21E69A10CA9D4253005029EEAFC`.
- Confermato che WANDRD usa il form Creator Community collegato dalla pagina ufficiale Affiliates & Collaborators e riesamina le candidature ogni trimestre.
- Preparata una risposta personalizzata sul profilo outdoor e landscape di Davide, sulle attività da Sigma Ambassador e sull'uso reale dell'attrezzatura durante workshop e photo tour; nessun form inviato.
- Corretta la guida Mail Merge: la variabile destinatario del CSV è `{{Email}}`, senza spazi tra le parentesi e rispettando la E maiuscola dell'intestazione; il messaggio va generato dal comando Mail Merge, non dal normale pulsante Invia.

## [2026-08-24] maintenance | Aggiornamento master dopo il batch Mail Merge
- Analizzate le nuove email indicizzate di `info@davideluongo.it`: WANDRD richiede il form Collaborators, GOMATIC ha preso in carico la proposta, Tenba ha inviato una ricevuta automatica e Boundary Supply ha restituito un errore permanente 550 5.1.1.
- Aggiunte nove righe al master e tre stati distinti: `INVIO_DA_VERIFICARE`, `INVIO_FALLITO` e `RISPOSTA_AUTOMATICA`; i conteggi restano calcolati con formule.
- Aggiornata la copertura Thunderbird a 896 messaggi Aruba, 12.429 su `fangoman91@gmail.com` e 3.151 su `daveluongo.ph@gmail.com`.
- Sostituito `L:\1_Social\Master_Storico_Collaborazioni_Completo.xlsx` con la versione verificata; SHA-256 `A59AEC3E784A0290DA9DAD5D3594297473F434515B2026ADF9ACB3454C7AA6B8`.

## [2026-08-24] maintenance | Report completo Not Just Analytics
- Scaricato e verificato il PDF di 43 pagine per `@davepics_91`, relativo al periodo 24 luglio–24 agosto 2026.
- Aggiornata la baseline Instagram con 5.477 follower, 105.346 visualizzazioni, reach 28.310, 95 nuovi follower e unfollow rate riportato del 70,53%.
- La definizione dell'unfollow rate resta da verificare prima di usarlo come indicatore decisionale.

## [2026-08-24] maintenance | Aggiornamento e consegna media kit Canva
- Aggiornato il progetto Canva del media kit mantenendo il design esistente e usando il report Not Just Analytics del periodo 24 luglio–24 agosto 2026.
- Inseriti 5.477 follower, 67% di follower in Italia, reach totale arrotondata a 28K, 113 like medi ed engagement rate arrotondato al 2,3%.
- Riscritto il testo introduttivo in inglese, chiarite le etichette delle metriche e corretto il titolo `EDUCATIONAL REELS & POSTS`.
- Consegnato `Media_Kit_Davide_Luongo_2026.pdf` in `L:\1_Social`; copia verificata con SHA-256 `6D4876E5E2E296C371FF02C7365A5674BCBFA7BEAA681A5196BF21E5BC45A52A`.

## [2026-08-25] analysis | Lista di revisione unfollow Instagram
- Confrontati gli export Instagram del 25 agosto 2026: 2.748 following, 908 follower e 147 rapporti reciproci.
- Preparato un Excel con 2.601 account non-follow-back, link diretti, data del follow, stato modificabile e priorità di revisione.
- La priorità non determina l'unfollow: 419 profili con possibili segnali foto, travel, brand o relazioni recenti sono indicati per una verifica più cauta.
- Controllati anche profili bloccati, richieste in sospeso, richieste recenti, profili rimossi di recente e suggerimenti rimossi; nessun account bloccato era presente tra i candidati.

## [2026-08-26] analysis | Riferimenti hospitality per media kit
- Verificato il reel `DTTC2x6iCTv`, pubblicato da `@hotelkeflavik`: la caption accredita direttamente Davide Luongo come autore video.
- Verificato il reel `DNyEEpsWmie`, pubblicato da `@davepics_91`: presenta Hotel Monopol a Tenerife con testo in italiano, inglese e spagnolo.
- Per una versione hospitality del media kit, usare i due reel come lavori precedenti verificati e non come prova di performance: like e commenti pubblici non sostituiscono reach, visualizzazioni e insight completi.
- Mantenere separato il media kit fotografico generale e creare una copia dedicata a hotel e strutture ricettive.

## [2026-08-26] maintenance | Media kit hospitality Canva
- Creata e salvata una copia separata del media kit Canva, titolo `Davide Luongo - Hospitality Media Kit 2026`, design ID `DAHTXYBJzj0`.
- Conservato intatto il media kit fotografico originale `DAGe4uhSwEE`.
- Adattati presentazione e servizi a hotel e travel brand: fotografia della struttura, reel verticali, esperienza e destinazione, pacchetti foto e video.
- Inseriti Hotel Keflavik e Hotel Monopol come lavori precedenti, con collegamenti ai reel Instagram verificati.
- Le immagini restano provvisoriamente quelle del progetto originale finché non sono disponibili gli scatti hospitality ad alta risoluzione.

## [2026-08-26] analysis | Concept dati e video per media kit hospitality
- Riesaminata la versione Canva hospitality `DAHTXYBJzj0`: testi e servizi sono coerenti, ma le immagini di astrofotografia mantengono ambiguo il posizionamento.
- Davide non dispone di fotografie hospitality originali; sono disponibili soltanto i due lavori video per Hotel Keflavik e Hotel Monopol.
- Proposto un concept basato su dati NJL verificati, grafici semplici, copertine o fotogrammi dei reel e collegamenti diretti ai due lavori.
- Evitare grafici decorativi o confronti tra grandezze non omogenee; distinguere metriche del profilo dai risultati specifici dei lavori hotel, per i quali non sono disponibili insight completi.
- Nessuna modifica applicata al progetto Canva in questa fase: la revisione resta una proposta da approvare.

## [2026-08-26] maintenance | Concept video-first del media kit hospitality
- Salvato su Canva il redesign definitivo del progetto `DAHTXYBJzj0`, mantenendo separato il media kit fotografico originale `DAGe4uhSwEE`.
- Sostituite le immagini di astrofotografia con quattro pannelli basati sul report NJL 24 luglio–24 agosto 2026: visibilità del profilo, pubblico, rendimento dei post e storie.
- Inserite le copertine e le schede dei reel Hotel Keflavik e Hotel Monopol; i nomi restano collegati ai rispettivi reel.
- Posizionamento aggiornato a `Travel & Hospitality Videomaker`; servizi riscritti intorno a video per hotel, reel, esperienza e destinazione, consegne per la struttura.
- I dati NJL sono presentati come metriche generali del profilo. Nessuna performance è attribuita ai singoli hotel senza insight completi.

## [2026-08-26] outreach | Risposta media kit per Hotel Örk
- Preparata la risposta in inglese alla richiesta ricevuta da Hotel Örk, con media kit hospitality da allegare manualmente.
- Inseriti i link ai reel realizzati per Hotel Keflavik e Hotel Monopol.
- Chiarito che concept, tono e montaggio di ciascun video sono stati concordati interamente con la relativa struttura; la differenza di mood mostra quindi un adattamento al carattere e agli obiettivi dell'hotel.
- Ripreso l'interesse espresso dalla struttura per il taglio winter wellness e per il racconto dell'hotel insieme ai dintorni.
- Nessun messaggio inviato.

## [2026-08-26] maintenance | Riconciliazione completa tracking strutture Islanda
- Confrontato il workbook allegato da Davide con il file madre e conservate le regole colore per `OK`, `APERTO`, `CHIUSO` e `NON INVIATA`.
- La Webmail ha confermato quattro invii assenti dal tracking: Hotel Skógá il 18 agosto; Hotel Vík í Mýrdal, Black Beach Suites e Hotel Dyrhólaey il 17 agosto.
- Registrato l'invio del media kit hospitality e di due reel a Hotel Örk il 26 agosto alle 10:23; la trattativa resta aperta.
- Il riepilogo corretto è 24 email inviate, 5 risposte, 1 `OK`, 16 `APERTO`, 7 `CHIUSO` e 1 `NON INVIATA`.
- Buubble è l'unico contatto pendente e usa esclusivamente il form ufficiale; la bozza è stata inserita nella nuova scheda `Da inviare` del workbook madre.
- Sincronizzato `L:\1_Social\Outreach_Islanda_2026.xlsx` dopo verifica di formule, colori, layout e hash SHA-256.

## [2026-08-26] maintenance | Aggiornamento master collaborazioni da Thunderbird
- Controllati i nuovi messaggi indicizzati nei tre account Thunderbird, con priorità a `info@davideluongo.it`.
- Aggiornati Shimoda e Peak Design da invio da verificare a risposta ricevuta o follow-up; aggiunti GRAYL, Afternoon Cottages e Hotel Örk senza duplicati.
- Le newsletter SIRUI e la risposta automatica Sigma non hanno cambiato lo stato delle collaborazioni.
- Il master contiene ora 57 realtà. I conteggi restano calcolati con formule e la copertura Thunderbird è aggiornata al 26 agosto 2026.

## [2026-08-26] maintenance | Raccolta JPG Islanda per il sito
- Scansionate le unità collegate `C:`, `D:`, `G:`, `I:`, `J:`, `K:`, `L:` e `Y:` cercando file `.jpg` e `.jpeg` riconducibili all'Islanda tramite cartelle, nomi e località.
- Copiati 588 file in `L:\1\_Social\SITO DATA\Islanda`, per 11,01 GB: 270 da `I:`, 315 da `K:`, 2 da `L:` e 1 da `C:`.
- Saltati 3 duplicati identici verificati con hash SHA-256. Escluse le miniature delle videocamere, le copie di backup WordPress e le riduzioni automatiche con dimensioni nel nome.
- Gli originali non sono stati spostati né cancellati. Il manifesto completo delle provenienze è `L:\1\_Social\SITO DATA\Islanda\_manifest_copia_islanda.csv`; tutti i 588 percorsi di destinazione risultano presenti.

## [2026-08-27] maintenance | Raccolte JPG Madeira e Tenerife per il sito
- Scansionate le unità disponibili `C:`, `D:`, `G:`, `I:`, `J:`, `K:` e `L:` cercando file `.jpg` e `.jpeg` tramite destinazione e località riconoscibili. L'unità `Y:` non era collegata durante questa scansione.
- Copiati 87 file di Tenerife in `L:\1\_Social\SITO DATA\Tenerife`, per 0,965 GB: 82 da `I:`, 3 da `J:`, 1 da `C:` e 1 da `L:`. Saltati 12 duplicati identici tramite hash SHA-256.
- Per Madeira è stato trovato un solo JPG certo, `Madeira-26.jpg`, copiato da `L:` in `L:\1\_Social\SITO DATA\Madeira`. Le altre occorrenze erano riduzioni automatiche o backup WordPress dello stesso file e sono state escluse.
- Gli originali non sono stati spostati né cancellati. I manifesti sono `_manifest_copia_tenerife.csv` e `_manifest_copia_madeira.csv` nelle rispettive cartelle; tutti gli 88 percorsi registrati risultano presenti.

## [2026-08-27] maintenance | Integrazione raccolte fotografiche dal disco Elements
- Scansionato il nuovo disco `M:` (`Elements`) per Islanda, Tenerife e Madeira, limitando la selezione ai file `.jpg` e `.jpeg` riconducibili alle destinazioni tramite cartelle, nomi e località.
- Madeira: aggiunti 307 file da `M:\0326_Madeira` e `M:\Backup`. La raccolta contiene ora 308 JPG per 3,145 GB.
- Tenerife: aggiunto 1 file da `M:\Backup`. La raccolta contiene ora 88 JPG per 0,966 GB.
- Islanda: i 2 candidati trovati su `M:` erano duplicati identici di file già raccolti e non sono stati ricopiati. Il totale resta 588 JPG per 11,006 GB.
- Nessun errore e nessun originale spostato o cancellato. I manifesti delle tre cartelle sono stati aggiornati; tutti i 984 percorsi registrati risultano presenti.

## [2026-08-27] outreach | Media kit INWILD / J Sport
- Analizzato il media kit Canva originale `DAGe4uhSwEE` senza modificarlo: due pagine A4, fotografia dominante, serif bianco e blu scuro.
- Preparato un PDF separato di 11 pagine per la proposta INWILD / J Sport. Il concept è un kit outdoor compatto e modulare, compatibile con il bagaglio a mano e usato nei progetti 2026-2027.
- Inseriti Islanda dicembre 2026 da confermare, Lapponia gennaio 2027, Thailandia 2027, Minorca maggio 2027, Azzorre luglio 2027 e Islanda ottobre 2027.
- La raccolta pubblica Instagram `Vanguard Pro` è stata verificata, ma le storie non erano accessibili senza login. Il case study usa quindi soltanto fatti già documentati: attrezzatura Vanguard sul campo e possibilità di prova durante i workshop.
- Il PDF è pronto per la revisione. Nessuna email è stata inviata a J Sport.

## [2026-08-27] maintenance | Progetto Canva INWILD / J Sport
- Il flusso automatico di generazione Canva è rimasto fermo alla fase di scelta del riferimento, anche dopo il riavvio segnalato da Davide.
- Creata una copia separata del media kit hospitality `DAHTXYBJzj0` e trasformata direttamente nel progetto `Davide Luongo × INWILD / J Sport - One kit. Multiple environments.`, design ID `DAHTejEGIjs`.
- Conservati griglia, palette, font e proporzioni del riferimento. La prima pagina raccoglie profilo, metriche e concept carry-on; la seconda riunisce kit, calendario, workshop e prova sul campo Vanguard.
- Inserite tre fotografie recuperate dai due post Instagram indicati da Davide: zaino e treppiede Vanguard sul ghiaccio, Davide con lo zaino davanti alla cascata e paesaggio di Madeira.
- La cartella Google Drive fornita non era accessibile con l'account `daveluongo.ph@gmail.com`; non è stata inviata una richiesta di accesso.
- Le modifiche sono state approvate da Davide e salvate su Canva. Nessuna email è stata inviata a J Sport.

## [2026-08-27] maintenance | Controllo raccolte fotografiche sul disco Data
- Scansionato il disco `M:` (`Data`, seriale `CE8BEF62`) per file `.jpg` e `.jpeg` riconducibili a Islanda, Tenerife e Madeira.
- Islanda e Madeira non hanno prodotto candidati. Per Tenerife sono stati trovati 4 file, tutti identici a immagini già presenti e quindi non ricopiati.
- I totali restano 588 JPG Islanda, 88 JPG Tenerife e 308 JPG Madeira. Tutti i 984 percorsi registrati nei manifesti risultano presenti.
- Nessun errore e nessun originale spostato o cancellato.

## [2026-08-27] maintenance | Integrazione Islanda dal secondo disco Data
- Scansionato il disco `M:` (`Data`, seriale `0609FCF1`) per Islanda, Tenerife e Madeira, limitando la selezione ai file `.jpg` e `.jpeg`.
- Islanda: trovati 364 candidati, aggiunti 53 file nuovi e saltati 311 duplicati identici. I nuovi file provengono da cartelle `Islanda_2025` e `Islanda_2025_2`, soprattutto dalle esportazioni A7RIII, BF e FPL.
- Tenerife e Madeira non hanno prodotto candidati. I totali sono ora 641 JPG Islanda, 88 JPG Tenerife e 308 JPG Madeira.
- Nessun errore e nessun originale spostato o cancellato. Tutti i 1.037 percorsi registrati nei manifesti risultano presenti.

## [2026-08-27] maintenance | Controllo raccolte sul terzo disco Data
- Scansionato il disco `M:` (`Data`, seriale `8286ECD3`) per file `.jpg` e `.jpeg` riconducibili a Islanda, Tenerife e Madeira.
- Nessuna delle tre destinazioni ha prodotto candidati. I totali restano 641 JPG Islanda, 88 JPG Tenerife e 308 JPG Madeira.
- Nessun errore e nessun originale spostato o cancellato. Tutti i 1.037 percorsi registrati nei manifesti risultano presenti.

## [2026-08-27] maintenance | Controllo raccolte sul quarto disco Data
- Scansionato il disco `M:` (`Data`, seriale `FA24CA0F`) per file `.jpg` e `.jpeg` riconducibili a Islanda, Tenerife e Madeira.
- Il disco era quasi vuoto e nessuna delle tre destinazioni ha prodotto candidati. I totali restano 641 JPG Islanda, 88 JPG Tenerife e 308 JPG Madeira.
- Nessun errore e nessun originale spostato o cancellato. Tutti i 1.037 percorsi registrati nei manifesti risultano presenti.

## [2026-08-27] maintenance | Integrazione Madeira dal disco SanDisk
- Scansionato il disco `M:` (`SanDisk`, seriale `BACE7454`) per Islanda, Tenerife e Madeira, limitando la selezione ai file `.jpg` e `.jpeg`.
- Madeira: trovati 74 candidati nella cartella `M:\Madeira_2025`, aggiunti 73 file nuovi e saltato 1 duplicato identico. Le fonti comprendono esportazioni, versioni web, GoPro e Sony.
- Islanda e Tenerife non hanno prodotto candidati. I totali sono ora 641 JPG Islanda, 88 JPG Tenerife e 381 JPG Madeira.
- Nessun errore e nessun originale spostato o cancellato. Tutti i 1.110 percorsi registrati nei manifesti risultano presenti.

## [2026-08-27] maintenance | Integrazione Tenerife dal disco senza etichetta
- Scansionato il disco `M:` senza etichetta, seriale `16BABE6A`, per Islanda, Tenerife e Madeira, limitando la selezione ai file `.jpg` e `.jpeg`.
- Tenerife: aggiunti 26 file dalla cartella `M:\24072027_Teide\Foto`, provenienti dalle sottocartelle A6700 e A7RIIIA. La raccolta contiene ora 114 JPG per 1,500 GB.
- Islanda e Madeira non hanno prodotto candidati. I totali restano 641 JPG Islanda e 381 JPG Madeira.
- Nessun errore e nessun originale spostato o cancellato. Tutti i 1.136 percorsi registrati nei manifesti risultano presenti.

## [2026-08-27] maintenance | Integrazione Tenerife 2026 dal secondo disco senza etichetta
- Scansionato il disco `M:` senza etichetta, seriale `0E088000`, per Islanda, Tenerife e Madeira, limitando la selezione ai file `.jpg` e `.jpeg`.
- Tenerife: aggiunti 20 file dalla cartella `M:\Tenerife_2026`, provenienti dalle esportazioni, da Osmo Nano, Sony A7RIII e dalla sottocartella `Sky`. La raccolta contiene ora 134 JPG per 1,879 GB.
- Islanda e Madeira non hanno prodotto candidati. I totali restano 641 JPG Islanda e 381 JPG Madeira.
- Nessun errore e nessun originale spostato o cancellato. Tutti i 1.156 percorsi registrati nei manifesti risultano presenti.

## [2026-08-27] maintenance | Recupero JPEG 1x da Thunderbird
- Controllata la Posta in arrivo locale Thunderbird dell'account `daveluongo.ph@gmail.com`, associata alla cartella IMAP `imap.gmail-1.com`.
- Individuati 47 messaggi provenienti da domini `1x.com` con 38 allegati JPEG complessivi. Sette file erano già presenti nell'archivio; aggiunti 31 JPEG nuovi tra immagini `published` e `accepted`.
- La cartella `L:\1_Social\1x` contiene ora 38 JPEG per 11,68 MB. Tutti hanno intestazione JPEG valida e hash SHA-256 coerente con `L:\1_Social\awards_download_manifest_2026-08-25.csv`.
- Thunderbird e i messaggi originali non sono stati modificati. Il plugin Gmail non è stato installato perché Davide ha chiesto di usare Thunderbird.

## [2026-08-27] maintenance | Selezione gallerie Islanda, Tenerife e Madeira
- Create le cartelle `selected` sotto `L:\1_Social\SITO DATA\Islanda`, `Tenerife` e `Madeira`. Il percorso corretto delle raccolte è `L:\1_Social\SITO DATA`, non la precedente variante `L:\1\_Social\SITO DATA` rimasta nei vecchi manifesti.
- Copiati 29 JPEG con fregio 1x, classificati visivamente per destinazione: 10 Islanda, 14 Tenerife e 5 Madeira. Il certificato generale 1x e i fregi relativi ad altri soggetti sono rimasti fuori.
- Selezionate inoltre 10 fotografie per ogni destinazione, escludendo i file `awarded`, `published` e `accepted`. La scelta ha considerato qualità tecnica, luce, composizione, varietà dei soggetti e duplicati visivi.
- Il manifesto `L:\1_Social\SITO DATA\_selected_all_collections_manifest.csv` contiene 59 copie con sorgente, destinazione e SHA-256; tutti gli hash risultano validi. Gli originali non sono stati spostati o cancellati.
- Tre file nella raccolta Tenerife (`A7R00156-Edit-2.jpg`, `A7R00420-Edit.jpg`, `A7R00463-Edit.jpg`) non sono leggibili come JPEG e non sono entrati nella selezione; non sono stati modificati.

## [2026-08-28] maintenance / website | Bonifica verificata di Sito_Dave_Opt

- Ricontrollata la copia `L:\Sito_Dave_Opt` senza modificare `L:\Sito_Dave`.
- Ripristinato il claim “Impara a leggere la luce anche dove sembra non esserci”, riordinata la homepage e aggiunto il menu mobile.
- Corretti canonical, hreflang, landmark, sitemap e alcune affermazioni tecniche assolute degli articoli SIGMA.
- I 29 test backend passano. La versione inglese resta incompleta ed è temporaneamente esclusa dall'indicizzazione.
- Commit locali della copia ottimizzata: `56f47e0`, `55524bf` ed `e45be53`; gli ultimi due correggono asset, poster e dati dinamici nelle pagine inglesi.
