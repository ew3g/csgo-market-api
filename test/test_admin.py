from dotenv import load_dotenv, find_dotenv
from .commons import validate_json
from main import app
from fastapi.testclient import TestClient
import os

from test.schemas import unprocessable_entity_response_schema

client = TestClient(app)

load_dotenv(find_dotenv())


def test_post_admin():
    response = client.post("/admin/", headers={"x-token": os.getenv("API_TOKEN")})
    assert response.status_code == 200
    assert response.json() == {"message": "Admin getting schwifty"}


def test_post_admin_unprocessable_entity_no_token():
    response = client.post("/admin/")
    json_response = response.json()
    assert response.status_code == 422
    assert validate_json(json_response, unprocessable_entity_response_schema)
