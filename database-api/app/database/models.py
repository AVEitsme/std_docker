from app import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    SmallInteger,
    BigInteger,
    VARCHAR,
    Table,
)


class Client(Base):
    __tablename__ = "clients"

    client_id = Column(BigInteger, primary_key=True)
    client_age = Column(SmallInteger, nullable=True)
    client_sex = Column(Boolean, nullable=True)


book_genre = Table(
    "book_genre",
    Base.metadata,
    Column("book_id", ForeignKey("books.book_id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.genre_id"), primary_key=True),
)

book_author = Table(
    "book_author",
    Base.metadata,
    Column("book_id", ForeignKey("books.book_id"), primary_key=True),
    Column("author_id", ForeignKey("authors.author_id"), primary_key=True),
)


class Book(Base):
    __tablename__ = "books"

    book_id = Column(BigInteger, primary_key=True)
    book_title = Column(VARCHAR(300), nullable=False)
    book_issue_year = Column(SmallInteger, nullable=True)
    genres = relationship("Genre", secondary="book_genre", back_populates="books")
    authors = relationship("Author", secondary="book_author", back_populates="books")


class Author(Base):
    __tablename__ = "authors"

    author_id = Column(BigInteger, primary_key=True)
    author_name = Column(VARCHAR(200), nullable=False)
    books = relationship("Book", secondary="book_author", back_populates="authors")


class Genre(Base):
    __tablename__ = "genres"

    genre_id = Column(SmallInteger, primary_key=True)
    genre_name = Column(VARCHAR(200), unique=True, nullable=False)
    books = relationship("Book", secondary="book_genre", back_populates="genres")


class Rating(Base):
    __tablename__ = "ratings"

    client_id = Column(BigInteger, ForeignKey("clients.client_id"), primary_key=True)
    book_id = Column(BigInteger, ForeignKey("books.book_id"), primary_key=True)
    start_date = Column(BigInteger, primary_key=True)
    progress = Column(SmallInteger, nullable=True)
    rating = Column(SmallInteger, nullable=True)
