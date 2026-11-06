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

Il 6 novembre è stata verificata la chiave SSH dal PC e installata sul VPS Aruba la release `3ac73c8`. Il servizio FastAPI gira come utente non privilegiato `sitemanager`, parte con systemd, ascolta solo su `127.0.0.1:8000` e viene esposto da Nginx. Il database persistente si trova fuori dalla release. Health check di produzione e routing Nginx con Host header sono riusciti.

La password iniziale è stata generata sul VPS, usata una volta per creare l'amministratore e rimossa dall'ambiente del servizio. La copia temporanea è leggibile solo da `root` e va eliminata dopo il primo cambio password. Nessun segreto è stato scritto nel repository o nel Second Brain.

Il sottodominio `sitemanager.davideluongo.it` non ha ancora un record DNS. Il backend risponde già sull'IP del VPS con Host header corretto, ma non è ancora dichiarabile pubblico: mancano record A, certificato TLS, verifica HTTPS e collaudo del login dall'esterno. PayPal resta in sandbox; SMTP e WhatsApp non sono configurati.

Nel pannello Aruba è ora presente il record A `sitemanager` verso `195.231.64.27`, con TTL di un'ora. I controlli immediati sui name server autoritativi Aruba e sul resolver pubblico `1.1.1.1` restituiscono ancora `NXDOMAIN`: la propagazione è in attesa. Certbot non è stato eseguito finché il record non risulta pubblicamente risolvibile.

## Audit sicurezza del VPS

Il controllo in sola lettura conferma UFW attivo con policy predefinita `deny`, porte pubbliche limitate a SSH e Nginx, FastAPI in ascolto soltanto su `127.0.0.1:8000`, Fail2ban attivo, aggiornamenti automatici attivi e servizio SiteManager non privilegiato con protezioni systemd. Ambiente, database e credenziali temporanee hanno permessi restrittivi.

L'hardening SSH è stato completato con procedura anti-lockout. È stato creato `sitemgradmin`, abilitato a `sudo` con password separata e accesso SSH tramite la chiave già verificata. Le nuove sessioni come `root` sono rifiutate; autenticazione password e tastiera interattiva sono disabilitate; sono ammessi soltanto chiave pubblica e utente `sitemgradmin`. I parametri effettivi sono `MaxAuthTries 3` e `LoginGraceTime 30`.

È stato inoltre eliminato un vecchio listener SSH, rimasto attivo dal 30 ottobre con la configurazione precedente. Il collaudo conclusivo conferma: accesso a chiave riuscito, password rifiutata e root rifiutato. Fail2ban usa ora quattro tentativi in dieci minuti, ban iniziale di un'ora e durata incrementale fino a una settimana. Nginx non espone più la versione. Gli aggiornamenti disponibili non soggetti a phasing sono stati installati; il sistema non ha richiesto un riavvio.

Le credenziali iniziali di `sudo` e SiteManager sono state trasferite senza mostrarne il contenuto nella cartella `.ssh` del PC, dove i permessi Windows le limitano all'utente, a `SYSTEM` e agli amministratori locali. Le copie originali e temporanee sono state eliminate dal VPS e la loro assenza è stata verificata. Dopo la chiusura della sessione root, un nuovo accesso come `sitemgradmin` ha confermato attivi SSH, Fail2ban, Nginx e SiteManager, con health check `production` riuscito.

Sul sito pubblico principale risultano HSTS, CSP e protezione anti-frame; `wp-login.php` e `xmlrpc.php` rispondono 403 e `wp-json/` risponde 404. Questo controllo esterno non equivale a un penetration test, ma non ha mostrato le consuete superfici WordPress esposte.
