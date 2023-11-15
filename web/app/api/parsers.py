import json

from fastapi import APIRouter, Depends, HTTPException

from app.utils import CATEGORY_MAP
from app.schemas.auth import UserDB
from app.schemas.parsers import ParserRequest
from app.tasks.tasks import worker, task_scrape_olx
from app.db.cache import get_async_client, AsyncRedis
from app.repositories.products import ProductRepository
from app.api.dependencies import get_current_user, get_products_repository

router = APIRouter()


@router.post("/")
async def scrape_category(
    request: ParserRequest,
    rclient: AsyncRedis = Depends(get_async_client),
    current_user: UserDB = Depends(get_current_user),
):
    """"""

    url = CATEGORY_MAP[request.category.value]

    cached_data = await rclient.hget(name='mycache', key=url)
    task = task_scrape_olx.delay(url)

    return {
        'task_id': task.id,
        'cached': json.loads(cached_data) if cached_data else None
    }


@router.get("/results/{task_id}")
async def get_result(
    task_id: str,
    current_user: UserDB = Depends(get_current_user),
    products_repo: ProductRepository = Depends(get_products_repository),
):
    """"""

    products = await products_repo.get_by_task_id(task_id=task_id)

    return products


@router.get("/statuses/{task_id}")
async def get_task_status(
    task_id: str,
    current_user: UserDB = Depends(get_current_user)
):
    """"""

    task = task_scrape_olx.AsyncResult(task_id, app=worker)
    return {"state": task.state}
