from pathlib import Path
import shutil
import tempfile

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles

from .bridge import DashboardBridge

ROOT = Path(__file__).resolve().parents[3]
WEB = ROOT / "web" / "dashboard"

app = FastAPI(title="MegaCoocookExcel")
bridge = DashboardBridge()


@app.post("/api/import")
async def import_pdf(pdf: UploadFile = File(...)):
    suffix = Path(pdf.filename or "import.pdf").suffix

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(pdf.file, tmp)
        tmp_path = Path(tmp.name)

    try:
        return bridge.import_article_pdf(str(tmp_path))
    finally:
        tmp_path.unlink(missing_ok=True)


@app.get("/api/articles")
def articles():
    return bridge.load_articles()


app.mount("/", StaticFiles(directory=WEB, html=True), name="dashboard")