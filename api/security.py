from .utils import decode_jwt_token

from fastapi.security import HTTPBearer
from fastapi.requests import Request
from fastapi import HTTPException, Depends


class BearerToken(HTTPBearer):
    async def __call__(self, request: Request) -> dict:
        token_info = await super().__call__(request)

        token = token_info.credentials

        decoded_token = await decode_jwt_token(token)
        self.verify_token(decoded_token)

        return decoded_token

    def verify_token(self, decoded_token: dict) -> None:
        raise NotImplementedError(
            "Метод verify_token должен быть реализован в подклассе."
        )


class AccessTokenBearer(BearerToken):
    def verify_token(self, data: dict) -> None:
        if data.get("refresh") == True:
            raise HTTPException(status_code=403, detail="Предоставьте access токен")


async def get_current_user(
    token: AccessTokenBearer = Depends(AccessTokenBearer()),
) -> dict:
    return token
