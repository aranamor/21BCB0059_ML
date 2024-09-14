# Code was written with the help of chatgpt

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


# Create a base class for our models
class Base(DeclarativeBase):
    pass


# Define the Document model
class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)


# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True, nullable=False)


# Set up database
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()


def init_db():
    # Create tables
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()
