"""Initial migration.

Revision ID: 3067e0d47987
Revises: 
Create Date: 2021-04-27 15:22:28.858183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3067e0d47987'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('films')
    # ### end Alembic commands ###
