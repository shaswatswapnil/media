from fastapi import FastAPI
from core.db import engine
from models import admins, stories, opinions, videos
from api.v1.admin import admins as admin_admins, stories as admin_stories, opinions as admin_opinions, videos as admin_videos
from api.v1.public import stories as public_stories, opinions as public_opinions, videos as public_videos

admins.Base.metadata.create_all(bind=engine)
stories.Base.metadata.create_all(bind=engine)
opinions.Base.metadata.create_all(bind=engine)
videos.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin_admins.router, prefix="/api/v1/admin/admins", tags=["admin_admins"])
app.include_router(admin_stories.router, prefix="/api/v1/admin/stories", tags=["admin_stories"])
app.include_router(admin_opinions.router, prefix="/api/v1/admin/opinions", tags=["admin_opinions"])
app.include_router(admin_videos.router, prefix="/api/v1/admin/videos", tags=["admin_videos"])

app.include_router(public_stories.router, prefix="/api/v1/public/stories", tags=["public_stories"])
app.include_router(public_opinions.router, prefix="/api/v1/public/opinions", tags=["public_opinions"])
app.include_router(public_videos.router, prefix="/api/v1/public/videos", tags=["public_videos"])
