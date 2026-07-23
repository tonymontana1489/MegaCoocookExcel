# Sprint 4R – REST Migration

## Ziel

Der bisherige Desktop-Ansatz mit PyWebView funktionierte in GitHub Codespaces nicht zuverlässig. Ziel dieses Sprints war daher ausschließlich der Austausch der Kommunikationsschicht.

Die eigentliche Anwendungslogik (Importer, Repository und DashboardBridge) sollte unverändert bleiben.

---

# Architektur

Vorher

Dashboard

↓

PyWebView

↓

DashboardBridge

↓

ArticleImporter

↓

ArticleRepository

Nachher

Dashboard

↓

REST (fetch)

↓

FastAPI

↓

DashboardBridge

↓

ArticleImporter

↓

ArticleRepository

---

# Umgesetzte Änderungen

## Dashboard

- Kommunikation vollständig auf `fetch()` umgestellt
- PDF wird als `multipart/form-data` hochgeladen
- keine Abhängigkeit mehr von PyWebView

---

## Backend

- FastAPI integriert
- Uvicorn als Webserver
- Dashboard wird über `StaticFiles` ausgeliefert
- REST-Endpunkt `/api/import`
- REST-Endpunkt `/api/articles`

---

## DashboardBridge

Die DashboardBridge blieb bewusst unverändert.

Sie bildet weiterhin die Schnittstelle zwischen Dashboard und Business-Logik.

Dashboard

↓

DashboardBridge

↓

ArticleImporter

↓

ArticleRepository

---

## Projektstruktur

Keine Änderungen an

- Importer
- Repository
- Models
- Config

Die REST-Migration betrifft ausschließlich die Kommunikation zwischen Browser und Python.

---

# Testergebnis

✔ Dashboard startet

✔ Browser öffnet automatisch

✔ REST-Kommunikation funktioniert

✔ PDF-Upload funktioniert

✔ DashboardBridge wird aufgerufen

✔ ArticleImporter wird aufgerufen

✔ Repository wird erreicht

Der Import liefert aktuell noch keine Artikel.

Die weitere Entwicklung erfolgt deshalb im nächsten Sprint direkt im Importer.

---

# Nächster Sprint

Sprint 5

Ziel:

- Analyse des ArticleImporters
- Artikel korrekt extrahieren
- Speicherung nach articles.json
- Artikelverwaltung im Dashboard