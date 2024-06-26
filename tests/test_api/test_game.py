from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_game():
    response = client.post("/game/new", json={"player_id": "player1"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert "board" in response.json()
    assert "current_player" in response.json()
