from app.schemas.mixins import DateTimeMixin


class ProductDB(DateTimeMixin):
    id: int
    name: str
    state: str
    location: str
    image_src: str | None
    product_url: str


class PageDB(DateTimeMixin):
    id: int
    task_id: str
    page_url: str

    products: list[ProductDB]
