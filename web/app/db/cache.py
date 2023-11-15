from redis import Redis

from redis.asyncio import Redis as AsyncRedis

from app.core.config import CACHE_URL


def get_sync_client() -> Redis:
    return Redis.from_url(url=CACHE_URL)


async def get_async_client() -> AsyncRedis:
    return AsyncRedis.from_url(url=CACHE_URL)
