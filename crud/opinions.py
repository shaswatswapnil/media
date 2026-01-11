from sqlalchemy.orm import Session
from models import Opinion
from schemas.opinions import OpinionCreate

def get_opinion(db: Session, opinion_id: int):
    return db.query(Opinion).filter(Opinion.id == opinion_id).first()

def get_opinions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Opinion).offset(skip).limit(limit).all()

def create_opinion(db: Session, opinion: OpinionCreate, author_id: int):
    db_opinion = Opinion(**opinion.dict(), author_id=author_id)
    db.add(db_opinion)
    db.commit()
    db.refresh(db_opinion)
    return db_opinion
