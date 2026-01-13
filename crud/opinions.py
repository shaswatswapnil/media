from sqlalchemy.orm import Session
from models.opinions import Opinion
from schemas.opinions import OpinionCreate

def get_opinion(db: Session, opinion_id: int):
    return db.query(Opinion).filter(Opinion.id == opinion_id).first()

def get_opinion_by_slug(db: Session, slug: str):
    return db.query(Opinion).filter(Opinion.slug == slug).first()

def get_opinions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Opinion).offset(skip).limit(limit).all()

def create_opinion(db: Session, opinion: OpinionCreate):
    db_opinion = Opinion(**opinion.dict())
    db.add(db_opinion)
    db.commit()
    db.refresh(db_opinion)
    return db_opinion

def update_opinion_by_slug(db: Session, slug: str, opinion: OpinionCreate):
    db_opinion = get_opinion_by_slug(db, slug)
    if db_opinion:
        for key, value in opinion.dict().items():
            setattr(db_opinion, key, value)
        db.commit()
        db.refresh(db_opinion)
    return db_opinion

def delete_opinion_by_slug(db: Session, slug: str):
    db_opinion = db.query(Opinion).filter(Opinion.slug == slug).first()
    if db_opinion:
        db.delete(db_opinion)
        db.commit()
    return db_opinion
