@router.get("/path", response_model=OutModel)
async def calculate(id:UUID):



    return OutModel.from_orm(result)
