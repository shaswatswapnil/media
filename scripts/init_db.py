
from sqlalchemy import create_engine
from core.config import settings
from core.db import Base
from models import stories, opinions, videos, admins

def create_tables():
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
