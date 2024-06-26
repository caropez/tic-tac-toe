from fastapi import FastAPI
from app.api.endpoints import game

app = FastAPI(title="Tic-Tac-Toe API")

app.include_router(game.router, prefix="/game", tags=["game"])