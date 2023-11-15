"""INITIAL MIGRATION

Revision ID: d3f7a23316dd
Revises: 
Create Date: 2023-11-15 00:09:15.691550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3f7a23316dd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """"""
    op.create_table('pages',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('page_url', sa.String(length=128), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    op.create_table('products',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=256), nullable=True),
        sa.Column('price', sa.String(length=128), nullable=True),
        sa.Column('state', sa.String(length=128), nullable=True),
        sa.Column('location', sa.String(length=256), nullable=True),
        sa.Column('image_src', sa.String(length=512), nullable=True),
        sa.Column('product_url', sa.String(length=512), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('page_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['page_id'], ['pages.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """"""
    op.drop_table('products')
    op.drop_table('users')
    op.drop_table('pages')
