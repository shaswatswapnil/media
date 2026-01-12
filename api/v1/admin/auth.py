from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.security import verify_password, create_access_token
from crud import admins as crud_admins
from schemas.admins import Admin
from core.db import get_db

router = APIRouter()

@router.post("/login", summary="Admin login")
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Logs in an admin user.

    - **username**: The admin's email.
    - **password**: The admin's password.
    """
    admin = crud_admins.get_admin_by_email(db, email=form_data.username)
    if not admin or not verify_password(form_data.password, admin.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": admin.email})
    return {"access_token": access_token, "token_type": "bearer"}
