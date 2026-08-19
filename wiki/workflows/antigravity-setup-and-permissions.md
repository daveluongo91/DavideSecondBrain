---
title: Antigravity Setup, Permessi e Ripristino Ambiente
type: workflow
status: reference
updated: 2026-08-19
summary: Registro storico della configurazione Antigravity; percorsi e permessi vanno verificati sulla macchina corrente.
tags:
  - setup
  - antigravity
  - permissions
  - workflow
  - environment
---

# Antigravity Setup, Permessi e Ripristino Ambiente

Questa pagina conserva la configurazione Antigravity usata in precedenza. Non va applicata alla cieca su una nuova macchina: percorsi, eseguibili e permessi dipendono dall'ambiente corrente. Al 19 agosto 2026 i repository attivi sono `L:\Sito_Dave` e `L:\Davide_SecondBrain`; Python e Git risultano disponibili dal `PATH`.

---

## 1. Percorsi Workspace e Junction Link

- **Repository Sito Web corrente**: `L:\Sito_Dave`
- **Repository Second Brain corrente**: `L:\Davide_SecondBrain`
- I successivi riferimenti a `D:` e al vecchio profilo Windows sono conservati come configurazione storica e devono essere adattati.
- **Directory Junction per Retrocompatibilità** (da eseguire in PowerShell/CMD come Amministratore se il percorso primario era su `C:`):

```powershell
cmd.exe /c mklink /J "C:\Users\luongo\Desktop\2nd\Sito_Dave" "D:\Sito_Dave"
```

---

## 2. Registro dei Permessi Concessi ad Antigravity

Per evitare di dover richiedere nuovamente l'approvazione manuale su ogni singola operazione di file o comando, ecco l'elenco dei permessi autorizzati:

### Permessi di File System (Read / Write)
- `read_file(D:\)` — Concesso (Lettura completa disco D:\)
- `write_file(D:\)` — Concesso (Scrittura ed editing completo disco D:\)
- `read_file(C:\Users\luongo\Desktop\2nd)` — Concesso

### Permessi di Esecuzione Comandi (Allowed Commands)
- `command(git status)`
- `command(Get-Command)`
- `command(Get-ChildItem)`
- `command(&)`
- `command(New-Item)`
- `command(Copy-Item)`
- `command(Test-Path)`
- `command(cmd.exe)`
- `command(py)`
- `command(npm install)`
- `command(Invoke-RestMethod)`
- `read_url(ibuxus.it)`

---

## 3. Eseguibili di Sistema & Periferiche

Se i comandi standard `python` o `git` non sono presenti nel PATH globale di Windows su una nuova macchina, utilizzare i seguenti percorsi assoluti verificati:

- **Python Binary**: `C:\Program Files\Siril\python\python.exe`
  - *Librerie necessarie per il backend*: `Pillow` (versione 12.3.0 o superiore per gestione profilo sRGB e generazione WebP).
  - *Comando installazione*: `& "C:\Program Files\Siril\python\python.exe" -m pip install Pillow`
- **Git Binary**: `C:\Users\luongo\AppData\Local\GitHubDesktop\app-3.6.3\resources\app\git\cmd\git.exe`

---

## 4. Repository GitHub & Remote URLs

- **Sito Web (`SitoDave`)**:
  - URL Remote: `https://github.com/daveluongo91/SitoDave.git`
  - Push branch: `main`
- **Second Brain (`DavideSecondBrain`)**:
  - URL Remote: `https://github.com/daveluongo91/DavideSecondBrain.git`
  - Push branch: `main`

---

## 5. Comandi di Gestione & Script di Sistema

### Avvio Server Backend & Admin CMS (`Sito_Dave`)
```powershell
& "C:\Program Files\Siril\python\python.exe" server.py
```
- **Sito Live**: `http://localhost:3000/`
- **Admin Dashboard**: `http://localhost:3000/admin`
- **REST API Content**: `http://localhost:3000/api/content`
- **REST API Upload (sRGB & WebP)**: `http://localhost:3000/api/upload`

### Manutenzione Wiki (`Davide_SecondBrain`)
```powershell
# Rigenerazione Indice Wiki
& "C:\Program Files\Siril\python\python.exe" scripts/rebuild_index.py

# Lint & Controllo Collegamenti
& "C:\Program Files\Siril\python\python.exe" scripts/lint_wiki.py
```

---

## 6. Regole di Elaborazione Immagini sRGB
Nelle elaborazioni fotografiche notturne e paesaggistiche:
1. Mantenere o convertire sempre esplicitamente le immagini allo spazio colore **sRGB**.
2. Preservare i metadati ICC dell'immagine caricata.
3. Generare in parallelo la versione **WebP sRGB** ad alta efficienza e la versione **JPEG sRGB** nella cartella `assets/upload/`.
