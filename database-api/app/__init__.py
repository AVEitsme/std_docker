import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import declarative_base
from fastapi.responses import RedirectResponse

engine = create_engine(os.environ["POSTGRES_CONNECTION_STRING"])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()
db = SessionLocal()

# from app.routes import *


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")