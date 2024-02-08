"""add content column to posts table

Revision ID: 5f245e715f84
Revises: c5dc387486fc
Create Date: 2024-01-30 13:29:39.893246

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f245e715f84'
down_revision: Union[str, None] = 'c5dc387486fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
# adding a new column, in paranteza prima e numele tabelului pe care il modificam, urmeaza numele coloanei e care o adaugam, tipul de variabila, nullable=False-adica trebuie sa fie neaparat completata
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass
# defiecare data cind setam upgrade function, trebuie sa setam si downgrade function- neaparat.

def downgrade() -> None:
    op.drop_column('posts', 'content') #numele tabelului si coloana pe care vrem sa o stergem
    pass
