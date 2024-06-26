from datetime import datetime
from typing import Optional, List


class Move:
    def __init__(self, player: str, x: int, y: int, timestamp: datetime):
        self.player = player
        self.x = x
        self.y = y
        self.timestamp = timestamp


class Game:
    def __init__(self, id: str, player_id: str):
        self.id: str = id
        self.player_id: str = player_id
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner: Optional[str] = None
        self.moves: List[Move] = []
        self.created_at = datetime.now()

    def add_move(self, move: Move):
        self.moves.append(move)