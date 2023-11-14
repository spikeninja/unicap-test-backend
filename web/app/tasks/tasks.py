from celery import Celery

from app.tasks.utils import parse_olx

worker = Celery(
    backend="redis://redis:6379/1",
    broker="redis://redis:6379/2",
)


@worker.task(bind=True)
def task_scrape_olx(self, url: str):
    """"""
    task_id = self.request.id

    # get olx items for 4 pages
    products = parse_olx(url=url)

    # add first page to the cache like (task_id, first_page_data)
    # store in the postgres db result of good pages
