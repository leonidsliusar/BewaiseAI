from aiohttp import ClientSession
from sqlalchemy.ext.asyncio import AsyncSession

from core.dals import DBManager
from core.models import QuestionSet, Question, QuestionDB


async def execute_task(question_num: int, db: AsyncSession) -> list[QuestionDB]:
    question_obj = await _fetch_question(question_num)
    question_obj_array = question_obj.obj
    inserted_obj_array = await _add_question(question_obj, db)
    repeat_req = len(question_obj_array) - len(inserted_obj_array)
    while repeat_req > 0:
        question_obj_repeat = await _fetch_question(repeat_req)
        inserted_obj_array_repeat = await _add_question(question_obj_repeat, db)
        repeat_req -= len(inserted_obj_array_repeat)
        inserted_obj_array.extend(inserted_obj_array_repeat)
    return inserted_obj_array


async def _add_question(question_obj: QuestionSet, db: AsyncSession) -> list[QuestionDB]:
    return await DBManager().create(question_obj, db)


async def _fetch_question(question_num: int) -> QuestionSet:
    url: str = f'https://jservice.io/api/random?count={question_num}'
    async with ClientSession() as session:
        async with session.get(url) as response:
            question_set = [Question(**i) for i in await response.json()]
    question_obj = QuestionSet(obj=question_set)
    return question_obj
