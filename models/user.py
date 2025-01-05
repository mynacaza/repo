from .mixins import MixinId, TimestampMixin

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from typing import List


class User(MixinId):
    __tablename__ = "users"

    email: Mapped[str]
    hash_password: Mapped[str]
    transaction: Mapped[List["Transaction"]] = relationship(back_populates="user")

    def __repr__(self):
        return "email: {self.email!r}"


class Category(MixinId):
    __tablename__ = "categories"

    operation_type: Mapped[str]
    transaction: Mapped["Transaction"] = relationship(back_populates="category")


class Transaction(MixinId, TimestampMixin):
    __tablename__ = "transactions"

    amount: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    caregory_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    user: Mapped["User"] = relationship(back_populates="transaction")
    category: Mapped["Category"] = relationship(back_populates="transaction")
