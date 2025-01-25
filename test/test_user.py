
import httpx
import pytest


print('ку')

@pytest.mark.asyncio
async def test_sign_up(client: httpx.AsyncClient):
  registration_data = {
    'test@test.com',
    'password'
    }
  
  
  response = await client.post('/sign_up', json=registration_data)
  assert response.status_code == 201
