import sqlalchemy as sa
from databases import Database


class BaseRepository:
    def __init__(self, database: Database, model):
        self.database = database
        self.model = model

    @property
    def table(self) -> sa.Table:
        return self.model.__table__

    async def raw_get_by_id(self, row_id: int | str) -> tuple | None:
        """"""
        query = self.table.select().where(self.table.c.id == row_id)
        return await self.database.fetch_one(query=query)
