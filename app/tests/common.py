from sqlalchemy.engine import create_engine
from app.core.config import settings
from sqlalchemy import orm

Session = orm.sessionmaker()
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI_TEST)
