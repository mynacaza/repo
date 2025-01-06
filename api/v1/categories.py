from fastapi import APIRouter



category_router = APIRouter(prefix="/categories", tags=["Категории"])


@category_router.post('/')
async def create_category():
  pass

@category_router.put('/{category_id}')
async def change_category(category_id):
  pass

@category_router.delete('/{category_id}')
async def delete_category(category_id):
  pass