"""change table name

Revision ID: e5b47b081321
Revises: 3067e0d47987
Create Date: 2021-04-27 15:36:55.372757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5b47b081321'
down_revision = '3067e0d47987'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('films')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=120), nullable=False),
    sa.Column('completed', sa.BOOLEAN(), nullable=True),
    sa.Column('timestamp', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('todos')
    # ### end Alembic commands ###