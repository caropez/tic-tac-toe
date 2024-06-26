from typing import List

from fastapi import APIRouter, HTTPException
from app.schemas.game import GameCreate, GameResponse, GameSummary, GameMove, GameMoveHistory
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


@router.get("/all", response_model=List[GameSummary])
async def get_games():
    games = game_service.get_all_games()
    if not games:
        raise HTTPException(status_code=404, detail="Games not found")
    return games


@router.get("/{game_id}", response_model=GameSummary)
async def get_game(game_id: str):
    try:
        return game_service.get_game(game_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.post("/{game_id}/move", response_model=GameResponse)
async def make_move(game_id: str, move: GameMove):
    try:
        return game_service.make_move(game_id, move)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{game_id}/moves", response_model=List[GameMoveHistory])
async def get_game_moves(game_id: str):
    moves = game_service.get_game_moves(game_id)
    if not moves:
        raise HTTPException(status_code=404, detail="Game not found")
    return moves

@router.get("/{game_id}/moves", response_model=List[GameMoveHistory])
async def get_game_moves(game_id: str):
    moves = game_service.get_game_moves(game_id)
    if not moves:
        raise HTTPException(status_code=404, detail="Game not found")
    return moves
