
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List, Optional

from schemas.opinions import Opinion, OpinionCreate, OpinionUpdate
from crud import opinions as crud_opinions
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin
from utils.file_uploads import save_upload_file

router = APIRouter()

@router.get("/", response_model=List[Opinion], summary="Get all opinions")
def read_opinions(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db), 
    current_admin: Admin = Depends(get_current_admin)
):
    """
    Retrieve all opinions.
    """
    opinions = crud_opinions.get_opinions(db, skip=skip, limit=limit)
    return opinions

@router.get("/{slug}", response_model=Opinion, summary="Get an opinion by slug")
def read_opinion(
    slug: str, 
    db: Session = Depends(get_db), 
    current_admin: Admin = Depends(get_current_admin)
):
    """
    Retrieve a single opinion by its slug.
    """
    db_opinion = crud_opinions.get_opinion_by_slug(db, slug=slug)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion

@router.post("/", response_model=Opinion, summary="Create a new opinion")
def create_opinion(
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
    Create a new opinion.
    """
    cover_image_path = None
    if cover_image:
        cover_image_path = save_upload_file(cover_image)

    main_photo_path = None
    if main_photo:
        main_photo_path = save_upload_file(main_photo)

    opinion_data = OpinionCreate(
        title=title,
        slug=slug,
        content=content,
        author=author,
        is_published=is_published,
        is_featured=is_featured,
        cover_image=cover_image_path,
        main_photo_path=main_photo_path
    )
    return crud_opinions.create_opinion(db=db, opinion=opinion_data)

@router.put("/{slug}", response_model=Opinion, summary="Update an opinion")
def update_opinion(
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
    Update an opinion by its slug.
    """
    opinion_update_data = {}
    if title is not None:
        opinion_update_data['title'] = title
    if new_slug is not None:
        opinion_update_data['slug'] = new_slug
    if content is not None:
        opinion_update_data['content'] = content
    if author is not None:
        opinion_update_data['author'] = author
    if is_published is not None:
        opinion_update_data['is_published'] = is_published
    if is_featured is not None:
        opinion_update_data['is_featured'] = is_featured

    if cover_image:
        opinion_update_data['cover_image'] = save_upload_file(cover_image)
    if main_photo:
        opinion_update_data['main_photo_path'] = save_upload_file(main_photo)

    opinion_update = OpinionUpdate(**opinion_update_data)

    db_opinion = crud_opinions.update_opinion_by_slug(db=db, slug=slug, opinion=opinion_update)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion

@router.delete("/{slug}", response_model=Opinion, summary="Delete an opinion")
def delete_opinion(slug: str, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Delete an opinion by its slug.
    """
    db_opinion = crud_opinions.delete_opinion_by_slug(db=db, slug=slug)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion
