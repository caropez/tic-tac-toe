import random
import uuid
from datetime import datetime
from typing import List, Optional

from app.db.in_memory_db import db
from app.models.game import Game, Move
from app.schemas.game import GameResponse, GameSummary, GameMove, GameMoveHistory


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
    def get_all_games() -> List[GameSummary]:
        games = db.games
        return [
            GameSummary(id=game.id, created_at=game.created_at, winner=game.winner)
            for game in games.values()
        ]

    @staticmethod
    def get_game(game_id: str) -> GameSummary:
        game = db.games.get(game_id)
        return GameSummary(id=game.id, created_at=game.created_at, winner=game.winner)

    @staticmethod
    def get_player_games(player_id: str) -> List[GameSummary]:
        games = db.get_player_games(player_id)
        return [
            GameSummary(id=game.id, created_at=game.created_at, winner=game.winner)
            for game in games
        ]

    @staticmethod
    def make_move(game_id: str, move: GameMove) -> GameResponse:
        game = db.get_game(game_id)
        if not game:
            raise ValueError("Game not found")

        if game.winner:
            raise ValueError("Game already finished")

        if game.board[move.y][move.x] != " ":
            raise ValueError("Invalid move")

        # Player move (always X)
        GameService._apply_move(game, move, "X")

        if GameService._check_game_end(game):
            return GameService._create_game_response(game)

        # Computer move (always O)
        computer_move = GameService._make_random_move(game.board)
        GameService._apply_move(game, computer_move, "O")

        if GameService._check_game_end(game):
            return GameService._create_game_response(game)

        db.save_game(game)
        return GameResponse(id=game.id, board=game.board, current_player="X", message="Move accepted")

    @staticmethod
    def _apply_move(game: Game, move: GameMove, player: str):
        game.board[move.y][move.x] = player
        game.add_move(Move("Player" if player == "X" else "Computer", move.x, move.y, datetime.now()))

    @staticmethod
    def _check_game_end(game: Game) -> bool:
        last_player = "X" if game.moves[-1].player == "Player" else "O"
        if GameService._check_winner(game.board, last_player):
            game.winner = last_player
            db.save_game(game)
            return True

        if GameService._is_board_full(game.board):
            game.winner = "Draw"
            db.save_game(game)
            return True

        return False

    @staticmethod
    def _create_game_response(game: Game) -> GameResponse:
        if game.winner == "Draw":
            message = "It's a draw!"
        else:
            message = f"{'Player' if game.winner == 'X' else 'Computer'} wins!"
        return GameResponse(id=game.id, board=game.board, current_player="X", winner=game.winner, message=message)

    @staticmethod
    def _check_winner(board, player):
        # Check rows, columns and diagonals
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
                    all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or \
                all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    @staticmethod
    def get_game_moves(game_id: str) -> Optional[List[GameMoveHistory]]:
        game = db.get_game(game_id)
        if not game:
            return None
        return [
            GameMoveHistory(
                player=move.player, x=move.x, y=move.y, timestamp=move.timestamp
            )
            for move in game.moves
        ]

    @staticmethod
    def _is_board_full(board):
        return all(cell != " " for row in board for cell in row)

    @staticmethod
    def _make_random_move(board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        y, x = random.choice(empty_cells)
        return GameMove(x=x, y=y)
