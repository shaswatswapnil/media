from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.opinions import Opinion, OpinionCreate
from crud import opinions as crud_opinions
from core.db import get_db
from models import Admin
from api.v1.admin.auth import get_current_admin

router = APIRouter()

@router.post("/", response_model=Opinion)
def create_opinion(opinion: OpinionCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    return crud_opinions.create_opinion(db=db, opinion=opinion, author_id=current_admin.id)

@router.get("/", response_model=list[Opinion])
def read_opinions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    opinions = crud_opinions.get_opinions(db, skip=skip, limit=limit)
    return opinions

@router.get("/{opinion_id}", response_model=Opinion)
def read_opinion(opinion_id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    db_opinion = crud_opinions.get_opinion(db, opinion_id=opinion_id)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion
