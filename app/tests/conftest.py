import pytest
from app.core.config import settings
from app.db.session import Session, engine
from app.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI_TEST)
session = scoped_session(sessionmaker(bind=engine))


@pytest.fixture
def db():
    yield Session
    session.close()


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
