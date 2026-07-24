# Sprint 5 -- Neuer Article Importer für Coocook-Einkaufslisten

## Ausgangslage

Nach Abschluss der REST-Migration (Sprint 4R) funktioniert der komplette
Importablauf:

``` text
Dashboard
    ↓
POST /api/import
    ↓
DashboardBridge
    ↓
ArticleImporter
    ↓
ArticleRepository
    ↓
articles.json
```

Der Upload funktioniert fehlerfrei.

Der Import liefert jedoch:

``` text
0 Artikel importiert
```

## Ursache

Der aktuelle `ArticleImporter` wurde ursprünglich für die
Coocook-Artikelstammdaten-PDF entwickelt.

Er erwartet Tabellen mit den Spalten:

-   Name
-   Comment
-   Shop Section
-   Suggested Unit
-   Tags

Die aktuelle Einkaufs-PDF besitzt stattdessen:

-   Amount
-   Article
-   Amounts
-   Dishes
-   Servings
-   Meals
-   Dates

Dadurch erkennt der Importer keine gültigen Datensätze.

## Analyse der Einkaufs-PDF

Die hochgeladene PDF ist eine Einkaufsliste.

### Shop-Struktur

Die Shopüberschrift gilt immer für alle folgenden Artikel bis zur
nächsten Überschrift.

Beispiel:

-   Aldi/Lidl
-   C&C

Der Shop steht nicht in jeder Tabellenzeile.

### Mehrzeilige Artikelnamen

Beispiele:

-   Basilikum (Topf)

-   Gewürzgurken (Abtropfgewicht 360g)

-   Knoblauchzehe (bitte in Knollen umrechnen)

Diese müssen zu einem einzigen Artikelnamen zusammengeführt werden.

Beispiel:

-   Gewürzgurken (Abtropfgewicht 360g)

## Was importiert werden soll

Nur:

-   Artikelname
-   Shop

Ignoriert werden:

-   Mengen
-   Portionen
-   Gerichte
-   Datumsangaben
-   Rezeptinformationen

## Ziel von Sprint 5

Die Datei

`src/megacoocookexcel/importer/article_importer.py`

wird vollständig ersetzt.

Die öffentliche Schnittstelle bleibt erhalten:

``` python
ArticleImporter().import_pdf(...)
```

Alle übrigen Komponenten bleiben unverändert.

## Neuer Ablauf

``` text
PDF öffnen
    ↓
Seiten durchlaufen
    ↓
aktuellen Shop erkennen
    ↓
Tabellen lesen
    ↓
Artikelnamen extrahieren
    ↓
mehrzeilige Namen zusammenführen
    ↓
Shop zuweisen
    ↓
Duplikate entfernen
    ↓
alphabetisch sortieren
    ↓
list[Article] zurückgeben
```

## Beispiel

``` python
Article(
    name="Gewürzgurken (Abtropfgewicht 360g)",
    shop="Aldi/Lidl"
)
```

``` python
Article(
    name="Bananen",
    shop="C&C"
)
```

## Entfernte Altlogik

Die bisherige Verarbeitung von

-   Comment
-   Suggested Unit
-   Tags
-   Shop Section
-   Header "name"

entfällt vollständig.

## Erwartetes Ergebnis

Nach Sprint 5 soll der Import:

-   alle Artikel aus der Coocook-Einkaufsliste erkennen,
-   den korrekten Shop zuweisen,
-   mehrzeilige Namen zusammenführen,
-   doppelte Artikel entfernen,
-   alphabetisch sortieren,
-   eine `list[Article]` zurückgeben,
-   die bestehende REST-Schnittstelle unverändert weiterverwenden.

Damit kann die Einkaufsliste direkt als Quelle für die Artikeldaten
verwendet werden.
