from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class GameCreate(BaseModel):
    player_id: str


class GameSummary(BaseModel):
    id: str
    winner: Optional[str]
    created_at: datetime


class GameResponse(BaseModel):
    id: str
    board: List[List[str]]
    current_player: str
    message: str


class GameMove(BaseModel):
    x: int
    y: int


class GameMoveHistory(BaseModel):
    player: str
    x: int
    y: int
    timestamp: datetime