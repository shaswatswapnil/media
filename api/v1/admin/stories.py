from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.stories import Story, StoryCreate
from crud import stories as crud_stories
from core.db import get_db
from models import Admin
from api.v1.admin.auth import get_current_admin

router = APIRouter()

@router.post("/", response_model=Story)
def create_story(story: StoryCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    return crud_stories.create_story(db=db, story=story, author_id=current_admin.id)

@router.get("/", response_model=list[Story])
def read_stories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    stories = crud_stories.get_stories(db, skip=skip, limit=limit)
    return stories

@router.get("/{story_id}", response_model=Story)
def read_story(story_id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    db_story = crud_stories.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story
