import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{user}:{password}@{url}:{port}/{name}".format(
    user=os.getenv('DATABASE_USER'), 
    password=os.getenv('DATABASE_PASSWORD'),
    url=os.getenv('DATABASE_URL'),
    port=os.getenv('DATABASE_PORT'),
    name=os.getenv('DATABASE_NAME')
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
