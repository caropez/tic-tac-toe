import pytest
from app.services.game_service import GameService


@pytest.fixture
def game_service():
    return GameService()


def test_create_new_game(game_service):
    game = game_service.create_new_game("player1")
    assert game.id is not None
    assert game.board == [[" " for _ in range(3)] for _ in range(3)]
    assert game.current_player == "X"

