from models.models import Transaction, Category
from schemas.transaction import TransactionModel

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete


class TransactionsService:
    async def get_transaction_by_id(
        self,
        user_id: int,
        category_name: str,
        transaction_id: int,
        session: AsyncSession,
    ):
        transaction = (
            select(Transaction)
            .join(Category)
            .where(
                Transaction.id == transaction_id,
                Transaction.user_id == user_id,
                Category.name == category_name,
            )
        )

        result = await session.scalar(transaction)
        return result

    async def add_transaction(
        self,
        user_id: int,
        category_id: int,
        transaction: TransactionModel,
        session: AsyncSession,
    ):
        transaction_data = transaction.model_dump()
        transaction = Transaction(**transaction_data)
        transaction.user_id = user_id
        transaction.category_id = category_id

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

    async def delete_transaction(
        self, user_id: int, transaction_id: int, session: AsyncSession
    ):
        stmt = delete(Transaction).where(
            Transaction.id == transaction_id, Transaction.user_id == user_id
        )

        await session.execute(stmt)
        await session.commit()
