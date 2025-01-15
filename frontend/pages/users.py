from .template import templates

from fastapi import APIRouter, Request

users_router = APIRouter(prefix='/users', tags=['Фронтенд. Пользователь'])

@users_router.get('/sign-up')
async def sign_up(request: Request):
  return templates.TemplateResponse(name='registration.html', context={"request": request})