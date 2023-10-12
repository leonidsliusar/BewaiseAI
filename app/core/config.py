import os
from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from pydantic_settings import BaseSettings, SettingsConfigDict

_python_path = os.environ.get('PYTHONPATH')
env_file_path = os.path.join(_python_path, '.env')


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file_path, env_file_encoding='utf-8')

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    REDIS_HOST: str
    REDIS_PORT: int
    db_connect: Optional[str] = None

    def __init__(self):
        super().__init__()
        self.db_connect = (f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/'
                           f'{self.DB_NAME}')


settings = Settings()

engine = create_async_engine(settings.db_connect, echo=True)
session = async_sessionmaker(engine, expire_on_commit=False)


async def db() -> AsyncSession:
    async with session() as connect:
        yield connect
