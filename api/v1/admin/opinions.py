from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.opinions import Opinion, OpinionCreate
from crud import opinions as crud_opinions
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin

router = APIRouter()

@router.post("/", response_model=Opinion)
def create_opinion(opinion: OpinionCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    return crud_opinions.create_opinion(db=db, opinion=opinion)

@router.delete("/{opinion_id}", response_model=Opinion)
def delete_opinion(opinion_id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    db_opinion = crud_opinions.delete_opinion(db=db, opinion_id=opinion_id)
    if db_opinion is None:
        raise HTTPException(status_code=404, detail="Opinion not found")
    return db_opinion
