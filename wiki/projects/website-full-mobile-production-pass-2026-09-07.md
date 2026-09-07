# Collaudo mobile completo del sito pubblico

Il 7 settembre 2026 sono state controllate 42 pagine pubbliche in cinque larghezze: 320, 375, 390, 430 e 768 pixel, per 210 rendering complessivi. Dopo le correzioni non risultano overflow orizzontali, immagini rotte o risposte HTTP 404/500.

La correzione mobile condivisa ora copre home, Blog e articoli, Gear, One-to-One, Travel, Lapponia e workshop italiani e inglesi. Recuperate dal backup WordPress tredici immagini originali usate negli indici Blog e trasferite nella nuova struttura. Sistemati i percorsi dell'immagine Travel inglese e della foto Dardagna inglese.

Le pagine Friuli e Dardagna usano gli endpoint PHP delle landing standalone gia funzionanti. Le pagine Canfaito e Foreste non interrogano piu contatori inesistenti: mantengono i dati editoriali senza inventare disponibilita. Disabilitata anche la richiesta globale al backend FastAPI non pubblicato. La CSP permette gli embed Instagram e le connessioni tecniche PayPal gia usate dalle pagine.

Pubblicazione eseguita con backup atomici, verifica sintattica JavaScript e purge HiSpeed Aruba. Nessun ordine PayPal, invio email o modifica ai dati delle prenotazioni durante i test.
