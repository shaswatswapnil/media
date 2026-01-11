from pydantic import BaseModel

class OpinionBase(BaseModel):
    title: str
    slug: str
    cover_image: str | None = None
    content: str
    author: str
    is_published: bool = False
    is_featured: bool = False

class OpinionCreate(OpinionBase):
    pass

class Opinion(OpinionBase):
    id: int

    class Config:
        from_attributes = True
