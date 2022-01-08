import sys
[sys.path.append(i) for i in ['.', '..']]
from fastapi import FastAPI
from model.offlineGame import OfflineGame
from model.offlinePlayer import OfflinePlayer

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/offline-game")
def offlineGame(player: OfflinePlayer):
    return OfflineGame(player.id)