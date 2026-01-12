from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.stories import Story
from crud import stories as crud_stories
from core.db import get_db

router = APIRouter()

@router.get("/", response_model=list[Story], summary="Read all stories")
def read_stories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Read all stories with pagination.

    - **skip**: The number of stories to skip.
    - **limit**: The maximum number of stories to return.
    """
    stories = crud_stories.get_stories(db, skip=skip, limit=limit)
    return stories

@router.get("/{story_id}", response_model=Story, summary="Read a story by ID")
def read_story(story_id: int, db: Session = Depends(get_db)):
    """
    Read a story by its ID.

    - **story_id**: The ID of the story to return.
    """
    db_story = crud_stories.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story
