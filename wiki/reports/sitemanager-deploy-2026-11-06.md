---
title: SiteManager - collaudo locale e preparazione VPS
type: report
date: 2026-11-06
tags:
  - website
  - sitemanager
  - backend
  - deployment
---

# SiteManager: collaudo locale e preparazione VPS

SiteManager è stato collaudato con un database temporaneo isolato. Login, workshop, operatività, insights, gestione pagine, ADV e controllo backend hanno caricato correttamente le rispettive API.

Il test nel browser ha individuato un errore che i test API non vedevano: i contatori ADV si aggiornavano, ma la tabella restava in caricamento perché mancava la funzione di escaping HTML. La correzione è stata applicata e verificata nella pagina reale.

Il gate finale locale ha superato 84 test, il controllo JavaScript e il controllo del diff. Il database temporaneo è stato eliminato; quello operativo non è stato modificato.

È stato preparato un pacchetto versionato per VPS Ubuntu con servizio systemd non privilegiato, Nginx HTTP/HTTPS, modello ambiente privo di segreti, bootstrap ripetibile e database persistente in `/srv/sitemanager/shared/database`, separato dalle release. Commit del sito: `f69ccd0`.

Dal commit è stato generato anche l'archivio temporaneo di rilascio `sitemanager-f69ccd0.tar.gz`: 723 voci, 130.689.795 byte, SHA-256 `7E6F7F230994DF4A7B533347513F58C8984C153829973DB0A38454856FF3BAE8`. Non contiene `.env`, database o dati runtime; sotto `private/` include soltanto il file protettivo `.htaccess`.

Il backend non è ancora pubblicato. Restano da verificare accesso SSH con chiave dal PC, DNS del sottodominio, segreti di produzione, certificato TLS e collaudo live. PayPal resta in sandbox.
