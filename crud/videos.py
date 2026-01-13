
from sqlalchemy.orm import Session
from models.videos import Video
from schemas.videos import VideoCreate, VideoUpdate

def get_video(db: Session, video_id: int):
    return db.query(Video).filter(Video.id == video_id).first()

def get_video_by_slug(db: Session, slug: str):
    return db.query(Video).filter(Video.slug == slug).first()

def get_videos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Video).offset(skip).limit(limit).all()

def create_video(db: Session, video: VideoCreate):
    db_video = Video(**video.model_dump())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def update_video_by_slug(db: Session, slug: str, video: VideoUpdate):
    db_video = get_video_by_slug(db, slug)
    if db_video:
        update_data = video.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_video, key, value)
        db.commit()
        db.refresh(db_video)
    return db_video

def delete_video_by_slug(db: Session, slug: str):
    db_video = db.query(Video).filter(Video.slug == slug).first()
    if db_video:
        db.delete(db_video)
        db.commit()
    return db_video
