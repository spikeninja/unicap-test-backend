from app.schemas.mixins import DateTimeMixin
from pydantic import BaseModel, EmailStr, constr


class ProductDB(DateTimeMixin):
    id: str
    name: str
    email: EmailStr

    hashed_password: str
