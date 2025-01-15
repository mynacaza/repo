from database import db_helper
from middleware import CustomMiddlewate

from api import api_router
from frontend.pages import pages_router

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    # подключение к бд

    yield

    await db_helper.dispose()


app = FastAPI(lifespan=life_span)
app.mount('/static', StaticFiles(directory='frontend/static'), 'static')

app.add_middleware(CustomMiddlewate)

app.include_router(pages_router)
app.include_router(api_router)
