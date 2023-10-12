import json
from abc import ABC, abstractmethod
from typing import Optional

import redis

from core.config import settings
from core.models import QuestionDB


class Cache(ABC):
    @abstractmethod
    def put(self, question_obj: list[QuestionDB]) -> None:
        ...

    @abstractmethod
    def get(self) -> Optional[list]:
        ...


class CacheInMem(Cache):
    _set: Optional[list] = []

    def put(self, question_obj: list[QuestionDB]) -> None:
        self._set = question_obj

    @property
    def get(self) -> Optional[list]:
        return self._set


class CacheInRedis(Cache):

    def __init__(self, db: int = 0):
        self._session = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True,
            db=db,
        )

    def put(self, question_obj: list[QuestionDB]) -> None:
        serialized_data = json.dumps([i.model_dump(mode='json') for i in question_obj])
        self._session.set('question', serialized_data)

    def get(self) -> list:
        last_questions = self._session.get('question')
        return json.loads(last_questions) if last_questions else []
