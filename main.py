from database import db_helper

from api import api_router

from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    # подключение к бд
    print('все гуд')
    yield

    await db_helper.dispose()


app = FastAPI(lifespan=life_span)


@app.get("/")
async def root() -> dict:
    return {"message": "start"}


app.include_router(api_router)
