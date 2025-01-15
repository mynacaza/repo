from .mixins import MixinId, TimestampMixin

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import false
from sqlalchemy import UniqueConstraint
from sqlalchemy import ForeignKey

from typing import List


class User(MixinId):
    __tablename__ = "users"

    email: Mapped[str]
    hash_password: Mapped[str]

    transaction: Mapped[List["Transaction"]] = relationship(back_populates="user")
    __table_args__ = {"extend_existing": True}

    def __repr__(self):
        return f"email: {self.email!r}"


class Transaction(MixinId, TimestampMixin):
    __tablename__ = "transactions"

    amount: Mapped[int]
    comment: Mapped[str] = mapped_column(nullable=False, default="")
    operation_type: Mapped[str]
    category_name: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="transaction")
    __table_args__ = {"extend_existing": True}

    def __repr__(self):
        return f"amount: {self.amount!r}, user_id: {self.user_id!r}"
