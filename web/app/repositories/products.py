import sqlalchemy as sa

from app.db import PageModel
from app.repositories.base import BaseRepository
from app.schemas.products import ProductDB, PageDB


class ProductRepository(BaseRepository):
    """"""

    async def get_by_task_id(self, task_id: str) -> list[PageDB]:
        """"""

        page_query = sa.select(PageModel).where(PageModel.task_id == task_id)

        raw_pages = await self.database.fetch_all(query=page_query)
        raw_pages = [dict(raw_page) for raw_page in raw_pages]

        results = []
        for raw_page in raw_pages:
            query = self.table.select().where(getattr(self.table.c, 'page_id') == raw_page['id'])
            raw_products = await self.database.fetch_all(query=query)

            if raw_products:
                products = [ProductDB.model_validate(dict(raw_product)) for raw_product in raw_products]
            else:
                products = []

            page = PageDB(
                id=raw_page['id'],
                task_id=task_id,
                page_url=raw_page['page_url'],
                updated_at=raw_page['updated_at'],
                created_at=raw_page['created_at'],
                products=products
            )

            results.append(page)

        return results
