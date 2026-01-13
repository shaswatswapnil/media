
from pydantic import BaseModel
from typing import Optional

class OpinionBase(BaseModel):
    title: str
    slug: str
    cover_image: Optional[str] = None
    main_photo_path: Optional[str] = None
    content: str
    author: str
    is_published: bool = False
    is_featured: bool = False

class OpinionCreate(OpinionBase):
    pass

class OpinionUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    cover_image: Optional[str] = None
    main_photo_path: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    is_published: Optional[bool] = None
    is_featured: Optional[bool] = None

class Opinion(OpinionBase):
    id: int

    class Config:
        from_attributes = True
