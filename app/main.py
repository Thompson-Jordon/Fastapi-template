from fastapi import FastAPI
from app.models import Base
from app.db import engine
from app.testdb import engine as test_engine
from fastapi.middleware.cors import CORSMiddleware

from app.routes import example

# Create all tables in the database.
# Comment this out if you using migrations.
Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=test_engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(example.router)

