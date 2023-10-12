from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import QuestionSet, QuestionDB
from core.schema import Questions


class DBManager:

    async def create(self, question: QuestionSet, db: AsyncSession) -> list[QuestionDB]:
        result = await db.scalars(insert(Questions).on_conflict_do_nothing().returning(Questions),
                                  question.serializeDB.model_dump().get('obj'))
        inserted_obj = [QuestionDB.model_validate(i) for i in result.fetchall()]
        await db.commit()
        return inserted_obj

    async def read(self, db: AsyncSession):
        """not implemented"""
        ...

    async def update(self, db: AsyncSession):
        """not implemented"""
        ...

    async def delete(self, db: AsyncSession):
        """not implemented"""
        ...
