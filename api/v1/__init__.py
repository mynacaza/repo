from .user import users_router
from .transaction import transaction_router

from fastapi import APIRouter


router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(users_router)
router_v1.include_router(transaction_router)
