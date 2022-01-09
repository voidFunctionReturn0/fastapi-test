from datetime import datetime
import hashlib
import logging
import sys
[sys.path.append(i) for i in ['.', '..']]
from enum import Enum


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


def makeSession(key: str):
    key = key + str(datetime.now())
    session = hashlib.sha256()
    session.update(key.encode('utf-8'))
    return session.hexdigest()


def makeLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)   # DEBUG < INFO < WARNING < ERROR < WARNING
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    '''
    # log를 파일에 출력
    file_handler = logging.FileHandler('my.log') # 폴더 경로 없으면 오류 발생
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    '''
    return logger


def getPlayerIdBySession(session: str):
    return