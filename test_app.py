from fastapi.testclient import TestClient

from app import app  # Assuming your FastAPI code is in a file named 'app.py'

client = TestClient(app)

def test_post():
    response = client.post("/")
    assert response.status_code == 200
    assert response.json() == {"status_code": 200}

def test_delete():
    response = client.delete("/")
    assert response.status_code == 200
    assert response.json() == {"status_code": 200}
