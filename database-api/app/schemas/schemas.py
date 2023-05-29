from typing import Union, List
from pydantic import BaseModel


class Client(BaseModel):

    client_id: int
    age_group: Union[str, None]
    client_sex: Union[bool, None]

    class Config: 
        orm_mode = True


class Book(BaseModel):
        
    book_id: int
    book_title: str
    book_issue_year: Union[int, None]
    genres: Union[List[str], None]
    authors: Union[List[str], None]

    class Config: 
        orm_mode = True


class Rating(BaseModel):
        
    client_id: int
    book_id: int
    start_date: int
    progress: Union[int, None]
    rating: Union[int, None]

    class Config: 
        orm_mode = True
        

class Message(BaseModel):
    message: str


transaction_responses = {
    200: {"model": Message},
    500: {"model": Message}
}