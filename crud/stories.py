from sqlalchemy.orm import Session
from models import Story
from schemas.stories import StoryCreate

def create_story(db: Session, story: StoryCreate):
    db_story = Story(**story.dict())
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story

def delete_story(db: Session, story_id: int):
    db_story = db.query(Story).filter(Story.id == story_id).first()
    if db_story:
        db.delete(db_story)
        db.commit()
    return db_story
