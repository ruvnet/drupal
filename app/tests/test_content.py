from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_content():
    response = client.post("/content/", json={"title": "Sample Content", "body": "This is a sample content.", "author_id": 1})
    assert response.status_code == 201
    assert response.json()["title"] == "Sample Content"
    assert response.json()["body"] == "This is a sample content."
    assert response.json()["author_id"] == 1

def test_read_content():
    response = client.get("/content/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Sample Content"
    assert response.json()["body"] == "This is a sample content."
    assert response.json()["author_id"] == 1

def test_update_content():
    response = client.put("/content/1", json={"title": "Updated Content", "body": "This is an updated content."})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Content"
    assert response.json()["body"] == "This is an updated content."
    assert response.json()["author_id"] == 1

def test_delete_content():
    response = client.delete("/content/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Content deleted successfully"
