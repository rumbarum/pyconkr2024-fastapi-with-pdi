from fastapi import APIRouter, Body, Query, Depends
from dependency_injector.wiring import Provide, inject
from .application import container
from .service import Service

router = APIRouter(prefix="/value")

@router.post("")
@inject
async def set_key_with_value(
    body: dict = Body(),
    service: Service=Depends(Provide[container.service])
):
    await service.set(body["key"], body["value"])
    return {"message": "success"}

@router.get("")
@inject
async def get_by_key(
    key: str = Query(),
    service=Depends(Provide[container.service])
):
    return await service.get(key)
