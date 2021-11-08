from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .config import settings 
from sqlalchemy.orm import sessionmaker
#import pymysql
#import time


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""while True:
    try:
        conn = pymysql.connect(host='localhost', database='pstore_api', user='makispal', password='makis6948910080')
        cursor = conn.cursor()
        print("Connect to Database Successfuly!!")
        break
    except Exception as error:
        print("Database Connection Failure!")
        print(error)
        time.sleep(2)"""