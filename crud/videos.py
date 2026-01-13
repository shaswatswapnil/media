from sqlalchemy.orm import Session
from models.videos import Video
from schemas.videos import VideoCreate

def get_video(db: Session, video_id: int):
    return db.query(Video).filter(Video.id == video_id).first()

def get_video_by_slug(db: Session, slug: str):
    return db.query(Video).filter(Video.slug == slug).first()

def get_videos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Video).offset(skip).limit(limit).all()

def create_video(db: Session, video: VideoCreate):
    db_video = Video(**video.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def update_video(db: Session, video_id: int, video: VideoCreate):
    db_video = get_video(db, video_id)
    if db_video:
        for key, value in video.dict().items():
            setattr(db_video, key, value)
        db.commit()
        db.refresh(db_video)
    return db_video

def delete_video(db: Session, video_id: int):
    db_video = db.query(Video).filter(Video.id == video_id).first()
    if db_video:
        db.delete(db_video)
        db.commit()
    return db_video
