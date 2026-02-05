poetry run alembic -c apps/backend/alembic.ini revision --autogenerate -m "create initial tables"
poetry run alembic -c apps/backend/alembic.ini upgrade head
poetry run alembic -c apps/backend/alembic.ini revision -m "seed currencies"
poetry run alembic -c apps/backend/alembic.ini upgrade head
