"""add foreign-key to posts table

Revision ID: f1393970f040
Revises: 36bfde7137b4
Create Date: 2024-01-31 08:27:07.773093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1393970f040'
down_revision: Union[str, None] = '36bfde7137b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# aceasta am creat-o folosind comanda alembic revision -m "add foreign-key to posts table" - to implement realtionship between users and posts
def upgrade() -> None:
# add a column to the posts table called owner id that will hold the foreign-key constarins
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
# set the link between two tables that will hold the foreign key
# posts_users_fk-numele foreignkey(between the posts and users table) dat de mine/ source_table="posts" -the foreignkey for the posts table/ referent_table="users"-the remote or refrent table/
#  local_cols=['owner_id']-the local colum that we will be using is the column that we just createt in posts table/ remote_cols=['id']-pecify the remote column in the users table, the id field of the user table
# ondelete-CASCADE- if we delete a record in the parent table then the corresponding record in the child table will be automatically deleted as well
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass

# to undo the changes above
def downgrade() -> None:
# 'posts_users_fk' - numele constraintului pe care vrem sa il stergem, table_name=posts-numele tabelului din care stergem 
    op.drop_constraint('posts_users_fk', table_name="posts")
# drop the column from the 'posts' tabel, and the column we want to drops its called 'owner_id'
    op.drop_column('posts', 'owner_id')
    pass
# dupa ce scriu totul de sus in terminal scriu comenzile 'alembic current' sa vad in ce curent revision sunt/ alembic heads- sa vad ultimul revision creat/ alembic upgrade head- sa vad comanda de upgrade si freign key add
# dupa verifc in pgAdmin modificarile la posts table + properties + constraints si tre sa fie 'posts_users_fk'