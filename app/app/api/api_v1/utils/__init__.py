from fastapi import APIRouter
from app.api.api_v1.utils import upload

router = APIRouter()
router.include_router(upload.router, prefix="/upload", tags=["uplaod"])
