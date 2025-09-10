from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.infrastructure.db.config import DBConfig


class Database:
    def __init__(self, config: DBConfig) -> None:
        self._async_engine = create_async_engine(
            config.url,
            echo=config.echo,
            isolation_level='READ COMMITTED',
            pool_pre_ping=True,
            pool_size=6,
            max_overflow=12,
            pool_timeout=30,
        )
        self._async_session_maker = async_sessionmaker(self._async_engine, expire_on_commit=False)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._async_session_maker() as session:
            yield session
