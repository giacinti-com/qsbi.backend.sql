from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from qsbi.backend.sql.config import settings


def get_qsbi_url() -> str:
    return settings.QSBI_DB_URL


def get_session_maker() -> sessionmaker:
    engine = create_engine(
        get_qsbi_url(),
        # required for sqlite
        connect_args={"check_same_thread": False},
    )
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Session:
    maker: sessionmaker = get_session_maker()
    session: Session = maker()
    return session
