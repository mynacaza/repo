from schemas.user import UserCreate
from crud.user import UserService
from api.utils import create_jwt_token, decode_jwt_token
from database.db_helper import db_helper

from fastapi import APIRouter
from fastapi import Form, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

users_router = APIRouter(prefix="/users", tags=["Пользователь"])
user_service = UserService()


@users_router.post("/create")
async def get_token(
    create_user: Annotated[UserCreate, Form()],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    email_in_db = await user_service.get_user_by_email(create_user, session)
    if email_in_db:
        raise HTTPException(
            status_code=403, detail="Пользователь с таким email уже зарегистрирован."
        )

    email = await user_service.add_user(create_user, session)
    access_token = await create_jwt_token({"email": email})

    return access_token
