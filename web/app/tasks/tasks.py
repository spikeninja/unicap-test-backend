import json
from datetime import datetime

import sqlalchemy as sa
from celery import Celery

from app.db.database import engine
from app.tasks.utils import parse_olx
from app.db.cache import get_sync_client
from app.db import PageModel, ProductModel
from app.core.config import BACKEND_URL, BROKER_URL


worker = Celery(backend=BACKEND_URL, broker=BROKER_URL)


@worker.task(bind=True)
def task_scrape_olx(self, url: str):
    """"""
    task_id = self.request.id
    rclient = get_sync_client()

    data = []
    pages_urls = [url, f'{url}?page=2', f'{url}?page=3', f'{url}?page=4']

    for idx, page_url in enumerate(pages_urls):
        products = parse_olx(url=page_url)
        data.append({'page': idx + 1, 'data': products, 'task_id': task_id})

    # add first page to the cache like (url, first_page_data)
    rclient.hset(name='mycache', key=url, value=json.dumps(data[0]))

    for page_data, page_url in zip(data, pages_urls):

        now_ = datetime.utcnow()
        page_insert = {
            'task_id': task_id,
            'page_url': page_url,
            'created_at': now_,
            'updated_at': now_,
        }

        with engine.connect() as conn:
            page_id = conn.execute(
                sa.insert(PageModel).returning(PageModel.id),
                page_insert
            ).scalar()

            product_bulk = [{'page_id': page_id, **product} for product in page_data['data']]

            conn.execute(sa.insert(ProductModel), product_bulk)
