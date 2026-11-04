from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite:///boxscore_ai.db"
engine = create_engine(DATABASE_URL)    # middleman of sqlalchemy and database


class Base(DeclarativeBase):
    pass  # inherit everything from the parent DeclarativeBase and dont add extra


def init_db():
    import models   # loads model classes (Games table) into python

    Base.metadata.create_all(
        engine
    )  # takes the model structure and generates the sql stamement to create a table in SQLite
