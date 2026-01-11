from sqlalchemy.orm import Session
from models import Admin
from schemas.admins import AdminCreate
from core.security import get_password_hash

def get_admin(db: Session, admin_id: int):
    return db.query(Admin).filter(Admin.id == admin_id).first()

def get_admin_by_email(db: Session, email: str):
    return db.query(Admin).filter(Admin.email == email).first()

def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Admin).offset(skip).limit(limit).all()

def create_admin(db: Session, admin: AdminCreate):
    hashed_password = get_password_hash(admin.password)
    db_admin = Admin(email=admin.email, password_hash=hashed_password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
