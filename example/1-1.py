@router.get("/path/{id}", response_model=OutModel)
async def do_something(id:UUID):
    stmt = select(Model).filter(Model.id == id)
    async with session_factory() as session:
        response = session.execute(stmt)
        result = response.scalar()

    return OutModel.from_orm(result)
