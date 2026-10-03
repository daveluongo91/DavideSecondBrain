---
title: Recensioni Google del sito e aggiornamento mensile
type: project
status: active
updated: 2026-10-03
created: 2026-09-25
owner: Davide
review_after: 2026-11-01
summary: Link pubblico corretto, recensioni centralizzate in JSON e controllo mensile delle nuove recensioni Google.
tags:
  - sito
  - recensioni-google
  - aruba
  - automazione
---

# Recensioni Google del sito e aggiornamento mensile

Il link del blocco recensioni puntava a una destinazione non più valida. Il 25 settembre 2026 è stato sostituito, nelle home italiana e inglese, con `https://share.google/BAb4AYWCa66b4ixCN`, verificato sul profilo pubblico di Davide Luongo.

Le sei recensioni mostrate in home ora sono raccolte in `data/reviews.json`. `main.js` carica il file, sceglie il testo italiano o inglese e ricostruisce il carosello. Se il file non risponde o contiene dati non validi, restano visibili le recensioni già presenti nell'HTML: un errore dell'aggiornamento non lascia vuota la sezione.

È attivo un controllo mensile, il primo giorno del mese alle 09:00. Il controllo confronta il profilo Google pubblico con il file del sito e aggiorna al massimo sei recensioni recenti, da cinque stelle e con testo utile. Non deve inventare, unire o completare recensioni. La versione italiana conserva il testo pubblico; quella inglese è una traduzione fedele. Se non ci sono cambiamenti verificabili, non pubblica nulla.

## Pubblicazione del 25 settembre

- Commit sorgente locale: `f867a25`.
- Repository pubblico `SitoDave-Release`: commit `69dcd00` sul branch `main`.
- Pubblicati su Aruba `.htaccess`, `index.html`, `en/index.html`, `main.js` e `data/reviews.json`, mantenendo una copia di backup dei file sostituiti.
- Svuotata HiSpeed Cache dal pannello Aruba.
- Verificate le home italiana e inglese: il link Google è corretto e le due lingue mostrano il testo previsto.
- Verificato `data/reviews.json` in produzione: HTTP 200, sei recensioni, cache con riconvalida e nessun header transitorio `Clear-Site-Data`.

## Prossime azioni

- Controllare il primo aggiornamento automatico del 1 ottobre 2026.
- Se Google cambia struttura o limita l'accesso alle recensioni, fermare l'aggiornamento senza alterare il file pubblicato e registrare l'errore.
- Non pubblicare nomi, testi o valutazioni che non siano visibili sulla scheda Google pubblica.

## Controllo del 3 ottobre

La scheda pubblica mostra 18 recensioni e una valutazione media di 5,0. Sono state trovate nuove recensioni a cinque stelle con riferimenti concreti a workshop, uscite fotografiche, didattica e organizzazione. La selezione del sito è stata aggiornata dando priorità alle più recenti: Luca Martinelli, Eleonora Fioravante, Cristina Monzoni, Mirco Galloni, Alessandro Peruzzi e Giancarlo Ferrari.

Nel JSON resta il testo italiano esattamente come pubblicato su Google, senza correzioni o unioni. Per la home inglese è stata aggiunta una traduzione fedele. Il caricamento dinamico e il fallback HTML non sono stati modificati.

## Collegamenti

- [Ricostruzione sito web](website-rebuild.md)
- [Bonifica cache dopo la pubblicazione](website-production-cache-fix-2026-09-07.md)
