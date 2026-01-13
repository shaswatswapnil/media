
from pydantic import BaseModel
from typing import Optional

class VideoBase(BaseModel):
    title: str
    slug: str
    cover_image: Optional[str] = None
    video_path: Optional[str] = None
    content: str
    author: str
    is_published: bool = False
    is_featured: bool = False

class VideoCreate(VideoBase):
    pass

class VideoUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    cover_image: Optional[str] = None
    video_path: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    is_published: Optional[bool] = None
    is_featured: Optional[bool] = None

class Video(VideoBase):
    id: int

    class Config:
        from_attributes = True
