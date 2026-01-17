import os
import shutil
import uuid
from fastapi import UploadFile, HTTPException

BASE_UPLOAD_DIR = "media"


def save_upload_file(file: UploadFile, folder: str = "others") -> str:
    """
    Saves an uploaded file to a specified folder within the BASE_UPLOAD_DIR,
    validates the file type, and returns the file path.
    """
    upload_dir = os.path.join(BASE_UPLOAD_DIR, folder)
    os.makedirs(upload_dir, exist_ok=True)

    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    file_path = os.path.join(upload_dir, filename)

    if folder == "images" and file.content_type not in ["image/png", "image/jpeg", "image/webp"]:
        raise HTTPException(status_code=400, detail="Invalid image type. Only PNG, JPEG, and WEBP are allowed.")

    if folder == "videos" and not file.content_type.startswith("video/"):
        raise HTTPException(status_code=400, detail="Invalid video type.")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
