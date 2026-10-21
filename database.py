from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
engine = create_engine("sqlite:///biblioteca.db")
class Base(DeclarativeBase):
    pass
SessionLocal = sessionmaker(bind=engine)