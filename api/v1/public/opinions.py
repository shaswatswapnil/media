from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.opinions import Opinion
from crud import opinions as crud_opinions
from core.db import get_db

router = APIRouter()

@router.get("/", response_model=list[Opinion])
def read_opinions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    opinions = crud_opinions.get_opinions(db, skip=skip, limit=limit)
    return opinions

@router.get("/{opinion_id}", response_model=Opinion)
def read_opinion(opinion_id: int, db: Session = Depends(get_db)):
    db_opinion = crud_opinions.get_opinion(db, opinion_id=opinion_id)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion
