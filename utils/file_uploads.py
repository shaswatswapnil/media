
import os
import shutil
from fastapi import UploadFile

UPLOAD_DIR = "media"

def save_upload_file(upload_file: UploadFile) -> str:
    """
    Saves an uploaded file to the UPLOAD_DIR and returns the file path.
    """
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    file_path = os.path.join(UPLOAD_DIR, upload_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return file_path
