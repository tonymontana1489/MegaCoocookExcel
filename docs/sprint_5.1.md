# Sprint 5.1 – Artikelrepository aufräumen

## Ziel

Der Speicherort der Artikeldatenbank soll zentral verwaltet werden.

Bisher mussten verschiedene Komponenten den Pfad zu `articles.json` kennen. Dadurch war die Ablage unnötig an mehreren Stellen im Projekt verteilt und Änderungen am Speicherort hätten mehrere Dateien betroffen.

---

## Änderungen

### Neuer Speicherort

Die Artikeldatenbank wurde von

```text
config/articles.json
```

nach

```text
data/articles.json
```

verschoben.

`config` enthält ausschließlich Konfigurationen.

`data` enthält persistente Projektdaten.

---

### ArticleRepository

Das `ArticleRepository` verwaltet den Speicherort nun selbst.

Die Methoden

```python
load()
save()
```

benötigen keinen Dateipfad mehr.

Der Dateizugriff ist vollständig innerhalb des Repositories gekapselt.

---

### Dashboard

Das Dashboard greift ausschließlich über das Repository auf die Artikeldaten zu.

Es kennt den Speicherort der JSON-Datei nicht mehr.

---

### CLI

Auch die Kommandozeile verwendet nur noch das Repository.

Es existieren keine direkten Dateizugriffe mehr außerhalb des `ArticleRepository`.

---

## Architektur

Vorher

```
Dashboard
      \
CLI ----> config/articles.json
      /
Importer
```

Nachher

```
Dashboard
        \
CLI -----> ArticleRepository -----> data/articles.json
        /
Importer
```

Dadurch besitzt nur noch eine einzige Klasse Wissen über den Speicherort der Artikeldatenbank.

---

## Vorteile

- klare Trennung zwischen Konfiguration und Nutzdaten
- zentraler Dateizugriff
- einfachere Wartung
- zukünftiger Wechsel auf SQLite oder eine andere Datenquelle betrifft nur das Repository
- sauberere Architektur

---

## Ergebnis

Sprint 5.1 wurde erfolgreich abgeschlossen.

Der Artikelimport arbeitet unverändert weiter.

Die Artikeldatenbank wird nun zentral unter

```text
data/articles.json
```

verwaltet.