"""add last few columns to posts table

Revision ID: 8fd0f9665c58
Revises: f1393970f040
Create Date: 2024-01-31 09:02:42.375288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fd0f9665c58'
down_revision: Union[str, None] = 'f1393970f040'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True')) # server_default='True'- if we dont provide the server default then it will be true
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

# dupa scriu alembic upgrade +1 sa vad modificarile de upgrade-adica ca s-a creat columnurile si verific in pgAdmin - refresh posts table+properties+columns sa vedem columnurile
# alembic downgrade + nr revisionului ca sa stergem orice colum vrem in functie de nr revision
#   Important: nr revisionului este in foecare file / Aceasta informatie este la min 11:08

