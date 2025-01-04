from schemas.user import UserCreate
from crud.user import UserService
from api.utils import create_jwt_token, decode_jwt_token
from database.db_helper import db_helper

from fastapi import APIRouter
from fastapi import Form
from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

users_router = APIRouter(prefix="/users", tags=["Пользователь"])
user_service = UserService()


@users_router.post("/create")
async def get_token(
    create_user: Annotated[UserCreate, Form()],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    user = await user_service.add_user(create_user, session)
    return user
