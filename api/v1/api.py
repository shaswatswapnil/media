from fastapi import APIRouter
from api.v1.admin import stories, opinions, videos, admins

api_router = APIRouter()

api_router.include_router(admins.router, prefix="/admins", tags=["admins"])
api_router.include_router(stories.router, prefix="/stories", tags=["stories"])
api_router.include_router(opinions.router, prefix="/opinions", tags=["opinions"])
api_router.include_router(videos.router, prefix="/videos", tags=["videos"])
