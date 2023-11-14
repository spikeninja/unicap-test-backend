import datetime
from typing import Literal

from app.core.security import hash_password
from app.schemas.auth import UserDB, UserCreate
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_by_field(self, field: Literal["id", "email"], value: any) -> UserDB | None:
        """"""

        query = self.table.select().where(getattr(self.table.c, field) == value)
        raw_user = await self.database.fetch_one(query=query)

        return UserDB.model_validate(dict(raw_user)) if raw_user else None

    async def create(self, u: UserCreate) -> int:
        """"""

        raw_user = u.model_dump()
        hashed = await hash_password(raw_user.pop("password"))

        raw_user.pop("id", None)
        raw_user.update({"hashed_password": hashed})

        now = datetime.datetime.utcnow()

        query = self.table.insert().values(
            **raw_user,
            created_at=now,
            updated_at=now,
        )

        result = await self.database.execute(query)

        return result
