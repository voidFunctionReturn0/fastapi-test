import sys
[sys.path.append(i) for i in ['.', '..']]
from datetime import date
from pydantic.main import BaseModel

class OfflinePlayer(BaseModel):
    id: int
    name: str
    deviceId: str
    """createdAt: date
    updatedAt: date
    winAsCitizen: int
    defeatAsCitizen: int
    winAsMafia: int
    defeatAsMafia: int
    totalNumOfGame: int
    heart: int"""

"""
class Player():
    def __init__(
        self,
        id: int,
        name: str,
        deviceId: str,
        createdAt: date,
        updatedAt: date,
        winAsCitizen: int,
        defeatAsCitizen: int,
        winAsMafia: int,
        defeatAsMafia: int,
        totalNumOfGame: int,
        heart: int
        ):
        self.id = id
        self.name = name
        self.deviceId = deviceId
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.winAsCitizen = winAsCitizen
        self.defeatAsCitizen = defeatAsCitizen
        self.winAsMafia = winAsMafia
        self.defeatAsMafia = defeatAsMafia
        self.totalNumOfGame = totalNumOfGame
        self.heart = heart
"""