from dataclasses import dataclass
import datetime


@dataclass(slots=True)
class ShoppingItem:
    """
    Represents one occurrence of an article in one meal.
    """

    # Article
    article: str

    # Total amount needed for the whole camp
    total_amount: float
    total_unit: str

    # Amount required for this specific dish
    recipe_amount: float
    recipe_unit: str

    # Dish / Recipe
    dish: str

    # Meal planning
    meal: str | None = None
    servings: int | None = None
    date: datetime.date | None = None

    # Shopping
    category: str | None = None
    store: str |None = None


@dataclass(slots=True)
class Article:
    """
    Master data of one article imported from the Coocook article list.
    """

    # Name used by Coocook
    name: str

    # Shop Section
    shop: str

    # Suggested Unit
    unit: str

    # Optional comment from Coocook
    comment: str = ""

    # Tags from Coocook
    tags: str = ""

    # Maintained by MegaCoocookExcel
    category: str = ""

    @property
    def key(self) -> str:
        """
        Returns a normalized key for lookups.
        """
        return self.name.strip().casefold()

    def to_dict(self) -> dict:
        """
        Converts the article into the JSON structure used by
        articles.json.
        """
        return {
            "shop": self.shop,
            "unit": self.unit,
            "comment": self.comment,
            "category": self.category,
            "tags": self.tags,
        }