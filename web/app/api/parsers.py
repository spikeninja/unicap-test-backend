from fastapi import APIRouter, Depends, HTTPException

from app.utils import CATEGORY_MAP
from app.schemas.auth import UserDB
from app.schemas.parsers import ParserRequest
from app.api.dependencies import get_current_user
from app.tasks.tasks import worker, task_scrape_olx

router = APIRouter()


@router.post("/")
async def scrape_category(
        request: ParserRequest,
        current_user: UserDB = Depends(get_current_user)
):
    """"""

    url = CATEGORY_MAP[request.category]
    task = task_scrape_olx.delay(url)

    return {'task_id': task.id}


@router.get("/results/{task_id}")
async def get_result(
        task_id: str,
        current_user: UserDB = Depends(get_current_user),
):
    """"""


@router.get("/statuses/{task_id}")
async def get_task_status(
        task_id: str,
        current_user: UserDB = Depends(get_current_user)
):
    """"""

    task = task_scrape_olx.AsyncResult(task_id, app=worker)
    return {"state": task.state}
