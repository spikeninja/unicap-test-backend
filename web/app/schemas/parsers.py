from enum import Enum
from pydantic import BaseModel


class CategoryEnum(Enum):
    cars = 'cars'  # https://www.olx.pl/motoryzacja/pozostala-motoryzacja/
    electronics = 'electronics'  # https://www.olx.pl/elektronika/gry-konsole/


class ParserRequest(BaseModel):
    category: CategoryEnum
