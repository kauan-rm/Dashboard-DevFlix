"""empty message

Revision ID: ef5950791a6a
Revises: 
Create Date: 2022-05-27 19:16:30.426971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef5950791a6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('senha', sa.String(length=64), nullable=False),
    sa.Column('criado_em', sa.DateTime(), nullable=False),
    sa.Column('ativo', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
