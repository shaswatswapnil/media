from sqlalchemy.orm import Session
from models.opinions import Opinion
from schemas.opinions import OpinionCreate

def create_opinion(db: Session, opinion: OpinionCreate):
    db_opinion = Opinion(**opinion.dict())
    db.add(db_opinion)
    db.commit()
    db.refresh(db_opinion)
    return db_opinion

def delete_opinion(db: Session, opinion_id: int):
    db_opinion = db.query(Opinion).filter(Opinion.id == opinion_id).first()
    if db_opinion:
        db.delete(db_opinion)
        db.commit()
    return db_opinion
