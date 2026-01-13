from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.opinions import Opinion
from crud import opinions as crud_opinions
from core.db import get_db

router = APIRouter()

@router.get("/", response_model=list[Opinion], summary="Read all opinions")
def read_opinions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Read all opinions with pagination.

    - **skip**: The number of opinions to skip.
    - **limit**: The maximum number of opinions to return.
    """
    opinions = crud_opinions.get_opinions(db, skip=skip, limit=limit)
    return opinions

@router.get("/{slug}", response_model=Opinion, summary="Read an opinion by slug")
def read_opinion_by_slug(slug: str, db: Session = Depends(get_db)):
    """
    Read an opinion by its slug.

    - **slug**: The slug of the opinion to return.
    """
    db_opinion = crud_opinions.get_opinion_by_slug(db, slug=slug)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion
