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
def test_post_fiscal_year_returns_200(client, payload):
    response = client.post(
        "/api/v1/fiscal_year",
        json=payload,
    )
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)

    # Assertions validating response_model
    assert "uuid" in data
    assert "name" in data
    assert "description" in data
    assert "start_date" in data
    assert "end_date" in data
    assert "base_currency_code" in data

    assert isinstance(data["uuid"], str)
    assert isinstance(data["name"], str)
    assert (data["description"] is None) or isinstance(data["description"], str)
    assert isinstance(data["base_currency_code"], str)

    assert isinstance(data["start_date"], str)
    assert isinstance(data["end_date"], str)
    date.fromisoformat(data["start_date"])
    date.fromisoformat(data["end_date"])


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
def test_post_fiscal_year_returns_422(client, payload):
    response = client.post(
        "/api/v1/fiscal_year",
        json=payload,
    )
    assert response.status_code == 422

    data = response.json()
    assert isinstance(data, dict)
    assert "detail" in data


def test_post_fiscal_year_returns_500(client, monkeypatch):

    def raise_error(db):
        raise RuntimeError("Boom")

    monkeypatch.setattr(
        "src.router.fiscal_year.router.create_fiscal_year_service",
        raise_error,
    )

    response = client.post(
        "/api/v1/fiscal_year",
        json={
            "name": "N" * 64,
            "description": "D" * 256,
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "base_currency_id": 1,
        },
    )
    assert response.status_code == 500
    assert "Internal Server Error" in response.text
