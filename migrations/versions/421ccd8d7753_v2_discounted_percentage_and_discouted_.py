"""V2 discounted_percentage and discouted_price column added to db

Revision ID: 421ccd8d7753
Revises: 6dcc4c33a0f5
Create Date: 2026-07-07 15:28:17.584565

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '421ccd8d7753'
down_revision: Union[str, Sequence[str], None] = '6dcc4c33a0f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
        op.alter_column(
    "products",
    "price",
    new_column_name="original_price"
)
    
        op.add_column(
    "products",
    sa.Column("discount_percentage", sa.Float(), nullable=True)
)

        op.add_column(
    "products",
    sa.Column("discounted_price", sa.Float(), nullable=True)
)
    
        op.execute("""
    UPDATE products
    SET discount_percentage = 10,
        discounted_price = original_price - (original_price * 10 / 100)
    WHERE id = 1;
    """)

        op.execute("""
    UPDATE products
    SET discount_percentage = 20,
        discounted_price = original_price - (original_price * 20 / 100)
    WHERE id = 2;
    """)

        op.execute("""
    UPDATE products
    SET discount_percentage = 15,
        discounted_price = original_price - (original_price * 15 / 100)
    WHERE id = 3;
    """)
              
        op.execute("""
    UPDATE products
    SET discount_percentage = 15,
        discounted_price = original_price - (original_price * 20 / 100)
    WHERE id = 8;
    """)  
    
        op.execute("""
    UPDATE products
    SET discount_percentage = 15,
        discounted_price = original_price - (original_price * 10 / 100)
    WHERE id = 9;
    """)


def downgrade() -> None:
    """Downgrade schema."""
    pass
