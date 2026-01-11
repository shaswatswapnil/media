from sqlalchemy.orm import Session
from models.admins import Admin
from schemas.admins import AdminCreate
from core.security import get_password_hash

def get_admin_by_email(db: Session, email: str):
    return db.query(Admin).filter(Admin.email == email).first()

def create_admin(db: Session, admin: AdminCreate):
    hashed_password = get_password_hash(admin.password)
    db_admin = Admin(email=admin.email, hashed_password=hashed_password, name=admin.name)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
