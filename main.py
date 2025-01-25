
from database import db_helper


from api import api_router
from fastapi import FastAPI

from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):

    yield
    await db_helper.dispose()


app = FastAPI(lifespan=life_span)


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)