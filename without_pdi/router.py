from fastapi import APIRouter, Depends, Query, Body
from .service import Service
from . import dependency

router = APIRouter(prefix="/value")

@router.post("")
async def set_key_with_value(
    body: dict = Body(),
    service: Service = Depends(dependency.get_service)
):
    await service.set(body["key"], body["value"])
    return {"message": "success"}

@router.get( "")
async def get_by_key(
    key: str = Query(),
    service: Service = Depends(dependency.get_service),
):
    return await service.get(key)
