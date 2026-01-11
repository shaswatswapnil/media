from sqlalchemy.orm import Session
from models import Video
from schemas.videos import VideoCreate

def get_video(db: Session, video_id: int):
    return db.query(Video).filter(Video.id == video_id).first()

def get_videos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Video).offset(skip).limit(limit).all()

def create_video(db: Session, video: VideoCreate, author_id: int):
    db_video = Video(**video.dict(), author_id=author_id)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video
