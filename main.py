import sys
[sys.path.append(i) for i in ['.', '..']]
from res.modules import getPlayerIdBySession, makeLogger, makeSession
from fastapi import FastAPI
from model.offlineGame import OfflineGame
from model.offlinePlayer import OfflinePlayer


app = FastAPI()

global logger
logger = makeLogger()

global currentPlayers
currentPlayers = []


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/offline-game")
def offlineGame(deviceId: str):
    global currentPlayers
    global logger

    player = OfflinePlayer(deviceId)
    currentPlayers.append(player) # 세션 관리: DB 사용 필요할 듯?
    game = OfflineGame(player.session)
    
    logger.debug("New Player is created: " + str(player.__dict__))
    logger.debug("Player Number: " + str(len(currentPlayers)))
    logger.debug("New Game is created: " + str(game.id))
    

    # 객체의 일부 정보만 보내는 방법 어떻게 할지 고민 필요(변수 이름 변화 등에 자동 대응 안됨)
    return {
        "game": {
            "id": game.id,
            "state": game.state,
            "maxNumOfPlayers": game.maxNumOfPlayers,
            "host": game.host,
            "players": game.players
        },
        "player": {
            "session": player.session,
            "name": player.name
        }
    }