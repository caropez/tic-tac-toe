from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class GameCreate(BaseModel):
    player_id: str


class GameSummary(BaseModel):
    id: str
    created_at: datetime


class GameResponse(BaseModel):
    id: str
    board: List[List[str]]
    current_player: str

