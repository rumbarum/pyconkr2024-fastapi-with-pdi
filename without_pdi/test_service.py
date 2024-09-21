"""Tests module."""

from unittest import mock
import pytest
from . import dependency


@pytest.mark.asyncio
async def test_service():
    service = dependency.get_service()
    test_key = "test_key"
    test_value = "test_value"

    await service.set(test_key, test_value)
    result = await service.get(test_key)

    assert result == test_value


@pytest.mark.asyncio
async def test_replace_repository_with_mock():
    mocking = mock.AsyncMock()
    mocking.set.return_value =  None
    mocking.get.return_value = "mocked_value"

    service = dependency.Service(repository=mocking)

    assert isinstance(service._repository, mock.AsyncMock)
    assert await service.set("test_key", "test_value") == None
    assert await service.get("test_key") == "mocked_value"


@pytest.mark.asyncio
async def test_replace_service_with_mock():
    mocking = mock.AsyncMock()
    mocking.set.return_value =  None
    mocking.get.return_value = "mocked_value"

    service = dependency.get_service(get_repository=lambda: mocking)

    assert isinstance(service._repository, mock.AsyncMock)
    assert await service.set("test_key", "test_value") == None
    assert await service.get("test_key") == "mocked_value"


@pytest.mark.asyncio
async def test_replace_service_with_other_redis():
    class NewRedis:
        async def set(self, key, value):
            return None
        async def get(self, key):
            return b"mocked_value"
    def _new_redis():
        return NewRedis()

    service = dependency.get_service(
        get_repository=lambda: dependency.get_repository(
            get_redis=_new_redis
        )
    )
    assert isinstance(service._repository._redis, NewRedis)
    assert await service.get("test_key") == "mocked_value"
