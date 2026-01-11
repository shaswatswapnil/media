from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.stories import Story, StoryCreate
from crud import stories as crud_stories
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin

router = APIRouter()

@router.post("/", response_model=Story)
def create_story(story: StoryCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    return crud_stories.create_story(db=db, story=story)

@router.delete("/{story_id}", response_model=Story)
def delete_story(story_id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    db_story = crud_stories.delete_story(db=db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story
