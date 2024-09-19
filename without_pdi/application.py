from fastapi import FastAPI
from without_pdi.router import router

app = FastAPI()
app.include_router(router)
