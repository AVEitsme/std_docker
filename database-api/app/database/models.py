from app import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, SmallInteger, BigInteger, VARCHAR, TIMESTAMP


class AgeGroup(Base):
    __tablename__ = "age_group"
    
    age_group_id = Column(SmallInteger, primary_key=True)
    group_name = Column(VARCHAR(10), unique=True, nullable=False)


class Client(Base):
    __tablename__ = "client"

    client_id = Column(BigInteger, primary_key=True)
    age_group_id = Column(SmallInteger, ForeignKey("age_group.age_group_id"), nullable=True)
    client_sex = Column(Boolean, nullable=True)


class Author(Base):
    __tablename__ = "author"

    author_id = Column(BigInteger, primary_key=True)
    author_name = Column(VARCHAR(200), nullable=False)


class Genre(Base):
    __tablename__ = "genre"

    genre_id = Column(SmallInteger, primary_key=True)
    genre_name = Column(VARCHAR(200), unique=True, nullable=False)


class Book(Base):
    __tablename__ = "book"

    book_id = Column(BigInteger, primary_key=True)
    book_title = Column(VARCHAR(300), nullable=False)
    book_issue_year = Column(SmallInteger, nullable=True)
    genres = relationship("Genre", secondary="book_genre", back_populates="genre")
    authors = relationship("Author", secondary="book_author", back_populates="author")


class BookGenre(Base):
    __tablename__ = "book_genre"

    book_id = Column(BigInteger, ForeignKey("book.book_id"), primary_key=True)
    genre_id = Column(SmallInteger, ForeignKey("genre.genre_id"), primary_key=True)


class BookAuthor(Base):
    __tablename__ = "book_author"

    book_id = Column(BigInteger, ForeignKey("book.book_id"), primary_key=True)
    author_id = Column(BigInteger, ForeignKey("author.author_id"), primary_key=True)


class Rating(Base):
    __tablename__ = "rating"

    client_id = Column(BigInteger, ForeignKey("client.client_id"), primary_key=True)
    book_id = Column(BigInteger, ForeignKey("book.book_id"), primary_key=True)
    start_date = Column(TIMESTAMP, primary_key=True)
    progress = Column(SmallInteger, nullable=True)
    rating = Column(SmallInteger, nullable=True)
