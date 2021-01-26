"""Initial migration.

Revision ID: 378f3953f396
Revises: 
Create Date: 2021-01-26 13:22:48.231136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '378f3953f396'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hotel',
    sa.Column('hotel_id', sa.String(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('estrelas', sa.Integer(), nullable=True),
    sa.Column('diaria', sa.Float(precision=2), nullable=True),
    sa.Column('cidade', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('hotel_id')
    )
    op.create_table('usuarios',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=40), nullable=True),
    sa.Column('senha', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    op.drop_table('hotel')
    # ### end Alembic commands ###
