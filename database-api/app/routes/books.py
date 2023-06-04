from app import schemas
from typing import List
from app import app, db
from app.database import models
from app.utils import commit_transaction

tags = ["Books"]

@app.get("/select_all_books", tags=tags, response_model=List[schemas.Book])
def select_all_books(limit: int=None): 
    return db.query(models.Book).limit(limit).all() 

@app.post("/select_books_by_ids", tags=tags, response_model=List[schemas.Book])
def select_books_by_ids(ids: List[int]):
    return db.query(models.Book).filter(models.Book.book_id.in_(ids)).all()

@app.post("/insert_books", tags=tags, responses=schemas.transaction_responses)
def insert_books(books: List[schemas.Book]):
    for book in books:
        db_book = models.Book(
            book_id=book.book_id,
            book_title=book.book_title, 
            book_issue_year=book.book_issue_year,
            genres=[
                models.Genre(genre_id=genre.genre_id, genre_name=genre.genre_name) for genre in book.genres
            ],
            authors=[
                models.Author(author_id=author.author_id, author_name=author.author_name) for author in book.authors
            ]
        )
        db.add(db_book)
    return commit_transaction()