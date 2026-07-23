# MegaCoocookExcel

Mega Coocook Excel helps camps, churches and large group kitchens transform Coocook shopping lists into structured Excel workbooks for easier purchasing and planning.

---

## Features

### Current

- Read Coocook shopping list PDFs
- Detect tables
- Extract shopping items
- Command line interface (CLI)

### Planned

- Excel export
- Automatic categorization
- Dashboard
- Shopping lists by category
- Shopping lists by day
- Multi-PDF support

---

## Installation

```bash
git clone https://github.com/<username>/MegaCoocookExcel.git
cd MegaCoocookExcel

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -e .
```

---

## Usage

```bash
python -m megacoocookexcel examples/cookook.pdf
```

---

## Project Structure

```
src/
 └── megacoocookexcel/
     ├── parser/
     ├── categorizer/
     ├── exporter/
     ├── dashboard/
     └── utils/
```

---

## Roadmap

- [x] Basic project structure
- [x] CLI
- [x] PDF reading
- [ ] Shopping item extraction
- [ ] Excel export
- [ ] Categorization
- [ ] Dashboard
- [ ] GUI

---

## License

MIT License

## Dashboard starten

```bash
python -m megacoocookexcel.dashboard.launcher
```

Anschließend das Dashboard im Browser öffnen

```
http://127.0.0.1:8000
```

---

## Aktueller Stand

Version 0.4.0 verwendet eine REST-Architektur auf Basis von FastAPI.

Die Kommunikation zwischen Browser und Python erfolgt vollständig über HTTP.

Die DashboardBridge sowie die Import- und Repositorylogik bleiben unverändert.