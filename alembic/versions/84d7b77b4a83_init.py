"""Init

Revision ID: 84d7b77b4a83
Revises: 
Create Date: 2024-04-24 09:47:40.679948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84d7b77b4a83'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_localization',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('about', sa.String(), nullable=False),
    sa.Column('banner_filename', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('money',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('currency', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sport',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sport_localization',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('event_localization_id', sa.Uuid(), nullable=False),
    sa.Column('postal_code', sa.String(), nullable=False),
    sa.Column('country', sa.String(length=2), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('line', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['event_localization_id'], ['event_localization.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('event_localization_id')
    )
    op.create_table('article',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('event_localization_id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['event_localization_id'], ['event_localization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('registration_start_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('registration_end_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('participation_start_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('participation_end_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('minimal_age', sa.Integer(), nullable=False),
    sa.Column('sport_id', sa.Uuid(), nullable=False),
    sa.Column('organizer_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['sport_id'], ['sport.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sport_localization_association',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('sport_id', sa.Uuid(), nullable=False),
    sa.Column('sport_localization_id', sa.Uuid(), nullable=False),
    sa.Column('language', sa.String(length=2), nullable=False),
    sa.ForeignKeyConstraint(['sport_id'], ['sport.id'], ),
    sa.ForeignKeyConstraint(['sport_localization_id'], ['sport_localization.id'], ),
    sa.PrimaryKeyConstraint('id', 'sport_id', 'sport_localization_id')
    )
    op.create_table('starter_item',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('event_localization_id', sa.Uuid(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['event_localization_id'], ['event_localization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket_localization',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('extra_title', sa.String(), nullable=False),
    sa.Column('price_id', sa.Uuid(), nullable=False),
    sa.ForeignKeyConstraint(['price_id'], ['money.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('document',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('event_id', sa.Uuid(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('event_id', 'title')
    )
    op.create_table('event_traslation_association',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('event_id', sa.Uuid(), nullable=False),
    sa.Column('event_localization_id', sa.Uuid(), nullable=False),
    sa.Column('language', sa.String(length=2), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['event_localization_id'], ['event_localization.id'], ),
    sa.PrimaryKeyConstraint('id', 'event_id', 'event_localization_id')
    )
    op.create_table('social_link',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('event_id', sa.Uuid(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('event_id', sa.Uuid(), nullable=False),
    sa.Column('max_places', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket_localization_assiciation',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('ticket_id', sa.Uuid(), nullable=False),
    sa.Column('ticket_localization_id', sa.Uuid(), nullable=False),
    sa.Column('language', sa.String(length=2), nullable=False),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.ForeignKeyConstraint(['ticket_localization_id'], ['ticket_localization.id'], ),
    sa.PrimaryKeyConstraint('id', 'ticket_id', 'ticket_localization_id')
    )
    op.create_table('ticket_registation',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('ticket_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('serial_number', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket_registation')
    op.drop_table('ticket_localization_assiciation')
    op.drop_table('ticket')
    op.drop_table('social_link')
    op.drop_table('event_traslation_association')
    op.drop_table('document')
    op.drop_table('ticket_localization')
    op.drop_table('starter_item')
    op.drop_table('sport_localization_association')
    op.drop_table('event')
    op.drop_table('article')
    op.drop_table('address')
    op.drop_table('sport_localization')
    op.drop_table('sport')
    op.drop_table('money')
    op.drop_table('event_localization')
    # ### end Alembic commands ###
