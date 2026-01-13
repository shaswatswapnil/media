from sqlalchemy.orm import Session
from models.stories import Story
from schemas.stories import StoryCreate

def get_story(db: Session, story_id: int):
    return db.query(Story).filter(Story.id == story_id).first()

def get_story_by_slug(db: Session, slug: str):
    return db.query(Story).filter(Story.slug == slug).first()

def get_stories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Story).offset(skip).limit(limit).all()

def create_story(db: Session, story: StoryCreate):
    db_story = Story(**story.dict())
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story

def update_story(db: Session, story_id: int, story: StoryCreate):
    db_story = get_story(db, story_id)
    if db_story:
        for key, value in story.dict().items():
            setattr(db_story, key, value)
        db.commit()
        db.refresh(db_story)
    return db_story

def delete_story(db: Session, story_id: int):
    db_story = db.query(Story).filter(Story.id == story_id).first()
    if db_story:
        db.delete(db_story)
        db.commit()
    return db_story
