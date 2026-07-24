from megacoocookexcel.importer.article_importer import ArticleImporter
from megacoocookexcel.importer.article_repository import ArticleRepository


class DashboardBridge:
    def __init__(self):
        self.importer = ArticleImporter()
        self.repo = ArticleRepository()

    def import_article_pdf(self, pdf_path):
        articles = self.importer.import_pdf(pdf_path)

        self.repo.save(articles)

        return {
            "success": True,
            "count": len(articles),
        }

    def load_articles(self):
        return self.repo.load()