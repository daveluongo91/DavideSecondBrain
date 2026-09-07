# Bonifica cache dopo la pubblicazione del sito

Il 7 settembre 2026 il nuovo frontend di davideluongo.it e stato pubblicato. Dopo il rilascio alcuni browser continuavano a mostrare la precedente installazione WordPress salvata in cache.

La configurazione Apache ora impedisce la conservazione delle pagine HTML e, per un periodo transitorio, chiede ai browser compatibili di cancellare la cache del dominio. CSS, JavaScript e dati pubblici vengono riconvalidati prima del riuso. Home italiana e inglese, Lapponia, Dardagna e Friuli hanno risposto correttamente; anche lo script PayPal controllato e rimasto disponibile.

La direttiva `Clear-Site-Data` va rimossa dopo il 21 settembre 2026. Le regole `Cache-Control` devono restare. La configurazione precedente e stata salvata sul server prima dell'aggiornamento.
