"""add-annotation-reply

Revision ID: e1901f623fd0
Revises: fca025d3b60f
Create Date: 2023-12-12 06:58:41.054544

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e1901f623fd0'
down_revision = 'fca025d3b60f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_annotation_hit_histories',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('app_id', postgresql.UUID(), nullable=False),
    sa.Column('annotation_id', postgresql.UUID(), nullable=False),
    sa.Column('source', sa.Text(), nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('account_id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP(0)'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='app_annotation_hit_histories_pkey')
    )
    with op.batch_alter_table('app_annotation_hit_histories', schema=None) as batch_op:
        batch_op.create_index('app_annotation_hit_histories_account_idx', ['account_id'], unique=False)
        batch_op.create_index('app_annotation_hit_histories_annotation_idx', ['annotation_id'], unique=False)
        batch_op.create_index('app_annotation_hit_histories_app_idx', ['app_id'], unique=False)

    with op.batch_alter_table('app_model_configs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('annotation_reply', sa.Text(), nullable=True))

    with op.batch_alter_table('dataset_collection_bindings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(length=40), server_default=sa.text("'dataset'::character varying"), nullable=False))

    with op.batch_alter_table('message_annotations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('hit_count', sa.Integer(), server_default=sa.text('0'), nullable=False))
        batch_op.alter_column('conversation_id',
               existing_type=postgresql.UUID(),
               nullable=True)
        batch_op.alter_column('message_id',
               existing_type=postgresql.UUID(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message_annotations', schema=None) as batch_op:
        batch_op.alter_column('message_id',
               existing_type=postgresql.UUID(),
               nullable=False)
        batch_op.alter_column('conversation_id',
               existing_type=postgresql.UUID(),
               nullable=False)
        batch_op.drop_column('hit_count')
        batch_op.drop_column('question')

    with op.batch_alter_table('dataset_collection_bindings', schema=None) as batch_op:
        batch_op.drop_column('type')

    with op.batch_alter_table('app_model_configs', schema=None) as batch_op:
        batch_op.drop_column('annotation_reply')

    with op.batch_alter_table('app_annotation_hit_histories', schema=None) as batch_op:
        batch_op.drop_index('app_annotation_hit_histories_app_idx')
        batch_op.drop_index('app_annotation_hit_histories_annotation_idx')
        batch_op.drop_index('app_annotation_hit_histories_account_idx')

    op.drop_table('app_annotation_hit_histories')
    # ### end Alembic commands ###