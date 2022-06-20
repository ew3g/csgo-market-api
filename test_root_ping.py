from main import app
from fastapi.testclient import TestClient
import os

client = TestClient(app)


def test_get_ping():
    print(os.getenv("API_TOKEN"))
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_post_admin():
    response = client.post("/admin", headers={"x-token": os.getenv("API_TOKEN")})
    print(response.raw)
    assert response.status_code == 200
    assert response.json() == {"message": "Admin getting schwifty"}
