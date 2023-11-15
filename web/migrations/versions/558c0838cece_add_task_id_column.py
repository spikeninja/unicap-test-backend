"""Add task_id column

Revision ID: 558c0838cece
Revises: d3f7a23316dd
Create Date: 2023-11-15 00:17:45.865546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '558c0838cece'
down_revision: Union[str, None] = 'd3f7a23316dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """"""
    op.add_column('pages', sa.Column('task_id', sa.String(length=36), nullable=True))


def downgrade() -> None:
    op.drop_column('pages', 'task_id')
