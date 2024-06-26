import uuid
from typing import List

from app.db.in_memory_db import db
from app.models.game import Game
from app.schemas.game import GameResponse, GameSummary


class GameService:
    @staticmethod
    def create_new_game(player_id: str) -> GameResponse:
        game_id = str(uuid.uuid4())
        game = Game(id=game_id, player_id=player_id)
        db.save_game(game)
        return GameResponse(
            id=game_id,
            board=game.board,
            current_player=game.current_player,
            message="New game started",
        )

    @staticmethod
    def get_player_games(player_id: str) -> List[GameSummary]:
        games = db.get_player_games(player_id)
        return [GameSummary(id=game.id, created_at=game.created_at) for game in games]
