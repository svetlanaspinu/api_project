"""create posts table

Revision ID: c5dc387486fc
Revises: 
Create Date: 2024-01-29 21:39:33.271248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5dc387486fc'
down_revision: Union[str, None] = None 
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Toate comenzile pentru a lucra cu tabelele sun t pe site-ul alembic.sqlalchemy.org + documentation + API details + DDL internals = toate comenzile sunt aici
# this function runs the commands for making the changes we want to do
def upgrade() -> None:
# accessing the op from alembic and create tabel/ in ghilimeme numele tabeluilui 'posts', define columns sa.Colums - grabing the sqlalchemy as sa  object
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False))   # cind nullable=False inseamna ca e required
    pass

# if we want to make some changes for the tables that we created in function above(to roll back) le scrim in functia de mai jos/ aici si stergem daca am scris ceva gresit
def downgrade() -> None:
# to delete the table that we have created above/
    op.drop_table('posts')
    pass
# dupa ce am scris comenzile de sus in alembic --help   verific comenzile care pot sa fac 
# dupa scriu in terminal alembic upgrade c5dc387486fc (codul acesta este revision) si ar trebui sa creeze tabele in PgAdmin