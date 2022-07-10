from main import app
from fastapi.testclient import TestClient
import os

client = TestClient(app)


def test_post_admin():
    response = client.post("/admin/", headers={"x-token": os.getenv("API_TOKEN")})
    assert response.status_code == 200
    assert response.json() == {"message": "Admin getting schwifty"}