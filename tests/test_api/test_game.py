from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_game():
    response = client.post("/game/new", json={"player_id": "player1"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert "board" in response.json()
    assert "current_player" in response.json()


def test_make_move():
    new_game_response = client.post("/game/new", json={"player_id": "player1"})
    game_id = new_game_response.json()["id"]

    move_response = client.post(f"/game/{game_id}/move", json={"x": 0, "y": "0"})
    assert move_response.status_code == 200
    assert move_response.json()["board"][0][0] == "X"


def test_get_game():
    new_game_response = client.post("/game/new", json={"player_id": "player1"})
    game_id = new_game_response.json()["id"]
    get_game_response = client.get(f"/game/{game_id}")
    assert get_game_response.status_code == 200
    assert get_game_response.json()["id"] == game_id

def test_get_all_games():
    client.post("/game/new", json={"player_id": "player1"})
    client.post("/game/new", json={"player_id": "player2"})
    get_game_response = client.get(f"/game/all")
    assert get_game_response.status_code == 200
    assert len(get_game_response.json()) > 1