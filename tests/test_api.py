import pytest
from src.app import create_app
from src.models import db

@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()

def test_create_task(client):
    response = client.post("/tasks", json={
        "title": "Tarefa Teste",
        "description": "Descrição da tarefa",
        "priority": 1
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Tarefa Teste"
    assert data["description"] == "Descrição da tarefa"
    assert data["priority"] == 1
    assert data["done"] is False

def test_get_tasks(client):
    client.post("/tasks", json={"title": "Tarefa 1", "description": "Teste", "priority": 2})
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["title"] == "Tarefa 1"

def test_update_task(client):
    res = client.post("/tasks", json={"title": "Tarefa Antiga", "description": "Desc", "priority": 1})
    task_id = res.get_json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Tarefa Atualizada", "done": True})
    assert response.status_code == 200
    data = response.get_json()
    assert data["title"] == "Tarefa Atualizada"
    assert data["done"] is True

def test_delete_task(client):
    res = client.post("/tasks", json={"title": "Tarefa a Deletar", "description": "Desc", "priority": 2})
    task_id = res.get_json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Task deletada com sucesso"
    get_res = client.get("/tasks")
    tasks = get_res.get_json()
    assert all(task["id"] != task_id for task in tasks)
