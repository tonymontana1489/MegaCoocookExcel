# Changelog

## Version 0.4.0

### Added

- FastAPI Backend
- REST API
- Dashboard Hosting über StaticFiles
- PDF Upload per multipart/form-data

### Changed

- Kommunikation vollständig auf REST umgestellt
- Browser verwendet fetch()
- Launcher startet Uvicorn

### Removed

- PyWebView
- GTK/Qt-Abhängigkeiten

### Status

Die Infrastruktur der Anwendung wurde erfolgreich auf eine browserbasierte REST-Architektur migriert.

Der nächste Entwicklungsschritt konzentriert sich ausschließlich auf den Importer.