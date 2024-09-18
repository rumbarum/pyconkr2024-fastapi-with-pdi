from fastapi import FastAPI
from .container import create_container
from .router import router

app = FastAPI()
app.include_router(router)
container = create_container()
