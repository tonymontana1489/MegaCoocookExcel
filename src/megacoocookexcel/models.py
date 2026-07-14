from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Einkaufsposten:
    """
    Repräsentiert einen einzelnen Eintrag aus einer Coocook-Einkaufsliste.
    """

    artikel: str
    menge: float
    einheit: str

    gericht: Optional[str] = None
    personen: Optional[int] = None
    tag: Optional[str] = None
    datum: Optional[str] = None

    kategorie: Optional[str] = None

    bemerkung: Optional[str] = None