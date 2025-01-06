from pydantic import BaseModel
from datetime import date


class TransactionCreate(BaseModel):
  amount: int
  date: date
  comment: str | None = None
