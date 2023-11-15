from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.core.config import POSTGRESQL_URL, SYNC_POSTGRESQL_URL


# async operations (API Layer)
database = Database(POSTGRESQL_URL)

# sync operations with db
engine = create_engine(url=SYNC_POSTGRESQL_URL)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
