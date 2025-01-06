from api.security import get_current_user
from database import db_helper
from schemas.transaction import TransactionModel
from crud.transactions import TransactionsService

from fastapi import APIRouter
from fastapi import Depends


from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession


transaction_router = APIRouter(prefix="/transactions", tags=["Транзакции"])
transaction_sevice = TransactionsService()

@transaction_router.post("/", status_code=201)
async def create_transaction(
    transaction: TransactionModel, 
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user)):
    
    user_id = int(user.get('sub'))

    await transaction_sevice.add_transaction(user_id=user_id, transaction=transaction,session=session)
    return {'message': f'Транзакция {transaction.model_dump()} добавлена.'}


@transaction_router.put("/", status_code=200)
async def update_transaction(
    transaction_id: int,
    transaction: TransactionModel, 
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user)):


    await transaction_sevice.editing_transaction(transaction_id, transaction, session)

    return {'message': f'Детали транзакции № {transaction_id} обновлены.'}


@transaction_router.delete("/", status_code=204)
async def delete_transaction(    
    transaction_id: int, 
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user)):

    await transaction_sevice.delete_transaction(transaction_id, session)




    
