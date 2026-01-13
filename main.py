
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.v1.admin import admins as admin_admins, stories as admin_stories, opinions as admin_opinions, videos as admin_videos, auth as admin_auth
from api.v1.public import stories as public_stories, opinions as public_opinions, videos as public_videos

app = FastAPI(
    title="My Personal API",
    description="This is my personal API. It has public endpoints for my stories, opinions, and videos. It also has admin endpoints for me to manage the content.",
    version="1.0.0",
)

# Mount the static directory to serve files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Admin Endpoints
app.include_router(admin_auth.router, prefix="/api/v1/admin/auth", tags=["Admin Authentication"])
app.include_router(admin_admins.router, prefix="/api/v1/admin/admins", tags=["Admin Management"])
app.include_router(admin_stories.router, prefix="/api/v1/admin/stories", tags=["Admin Stories"])
app.include_router(admin_opinions.router, prefix="/api/v1/admin/opinions", tags=["Admin Opinions"])
app.include_router(admin_videos.router, prefix="/api/v1/admin/videos", tags=["Admin Videos"])

# Public Endpoints
app.include_router(public_stories.router, prefix="/api/v1/public/stories", tags=["Public Stories"])
app.include_router(public_opinions.router, prefix="/api/v1/public/opinions", tags=["Public Opinions"])
app.include_router(public_videos.router, prefix="/api/v1/public/videos", tags=["Public Videos"])
