import os
import tempfile
import pytest
from fastapi.testclient import TestClient

from src.main import app
import os


@pytest.fixture(autouse=True)
def cleanup_db():
    # ensure a clean DB per test run
    db_path = os.path.join(os.getcwd(), "app.db")
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
        except OSError:
            pass
    yield


@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_register_and_get(client):
    payload = {
        "first_name": "Alice",
        "last_name": "Tester",
        "email": "alice+test@example.com",
        "phone": "123-456-7890",
        "organization": "Acme",
        "notes": "Looking forward",
    }
    r = client.post("/register", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["email"] == payload["email"]
    reg_id = data["id"]

    r2 = client.get(f"/registrations/{reg_id}")
    assert r2.status_code == 200
    assert r2.json()["id"] == reg_id
