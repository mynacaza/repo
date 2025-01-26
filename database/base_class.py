from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    modified_ad: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
