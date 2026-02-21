from __future__ import annotations

from datetime import date


def test_get_fiscal_year_returns_200(client):
    response = client.get("/api/v1/fiscal_year")
    assert response.status_code == 200

    data = response.json()

    # Assertions validating response_model
    assert isinstance(data, list)

    for item in data:
        assert isinstance(item, dict)

        # Required keys from response_model (excluding exclude=True fields)
        assert "uuid" in item
        assert "name" in item
        assert "start_date" in item
        assert "end_date" in item
        assert "base_currency_code" in item

        # Basic types
        assert isinstance(item["uuid"], str)
        assert isinstance(item["name"], str)
        assert isinstance(item["base_currency_code"], str)

        assert isinstance(item["start_date"], str)
        assert isinstance(item["end_date"], str)

        # Optional fields
        if "description" in item:
            assert item["description"] is None or isinstance(item["description"], str)

        # ISO date parseability
        date.fromisoformat(item["start_date"])
        date.fromisoformat(item["end_date"])


def test_get_fiscal_year_returns_500(client, monkeypatch):
    def raise_error(db):
        raise RuntimeError("Boom")

    monkeypatch.setattr(
        "src.router.fiscal_year.router.get_fiscal_years_service",
        raise_error,
    )

    response = client.get("/api/v1/fiscal_year")
    assert response.status_code == 500
    assert "Internal Server Error" in response.text
