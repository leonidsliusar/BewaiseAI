import asyncio
import subprocess

import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.models import QuestionSet, Question
from app.core.schema import Base


@pytest.fixture
async def setup_and_teardown_db():
    start_command = (
        "docker compose -f tests/docker-compose.yml up -d"
    )
    subprocess.run(["bash", "-c", start_command])
    await asyncio.sleep(2)
    mock_engine = create_async_engine(
        "postgresql+asyncpg://postgres:postgres@localhost:5460/test", echo=True
    )
    mock_session = async_sessionmaker(mock_engine, expire_on_commit=False)
    async with mock_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with mock_session() as connect:
        yield connect
    stop_command = "docker rm test -f -v"
    subprocess.run(["bash", "-c", stop_command])


@pytest.fixture
def question():
    return mock_question()


@pytest.fixture
async def mock_fetch(*args, **kwargs):
    return mock_question()


@pytest.fixture
async def mock_add(*args, **kwargs):
    obj_db = mock_question().serializeDB.obj
    return obj_db


def mock_question():
    quest_1 = {"id": 126127,
               "answer": "Edinburgh",
               "question": "The Last Drop Tavern was named for its proximity to the spot where public hangings took "
                           "place in this Scottish capital",
               "value": 200,
               "airdate": "2009-07-03T19:00:00.000Z",
               "created_at": "2022-12-30T20:02:49.022Z",
               "updated_at": "2022-12-30T20:02:49.022Z",
               "category_id": 14118,
               "game_id": 3083,
               "invalid_count": None,
               "category": {
                   "id": 14118,
                   "title": "pubs \u0026 taverns",
                   "created_at": "2022-12-30T20:02:48.833Z",
                   "updated_at": "2022-12-30T20:02:48.833Z",
                   "clues_count": 5
               }}
    quest_2 = {"id": 148275,
               "answer": "Ray Bradbury",
               "question": "In 2007 the Pulitzer Prize board gave this sci fi author a special citation for his "
                           "distinguished career",
               "value": 400,
               "airdate": "2012-04-20T19:00:00.000Z",
               "created_at": "2022-12-30T20:33:07.474Z",
               "updated_at": "2022-12-30T20:33:07.474Z",
               "category_id": 17460,
               "game_id": 3877,
               "invalid_count": None,
               "category": {
                   "id": 17460,
                   "title": "man: ray",
                   "created_at": "2022-12-30T20:33:06.975Z",
                   "updated_at": "2022-12-30T20:33:06.975Z",
                   "clues_count": 5
               }}
    obj_set = [Question(**quest_1), Question(**quest_2)]
    return QuestionSet(obj=obj_set)
