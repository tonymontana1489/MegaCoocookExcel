# Sprint 3.4 – Repository Integration

## Ziel

Das Dashboard kennt ausschließlich die DashboardAPI.

Dashboard
    ↓
DashboardAPI
    ↓
DashboardBridge
    ↓
ArticleRepository

Der PDF-Import ist nur noch eine Aktion, deren Ergebnis anschließend aus dem
Repository geladen wird.

## Nächster Sprint

- ArticleImporter wirklich aufrufen
- ArticleRepository anbinden
- Artikel automatisch im Dashboard anzeigen
