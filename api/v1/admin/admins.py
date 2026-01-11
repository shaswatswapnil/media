from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.admins import Admin, AdminCreate
from crud import admins as crud_admins
from core.db import get_db

router = APIRouter()

@router.post("/", response_model=Admin)
def create_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud_admins.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_admins.create_admin(db=db, admin=admin)
