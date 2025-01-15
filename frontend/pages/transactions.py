from .template import templates
from api.v1.transaction import get_all_transactions

from fastapi import APIRouter, Depends, Request


transactions_router = APIRouter(prefix="/transactions", tags=["Фронтенд. Транзакции"])



@transactions_router.get("/")
async def get_students_html(request: Request, transactions=Depends(get_all_transactions)):
    return templates.TemplateResponse(
        name="transactions.html", context={"request": request, 'transactions': transactions}
    )
