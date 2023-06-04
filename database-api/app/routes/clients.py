from app import schemas
from typing import List
from app import app, db
from app.database import models
from app.utils import commit_transaction

tags = ["Clients"]

@app.get("/select_all_clients", tags=tags, response_model=List[schemas.Client])
def select_all_clients(limit: int=None):
    return db.query(models.Client).limit(limit).all()

@app.post("/select_clients_by_ids", tags=tags, response_model=List[schemas.Client])
def select_clients_by_ids(ids: List[int]):
    return db.query(models.Client).filter(models.Client.client_id.in_(ids)).all()

@app.post("/insert_clients", tags=tags, responses=schemas.transaction_responses)
def insert_clients(clients: List[schemas.Client]):
    for client in clients:
        db_client = models.Client(
            client_id=client.client_id,
            client_age=client.client_age,
            client_sex=client.client_sex
        )
        db.add(db_client)
    return commit_transaction()
