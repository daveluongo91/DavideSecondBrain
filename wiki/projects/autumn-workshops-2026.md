---
title: Workshop autunnali 2026
type: project
status: active
updated: 2026-08-19
summary: Due landing autonome per Canfaito & Conero e Foreste Casentinesi, collegate al backend condiviso di SitoDave.
tags:
  - workshops
  - website
  - payments
  - 2026
---

# Workshop autunnali 2026

## Obiettivo

Preparare due pagine autonome, con la stessa struttura tecnica di Friuli e Dardagna, per gli ultimi appuntamenti del calendario 2026:

- Canfaito & Conero, 7-8 novembre 2026;
- Foreste Casentinesi, 28-29 novembre 2026.

## Stato

Le pagine sono pronte in locale nelle cartelle `L:\Canfaito_Conero_Prod` e `L:\Foreste_Casentinesi_Prod`. Una copia di entrambe è versionata in `Sito_Dave/standalone_pages/`.

Il backend contiene i due workshop con 8 posti ciascuno, quota di lavoro €350, caparra €50, saldo €300, cutoff alla mezzanotte locale che precede il primo giorno e marker email distinti. Le fotografie definitive non sono ancora disponibili: la hero e le tre schede fotografiche di ogni pagina usano segnaposto nominati in modo esplicito.

## Risultato osservabile

- Due landing statiche complete di modale di pagamento, PayPal Pay Later, richiesta informazioni, avvisi a 2/1 posti, cookie consent e pagina di ringraziamento.
- Backend condiviso per posti, ordini, cattura pagamento, email e report cutoff.
- 21 test backend superati il 19 agosto 2026.
- Nessuna pubblicazione live dichiarata per le due nuove pagine.

## Prossime azioni

1. Sostituire tutti i file `placeholder-*.svg` con le fotografie approvate.
2. Confermare quota, punti di ritrovo, difficoltà dei percorsi e programma definitivo.
3. Verificare il rendering desktop/mobile e completare un pagamento sandbox con account buyer.
4. Provare email informazioni, conferma pagamento e avvisi disponibilità con SMTP di test.
5. Pubblicare nei percorsi `/Canfaito_Conero_2026/` e `/Foreste_Casentinesi_2026/` soltanto dopo il controllo finale.

## Dipendenze

- Repository `SitoDave` e backend FastAPI.
- Credenziali PayPal sandbox/live e configurazione SMTP, non versionate.
- Fotografie definitive e conferma delle informazioni operative.

## Rischi

- Considerare definitivi quota e programma prima della conferma di Davide e Manuel.
- Confondere un test PayPal sandbox con un pagamento reale.
- Pubblicare database, backup o credenziali insieme ai file statici.

## Decisioni

- Le cartelle esterne `*_Prod` restano utilizzabili come pacchetti autonomi.
- Le copie nel repository servono a tracciare il codice delle due nuove pagine.
- L'opzione aggiuntiva “dal venerdì” resta esclusiva del Friuli.
- Le email informative riportano `[CANFAITO & CONERO 2026]` oppure `[FORESTE CASENTINESI 2026]` per rendere immediata la provenienza.

## Materiali

- Calendario Workshop 2026 condiviso il 19 agosto 2026.
- `L:\Canfaito_Conero_Prod`
- `L:\Foreste_Casentinesi_Prod`
- `Sito_Dave/standalone_pages/`

## Revisione

Rivedere la pagina appena arrivano le fotografie o prima della pubblicazione live, a seconda di quale evento avviene prima.

## Collegamenti

- [Workshop e photo tour](../areas/workshops-and-photo-tours.md)
- [Ricostruzione sito web](website-rebuild.md)
- [Workflow di lancio workshop](../workflows/workshop-launch.md)
