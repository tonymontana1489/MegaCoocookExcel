from dataclasses import dataclass
from datetime import date


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
    date: date | None = None

    # Shopping
    category: str | None = None