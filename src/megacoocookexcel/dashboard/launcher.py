"""
Sprint 3.6 - Smarter Launcher

- Mit GUI: startet PyWebView
- Ohne GUI (z.B. GitHub Codespaces): startet lokalen HTTP-Server
"""

from pathlib import Path
import os
import threading
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from .api import DashboardAPI


def _dashboard_paths():
    project_root = Path(__file__).resolve().parents[3]
    web_root = project_root / "web"
    dashboard = web_root / "dashboard" / "index.html"
    return project_root, web_root, dashboard


def _start_browser_mode():
    _, web_root, _ = _dashboard_paths()

    os.chdir(web_root)

    server = ThreadingHTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)

    threading.Thread(target=server.serve_forever, daemon=True).start()

    print("🌐 Browsermodus aktiv")
    print("http://127.0.0.1:8000/dashboard/")
    webbrowser.open("http://127.0.0.1:8000/dashboard/")

    input("ENTER beendet den Server...")
    server.shutdown()


def _start_desktop_mode():
    import webview

    _, _, dashboard = _dashboard_paths()

    api = DashboardAPI()

    webview.create_window(
        "MegaCoocookExcel",
        url=dashboard.as_uri(),
        js_api=api,
        width=1400,
        height=900,
    )
    webview.start(debug=True)


def main():
    try:
        _start_desktop_mode()
    except Exception as ex:
        print("Desktopmodus nicht verfügbar.")
        print(ex)
        print("Wechsle in Browsermodus...")
        _start_browser_mode()


if __name__ == "__main__":
    main()
