
from models.user import User, Transaction
from schemas.transaction import TransactionCreate

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class TransactionsService:
    async def get_transaction(self, user_id: ..., data: ..., session: ...):
        pass

    async def add_transaction(self, user_id: int, transaction: TransactionCreate, session: AsyncSession):
        transaction_data = transaction.model_dump()
        transaction = Transaction(**transaction_data)
        transaction.user_id = user_id
        session.add(transaction)
        await session.commit()
        return True
        

    async def editing_transaction(self, user_id: ..., data: ..., session: ...):
        pass

    async def delete_transaction(self, user_id: ..., data: ..., session: ...):
        pass
