"""empty message

Revision ID: 512bd45f4b23
Revises: 1df363a81175
Create Date: 2020-05-22 00:12:04.834542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '512bd45f4b23'
down_revision = '1df363a81175'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('address', 'coords')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('coords', sa.NUMERIC(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###