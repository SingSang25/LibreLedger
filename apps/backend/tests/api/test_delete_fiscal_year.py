from __future__ import annotations


def test_delete_fiscal_year_returns_200(client, get_fiscal_year_uuid_for_test):
    response = client.delete(f"/api/v1/fiscal_year/{get_fiscal_year_uuid_for_test}")
    assert response.status_code == 200

    data = response.json()

    # Assertions validating response_model
    assert isinstance(data, dict)
    assert "id" in data
    assert "message" in data
    assert "status" in data

    assert isinstance(data["id"], str)
    assert isinstance(data["message"], str)
    assert isinstance(data["status"], str)


def test_delete_fiscal_year_returns_404(client):
    response = client.delete("/api/v1/fiscal_year/ffffffff-ffff-ffff-ffff-ffffffffffff")
    assert response.status_code == 404

    data = response.json()

    # Assertions validating error response format
    assert isinstance(data, dict)
    assert "detail" in data
    assert isinstance(data["detail"], (str, dict, list))


def test_delete_fiscal_year_returns_422(client):
    response = client.delete("/api/v1/fiscal_year/not-a-uuid")
    assert response.status_code == 422

    data = response.json()

    # Assertions validating error response format
    assert isinstance(data, dict)
    assert "detail" in data
    assert isinstance(data["detail"], list)


def test_delete_fiscal_year_returns_500(
    client, get_fiscal_year_uuid_for_test, monkeypatch
):
    def raise_error():
        raise RuntimeError("Boom")

    monkeypatch.setattr(
        "src.router.fiscal_year.fiscal_year_uuid.delete_fiscal_year_service",
        raise_error,
    )
    response = client.delete(f"/api/v1/fiscal_year/{get_fiscal_year_uuid_for_test}")
    assert response.status_code == 500
    assert "Internal Server Error" in response.text
