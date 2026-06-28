from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import shutil
import os

from app.services.pdf_service import extract_text
from app.models.document import DocumentResponse

router = APIRouter()


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload", response_model=DocumentResponse)
async def upload_pdf(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_DIR, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = extract_text(filepath)

    return DocumentResponse(
        filename=file.filename,
        pages=result["pages"],
        extracted_text=result["text"]
    )