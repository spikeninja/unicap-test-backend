from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.db.database import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """"""
    await database.connect()
    yield
    await database.disconnect()


CATEGORY_MAP = {
    'cars': 'https://www.olx.pl/motoryzacja/pozostala-motoryzacja/',
    'electronics': 'https://www.olx.pl/elektronika/gry-konsole/',
    'sport': 'https://www.olx.pl/sport-hobby/sporty-zimowe/',
    'motorbike_parts': 'https://www.olx.pl/motoryzacja/czesci-motocyklowe/'
}
