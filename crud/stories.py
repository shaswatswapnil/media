from sqlalchemy.orm import Session
from models import Story
from schemas.stories import StoryCreate

def get_story(db: Session, story_id: int):
    return db.query(Story).filter(Story.id == story_id).first()

def get_stories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Story).offset(skip).limit(limit).all()

def create_story(db: Session, story: StoryCreate, author_id: int):
    db_story = Story(**story.dict(), author_id=author_id)
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story
