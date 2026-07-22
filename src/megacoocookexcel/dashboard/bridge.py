"""
Sprint 3.8 - Dashboard <-> Importer <-> Repository

Importpfade ggf. an den aktuellen Projektstand anpassen.
"""

from pathlib import Path

from megacoocookexcel.importer.article_importer import ArticleImporter
from megacoocookexcel.importer.article_repository import ArticleRepository


class DashboardBridge:

    def __init__(self):
        self.repository = ArticleRepository()
        self.importer = ArticleImporter()

        self.json_file = (
            Path(__file__).resolve().parents[3]
            / "config"
            / "articles.json"
        )

    def import_article_pdf(self, pdf_path: str):
        articles = self.importer.import_pdf(pdf_path)
        self.repository.save(articles, self.json_file)
        return {
            "success": True,
            "articles": self.repository.load(self.json_file),
        }

    def load_articles(self):
        return self.repository.load(self.json_file)

    def save_articles(self, articles):
        self.repository.save(articles, self.json_file)
        return {"success": True}
