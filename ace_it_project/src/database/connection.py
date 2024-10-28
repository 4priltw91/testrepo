from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# 환경 변수에서 DATABASE_URL 가져오기
DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True)

SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()

