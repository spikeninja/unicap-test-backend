from app.schemas.mixins import DateTimeMixin
from pydantic import BaseModel, EmailStr, constr


class UserDB(DateTimeMixin):
    id: int
    email: EmailStr

    hashed_password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserPublic(BaseModel):
    id: int
    email: str


class AuthResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserPublic


class LoginRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
