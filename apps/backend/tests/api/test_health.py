from datetime import datetime


def test_health_returns_live_and_timestamp(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    data = response.json()

    # Have keys
    assert "message" in data
    assert "timestamp" in data

    # Contents
    assert data["message"] == "Live"

    # timestamp parseable (ISO 8601)
    ts = data["timestamp"]
    parsed = datetime.fromisoformat(ts)

    # timestamp is recent (within 10 seconds)
    now = datetime.now(parsed.tzinfo) if parsed.tzinfo else datetime.now()
    delta_seconds = abs((now - parsed).total_seconds())
    assert delta_seconds < 10
