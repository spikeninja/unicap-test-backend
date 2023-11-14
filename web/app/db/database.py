from databases import Database

from app.core.config import POSTGRESQL_URL


database = Database(POSTGRESQL_URL)
