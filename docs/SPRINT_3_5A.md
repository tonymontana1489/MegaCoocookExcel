# Sprint 3.5a - Packaging

## Änderungen

- Doppelte Blöcke entfernt
- src-Layout konfiguriert
- pywebview als Abhängigkeit ergänzt
- project.scripts vorerst deaktiviert, bis cli.py existiert

## Danach testen

pip install -e .

python -c "import megacoocookexcel; print(megacoocookexcel.__file__)"
