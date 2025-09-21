from fastapi.testclient import TestClient
from src.multiagent.api.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_process_endpoint():
    response = client.post("/process", json={"query": "AI в кибербезопасности"})
    assert response.status_code == 200
    body = response.json()
    assert "query" in body
    assert "report" in body
    assert "insights" in body
    assert "confidence" in body
