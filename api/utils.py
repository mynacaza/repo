import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from passlib.context import CryptContext

SECRET = "vvvvvvvvvvvvvvv"
ALGORITHM = "HS256"
AccessTokenExpire = 15


async def create_jwt_token(
    data: dict, exp_time: int | None = None, refresh: bool = False
) -> str:
    payload = {}

    payload.update({"sub": data["email"]})
    payload.update(
        {
            "exp": datetime.now(timezone.utc)
            + (timedelta(minutes=exp_time if exp_time else AccessTokenExpire))
        }
    )
    payload.update({"refresh": refresh})

    to_encode = jwt.encode(payload=payload, key=SECRET, algorithm=ALGORITHM)
    return to_encode


async def decode_jwt_token(token):
    try:
        to_decode = jwt.decode(token, key=SECRET, algorithms=[ALGORITHM])
    except jwt.PyJWTError as e:
        raise e

    return to_decode


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
