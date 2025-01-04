from database.base_class import Base
from .mixins import MixinId, TimestampMixin

from sqlalchemy.orm import Mapped, mapped_column


class User(MixinId, TimestampMixin):
    __tablename__ = "users"

    email: Mapped[str]
    hash_password: Mapped[str]

    def __repr__(self):
        return "email: {self.email!r}"
