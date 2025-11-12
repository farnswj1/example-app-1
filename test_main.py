from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello DevLaunch! From app1!"}


def test_greet_person():
    person_name = "Alice"
    response = client.get(f"/greet/{person_name}")
    assert response.status_code == 200
    assert response.json() == {"greeting": f"Hello, {person_name}!"}


def test_create_person():
    person_data = {"name": "Bob", "age": 30}
    response = client.post("/person/", json=person_data)
    assert response.status_code == 201
    assert response.json() == person_data
