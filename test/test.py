from main import app
from fastapi.testclient import TestClient
from jsonschema import validate, exceptions
from schemas import (
    empty_item_list_response_schema,
    item_response_schema,
    item_list_response_schema,
    item_not_found_response_schema,
    unprocessable_entity_response_schema
)
from dotenv import load_dotenv, find_dotenv

import os


client = TestClient(app)
load_dotenv(find_dotenv())


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
    response = client.post("/admin/", headers={"x-token": os.getenv("API_TOKEN")})
    assert response.status_code == 200
    assert response.json() == {"message": "Admin getting schwifty"}


def test_post_admin_unprocessable_entity_no_token():
    response = client.post("/admin/")
    json_response = response.json()
    assert validate_json(json_response, unprocessable_entity_response_schema)
    assert response.status_code == 422


def test_get_item_list_ok():
    response = client.get("/item/?page=1&limit=2", headers={"x-token": os.getenv("API_TOKEN")})
    json_response = response.json()
    assert 200 == response.status_code
    assert validate_json(json_response, item_list_response_schema)
    assert 2 == len(json_response["data"])


def test_get_item_list_empty_ok():
    response = client.get("/item/?page=999999&limit=2", headers={"x-token": os.getenv("API_TOKEN")})
    json_response = response.json()
    assert 200 == response.status_code
    assert validate_json(json_response, empty_item_list_response_schema)
    assert 0 == len(json_response["data"])


def test_get_item_ok():
    response = client.get("/item/629d4b340fb273faf5e846db", headers={"x-token": os.getenv("API_TOKEN")})
    json_response = response.json()
    assert 200 == response.status_code
    assert validate_json(json_response, item_response_schema)


def test_get_item_not_found():
    response = client.get("/item/629d4b340fb273faf5e846d2", headers={"x-token": os.getenv("API_TOKEN")})
    json_response = response.json()
    assert 404 == json_response["code"]
    assert validate_json(json_response, item_not_found_response_schema)
