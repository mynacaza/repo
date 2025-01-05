from .mixins import MixinId, TimestampMixin

from sqlalchemy.orm import Mapped

class User(MixinId):
    __tablename__ = "users"

    email: Mapped[str]
    hash_password: Mapped[str]

    def __repr__(self):
        return "email: {self.email!r}"


class Category(MixinId):
    __tablename__ = "categories"
    
    operation_type: Mapped[str]


