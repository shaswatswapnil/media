from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.stories import Story, StoryCreate
from crud import stories as crud_stories
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin

router = APIRouter()

@router.get("/", response_model=List[Story], summary="Get all stories")
def read_stories(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db), 
    current_admin: Admin = Depends(get_current_admin)
):
    """
    Retrieve all stories.
    """
    stories = crud_stories.get_stories(db, skip=skip, limit=limit)
    return stories

@router.get("/{story_id}", response_model=Story, summary="Get a story by ID")
def read_story(
    story_id: int, 
    db: Session = Depends(get_db), 
    current_admin: Admin = Depends(get_current_admin)
):
    """
    Retrieve a single story by its ID.
    """
    db_story = crud_stories.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story

@router.post("/", response_model=Story, summary="Create a new story")
def create_story(story: StoryCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Create a new story.

    - **title**: The title of the story.
    - **content**: The content of the story.
    """
    return crud_stories.create_story(db=db, story=story)

@router.put("/{story_id}", response_model=Story, summary="Update a story")
def update_story(story_id: int, story: StoryCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Update a story by its ID.

    - **story_id**: The ID of the story to update.
    """
    db_story = crud_stories.update_story(db=db, story_id=story_id, story=story)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story

@router.delete("/{story_id}", response_model=Story, summary="Delete a story")
def delete_story(story_id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Delete a story by its ID.

    - **story_id**: The ID of the story to delete.
    """
    db_story = crud_stories.delete_story(db=db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story
