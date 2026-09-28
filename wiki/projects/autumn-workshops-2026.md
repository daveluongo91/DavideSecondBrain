---
title: Workshop autunnali 2026
type: project
status: active
updated: 2026-09-28
summary: Due landing autonome per Riviera del Conero 2026 e Foreste Casentinesi 2026 con fotografie reali a proporzioni native, collegate al backend condiviso di SitoDave.
tags:
  - workshops
  - website
  - payments
  - 2026
---

# Workshop autunnali 2026

## Obiettivo

Completare e rifinire le due landing page autonome per gli appuntamenti autunnali 2026, collegate all'infrastruttura backend e dotate di materiale fotografico reale ad alto impatto:

- **Riviera del Conero 2026** (7–8 novembre 2026): focus esclusivo sulla costa del Conero (La Vela, Le Due Sorelle con sentiero panoramico di 45 min a piedi, La Seggiola del Papa al Passetto).
- **Foreste Casentinesi 2026** (28–29 novembre 2026): boschi maturi, sentiero nella nebbia, foliage, cascate e dettagli del sottobosco primordiale.

## Stato Attuale (28 Settembre 2026)

### Pubblicazione e collaudo live

- Le landing canoniche sono online su `/Conero_2026/` e `/Foreste_Casentinesi_2026/`; le copie sotto `workshops_2026/` restano fuori dall'indice e puntano alle canoniche.
- Le card IT e EN della home non sono più `coming soon`: aprono le pagine corrette e mostrano le fotografie reali.
- API locali separate per ciascun workshop. Corretto il routing di disponibilità posti e predisposte configurazioni private protette per SMTP e PayPal.
- Loader PayPal verificati sull'ambiente live, entrambi collegati all'SDK di produzione. Testata la validazione degli ordini con richieste non valide, senza creare o addebitare pagamenti.
- Inviate due email reali di collaudo a `info@davideluongo.it`, una dal modulo Conero e una dal modulo Foreste. Entrambe accettate dal server con HTTP 200 e risposta `status: ok`.
- SEO aggiornata: title e description specifici, canonical, hreflang IT/EN, Open Graph, Twitter Card, dati strutturati `EducationEvent` e sitemap.
- Cache Aruba HiSpeed svuotata dopo il rilascio. Commit locale sito: `531e78b`; release GitHub: `0a98c8d`.

- **Riviera del Conero 2026**:
  - Landing autonoma attiva in `Conero_2026/` e `workshops_2026/conero-2026.html` (e versione EN).
  - Integrate 3 fotografie reali fornite da Davide nel loro aspect ratio nativo:
    - *La Vela* (682x1024, Verticale 2:3)
    - *Le Due Sorelle* (1024x682, Orizzontale 3:2)
    - *La Seggiola del Papa* (1024x682, Orizzontale 3:2)
  - Aggiunta sezione galleria "Scatti sul Campo" con visualizzazione non tagliata al 100%.
  - Specificata nota logistica sul cammino di 45 minuti per i faraglioni delle Due Sorelle.

- **Foreste Casentinesi 2026**:
  - Landing autonoma attiva in `Foreste_Casentinesi_2026/` e `workshops_2026/foreste-casentinesi-2026.html` (e versione EN).
  - Integrate 5 fotografie reali a proporzioni native in WebP/JPG:
    - *Sentiero nella nebbia tra i faggi* (1024x682, Orizzontale 3:2) - Hero & Boschi
    - *Cascata nel bosco e foliage* (1024x682, Orizzontale 3:2) - Corsi d'acqua
    - *Tronco monumentale con muschio* (682x1024, Verticale 2:3) - Sottobosco
    - *Cascata dell'Acquacheta a balze* (682x1024, Verticale 2:3) - Salti d'acqua
    - *Faggeta mistica con bruma azzurra* (1024x682, Orizzontale 3:2) - Atmosfera
  - Creata galleria visiva completa a 5 fotografie responsive.

- **Home Page & Backend**:
  - Caroselli in `index.html` e `en/index.html` completamente attivi con collegamenti diretti e foto reali.
  - Test di regressione backend: **58/58 test superati**.

## Prossimo risultato osservabile

Ricevere e verificare una prenotazione reale per ciascuna landing. Il collaudo non ha effettuato transazioni economiche.

## Collegamenti

- [Workshop e photo tour](../areas/workshops-and-photo-tours.md)
- [Ricostruzione sito web](website-rebuild.md)
- [Minorca Photo Experience 2027](minorca-2027.md)
