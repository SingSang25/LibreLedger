from datetime import datetime


def test_health_returns_live_and_timestamp(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    data = response.json()

    # Keys vorhanden
    assert "message" in data
    assert "timestamp" in data

    # Inhalt
    assert data["message"] == "Live"

    # timestamp parsebar (ISO 8601)
    ts = data["timestamp"]

    # Unterstützt sowohl "2026-02-09T12:34:56.123456" als auch "...+00:00"
    parsed = datetime.fromisoformat(ts)

    # Optional: Plausibilität - nicht in der Zukunft und nicht uralt
    now = datetime.now(parsed.tzinfo) if parsed.tzinfo else datetime.now()
    delta_seconds = abs((now - parsed).total_seconds())
    assert delta_seconds < 10  # 10 Sekunden Toleranz
