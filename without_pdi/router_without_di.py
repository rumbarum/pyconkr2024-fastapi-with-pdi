from fastapi import APIRouter, Query, Body
from . import dependency

router = APIRouter(prefix="/value")

@router.post("")
async def set_key_with_value(body: dict = Body()):
    service = dependency.Service(
        repository=dependency.Repository(
            redis=dependency.get_redis()
        )
    )
    await service.set(body["key"], body["value"])
    return {"message": "success"}

@router.get("")
async def get_by_key(key: str = Query()):
    service = dependency.Service(
        repository=dependency.Repository(
            redis=dependency.get_redis()
        )
    )
    return await service.get(key)
