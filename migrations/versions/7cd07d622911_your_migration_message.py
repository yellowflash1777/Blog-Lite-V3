"""Your migration message

Revision ID: 7cd07d622911
Revises: 
Create Date: 2023-04-02 15:11:51.284123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cd07d622911'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)

    with op.batch_alter_table('follows', schema=None) as batch_op:
        batch_op.alter_column('follower_user_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('followed_user_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)

    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    with op.batch_alter_table('follows', schema=None) as batch_op:
        batch_op.alter_column('followed_user_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
        batch_op.alter_column('follower_user_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    # ### end Alembic commands ###
