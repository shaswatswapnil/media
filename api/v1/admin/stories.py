
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List, Optional

from schemas.stories import Story, StoryCreate, StoryUpdate
from crud import stories as crud_stories
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin
from utils.file_uploads import save_upload_file

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
def create_story(
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
    title: str = Form(...),
    slug: str = Form(...),
    content: str = Form(...),
    author: str = Form(...),
    is_published: bool = Form(False),
    is_featured: bool = Form(False),
    cover_image: Optional[UploadFile] = File(None),
    main_photo: Optional[UploadFile] = File(None)
):
    """
    Create a new story.
    """
    cover_image_path = None
    if cover_image:
        cover_image_path = save_upload_file(cover_image)

    main_photo_path = None
    if main_photo:
        main_photo_path = save_upload_file(main_photo)

    story_data = StoryCreate(
        title=title,
        slug=slug,
        content=content,
        author=author,
        is_published=is_published,
        is_featured=is_featured,
        cover_image=cover_image_path,
        main_photo_path=main_photo_path
    )
    return crud_stories.create_story(db=db, story=story_data)

@router.put("/{slug}", response_model=Story, summary="Update a story")
def update_story(
    slug: str,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin),
    title: Optional[str] = Form(None),
    new_slug: Optional[str] = Form(None),
    content: Optional[str] = Form(None),
    author: Optional[str] = Form(None),
    is_published: Optional[bool] = Form(None),
    is_featured: Optional[bool] = Form(None),
    cover_image: Optional[UploadFile] = File(None),
    main_photo: Optional[UploadFile] = File(None)
):
    """
    Update a story by its slug.
    """
    story_update_data = {}
    if title is not None:
        story_update_data['title'] = title
    if new_slug is not None:
        story_update_data['slug'] = new_slug
    if content is not None:
        story_update_data['content'] = content
    if author is not None:
        story_update_data['author'] = author
    if is_published is not None:
        story_update_data['is_published'] = is_published
    if is_featured is not None:
        story_update_data['is_featured'] = is_featured

    if cover_image:
        story_update_data['cover_image'] = save_upload_file(cover_image)
    if main_photo:
        story_update_data['main_photo_path'] = save_upload_file(main_photo)

    story_update = StoryUpdate(**story_update_data)

    db_story = crud_stories.update_story_by_slug(db=db, slug=slug, story=story_update)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story

@router.delete("/{slug}", response_model=Story, summary="Delete a story")
def delete_story(slug: str, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Delete a story by its slug.
    """
    db_story = crud_stories.delete_story_by_slug(db=db, slug=slug)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story
