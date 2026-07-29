---
title: Antigravity Setup, Permessi e Ripristino Ambiente
type: workflow
status: active
updated: 2026-07-29
summary: Guida completa per il ripristino dell'ambiente Antigravity, permessi concessi, eseguibili di sistema e configurazione su nuove macchine.
tags:
  - setup
  - antigravity
  - permissions
  - workflow
  - environment
---

# Antigravity Setup, Permessi e Ripristino Ambiente

Guida operativa per ripristinare istantaneamente l'ambiente di lavoro dell'agente AI (Antigravity), i permessi concessi, gli eseguibili e la struttura dei repository su qualsiasi nuova macchina Windows.

---

## 1. Percorsi Workspace e Junction Link

- **Repository Sito Web**: `D:\Sito_Dave`
- **Repository Second Brain**: `D:\Davide_SecondBrain`
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
