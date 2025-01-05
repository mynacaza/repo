from models import User
from schemas.user import UserCreate
from api.utils import get_password_hash
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    async def get_user_by_email(self, email: str, session: AsyncSession):
        stmt = select(User).where(User.email == email)
        return await session.scalar(stmt)

    async def add_user(self, create_user: UserCreate, session: AsyncSession):
        user_data = create_user.model_dump()

        del user_data["password"]
        user_data["hash_password"] = get_password_hash(create_user.password)

        user = User(**user_data)
        session.add(user)
        await session.commit()
        return user.email
