from enum import Enum
from pydantic import BaseModel


class CategoryEnum(Enum):
    cars = 'cars'  # https://www.olx.pl/motoryzacja/pozostala-motoryzacja/
    electronics = 'electronics'  # https://www.olx.pl/elektronika/gry-konsole/
    sport = 'sport'
    motorbike_parts = 'motorbike_parts'


class ParserRequest(BaseModel):
    category: CategoryEnum
