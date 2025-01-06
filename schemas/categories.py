from pydantic import BaseModel
from enum import StrEnum

class TypeCategory(StrEnum):
  income = 'Доход'
  expense = 'Расход'

class CategoryModel(BaseModel):
  name: str
  type: TypeCategory
  glob: bool = False