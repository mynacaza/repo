from fastapi import APIRouter
from fastapi import Form

from schemas.user import UserCreate

from typing import Annotated

users_router = APIRouter(prefix='/users', tags=['Пользователь'])



@users_router.post('/create')
async def create_user(form_data: Annotated[UserCreate, Form()]):
  return form_data