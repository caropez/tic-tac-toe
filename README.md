# tic-tac-toe game
This is a FastAPI-based Tic-Tac-Toe game API.
## Features
* Create a new game and get a game ID
* Make moves using x and y coordinates
* Automatic computer moves (random)
* View all moves in a game, chronologically ordered
* View all games played by a player, chronologically ordered

## Setup

1. Clone Repository
2. Create virtual environment
3. Activate the virtual environment
4. Install dependencies
5. Run the application

## API Endpoints
### Create a new game
- **Endpoint:** `POST /game/new`
- **Description:** Creates a new game and returns the game 'id', the 'board' and the 'current_player'.
- **Payload:**
  ```json
  {
    "player_id": "string"
  }
  
### Make a move
- **Endpoint:** `POST /game/{game_id}/move`
- **Description:** Makes a move in the specified game. The computer will automatically make a move.
- **Payload:**
  ```json
  {
    "x": 0,
    "y": 0
  }
  
### Get all games for a player
- **Endpoint:** `GET /game/player/{player_id}`
- **Description:** Retrieves all games played by the specified player.
 
### Get all moves for a game
- **Endpoint:** `GET /game/{game_id}/move`
- **Description:** Retrieves all moves made in the specified game.

### Get all games for a player

- **Endpoint:** `GET /game/player/{player_id}`
- **Description:** Retrieves all games played by the specified player, in chronological order.


