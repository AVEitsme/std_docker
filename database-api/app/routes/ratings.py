from app import schemas
from typing import List
from app import app, db
from app.database import models
from app.utils import commit_transaction

tags = ["Ratings"]

@app.get("/select_all_ratings", tags=tags, response_model=List[schemas.Rating])
def select_all_ratings(limit: int=None):
    return db.query(models.Rating).limit(limit).all()

@app.post("/insert_ratings", tags=tags, responses=schemas.transaction_responses)
def insert_ratings(ratings: List[schemas.Rating]):
    for rating in ratings:
        db_rating = models.Rating(
            client_id=rating.client_id,
            book_id=rating.book_id,
            progress=rating.progress,
            rating=rating.rating,
            start_date=rating.start_date,
        )
        db.add(db_rating)
    return commit_transaction()