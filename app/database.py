from app.config import settings

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

print(settings.db_url)
engie = create_async_engine(settings.db_url)

async_session_maker = sessionmaker(
    engie,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass
