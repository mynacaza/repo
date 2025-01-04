from .v1 import router_v1

from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

api_router.include_router(router_v1)
