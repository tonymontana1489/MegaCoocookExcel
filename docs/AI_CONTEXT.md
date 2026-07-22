# MegaCoocookExcel AI Context

## Purpose

MegaCoocookExcel converts Coocook PDF shopping lists into structured
Excel shopping lists for camp purchasing.

## User Preferences

-   Always provide complete replacement files, never snippets.
-   English comments/docstrings in source code.
-   Keep architecture simple and maintainable.
-   Coocook remains the source of truth whenever possible.
-   Categories optimize walking through supermarkets.

## Current Status

Completed: - Parser pipeline - PDF importer - Article repository -
Article model - ShoppingItem model

Current work: - Dashboard (`src/megacoocookexcel/dashboard/`)

Target features: - JSON import/export - Autosave (localStorage) -
Undo/Redo - Search - Filter uncategorized - Keyboard shortcuts -
Multi-selection - Progress bar - Category statistics - Sorting - Colored
categories

## Dashboard Files

-   article_categorizer.html
-   article_categorizer.css
-   article_categorizer.js
