import sys
[sys.path.append(i) for i in ['.', '..']]
from datetime import datetime, date
import res.constants as constants
from model.offlinePlayer import OfflinePlayer

class OfflineGame:
    cntId = 0

    def makeId(self):
        # 락 필요(스레드 안전)
        currentId = OfflineGame.cntId
        OfflineGame.cntId += 1
        return currentId


    def __init__(self, gameMakerId: int):
        self.id = self.makeId()
        self.state = constants.GAME_STATE.WAITING
        self.maxNumOfPlayers = constants.MAX_NUM_OF_PALYERS
        self.createdAt = datetime.now()
        self.lastPlayOn: date | None = None
        self.leader = 0 # players의 인덱스
        self.players = [gameMakerId]