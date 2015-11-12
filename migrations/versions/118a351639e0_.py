"""empty message

Revision ID: 118a351639e0
Revises: f8b7a87b778
Create Date: 2015-11-10 15:42:52.101519

"""

# revision identifiers, used by Alembic.
revision = '118a351639e0'
down_revision = 'f8b7a87b778'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###