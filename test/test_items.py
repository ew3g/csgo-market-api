import asyncio
import os

import pytest
from dotenv import load_dotenv, find_dotenv
from starlette.testclient import TestClient

from main import app
from test.commons import validate_json
from test.schemas import item_list_response_schema, item_not_found_response_schema

load_dotenv(find_dotenv())

client = TestClient(app)


@pytest.mark.asyncio
async def test_add_item_data():
    token = os.getenv("API_TOKEN")
    response = client.post(
        "/item/",
        json={
            "name": "MyTest",
            "type": "MyTest",
            "subtype": "MyTest",
            "game_type": "MyTest"
        },
        headers={"x-token": token})

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_items_data():
    response = client.get("/item/?page=0&limit=1", headers={"x-token": os.getenv("API_TOKEN")})

    assert response.status_code == 200
    assert 1 == len(response.json()["data"])
    assert validate_json(response.json(), item_list_response_schema)


@pytest.mark.asyncio
async def test_get_item_not_found():
    response = client.get("/item/629d4b340fb273faf5e846d2", headers={"x-token": os.getenv("API_TOKEN")})
    json_response = response.json()
    assert 404 == json_response["code"]
    assert validate_json(json_response, item_not_found_response_schema)
