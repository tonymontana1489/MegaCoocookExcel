from pathlib import Path
from megacoocookexcel.importer.article_importer import ArticleImporter
from megacoocookexcel.importer.article_repository import ArticleRepository

class DashboardBridge:
    def __init__(self):
        self.importer=ArticleImporter()
        self.repo=ArticleRepository()
        self.json=Path(__file__).resolve().parents[3]/"config"/"articles.json"
    def import_article_pdf(self,pdf_path):
        arts=self.importer.import_pdf(pdf_path)
        self.repo.save(arts,self.json)
        return {"success":True,"count":len(arts)}
    def load_articles(self):
        return self.repo.load(self.json)
