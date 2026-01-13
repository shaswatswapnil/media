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

@router.get("/{slug}", response_model=Video, summary="Read a video by slug")
def read_video_by_slug(slug: str, db: Session = Depends(get_db)):
    """
    Read a video by its slug.

    - **slug**: The slug of the video to return.
    """
    db_video = crud_videos.get_video_by_slug(db, slug=slug)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video
