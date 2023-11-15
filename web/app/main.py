from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils import lifespan
from app.api import parsers, users


def application_factory() -> FastAPI:
    """"""

    app = FastAPI(lifespan=lifespan)

    # In dev purposes
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    app.include_router(users.router, prefix='/api/users', tags=['users'])
    app.include_router(parsers.router, prefix='/api/parsers', tags=['parsers'])

    return app


app = application_factory()
