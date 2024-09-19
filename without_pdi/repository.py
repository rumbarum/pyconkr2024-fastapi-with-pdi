from redis.asyncio import Redis

class Repository:
    def __init__(self, redis: Redis) -> None:
        self._redis = redis

    async def set(self, key: str, value: str) -> None:
        await self._redis.set(name=key, value=value)

    async def get(self, key) -> str:
        return (await self._redis.get(key)).decode()
