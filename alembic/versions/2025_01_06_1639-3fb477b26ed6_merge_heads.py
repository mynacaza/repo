"""Merge heads

Revision ID: 3fb477b26ed6
Revises: a8bfae418611, 6aaa84925875
Create Date: 2025-01-06 16:39:06.828010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fb477b26ed6'
down_revision: Union[str, None] = ('a8bfae418611', '6aaa84925875')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
