"""create simple_people table

Revision ID: f0546da1550d
Revises:
Create Date: 2024-12-12 20:19:35.532198

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f0546da1550d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "simple_people",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("age", sa.Integer),
        sa.Column("bio", sa.String(2000)),
    )


def downgrade() -> None:
    op.drop_table("simple_people")
