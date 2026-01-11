
from pydantic import BaseModel

class Admin(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True
