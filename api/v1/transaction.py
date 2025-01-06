from api.security import get_current_user
from database import db_helper
from schemas.transaction import TransactionCreate

from fastapi import APIRouter
from fastapi import Depends


from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession


transaction_router = APIRouter(prefix="/transactions", tags=["Транзакции"])


@transaction_router.post("/")
async def create_transaction(
    transaction: TransactionCreate, 
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user)):
    
    return transaction


@transaction_router.put("/")
async def update_transaction(user=Depends(get_current_user)):
    pass


@transaction_router.delete("/")
async def delete_transaction(user=Depends(get_current_user)):
    pass
