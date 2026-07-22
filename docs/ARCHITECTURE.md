# MegaCoocookExcel Architecture

## Project Structure

``` text
src/
    megacoocookexcel/
        parser/
        importer/
        categorizer/
        dashboard/
        config/
        utils/
```

## Parser Pipeline

``` text
PDF
 ↓
PDFReader
 ↓
PdfTableExtractor
 ↓
TableCleaner
 ↓
ShoppingItemMapper
 ↓
ShoppingItem
```

## Dashboard Architecture

``` text
article_categorizer.js
├── Constants
├── Utility Functions
├── StorageManager
├── HistoryManager
├── SelectionManager
├── ImportExportManager
├── StatisticsManager
├── Renderer
├── KeyboardController
└── ArticleCategorizerApp
```

## Design Principles

-   Separation of concerns.
-   No framework.
-   Plain HTML/CSS/JavaScript.
-   Readability over cleverness.
-   One responsibility per class.
-   JSON is the persistence format.
-   localStorage only as safety backup.
