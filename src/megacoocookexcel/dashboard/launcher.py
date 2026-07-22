from pathlib import Path
import os
import threading
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from .api import DashboardAPI

def main():
    try:
        import webview
        project_root = Path(__file__).resolve().parents[3]
        page = project_root / "web" / "dashboard" / "index.html"
        webview.create_window(
            "MegaCoocookExcel",
            url=page.as_uri(),
            js_api=DashboardAPI()
        )
        webview.start(debug=True)
    except Exception:
        project_root = Path(__file__).resolve().parents[3]
        os.chdir(project_root / "web")
        server = ThreadingHTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        webbrowser.open("http://127.0.0.1:8000/dashboard/")
        print("Dashboard läuft unter http://127.0.0.1:8000/dashboard/")
        input("ENTER beendet den Server...")
        server.shutdown()

if __name__ == "__main__":
    main()
