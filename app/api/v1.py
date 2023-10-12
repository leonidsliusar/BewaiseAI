from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.config import db
from core.models import InputData, QuestionDB
from core.services import execute_task
from utils.cache import CacheInRedis

rout = APIRouter(prefix='/api/v1')

cache = CacheInRedis()


@rout.post('/questions', response_model=list[QuestionDB],
           description='endpoint to add new questions and fetch previous added questions')
async def append_question(data: InputData, session: AsyncSession = Depends(db)):
    prev_obj = cache.get()
    obj = await execute_task(data.questions_num, session)
    cache.put(obj)
    return prev_obj
