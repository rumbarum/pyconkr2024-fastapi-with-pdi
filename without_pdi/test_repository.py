"""Tests module."""

from unittest import mock

import pytest

from . import dependency


@pytest.mark.asyncio
async def test_repository():
    repository = dependency.get_repository()
    test_key = "test_key"
    test_value = "test_value"

    await repository.set(test_key, test_value)
    result = await repository.get(test_key)

    assert result == test_value


@pytest.mark.asyncio
async def test_replace_repository_with_mock():
    mocking = mock.AsyncMock()
    mocking.set.return_value =  None
    mocking.get.return_value = b"mocked_value"

    repository = dependency.get_repository(get_redis=lambda: mocking)

    assert isinstance(repository._redis, mock.AsyncMock)
    assert await repository.set("test_key", "test_value") == None
    assert await repository.get("test_key") == "mocked_value"


@pytest.mark.asyncio
async def test_replace_repository_with_other_redis():
    class NewRedis:
        async def set(self, key, value):
            return None
        async def get(self, key):
            return b"mocked_value"

    def _new_redis():
        return NewRedis()

    repository = dependency.get_repository(get_redis=_new_redis)

    assert isinstance(repository._redis, NewRedis)
    assert await repository.get("test_key") == "mocked_value"
