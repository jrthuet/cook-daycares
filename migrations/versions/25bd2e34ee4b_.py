"""empty message

Revision ID: 25bd2e34ee4b
Revises: ca4aceeab91e
Create Date: 2020-05-21 20:30:23.210030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25bd2e34ee4b'
down_revision = 'ca4aceeab91e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tr_geoid', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=180), nullable=True),
    sa.Column('census_tract', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('logitude', sa.Float(), nullable=True),
    sa.Column('requested_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    # ### end Alembic commands ###
