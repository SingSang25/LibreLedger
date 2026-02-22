from __future__ import annotations

import pytest

from datetime import date


@pytest.mark.parametrize(
    "payload",
    [
        {
            "name": "N" * 64,
            "description": "D" * 256,
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "base_currency_id": 1,
        },
        {
            "name": "Y" * 64,
            "description": None,
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "base_currency_id": 1,
        },
    ],
)
def test_put_fiscal_year_returns_200(client, get_fiscal_year_uuid_for_test, payload):
    response = client.put(
        f"/api/v1/fiscal_year/{get_fiscal_year_uuid_for_test}", json=payload
    )
    assert response.status_code == 200

    data = response.json()

    # Assertions validating response_model
    assert isinstance(data, dict)

    # Required keys (exclude=True fields are not asserted)
    assert "uuid" in data
    assert "name" in data
    assert "description" in data
    assert "start_date" in data
    assert "end_date" in data
    assert "base_currency_code" in data

    # Basic types
    assert isinstance(data["uuid"], str)
    assert isinstance(data["name"], str)
    assert (data["description"] is None) or isinstance(data["description"], str)
    assert isinstance(data["base_currency_code"], str)

    # ISO date parseability
    date.fromisoformat(data["start_date"])
    date.fromisoformat(data["end_date"])


def test_put_fiscal_year_returns_404(client):
    payload = {
        "name": "Y" * 64,
        "description": "D" * 256,
        "start_date": "2026-01-01",
        "end_date": "2026-12-31",
        "base_currency_id": 1,
    }
    response = client.put(
        "/api/v1/fiscal_year/ffffffff-ffff-ffff-ffff-ffffffffffff", json=payload
    )
    assert response.status_code == 404

    data = response.json()

    # Assertions validating response_model
    assert isinstance(data, dict)


@pytest.mark.parametrize(
    "payload",
    [
        {
            # Too long name
            "name": "N" * 65,
            "description": "D" * 256,
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "base_currency_id": 1,
        },
        {
            # Too long description
            "name": "Y" * 64,
            "description": "D" * 257,
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "base_currency_id": 1,
        },
        {
            # No name
            "description": "D" * 256,
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "base_currency_id": 1,
        },
        {
            # No base_currency_id
            "name": "Y" * 64,
            "description": "D" * 256,
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
        },
        {
            # Invalid base_currency_id
            "name": "Y" * 64,
            "description": "D" * 256,
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "base_currency_id": "a",
        },
        {
            # No end_date
            "name": "Y" * 64,
            "description": "D" * 256,
            "start_date": "2026-01-01",
            "base_currency_id": 1,
        },
        {
            # No start_date
            "name": "Y" * 64,
            "description": "D" * 256,
            "end_date": "2026-12-31",
            "base_currency_id": 1,
        },
        {
            # Invalid date range
            "name": "FY Invalid Range",
            "description": None,
            "start_date": "2026-12-31",
            "end_date": "2026-01-01",
            "base_currency_id": 1,
        },
    ],
)
def test_put_fiscal_year_returns_422(client, get_fiscal_year_uuid_for_test, payload):
    response = client.put(
        f"/api/v1/fiscal_year/{get_fiscal_year_uuid_for_test}", json=payload
    )
    assert response.status_code == 422

    data = response.json()

    # Assertions validating response_model
    assert isinstance(data, dict)


def test_put_fiscal_year_returns_500(
    client, get_fiscal_year_uuid_for_test, monkeypatch
):

    def raise_error():
        raise RuntimeError("Boom")

    monkeypatch.setattr(
        "src.router.fiscal_year.fiscal_year_uuid.update_fiscal_year_service",
        raise_error,
    )

    payload = {
        "name": "Y" * 64,
        "description": "D" * 256,
        "start_date": "2026-01-01",
        "end_date": "2026-12-31",
        "base_currency_id": 1,
    }
    response = client.put(
        f"/api/v1/fiscal_year/{get_fiscal_year_uuid_for_test}", json=payload
    )
    assert response.status_code == 500
    assert "Internal Server Error" in response.text
