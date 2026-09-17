---
title: Ripristino moduli email del sito
type: project-log
status: completed
updated: 2026-09-17
tags:
  - website
  - email
  - aruba
  - smtp
---

# Ripristino moduli email del sito

Il 17 settembre 2026 è stato verificato che i moduli del nuovo sito non consegnavano le richieste. La connessione al server SMTP Aruba funzionava, ma l'autenticazione veniva rifiutata. Alcuni endpoint mostravano comunque un falso messaggio di successo perché ricadevano sul mailer PHP locale.

La configurazione SMTP privata è stata aggiornata senza inserirla nel repository. Il fallback ambiguo è stato rimosso: il sito ora conferma l'invio soltanto quando il server SMTP autenticato accetta il messaggio. Sono stati corretti anche il percorso del modulo One-to-One inglese, le copie workshop e le autorizzazioni Apache degli endpoint Minorca in italiano e inglese.

Il collaudo finale ha inviato richieste reali da tutti i 15 moduli o varianti pubbliche. Home, One-to-One IT/EN, Canfaito, Foreste Casentinesi, copie workshop, Dardagna, Friuli, Lapponia IT/EN e Minorca IT/EN hanno ricevuto risposta positiva dal server SMTP. La configurazione privata continua a rispondere con HTTP 403 dall'esterno.

Il percorso sorgente verificato del sito è `L:\Sito_Dave_Opt`. La variante `L:\Sito\_Dave\_Opt` non esiste sul disco.
