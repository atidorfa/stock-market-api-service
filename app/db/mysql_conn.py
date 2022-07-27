from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import get_settings

_database_uri = f"mysql+pymysql://{get_settings().DB_USER}:{get_settings().DB_PASSWD}@{get_settings().DB_HOST}:" \
                f"{get_settings().DB_PORT}/{get_settings().DB}"


engine = create_engine(_database_uri, pool_pre_ping=True, pool_size=get_settings().DB_POOL_SIZE,
                       max_overflow=get_settings().DB_POOL_MAX_SIZE, echo=get_settings().DB_LOG_QUERY)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    return SessionLocal()
