import os
import secrets
import string
import pytest

from alembic import command
from alembic.config import Config
from dotenv import load_dotenv
from datetime import date, timedelta
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from src.main import app
from src.database.dependencies import get_db
from src.models.currency import Currency
from src.models.fiscal_year import FiscalYear

load_dotenv(".env.test", override=True)

# --- Test database ---
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")

SQLALCHEMY_TEST_DATABASE_URL = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# --- Override get_db dependency ---
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- Helpers ---
def generate_random_date() -> date:
    return date.today() + timedelta(days=secrets.randbelow(365 * 5))


def generate_random_string(length: int = 10) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def get_random_currency_id(db: Session) -> int:
    return db.query(Currency).first().id


@pytest.fixture()
def get_fiscal_year_uuid_for_test() -> str:
    db = TestingSessionLocal()
    data = db.query(FiscalYear).first().uuid
    db.close()
    return str(data)


# --- Pytest fixtures ---


@pytest.fixture(scope="session")
def setup_database():
    """
    Reset schema, run Alembic migrations once for the whole test session.
    """
    # Clean schema (Postgres)
    with engine.begin() as conn:
        conn.execute(text("DROP SCHEMA IF EXISTS public CASCADE;"))
        conn.execute(text("CREATE SCHEMA public;"))

    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", SQLALCHEMY_TEST_DATABASE_URL)

    command.upgrade(alembic_cfg, "head")

    yield

    with engine.begin() as conn:
        conn.execute(text("DROP SCHEMA IF EXISTS public CASCADE;"))
        conn.execute(text("CREATE SCHEMA public;"))

    engine.dispose()


@pytest.fixture(scope="function", autouse=True)
def generate_random_fiscal_year(setup_database):
    """
    Insert one FiscalYear for the whole test session.
    Ensures migrations ran before seeding.
    """
    db = TestingSessionLocal()
    try:
        for i in range(10):
            random_date = generate_random_date()
            payload = FiscalYear(
                name=f"{generate_random_string(10)}_{i}",
                description=f"{generate_random_string(20)}_{i}",
                start_date=random_date,
                end_date=random_date + timedelta(days=365),
                base_currency_id=get_random_currency_id(db),
            )

            db.add(payload)
            db.commit()
    finally:
        db.close()


@pytest.fixture()
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
    app.dependency_overrides.clear()
