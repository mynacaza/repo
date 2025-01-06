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
        return f"email: {self.email!r}"


class Category(MixinId):
    __tablename__ = "categories"

    operation_type: Mapped[str]
    name: Mapped[str]
    parent_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=True)

    is_default: Mapped[bool] = mapped_column(default=False) 

    def __repr__(self):
        return f"operation_type: {self.operation_type!r}, transaction: {self.transaction!r}"


class Transaction(MixinId, TimestampMixin):
    __tablename__ = "transactions"

    amount: Mapped[int]
    comment: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="transaction")

    def __repr__(self):
        return f"amount: {self.amount!r}, user_id: {self.user_id!r}, category: {self.caregory_id!r}"

