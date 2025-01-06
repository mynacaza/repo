from datetime import datetime
from sqlalchemy import func, Date
from database.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column


class MixinId(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)


class TimestampMixin(Base):
    __abstract__ = True

    date: Mapped[datetime.date] = mapped_column(
        Date, server_default=func.current_date()
    )
