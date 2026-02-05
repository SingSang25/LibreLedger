"""Model registration for SQLAlchemy class registry.

Importing this package ensures all model modules are loaded so string-based
relationship() targets resolve correctly.
"""

from src.models import currency  # noqa: F401
from src.models import entry  # noqa: F401
from src.models import fiscal_year  # noqa: F401
from src.models import ledger_account  # noqa: F401
from src.models import ledger_account_budget  # noqa: F401
from src.models import transaction  # noqa: F401
