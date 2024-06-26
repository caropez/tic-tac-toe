# tic-tac-toe game
This is a FastAPI-based Tic-Tac-Toe game API.
## Features
* Create a new game and get a game ID
* Make moves using x and y coordinates
* Automatic computer moves (random)
* View all moves in a game, chronologically ordered
* View all games played by a player, chronologically ordered

## Setup and Run

1. Clone Repository
```bash
git clone  https://github.com/caropez/tic-tac-toe.git
```
2. Create virtual environment
```bash
python -m venv venv
```
3. Activate the virtual environment
```bash
On Windows: venv\Scripts\activate
On macOS and Linux: source venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run the application
```bash
uvicorn app.main:app --reload
```

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
  
### Get all games
- **Endpoint:** `GET /game/all`
- **Description:** Retrieves all games played.
 
  
### Get all games for a player
- **Endpoint:** `GET /game/player/{player_id}`
- **Description:** Retrieves all games played by the specified player.
 
### Get all moves for a game
- **Endpoint:** `GET /game/{game_id}/move`
- **Description:** Retrieves all moves made in the specified game.

### Get all games for a player

- **Endpoint:** `GET /game/player/{player_id}`
- **Description:** Retrieves all games played by the specified player, in chronological order.

# Others
**Dev Time:** 
I expent 3.5 Hours. Including planning and developing. I did it in 3 sessions. 1n, 1.30h and 1h.
**Considerations:**
I assumed it should be easy to test, so I made some trade-offs like not including a database but instead using a python class to store data (in-memory db).
I prioritized project structure and code design over tools and deployment.
**Others:**
I didn't have time to add more tests or extra features.

