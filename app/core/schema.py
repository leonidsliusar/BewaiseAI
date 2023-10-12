import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    ...


class Questions(Base):
    __tablename__ = 'Questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    answer: Mapped[str]
    question: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))

    def __str__(self):
        return f'id: {self.id}\nquestion: {self.question}\nanswer: {self.answer}\ncreated: {self.created_at}'
