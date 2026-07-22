from .bridge import DashboardBridge

class DashboardAPI:
    def __init__(self):
        self.bridge = DashboardBridge()

    def import_article_pdf(self, pdf_path):
        return self.bridge.import_article_pdf(pdf_path)

    def load_articles(self):
        return self.bridge.load_articles()

    def save_articles(self, articles):
        return self.bridge.save_articles(articles)
