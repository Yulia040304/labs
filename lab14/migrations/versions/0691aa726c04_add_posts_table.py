"""Add posts table.

Revision ID: 0691aa726c04
Revises: 8b54af7f3ee6
Create Date: 2023-11-26 22:52:23.476605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0691aa726c04'
down_revision = '8b54af7f3ee6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('text', sa.String(length=750), nullable=True),
    sa.Column('image', sa.String(length=50), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('postType', sa.Enum('SPORT', 'NEWS', 'MEMES', 'PUBLICATION', 'OTHER', name='posttypes'), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
