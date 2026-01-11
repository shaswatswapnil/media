from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.videos import Video, VideoCreate
from crud import videos as crud_videos
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin

router = APIRouter()

@router.post("/", response_model=Video)
def create_video(video: VideoCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    return crud_videos.create_video(db=db, video=video)

@router.delete("/{video_id}", response_model=Video)
def delete_video(video_id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    db_video = crud_videos.delete_video(db=db, video_id=video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video
