from datetime import datetime
from sqlalchemy import func
from database.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column


class MixinId(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)


class TimestampMixin(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
