from .budget import BudgetService
from models.models import Category, Incomes, Expenses, Transaction
from schemas.categories import CategoryModel

budget_service = BudgetService()

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select, delete


class CategoriesService:
    async def get_category(
        self,
        user_id: int,
        operation_type: str,
        category_name: str,
        session: AsyncSession,
    ):
        stmt = (
            select(Category.id)
            .join(Incomes)
            .where(Incomes.user_id == user_id, Incomes.category_name == category_name)
        )

        return await session.scalar(stmt)

    async def add_category(
        self,
        user_id: int,
        operation_type: Incomes | Expenses,
        name: str,
        session: AsyncSession,
    ):
        category = Category(operation_type=operation_type, name=name)
        category.user_id = user_id

        session.add(category)

        await session.commit()
        return category

    async def delete_category(self, category_id: int, session: AsyncSession):
        stmt_delete_category = select(Category).where(Category.id == category_id)
        result = await session.execute(stmt_delete_category)
        category = result.scalar_one_or_none()
        print(category_id)
        if category:
            await session.delete(category)
            await session.commit()
        else:
            print("Категория не найдена.")
