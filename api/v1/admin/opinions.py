from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.opinions import Opinion, OpinionCreate
from crud import opinions as crud_opinions
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin

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
def create_opinion(opinion: OpinionCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Create a new opinion.

    - **title**: The title of the opinion.
    - **content**: The content of the opinion.
    """
    return crud_opinions.create_opinion(db=db, opinion=opinion)

@router.put("/{slug}", response_model=Opinion, summary="Update an opinion")
def update_opinion(slug: str, opinion: OpinionCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Update an opinion by its slug.

    - **slug**: The slug of the opinion to update.
    """
    db_opinion = crud_opinions.update_opinion_by_slug(db=db, slug=slug, opinion=opinion)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion

@router.delete("/{slug}", response_model=Opinion, summary="Delete an opinion")
def delete_opinion(slug: str, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Delete an opinion by its slug.

    - **slug**: The slug of the opinion to delete.
    """
    db_opinion = crud_opinions.delete_opinion_by_slug(db=db, slug=slug)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion
