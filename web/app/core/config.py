import os

# JWT CONFIGS
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 50
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    default='i_am_super_secret'
)
# DATABASE ================================

PG_HOST = os.getenv(
    "POSTGRES_HOST",
    default="localhost"
)

PG_PORT = os.getenv(
    "POSTGRES_PORT",
    default=5432
)

PG_USER = os.getenv(
    "POSTGRES_USER",
    default="postgres"
)

PG_PASS = os.getenv(
    "POSTGRES_PASSWORD",
    default="example"
)

DATABASE = os.getenv(
    "POSTGRES_DB",
    default="veetok_backend"
)

LEVEL = os.getenv("LEVEL", default="DEV")

POSTGRESQL_URL = f"postgresql+asyncpg://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DATABASE}"
