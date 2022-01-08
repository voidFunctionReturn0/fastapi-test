import sys
[sys.path.append(i) for i in ['.', '..']]
from res.modules import StrEnum
from enum import auto

class GAME_STATE(StrEnum):
    WAITING = auto()
    IN_GAME = auto()

class GAME_MODE(StrEnum):
    NORMAL = auto()
    SPY = auto()

MAX_NUM_OF_PALYERS = 8