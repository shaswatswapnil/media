
from pydantic import BaseModel
from typing import Optional
from fastapi import Form


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

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        slug: str = Form(...),
        content: str = Form(...),
        author: str = Form(...),
        is_published: bool = Form(False),
        is_featured: bool = Form(False),
    ):
        return cls(
            title=title,
            slug=slug,
            content=content,
            author=author,
            is_published=is_published,
            is_featured=is_featured,
        )


class VideoUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    cover_image: Optional[str] = None
    video_path: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    is_published: Optional[bool] = None
    is_featured: Optional[bool] = None

    @classmethod
    def as_form(
        cls,
        title: Optional[str] = Form(None),
        slug: Optional[str] = Form(None),
        content: Optional[str] = Form(None),
        author: Optional[str] = Form(None),
        is_published: Optional[bool] = Form(None),
        is_featured: Optional[bool] = Form(None),
    ):
        return cls(
            title=title,
            slug=slug,
            content=content,
            author=author,
            is_published=is_published,
            is_featured=is_featured,
        )


class Video(VideoBase):
    id: int

    class Config:
        from_attributes = True
