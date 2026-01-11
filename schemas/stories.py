
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .admins import Admin

class StoryBase(BaseModel):
    title: str
    slug: str
    cover_image: Optional[str] = None
    content: Optional[str] = None
    is_published: bool = False
    is_featured: bool = False

class StoryCreate(StoryBase):
    pass

class Story(StoryBase):
    id: int
    author: Admin
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
