from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class ShoppingItem:
    name: str
    quantity: float
    unit: str

    recipe: str | None = None
    servings: int | None = None
    day: str | None = None
    date: str | None = None

    category: str | None = None
    notes: str | None = None