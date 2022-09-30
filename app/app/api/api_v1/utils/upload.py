from urllib.request import Request
from app.extensions.utils import list_to_tree
from app.api import deps
from app import models, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi import FastAPI, File, UploadFile
from typing import List
from app.core.config import settings
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
import shutil

router = APIRouter()


@router.post("/files", response_model=schemas.Response)
async def upload_image(file: UploadFile = File(...)):

    save_dir = f"{settings.ASSETS_DIR}/img"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    try:
        suffix = Path(file.filename).suffix

        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_file_name = Path(tmp.name).name
    finally:
        file.file.close()

    return {"code": 20000, "data": {"name": tmp_file_name, "url": f"{settings.ASSETS_URL}/img/{tmp_file_name}"}}
