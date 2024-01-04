"""initial

Revision ID: f94624fbef77
Revises: 
Create Date: 2024-01-04 14:30:44.484619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f94624fbef77'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "students" , 
        sa.Column("ID" , sa.Integer , primary_key= True) , 
        sa.Column("name" , sa.String(50) , nullable=False) , 
        sa.Column("mail" , sa.String(50) , unique= True)
    )


def downgrade() -> None:
    op.drop_table("students")
