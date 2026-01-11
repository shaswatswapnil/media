from pydantic import BaseModel

class VideoBase(BaseModel):
    title: str
    slug: str
    cover_image: str | None = None
    content: str
    author: str
    is_published: bool = False
    is_featured: bool = False

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True
