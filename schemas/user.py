from pydantic import BaseModel, EmailStr


class UserRead(BaseModel):
    email: EmailStr


class UserCreate(UserRead):
    password: str
