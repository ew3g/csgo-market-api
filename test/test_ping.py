from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
