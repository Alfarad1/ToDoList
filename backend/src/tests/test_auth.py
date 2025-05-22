import pytest
from fastapi.testclient import TestClient
from api.main import app

def test_login_success():
    with TestClient(app=app, base_url="http://test") as tc:
        response = tc.post("/auth/login", data={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()