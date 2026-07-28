# Caricamento su GitHub

## Metodo consigliato — Git da terminale

1. Estrai lo ZIP.
2. Apri il terminale nella cartella `davide-second-brain`.
3. Esegui:

```bash
git init
git add .
git commit -m "Initial second brain"
git branch -M main
git remote add origin URL_DEL_REPOSITORY
git push -u origin main
```

Prima crea su GitHub un repository vuoto, senza README, `.gitignore` o licenza, perché questi file sono già inclusi.

## Metodo GitHub Desktop

1. Estrai lo ZIP.
2. In GitHub Desktop scegli **File → Add local repository**.
3. Seleziona la cartella estratta.
4. Scegli **Create a repository** quando richiesto.
5. Esegui il primo commit e poi **Publish repository**.

## Metodo browser

GitHub non trasforma automaticamente uno ZIP nel contenuto di un repository. Estrai prima lo ZIP, crea un repository vuoto e trascina nella pagina di upload **il contenuto della cartella estratta**, inclusi i file nascosti `.github`, `.obsidian`, `.gitignore` e `.gitattributes`.

## Repository pubblico o privato

La base è stata ripulita dai dati sensibili, ma per un second brain personale è comunque consigliato iniziare con un repository **Private**.
