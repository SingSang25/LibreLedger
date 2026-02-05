"""seed currencies

Revision ID: da467a25fe7f
Revises: c5a1f06963d7
Create Date: 2026-02-05 22:57:55.465335

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "da467a25fe7f"
down_revision: Union[str, Sequence[str], None] = "c5a1f06963d7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
        """
        INSERT INTO currencies (code, name, symbol, minor_units, is_active)
        VALUES
          ('EUR', 'Euro', '€', 2, true),
          ('USD', 'US Dollar', '$', 2, true),
          ('CHF', 'Swiss Franc', 'CHF', 2, true)
        ON CONFLICT (code) DO NOTHING;
    """
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM currencies WHERE code IN ('EUR','USD','CHF')")
