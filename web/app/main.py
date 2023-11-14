from fastapi import FastAPI

from app.utils import lifespan
from app.api import parsers, users


def application_factory() -> FastAPI:
    """"""

    app = FastAPI(lifespan=lifespan)

    app.include_router(users.router, prefix='/api/users', tags=['users'])
    app.include_router(parsers.router, prefix='/api/parsers', tags=['parsers'])

    return app


app = application_factory()
