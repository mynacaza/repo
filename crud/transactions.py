from models import Transaction
from schemas.transaction import TransactionModel
from schemas.transaction import TypeCategory

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete


class TransactionsService:
    async def get_list_transaction(
        self, user_id: int, operation_type: TypeCategory, session: AsyncSession
    ):
        stmt = select(Transaction).where(
            Transaction.user_id == user_id, Transaction.operation_type == operation_type
        )
        result = await session.scalars(stmt)

        return result

    async def get_transaction(
        self, user_id: int, transaction_id: int, session: AsyncSession
    ):
        stmt = select(Transaction).where(
            Transaction.user_id == user_id, Transaction.id == transaction_id
        )
        return await session.scalar(stmt)

    async def add_transaction(
        self, user_id: int, transaction: TransactionModel, session: AsyncSession
    ):
        transaction_data = transaction.model_dump()
        transaction = Transaction(**transaction_data)
        transaction.user_id = user_id
        session.add(transaction)
        await session.commit()

    async def editing_transaction(
        self,
        user_id: int,
        transaction_id: int,
        transaction: TransactionModel,
        session: AsyncSession,
    ):
        stmt = (
            update(Transaction)
            .where(Transaction.id == transaction_id, Transaction.user_id == user_id)
            .values(**transaction.model_dump())
        )

        result = await session.execute(stmt)
        await session.commit()
        return result.rowcount

    async def delete_transaction(
        self, user_id: int, transaction_id: int, session: AsyncSession
    ):
        stmt = delete(Transaction).where(Transaction.id == transaction_id)

        await session.execute(stmt)
        await session.commit()
