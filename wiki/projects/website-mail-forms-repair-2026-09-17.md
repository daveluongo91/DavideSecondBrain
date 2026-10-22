---
title: Ripristino moduli email del sito
type: project-log
status: completed
updated: 2026-10-22
summary: Ripristino e collaudo SMTP dei moduli pubblici, comprese le scelte dei destinatari per Minorca e Lapponia.
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

## Verifica dei destinatari dei viaggi

È stato eseguito anche un test mirato sui destinatari selezionabili nelle pagine Minorca e Lapponia, in italiano e inglese. Minorca indirizza correttamente le richieste a Davide, Atelier dei Viaggi o Loris; Lapponia permette di scegliere tra Davide e il tour operator. Gli invii reali sono stati accettati dal server SMTP per tutti i destinatari. Una prova duplicata sulla variante inglese di Minorca è stata fermata correttamente dal limite antispam dopo cinque richieste ravvicinate; lo stesso destinatario era già stato verificato tramite la pagina italiana.

Le quattro pagine pubbliche espongono le opzioni previste. Gli endpoint accettano soltanto le chiavi dei destinatari definite sul server e rispondono con HTTP 400 quando viene fornito un destinatario arbitrario.

## Aggiornamento 22 ottobre 2026

Il modulo Azzorre risultava bloccato prima dell'esecuzione con HTTP 403: la cartella API non era inclusa nell'allowlist Apache. Lo stesso difetto era presente nella nuova pagina Islanda. L'allowlist è stata estesa soltanto ai due percorsi pubblici necessari.

Il vecchio endpoint Azzorre usava inoltre `mail()` e restituiva un messaggio positivo anche quando la consegna falliva. Ora usa il trasporto SMTP condiviso, accetta JSON come gli altri moduli, applica un limite per indirizzo IP e risponde con errore quando il server non accetta il messaggio.

Sono state inviate due richieste reali marcate come test tecnico, una verso il recapito di Davide e una verso il referente del tour operator. Entrambe hanno ricevuto HTTP 200 e conferma di accettazione SMTP. Non erano richieste cliente e non contenevano dati di pagamento.

Nello stesso rilascio sono stati aggiornati title e meta description, canonical e hreflang delle nuove pagine, oltre alla sitemap. Azzorre, Islanda, Minorca in italiano e inglese e The Project risultano ora presenti nella sitemap. Il controllo finale ha confrontato 29 file pubblici con la copia locale tramite SHA-256, senza differenze. La cache Aruba è stata svuotata dopo la pubblicazione.

Commit del sito: `80c18f6a2829f7a257eac32131ee2f2b1a655771`.

## Verifica della pubblicazione

Il controllo successivo del sito pubblico ha confrontato i file principali con `L:\Sito_Dave_Opt`: home italiana e inglese, JavaScript, CSS, Blog, Gear, One-to-One, Lapponia, Minorca, workshop, robots e sitemap corrispondono alla copia operativa. L'unica differenza binaria rilevata era dovuta alle terminazioni di riga trasformate dal server e non modificava il contenuto. Tutte le 32 URL presenti nella sitemap hanno risposto con HTTP 200; i file di configurazione e i dati privati controllati hanno risposto con HTTP 403. Non è stato necessario ripubblicare il sito.

## Verifica del 22 ottobre 2026 — tutti i moduli email

Sono stati eseguiti invii reali marcati `TEST TECNICO` usando `fangoman91@gmail.com` come indirizzo per la risposta. Gli endpoint generale, Conero, Foreste Casentinesi, Azzorre, Islanda, Lapponia e Minorca IT/EN hanno risposto HTTP 200 con accettazione del messaggio. Il vecchio alias Canfaito/Conero ha invece restituito HTTP 500: la causa era il BOM UTF-8 prima di `<?php` in `Canfaito_Conero_2026/api/common.php`, incompatibile con `declare(strict_types=1)`. Il BOM è stato rimosso nella copia locale; il collaudo pubblico definitivo richiede la pubblicazione del file corretto.

Nelle pagine Azzorre e Islanda i pulsanti esterni non nominano più il referente: distinguono soltanto tra informazioni sul viaggio e informazioni fotografiche. Nel form rimane la scelta esplicita tra Davide ed Eleonora. Lapponia era già coerente. Minorca non è stata modificata, come richiesto.

Commit locale del sito: `6de8d59b9bcac9ef533b479b3ec713e7d9524016`.
