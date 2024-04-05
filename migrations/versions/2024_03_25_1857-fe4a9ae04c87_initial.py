"""initial

Revision ID: fe4a9ae04c87
Revises: 64ec9a0a8787
Create Date: 2024-03-25 18:57:48.560521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fe4a9ae04c87'
down_revision: Union[str, None] = '64ec9a0a8787'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trip')
    op.drop_table('driver')
    op.alter_column('user', 'group',
               existing_type=sa.CHAR(length=10),
               type_=sa.String(length=10),
               existing_nullable=False)
    op.create_index(op.f('ix_user_first_name'), 'user', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_group'), 'user', ['group'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=False)
    op.create_index(op.f('ix_user_patronymic'), 'user', ['patronymic'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_patronymic'), table_name='user')
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_group'), table_name='user')
    op.drop_index(op.f('ix_user_first_name'), table_name='user')
    op.alter_column('user', 'group',
               existing_type=sa.String(length=10),
               type_=sa.CHAR(length=10),
               existing_nullable=False)
    # ### end Alembic commands ###
