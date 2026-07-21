from abc import ABC, abstractmethod

from megacoocookexcel.models import ShoppingItem


class BaseParser(ABC):
    """Base class for all shopping list parsers."""

    @abstractmethod
    def parse(self, file_path: str) -> list[ShoppingItem]:
        """Parse a shopping list and return ShoppingItems."""
        raise NotImplementedError