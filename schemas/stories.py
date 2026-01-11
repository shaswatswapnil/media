from pydantic import BaseModel

class StoryBase(BaseModel):
    title: str
    slug: str
    cover_image: str | None = None
    content: str
    author: str
    is_published: bool = False
    is_featured: bool = False

class StoryCreate(StoryBase):
    pass

class Story(StoryBase):
    id: int

    class Config:
        orm_mode = True
