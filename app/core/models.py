import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Categories(BaseModel):
    id: int
    title: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    clues_count: int


class QuestionDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    answer: str
    question: str
    created_at: datetime.datetime


class Question(BaseModel):
    id: int
    answer: str
    question: str
    value: Optional[int] = None
    airdate: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    category_id: int
    game_id: int
    invalid_count: Optional[int] = None
    category: Categories

    @property
    def serializeDB(self) -> QuestionDB:
        return QuestionDB(
            id=self.id,
            answer=self.answer,
            question=self.question,
            created_at=self.created_at
        )


class QuestionDBSet(BaseModel):
    obj: list[QuestionDB]


class QuestionSet(BaseModel):
    obj: list[Question]

    @property
    def serializeDB(self) -> QuestionDBSet:
        obj_db = []
        for item in self.obj:
            obj_db.append(item.serializeDB)
        return QuestionDBSet(obj=obj_db)


class InputData(BaseModel):
    questions_num: int = Field(..., gt=0, le=100)
