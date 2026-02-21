```text
Erzeuge API-Tests für FastAPI mit pytest.

WICHTIG:
- Erzeuge einen LAUFFÄHIGEN Test (kein Pseudocode).
- Gib NUR Code aus (keine Erklärungen außerhalb des Codes).
- Comments and headings must be in English.
- KEINE zusätzlichen Pydantic-Hilfsmodelle erzeugen (kein BaseModel, kein TypeAdapter, kein eigenes Response-Schema im Test).

Ziel:
- API-Tests (HTTP / FastAPI)
- Test-Framework: pytest
- Der Test MUSS prüfen, dass die Response dem response_model entspricht – NUR über:
  - required keys
  - basic types
  - parseability (ISO dates/timestamps)

Naming-Regeln:
- Die HTTP-Methode MUSS im Namen enthalten sein:
  get_, post_, put_, patch_, delete_
- Dateiname: test_<http_method>_<endpoint>.py
- Endpoint-Name ohne führendes oder trailing "/"
- Endpoint-Name basiert auf der Resource, NICHT auf dem kompletten Pfad:
  - Entferne Prefixe wie "api", "v1" aus dem Dateinamen und Testnamen
  - Beispiel: /api/v1/fiscal_year -> endpoint = fiscal_year
- expected_behavior kurz und allgemein (z. B. returns_200, returns_list, returns_404)

Testfunktions-Format (EXAKT):
def test_<http_method>_<endpoint>_<expected_behavior>(client):
    response = client.<http_method>("<api_endpoint>")
    assert response.status_code == <http_status_code>

    data = response.json()

    # Assertions validating response_model

HTTP-Fehlercodes (WICHTIG):
- Verwende NUR sinnvolle HTTP-Fehlercodes für den jeweiligen Endpoint
  (z. B. 400, 401, 403, 404, 409, 422, 500)
- 200 und 500 muss enthalten sein.
- Bei 500 sollen eine generiert werden um zu prüfen das keine Python-Fehler unbehandelt durchkommen, sondern eine saubere Fehlermeldung zurückgegeben wird.
  Antowert {"code": 500, "detail": "Internal Server Error"}
- Wenn ein Fehlercode für den Endpoint nicht realistisch ist, generiere keinen Test dafür.

Inhaltliche Test-Regeln (SEHR WICHTIG):
- Kein Mocking-Code, keine Fixtures definieren
- Kein Pydantic im Test (kein BaseModel/TypeAdapter)
- Der Test MUSS:
  - Rückgabetyp prüfen (list/dict)
  - required keys prüfen (aus response_model ableiten; exclude=True Felder NICHT prüfen)
  - basic types prüfen (str/int/bool/None)
  - date/datetime parseability prüfen (date.fromisoformat / datetime.fromisoformat)
- Keine Business-Werte prüfen

Beispiel (verbindlich – Stil & Tiefe):
# Filename: test_get_health.py
from __future__ import annotations

from datetime import datetime

def test_get_health_returns_200(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert "timestamp" in data
    datetime.fromisoformat(data["timestamp"])

Input:
- API-Endpunkt:
- HTTP-Methode:
- Kurze Feature-Beschreibung:
- response_model:

Output:
- Codeblock mit Kommentar: "# Filename: <filename>"
- Vollständige Testfunktion im gewünschten Stil (ohne Pydantic-Hilfsmodelle)
- Zusätzlich: weitere Testfunktionen für NUR sinnvolle HTTP-Fehlercodes (falls zutreffend)
```
