# MegaCoocookExcel

## Complete Developer Handbook

Version: 1.0 (AI Working Copy) Generated: 2026-07-21

------------------------------------------------------------------------

# Table of Contents

1.  Vision
2.  Goals
3.  Non-Goals
4.  Architecture
5.  Project Structure
6.  Data Flow
7.  Domain Models
8.  Parser
9.  Importer
10. Repository
11. Configuration
12. Dashboard
13. Dashboard UI Specification
14. Dashboard JavaScript Architecture
15. Category System
16. Coding Standards
17. Error Handling
18. Testing Strategy
19. Release Strategy
20. Roadmap
21. AI Collaboration Rules
22. Design Decisions
23. Future Ideas

------------------------------------------------------------------------

# 1 Vision

MegaCoocookExcel exists to transform Coocook shopping PDFs into
structured, editable shopping data while keeping Coocook itself as the
single source of truth.

The software is designed for recurring use in Christian youth camps
where shopping, planning and logistics repeat every year.

------------------------------------------------------------------------

# 2 Goals

-   Save volunteer time.
-   Remove repetitive manual Excel work.
-   Produce predictable output.
-   Be understandable without software engineering knowledge.
-   Prefer robustness over cleverness.

------------------------------------------------------------------------

# 3 Non-Goals

The project is NOT intended to:

-   replace Coocook
-   become a recipe manager
-   become an ERP system
-   synchronize with online services

------------------------------------------------------------------------

# 4 Overall Architecture

PDF → Parser → ShoppingItem objects → Repository → Dashboard →
Categorized JSON → Excel export (future)

Every layer has exactly one responsibility.

------------------------------------------------------------------------

# 5 Folder Layout

``` text
src/
    megacoocookexcel/
        parser/
        importer/
        dashboard/
        categorizer/
        config/
        utils/
```

Rule: No module should depend on dashboard code except the dashboard
itself.

------------------------------------------------------------------------

# 6 Domain Model

## ShoppingItem

Represents one parsed shopping entry.

Contains:

-   article
-   total amount
-   unit
-   recipe amount
-   recipe unit
-   dish
-   meal
-   date
-   category
-   store

## Article

Persistent master data.

Fields:

-   key
-   name
-   category
-   shop
-   unit
-   comment
-   tags

articles.json is the editable knowledge base.

------------------------------------------------------------------------

# 7 Parser

Pipeline:

Reader → Extractor → Cleaner → Mapper

Responsibilities:

Reader: Loads PDF.

Extractor: Finds tables.

Cleaner: Normalizes data.

Mapper: Creates ShoppingItem objects.

Business rules never belong inside parser classes.

------------------------------------------------------------------------

# 8 Importer

Purpose:

Import Coocook article catalogue.

Extract:

-   article
-   shop
-   tags
-   unit
-   comment

Leave category empty.

------------------------------------------------------------------------

# 9 Repository

Responsible for:

-   loading
-   validation
-   lookup
-   saving

No parsing.

No UI.

------------------------------------------------------------------------

# 10 Dashboard

Purpose:

Assign categories quickly.

Primary user:

Kitchen manager before camp.

Primary requirement:

Speed.

------------------------------------------------------------------------

# 11 Dashboard Requirements

Mandatory features

-   import JSON
-   export JSON
-   autosave
-   undo
-   redo
-   search
-   filter
-   sort
-   progress
-   statistics
-   keyboard navigation
-   multi selection
-   color coded categories

No frameworks.

------------------------------------------------------------------------

# 12 JavaScript Architecture

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

Every class owns one concern only.

------------------------------------------------------------------------

# 13 UI Philosophy

The interface should feel closer to a spreadsheet than a website.

Mouse usage should be optional.

Keyboard shortcuts should make categorization extremely fast.

------------------------------------------------------------------------

# 14 Category Philosophy

Categories describe walking order inside supermarkets.

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

Never optimize for warehouse accounting.

------------------------------------------------------------------------

# 15 Coding Standards

-   English comments
-   descriptive names
-   avoid magic numbers
-   avoid global state
-   keep methods short
-   prefer readability

------------------------------------------------------------------------

# 16 Error Handling

User mistakes should never lose data.

Always:

-   validate input
-   autosave
-   support undo
-   confirm destructive actions

------------------------------------------------------------------------

# 17 Testing

Parser

-   unit tests

Importer

-   PDF regression tests

Dashboard

-   manual workflow tests

Repository

-   JSON validation tests

------------------------------------------------------------------------

# 18 Release Strategy

Suggested versions

0.1 parser

0.2 importer

0.3 repository

0.4 dashboard alpha

0.5 dashboard beta

1.0 production

------------------------------------------------------------------------

# 19 Future Ideas

-   Excel export
-   duplicate detection
-   barcode support
-   dark mode
-   shopping route optimization
-   multilingual UI

Ideas should remain optional until clearly valuable.

------------------------------------------------------------------------

# 20 AI Collaboration Rules

When an AI continues this project:

-   preserve architecture
-   preserve folder structure
-   never replace Coocook
-   prefer complete files over snippets
-   document every important design decision
-   avoid unnecessary dependencies

------------------------------------------------------------------------

# 21 Design Decisions

Important decisions already made:

-   Vanilla HTML/CSS/JavaScript
-   Python backend tools
-   JSON persistence
-   Categories represent supermarket routes
-   Coocook remains authoritative
-   Simplicity beats abstraction

------------------------------------------------------------------------

# 22 Long-Term Vision

The project should eventually allow a camp organizer to:

1.  Export PDF from Coocook.
2.  Import with one command.
3.  Categorize only new articles.
4.  Export shopping lists.
5.  Finish preparation in minutes instead of hours.

This handbook should evolve together with the source code. Any
architectural change should be reflected here so future contributors,
including AI assistants, can understand not only *what* the software
does but *why* it was built that way.
