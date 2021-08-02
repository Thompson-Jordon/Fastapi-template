from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import test_settings
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(test_settings.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()