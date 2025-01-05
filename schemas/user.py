from pydantic import BaseModel, model_validator, EmailStr

from typing import Self


class UserRead(BaseModel):
    email: EmailStr


class UserCreate(UserRead):
    password: str


class FormResetPassword(BaseModel):
    password: str
    password_repeat: str

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Пароли не совпадают.")
        return self
