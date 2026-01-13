import os
from sqlalchemy import create_engine
from core.db import Base
from models import admins, opinions, stories, videos # Import all your models here
from core.config import settings

def main():
    print("Initializing database...")
    engine = create_engine(settings.DATABASE_URL)
    
    # This will drop all tables first and then recreate them.
    # This is useful for development but should be used with caution in production.
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
    main()
