from sqlalchemy.orm import Session
from models import Video
from schemas.videos import VideoCreate

def create_video(db: Session, video: VideoCreate):
    db_video = Video(**video.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def delete_video(db: Session, video_id: int):
    db_video = db.query(Video).filter(Video.id == video_id).first()
    if db_video:
        db.delete(db_video)
        db.commit()
    return db_video
