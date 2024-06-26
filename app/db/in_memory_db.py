from typing import Dict, List

from app.models.game import Game


class InMemoryDB:
    def __init__(self):
        self.games: Dict[str, Game] = {}
        self.player_games: Dict[str, List[str]] = {}

    def save_game(self, game: Game):
        self.games[game.id] = game
        if game.player_id not in self.player_games:
            self.player_games[game.player_id] = []
        if game.id not in self.player_games[game.player_id]:
            self.player_games[game.player_id].append(game.id)

    def get_player_games(self, player_id: str) -> List[Game]:
        game_ids = self.player_games.get(player_id, [])
        return [self.games[game_id] for game_id in game_ids]

    def get_game(self, game_id: str) -> Game:
        return self.games.get(game_id)


db = InMemoryDB()