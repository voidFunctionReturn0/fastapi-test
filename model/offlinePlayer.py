from res.modules import makeSession
from datetime import date, datetime
import sys
[sys.path.append(i) for i in ['.', '..']]


class OfflinePlayer:
    def __init__(self, deviceId: str):
        self.session: str = makeSession(deviceId) # id 역할, 이론상 중복 가능
        self.name: str = "익명의 플레이어"
        self.deviceId: str | None = deviceId
        self.createdAt: date = datetime.now()
        self.updatedAt: date = datetime.now()
        self.winAsCitizen: int = 0
        self.defeatAsCitizen: int = 0
        self.winAsMafia: int = 0
        self.defeatAsMafia: int = 0
        self.totalNumOfGame: int = 0
        self.heart: int = 0