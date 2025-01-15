from sqlalchemy.ext.asyncio import AsyncSession
from models import Incomes, Expenses
from models import Category

from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import selectinload


class BudgetService:
    async def get_budget(
        self, user_id: int, operation_type: Incomes | Expenses, session: AsyncSession
    ):
        stmt = (
            select(operation_type)
            .options(selectinload(operation_type.category))
            .where(operation_type.user_id == user_id)
        )
        result = await session.execute(stmt)
        return result.scalars().all()

    async def get_by_category_name(
        self,
        user_id: int,
        category_name: str,
        operation_type: Incomes | Expenses,
        session: AsyncSession,
    ):
        stmt = select(operation_type).where(
            operation_type.category_name == category_name,
            operation_type.user_id == user_id,
        )

        print(stmt)
        result = await session.execute(stmt)
        return result.scalar()

    async def add(
        self,
        category_name: str,
        Operation: Incomes | Expenses,
        user_id: int,
        category_id: int,
        session: AsyncSession,
    ):
        operations_model = Operation(
            category_name=category_name, user_id=user_id, category_id=category_id
        )

        # check_in_db = await self.get_by_category_name(
        #     user_id=user_id,
        #     category_name=category_name,
        #     operation=Operation,
        #     session=session)

        # if check_in_db:
        #     raise HTTPException(status_code=403, detail='Категория уже существует')

        session.add(operations_model)

        await session.commit()
        return operations_model
