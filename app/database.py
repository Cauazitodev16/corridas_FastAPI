from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from pathlib import Path
from os import getenv
from dotenv import load_dotenv
 
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
 

SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}"
engine_server = create_engine(SERVER_URL)
 
with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}"))
    conn.commit()
 

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"
 

engine = create_engine(SQLALCHEMY_DATABASE_URL)
 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 

Base = declarative_base()
 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()