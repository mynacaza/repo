from api.security import get_current_user
from database import db_helper

from schemas.transaction import TransactionModel
from schemas.transaction import TypeCategory
from crud.transactions import TransactionsService

from fastapi import APIRouter
from fastapi import Depends


from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, List


transaction_router = APIRouter(prefix="/transactions", tags=["Транзакции"])
transaction_service = TransactionsService()


@transaction_router.get("/all", response_model=List[TransactionModel])
async def get_all_transactions(
    operation_type: TypeCategory,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user),
):
    user_id = int(user.get("sub"))

    transactions = await transaction_service.get_list_transaction(
        user_id=user_id, operation_type=operation_type, session=session
    )

    return transactions


@transaction_router.get("/", response_model=TransactionModel)
async def my_transactions(
    transaction_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user),
):
    user_id = int(user.get("sub"))

    result = await transaction_service.get_transaction(
        user_id=user_id, transaction_id=transaction_id, session=session
    )
    return result


@transaction_router.post("/", response_model=TransactionModel)
async def create_transaction(
    transaction: TransactionModel,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user),
):
    user_id = int(user.get("sub"))

    result = await transaction_service.add_transaction(
        user_id=user_id, transaction=transaction, session=session
    )
    return result


@transaction_router.put("/{transaction_id}", response_model=TransactionModel)
async def update_transaction(
    transaction_id: int,
    transaction: TransactionModel,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user),
):
    user_id = int(user.get("sub"))
    rowcount = await transaction_service.editing_transaction(
        user_id=user_id,
        transaction_id=transaction_id,
        transaction=transaction,
        session=session,
    )

    if not rowcount:
        raise ValueError("Transaction not found no changes made")

    new_transaction = await transaction_service.get_transaction(
        user_id=user_id, transaction_id=transaction_id, session=session
    )

    return new_transaction


@transaction_router.delete("/{transaction_id}", status_code=204)
async def delete_transaction(
    transaction_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user=Depends(get_current_user),
) -> None:
    user_id = int(user.get("sub"))

    await transaction_service.delete_transaction(
        user_id=user_id, transaction_id=transaction_id, session=session
    )
