from schemas.user import UserCreate
from crud.user import UserService
from api.utils import create_jwt_token, decode_jwt_token
from database.db_helper import db_helper
from core.config import settings

from fastapi import APIRouter
from fastapi import Form, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

users_router = APIRouter(prefix="/users", tags=["Пользователь"])
user_service = UserService()


@users_router.post("/create-account")
async def get_token(
    create_user: Annotated[UserCreate, Form()],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    email_in_db = await user_service.get_user_by_email(create_user.email, session)

    if email_in_db:
        raise HTTPException(
            status_code=403, detail="Пользователь с таким email уже зарегистрирован."
        )

    email = await user_service.add_user(create_user, session)
    access_token = await create_jwt_token({"email": email})

    return access_token


@users_router.post("/forget-password")
async def forget_password(email: str):
    token = await create_jwt_token({'email': email}, 10)

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
async def reset_password(token: str):
    # метод недоступен, нужен фронт
    pass