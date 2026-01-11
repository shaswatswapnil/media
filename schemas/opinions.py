
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .admins import Admin

class OpinionBase(BaseModel):
    title: str
    slug: str
    cover_image: Optional[str] = None
    content: Optional[str] = None
    is_published: bool = False
    is_featured: bool = False

class OpinionCreate(OpinionBase):
    pass

class Opinion(OpinionBase):
    id: int
    author: Admin
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
