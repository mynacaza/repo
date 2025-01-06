from models.user import Transaction
from schemas.transaction import TransactionModel

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete


class TransactionsService:
    async def add_transaction(
        self, user_id: int, transaction: TransactionModel, session: AsyncSession
    ):
        transaction_data = transaction.model_dump()
        transaction = Transaction(**transaction_data)
        transaction.user_id = user_id
        session.add(transaction)
        await session.commit()

    async def editing_transaction(
        self, transaction_id: int, transaction: TransactionModel, session: AsyncSession
    ):
        stmt = (
            update(Transaction)
            .where(Transaction.id == transaction_id)
            .values(**transaction.model_dump())
        )

        await session.execute(stmt)
        await session.commit()

    async def delete_transaction(self, transaction_id: int, session: AsyncSession):
        stmt = delete(Transaction).where(Transaction.id == transaction_id)

        await session.execute(stmt)
        await session.commit()
