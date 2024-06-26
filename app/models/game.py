from datetime import datetime


class Game:
    def __init__(self, id: str, player_id: str):
        self.id: str = id
        self.player_id: str = player_id
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.created_at = datetime.now()