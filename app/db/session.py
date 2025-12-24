from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False)

Base = declarative_base()