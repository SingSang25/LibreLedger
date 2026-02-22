from __future__ import annotations

from datetime import date


def test_get_fiscal_year_returns_200(client, get_fiscal_year_uuid_for_test):
    response = client.get(f"/api/v1/fiscal_year/{get_fiscal_year_uuid_for_test}")
    assert response.status_code == 200

    data = response.json()

    # Assertions validating response_model
    assert isinstance(data, dict)

    # Required keys (exclude=True fields are not asserted)
    assert "uuid" in data
    assert "name" in data
    assert "start_date" in data
    assert "end_date" in data
    assert "base_currency_code" in data

    # Basic types
    assert isinstance(data["uuid"], str)
    assert isinstance(data["name"], str)
    assert isinstance(data["base_currency_code"], str)

    if "description" in data:
        assert data["description"] is None or isinstance(data["description"], str)

    # Date parseability
    assert isinstance(data["start_date"], str)
    assert isinstance(data["end_date"], str)
    date.fromisoformat(data["start_date"])
    date.fromisoformat(data["end_date"])


def test_get_fiscal_year_returns_404(client):
    response = client.get("/api/v1/fiscal_year/ffffffff-ffff-ffff-ffff-ffffffffffff")
    assert response.status_code == 404

    data = response.json()

    # Assertions validating error response shape
    assert isinstance(data, dict)
    assert "detail" in data
    assert isinstance(data["detail"], (str, dict, list))


def test_get_fiscal_year_returns_422(client):
    response = client.get("/api/v1/fiscal_year/not-a-uuid")
    assert response.status_code == 422

    data = response.json()

    # Assertions validating error response shape
    assert isinstance(data, dict)
    assert "detail" in data
    assert isinstance(data["detail"], list)


def test_get_fiscal_year_returns_500(client, monkeypatch):
    def raise_error():
        raise RuntimeError("Boom")

    monkeypatch.setattr(
        "src.router.fiscal_year.fiscal_year_uuid.get_fiscal_year_by_uuid",
        raise_error,
    )

    response = client.get("/api/v1/fiscal_year/ffffffff-ffff-ffff-ffff-ffffffffffff")
    assert response.status_code == 500
    assert "Internal Server Error" in response.text
