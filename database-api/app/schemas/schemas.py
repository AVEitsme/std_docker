from typing import Union, List
from pydantic import BaseModel


class OrmBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Client(OrmBaseModel):
    client_id: int
    client_age: Union[int, None]
    client_sex: Union[bool, None]

    class Config:
        orm_mode = True


class Genre(OrmBaseModel):
    genre_id: int
    genre_name: str

    class Config:
        orm_mode = True


class Author(OrmBaseModel):
    author_id: int
    author_name: str

    class Config:
        orm_mode = True


class Book(OrmBaseModel):
    book_id: int
    book_title: str
    book_issue_year: Union[int, None]
    genres: Union[List[Genre], None]
    authors: Union[List[Author], None]

    class Config:
        orm_mode = True


class Rating(OrmBaseModel):
    client_id: int
    book_id: int
    start_date: int
    progress: Union[int, None]
    rating: Union[int, None]

    class Config:
        orm_mode = True


class Message(OrmBaseModel):
    message: str


transaction_responses = {200: {"model": Message}, 500: {"model": Message}}
