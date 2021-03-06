"""activation_request_time

Revision ID: 15abfd03de3e
Revises: None
Create Date: 2014-10-15 22:15:27.945705

"""

# revision identifiers, used by Alembic.
revision = '15abfd03de3e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('activation_request_time', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'activation_request_time')
    ### end Alembic commands ###
