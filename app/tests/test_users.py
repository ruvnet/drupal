from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "john_doe", "email": "john@example.com", "password": "password123"})
    assert response.status_code == 201
    assert response.json()["username"] == "john_doe"
    assert response.json()["email"] == "john@example.com"

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "john_doe"
    assert response.json()["email"] == "john@example.com"

def test_update_user():
    response = client.put("/users/1", json={"username": "john_doe_updated", "email": "john_updated@example.com", "password": "newpassword123"})
    assert response.status_code == 200
    assert response.json()["username"] == "john_doe_updated"
    assert response.json()["email"] == "john_updated@example.com"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"
