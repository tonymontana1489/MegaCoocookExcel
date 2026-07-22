# MegaCoocookExcel -- Developer Handbook

Version: Draft 1.0

------------------------------------------------------------------------

# 1. Vision

MegaCoocookExcel converts Coocook shopping PDFs into structured,
editable Excel files for camp logistics.

The project is intentionally **not** a replacement for Coocook. Coocook
remains the source of truth for recipes, servings and shopping
quantities.

MegaCoocookExcel exists to improve everything that happens **after** the
PDF has been exported.

Goals:

-   simplify purchasing
-   reduce manual work
-   improve supermarket workflow
-   preserve manual control

------------------------------------------------------------------------

# 2. Guiding Principles

## Keep it simple

Avoid unnecessary frameworks.

Preferred stack:

-   Python
-   HTML
-   CSS
-   Vanilla JavaScript

## Human first

Every generated result should be understandable by volunteers.

## Maintainability

Readable code is preferred over clever code.

------------------------------------------------------------------------

# 3. Project Structure

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

Each package has exactly one responsibility.

------------------------------------------------------------------------

# 4. Parser

Pipeline:

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

Responsibilities:

-   Reader
    -   load PDF
-   Extractor
    -   locate tables
-   Cleaner
    -   normalize values
-   Mapper
    -   create domain objects

No business logic belongs in the parser.

------------------------------------------------------------------------

# 5. Domain Models

## ShoppingItem

Represents one row from Coocook.

Contains article, units, recipe information, category and store.

## Article

Master data object.

Fields:

-   key
-   name
-   category
-   shop
-   unit
-   comment
-   tags

------------------------------------------------------------------------

# 6. Importer

Purpose:

Import Coocook article catalogue into articles.json.

Importer extracts:

-   article
-   unit
-   shop
-   tags
-   comments

Categories stay empty initially.

------------------------------------------------------------------------

# 7. Repository

articles.json is the editable master database.

The repository:

-   loads
-   validates
-   updates
-   saves

No parsing logic belongs here.

------------------------------------------------------------------------

# 8. Dashboard

Location:

``` text
src/megacoocookexcel/dashboard/
```

Files:

-   article_categorizer.html
-   article_categorizer.css
-   article_categorizer.js

Purpose:

Fast categorization of articles.

------------------------------------------------------------------------

# 9. Dashboard Features

Required:

-   JSON import
-   JSON export
-   autosave
-   undo / redo
-   search
-   sorting
-   statistics
-   progress bar
-   colored categories
-   keyboard shortcuts
-   multi selection
-   uncategorized filter

------------------------------------------------------------------------

# 10. JavaScript Architecture

``` text
Constants
Utilities
StorageManager
HistoryManager
SelectionManager
ImportExportManager
StatisticsManager
Renderer
KeyboardController
ArticleCategorizerApp
```

Each class has one responsibility.

------------------------------------------------------------------------

# 11. Category Philosophy

Categories are **not** warehouse categories.

Categories represent the walking path inside a supermarket.

Example:

Entrance

Fruit

Vegetables

Bread

Dairy

Cheese

Frozen

Drinks

Checkout

This minimizes walking time.

------------------------------------------------------------------------

# 12. Coding Standards

-   English comments
-   descriptive names
-   no magic numbers
-   small methods
-   avoid duplicated code

------------------------------------------------------------------------

# 13. UI Principles

-   keyboard friendly
-   large clickable areas
-   fast rendering
-   minimal dialogs
-   no unnecessary animations

------------------------------------------------------------------------

# 14. Future Ideas

Possible later additions:

-   Excel export
-   barcode support
-   shopping route optimization
-   duplicate detection
-   article search by tags
-   dark mode

These are optional.

------------------------------------------------------------------------

# 15. AI Collaboration Rules

When continuing this project:

-   Never return snippets if a complete replacement file is requested.
-   Preserve architecture.
-   Keep Coocook as source of truth.
-   Prefer simple solutions.
-   Avoid introducing frameworks without strong justification.
-   Keep documentation synchronized with implementation.

------------------------------------------------------------------------

# 16. Current Status

Completed

-   Parser
-   Importer
-   Repository
-   Domain models

Current milestone

Dashboard implementation.

Next target

Complete article categorizer UI and integrate it into the repository.
