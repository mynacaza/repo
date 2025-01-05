from core.config import settings

import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext


async def create_jwt_token(
    data: dict, exp_time: int | None = None, refresh: bool = False
) -> str:


    payload = {}

    payload.update({"sub": data["user_id"]})
    payload.update(
        {
            "exp": datetime.now(timezone.utc)
            + (timedelta(minutes=exp_time if exp_time else settings.jwt.expire))
        }
    )
    payload.update({"refresh": refresh})

    to_encode = jwt.encode(
        payload=payload, key=settings.jwt.secret, algorithm=settings.jwt.algorithm
    )
    return to_encode


async def decode_jwt_token(token) -> dict:
    try:
        to_decode = jwt.decode(
            token, key=settings.jwt.secret, algorithms=[settings.jwt.algorithm]
        )
    except jwt.PyJWTError as e:
        raise e

    return to_decode


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
