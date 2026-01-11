from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.admins import AdminCreate, Admin, Token
from crud import admins as crud_admins
from core.db import get_db
from core.security import create_access_token, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

router = APIRouter()

@router.post("/", response_model=Admin)
def create_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud_admins.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_admins.create_admin(db=db, admin=admin)

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    admin = crud_admins.get_admin_by_email(db, email=form_data.username)
    if not admin or not verify_password(form_data.password, admin.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": admin.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
