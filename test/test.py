from main import app
from fastapi.testclient import TestClient
from jsonschema import validate, exceptions
from schemas import unprocessable_entity_response_schema

import os


client = TestClient(app)


def test_get_ping_ok():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def validate_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
    except exceptions.ValidationError as err:
        return False
    return True


def test_post_admin_ok():
    print("\n{}".format(os.getenv("API_TOKEN")))
    response = client.post("/admin/", headers={"x-token": os.getenv("API_TOKEN")})
    assert response.status_code == 200
    assert response.json() == {"message": "Admin getting schwifty"}


def test_post_admin_unprocessable_entity_no_token():
    response = client.post("/admin/")
    json_response = response.json()
    assert validate_json(json_response, unprocessable_entity_response_schema)
    assert response.status_code == 422
