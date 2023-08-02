from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your own database URL
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
SQLITE_DATABASE_URL = "sqlite:///./sqlite_testing.db"

engine = create_engine(
    SQLITE_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()