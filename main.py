from database import db_helper


import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # подключение к бд
    yield

    db_helper.dispose()


app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "start"}

