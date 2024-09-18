from .repository import Repository


class Service:
    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    async def get(self, key: str) -> str:
        return await self._repository.get(key)

    async def set(self, key: str, value: str) -> None:
        await self._repository.set(key, value)
