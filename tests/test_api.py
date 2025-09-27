import pytest
from src.app import create_app
from src.models import db

@pytest.fixture
def client():
    app = create_app(database_uri="sqlite:///:memory:")
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_task(client):
    r = client.post("/tasks", json={"title":"Tarefa 1"})
    assert r.status_code == 201
    assert r.get_json()["title"] == "Tarefa 1"

def test_list_empty(client):
    r = client.get("/tasks")
    assert r.status_code == 200
    assert r.get_json() == []
