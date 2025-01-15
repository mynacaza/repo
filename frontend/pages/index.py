from .template import templates

from fastapi import APIRouter
from fastapi import Request


index_router = APIRouter(tags=['Фронтенд. Главная страница'])


@index_router.get('/')
async def home_page(request: Request):
    return templates.TemplateResponse(name='home.html', context={'request': request})