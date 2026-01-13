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

@router.get("/{slug}", response_model=Story, summary="Get a story by slug")
def read_story(
    slug: str, 
    db: Session = Depends(get_db), 
    current_admin: Admin = Depends(get_current_admin)
):
    """
    Retrieve a single story by its slug.
    """
    db_story = crud_stories.get_story_by_slug(db, slug=slug)
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

@router.put("/{slug}", response_model=Story, summary="Update a story")
def update_story(slug: str, story: StoryCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Update a story by its slug.

    - **slug**: The slug of the story to update.
    """
    db_story = crud_stories.update_story_by_slug(db=db, slug=slug, story=story)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story

@router.delete("/{slug}", response_model=Story, summary="Delete a story")
def delete_story(slug: str, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Delete a story by its slug.

    - **slug**: The slug of the story to delete.
    """
    db_story = crud_stories.delete_story_by_slug(db=db, slug=slug)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story
