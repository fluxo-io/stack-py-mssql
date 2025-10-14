# 🐍 stack-py-mssql

Ein leichtgewichtiges Docker-Setup für Python-Entwicklung mit **pandas** und **MSSQL-Anbindung**.  
Ideal für ETL-, Analyse- und Datenverarbeitungsprojekte, bei denen Python mit einer bestehenden Microsoft SQL Server-Instanz kommunizieren soll.

---

## 🚀 Features

- Docker-basiertes Python 3.11 Environment  
- Zugriff auf externe MSSQL-Server (optional lokaler MSSQL-Container)  
- Unterstützung für `pandas`, `pyodbc`, `SQLAlchemy` und `openpyxl`  
- Persistentes Volume für Dateien (`./data`)  
- Optionaler Shell-Service für direkte Container-Interaktion

---

## 🗂 Projektstruktur

```
stack-py-mssql/
│
├── app.py                # Beispielskript
├── docker-compose.yml    # Docker Compose Definition mit Python-Container
├── Dockerfile            # Image-Build mit ODBC-Treiber und Python-Paketen
├── requirements.txt      # Python-Abhängigkeiten
├── .env                  # Umgebungsvariablen für DB-Verbindung
└── data/                 # Ordner für Dateien (wird synchronisiert)
    └── template.xlsx     
```

---

## ⚙️ Konfiguration

Alle Datenbankparameter werden über die Datei `.env` gesteuert:

```bash
MSSQL_HOST=your-sql-host
MSSQL_PORT=1433
MSSQL_DB=master
MSSQL_USER=sa
MSSQL_PASSWORD=YourStrong!Passw0rd
```

> 💡 Hinweis: Das Projekt erwartet eine bestehende MSSQL-Instanz

---

## 🧰 Nutzung

### 1️⃣ Build und Start im Vordergrund
```bash
docker compose up --build
```

### 2️⃣ Start im Hintergrund (detached)
```bash
docker compose up -d
```

### 3️⃣ direkt in das Python-Image wechseln
```bash
docker compose run shell
```
Dadurch öffnet sich eine Bash-Shell mit Zugriff auf alle Python-Pakete und dein synchronisiertes `./data`-Verzeichnis.

---

## 🧹 Container stoppen und bereinigen

```bash
docker compose down
```

---

## 🧩 Erweiterungen

- Lokale MSSQL-Instanz (z. B. für Tests) kann bei Bedarf wieder aktiviert werden:
  ```yaml
  # In docker-compose.yml
  # mssql:
  #   image: mcr.microsoft.com/mssql/server:2022-latest
  #   environment:
  #     - ACCEPT_EULA=Y
  #     - MSSQL_SA_PASSWORD=${MSSQL_SA_PASSWORD}
  #     - MSSQL_PID=Developer
  #   ports:
  #     - "1433:1433"
  ```
- Weitere Python-Pakete kannst du in `requirements.txt` ergänzen.
