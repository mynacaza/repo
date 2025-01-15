from core.config import settings
from database.db_helper import db_helper

from api.utils import create_jwt_token
from api.utils import verify_password
from api.security import get_current_user
from schemas.user import UserCreate, UserLogin, FormResetPassword
from schemas.jwt import TokenInfo
from crud.user import UserService


from fastapi import APIRouter
from fastapi import Form, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

users_router = APIRouter(prefix="/users", tags=["Пользователь"])
user_service = UserService()


@users_router.post("/sign-up")
async def create_account(
    create_user: Annotated[UserCreate, Form()],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    email_in_db = await user_service.get_user_by_email(create_user.email, session)

    if email_in_db:
        raise HTTPException(
            status_code=403, detail="Пользователь с таким email уже зарегистрирован."
        )

    email = await user_service.add_user(create_user, session)

    return {"message": f"Email: {email} успешно зарегистрирован."}


@users_router.post("/login", status_code=200)
async def login(
    user_data: Annotated[UserLogin, Form()],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> TokenInfo:
    email, password = user_data.email, user_data.password

    email_in_db = await user_service.get_user_by_email(email, session)

    if not email_in_db:
        raise HTTPException(
            status_code=404, detail="Пользователь c таким email не зарегистрирован."
        )

    hashed_password = email_in_db.hash_password

    if not verify_password(password, hashed_password):
        raise HTTPException(status_code=403, detail="Пароли не совпадают.")

    user = await user_service.get_user_by_email(email, session)

    access_token = await create_jwt_token({"user_id": str(user.id)})

    return TokenInfo(access_token=access_token)


@users_router.post("/forget-password")
async def forget_password(email: str) -> None:
    token = await create_jwt_token({"email": email}, 10)

    smtp_server, port = settings.smtp.host, settings.smtp.port
    username, password = settings.smtp.user, settings.smtp.password

    message = MIMEMultipart("alternative")
    message["Subject"], message["From"], message["To"] = (
        "Восстановление пароля",
        username,
        email,
    )
    html = f"""
    <html>
        <body>
            <div>
                <p style="margin-bottom: 0px;">
                    Перейдите по <a href="http://127.0.0.1:8000/api/v1/users/forget-password/{token}"> ссылке</a>, чтобы восстановить пароль. Ссылка будет действительна 10 минут.
                </p>
                <p style="margin-top: 0px;">
                    Если вы не запрашивали сбрасывание пароля, то просто проигнорируйте это сообщение.
                </p>
            </div>
        </body> 
    </html>"""

    message.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(message)
        print("Письмо успешно отправлено")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")


@users_router.post("/forget-password/{token}")
async def reset_password(
    token: str, reset_password: Annotated[FormResetPassword, Form()]
) -> None:
    # нужен фронт
    # редирект если пользователь активен
    pass
