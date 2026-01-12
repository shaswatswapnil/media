from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.videos import Video
from crud import videos as crud_videos
from core.db import get_db

router = APIRouter()

@router.get("/", response_model=list[Video], summary="Read all videos")
def read_videos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Read all videos with pagination.

    - **skip**: The number of videos to skip.
    - **limit**: The maximum number of videos to return.
    """
    videos = crud_videos.get_videos(db, skip=skip, limit=limit)
    return videos

@router.get("/{video_id}", response_model=Video, summary="Read a video by ID")
def read_video(video_id: int, db: Session = Depends(get_db)):
    """
    Read a video by its ID.

    - **video_id**: The ID of the video to return.
    """
    db_video = crud_videos.get_video(db, video_id=video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video
