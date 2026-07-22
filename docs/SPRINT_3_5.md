# Sprint 3.5 – PyWebView Integration

## Installation

```bash
pip install -r requirements-dashboard.txt
```

## Start

```bash
python -m megacoocookexcel.dashboard.launcher
```

## Test

Öffnet sich das Dashboard in einem Desktop-Fenster?

Danach kann im Browser-Developer-Tool getestet werden:

```javascript
await window.pywebview.api.ping()
```

Erwartete Antwort:

```json
{
  "success": true,
  "message": "Python API erreichbar."
}
```

Wenn das funktioniert, ist JavaScript ↔ Python verbunden.
