import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException

SECRET = 'vvvvvvvvvvvvvvv'
ALGORITHM = 'HS256'
AccessTokenExpire = 15

async def create_jwt_token(data: dict, exp_time: int | None = None, refresh: bool = False) -> str:
  payload = {}

  payload.update({"sub": data['email']})
  payload.update({"exp": datetime.now(timezone.utc) + (timedelta(minutes=exp_time if exp_time else AccessTokenExpire))})
  payload.update({"refresh": refresh})

  to_encode = jwt.encode(payload=payload, key=SECRET, algorithm=ALGORITHM)
  return to_encode


async def decode_jwt_token(token):
  print(token)
  try:
    to_decode = jwt.decode(token, key=SECRET, algorithms=[ALGORITHM])
  except jwt.PyJWTError as e:
      raise e
  
  return to_decode