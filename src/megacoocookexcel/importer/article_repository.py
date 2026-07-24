from __future__ import annotations

import json
from pathlib import Path

from megacoocookexcel.models import Article


class ArticleRepository:
    """
    Reads and writes the persistent articles database.
    """

    def _json_file(self) -> Path:
        return (
            Path(__file__).resolve().parents[2]
            / "data"
            / "articles.json"
        )

    # ----------------------------------------------------------

    def load(self) -> dict[str, Article]:

        json_file = self._json_file()

        if not json_file.exists():
            return {}

        with json_file.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(file)

        articles: dict[str, Article] = {}

        for name, values in data.items():

            articles[name.casefold()] = Article(
                name=name,
                shop=values.get("shop", ""),
                unit=values.get("unit", ""),
                comment=values.get("comment", ""),
                category=values.get("category", ""),
            )

        return articles

    # ----------------------------------------------------------

    def save(
        self,
        articles: list[Article],
    ) -> None:

        json_file = self._json_file()

        existing = self.load()

        #
        # Merge existing user data into imported articles
        #

        for article in articles:

            old = existing.get(article.key)

            if old:

                article.category = old.category

        #
        # Build JSON structure
        #

        output: dict[str, dict] = {}

        for article in sorted(
            articles,
            key=lambda a: a.name.casefold(),
        ):

            output[article.name] = article.to_dict()

        #
        # Save
        #

        json_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with json_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                output,
                file,
                indent=4,
                ensure_ascii=False,
            )