"""add user table

Revision ID: 36bfde7137b4
Revises: 5f245e715f84
Create Date: 2024-01-30 14:13:10.872921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36bfde7137b4'
down_revision: Union[str, None] = '5f245e715f84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
# toate asta sunt specificate si la models.py class user
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'), # aceasta se poate de scris si la prima linie-id (primaryKey=true) ca sa o setam ca primary key sau se poate de notat aici ca ptimarykeyconstarin
    sa.UniqueConstraint('email')) # uniqueconstraint for emails not to have dupplicate emails
    pass
# in terminal sa mai scriu alembic current sa vad in ce revision(file) sunt sau revision history pt a vedea istoria revisiunilor

def downgrade() -> None:
    op.drop_table('users')
    pass
