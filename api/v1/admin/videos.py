from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.videos import Video, VideoCreate
from crud import videos as crud_videos
from core.db import get_db
from api.v1.dependencies import get_current_admin
from models.admins import Admin

router = APIRouter()

@router.get("/", response_model=List[Video], summary="Get all videos")
def read_videos(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db), 
    current_admin: Admin = Depends(get_current_admin)
):
    """
    Retrieve all videos.
    """
    videos = crud_videos.get_videos(db, skip=skip, limit=limit)
    return videos

@router.get("/{slug}", response_model=Video, summary="Get a video by slug")
def read_video(
    slug: str, 
    db: Session = Depends(get_db), 
    current_admin: Admin = Depends(get_current_admin)
):
    """
    Retrieve a single video by its slug.
    """
    db_video = crud_videos.get_video_by_slug(db, slug=slug)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@router.post("/", response_model=Video, summary="Create a new video")
def create_video(video: VideoCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Create a new video.

    - **title**: The title of the video.
    - **url**: The URL of the video.
    """
    return crud_videos.create_video(db=db, video=video)

@router.put("/{slug}", response_model=Video, summary="Update a video")
def update_video(slug: str, video: VideoCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Update a video by its slug.

    - **slug**: The slug of the video to update.
    """
    db_video = crud_videos.update_video_by_slug(db=db, slug=slug, video=video)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@router.delete("/{slug}", response_model=Video, summary="Delete a video")
def delete_video(slug: str, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)):
    """
    Delete a video by its slug.

    - **slug**: The slug of the video to delete.
    """
    db_video = crud_videos.delete_video_by_slug(db=db, slug=slug)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video
