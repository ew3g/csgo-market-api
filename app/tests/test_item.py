from main import app
from fastapi.testclient import TestClient

import os

client = TestClient(app)


def test_get_items_data():
    response = client.get("/item/", headers={"x-token": os.getenv("API_TOKEN")})
    assert response.status_code == 200

    #https://stackoverflow.com/questions/48407135/tornado-motor-with-mongomock-for-testing