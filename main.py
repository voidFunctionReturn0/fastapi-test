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


@app.post("/guest-session")
def guestSession(deviceId: str):
    global currentPlayers
    global logger

    session: str = makeSession(deviceId)

    player = OfflinePlayer(session, deviceId)
    logger.debug("New Player: " + str(player.__dict__))

    currentPlayers.append(player) # 세션 관리: DB 사용 필요할 듯?
    logger.debug("Player Number: " + str(len(currentPlayers)))

    return {
        "session": player.session
    }


@app.post("/offline-game")
def offlineGame(session: str):
    game = OfflineGame(getPlayerIdBySession(session))

    # 객체의 일부 정보만 보내는 방법 어떻게 할지 고민 필요(변수 이름 변화 등에 자동 대응 안됨)
    return {
        "game": {
            "id": game.id,
            "state": game.state,
            "maxNumOfPlayers": game.maxNumOfPlayers,
            "host": game.host,
            "players": game.players
        },
        "playerId": {
            "id": player.id,
            "name": player.name
        }
    }