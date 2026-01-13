from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.videos import Video, VideoCreate
from crud import videos as crud_videos
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin

router = APIRouter()

@router.post("/", response_model=Video, summary="Create a new video")
def create_video(video: VideoCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Create a new video.

    - **title**: The title of the video.
    - **url**: The URL of the video.
    """
    return crud_videos.create_video(db=db, video=video)

@router.delete("/{video_id}", response_model=Video, summary="Delete a video")
def delete_video(video_id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Delete a video by its ID.

    - **video_id**: The ID of the video to delete.
    """
    db_video = crud_videos.delete_video(db=db, video_id=video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video
