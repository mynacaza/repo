from pydantic import BaseModel, Field, field_validator
from datetime import date




class TransactionModel(BaseModel):
    amount: int = Field(gt=0, le=100000)
    date: date 
    comment: str = Field(max_length=140)

    @field_validator('date')
    def check_date(cls, value):
        today = date.today()
        if value > today:
            raise ValueError('Некорректная дата: дата не может быть в будущем')
        return value
