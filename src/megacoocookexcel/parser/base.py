from abc import ABC, abstractmethod

from typing import List

from megacoocookexcel.models import ShoppingItem


class BaseParser(ABC):

    @abstractmethod
    def parse(self, file_path: str) -> List[ShoppingItem]:
        pass