from fastapi import APIRouter, Depends, HTTPException, status

from app.repositories.users import UserRepository
from app.core.security import verify_password, create_access_token
from app.api.dependencies import get_current_user, get_user_repository
from app.schemas.auth import UserPublic, UserCreate, UserDB, AuthResponse, LoginRequest


router = APIRouter()


@router.get("/me", response_model=UserPublic)
async def get_me(current_user: UserDB = Depends(get_current_user)):
    """"""

    return current_user


@router.post("/login", response_model=AuthResponse)
async def auth(
        login: LoginRequest,
        users_repo: UserRepository = Depends(get_user_repository)
):
    """"""

    db_user = await users_repo.get_by_field(field="email", value=login.email)

    if not db_user:
        raise HTTPException(
            detail="Invalid credentials",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    password_verified = await verify_password(login.password, db_user.hashed_password)

    if not password_verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials"
        )

    token = await create_access_token({'sub': str(db_user.id)})

    return {
        'access_token': token,
        'token_type': 'Bearer',
        'user': db_user
    }


@router.post("/register", response_model=AuthResponse)
async def register(
        user: UserCreate,
        users_repo: UserRepository = Depends(get_user_repository)
):
    """"""
    db_user = await users_repo.get_by_field(field="email", value=user.email)

    if db_user:
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists."
        )

    user_id = await users_repo.create(u=user)
    user = await users_repo.get_by_field(field='id', value=user_id)

    access_token = await create_access_token({"sub": str(user.id)})

    return {
        'access_token': access_token,
        'token_type': 'Bearer',
        'user': user,
    }
