"""add asdf column on simple_people

Revision ID: aa1003e490d3
Revises: 37cf0eb7e9d9
Create Date: 2024-12-13 18:24:09.898054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa1003e490d3'
down_revision = '37cf0eb7e9d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('simple_people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('asdf', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('simple_people', schema=None) as batch_op:
        batch_op.drop_column('asdf')

    # ### end Alembic commands ###
