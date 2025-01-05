from pydantic import BaseModel


class TokenInfo(BaseModel):
    type: str = "Bearer"
    access_token: str
    refresh_token: str | None = None
