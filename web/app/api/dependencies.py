from fastapi import HTTPException, Depends, status

from app.db.database import database
from app.repositories.users import UserRepository
from app.db import UserModel, PageModel, ProductModel
from app.repositories.products import ProductRepository

from app.core.security import decode_access_token, JWTBearer


def get_user_repository() -> UserRepository:
    return UserRepository(database=database, model=UserModel)


def get_products_repository() -> ProductRepository:
    return ProductRepository(database=database, model=ProductModel)


async def get_current_user(
        user_repo: UserRepository = Depends(get_user_repository),
        token: str = Depends(JWTBearer())
):
    """"""
    cred_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Credentials are not valid."
    )

    payload = await decode_access_token(token)

    if not payload:
        raise cred_exception

    user_id = payload.get("sub", None)

    if not user_id:
        raise cred_exception

    user = await user_repo.get_by_field(field='id', value=int(user_id))

    if not user:
        return cred_exception

    return user
