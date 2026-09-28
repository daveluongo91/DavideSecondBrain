---
title: Workshop autunnali 2026
type: project
status: active
updated: 2026-09-28
summary: Landing Conero e Foreste Casentinesi online con fotografie reali, API locali, PayPal live e moduli email collaudati.
tags:
  - workshops
  - website
  - payments
  - 2026
---

# Workshop autunnali 2026

## Obiettivo

Pubblicare due pagine autonome, con la stessa struttura tecnica di Friuli e Dardagna, per gli ultimi appuntamenti del calendario 2026:

- Riviera del Conero, 7-8 novembre 2026;
- Foreste Casentinesi, 28-29 novembre 2026.

## Stato

Le landing canoniche sono online su `/Conero_2026/` e `/Foreste_Casentinesi_2026/`, con versioni inglesi, fotografie reali e card attive nelle due home. Le copie sotto `workshops_2026/` restano fuori dall'indice e puntano alle canoniche.

Ogni pagina usa la propria API per posti, richieste email e PayPal. Il 28 settembre 2026 i loader PayPal live, la disponibilità e la validazione server sono risultati operativi. Due email reali di collaudo, una per pagina, sono state accettate dal server e indirizzate a `info@davideluongo.it`. Il test non ha creato né addebitato pagamenti.

SEO aggiornata con title e description specifici, canonical, hreflang IT/EN, Open Graph, Twitter Card, dati strutturati `EducationEvent` e sitemap. Cache Aruba HiSpeed svuotata dopo il rilascio.

## Risultato osservabile

- Due landing statiche complete di modale di pagamento, PayPal Pay Later, richiesta informazioni, avvisi a 2/1 posti, cookie consent e pagina di ringraziamento.
- Backend condiviso per posti, ordini, cattura pagamento, email e report cutoff.
- API live raggiungibili e configurazioni private protette.
- Commit sito locale `531e78b`; release GitHub `0a98c8d`.

## Prossime azioni

1. Verificare la prima prenotazione reale ricevuta da ciascuna landing.
2. Controllare periodicamente posti disponibili, consegna email e log PayPal.

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
- Le email informative riportano `[CONERO 2026]` oppure `[FORESTE CASENTINESI 2026]` per rendere immediata la provenienza.

## Materiali

- Calendario Workshop 2026 condiviso il 19 agosto 2026.
- `L:\Sito_Dave_Opt\Conero_2026`
- `L:\Sito_Dave_Opt\Foreste_Casentinesi_2026`
- `Sito_Dave/standalone_pages/`

## Revisione

Rivedere la pagina dopo la prima prenotazione reale o in caso di variazioni operative.

## Collegamenti

- [Workshop e photo tour](../areas/workshops-and-photo-tours.md)
- [Ricostruzione sito web](website-rebuild.md)
- [Workflow di lancio workshop](../workflows/workshop-launch.md)
