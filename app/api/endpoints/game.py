from typing import List

from fastapi import APIRouter
from app.schemas.game import GameCreate, GameResponse, GameSummary
from app.services.game_service import GameService

router = APIRouter()
game_service = GameService()


@router.post("/new", response_model=GameResponse)
async def new_game(game: GameCreate):
    return game_service.create_new_game(game.player_id)


@router.get("/player/{player_id}", response_model=List[GameSummary])
async def get_player_games(player_id: str):
    games = game_service.get_player_games(player_id)
    return games
